<?php
/**
 * THE FACES · treatments page: THE FACES header + shop + footer, without the theme header.
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
remove_action( 'wp_head', '_block_template_viewport_meta_tag', 0 );
wp_head();
?>
</head>
<body <?php body_class( 'tf-canvas tf-shop-page' ); ?>>
<?php
wp_body_open();
$tf_has_spa = shortcode_exists( 'thefaces' );
if ( $tf_has_spa ) {
	echo do_shortcode( '[thefaces block="header" lang="en"]' ); // phpcs:ignore WordPress.Security.EscapeOutput -- plugin markup.
}
echo do_shortcode( '[thefaces_shop hero="' . ( $tf_has_spa ? '1' : '0' ) . '"]' ); // phpcs:ignore WordPress.Security.EscapeOutput -- escaped inside.
if ( $tf_has_spa ) {
	echo do_shortcode( '[thefaces block="footer" lang="en"]' ); // phpcs:ignore WordPress.Security.EscapeOutput -- plugin markup.
}
wp_footer();
?>
</body>
</html>
