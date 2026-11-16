#!/usr/bin/env python3
"""Genera el plugin de WordPress «SeñalVal · Entradas del blog» con las entradas de posts_*.py.

Uso:  python3 tools/blog/build_plugin.py [--sin-comprobar]
Salida: wordpress/plugin/senalval-blog-entradas.zip
Comprueba (salvo --sin-comprobar) que cada imagen y cada enlace interno responden en senalval.es.
"""
import base64, html, json, pathlib, re, subprocess, sys, zipfile
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from posts_1 import POSTS as P1
from posts_2 import POSTS as P2
from posts_3 import POSTS as P3
from faqs import FAQS

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'wordpress' / 'plugin'; OUT.mkdir(parents=True, exist_ok=True)
SITE = 'https://senalval.es'
UP = SITE + '/wp-content/uploads/'
POSTS = P1 + P2 + P3
for _p in POSTS:  # preguntas frecuentes antes del párrafo final
    q = FAQS[_p['slug']]
    faq = '\n## Preguntas frecuentes\n' + '\n'.join(f'### {a}\n{b}' for a, b in q) + '\n'
    body = _p['body'].rstrip()
    i = body.rfind('\n> ')
    _p['body'] = body[:i] + '\n' + faq + body[i:] + '\n'
assert set(FAQS) == {p['slug'] for p in POSTS}, 'faltan o sobran FAQ'
CHECK = '--sin-comprobar' not in sys.argv

slugs = [p['slug'] for p in POSTS]
assert len(slugs) == len(set(slugs)), 'slugs repetidos'

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    def link(m):
        txt, href = m.group(1), m.group(2)
        if href.startswith('/'): href = SITE + href
        return f'<a href="{href}">{txt}</a>'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, s)

def to_blocks(p):
    out, lst = [], []
    def flush():
        if lst:
            items = ''.join(f'<!-- wp:list-item --><li>{x}</li><!-- /wp:list-item -->' for x in lst)
            out.append(f'<!-- wp:list --><ul class="wp-block-list">{items}</ul><!-- /wp:list -->')
            lst.clear()
    for raw in p['body'].strip().splitlines():
        line = raw.strip()
        if not line: flush(); continue
        if line.startswith('- '): lst.append(inline(line[2:])); continue
        flush()
        if line.startswith('### '):
            out.append(f'<!-- wp:heading {{"level":3}} --><h3 class="wp-block-heading">{inline(line[4:])}</h3><!-- /wp:heading -->')
        elif line.startswith('## '):
            out.append(f'<!-- wp:heading --><h2 class="wp-block-heading">{inline(line[3:])}</h2><!-- /wp:heading -->')
        elif line == '[[IMG2]]':
            alt = html.escape(p['img2_alt'])
            out.append(f'<!-- wp:image {{"sizeSlug":"large"}} --><figure class="wp-block-image size-large"><img src="{UP}{p["img2"]}" alt="{alt}"/><figcaption class="wp-element-caption">{alt}. Proyecto SeñalVal.</figcaption></figure><!-- /wp:image -->')
        elif line.startswith('> '):
            out.append(f'<!-- wp:paragraph {{"className":"senalval-cta"}} --><p class="senalval-cta"><strong>{inline(line[2:])}</strong></p><!-- /wp:paragraph -->')
        else:
            out.append(f'<!-- wp:paragraph --><p>{inline(line)}</p><!-- /wp:paragraph -->')
    flush()
    out.append('<!-- wp:paragraph --><p>SeñalVal · Calle Oro 34, 1º F (Valladolid) · <a href="tel:+34665863597">665 863 597</a> · '
               '<a href="mailto:luismi.olea@senalval.es">luismi.olea@senalval.es</a> · <a href="https://senalval.es/#contacto">Pedir presupuesto</a></p><!-- /wp:paragraph -->')
    return '\n'.join(out)

