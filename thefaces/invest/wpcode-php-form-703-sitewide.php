<?php
/**
 * THE FACES · prints Forminator form 703 (hidden) at the end of every page,
 * so the site-wide contact bar can open it in its window ("Send a request").
 * WPCode → Add snippet → PHP snippet → Insert method: Auto Insert → Location: "Run Everywhere" → Activate.
 * Not printed on "Book an Investor Meeting": that page already shows the form in its own contact card.
 */
add_action( 'wp_footer', function () {
	if ( is_admin() || is_page( 'book-an-investor-meeting' ) ) {
		return;
	}
	echo '<div id="tf-form-703-src" style="display:none">' . do_shortcode( '[forminator_form id="703"]' ) . '</div>';
}, 5 );
