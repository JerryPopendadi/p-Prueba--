<?php
/**
 * Plugin Name: THE FACES · Meta domain verification
 * Description: Adds the facebook-domain-verification meta tag to the head of every page.
 * Version:     1.0.0
 * Author:      THE FACES
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
function tf_meta_domain_tag() {
	if ( function_exists( 'tf_spa_fb_domain_verification' ) ) {
		return; // THE FACES Spa 1.7.2+ already prints it.
	}
	echo '<meta name="facebook-domain-verification" content="2l9h5pvi1chwbqynqsgdjf9bllu214" />' . "\n";
}
add_action( 'wp_head', 'tf_meta_domain_tag', 1 );
