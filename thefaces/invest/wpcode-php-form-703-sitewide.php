<?php
/**
 * THE FACES · prints Forminator form 703 (hidden) at the end of every page.
 * The investor pages (Ubud, Hotels, Hub, Global, Book an Investor Meeting) and the site-wide
 * contact bar take the form from here and show it in their own contact card / window.
 * WPCode → Add snippet → PHP snippet → Insert method: Auto Insert → Location: "Run Everywhere" → Activate.
 * (Earlier version skipped "Book an Investor Meeting"; its new v2 page needs the form too.)
 */
add_action( 'wp_footer', function () {
	if ( is_admin() ) {
		return;
	}
	echo '<div id="tf-form-703-src" style="display:none">' . do_shortcode( '[forminator_form id="703"]' ) . '</div>';
}, 5 );
