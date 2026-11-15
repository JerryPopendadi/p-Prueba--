<?php
/**
 * THE FACES Spa · security hardening.
 *
 * Conservative protections that do not change how the site looks or works for visitors:
 * security headers, no WordPress version leak, no user enumeration, login brute-force limit,
 * generic login errors, theme/plugin file editor off and (optional) XML-RPC off.
 * Each group can be switched off in Ajustes > THE FACES > Seguridad.
 *
 * @package TheFacesSpa
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Security switches: main switch and XML-RPC. */
function tf_spa_sec_on() {
	return (bool) tf_spa_opt( 'security' );
}

/* ---------- 1. Security headers (site and login page) ---------- */

function tf_spa_sec_headers() {
	if ( ! tf_spa_sec_on() || headers_sent() || is_admin() ) {
		return;
	}
	header( 'X-Content-Type-Options: nosniff' );
	header( 'X-Frame-Options: SAMEORIGIN' );
	header( 'Referrer-Policy: strict-origin-when-cross-origin' );
	header( 'Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()' );
	header( 'Cross-Origin-Opener-Policy: same-origin-allow-popups' );
	// Scripts are not restricted, so Google Tag Manager, Maps and the booking links keep working.
	header( 'Content-Security-Policy: ' . ( is_ssl() ? 'upgrade-insecure-requests; ' : '' ) . "frame-ancestors 'self'; base-uri 'self'; object-src 'none'; form-action 'self' https:" );
	if ( is_ssl() ) {
		header( 'Strict-Transport-Security: max-age=31536000' );
	}
}
add_action( 'send_headers', 'tf_spa_sec_headers' );
add_action( 'login_init', 'tf_spa_sec_headers' );

/* ---------- 2. Do not reveal the WordPress version ---------- */

function tf_spa_sec_hide_version() {
	if ( ! tf_spa_sec_on() ) {
		return;
	}
	remove_action( 'wp_head', 'wp_generator' );
	add_filter( 'the_generator', '__return_empty_string' );
}
add_action( 'init', 'tf_spa_sec_hide_version' );

/* ---------- 3. No user enumeration (?author=1, REST users, user sitemap) ---------- */

function tf_spa_sec_block_author_scan() {
	if ( ! tf_spa_sec_on() || is_admin() || is_user_logged_in() ) {
		return;
	}
	// phpcs:ignore WordPress.Security.NonceVerification.Recommended -- read-only check of a public query var.
	if ( isset( $_GET['author'] ) && preg_match( '/\d/', (string) wp_unslash( $_GET['author'] ) ) ) {
		wp_safe_redirect( home_url( '/' ), 301 );
		exit;
	}
}
add_action( 'init', 'tf_spa_sec_block_author_scan', 1 );

function tf_spa_sec_rest_users( $endpoints ) {
	if ( tf_spa_sec_on() && ! is_user_logged_in() ) {
		foreach ( array_keys( $endpoints ) as $route ) {
			if ( 0 === strpos( $route, '/wp/v2/users' ) ) {
				unset( $endpoints[ $route ] );
			}
		}
	}
	return $endpoints;
}
add_filter( 'rest_endpoints', 'tf_spa_sec_rest_users' );

function tf_spa_sec_sitemap_users( $provider, $name ) {
	return ( tf_spa_sec_on() && 'users' === $name ) ? false : $provider;
}
add_filter( 'wp_sitemaps_add_provider', 'tf_spa_sec_sitemap_users', 10, 2 );

/* ---------- 4. Login: generic errors and a limit on failed attempts ---------- */

function tf_spa_sec_login_error() {
	return tf_spa_sec_on() ? '<strong>Error:</strong> usuario o contraseña incorrectos.' : null;
}
add_filter(
	'login_errors',
	function ( $error ) {
		$generic = tf_spa_sec_login_error();
		return ( $generic && false === strpos( (string) $error, 'tf-locked' ) ) ? $generic : $error;
	}
);

/** Visitor IP (Cloudflare's header when present, so a CDN does not lock everyone out together). */
function tf_spa_sec_ip() {
	$cf = isset( $_SERVER['HTTP_CF_CONNECTING_IP'] ) ? sanitize_text_field( wp_unslash( $_SERVER['HTTP_CF_CONNECTING_IP'] ) ) : '';
	if ( $cf && filter_var( $cf, FILTER_VALIDATE_IP ) ) {
		return $cf;
	}
	$ip = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '';
	return filter_var( $ip, FILTER_VALIDATE_IP ) ? $ip : '0.0.0.0';
}

