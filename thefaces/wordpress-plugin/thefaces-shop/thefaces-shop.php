<?php
/**
 * Plugin Name: THE FACES · Treatments shop page
 * Description: Luxury spa-menu page to find and prepay THE FACES treatments, with the THE FACES header and footer, descriptions in 9 languages, search, category and salon filters, motion and optional video per treatment. Page /prepay-treatments/ (shortcode [thefaces_shop]). /tienda/ redirects here.
 * Version:     1.2.2
 * Author:      THE FACES
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'TF_SHOP_VER', '1.2.2' );
define( 'TF_SHOP_URL', plugin_dir_url( __FILE__ ) );
define( 'TF_SHOP_DIR', plugin_dir_path( __FILE__ ) );

function tf_shop_cat_order() {
	return array( 'Face massage', 'Air kiss & foam', 'Head spa & hair', 'Cleansing & care', 'Five elements', 'Packages', 'For couples', 'For men', 'Body, feet & legs' );
}

function tf_shop_price( $n ) {
	return number_format( (float) $n, 0, '.', ' ' );
}

function tf_shop_i18n() {
	static $d = null;
	if ( null === $d ) {
		$f = TF_SHOP_DIR . 'assets/i18n.json';
		$d = file_exists( $f ) ? json_decode( file_get_contents( $f ), true ) : array();
	}
	return is_array( $d ) ? $d : array();
}

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
	$items = array();
	foreach ( wc_get_products( array( 'status' => 'publish', 'limit' => -1 ) ) as $p ) {
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
				$buy[ $salon ? $salon : 'all' ] = array( 'price' => $v->get_price(), 'url' => add_query_arg( $args, wc_get_cart_url() ) );
			}
		} elseif ( $p->is_purchasable() ) {
			$buy['all'] = array( 'price' => $p->get_price(), 'url' => add_query_arg( 'add-to-cart', $p->get_id(), wc_get_cart_url() ) );
		}
		if ( ! $buy ) {
			continue;
		}
		ksort( $buy );
		$items[] = array(
			'sku'   => $p->get_sku(),
			'name'  => $p->get_name(),
			'url'   => get_permalink( $p->get_id() ),
			'cat'   => $cat,
			'img'   => $p->get_image_id() ? wp_get_attachment_image_url( $p->get_image_id(), 'medium' ) : '',
			'video' => esc_url_raw( (string) get_post_meta( $p->get_id(), '_tf_video', true ) ),
			'short' => trim( preg_replace( '/\s*Duration:.*$/s', '', wp_strip_all_tags( $p->get_short_description() ) ) ),
			'dur'   => $p->get_attribute( 'Duration' ),
			'buy'   => $buy,
		);
	}
	return $items;
}

function tf_shop_shortcode( $atts ) {
	$atts  = shortcode_atts( array( 'hero' => '0' ), $atts, 'thefaces_shop' );
	$items = tf_shop_data();
	if ( ! $items ) {
		return '<p style="padding:140px 20px;text-align:center">Treatments will appear here soon. Book on WhatsApp: Ubud +62 822 6699 9965 · Sanur +62 813 3770 9190.</p>';
	}
	$order  = tf_shop_cat_order();
	$rank   = function ( $c ) use ( $order ) {
		$i = array_search( $c, $order, true );
		return false === $i ? 99 : $i;
	};
	$groups = array();
	foreach ( $items as $it ) {
		$groups[ $it['cat'] ][] = $it;
	}
	uksort(
		$groups,
		function ( $a, $b ) use ( $rank ) {
			return $rank( $a ) - $rank( $b );
		}
	);
	foreach ( $groups as &$g ) {
		usort(
			$g,
			function ( $a, $b ) {
				return min( wp_list_pluck( $a['buy'], 'price' ) ) - min( wp_list_pluck( $b['buy'], 'price' ) );
			}
		);
	}
	unset( $g );
	$i18n  = tf_shop_i18n();
	$descs = array();
	foreach ( $items as $it ) {
		if ( isset( $i18n['desc'][ $it['sku'] ] ) ) {
			$descs[ $it['sku'] ] = $i18n['desc'][ $it['sku'] ];
		}
	}
	$hero_video = defined( 'TF_SPA_URL' ) ? TF_SPA_URL . 'assets/media/hero-1280.mp4' : '';
	$hero_img   = TF_SHOP_URL . 'assets/img/headspa-pool-2.jpg';

	ob_start();
	?>
<div id="tfshop" class="<?php echo '1' === $atts['hero'] ? 'with-hero' : ''; ?>">
<style>
#tfshop{--g:#B08D45;--g2:#E7C67A;--ink:#16130f;--mut:#7d776c;--line:#ece6db;--bg:#f8f5ef;font-family:Montserrat,system-ui,sans-serif;color:var(--ink);background:#fff}
#tfshop *{box-sizing:border-box}
#tfshop a{text-decoration:none}
#tfshop .hero{position:relative;overflow:hidden;color:#fff;text-align:center;padding:170px 20px 90px;background:#14110d center/cover no-repeat;min-height:78vh;display:flex;flex-direction:column;justify-content:center}
#tfshop .hero video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
#tfshop .hero:after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(12,10,8,.35),rgba(12,10,8,.8))}
#tfshop .hero>*:not(video){position:relative;z-index:1}
#tfshop .eye{font-size:11px;letter-spacing:.34em;text-transform:uppercase;color:var(--g2);font-weight:500;margin:0 0 20px}
#tfshop .hero h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(42px,7vw,84px);line-height:1;margin:0 0 22px;color:#fff;letter-spacing:.02em}
#tfshop .hero h1 em{font-style:italic;color:var(--g2)}
#tfshop .lead{max-width:620px;margin:0 auto;font-weight:300;font-size:16px;line-height:1.8;color:rgba(255,255,255,.88)}
#tfshop .steps{display:flex;justify-content:center;gap:34px;flex-wrap:wrap;list-style:none;margin:40px 0 0;padding:0;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.8);font-weight:400}
#tfshop .steps b{display:inline-block;width:26px;height:26px;line-height:25px;border:1px solid var(--g2);border-radius:50%;color:var(--g2);font-weight:400;margin-right:10px;font-family:'Cormorant Garamond',serif;font-size:15px;text-transform:none}
#tfshop .scroll{position:absolute;bottom:26px;left:50%;transform:translateX(-50%);width:1px;height:46px;background:linear-gradient(var(--g2),transparent);z-index:1;animation:tfs-drop 2.4s ease-in-out infinite}
@keyframes tfs-drop{0%{opacity:0;transform:translate(-50%,-12px)}50%{opacity:1}100%{opacity:0;transform:translate(-50%,12px)}}
#tfshop .hero .reveal{animation:tfs-up 1.2s cubic-bezier(.2,.7,.2,1) both}
#tfshop .hero .reveal:nth-child(3){animation-delay:.15s}#tfshop .hero .reveal:nth-child(4){animation-delay:.3s}#tfshop .hero .reveal:nth-child(5){animation-delay:.45s}
@keyframes tfs-up{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
#tfshop .bar{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.96);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
#tfshop.with-hero .bar{top:64px}
body.admin-bar #tfshop .bar{top:32px}body.admin-bar #tfshop.with-hero .bar{top:96px}
#tfshop .in{max-width:1100px;margin:0 auto;padding:0 22px}
#tfshop .row1{display:flex;gap:12px;align-items:center;padding:16px 0 8px;flex-wrap:wrap}
#tfshop input[type=search]{flex:1 1 240px;min-width:0;height:46px;padding:0 20px;border:1px solid var(--line);border-radius:30px;font:inherit;font-size:14px;background:var(--bg);color:var(--ink);outline:none;transition:border-color .3s}
#tfshop input[type=search]:focus{border-color:var(--g)}
#tfshop .seg{display:inline-flex;border:1px solid var(--line);border-radius:30px;padding:3px;background:#fff}
#tfshop .seg button{border:0;background:transparent;border-radius:30px;padding:9px 16px;font:inherit;font-size:13px;cursor:pointer;color:var(--mut);transition:all .3s}
#tfshop .seg button.on{background:var(--ink);color:#fff}
#tfshop .langs{display:flex;gap:2px}
#tfshop .langs button{border:0;background:transparent;font:inherit;font-size:11px;letter-spacing:.1em;padding:8px 6px;cursor:pointer;color:var(--mut)}
#tfshop .langs button.on{color:var(--g);font-weight:600}
#tfshop .chips{display:flex;gap:4px;overflow-x:auto;padding:0 0 12px;scrollbar-width:none}
#tfshop .chips::-webkit-scrollbar{display:none}
#tfshop .chips button{flex:0 0 auto;border:0;background:transparent;border-bottom:1px solid transparent;padding:8px 11px;font:inherit;font-size:12px;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;color:var(--mut);white-space:nowrap;transition:all .3s}
#tfshop .chips button.on,#tfshop .chips button:hover{color:var(--ink);border-bottom-color:var(--g)}
#tfshop .list{max-width:1100px;margin:0 auto;padding:10px 22px 20px}
#tfshop section.grp{padding:46px 0 8px}
#tfshop section.grp>h2{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:42px;margin:0 0 10px;color:var(--ink);display:flex;align-items:baseline;gap:14px}
#tfshop section.grp>h2:after{content:"";flex:1;height:1px;background:linear-gradient(90deg,var(--g),transparent);opacity:.5;align-self:center}
#tfshop section.grp>h2 small{font-family:Montserrat,sans-serif;font-size:11px;letter-spacing:.24em;color:var(--g)}
#tfshop .item{display:grid;grid-template-columns:110px 1fr auto;gap:28px;align-items:center;padding:26px 0;border-top:1px solid var(--line);opacity:0;transform:translateY(18px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.2,1)}
#tfshop .item.in-view{opacity:1;transform:none}
#tfshop .media{position:relative;width:110px;height:110px;border-radius:50%;overflow:hidden;display:block;background:var(--bg);box-shadow:0 0 0 1px var(--line),0 0 0 5px #fff,0 0 0 6px rgba(176,141,69,.25)}
#tfshop .media img,#tfshop .media video{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1.4s cubic-bezier(.2,.7,.2,1)}
#tfshop .item:hover .media img,#tfshop .item:hover .media video{transform:scale(1.12)}
#tfshop .item h3{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:27px;line-height:1.12;margin:0 0 6px}
#tfshop .item h3 a{color:var(--ink);transition:color .3s}
#tfshop .item h3 a:hover{color:var(--g)}
#tfshop .meta{font-size:11px;letter-spacing:.18em;color:var(--g);text-transform:uppercase;margin:0 0 8px}
#tfshop .sd{font-size:14px;font-weight:300;line-height:1.65;color:#5c574e;margin:0;max-width:600px}
#tfshop .act{display:flex;flex-direction:column;align-items:flex-end;gap:12px;min-width:230px}
#tfshop .price{font-family:'Cormorant Garamond',Georgia,serif;font-size:28px;font-weight:400;white-space:nowrap;line-height:1}
#tfshop .price small{font-family:Montserrat,sans-serif;font-size:10px;color:var(--mut);letter-spacing:.16em;margin-left:5px}
#tfshop .price .fr{font-family:Montserrat,sans-serif;font-size:10px;letter-spacing:.16em;color:var(--mut);text-transform:uppercase;margin-right:6px}
#tfshop .ctl{display:flex;gap:8px;align-items:center}
#tfshop .pick{display:inline-flex;border:1px solid var(--line);border-radius:30px;padding:2px}
#tfshop .pick button{border:0;background:transparent;border-radius:30px;padding:7px 13px;font:inherit;font-size:12px;cursor:pointer;color:var(--mut);transition:all .3s}
#tfshop .pick button.on{background:var(--bg);color:var(--ink);font-weight:600}
#tfshop .only{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--mut);padding:0 6px}
#tfshop .book{position:relative;overflow:hidden;display:inline-block;background:var(--ink);color:#fff;border-radius:30px;padding:12px 26px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;font-weight:500;transition:color .4s}
#tfshop .book:before{content:"";position:absolute;inset:0;background:var(--g);transform:translateX(-101%);transition:transform .5s cubic-bezier(.2,.7,.2,1)}
#tfshop .book:hover:before{transform:none}
#tfshop .book span{position:relative}
#tfshop .none{display:none;text-align:center;padding:60px 10px;color:var(--mut)}
#tfshop .help{max-width:1100px;margin:30px auto 80px;padding:0 22px}
#tfshop .help div{text-align:center;background:var(--ink);color:rgba(255,255,255,.85);border-radius:20px;padding:40px 22px;line-height:1.9;font-size:14px;font-weight:300}
#tfshop .help b{display:block;font-family:'Cormorant Garamond',serif;font-weight:300;font-size:30px;color:#fff;margin-bottom:6px}
#tfshop .help a{color:var(--g2);font-weight:500;border-bottom:1px solid rgba(231,198,122,.4)}
#tfshop [hidden]{display:none!important}
@media(prefers-reduced-motion:reduce){#tfshop .item{opacity:1;transform:none;transition:none}#tfshop .hero .reveal,#tfshop .scroll{animation:none}}
@media(max-width:760px){
#tfshop .hero{padding:130px 18px 70px;min-height:70vh}
#tfshop .steps{gap:14px 20px;font-size:11px}
#tfshop.with-hero .bar{top:56px}
#tfshop .item{grid-template-columns:76px 1fr;gap:16px;padding:22px 0}
#tfshop .media{width:76px;height:76px}
#tfshop .item h3{font-size:23px}
#tfshop .act{grid-column:1/-1;flex-direction:row;justify-content:space-between;align-items:center;min-width:0;flex-wrap:wrap}
#tfshop .price{font-size:24px}
#tfshop section.grp>h2{font-size:32px}
#tfshop .langs{width:100%;justify-content:center;flex-wrap:wrap}
}
</style>
	<?php if ( '1' === $atts['hero'] ) : ?>
<div class="hero" style="background-image:url('<?php echo esc_url( $hero_img ); ?>')">
		<?php if ( $hero_video ) : ?>
<video autoplay muted loop playsinline preload="metadata" poster="<?php echo esc_url( $hero_img ); ?>"><source src="<?php echo esc_url( $hero_video ); ?>" type="video/mp4"></video>
		<?php endif; ?>
<p class="eye reveal" data-t="eye">THE FACES · Ubud &amp; Sanur</p>
<h1 class="reveal" data-t="h1">Prepay your <em>ritual</em></h1>
<p class="lead reveal" data-t="lead">Choose your treatment and your salon, pay online, then pick the date that suits you. Valid for 6 months.</p>
<ol class="steps reveal"><li><b>1</b><span data-t="s1">Choose a treatment</span></li><li><b>2</b><span data-t="s2">Choose Ubud or Sanur</span></li><li><b>3</b><span data-t="s3">Pay online</span></li><li><b>4</b><span data-t="s4">Pick your date</span></li></ol>
<span class="scroll" aria-hidden="true"></span>
</div>
	<?php endif; ?>
<div class="bar"><div class="in">
<div class="row1">
<input type="search" id="tfs-q" placeholder="Search a treatment…" data-tp="ph" aria-label="Search">
<div class="seg" role="group" aria-label="Salon"><button type="button" class="on" data-salon="" data-t="all_s">All salons</button><button type="button" data-salon="ubud">Ubud</button><button type="button" data-salon="sanur">Sanur</button></div>
<div class="langs" role="group" aria-label="Language">
	<?php foreach ( array( 'en', 'ru', 'es', 'de', 'fr', 'uk', 'id', 'th', 'ja' ) as $l ) : ?>
<button type="button" data-lang="<?php echo esc_attr( $l ); ?>"><?php echo esc_html( strtoupper( $l ) ); ?></button>
	<?php endforeach; ?>
</div>
</div>
<div class="chips" role="group" aria-label="Category"><button type="button" class="on" data-cat="" data-t="all_t">All treatments</button>
	<?php foreach ( array_keys( $groups ) as $c ) : ?>
<button type="button" data-cat="<?php echo esc_attr( sanitize_title( $c ) ); ?>" data-c="<?php echo esc_attr( $c ); ?>"><?php echo esc_html( $c ); ?></button>
	<?php endforeach; ?>
</div>
</div></div>
<div class="list">
	<?php foreach ( $groups as $c => $list ) : ?>
<section class="grp" data-cat="<?php echo esc_attr( sanitize_title( $c ) ); ?>">
<h2><span data-c="<?php echo esc_attr( $c ); ?>"><?php echo esc_html( $c ); ?></span><small class="n"><?php echo count( $list ); ?></small></h2>
		<?php
		foreach ( $list as $it ) :
			$keys  = array_keys( $it['buy'] );
			$first = $it['buy'][ $keys[0] ];
			$min   = min( wp_list_pluck( $it['buy'], 'price' ) );
			$same  = count( array_unique( wp_list_pluck( $it['buy'], 'price' ) ) ) === 1;
			$where = implode( ' & ', array_map( 'ucfirst', array_diff( $keys, array( 'all' ) ) ) );
			?>
<article class="item" data-sku="<?php echo esc_attr( $it['sku'] ); ?>" data-salons="<?php echo esc_attr( implode( ' ', $keys ) ); ?>" data-text="<?php echo esc_attr( mb_strtolower( $it['name'] . ' ' . $c . ' ' . $it['short'] ) ); ?>">
<a class="media" href="<?php echo esc_url( $it['url'] ); ?>" aria-label="<?php echo esc_attr( $it['name'] ); ?>">
			<?php if ( $it['video'] ) : ?>
<video muted loop playsinline preload="none" poster="<?php echo esc_url( $it['img'] ); ?>" data-src="<?php echo esc_url( $it['video'] ); ?>"></video>
			<?php else : ?>
<img src="<?php echo esc_url( $it['img'] ); ?>" alt="" loading="lazy">
			<?php endif; ?>
</a>
<div>
<p class="meta"><?php echo esc_html( trim( $it['dur'] . ( $it['dur'] && $where ? ' · ' : '' ) . $where ) ); ?></p>
<h3><a href="<?php echo esc_url( $it['url'] ); ?>"><?php echo esc_html( $it['name'] ); ?></a></h3>
<p class="sd"><?php echo esc_html( isset( $descs[ $it['sku'] ]['en'] ) ? $descs[ $it['sku'] ]['en'] : $it['short'] ); ?></p>
</div>
<div class="act">
<div class="price" data-price><?php echo ( $same ? '' : '<span class="fr" data-t="from">from</span>' ) . esc_html( tf_shop_price( $min ) ); ?><small>IDR</small></div>
<div class="ctl">
			<?php if ( count( $keys ) > 1 ) : ?>
<div class="pick" role="group" aria-label="Salon">
				<?php foreach ( $it['buy'] as $s => $b ) : ?>
<button type="button" class="<?php echo $s === $keys[0] ? 'on' : ''; ?>" data-s="<?php echo esc_attr( $s ); ?>" data-url="<?php echo esc_url( $b['url'] ); ?>" data-p="<?php echo esc_attr( tf_shop_price( $b['price'] ) ); ?>"><?php echo esc_html( ucfirst( $s ) ); ?></button>
				<?php endforeach; ?>
</div>
			<?php elseif ( 'all' !== $keys[0] ) : ?>
<span class="only" data-only="<?php echo esc_attr( ucfirst( $keys[0] ) ); ?>"><?php echo esc_html( ucfirst( $keys[0] ) ); ?> only</span>
			<?php endif; ?>
<a class="book" href="<?php echo esc_url( $first['url'] ); ?>" rel="nofollow"><span data-t="book">Book</span></a>
</div>
</div>
</article>
		<?php endforeach; ?>
</section>
	<?php endforeach; ?>
<div class="none" id="tfs-none" data-t="none">No treatment matches your search.</div>
</div>
<div class="help"><div><b data-t="help_t">Not sure which ritual to choose?</b><span data-t="help">Our team will help you on WhatsApp.</span><br>
<a href="https://wa.me/6282266999965" target="_blank" rel="noopener">Ubud · +62 822 6699 9965</a> &nbsp;·&nbsp; <a href="https://wa.me/6281337709190" target="_blank" rel="noopener">Sanur · +62 813 3770 9190</a></div></div>
<script type="application/json" id="tfs-desc"><?php echo wp_json_encode( $descs ); ?></script>
<script>
(function(){
var root=document.getElementById('tfshop');if(!root){return}
var UI={
en:{eye:'THE FACES · Ubud & Sanur',h1:'Prepay your <em>ritual</em>',lead:'Choose your treatment and your salon, pay online, then pick the date that suits you. Valid for 6 months.',s1:'Choose a treatment',s2:'Choose Ubud or Sanur',s3:'Pay online',s4:'Pick your date',ph:'Search a treatment…',all_s:'All salons',all_t:'All treatments',from:'from',only:'{s} only',book:'Book',none:'No treatment matches your search.',help_t:'Not sure which ritual to choose?',help:'Our team will help you on WhatsApp.',cats:{}},
ru:{eye:'THE FACES · Убуд и Санур',h1:'Оплатите <em>ритуал</em> заранее',lead:'Выберите процедуру и салон, оплатите онлайн, а затем удобную дату. Действует 6 месяцев.',s1:'Выберите процедуру',s2:'Убуд или Санур',s3:'Оплата онлайн',s4:'Выберите дату',ph:'Поиск процедуры…',all_s:'Все салоны',all_t:'Все процедуры',from:'от',only:'Только {s}',book:'Купить',none:'Ничего не найдено.',help_t:'Не знаете, что выбрать?',help:'Наша команда поможет в WhatsApp.',cats:{'Face massage':'Массаж лица','Air kiss & foam':'Air kiss и пена','Head spa & hair':'Хэд-спа и волосы','Cleansing & care':'Чистка и уход','Five elements':'Пять стихий','Packages':'Пакеты','For couples':'Для пар','For men':'Для мужчин','Body, feet & legs':'Тело, стопы и ноги'}},
es:{eye:'THE FACES · Ubud y Sanur',h1:'Prepaga tu <em>ritual</em>',lead:'Elige tu tratamiento y tu salón, paga online y después escoge la fecha que prefieras. Válido 6 meses.',s1:'Elige un tratamiento',s2:'Ubud o Sanur',s3:'Paga online',s4:'Elige la fecha',ph:'Busca un tratamiento…',all_s:'Todos los salones',all_t:'Todos los tratamientos',from:'desde',only:'Solo {s}',book:'Reservar',none:'Ningún tratamiento coincide.',help_t:'¿No sabes cuál elegir?',help:'Nuestro equipo te ayuda por WhatsApp.',cats:{'Face massage':'Masaje facial','Air kiss & foam':'Air kiss y espuma','Head spa & hair':'Head spa y cabello','Cleansing & care':'Limpieza y cuidado','Five elements':'Cinco elementos','Packages':'Paquetes','For couples':'Para parejas','For men':'Para hombres','Body, feet & legs':'Cuerpo, pies y piernas'}},
de:{eye:'THE FACES · Ubud & Sanur',h1:'Ihr <em>Ritual</em> im Voraus',lead:'Wählen Sie Behandlung und Salon, zahlen Sie online und wählen Sie dann Ihren Termin. 6 Monate gültig.',s1:'Behandlung wählen',s2:'Ubud oder Sanur',s3:'Online zahlen',s4:'Termin wählen',ph:'Behandlung suchen…',all_s:'Alle Salons',all_t:'Alle Behandlungen',from:'ab',only:'Nur {s}',book:'Buchen',none:'Keine Behandlung gefunden.',help_t:'Unsicher, was Sie wählen sollen?',help:'Unser Team hilft Ihnen per WhatsApp.',cats:{'Face massage':'Gesichtsmassage','Air kiss & foam':'Air kiss & Schaum','Head spa & hair':'Head Spa & Haar','Cleansing & care':'Reinigung & Pflege','Five elements':'Fünf Elemente','Packages':'Pakete','For couples':'Für Paare','For men':'Für Männer','Body, feet & legs':'Körper, Füße & Beine'}},
fr:{eye:'THE FACES · Ubud & Sanur',h1:'Offrez-vous votre <em>rituel</em>',lead:'Choisissez votre soin et votre salon, payez en ligne, puis la date qui vous convient. Valable 6 mois.',s1:'Choisissez un soin',s2:'Ubud ou Sanur',s3:'Payez en ligne',s4:'Choisissez la date',ph:'Rechercher un soin…',all_s:'Tous les salons',all_t:'Tous les soins',from:'dès',only:'{s} uniquement',book:'Réserver',none:'Aucun soin ne correspond.',help_t:'Vous hésitez ?',help:'Notre équipe vous aide sur WhatsApp.',cats:{'Face massage':'Massage du visage','Air kiss & foam':'Air kiss & mousse','Head spa & hair':'Head spa & cheveux','Cleansing & care':'Nettoyage & soin','Five elements':'Cinq éléments','Packages':'Forfaits','For couples':'En duo','For men':'Pour hommes','Body, feet & legs':'Corps, pieds & jambes'}},
uk:{eye:'THE FACES · Убуд і Санур',h1:'Оплатіть <em>ритуал</em> заздалегідь',lead:'Оберіть процедуру та салон, оплатіть онлайн, а потім зручну дату. Діє 6 місяців.',s1:'Оберіть процедуру',s2:'Убуд або Санур',s3:'Оплата онлайн',s4:'Оберіть дату',ph:'Пошук процедури…',all_s:'Усі салони',all_t:'Усі процедури',from:'від',only:'Лише {s}',book:'Купити',none:'Нічого не знайдено.',help_t:'Не знаєте, що обрати?',help:'Наша команда допоможе у WhatsApp.',cats:{'Face massage':'Масаж обличчя','Air kiss & foam':'Air kiss і піна','Head spa & hair':'Хед-спа і волосся','Cleansing & care':'Чистка та догляд','Five elements':'Пʼять стихій','Packages':'Пакети','For couples':'Для пар','For men':'Для чоловіків','Body, feet & legs':'Тіло, стопи та ноги'}},
id:{eye:'THE FACES · Ubud & Sanur',h1:'Bayar <em>ritual</em> Anda di muka',lead:'Pilih perawatan dan salon, bayar online, lalu pilih tanggal yang Anda inginkan. Berlaku 6 bulan.',s1:'Pilih perawatan',s2:'Ubud atau Sanur',s3:'Bayar online',s4:'Pilih tanggal',ph:'Cari perawatan…',all_s:'Semua salon',all_t:'Semua perawatan',from:'mulai',only:'Hanya {s}',book:'Pesan',none:'Tidak ada perawatan yang cocok.',help_t:'Bingung memilih?',help:'Tim kami siap membantu lewat WhatsApp.',cats:{'Face massage':'Pijat wajah','Air kiss & foam':'Air kiss & busa','Head spa & hair':'Head spa & rambut','Cleansing & care':'Pembersihan & perawatan','Five elements':'Lima elemen','Packages':'Paket','For couples':'Untuk pasangan','For men':'Untuk pria','Body, feet & legs':'Tubuh, kaki & tungkai'}},
th:{eye:'THE FACES · อูบุด และ ซานูร์',h1:'ชำระ<em>พิธีกรรม</em>ล่วงหน้า',lead:'เลือกทรีตเมนต์และสาขา ชำระเงินออนไลน์ แล้วเลือกวันที่สะดวก ใช้ได้ 6 เดือน',s1:'เลือกทรีตเมนต์',s2:'อูบุด หรือ ซานูร์',s3:'ชำระออนไลน์',s4:'เลือกวันที่',ph:'ค้นหาทรีตเมนต์…',all_s:'ทุกสาขา',all_t:'ทรีตเมนต์ทั้งหมด',from:'เริ่มต้น',only:'เฉพาะ {s}',book:'จอง',none:'ไม่พบทรีตเมนต์ที่ตรงกัน',help_t:'ยังไม่แน่ใจว่าจะเลือกอะไร?',help:'ทีมงานช่วยคุณได้ทาง WhatsApp',cats:{'Face massage':'นวดหน้า','Air kiss & foam':'Air kiss และโฟม','Head spa & hair':'เฮดสปาและเส้นผม','Cleansing & care':'ทำความสะอาดและดูแลผิว','Five elements':'ธาตุทั้งห้า','Packages':'แพ็กเกจ','For couples':'สำหรับคู่รัก','For men':'สำหรับผู้ชาย','Body, feet & legs':'ร่างกาย เท้า และขา'}},
ja:{eye:'THE FACES · ウブド & サヌール',h1:'<em>リチュアル</em>を事前予約',lead:'施術とサロンを選び、オンラインで支払い、ご都合のよい日をお選びください。有効期限6か月。',s1:'施術を選ぶ',s2:'ウブドまたはサヌール',s3:'オンライン決済',s4:'日付を選ぶ',ph:'施術を検索…',all_s:'すべてのサロン',all_t:'すべての施術',from:'から',only:'{s}のみ',book:'予約',none:'該当する施術がありません。',help_t:'どれを選べばよいか迷ったら',help:'WhatsAppでチームがご案内します。',cats:{'Face massage':'フェイシャルマッサージ','Air kiss & foam':'Air kiss & 泡','Head spa & hair':'ヘッドスパ & ヘア','Cleansing & care':'クレンジング & ケア','Five elements':'五元素','Packages':'パッケージ','For couples':'カップル','For men':'メンズ','Body, feet & legs':'ボディ・足・脚'}}
};
var D={};try{D=JSON.parse(document.getElementById('tfs-desc').textContent)}catch(e){}
function $$(s,el){return [].slice.call((el||root).querySelectorAll(s))}
var st={q:'',cat:'',salon:'',lang:'en'};
function setLang(l){if(!UI[l]){l='en'}st.lang=l;var u=UI[l];
$$('[data-t]').forEach(function(el){var k=el.getAttribute('data-t');if(u[k]){if(k==='h1'){el.innerHTML=u[k]}else{el.textContent=u[k]}}});
$$('[data-tp]').forEach(function(el){el.setAttribute('placeholder',u[el.getAttribute('data-tp')])});
$$('[data-only]').forEach(function(el){el.textContent=u.only.replace('{s}',el.getAttribute('data-only'))});
$$('[data-c]').forEach(function(el){var c=el.getAttribute('data-c');el.textContent=(u.cats&&u.cats[c])||c});
$$('.item').forEach(function(it){var d=D[it.getAttribute('data-sku')];if(d){it.querySelector('.sd').textContent=d[l]||d.en}});
$$('.langs button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-lang')===l)});
root.setAttribute('lang',l);try{sessionStorage.setItem('tfs_lang',l)}catch(e){}}
function choose(item,s){var bs=$$('.pick button',item);if(!bs.length){return}var t=null;bs.forEach(function(b){if(b.getAttribute('data-s')===s){t=b}});if(!t){t=bs[0]}
bs.forEach(function(b){b.classList.toggle('on',b===t)});item.querySelector('.book').setAttribute('href',t.getAttribute('data-url'));
item.querySelector('[data-price]').innerHTML=t.getAttribute('data-p')+'<small>IDR</small>'}
function apply(){var total=0;
$$('section.grp').forEach(function(sec){var n=0,catOk=!st.cat||sec.getAttribute('data-cat')===st.cat;
$$('.item',sec).forEach(function(it){var ok=catOk,ss=' '+it.getAttribute('data-salons')+' ';
if(ok){if(st.salon){ok=ss.indexOf(' '+st.salon+' ')>-1||ss.indexOf(' all ')>-1}}
if(ok){if(st.q){ok=(it.getAttribute('data-text')+' '+it.querySelector('.sd').textContent.toLowerCase()).indexOf(st.q)>-1}}
it.hidden=!ok;if(ok){n++;if(st.salon){choose(it,st.salon)}}});
sec.hidden=!n;sec.querySelector('.n').textContent=n;total+=n});
document.getElementById('tfs-none').style.display=total?'none':'block'}
$$('.pick button').forEach(function(b){b.addEventListener('click',function(){choose(b.closest('.item'),b.getAttribute('data-s'))})});
var q=root.querySelector('#tfs-q');q.addEventListener('input',function(){st.q=q.value.trim().toLowerCase();apply()});
function group(sel,key,attr){$$(sel).forEach(function(b){b.addEventListener('click',function(){$$(sel).forEach(function(x){x.classList.remove('on')});b.classList.add('on');st[key]=b.getAttribute(attr);apply()})})}
group('.chips button','cat','data-cat');group('.seg button','salon','data-salon');
$$('.langs button').forEach(function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-lang'))})});
/* language: ?lang= > this visit > device language */
var l=null,m=location.search.match(/[?&]lang=([a-z]{2})/);if(m){l=m[1]}
if(!l){try{l=sessionStorage.getItem('tfs_lang')}catch(e){}}
if(!l){var nl=(navigator.languages||[navigator.language||'en']);for(var i=0;i<nl.length;i++){var c=String(nl[i]).slice(0,2).toLowerCase();if(UI[c]){l=c;break}}}
setLang(l||'en');
/* motion: reveal rows, play treatment videos when visible */
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){var it=e.target;if(e.isIntersecting){it.classList.add('in-view');var v=it.querySelector('video[data-src]');if(v){if(!v.src){v.src=v.getAttribute('data-src')}var p=v.play();if(p){p.catch(function(){})}}}else{var v2=it.querySelector('video[data-src]');if(v2){v2.pause()}}})},{rootMargin:'0px 0px -8% 0px'});$$('.item').forEach(function(it){io.observe(it)})}else{$$('.item').forEach(function(it){it.classList.add('in-view')})}
var h=(location.hash||'').replace('#','');if(h==='ubud'||h==='sanur'){var sb=root.querySelector('.seg button[data-salon="'+h+'"]');if(sb){sb.click()}}
apply();
})();
</script>
</div>
	<?php
	return ob_get_clean();
}
add_shortcode( 'thefaces_shop', 'tf_shop_shortcode' );