# ---------- Comprobaciones ----------
def code(u):
    r = subprocess.run(['curl', '-sS', '-m', '25', '-o', '/dev/null', '-w', '%{http_code}', '-L', u], capture_output=True, text=True)
    return r.stdout.strip()
words = {}
for p in POSTS:
    words[p['slug']] = len(re.findall(r'\w+', re.sub(r'\]\([^)]*\)', '', p['body'])))
    assert len(p['metadesc']) <= 160, ('metadesc larga', p['slug'], len(p['metadesc']))
    assert len(p['seo_title']) <= 65, ('título largo', p['slug'], len(p['seo_title']))
    assert '[[IMG2]]' in p['body'], p['slug']
if CHECK:
    bad = []
    imgs = sorted({p['img'] for p in POSTS} | {p['img2'] for p in POSTS})
    for i in imgs:
        c = code(UP + i)
        if c != '200': bad.append(('img', c, i))
    links = sorted({m for p in POSTS for m in re.findall(r'\]\((/[^)]*)\)', p['body'])})
    for l in links:
        if l.strip('/').split('/')[-1] in slugs: continue
        c = code(SITE + l)
        if c != '200': bad.append(('enlace', c, l))
    print(f'Comprobadas {len(imgs)} imágenes y {len(links)} enlaces internos')
    for b in bad: print('  ✗', *b)
    assert not bad, 'hay imágenes o enlaces rotos'

data = [dict(slug=p['slug'], title=p['title'], content=to_blocks(p), excerpt=p['excerpt'], cats=p['cats'], tags=p['tags'],
             img=UP + p['img'], seo_title=p['seo_title'], metadesc=p['metadesc'], focus=p['focus']) for p in POSTS]
payload = base64.b64encode(json.dumps(data, ensure_ascii=False).encode('utf-8')).decode('ascii')