function tf_spa_sec_key() {
	return 'tf_login_' . md5( tf_spa_sec_ip() );
}

/** 5 failed logins from one IP lock that IP out for 15 minutes. */
function tf_spa_sec_check_lock( $user ) {
	if ( tf_spa_sec_on() && (int) get_transient( tf_spa_sec_key() ) >= 5 ) {
		return new WP_Error( 'tf_locked', '<span class="tf-locked"></span><strong>Error:</strong> demasiados intentos fallidos. Vuelve a intentarlo dentro de 15 minutos.' );
	}
	return $user;
}
add_filter( 'authenticate', 'tf_spa_sec_check_lock', 30 );

function tf_spa_sec_failed() {
	if ( ! tf_spa_sec_on() ) {
		return;
	}
	$k = tf_spa_sec_key();
	set_transient( $k, (int) get_transient( $k ) + 1, 15 * MINUTE_IN_SECONDS );
}
add_action( 'wp_login_failed', 'tf_spa_sec_failed' );

function tf_spa_sec_success() {
	delete_transient( tf_spa_sec_key() );
}
add_action( 'wp_login', 'tf_spa_sec_success' );

/* ---------- 5. No editing of theme and plugin code from the dashboard ---------- */

if ( ! defined( 'DISALLOW_FILE_EDIT' ) && (bool) tf_spa_opt( 'security' ) ) {
	define( 'DISALLOW_FILE_EDIT', true );
}

/* ---------- 6. XML-RPC off (old remote-publishing door, a common brute-force target) ---------- */

function tf_spa_sec_xmlrpc() {
	if ( ! tf_spa_opt( 'xmlrpc_off' ) ) {
		return;
	}
	if ( defined( 'XMLRPC_REQUEST' ) && XMLRPC_REQUEST ) {
		status_header( 403 );
		exit( 'XML-RPC is disabled.' );
	}
	add_filter( 'xmlrpc_enabled', '__return_false' );
	add_filter( 'xmlrpc_methods', '__return_empty_array' );
	add_filter(
		'wp_headers',
		function ( $h ) {
			unset( $h['X-Pingback'] );
			return $h;
		}
	);
	remove_action( 'wp_head', 'rsd_link' );
}
add_action( 'plugins_loaded', 'tf_spa_sec_xmlrpc' );

/* ---------- 7. Security checklist for the settings page ---------- */

/** List of [ok, text] checks the site owner can act on. */
function tf_spa_sec_checks() {
	global $wp_version;
	$admins = get_users( array( 'role' => 'administrator', 'fields' => array( 'user_login' ) ) );
	$logins = wp_list_pluck( $admins, 'user_login' );
	$checks = array(
		array( 0 === strpos( home_url(), 'https://' ), 'La web usa HTTPS (candado).' ),
		array( ! in_array( 'admin', $logins, true ), 'No hay ningún administrador llamado «admin» (es el primer nombre que prueban los ataques).' ),
		array( count( $admins ) <= 3, 'Hay pocos administradores (' . count( $admins ) . '). Cuantos menos, menos riesgo.' ),
		array( ! ( defined( 'WP_DEBUG_DISPLAY' ) && WP_DEBUG_DISPLAY && defined( 'WP_DEBUG' ) && WP_DEBUG ), 'Los errores de PHP no se muestran a los visitantes.' ),
		array( version_compare( PHP_VERSION, '8.1', '>=' ), 'PHP ' . PHP_VERSION . ' (recomendado 8.1 o superior, con soporte de seguridad).' ),
		array( defined( 'DISALLOW_FILE_EDIT' ) && DISALLOW_FILE_EDIT, 'El editor de archivos de temas y plugins está desactivado.' ),
	);
	if ( function_exists( 'get_core_updates' ) ) {
		$up = get_core_updates();
		$checks[] = array( empty( $up ) || ! isset( $up[0]->response ) || 'upgrade' !== $up[0]->response, 'WordPress ' . $wp_version . ' está actualizado.' );
	}
	return $checks;
}
