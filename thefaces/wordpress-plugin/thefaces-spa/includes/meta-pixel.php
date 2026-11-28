<?php
/**
 * Meta Pixel (Facebook / Instagram ads).
 *
 * Prints the pixel on every public page (one or more IDs). Standard events:
 *  - PageView on every page;
 *  - ViewContent on service and salon pages;
 *  - Schedule on clicks to the booking system (alteg.io);
 *  - Contact on clicks to WhatsApp, phone or email.
 * With "pixel_consent" on, consent starts revoked and Meta receives the queued events
 * only after the visitor accepts the cookie banner (window.tfConsent / tf_consent).
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tf_spa_meta_pixel_ids() {
	return array_values( array_filter( preg_split( '/[^0-9]+/', (string) tf_spa_opt( 'meta_pixel' ) ) ) );
}

/** Settings saved with 1.7.0 hold only the first pixel; add the Events Manager dataset of the account. */
function tf_spa_meta_pixel_upgrade() {
	$o = get_option( 'thefaces_spa' );
	if ( is_array( $o ) && isset( $o['meta_pixel'] ) && '1557758462849935' === $o['meta_pixel'] ) {
		$o['meta_pixel'] = '1412057363697561, 1557758462849935';
		update_option( 'thefaces_spa', $o );
	}
}
add_action( 'init', 'tf_spa_meta_pixel_upgrade' );

function tf_spa_meta_pixel_head() {
	$ids = tf_spa_meta_pixel_ids();
	if ( ! $ids || is_admin() || is_customize_preview() ) {
		return;
	}
	$consent = (int) tf_spa_opt( 'pixel_consent' );
	$path    = trim( (string) wp_parse_url( isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : '/', PHP_URL_PATH ), '/' ); // phpcs:ignore WordPress.Security.ValidatedSanitizedInput
	$parts   = explode( '/', $path );
	if ( isset( $parts[0] ) && 2 === strlen( $parts[0] ) ) {
		array_shift( $parts ); // language prefix
	}
	$slug    = isset( $parts[0] ) ? $parts[0] : '';
	$content = array( 'menu', 'ubud', 'sanur', 'body-massage', 'face-massage', 'head-spa', 'skin-care', 'couples-spa', 'five-elements', 'certificates' );
	$view    = in_array( $slug, $content, true ) ? $slug : '';
	?>
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
(function(){
var needConsent=<?php echo $consent ? 'true' : 'false'; ?>;
if(needConsent){var ok=false;try{ok=localStorage.getItem('tf_consent')==='granted'}catch(e){}fbq('consent',ok?'grant':'revoke');
var prev=window.tfConsent;window.tfConsent=function(yes){if(prev){prev(yes)}else{try{localStorage.setItem('tf_consent',yes?'granted':'denied')}catch(e){}}fbq('consent',yes?'grant':'revoke')};}
<?php foreach ( $ids as $id ) : ?>
fbq('init','<?php echo esc_js( $id ); ?>');
<?php endforeach; ?>
fbq('track','PageView');
<?php if ( $view ) : ?>
fbq('track','ViewContent',{content_name:'<?php echo esc_js( $view ); ?>',content_category:'spa'});
<?php endif; ?>
document.addEventListener('click',function(ev){
var a=ev.target.closest?ev.target.closest('a[href]'):null;if(!a)return;var h=a.getAttribute('href')||'';
if(/alteg\.io/i.test(h)){fbq('track','Schedule',{content_name:'online_booking'})}
else if(/wa\.me|whatsapp\.com/i.test(h)){fbq('track','Contact',{content_name:'whatsapp'})}
else if(/^tel:/i.test(h)){fbq('track','Contact',{content_name:'phone'})}
else if(/^mailto:/i.test(h)){fbq('track','Contact',{content_name:'email'})}
},true);
})();
</script>
<!-- End Meta Pixel Code -->
	<?php
}
add_action( 'wp_head', 'tf_spa_meta_pixel_head', 2 );

/** Meta Business domain verification tag. */
function tf_spa_fb_domain_verification() {
	$code = preg_replace( '/[^a-z0-9]/', '', strtolower( (string) tf_spa_opt( 'fb_domain' ) ) );
	if ( $code ) {
		echo '<meta name="facebook-domain-verification" content="' . esc_attr( $code ) . '" />' . "\n";
	}
}
add_action( 'wp_head', 'tf_spa_fb_domain_verification', 1 );