PHP = r'''<?php
/**
 * Plugin Name: SeñalVal · Entradas del blog
 * Description: Crea __N__ entradas de blog optimizadas para SEO (señalética en Valladolid, Madrid, Burgos, Castilla y León, sectores y normativa) con imágenes de la biblioteca de medios. Herramientas → Entradas SeñalVal.
 * Version: 1.0.0
 * Author: SeñalVal
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Text Domain: senalval-blog
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

function senalval_blog_data() {
	static $data = null;
	if ( null === $data ) {
		$data = json_decode( base64_decode( '__DATA__' ), true );
	}
	return $data;
}

function senalval_blog_existing( $slug ) {
	$q = get_posts( array( 'name' => $slug, 'post_type' => 'post', 'post_status' => array( 'publish', 'future', 'draft', 'pending', 'private' ), 'numberposts' => 1 ) );
	return $q ? $q[0] : null;
}

function senalval_blog_term_ids( $slugs ) {
	$ids = array();
	foreach ( $slugs as $slug ) {
		$term = get_category_by_slug( $slug );
		if ( ! $term ) {
			$name = ucfirst( str_replace( '-', ' ', $slug ) );
			$new  = wp_insert_term( $name, 'category', array( 'slug' => $slug ) );
			if ( ! is_wp_error( $new ) ) { $ids[] = (int) $new['term_id']; }
		} else {
			$ids[] = (int) $term->term_id;
		}
	}
	return $ids;
}

function senalval_blog_attachment_id( $url ) {
	$id = attachment_url_to_postid( $url );
	if ( ! $id ) { // por si la imagen original se guardó como -scaled
		$id = attachment_url_to_postid( preg_replace( '/\.(jpe?g|png)$/i', '-scaled.$1', $url ) );
	}
	return (int) $id;
}

add_action( 'admin_menu', function () {
	add_management_page( 'Entradas SeñalVal', 'Entradas SeñalVal', 'publish_posts', 'senalval-blog', 'senalval_blog_page' );
} );

function senalval_blog_run( $mode, $days, $hour ) {
	$created = 0; $skipped = 0; $n = 0;
	$tz   = wp_timezone();
	$base = new DateTime( 'now', $tz );
	foreach ( senalval_blog_data() as $p ) {
		if ( senalval_blog_existing( $p['slug'] ) ) { $skipped++; continue; }
		$post = array(
			'post_type'    => 'post',
			'post_name'    => $p['slug'],
			'post_title'   => $p['title'],
			'post_content' => $p['content'],
			'post_excerpt' => $p['excerpt'],
			'post_category'=> senalval_blog_term_ids( $p['cats'] ),
			'tags_input'   => $p['tags'],
			'post_author'  => get_current_user_id(),
			'post_status'  => 'draft',
		);
		if ( 'publish' === $mode ) {
			$post['post_status'] = 'publish';
		} elseif ( 'schedule' === $mode ) {
			$d = clone $base;
			$d->modify( '+' . ( $n * $days + 1 ) . ' days' );
			$d->setTime( $hour, 15 );
			$post['post_status']   = 'future';
			$post['post_date']     = $d->format( 'Y-m-d H:i:s' );
			$post['post_date_gmt'] = get_gmt_from_date( $post['post_date'] );
		}
		$id = wp_insert_post( wp_slash( $post ), true );
		if ( is_wp_error( $id ) ) { continue; }
		$att = senalval_blog_attachment_id( $p['img'] );
		if ( $att ) { set_post_thumbnail( $id, $att ); }
		update_post_meta( $id, '_yoast_wpseo_title', $p['seo_title'] );
		update_post_meta( $id, '_yoast_wpseo_metadesc', $p['metadesc'] );
		update_post_meta( $id, '_yoast_wpseo_focuskw', $p['focus'] );
		update_post_meta( $id, 'rank_math_title', $p['seo_title'] );
		update_post_meta( $id, 'rank_math_description', $p['metadesc'] );
		update_post_meta( $id, 'rank_math_focus_keyword', $p['focus'] );
		update_post_meta( $id, '_senalval_blog_pack', '1' );
		$created++; $n++;
	}
	return array( $created, $skipped );
}

function senalval_blog_page() {
	if ( ! current_user_can( 'publish_posts' ) ) { return; }
	$msg = '';
	if ( isset( $_POST['senalval_blog_nonce'] ) && wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['senalval_blog_nonce'] ) ), 'senalval_blog' ) ) {
		if ( isset( $_POST['crear'] ) ) {
			$mode = in_array( $_POST['modo'] ?? '', array( 'publish', 'schedule', 'draft' ), true ) ? $_POST['modo'] : 'schedule';
			$days = max( 1, min( 14, (int) ( $_POST['dias'] ?? 2 ) ) );
			$hour = max( 0, min( 23, (int) ( $_POST['hora'] ?? 9 ) ) );
			list( $c, $s ) = senalval_blog_run( $mode, $days, $hour );
			$msg = sprintf( 'Entradas creadas: %d. Ya existían (no se han tocado): %d.', $c, $s );
		} elseif ( isset( $_POST['borrar'] ) ) {
			$ids = get_posts( array( 'post_type' => 'post', 'post_status' => 'any', 'meta_key' => '_senalval_blog_pack', 'meta_value' => '1', 'numberposts' => -1, 'fields' => 'ids' ) );
			foreach ( $ids as $id ) { wp_trash_post( $id ); }
			$msg = sprintf( 'Entradas movidas a la papelera: %d.', count( $ids ) );
		}
	}
	$data = senalval_blog_data();
	echo '<div class="wrap"><h1>Entradas del blog SeñalVal</h1>';
	if ( $msg ) { echo '<div class="notice notice-success"><p>' . esc_html( $msg ) . '</p></div>'; }
	echo '<p>Este plugin crea <strong>' . count( $data ) . ' entradas</strong> con texto, categorías, etiquetas, imagen destacada de su biblioteca de medios y título y descripción para Yoast SEO. Las entradas que ya existan (mismo slug) no se tocan.</p>';
	echo '<form method="post">';
	wp_nonce_field( 'senalval_blog', 'senalval_blog_nonce' );
	echo '<table class="form-table"><tr><th>Cómo publicarlas</th><td>';
	echo '<label><input type="radio" name="modo" value="schedule" checked> <strong>Programar</strong> (recomendado): una entrada cada <input type="number" name="dias" value="2" min="1" max="14" style="width:60px"> días a las <input type="number" name="hora" value="9" min="0" max="23" style="width:60px"> h</label><br>';
	echo '<label><input type="radio" name="modo" value="publish"> Publicar todas ahora</label><br>';
	echo '<label><input type="radio" name="modo" value="draft"> Crear como borradores para revisarlas antes</label>';
	echo '</td></tr></table>';
	submit_button( 'Crear las entradas', 'primary', 'crear' );
	echo '</form>';
	echo '<h2>Entradas incluidas</h2><table class="widefat striped"><thead><tr><th>#</th><th>Título</th><th>Palabra clave</th><th>Estado</th></tr></thead><tbody>';
	foreach ( $data as $i => $p ) {
		$e = senalval_blog_existing( $p['slug'] );
		$st = $e ? '<a href="' . esc_url( get_edit_post_link( $e->ID ) ) . '">' . esc_html( $e->post_status ) . '</a>' : '—';
		echo '<tr><td>' . ( $i + 1 ) . '</td><td>' . esc_html( $p['title'] ) . '</td><td>' . esc_html( $p['focus'] ) . '</td><td>' . $st . '</td></tr>';
	}
	echo '</tbody></table>';
	echo '<form method="post" style="margin-top:24px" onsubmit="return confirm(\'¿Mover a la papelera todas las entradas creadas por este plugin?\')">';
	wp_nonce_field( 'senalval_blog', 'senalval_blog_nonce' );
	submit_button( 'Mover a la papelera las entradas creadas por el plugin', 'delete', 'borrar' );
	echo '</form></div>';
}
'''.replace('__DATA__', payload).replace('__N__', str(len(data)))