/* ---------- Page on the THE FACES template ---------- */

function tf_shop_activate() {
	$page = get_page_by_path( 'prepay-treatments' );
	$id   = $page ? $page->ID : wp_insert_post(
		array(
			'post_type'   => 'page',
			'post_status' => 'publish',
			'post_title'  => 'Prepay a treatment',
			'post_name'   => 'prepay-treatments',
		)
	);
	if ( $id && ! is_wp_error( $id ) ) {
		$canvas  = function_exists( 'tf_spa_file' );
		$content = $canvas ? '[thefaces block="header"][thefaces_shop hero="1"][thefaces block="footer"]' : '[thefaces_shop]';
		wp_update_post( array( 'ID' => $id, 'post_content' => $content ) );
		if ( $canvas ) {
			update_post_meta( $id, '_wp_page_template', 'thefaces-canvas' );
		}
	}
}
register_activation_hook( __FILE__, 'tf_shop_activate' );

function tf_shop_ensure_page() {
	if ( current_user_can( 'manage_options' ) && TF_SHOP_VER !== get_option( 'tf_shop_page_ver' ) ) {
		tf_shop_activate();
		update_option( 'tf_shop_page_ver', TF_SHOP_VER, false );
	}
}
add_action( 'admin_init', 'tf_shop_ensure_page' );

