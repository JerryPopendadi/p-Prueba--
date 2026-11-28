<?php
/**
 * Plugin Name: THE FACES · Treatments shop page
 * Description: A clear page to find and prepay THE FACES treatments: search, category filter, Ubud / Sanur filter and one "Buy" button per salon. Shortcode [thefaces_shop]. On activation it creates the page "Prepay a treatment" (/prepay-treatments/).
 * Version:     1.0.1
 * Author:      THE FACES
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Category order on the page (product category names as imported). */
function tf_shop_cat_order() {
	return array( 'Face massage', 'Air kiss & foam', 'Head spa & hair', 'Cleansing & care', 'Five elements', 'Packages', 'For couples', 'For men', 'Body, feet & legs' );
}

function tf_shop_price( $n ) {
	return number_format( (float) $n, 0, '.', ' ' ) . ' IDR';
}

/** Salon slug of a variation (works with the global "Salon" attribute or a local one). */
function tf_shop_variation_salon( $attrs ) {
	foreach ( (array) $attrs as $k => $v ) {
		if ( false !== strpos( strtolower( $k ), 'salon' ) ) {
			return sanitize_title( $v );
		}
	}
	return '';
}

function tf_shop_data() {
	if ( ! function_exists( 'wc_get_products' ) ) {
		return array();
	}
	$items    = array();
	$products = wc_get_products( array( 'status' => 'publish', 'limit' => -1, 'orderby' => 'menu_order', 'order' => 'ASC' ) );
	foreach ( $products as $p ) {
		$cat   = '';
		$terms = get_the_terms( $p->get_id(), 'product_cat' );
		foreach ( (array) $terms as $t ) {
			if ( is_object( $t ) && $t->parent ) {
				$cat = $t->name;
			}
		}
		if ( ! $cat && $terms && is_object( $terms[0] ) ) {
			$cat = $terms[0]->name;
		}
		$buy = array();
		if ( $p->is_type( 'variable' ) ) {
			foreach ( $p->get_children() as $vid ) {
				$v = wc_get_product( $vid );
				if ( ! $v || ! $v->is_purchasable() ) {
					continue;
				}
				$attrs = $v->get_variation_attributes();
				$salon = tf_shop_variation_salon( $attrs );
				$args  = array( 'add-to-cart' => $p->get_id(), 'variation_id' => $vid );
				foreach ( $attrs as $k => $val ) {
					$args[ $k ] = $val;
				}
				$buy[ $salon ? $salon : 'all' ] = array(
					'price' => $v->get_price(),
					'url'   => add_query_arg( $args, wc_get_cart_url() ),
				);
			}
		} elseif ( $p->is_purchasable() ) {
			$buy['all'] = array( 'price' => $p->get_price(), 'url' => add_query_arg( 'add-to-cart', $p->get_id(), wc_get_cart_url() ) );
		}
		if ( ! $buy ) {
			continue;
		}
		ksort( $buy );
		$img     = $p->get_image_id() ? wp_get_attachment_image_url( $p->get_image_id(), 'medium_large' ) : '';
		$items[] = array(
			'name'  => $p->get_name(),
			'url'   => get_permalink( $p->get_id() ),
			'cat'   => $cat,
			'img'   => $img,
			'short' => wp_strip_all_tags( $p->get_short_description() ),
			'dur'   => $p->get_attribute( 'Duration' ),
			'buy'   => $buy,
		);
	}
	return $items;
}