plug = OUT / 'senalval-blog-entradas'
plug.mkdir(exist_ok=True)
(plug / 'senalval-blog-entradas.php').write_text(PHP, encoding='utf-8')
(plug / 'readme.txt').write_text(f'''=== SeñalVal · Entradas del blog ===
Crea {len(data)} entradas de blog. Instalar: Plugins > Añadir nuevo > Subir plugin > elegir el .zip > Activar.
Usar: Herramientas > Entradas SeñalVal > elegir cómo publicarlas > «Crear las entradas».
Cuando estén creadas, el plugin se puede desactivar y borrar: las entradas se quedan.
''', encoding='utf-8')
z = OUT / 'senalval-blog-entradas.zip'
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as f:
    for x in plug.iterdir(): f.write(x, f'senalval-blog-entradas/{x.name}')
# Vista previa legible de todas las entradas
prev = ['<!doctype html><meta charset="utf-8"><title>Entradas SeñalVal</title><style>body{font:16px/1.6 system-ui;max-width:820px;margin:40px auto;padding:0 16px}img{max-width:100%}h1{border-top:4px solid #0B5CAD;padding-top:30px;margin-top:60px}.m{color:#5B6475;font-size:14px}</style>']
for i, p in enumerate(data, 1):
    prev.append(f'<h1>{i}. {html.escape(p["title"])}</h1><p class="m">/{p["slug"]} · Palabra clave: <b>{html.escape(p["focus"])}</b> · Categorías: {", ".join(p["cats"])} · {words[p["slug"]]} palabras<br>SEO: {html.escape(p["seo_title"])}<br>{html.escape(p["metadesc"])}</p><img src="{p["img"]}">' + p['content'])
(OUT / 'vista-previa-entradas.html').write_text('\n'.join(prev), encoding='utf-8')
print(f'{len(data)} entradas · palabras: mín {min(words.values())}, media {sum(words.values())//len(words)}, máx {max(words.values())}')
print('->', z.relative_to(ROOT), round(z.stat().st_size / 1024), 'KB')