/** THE FACES styles and scripts on the shop page (THE FACES Spa only loads them on its own pages). */
function tf_shop_assets() {
	if ( ! is_page( 'prepay-treatments' ) || ! defined( 'TF_SPA_URL' ) ) {
		return;
	}
	$ver = defined( 'TF_SPA_VERSION' ) ? TF_SPA_VERSION : TF_SHOP_VER;
	wp_enqueue_style( 'thefaces-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Montserrat:wght@200;300;400;500;600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap', array(), null );
	wp_enqueue_style( 'thefaces-spa', TF_SPA_URL . 'assets/thefaces.css', array(), $ver );
	wp_add_inline_style( 'thefaces-spa', 'body.tf-canvas{margin:0;background:#fff}body.admin-bar .tf .top{top:32px}@media (max-width:782px){body.admin-bar .tf .top{top:46px}}' );
	wp_enqueue_script( 'thefaces-spa', TF_SPA_URL . 'assets/thefaces.js', array(), $ver, true );
}
add_action( 'wp_enqueue_scripts', 'tf_shop_assets', 20 );

/* ---------- Video per treatment (product edit screen) ---------- */

function tf_shop_video_box() {
	add_meta_box( 'tf_shop_video', 'THE FACES · Vídeo del tratamiento', 'tf_shop_video_box_html', 'product', 'side' );
}
add_action( 'add_meta_boxes', 'tf_shop_video_box' );

