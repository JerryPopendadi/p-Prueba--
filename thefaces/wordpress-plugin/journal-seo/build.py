"""Builds the small WordPress plugin that adds the 5 SEO articles to the THE FACES Journal."""
import json
import os
import re
import shutil
import subprocess

from articles import ARTICLES
from articles2 import ARTICLES2, related, R_MASS, R_FACIAL, R_LYMPH, R_UBUD, R_HEAD, R_FACE, R_SANUR, R_COUPLE

LINKS1 = {
    'best-spa-in-ubud-guide': (R_MASS, R_FACE, R_HEAD, R_COUPLE),
    'head-spa-bali-guide': (('shirodhara-bali-ayurveda', 'Shirodhara in Bali: the Ayurvedic oil ritual'), R_MASS, R_UBUD, R_SANUR),
    'face-massage-bali-guide': (R_FACIAL, R_LYMPH, R_HEAD, R_UBUD),
    'spa-in-sanur-guide': (('things-to-do-in-sanur', 'Things to do in Sanur: a slow guide'), R_COUPLE, R_LYMPH, R_FACE),
    'couples-spa-bali-honeymoon': (R_UBUD, R_SANUR, ('things-to-do-in-sanur', 'Things to do in Sanur'), R_MASS),
}
for _a in ARTICLES:
    _a['html'] = _a['html'] + related(*LINKS1[_a['slug']])
from extra2 import EXTRA2
for _a in ARTICLES2:
    if _a['slug'] in EXTRA2:
        _i = _a['html'].find('<h2>Book')
        _a['html'] = _a['html'][:_i] + EXTRA2[_a['slug']].strip() + '\n\n' + _a['html'][_i:]
ARTICLES = ARTICLES + ARTICLES2

H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(H, '..', 'thefaces-journal-seo')

data = []
for a in ARTICLES:
    html = re.sub(r'\n{2,}', '\n', a['html'].strip())
    words = len(re.sub(r'<[^>]+>', ' ', html).split())
    print(a['slug'], words, 'words')
    data.append(dict(slug=a['slug'], title=a['title'], excerpt=a['excerpt'], html=html, catkey=a['catkey'], cat=a['cat'],
                     img=a['img'], seo_title=a['seo_title'], metadesc=a['metadesc'], faq=a['faq']))

blob = json.dumps(data, ensure_ascii=False)
assert 'TFJSON' not in blob