function tf_shop_shortcode() {
	$items = tf_shop_data();
	if ( ! $items ) {
		return '<p>Treatments will appear here soon. Meanwhile, book on WhatsApp: Ubud +62 822 6699 9965 · Sanur +62 813 3770 9190.</p>';
	}
	$order = tf_shop_cat_order();
	$cats  = array_values( array_unique( wp_list_pluck( $items, 'cat' ) ) );
	usort(
		$cats,
		function ( $a, $b ) use ( $order ) {
			$ia = array_search( $a, $order, true );
			$ib = array_search( $b, $order, true );
			return ( false === $ia ? 99 : $ia ) - ( false === $ib ? 99 : $ib );
		}
	);
	usort(
		$items,
		function ( $a, $b ) use ( $order ) {
			$ia = array_search( $a['cat'], $order, true );
			$ib = array_search( $b['cat'], $order, true );
			$d  = ( false === $ia ? 99 : $ia ) - ( false === $ib ? 99 : $ib );
			return $d ? $d : strcmp( $a['name'], $b['name'] );
		}
	);

	ob_start();
	?>
<div id="tfshop">
<style>
#tfshop{--g:#B8913E;--ink:#17140F;--mut:#6f6a62;--line:#e8e2d6;--bg:#faf8f4;font-family:Montserrat,system-ui,sans-serif;color:var(--ink);max-width:1180px;margin:0 auto;padding:8px 0 40px}
#tfshop *{box-sizing:border-box}
#tfshop .hd{text-align:center;margin:10px 0 26px}
#tfshop .hd h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:clamp(32px,5vw,48px);margin:0 0 8px;line-height:1.1}
#tfshop .hd p{color:var(--mut);margin:0 auto;max-width:640px;line-height:1.6}
#tfshop .steps{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:18px 0 0;padding:0;list-style:none;font-size:13px;color:var(--mut)}
#tfshop .steps li{background:var(--bg);border:1px solid var(--line);border-radius:30px;padding:7px 14px}
#tfshop .steps b{color:var(--g)}
#tfshop .bar{position:sticky;top:0;z-index:5;background:#fff;padding:12px 0;border-bottom:1px solid var(--line);margin-bottom:18px}
#tfshop .row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
#tfshop input[type=search]{flex:1 1 260px;min-width:0;padding:13px 16px;border:1px solid var(--line);border-radius:10px;font:inherit;font-size:15px;background:var(--bg)}
#tfshop .salon{display:flex;border:1px solid var(--line);border-radius:10px;overflow:hidden}
#tfshop .salon button{border:0;background:#fff;padding:12px 16px;font:inherit;font-size:14px;cursor:pointer;color:var(--ink)}
#tfshop .salon button.on{background:var(--ink);color:#fff}
#tfshop .chips{display:flex;gap:8px;overflow-x:auto;padding:12px 0 2px;scrollbar-width:none}
#tfshop .chips button{flex:0 0 auto;border:1px solid var(--line);background:#fff;border-radius:30px;padding:9px 15px;font:inherit;font-size:13px;cursor:pointer;white-space:nowrap}
#tfshop .chips button.on{border-color:var(--g);background:var(--g);color:#fff}
#tfshop .count{font-size:13px;color:var(--mut);margin:0 0 12px}
#tfshop .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:18px}
#tfshop .card{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff;display:flex;flex-direction:column}
#tfshop .ph{aspect-ratio:4/3;background:var(--bg) center/cover no-repeat}
#tfshop .bd{padding:16px 16px 18px;display:flex;flex-direction:column;gap:8px;flex:1}
#tfshop .tag{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--g);font-weight:600}
#tfshop .card h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;font-weight:500;margin:0;line-height:1.15}
#tfshop .card h3 a{color:inherit;text-decoration:none}
#tfshop .meta{font-size:13px;color:var(--mut)}
#tfshop .sd{font-size:14px;line-height:1.5;color:#3b372f;margin:0;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
#tfshop .buy{margin-top:auto;display:flex;flex-direction:column;gap:8px;padding-top:6px}
#tfshop .buy a{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:12px 14px;border-radius:10px;background:var(--ink);color:#fff;text-decoration:none;font-size:14px;font-weight:600}
#tfshop .buy a span{font-weight:400;opacity:.85}
#tfshop .buy a:hover{background:var(--g)}
#tfshop .more{font-size:13px;color:var(--mut);text-decoration:underline;align-self:flex-start}
#tfshop .none{display:none;text-align:center;padding:40px 10px;color:var(--mut)}
#tfshop .help{margin-top:30px;text-align:center;background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:22px 16px;line-height:1.7}
#tfshop .help a{color:var(--ink);font-weight:600}
#tfshop [hidden]{display:none!important}
</style>
<div class="hd">
<h1>Prepay your treatment</h1>
<p>Choose a treatment and a salon, pay online, then pick your date and time. Prepaid treatments are valid for 6 months.</p>
<ul class="steps"><li><b>1</b> Choose a treatment</li><li><b>2</b> Choose Ubud or Sanur</li><li><b>3</b> Pay online</li><li><b>4</b> Pick your date</li></ul>
</div>
<div class="bar">
<div class="row">
<input type="search" id="tfs-q" placeholder="Search: face massage, head spa, couples…" aria-label="Search treatments">
<div class="salon" role="group" aria-label="Salon">
<button type="button" class="on" data-salon="">All salons</button><button type="button" data-salon="ubud">Ubud</button><button type="button" data-salon="sanur">Sanur</button>
</div>
</div>
<div class="chips" role="group" aria-label="Category"><button type="button" class="on" data-cat="">All</button>
	<?php foreach ( $cats as $c ) : ?>
<button type="button" data-cat="<?php echo esc_attr( sanitize_title( $c ) ); ?>"><?php echo esc_html( $c ); ?></button>
	<?php endforeach; ?>
</div>
</div>
<p class="count" id="tfs-count"></p>
<div class="grid">
	<?php foreach ( $items as $it ) : ?>
		<?php $salons = implode( ' ', array_keys( $it['buy'] ) ); ?>
<article class="card" data-cat="<?php echo esc_attr( sanitize_title( $it['cat'] ) ); ?>" data-salons="<?php echo esc_attr( $salons ); ?>" data-text="<?php echo esc_attr( mb_strtolower( $it['name'] . ' ' . $it['cat'] . ' ' . $it['short'] ) ); ?>">
<a class="ph" href="<?php echo esc_url( $it['url'] ); ?>" style="background-image:url('<?php echo esc_url( $it['img'] ); ?>')" aria-label="<?php echo esc_attr( $it['name'] ); ?>"></a>
<div class="bd">
<div class="tag"><?php echo esc_html( $it['cat'] ); ?></div>
<h3><a href="<?php echo esc_url( $it['url'] ); ?>"><?php echo esc_html( $it['name'] ); ?></a></h3>
<div class="meta"><?php echo esc_html( trim( ( $it['dur'] ? $it['dur'] . ' · ' : '' ) . ucwords( str_replace( 'all', '', implode( ' & ', array_keys( $it['buy'] ) ) ) ) ) ); ?></div>
<p class="sd"><?php echo esc_html( $it['short'] ); ?></p>
<div class="buy">
		<?php foreach ( $it['buy'] as $salon => $b ) : ?>
<a href="<?php echo esc_url( $b['url'] ); ?>" data-salon="<?php echo esc_attr( $salon ); ?>" rel="nofollow">Buy<?php echo 'all' === $salon ? '' : ' · ' . esc_html( ucfirst( $salon ) ); ?> <span><?php echo esc_html( tf_shop_price( $b['price'] ) ); ?></span></a>
		<?php endforeach; ?>
</div>
<a class="more" href="<?php echo esc_url( $it['url'] ); ?>">Details</a>
</div>
</article>
	<?php endforeach; ?>
</div>
<div class="none" id="tfs-none">No treatment matches. Try another word or choose "All".</div>
<div class="help">Not sure what to choose? Write to us on WhatsApp and we will help you:<br>
<a href="https://wa.me/6282266999965" target="_blank" rel="noopener">Ubud · +62 822 6699 9965</a> · <a href="https://wa.me/6281337709190" target="_blank" rel="noopener">Sanur · +62 813 3770 9190</a></div>
<script>
(function(){
var root=document.getElementById('tfshop');if(!root){return}
var q=root.querySelector('#tfs-q'),cards=[].slice.call(root.querySelectorAll('.card')),cnt=root.querySelector('#tfs-count'),none=root.querySelector('#tfs-none');
var st={q:'',cat:'',salon:''};
function apply(){
var n=0;
cards.forEach(function(c){
var ok=true;
if(st.cat){ok=c.getAttribute('data-cat')===st.cat}
if(ok){if(st.salon){ok=(' '+c.getAttribute('data-salons')+' ').indexOf(' '+st.salon+' ')>-1||c.getAttribute('data-salons')==='all'}}
if(ok){if(st.q){ok=c.getAttribute('data-text').indexOf(st.q)>-1}}
c.hidden=!ok;
[].slice.call(c.querySelectorAll('.buy a')).forEach(function(a){var s=a.getAttribute('data-salon');a.hidden=st.salon?(s!==st.salon?(s!=='all'):false):false});
if(ok){n++}
});
cnt.textContent=n+(n===1?' treatment':' treatments');none.style.display=n?'none':'block';
}
q.addEventListener('input',function(){st.q=q.value.trim().toLowerCase();apply()});
function group(sel,key){[].slice.call(root.querySelectorAll(sel)).forEach(function(b){b.addEventListener('click',function(){[].slice.call(root.querySelectorAll(sel)).forEach(function(x){x.classList.remove('on')});b.classList.add('on');st[key]=b.getAttribute(key==='cat'?'data-cat':'data-salon');apply()})})}
group('.chips button','cat');group('.salon button','salon');
var h=(location.hash||'').replace('#','');if(h==='ubud'||h==='sanur'){var b=root.querySelector('.salon button[data-salon="'+h+'"]');if(b){b.click()}}
apply();
})();
</script>
</div>
	<?php
	return ob_get_clean();
}
add_shortcode( 'thefaces_shop', 'tf_shop_shortcode' );

/** Create the page once. */
function tf_shop_activate() {
	if ( get_page_by_path( 'prepay-treatments' ) ) {
		return;
	}
	wp_insert_post(
		array(
			'post_type'    => 'page',
			'post_status'  => 'publish',
			'post_title'   => 'Prepay a treatment',
			'post_name'    => 'prepay-treatments',
			'post_content' => '<!-- wp:shortcode -->[thefaces_shop]<!-- /wp:shortcode -->',
		)
	);
}
register_activation_hook( __FILE__, 'tf_shop_activate' );

/** Also create the page if the plugin was activated another way (replace upload, bulk activation). */
function tf_shop_ensure_page() {
	if ( current_user_can( 'manage_options' ) && ! get_option( 'tf_shop_page_ok' ) ) {
		tf_shop_activate();
		update_option( 'tf_shop_page_ok', 1, false );
		flush_rewrite_rules( false );
	}
}
add_action( 'admin_init', 'tf_shop_ensure_page' );