function tf_shop_video_box_html( $post ) {
	wp_nonce_field( 'tf_shop_video', 'tf_shop_video_nonce' );
	echo '<p><input type="url" name="tf_shop_video" value="' . esc_attr( get_post_meta( $post->ID, '_tf_video', true ) ) . '" placeholder="https://…/video.mp4" style="width:100%"></p>';
	echo '<p class="description">Enlace a un vídeo MP4 corto (5–10 s, vertical u horizontal, sin sonido). Súbelo en Medios y pega aquí su URL. Se reproduce en la página de tratamientos en lugar de la foto.</p>';
}

function tf_shop_video_save( $post_id ) {
	if ( ! isset( $_POST['tf_shop_video_nonce'] ) || ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['tf_shop_video_nonce'] ) ), 'tf_shop_video' ) ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	$url = isset( $_POST['tf_shop_video'] ) ? esc_url_raw( wp_unslash( $_POST['tf_shop_video'] ) ) : '';
	update_post_meta( $post_id, '_tf_video', $url );
}
add_action( 'save_post_product', 'tf_shop_video_save' );

/* ---------- /tienda/ goes to the treatments page ---------- */

function tf_shop_redirect_shop() {
	if ( is_admin() || ! function_exists( 'is_shop' ) ) {
		return;
	}
	if ( is_shop() || is_product_category() ) {
		$page = get_page_by_path( 'prepay-treatments' );
		if ( $page ) {
			wp_safe_redirect( get_permalink( $page ), 301 );
			exit;
		}
	}
}
add_action( 'template_redirect', 'tf_shop_redirect_shop' );

