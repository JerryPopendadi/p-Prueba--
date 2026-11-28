<?php
/**
 * THE FACES Spa · hide gift certificates (temporary switch).
 *
 * While "Ocultar certificados de regalo" is on (Ajustes > THE FACES), the whole site behaves as if
 * gift certificates did not exist, without deleting anything:
 *  - the gift section is left out of the home page;
 *  - every link to the gift page, to the gift article of the Journal and to the gift terms is removed
 *    (main menu, phone menu, footer, site map, explore tiles, "explore more" chips, Journal cards);
 *  - the gift question of the FAQ (and its Google data), the gift sentence of the menu and the gift
 *    section of the terms page are removed; titles that mention gifts are shortened;
 *  - the gift page and the gift article send visitors to the home page of their language (temporary
 *    302 redirect, so Google keeps them for later) and leave the sitemaps.
 * Turning the switch off brings everything back as before.
 *
 * @package TheFacesSpa
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function tf_spa_gifts_hidden() {
	return (bool) tf_spa_opt( 'gifts_off' );
}

/** Texts that mention gifts, and the same text without them (all 9 languages). */
function tf_spa_gifts_texts() {
	return array(
		// Note under the menu builder.
		'Hair spa for kids, rituals for couples and gift certificates are available.' => 'Hair spa for kids and rituals for couples are available.',
		'Есть хэд-спа для детей, ритуалы для пар и подарочные сертификаты.'          => 'Есть хэд-спа для детей и ритуалы для пар.',
		'Hay head spa para niños, rituales para parejas y certificados de regalo.'   => 'Hay head spa para niños y rituales para parejas.',
		'Head Spa für Kinder, Rituale für Paare und Geschenkgutscheine sind verfügbar.' => 'Head Spa für Kinder und Rituale für Paare sind verfügbar.',
		'มีเฮดสปาสำหรับเด็ก พิธีกรรมสำหรับคู่รัก และบัตรของขวัญ'                         => 'มีเฮดสปาสำหรับเด็ก และพิธีกรรมสำหรับคู่รัก',
		'Tersedia head spa untuk anak, ritual untuk pasangan, dan voucher hadiah.'   => 'Tersedia head spa untuk anak dan ritual untuk pasangan.',
		'キッズ向けヘッドスパ、カップル向けリチュアル、ギフト券もご用意しています。'               => 'キッズ向けヘッドスパ、カップル向けリチュアルもご用意しています。',
		'Head spa pour enfants, rituels pour couples et cartes cadeaux disponibles.' => 'Head spa pour enfants et rituels pour couples disponibles.',
		'Є хед-спа для дітей, ритуали для пар і подарункові сертифікати.'            => 'Є хед-спа для дітей і ритуали для пар.',
		// Name of the terms page (footer link, page title, breadcrumb).
		'Booking terms, cancellation &amp; gift certificates'        => 'Booking terms &amp; cancellation',
		'Booking terms, cancellation & gift certificates'            => 'Booking terms & cancellation',
		'Условия записи, отмена и сертификаты'                       => 'Условия записи и отмена',
		'Condiciones de reserva, cancelación y certificados'         => 'Condiciones de reserva y cancelación',
		'Buchungsbedingungen, Stornierung &amp; Gutscheine'          => 'Buchungsbedingungen &amp; Stornierung',
		'Buchungsbedingungen, Stornierung & Gutscheine'              => 'Buchungsbedingungen & Stornierung',
		'เงื่อนไขการจอง การยกเลิก และบัตรของขวัญ'                        => 'เงื่อนไขการจองและการยกเลิก',
		'Ketentuan pemesanan, pembatalan &amp; voucher'              => 'Ketentuan pemesanan &amp; pembatalan',
		'Ketentuan pemesanan, pembatalan & voucher'                  => 'Ketentuan pemesanan & pembatalan',
		'予約条件・キャンセル・ギフト券'                                   => '予約条件・キャンセル',
		'Conditions de réservation, annulation &amp; cartes cadeaux' => 'Conditions de réservation &amp; annulation',
		'Conditions de réservation, annulation & cartes cadeaux'     => 'Conditions de réservation & annulation',
		'Умови запису, скасування та сертифікати'                    => 'Умови запису та скасування',
		// Introduction of the terms page.
		'Cancellation, rescheduling, terms of use and gift certificate terms of THE FACES Spa' => 'Cancellation, rescheduling and terms of use of THE FACES Spa',
		'Отмена, перенос, условия использования и правила подарочных сертификатов THE FACES Spa' => 'Отмена, перенос и условия использования THE FACES Spa',
		'Cancelación, cambios de cita, condiciones de uso y de los certificados regalo de THE FACES Spa' => 'Cancelación, cambios de cita y condiciones de uso de THE FACES Spa',
		'Stornierung, Umbuchung, Nutzungsbedingungen und Gutscheinbedingungen von THE FACES Spa' => 'Stornierung, Umbuchung und Nutzungsbedingungen von THE FACES Spa',
		'การยกเลิก การเลื่อนนัด ข้อกำหนดการใช้งาน และเงื่อนไขบัตรของขวัญของ THE FACES Spa' => 'การยกเลิก การเลื่อนนัด และข้อกำหนดการใช้งานของ THE FACES Spa',
		'Pembatalan, penjadwalan ulang, ketentuan penggunaan, dan ketentuan voucher THE FACES Spa' => 'Pembatalan, penjadwalan ulang, dan ketentuan penggunaan THE FACES Spa',
		'キャンセル、日時変更、利用規約、ギフト券規約。'                     => 'キャンセル、日時変更、利用規約。',
		'Annulation, report, conditions d&#x27;utilisation et conditions des cartes cadeaux de THE FACES Spa' => 'Annulation, report et conditions d&#x27;utilisation de THE FACES Spa',
		'Скасування, перенесення, умови використання та правила подарункових сертифікатів THE FACES Spa' => 'Скасування, перенесення та умови використання THE FACES Spa',
	);
}