php = r"""<?php
/**
 * Plugin Name: THE FACES · Journal SEO articles
 * Description: Adds 13 long SEO articles (English) to the THE FACES Journal (spa Ubud, massage Ubud, Balinese massage, head spa, Shirodhara, face massage, facial, lymphatic drainage, reflexology, men's spa, spa Sanur, things to do in Sanur, couples spa). Activate once: the articles are created as normal posts (they stay if you deactivate the plugin). Also prints FAQ structured data for them.
 * Version:     1.1.0
 * Author:      THE FACES
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tf_jseo_data() {
	static $d = null;
	if ( null === $d ) {
		$d = json_decode( <<<'TFJSON'
""" + blob + r"""
TFJSON
		, true );
	}
	return is_array( $d ) ? $d : array();
}

/** Create the articles (once; existing slugs are left untouched). */
function tf_jseo_install() {
	$created = 0;
	$i       = 0;
	foreach ( tf_jseo_data() as $a ) {
		$i++;
		if ( get_page_by_path( $a['slug'], OBJECT, 'post' ) ) {
			continue;
		}
		$id = wp_insert_post(
			array(
				'post_type'    => 'post',
				'post_status'  => 'publish',
				'post_title'   => $a['title'],
				'post_name'    => $a['slug'],
				'post_excerpt' => $a['excerpt'],
				'post_content' => $a['html'],
				'post_date'    => gmdate( 'Y-m-d H:i:s', time() - ( 20 - $i ) * HOUR_IN_SECONDS ),
			)
		);
		if ( is_wp_error( $id ) || ! $id ) {
			continue;
		}
		update_post_meta( $id, '_tf_lang', 'en' );
		update_post_meta( $id, '_tf_img', $a['img'] );
		update_post_meta( $id, '_tf_cat', $a['cat'] );
		update_post_meta( $id, '_tf_catkey', $a['catkey'] );
		update_post_meta( $id, '_tf_jseo', $a['slug'] );
		update_post_meta( $id, '_wp_page_template', 'thefaces-canvas' );
		update_post_meta( $id, '_yoast_wpseo_title', $a['seo_title'] );
		update_post_meta( $id, '_yoast_wpseo_metadesc', $a['metadesc'] );
		$term = get_term_by( 'slug', $a['catkey'], 'category' );
		if ( $term ) {
			wp_set_post_categories( $id, array( $term->term_id ), false );
		}
		$created++;
	}
	update_option( 'tf_jseo_created', $created, false );
	delete_transient( 'tf_seo_canonical_ids' );
}
register_activation_hook( __FILE__, 'tf_jseo_install' );

/** After replacing the plugin with a newer zip, add the new articles too. */
function tf_jseo_maybe_upgrade() {
	if ( '1.1.0' !== get_option( 'tf_jseo_ver' ) && current_user_can( 'manage_options' ) ) {
		tf_jseo_install();
		update_option( 'tf_jseo_ver', '1.1.0', false );
	}
}
add_action( 'admin_init', 'tf_jseo_maybe_upgrade' );

/** FAQ structured data (FAQPage) on each article. */
function tf_jseo_faq_schema() {
	if ( ! is_singular( 'post' ) ) {
		return;
	}
	$slug = get_post_meta( get_queried_object_id(), '_tf_jseo', true );
	if ( ! $slug ) {
		return;
	}
	foreach ( tf_jseo_data() as $a ) {
		if ( $a['slug'] !== $slug || empty( $a['faq'] ) ) {
			continue;
		}
		$items = array();
		foreach ( $a['faq'] as $qa ) {
			$items[] = array(
				'@type'          => 'Question',
				'name'           => $qa[0],
				'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $qa[1] ),
			);
		}
		echo '<script type="application/ld+json">' . wp_json_encode( array( '@context' => 'https://schema.org', '@type' => 'FAQPage', 'mainEntity' => $items ) ) . '</script>' . "\n";
	}
}
add_action( 'wp_head', 'tf_jseo_faq_schema', 30 );

/** Visible FAQ block at the end of each article. */
function tf_jseo_faq_html( $content ) {
	if ( ! is_singular( 'post' ) || ! in_the_loop() && ! doing_filter( 'the_content' ) ) {
		return $content;
	}
	$slug = get_post_meta( get_the_ID(), '_tf_jseo', true );
	if ( ! $slug || false !== strpos( $content, 'tf-jseo-faq' ) ) {
		return $content;
	}
	foreach ( tf_jseo_data() as $a ) {
		if ( $a['slug'] === $slug && ! empty( $a['faq'] ) ) {
			$out = '<h2 class="tf-jseo-faq">Frequently asked questions</h2>';
			foreach ( $a['faq'] as $qa ) {
				$out .= '<h3>' . esc_html( $qa[0] ) . '</h3><p>' . esc_html( $qa[1] ) . '</p>';
			}
			return $content . $out;
		}
	}
	return $content;
}
add_filter( 'the_content', 'tf_jseo_faq_html', 20 );

/** Notice after activation. */
function tf_jseo_notice() {
	$n = get_option( 'tf_jseo_created', null );
	if ( null === $n || ! current_user_can( 'manage_options' ) ) {
		return;
	}
	echo '<div class="notice notice-success is-dismissible"><p><strong>THE FACES · Journal SEO:</strong> ' . (int) $n . ' artículos creados en el Journal (inglés). Revísalos en Entradas.</p></div>';
	delete_option( 'tf_jseo_created' );
}
add_action( 'admin_notices', 'tf_jseo_notice' );
"""

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
with open(os.path.join(OUT, 'thefaces-journal-seo.php'), 'w', encoding='utf-8') as f:
    f.write(php)
print(subprocess.run(['php', '-l', os.path.join(OUT, 'thefaces-journal-seo.php')], capture_output=True, text=True).stdout)