function tf_shop_return_url( $url ) {
	$page = get_page_by_path( 'prepay-treatments' );
	return $page ? get_permalink( $page ) : $url;
}
add_filter( 'woocommerce_return_to_shop_redirect', 'tf_shop_return_url' );
add_filter( 'woocommerce_continue_shopping_redirect', 'tf_shop_return_url' );

/* ---------- After payment: book date, time and therapist in Altegio ---------- */

function tf_shop_booking_links() {
	return array(
		'ubud'  => 'https://n831884.alteg.io/company/780725/personal/select-services?o=m-1',
		'sanur' => 'https://n811764.alteg.io/company/762669/personal/select-services?o=m-1',
	);
}

/** Salons of the treatments in an order, with the treatment names. */
function tf_shop_order_salons( $order ) {
	$out = array();
	foreach ( $order->get_items() as $item ) {
		$salon = '';
		foreach ( $item->get_meta_data() as $m ) {
			$d = $m->get_data();
			if ( false !== stripos( (string) $d['key'], 'salon' ) ) {
				$salon = sanitize_title( $d['value'] );
			}
		}
		if ( ! $salon ) {
			$product = $item->get_product();
			if ( $product && $product->is_type( 'variation' ) ) {
				$salon = tf_shop_variation_salon( $product->get_variation_attributes() );
			}
		}
		if ( $salon ) {
			$out[ $salon ][] = $item->get_name();
		}
	}
	return $out;
}