/** Remove every trace of gift certificates from a piece of generated HTML. */
function tf_spa_gifts_strip( $html ) {
	if ( ! tf_spa_gifts_hidden() || '' === $html ) {
		return $html;
	}
	$orig = $html;
	// Links to the gift page (any language), to the gift article and to the gift terms.
	$url = '[^"]*/(?:gift-certificates/|spa-gift-certificates-bali[^"]*|terms/#gift)';
	$html = preg_replace( '~<li>\s*<a\b[^>]*href="' . $url . '"[^>]*>.*?</a>\s*</li>~s', '', $html );
	$html = preg_replace( '~<a\b[^>]*href="' . $url . '"[^>]*>.*?</a>~s', '', $html );
	// The gift block (if it comes in through a single-block shortcode).
	$html = preg_replace( '#<div class="tf"[^>]*data-block="11-gifts".*?</section>\s*</div>#s', '', $html );
	// FAQ: the gift question and its Google data.
	$kw   = '(?:gift|подар|regalo|Gutschein|ของขวัญ|hadiah|ギフト|cadeau)';
	$html = preg_replace( '#<details><summary>[^<]*' . $kw . '[^<]*</summary>.*?</details>#su', '', $html );
	$html = preg_replace( '#,\s*\{"@type": "Question", "name": "[^"]*' . $kw . '[^"]*", "acceptedAnswer": \{"@type": "Answer", "text": "(?:[^"\\\\]|\\\\.)*"\}\}#su', '', $html );
	$html = preg_replace( '#\{"@type": "Question", "name": "[^"]*' . $kw . '[^"]*", "acceptedAnswer": \{"@type": "Answer", "text": "(?:[^"\\\\]|\\\\.)*"\}\},\s*#su', '', $html );
	// Terms page: the gift section.
	$html = preg_replace( '#<h2 id="gift">.*?</h2>\s*<p>.*?</p>#s', '', $html );
	// Sentences and titles.
	$html = strtr( $html, tf_spa_gifts_texts() );
	// Footer site map: keep the number of links right.
	$html = preg_replace_callback(
		'#(<details class="f-map"><summary>[^<]*?)(\d+)(</summary><ul>)(.*?)(</ul>)#s',
		function ( $m ) {
			return $m[1] . substr_count( $m[4], '<li>' ) . $m[3] . $m[4] . $m[5];
		},
		$html
	);
	return ( is_string( $html ) && '' !== $html ) ? $html : $orig;
}

