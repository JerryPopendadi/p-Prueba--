<?php
/**
 * Meta Pixel (Facebook / Instagram ads).
 *
 * The pixel code is printed on every public page so Meta can find it, but it starts
 * with consent revoked: nothing is sent until the visitor accepts the cookie banner
 * (localStorage tf_consent = granted, set by window.tfConsent). Then the queued
 * PageView is sent.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tf_spa_meta_pixel_id() {
	return preg_replace( '/[^0-9]/', '', (string) tf_spa_opt( 'meta_pixel' ) );
}

function tf_spa_meta_pixel_head() {
	$id = tf_spa_meta_pixel_id();
	if ( ! $id || is_admin() || is_customize_preview() ) {
		return;
	}
	?>
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
(function(){
var ok=false;try{ok=localStorage.getItem('tf_consent')==='granted'}catch(e){}
fbq('consent',ok?'grant':'revoke');
fbq('init','<?php echo esc_js( $id ); ?>');
fbq('track','PageView');
var prev=window.tfConsent;
window.tfConsent=function(yes){
if(prev){prev(yes)}else{try{localStorage.setItem('tf_consent',yes?'granted':'denied')}catch(e){}}
fbq('consent',yes?'grant':'revoke');
};
})();
</script>
<!-- End Meta Pixel Code -->
	<?php
}
add_action( 'wp_head', 'tf_spa_meta_pixel_head', 2 );