function tf_shop_booking_html( $order, $plain = false ) {
	$links  = tf_shop_booking_links();
	$salons = tf_shop_order_salons( $order );
	if ( ! $salons ) {
		$salons = array( 'ubud' => array(), 'sanur' => array() );
	}
	$wa = array( 'ubud' => '+62 822 6699 9965', 'sanur' => '+62 813 3770 9190' );
	if ( $plain ) {
		$t = "\nCHOOSE YOUR DATE, TIME AND THERAPIST\n";
		foreach ( $salons as $s => $names ) {
			if ( isset( $links[ $s ] ) ) {
				$t .= ucfirst( $s ) . ': ' . $links[ $s ] . ' (WhatsApp ' . $wa[ $s ] . ")\n";
			}
		}
		return $t . "Order number: " . $order->get_order_number() . "\n";
	}
	$h = '<div style="margin:28px 0;padding:26px;border:1px solid #e7dfcf;border-radius:14px;background:#faf7f1;font-family:Montserrat,Arial,sans-serif;color:#16130f">'
		. '<p style="margin:0 0 6px;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#B08D45">Next step</p>'
		. '<p style="margin:0 0 16px;font-size:20px;font-family:Georgia,serif">Choose your date, time and therapist</p>'
		. '<p style="margin:0 0 18px;font-size:14px;line-height:1.6;color:#5c574e">Your treatment is paid. Book the moment that suits you in our online calendar. When you book, mention your order number <strong>#' . esc_html( $order->get_order_number() ) . '</strong>.</p>';
	foreach ( $salons as $s => $names ) {
		if ( ! isset( $links[ $s ] ) ) {
			continue;
		}
		$h .= '<p style="margin:0 0 12px"><a href="' . esc_url( $links[ $s ] ) . '" style="display:inline-block;background:#16130f;color:#ffffff;text-decoration:none;padding:13px 26px;border-radius:30px;font-size:13px;letter-spacing:.12em;text-transform:uppercase">Book in ' . esc_html( ucfirst( $s ) ) . '</a>'
			. ( $names ? '<br><span style="font-size:12px;color:#7d776c">' . esc_html( implode( ' · ', $names ) ) . '</span>' : '' ) . '</p>';
	}
	$h .= '<p style="margin:14px 0 0;font-size:13px;color:#7d776c">Prefer WhatsApp? Ubud ' . esc_html( $wa['ubud'] ) . ' · Sanur ' . esc_html( $wa['sanur'] ) . '</p></div>';
	return $h;
}