/** Document title of the terms page without the gift part. */
function tf_spa_gifts_title( $title ) {
	return tf_spa_gifts_hidden() ? strtr( $title, tf_spa_gifts_texts() ) : $title;
}
add_filter( 'pre_get_document_title', 'tf_spa_gifts_title', 30 );
add_filter( 'wpseo_title', 'tf_spa_gifts_title', 30 );
add_filter( 'wpseo_opengraph_title', 'tf_spa_gifts_title', 30 );
add_filter( 'wpseo_metadesc', 'tf_spa_gifts_title', 30 );
add_filter( 'wpseo_opengraph_desc', 'tf_spa_gifts_title', 30 );

/** IDs of the gift page (all languages) and of the gift article (all languages). */
function tf_spa_gifts_ids() {
	static $ids = null;
	if ( null !== $ids ) {
		return $ids;
	}
	$ids = array();
	foreach ( (array) get_option( 'thefaces_spa_pages', array() ) as $lang => $map ) {
		if ( is_array( $map ) && ! empty( $map['gift-certificates'] ) ) {
			$ids[] = (int) $map['gift-certificates'];
		}
	}
	$posts = get_posts(
		array(
			'post_type'        => 'post',
			'post_status'      => 'any',
			'numberposts'      => 50,
			'fields'           => 'ids',
			'meta_key'         => '_tf_group',
			'meta_value'       => 'gifts',
			'tf_gifts_skip'    => 1,
			'suppress_filters' => true,
		)
	);
	$ids = array_values( array_unique( array_merge( $ids, array_map( 'intval', $posts ) ) ) );
	return $ids;
}

/** Leave the gift article out of the Journal lists, related posts, feeds and search. */
function tf_spa_gifts_exclude_posts( $q ) {
	if ( is_admin() || ! tf_spa_gifts_hidden() || $q->get( 'tf_gifts_skip' ) ) {
		return;
	}
	$type = $q->get( 'post_type' );
	if ( $type && 'post' !== $type && 'any' !== $type && ! ( is_array( $type ) && in_array( 'post', $type, true ) ) ) {
		return;
	}
	if ( $q->is_singular() && $q->is_main_query() ) {
		return; // The gift article itself is redirected below.
	}
	$ids = tf_spa_gifts_ids();
	if ( $ids ) {
		$q->set( 'post__not_in', array_merge( (array) $q->get( 'post__not_in' ), $ids ) );
	}
}
add_action( 'pre_get_posts', 'tf_spa_gifts_exclude_posts' );

/** The gift page and the gift article send visitors to the home page of their language. */
function tf_spa_gifts_redirect() {
	if ( ! tf_spa_gifts_hidden() || is_admin() || ! is_singular() ) {
		return;
	}
	$id   = get_queried_object_id();
	$lang = '';
	$cur  = tf_spa_current_page();
	if ( $cur && 'gift-certificates' === $cur['page'] ) {
		$lang = tf_spa_lang( $cur['lang'] );
	} elseif ( is_singular( 'post' ) && 'gifts' === get_post_meta( $id, '_tf_group', true ) ) {
		$lang = get_post_meta( $id, '_tf_lang', true );
		$lang = $lang ? $lang : tf_spa_lang();
	} elseif ( ! in_array( $id, tf_spa_gifts_ids(), true ) ) {
		return;
	}
	$lang = $lang ? $lang : tf_spa_lang();
	wp_safe_redirect( tf_spa_key_url( 'home', $lang ), 302 );
	exit;
}
add_action( 'template_redirect', 'tf_spa_gifts_redirect', 1 );

/** Sitemaps: Yoast and the WordPress core sitemap. */
function tf_spa_gifts_sitemap_ids( $ids ) {
	return tf_spa_gifts_hidden() ? array_merge( (array) $ids, tf_spa_gifts_ids() ) : $ids;
}
add_filter( 'wpseo_exclude_from_sitemap_by_post_ids', 'tf_spa_gifts_sitemap_ids' );

function tf_spa_gifts_core_sitemap( $args ) {
	if ( tf_spa_gifts_hidden() ) {
		$args['post__not_in'] = array_merge( isset( $args['post__not_in'] ) ? (array) $args['post__not_in'] : array(), tf_spa_gifts_ids() );
	}
	return $args;
}
add_filter( 'wp_sitemaps_posts_query_args', 'tf_spa_gifts_core_sitemap' );
