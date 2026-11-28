<?php
/**
 * THE FACES Spa · images in the WordPress Media Library and in the sitemap.
 *
 * The site's photos live inside the plugin. When the same photos are uploaded to Medios with the
 * SEO file names of includes/media.json (folder "THE-FACES-imagenes-web"), the plugin:
 *  - recognises each one by its file name and fills its title and alternative text (if empty);
 *  - serves the site with the Media Library copy of each photo;
 *  - lists the photos of every page and article in the Yoast sitemap (also before the upload,
 *    then with the plugin copy).
 * Nothing changes for photos that are not uploaded: the plugin copy keeps being used.
 *
 * @package TheFacesSpa
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** data/media.json: original file => array( file, title, alt ). */
function tf_spa_media_json( $name ) {
	static $c = array();
	if ( ! isset( $c[ $name ] ) ) {
		$f          = TF_SPA_DIR . 'includes/' . $name . '.json';
		$c[ $name ] = file_exists( $f ) ? json_decode( file_get_contents( $f ), true ) : array();
		$c[ $name ] = is_array( $c[ $name ] ) ? $c[ $name ] : array();
	}
	return $c[ $name ];
}

function tf_spa_media_list() {
	return tf_spa_media_json( 'media' );
}

/** Saved connections: original file => attachment ID. */
function tf_spa_media_map() {
	$m = get_option( 'thefaces_spa_media', array() );
	return is_array( $m ) ? $m : array();
}

/** Which plugin image an uploaded file is (by its file name), or ''. */
function tf_spa_media_match( $attached_file ) {
	$base = strtolower( pathinfo( $attached_file, PATHINFO_FILENAME ) );
	$base = preg_replace( '/-(\d+|scaled|e\d+)$/', '', $base ); // WordPress suffixes: name-1, name-scaled.
	foreach ( tf_spa_media_list() as $orig => $m ) {
		if ( strtolower( pathinfo( $m['file'], PATHINFO_FILENAME ) ) === $base ) {
			return $orig;
		}
	}
	return '';
}

/** Fill title and alternative text of a connected image, only where they are empty or the bare file name. */
function tf_spa_media_fill( $id, $orig ) {
	$list = tf_spa_media_list();
	if ( empty( $list[ $orig ] ) ) {
		return;
	}
	$m = $list[ $orig ];
	if ( '' === (string) get_post_meta( $id, '_wp_attachment_image_alt', true ) ) {
		update_post_meta( $id, '_wp_attachment_image_alt', $m['alt'] );
	}
	$post = get_post( $id );
	if ( $post && ( '' === $post->post_title || sanitize_title( $post->post_title ) === sanitize_title( pathinfo( $m['file'], PATHINFO_FILENAME ) ) ) ) {
		wp_update_post( array( 'ID' => $id, 'post_title' => $m['title'] ) );
	}
}

/** Look for every image of the list in the Media Library and save the connections. */
function tf_spa_media_scan() {
	$map = array();
	$ids = get_posts(
		array(
			'post_type'      => 'attachment',
			'post_status'    => 'inherit',
			'post_mime_type' => 'image',
			'numberposts'    => -1,
			'fields'         => 'ids',
			'orderby'        => 'ID',
			'order'          => 'ASC',
		)
	);
	foreach ( $ids as $id ) {
		$orig = tf_spa_media_match( (string) get_post_meta( $id, '_wp_attached_file', true ) );
		if ( $orig && empty( $map[ $orig ] ) ) {
			$map[ $orig ] = (int) $id;
			tf_spa_media_fill( $id, $orig );
		}
	}
	update_option( 'thefaces_spa_media', $map, false );
	tf_spa_media_clear_sitemap();
	return $map;
}

function tf_spa_media_clear_sitemap() {
	if ( class_exists( 'WPSEO_Sitemaps_Cache' ) && method_exists( 'WPSEO_Sitemaps_Cache', 'clear' ) ) {
		WPSEO_Sitemaps_Cache::clear();
	}
}

/** New upload with one of the names: connect it at once. */
function tf_spa_media_on_upload( $id ) {
	$orig = tf_spa_media_match( (string) get_post_meta( $id, '_wp_attached_file', true ) );
	if ( ! $orig ) {
		return;
	}
	$map = tf_spa_media_map();
	if ( empty( $map[ $orig ] ) || ! get_post( $map[ $orig ] ) ) {
		$map[ $orig ] = (int) $id;
		update_option( 'thefaces_spa_media', $map, false );
		tf_spa_media_clear_sitemap();
	}
	tf_spa_media_fill( $id, $orig );
}
add_action( 'add_attachment', 'tf_spa_media_on_upload', 20 );

function tf_spa_media_on_delete( $id ) {
	$map = tf_spa_media_map();
	$key = array_search( (int) $id, array_map( 'intval', $map ), true );
	if ( false !== $key ) {
		unset( $map[ $key ] );
		update_option( 'thefaces_spa_media', $map, false );
	}
}
add_action( 'delete_attachment', 'tf_spa_media_on_delete' );

/** URL of a plugin image: the Media Library copy when connected, otherwise the plugin copy. */
function tf_spa_media_url( $orig ) {
	static $cache = array();
	if ( isset( $cache[ $orig ] ) ) {
		return $cache[ $orig ];
	}
	$map = tf_spa_media_map();
	$url = '';
	if ( ! empty( $map[ $orig ] ) ) {
		$url = (string) wp_get_attachment_url( $map[ $orig ] );
	}
	$cache[ $orig ] = $url ? $url : TF_SPA_URL . 'assets/media/' . $orig;
	return $cache[ $orig ];
}