/** Thank-you page after checkout. */
function tf_shop_thankyou( $order_id ) {
	$order = wc_get_order( $order_id );
	if ( $order ) {
		echo tf_shop_booking_html( $order ); // phpcs:ignore WordPress.Security.EscapeOutput -- escaped inside.
	}
}
add_action( 'woocommerce_thankyou', 'tf_shop_thankyou', 5 );

/** Order emails to the customer (processing and completed). */
function tf_shop_email_booking( $order, $sent_to_admin, $plain_text, $email ) {
	if ( $sent_to_admin || ! is_object( $email ) || ! in_array( $email->id, array( 'customer_processing_order', 'customer_completed_order', 'customer_on_hold_order' ), true ) ) {
		return;
	}
	echo tf_shop_booking_html( $order, $plain_text ); // phpcs:ignore WordPress.Security.EscapeOutput -- escaped inside.
}
add_action( 'woocommerce_email_after_order_table', 'tf_shop_email_booking', 10, 4 );

/* ---------- Hidden mode: the shop works by direct link (ads), but Google does not index it ---------- */

function tf_shop_is_public() {
	return (bool) get_option( 'tf_shop_public', 0 );
}

/** Is the current request part of the shop (treatments page, products, cart, checkout, account)? */
function tf_shop_is_shop_request() {
	if ( is_page( 'prepay-treatments' ) ) {
		return true;
	}
	if ( function_exists( 'is_woocommerce' ) && ( is_woocommerce() || is_cart() || is_checkout() || is_account_page() ) ) {
		return true;
	}
	return false;
}

