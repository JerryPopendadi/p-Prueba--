<?php
/**
 * THE FACES · pantalla completa: the page content only, without the theme header, footer or sidebars.
 * The site header, footer and cookie banner come from the plugin blocks.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php
// Block themes print a second viewport tag; this page already has one.
remove_action( 'wp_head', '_block_template_viewport_meta_tag', 0 );
wp_head();
?>
</head>
<body <?php body_class( 'tf-canvas' ); ?>>
<?php
wp_body_open();
while ( have_posts() ) {
	the_post();
	if ( is_singular( 'post' ) && function_exists( 'tf_spa_render_post' ) ) {
		echo tf_spa_render_post( get_post() ); // phpcs:ignore WordPress.Security.EscapeOutput -- built from escaped parts.
	} else {
		the_content();
	}
}
wp_footer();
?>
</body>
</html>