/** Swap the plugin image addresses in generated HTML for the Media Library ones. */
function tf_spa_media_swap( $html ) {
	$map = tf_spa_media_map();
	if ( ! $map || '' === $html ) {
		return $html;
	}
	$pairs = array();
	foreach ( array_keys( $map ) as $orig ) {
		$url = tf_spa_media_url( $orig );
		if ( 0 !== strpos( $url, TF_SPA_URL ) ) {
			$pairs[ TF_SPA_URL . 'assets/media/' . $orig ] = $url;
		}
	}
	return $pairs ? strtr( $html, $pairs ) : $html;
}

/* ---------- Yoast sitemap: the photos of each page and article ---------- */

/** Plugin page key of a WordPress page (home, menu, ubud…), or ''. */
function tf_spa_media_page_key( $post_id ) {
	static $rev = null;
	if ( null === $rev ) {
		$rev = array();
		foreach ( (array) get_option( 'thefaces_spa_pages', array() ) as $lang => $keys ) {
			foreach ( (array) $keys as $key => $id ) {
				$rev[ (int) $id ] = $key;
			}
		}
	}
	return isset( $rev[ (int) $post_id ] ) ? $rev[ (int) $post_id ] : '';
}

function tf_spa_media_sitemap_images( $images, $post_id ) {
	$list  = tf_spa_media_list();
	$files = array();
	$key   = tf_spa_media_page_key( $post_id );
	if ( $key ) {
		$per = tf_spa_media_json( 'page-images' );
		$files = isset( $per[ $key ] ) ? (array) $per[ $key ] : array();
	} elseif ( 'post' === get_post_type( $post_id ) ) {
		$img = get_post_meta( $post_id, '_tf_img', true );
		if ( $img ) {
			$files[] = $img;
		}
	}
	if ( function_exists( 'tf_spa_gifts_hidden' ) && tf_spa_gifts_hidden() && 'gift-certificates' === $key ) {
		return $images;
	}
	$have = array();
	foreach ( (array) $images as $im ) {
		if ( ! empty( $im['src'] ) ) {
			$have[ $im['src'] ] = true;
		}
	}
	foreach ( $files as $f ) {
		$src = tf_spa_media_url( $f );
		if ( isset( $have[ $src ] ) ) {
			continue;
		}
		$have[ $src ] = true;
		$images[]     = array(
			'src'   => $src,
			'title' => isset( $list[ $f ]['title'] ) ? $list[ $f ]['title'] : '',
			'alt'   => isset( $list[ $f ]['alt'] ) ? $list[ $f ]['alt'] : '',
		);
	}
	return $images;
}
add_filter( 'wpseo_sitemap_urlimages', 'tf_spa_media_sitemap_images', 10, 2 );

/* ---------- Admin: connect button and status ---------- */

function tf_spa_media_handle() {
	if ( ! current_user_can( 'manage_options' ) || ! check_admin_referer( 'tf_spa_media' ) ) {
		wp_die( 'No permitido.' );
	}
	$map = tf_spa_media_scan();
	wp_safe_redirect( add_query_arg( array( 'page' => 'thefaces-spa', 'tf_media' => count( $map ) ), admin_url( 'options-general.php' ) ) );
	exit;
}
add_action( 'admin_post_tf_spa_media', 'tf_spa_media_handle' );

/** Section shown on Ajustes > THE FACES. */
function tf_spa_media_admin_section() {
	$list = tf_spa_media_list();
	$map  = tf_spa_media_map();
	$n    = 0;
	foreach ( $map as $id ) {
		if ( get_post( $id ) ) {
			$n++;
		}
	}
	?>
	<h2>Imágenes en Medios y en el sitemap</h2>
	<?php if ( isset( $_GET['tf_media'] ) ) : // phpcs:ignore WordPress.Security.NonceVerification.Recommended ?>
		<div class="notice notice-success inline"><p>Imágenes conectadas: <?php echo (int) $_GET['tf_media']; // phpcs:ignore ?> de <?php echo count( $list ); ?>.</p></div>
	<?php endif; ?>
	<p>Sube a <strong>Medios › Añadir nuevo</strong> las fotos de la carpeta <em>THE-FACES-imagenes-web</em> sin cambiarles el nombre. El plugin las reconoce, rellena su título y texto alternativo y la web pasa a usarlas desde Medios. Las fotos de cada página y artículo ya aparecen en el sitemap de Yoast.</p>
	<p><strong>Conectadas: <?php echo (int) $n; ?> de <?php echo count( $list ); ?></strong></p>
	<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
		<input type="hidden" name="action" value="tf_spa_media">
		<?php wp_nonce_field( 'tf_spa_media' ); ?>
		<?php submit_button( 'Buscar y conectar las imágenes de Medios', 'secondary', 'submit', false ); ?>
	</form>
	<details style="margin-top:10px"><summary>Ver la lista de imágenes</summary>
		<table class="widefat striped" style="max-width:900px;margin-top:8px"><thead><tr><th>Archivo para subir</th><th>Texto alternativo</th><th>Estado</th></tr></thead><tbody>
		<?php foreach ( $list as $orig => $m ) : ?>
			<tr><td><code><?php echo esc_html( $m['file'] ); ?></code></td><td><?php echo esc_html( $m['alt'] ); ?></td>
			<td><?php echo ( ! empty( $map[ $orig ] ) && get_post( $map[ $orig ] ) ) ? '<span style="color:#1a7f37">✔ conectada</span>' : '—'; ?></td></tr>
		<?php endforeach; ?>
		</tbody></table>
	</details>
	<?php
}
