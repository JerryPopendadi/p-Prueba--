<?php
/**
 * Plugin Name: THE FACES · SEO sitemap fix
 * Description: Keeps the Yoast sitemap clean so Google only gets pages it can index: removes category archives (they redirect to the Journal), journal articles whose canonical is a main page, cart / checkout / account pages and the author archive.
 * Version:     1.0.0
 * Author:      THE FACES
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Category archives 301-redirect to /journal/?cat=…, so they do not belong in the sitemap. */
function tf_seo_exclude_taxonomies( $excluded, $taxonomy ) {
	if ( in_array( $taxonomy, array( 'category', 'post_tag', 'post_format' ), true ) ) {
		return true;
	}
	return $excluded;
}
add_filter( 'wpseo_sitemap_exclude_taxonomy', 'tf_seo_exclude_taxonomies', 10, 2 );

/** One author only: the author archive is a thin duplicate of the journal. */
add_filter( 'wpseo_sitemap_exclude_author', '__return_empty_array' );

/** Post IDs to leave out of the sitemap. */
function tf_seo_excluded_ids( $ids ) {
	$ids = is_array( $ids ) ? $ids : array();

	// WooCommerce pages that are noindex by design (cart, checkout, my account).
	if ( function_exists( 'wc_get_page_id' ) ) {
		foreach ( array( 'cart', 'checkout', 'myaccount' ) as $p ) {
			$id = (int) wc_get_page_id( $p );
			if ( $id > 0 ) {
				$ids[] = $id;
			}
		}
	}

	// Journal articles whose canonical is a main page (THE FACES Spa plugin).
	if ( function_exists( 'tf_spa_post_canonical' ) ) {
		$cached = get_transient( 'tf_seo_canonical_ids' );
		if ( false === $cached ) {
			$cached = array();
			$posts  = get_posts( array( 'post_type' => 'post', 'post_status' => 'publish', 'numberposts' => -1, 'fields' => 'ids' ) );
			foreach ( $posts as $pid ) {
				if ( tf_spa_post_canonical( $pid ) ) {
					$cached[] = (int) $pid;
				}
			}
			set_transient( 'tf_seo_canonical_ids', $cached, DAY_IN_SECONDS );
		}
		$ids = array_merge( $ids, $cached );
	}

	return array_values( array_unique( array_map( 'intval', $ids ) ) );
}
add_filter( 'wpseo_exclude_from_sitemap_by_post_ids', 'tf_seo_excluded_ids' );

/** Refresh the list when posts change. */
function tf_seo_flush() {
	delete_transient( 'tf_seo_canonical_ids' );
}
add_action( 'save_post', 'tf_seo_flush' );
register_activation_hook( __FILE__, 'tf_seo_flush' );