function tf_shop_robots( $robots ) {
	if ( ! tf_shop_is_public() && tf_shop_is_shop_request() ) {
		$robots['noindex']  = true;
		$robots['nofollow'] = true;
		unset( $robots['index'], $robots['follow'], $robots['max-image-preview'] );
	}
	return $robots;
}
add_filter( 'wp_robots', 'tf_shop_robots', 99 );

/** Yoast writes its own robots tag. */
function tf_shop_yoast_robots( $robots ) {
	if ( ! tf_shop_is_public() && tf_shop_is_shop_request() ) {
		return 'noindex, nofollow';
	}
	return $robots;
}
add_filter( 'wpseo_robots', 'tf_shop_yoast_robots', 99 );

/** Keep products and the shop page out of the Yoast sitemap while hidden. */
function tf_shop_sitemap_exclude_type( $excluded, $post_type ) {
	if ( ! tf_shop_is_public() && 'product' === $post_type ) {
		return true;
	}
	return $excluded;
}
add_filter( 'wpseo_sitemap_exclude_post_type', 'tf_shop_sitemap_exclude_type', 10, 2 );
add_filter( 'wpseo_sitemap_exclude_taxonomy', function ( $excluded, $tax ) {
	if ( ! tf_shop_is_public() && in_array( $tax, array( 'product_cat', 'product_tag', 'product_brand' ), true ) ) {
		return true;
	}
	return $excluded;
}, 10, 2 );

function tf_shop_sitemap_exclude_ids( $ids ) {
	$ids = is_array( $ids ) ? $ids : array();
	if ( ! tf_shop_is_public() ) {
		$page = get_page_by_path( 'prepay-treatments' );
		if ( $page ) {
			$ids[] = (int) $page->ID;
		}
	}
	return $ids;
}
add_filter( 'wpseo_exclude_from_sitemap_by_post_ids', 'tf_shop_sitemap_exclude_ids' );

/** Setting: Ajustes → Lectura → "THE FACES · Tienda visible en Google". */
function tf_shop_settings() {
	register_setting( 'reading', 'tf_shop_public', array( 'type' => 'boolean', 'sanitize_callback' => function ( $v ) { return $v ? 1 : 0; } ) );
	add_settings_field(
		'tf_shop_public',
		'THE FACES · Tienda',
		function () {
			echo '<label><input type="checkbox" name="tf_shop_public" value="1" ' . checked( 1, (int) get_option( 'tf_shop_public', 0 ), false ) . '> Mostrar la tienda en Google (indexar /prepay-treatments/ y los productos)</label>';
			echo '<p class="description">Desmarcado: la tienda funciona con el enlace directo (para anuncios), pero Google no la indexa y no aparece en el sitemap. La web principal no cambia.</p>';
		},
		'reading'
	);
}
add_action( 'admin_init', 'tf_shop_settings' );

/** The treatments page always uses the THE FACES layout (header and footer of the site), whatever the theme or page template. */
function tf_shop_template( $template ) {
	if ( is_page( 'prepay-treatments' ) ) {
		return TF_SHOP_DIR . 'templates/shop.php';
	}
	return $template;
}
add_filter( 'template_include', 'tf_shop_template', 99 );
