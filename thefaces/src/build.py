#!/usr/bin/env python3
"""THE FACES website generator.

Writes:
  thefaces/tilda/00-site-head.html                  -> Tilda: Site settings > More > HTML code for HEAD (once)
  thefaces/tilda/<lang>/NN-<block>.html             -> one T123 block per section and language
  thefaces/tilda/<lang>/pages/<page>-intro.html     -> H1 + breadcrumbs block for inner pages
  thefaces/tilda/<lang>/head/<page>.html            -> per-page HEAD code (hreflang, Open Graph)
  thefaces/preview/<lang>/<page>/index.html          -> full preview of every page in every language
  thefaces/SEO_ESTRUCTURA.md                         -> page map with titles and descriptions

Usage: python3 thefaces/src/build.py [--assets-base URL] [--site https://thefacesworld.com]
Images in the Tilda blocks use --assets-base (or src/assets_base.txt). Files listed in
src/assets_map.json ({"founders.webp": "https://static.tildacdn.com/..."}) override single images.
"""
import argparse, html, json, re, sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
from content_ui import UI, LANGS, DUR, LANG_NAMES, HTML_LANG, OG_LOCALE, WA, WA_FOR  # noqa: E402
from content_rich import SENSES, ELEMENTS, CATS, DESC, FAQ  # noqa: E402
from content_seo import PAGES  # noqa: E402
from menu import MENU, SIGNATURES, GIFTS, SALONS, LINKS, GALLERY  # noqa: E402
from content_waterfall import WF_UI, WF_RITUALS  # noqa: E402
UI.update(WF_UI)

E = lambda s: html.escape(str(s), quote=True)  # noqa: E731
LI = {l: i for i, l in enumerate(LANGS)}
GROUP = {"en": ",", "th": ",", "ja": ",", "ru": " ", "es": ".", "de": ".", "id": "."}


class Ctx:
    def __init__(self, lang, mode, slug, site, assets_base, assets_map):
        self.lang, self.mode, self.slug, self.site = lang, mode, slug, site
        self.assets_base, self.assets_map = assets_base, assets_map
        self.i = LI[lang]

    def t(self, key, **kw):
        s = UI[key][self.i]
        for k, v in kw.items():
            s = s.replace("{" + k + "}", str(v))
        return s

    def pick(self, lst):
        return lst[self.i]

    def price(self, n):
        return "IDR " + f"{n:,}".replace(",", GROUP[self.lang])

    def dur(self, m):
        h, mi, j = DUR[self.lang]
        sp = " " if j else ""
        parts = []
        if m // 60:
            parts.append(f"{m // 60}{sp}{h}")
        if m % 60:
            parts.append(f"{m % 60}{sp}{mi}")
        return j.join(parts)

    def asset(self, name):
        if self.mode == "preview":
            return "../" * self.depth() + "assets/" + name
        return self.assets_map.get(name) or self.assets_base.rstrip("/") + "/" + name

    def depth(self):  # preview/<lang>/<slug>/index.html -> 3 (or 2 for home)
        return 3 if self.slug else 2

    def url(self, slug="", anchor="", lang=None):
        lang = lang or self.lang
        if self.mode == "preview":
            path = "../" * (self.depth() - 1) + lang + "/" + (slug + "/" if slug else "") + "index.html"
        else:
            path = ("/" if lang == "en" else f"/{lang}/") + (slug if slug else "")
        return path + (("#" + anchor) if anchor else "")

    def abs_url(self, slug, lang=None):
        lang = lang or self.lang
        return self.site.rstrip("/") + ("/" if lang == "en" else f"/{lang}/") + slug


def label(ctx, n, key):
    return f'<p class="eyebrow rv"><span class="n">{n:02d} —</span>{E(ctx.t(key))}</p>'


def add_attrs(item):
    cat, iid, name, d, p, only = item
    return (f'data-add="{iid}" data-name="{E(name)}" data-d="{d}" data-p="{p}" data-cat="{cat}"'
            + (f' data-only="{",".join(only)}"' if only else ""))


ITEM = {m[1]: m for m in MENU}
CUR = ' aria-current="true"'
ON = ' class="on"'

SOCIAL_SVG = {
 "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zm0 4.8a5 5 0 100 10 5 5 0 000-10zm0 8.2a3.2 3.2 0 110-6.4 3.2 3.2 0 010 6.4zm5.2-9.6a1.2 1.2 0 100 2.4 1.2 1.2 0 000-2.4z"/></svg>',
 "tiktok": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.6 5.8A4.3 4.3 0 0115.5 3h-3.1v12.4a2.6 2.6 0 11-2.6-2.6c.3 0 .5 0 .8.1V9.7a5.8 5.8 0 105 5.7V9.1a7.4 7.4 0 004.3 1.4V7.4a4.3 4.3 0 01-3.3-1.6z"/></svg>',
 "whatsapp": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.8 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.2.1-1.9-.1-.4-.1-1-.3-1.7-.6-3-1.3-4.9-4.3-5.1-4.5-.1-.2-1.2-1.6-1.2-3.1s.8-2.2 1-2.5c.3-.3.6-.4.8-.4h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.7 1.2 1.6 2 1.1 1 2 1.3 2.3 1.4.3.1.4.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.1.1.7-.1 1.4z"/></svg>',
 "email": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v14H3V5zm9 7L4.5 6.5v1.7L12 14l7.5-5.8V6.5L12 12z"/></svg>',
}

# ------------------------------------------------------------------ blocks

def b_header(ctx):
    T = {"lang": ctx.lang, "dur": list(DUR[ctx.lang]), "wa": WA[WA_FOR[ctx.lang]],
         "toast_added": ctx.t("toast_added"), "toast_switched": UI["toast_switched"][ctx.i],
         "remove": ctx.t("remove"), "ft_thanks": ctx.t("ft_thanks")}
    nav = [("nav_elements", ctx.url("five-elements")),
           ("nav_menu", ctx.url("menu")), ("nav_salons", ctx.url("", "salons")), ("nav_founders", ctx.url("founders")),
           ("nav_gifts", ctx.url("gift-certificates")), ("nav_partners", ctx.url("partners")), ("nav_journal", ctx.url("journal"))]
    navh = "".join(f'<a href="{E(u)}">{E(ctx.t(k))}</a>' for k, u in nav)
    page_slug = ctx.slug
    langs = "".join(f'<li><a href="{E(ctx.url(page_slug, lang=l))}" hreflang="{l}" lang="{l}"{CUR if l == ctx.lang else ""}>{E(LANG_NAMES[l])}</a></li>' for l in LANGS)
    mlangs = "".join(f'<a href="{E(ctx.url(page_slug, lang=l))}" hreflang="{l}" lang="{l}"{CUR if l == ctx.lang else ""}>{E(LANG_NAMES[l])}</a>' for l in LANGS)
    mnav = (f'<a href="{E(ctx.url("", "philosophy"))}">{E(ctx.t("nav_philosophy"))}</a>'
            f'<a href="{E(ctx.url("five-elements", "senses"))}">{E(ctx.t("nav_senses"))}</a>' + navh)
    return f'''<script type="application/json" id="tf-i18n">{json.dumps(T, ensure_ascii=False)}</script>
<header class="top">
 <div class="bar">
  <a href="{E(ctx.url())}" class="logo" aria-label="THE FACES"><img src="{ctx.asset("logo-white.png")}" alt="THE FACES" width="600" height="338"></a>
  <nav aria-label="Main">{navh}</nav>
  <div class="langsel"><button type="button" aria-expanded="false" aria-label="{E(ctx.t("language"))}">{ctx.lang.upper()} <span aria-hidden="true">▾</span></button><ul>{langs}</ul></div>
  <a class="cartbtn" href="{E(ctx.url("menu", "menu"))}" data-open-builder><span class="lbl">{E(ctx.t("your_ritual"))}</span><b data-count>0</b></a>
  <a href="{E(ctx.url("menu", "menu"))}" class="btn book" data-open-builder>{E(ctx.t("book"))}</a>
  <button type="button" class="burger" aria-label="{E(ctx.t("open_menu"))}"><span></span><span></span><span></span></button>
 </div>
</header>
<div class="mnav" role="dialog" aria-label="{E(ctx.t("open_menu"))}">
 <button type="button" class="close" aria-label="{E(ctx.t("close"))}">×</button>
 {mnav}
 <div class="langs">{mlangs}</div>
</div>'''


def b_hero(ctx):
    return f'''<section class="hero" aria-label="THE FACES">
 <video autoplay muted loop playsinline preload="metadata" poster="{ctx.asset("hero-poster.jpg")}"><source src="{ctx.asset("hero-720.mp4")}" type="video/mp4"></video>
 <button type="button" class="sound" data-off="{E(ctx.t("sound_off"))}" data-on="{E(ctx.t("sound_on"))}">{E(ctx.t("sound_off"))}</button>
 <div class="wrap in">
  <h1 class="eyebrow">{E(ctx.t("hero_h1"))}</h1>
  <p class="display" aria-hidden="true"><span class="line"><span>{E(ctx.t("hero_t1"))}</span></span><span class="line"><span>{E(ctx.t("hero_t2"))}</span></span></p>
  <p class="lead sub">{E(ctx.t("hero_sub"))}</p>
  <div class="ctas">
   <a href="{E(ctx.url("menu", "menu"))}" class="btn solid" data-open-builder>{E(ctx.t("hero_cta1"))}</a>
   <a href="#elements" class="btn">{E(ctx.t("hero_cta2"))}</a>
  </div>
  <div class="chips"><span>{E(ctx.t("chip_from", p=ctx.price(300000)))}</span><span>Ubud · Sanur</span><span>{E(ctx.t("chip_vegan"))}</span><span>{E(ctx.t("chip_two"))}</span></div>
 </div>
 <div class="side">Five Elements.<br>Guided by Love.</div>
 <div class="cue" aria-hidden="true"></div>
</section>'''


def b_philosophy(ctx):
    words = [ctx.pick(e["name"]) for e in ELEMENTS] + [ctx.pick(s["name"]) for s in SENSES[:5]]
    track = "".join(f"<span>{E(w)}</span>" for w in words * 2)
    return f'''<section class="sec" id="philosophy">
 <div class="wrap philo">
  <div class="imgs">
   <div class="a mask rv"><img src="{ctx.asset("g04-interior.webp")}" alt="{E(ctx.t("ga_alt"))}" loading="lazy" width="1000" height="1500"></div>
   <div class="b mask rv d2" data-parallax="-0.08"><img src="{ctx.asset("g08-interior.webp")}" alt="{E(ctx.t("ga_alt"))}" loading="lazy" width="1000" height="1500"></div>
  </div>
  <div>
   {label(ctx, 1, "ph_label")}
   <h2 class="h2 rv d1">{E(ctx.t("ph_h2"))}</h2>
   <p class="lead rv d2">{E(ctx.t("ph_lead"))}</p>
   <p class="muted rv d3">{E(ctx.t("ph_p1"))}</p>
   <p class="sign rv d4">{E(ctx.t("ph_sign"))}</p>
  </div>
 </div>
</section>
<div class="words" aria-hidden="true"><div class="track">{track}</div></div>'''


def b_senses(ctx):
    n = len(SENSES)
    imgs = "".join(f'<img src="{ctx.asset(s["img"])}" alt="{E(ctx.pick(s["name"]) + " · " + ctx.pick(s["line"]))}" loading="lazy" width="750" height="1000"{ON if k == 0 else ""}>' for k, s in enumerate(SENSES))
    dots = "".join(f'<i{ON if k == 0 else ""}></i>' for k in range(n))
    items = "".join(f'''<article class="sn-item{" on" if k == 0 else ""}">
   <div class="mimg"><img src="{ctx.asset(s["img"])}" alt="" loading="lazy" width="750" height="1000"></div>
   <span class="k">{k + 1:02d} / {n:02d}</span>
   <h3>{E(ctx.pick(s["name"]))}</h3>
   <p class="line">{E(ctx.pick(s["line"]))}</p>
   <p>{E(ctx.pick(s["text"]))}</p>
  </article>''' for k, s in enumerate(SENSES))
    return f'''<section class="senses sec" id="senses">
 <div class="wrap sec-head">
  <div>{label(ctx, 2, "se_label")}<h2 class="h2 rv d1">{E(ctx.t("se_h2"))}</h2></div>
  <p class="muted rv d2">{E(ctx.t("se_intro"))}</p>
 </div>
 <div class="sn">
  <div class="sn-stage" aria-hidden="true"><div class="sn-frame">{imgs}<span class="num">01</span><div class="sn-dots">{dots}</div></div></div>
  <div class="sn-list">{items}</div>
 </div>
</section>'''


def b_elements(ctx):
    cards = []
    for k, e in enumerate(ELEMENTS):
        it = ITEM[e["id"]]
        cards.append(f'''<article class="el{" open" if k == 0 else ""}" tabindex="0" aria-expanded="{"true" if k == 0 else "false"}">
   <img src="{ctx.asset(e["img"])}" alt="{E(ctx.pick(e["name"]) + " · " + ctx.pick(e["t"]))}" loading="lazy">
   <span class="num">{k + 1:02d} / 05</span>
   <div class="c"><h3>{E(ctx.pick(e["name"]))}</h3><p class="t">{E(ctx.pick(e["t"]))}</p>
    <div class="more"><dl><dt>{E(ctx.t("el_when"))}</dt><dd>{E(ctx.pick(e["when"]))}</dd><dt>{E(ctx.t("el_inc"))}</dt><dd>{E(ctx.pick(e["inc"]))}</dd></dl>
     <div class="meta"><span>{E(ctx.t("about3h"))} · {ctx.price(it[4])}</span><button type="button" class="btn" {add_attrs(it)} data-l-add="{E(ctx.t("add_to_ritual"))}" data-l-on="{E(ctx.t("in_ritual"))}">{E(ctx.t("add_to_ritual"))}</button></div>
    </div>
   </div>
  </article>''')
    return f'''<section class="elements sec" id="elements">
 <div class="wrap sec-head">
  <div>{label(ctx, 3, "el_label")}<h2 class="h2 rv d1">{E(ctx.t("el_h2"))}</h2></div>
  <p class="muted rv d2">{E(ctx.t("el_intro", p=ctx.price(1800000)))}</p>
 </div>
 <div class="el-grid">{"".join(cards)}</div>
</section>'''


def b_signatures(ctx):
    cards = []
    for iid, tag, img in SIGNATURES:
        it = ITEM[iid]
        desc = ctx.pick(DESC[iid]) if iid in DESC else ""
        cards.append(f'''<article class="card"><div class="ph"><img src="{ctx.asset(img)}" alt="{E(it[2])}" loading="lazy"><span class="tag">{E(ctx.t(tag))}</span></div>
   <h3>{E(it[2])}</h3><p class="pr">{ctx.dur(it[3])} · {ctx.price(it[4])}</p><p>{E(desc)}</p>
   <button type="button" class="btn" {add_attrs(it)} data-l-add="{E(ctx.t("add_to_ritual"))}" data-l-on="{E(ctx.t("added"))}">{E(ctx.t("add_to_ritual"))}</button></article>''')
    return f'''<section class="sig sec" id="signature">
 <div class="wrap sec-head">
  <div>{label(ctx, 4, "sg_label")}<h2 class="h2 rv d1">{E(ctx.t("sg_h2"))}</h2></div>
  <div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><p class="muted rv d2" style="max-width:420px">{E(ctx.t("sg_intro"))}</p>
   <div class="railnav"><button type="button" class="prev" aria-label="{E(ctx.t("prev"))}">←</button><button type="button" class="next" aria-label="{E(ctx.t("next"))}">→</button></div></div>
 </div>
 <div class="rail">{"".join(cards)}</div>
</section>'''


def b_menu(ctx):
    tabs, cats = [], []
    for k, (cid, names) in enumerate(CATS):
        items = [m for m in MENU if m[0] == cid]
        tabs.append(f'<button type="button" role="tab" data-tab="{cid}" aria-selected="{"true" if k == 0 else "false"}" aria-controls="cat-{cid}">{E(ctx.pick(names))}<span>{len(items)}</span></button>')
        rows = []
        for m in items:
            cat, iid, name, d, p, only = m
            badge = f'<span class="badge">{E(ctx.t("only_in", salon=", ".join(SALONS[s]["name"] for s in only)))}</span>' if only else ""
            ds = f'<p class="ds">{E(ctx.pick(DESC[iid]))}</p>' if iid in DESC else ""
            rows.append(f'<li class="item"><div><p class="nm">{E(name)}{badge}</p>{ds}</div><span class="du">{ctx.dur(d)}</span><span class="pc">{ctx.price(p)}</span>'
                        f'<button type="button" class="plus" {add_attrs(m)} aria-label="{E(ctx.t("add"))}: {E(name)}">+</button></li>')
        cats.append(f'<div class="cat" id="cat-{cid}" role="tabpanel"{"" if k == 0 else " hidden"}><h3>{E(ctx.pick(names))}</h3><ul class="items">{"".join(rows)}</ul></div>')
    return f'''<section class="menu-sec sec" id="menu">
 <div class="wrap sec-head">
  <div>{label(ctx, 5, "mn_label")}<h2 class="h2 rv d1">{E(ctx.t("mn_h2"))}</h2></div>
  <p class="muted rv d2">{E(ctx.t("mn_intro"))}</p>
 </div>
 <div class="wrap menu-layout">
  <div>
   <div class="salon-switch" role="group" aria-label="{E(ctx.t("salon_label"))}"><button type="button" data-salon="ubud" class="on">Ubud</button><button type="button" data-salon="sanur">Sanur</button></div>
   <div class="tabs" role="tablist">{"".join(tabs)}</div>
   {"".join(cats)}
   <p class="note">{E(ctx.t("mn_note"))}</p>
  </div>
  <aside class="builder" id="tf-builder" aria-label="{E(ctx.t("your_ritual"))}">
   <p class="eyebrow">{E(ctx.t("your_ritual"))}</p>
   <h3>{E(ctx.t("b_h3"))}</h3>
   <p class="empty" id="tf-bempty">{E(ctx.t("b_empty"))}</p>
   <ul class="bl" id="tf-blist"></ul>
   <div class="tot"><span>{E(ctx.t("b_time"))}</span><strong id="tf-btime">—</strong></div>
   <div class="tot"><span>{E(ctx.t("b_total"))}</span><strong id="tf-btotal">IDR 0</strong></div>
   <div class="step"><span class="lbl">{E(ctx.t("b_step1"))}</span><div class="choice"><button type="button" data-salon="ubud" class="on">Ubud</button><button type="button" data-salon="sanur">Sanur</button></div></div>
   <div class="step"><label for="tf-bdate">{E(ctx.t("b_step2"))}</label><input id="tf-bdate" type="text" placeholder="{E(ctx.t("b_ph"))}" autocomplete="off"></div>
   <div class="go">
    <a class="btn solid" id="tf-bonline" href="{SALONS["ubud"]["online"]}" target="_blank" rel="noopener">{E(ctx.t("b_online"))} · <span class="s">Ubud</span></a>
    <a class="btn wa" id="tf-bwa" href="https://wa.me/{SALONS["ubud"]["wa"]}" target="_blank" rel="noopener">{E(ctx.t("b_wa"))}</a>
   </div>
   <p class="fine">{E(ctx.t("b_fine"))}</p>
  </aside>
 </div>
</section>'''


def b_gallery(ctx):
    alt = E(ctx.t("ga_alt"))
    row = lambda g: "".join(f'<img src="{ctx.asset(x + ".webp")}" alt="{alt if i < len(g) else ""}" loading="lazy">' for i, x in enumerate(g + g))  # noqa: E731
    g1, g2 = GALLERY[:7], GALLERY[6:] + GALLERY[:1]
    return f'''<section class="gal sec" aria-labelledby="tf-gal-h">
 <div class="wrap head"><div><p class="eyebrow rv">{E(ctx.t("ga_label"))}</p><h2 class="h2 rv d1" id="tf-gal-h" style="margin-top:18px">{E(ctx.t("ga_h2"))}</h2></div>
  <a class="link rv d2" href="{LINKS["instagram"]}" target="_blank" rel="noopener">Instagram @thefacesbali ↗</a></div>
 <div class="strip">{row(g1)}</div>
 <div class="strip rev">{row(g2)}</div>
</section>'''


def b_salons(ctx):
    cards = []
    for k, (sid, s) in enumerate(SALONS.items()):
        wa = f'https://wa.me/{s["wa"]}?text=' + html.escape(f'Hello! I would like to book at THE FACES {s["name"]}').replace(" ", "%20")
        cards.append(f'''<article class="salon rv{" d2" if k else ""}" id="salon-{sid}">
   <div class="ph"><img src="{ctx.asset(s["img"])}" alt="{E(ctx.t(s["alt"]))}" loading="lazy"></div>
   <h3><a href="{E(ctx.url(sid))}">{s["name"]}</a></h3>
   <address>{E(s["addr"])}</address>
   <div class="acts">
    <a class="btn darksolid" href="{E(ctx.url("menu", "menu"))}" data-book-salon="{sid}">{E(ctx.t("sa_book", salon=s["name"]))}</a>
    <a class="btn dark" href="{wa}" target="_blank" rel="noopener">WhatsApp</a>
    <a class="btn dark" href="tel:{s["tel"].replace(" ", "")}">{s["tel"]}</a>
    <a class="btn dark" href="{s["maps"]}" target="_blank" rel="noopener">{E(ctx.t("sa_dir"))}</a>
   </div>
  </article>''')
    return f'''<section class="sec" id="salons">
 <div class="wrap sec-head">
  <div>{label(ctx, 6, "sa_label")}<h2 class="h2 rv d1">{E(ctx.t("sa_h2"))}</h2></div>
  <p class="muted rv d2">{E(ctx.t("sa_intro"))}</p>
 </div>
 <div class="wrap"><div class="salons">{"".join(cards)}</div><p class="soon">{E(ctx.t("sa_soon"))}</p></div>
</section>'''


def b_founders(ctx):
    return f'''<section class="founders sec" id="founders">
 <div class="wrap fo-grid">
  <figure class="fo-photo rv"><div class="ph"><img src="{ctx.asset("founders.webp")}" alt="{E(ctx.t("fo_alt"))}" loading="lazy" width="1100" height="1100" data-parallax="0.1"></div>
   <figcaption>Anna &amp; Evgenii Dubinin</figcaption></figure>
  <div>
   {label(ctx, 7, "fo_label")}
   <h2 class="h2 rv d1">{E(ctx.t("fo_h2"))}</h2>
   <p class="lead rv d2">{E(ctx.t("fo_lead"))}</p>
   <p class="rv d2">{E(ctx.t("fo_p1"))}</p>
   <blockquote class="quote rv d3">{E(ctx.t("fo_quote"))}</blockquote>
   <ul class="timeline rv d3"><li><b>2013</b><span>{E(ctx.t("fo_t1"))}</span></li><li><b>+5</b><span>{E(ctx.t("fo_t2"))}</span></li><li><b>Bali</b><span>{E(ctx.t("fo_t3"))}</span></li></ul>
   <div class="stats rv d4"><div><b>20+</b><span>{E(ctx.t("st_years"))}</span></div><div><b>2</b><span>{E(ctx.t("st_salons"))}</span></div><div><b>50+</b><span>{E(ctx.t("st_treat"))}</span></div></div>
  </div>
 </div>
</section>'''


def b_gifts(ctx):
    cards = []
    for pay, get in GIFTS:
        msg = f"Hello! I would like a gift certificate: pay IDR {pay:,}, value IDR {get:,}."
        cards.append(f'''<div class="gift rv"><span class="p">{E(ctx.t("gi_pay", p=ctx.price(pay)))}</span><span class="v">{ctx.price(get)}</span><span class="bonus">{E(ctx.t("gi_bonus", n=round((get / pay - 1) * 100)))}</span>
   <a class="btn dark" target="_blank" rel="noopener" href="https://wa.me/{SALONS["ubud"]["wa"]}?text={html.escape(msg).replace(" ", "%20")}">{E(ctx.t("gi_order"))}</a></div>''')
    return f'''<section class="sec" id="gifts">
 <div class="wrap sec-head">
  <div>{label(ctx, 8, "gi_label")}<h2 class="h2 rv d1">{E(ctx.t("gi_h2"))}</h2></div>
  <p class="muted rv d2">{E(ctx.t("gi_intro"))}</p>
 </div>
 <div class="wrap"><div class="gifts">{"".join(cards)}</div></div>
</section>'''


def b_partners(ctx):
    names = ["The White Temple · Sanur", "THE FACES Ubud", "WATERFALL · Bali", "THE FACES SANUR"]
    proj = "".join(f'<a class="rv d{k}" href="{LINKS["projects"][k]}" target="_blank" rel="noopener"><span class="st">{E(ctx.t(f"pa_s{k + 1}"))}</span><h3>{names[k]}</h3><p>{E(ctx.t(f"pa_d{k + 1}"))}</p><span class="ar">{E(ctx.t("pa_read"))}</span></a>' for k in range(4))
    ways = "".join(f'<div class="rv d{k}"><span class="eyebrow k">{E(ctx.t(f"pa_w{k + 1}k"))}</span><h3>{E(ctx.t(f"pa_w{k + 1}h"))}</h3><p>{E(ctx.t(f"pa_w{k + 1}p"))}</p></div>' for k in range(3))
    return f'''<section class="partner sec" id="partners">
 <div class="bg" data-parallax="0.15" style="background-image:url('{ctx.asset("waterfall.webp")}')"></div>
 <div class="wrap">
  {label(ctx, 9, "pa_label")}
  <div class="sec-head" style="margin:22px 0 0"><h2 class="h2 rv d1">{E(ctx.t("pa_h2"))}</h2><p class="rv d2" style="opacity:.75">{E(ctx.t("pa_intro"))}</p></div>
  <div class="pgrid">{proj}</div>
  <div class="ways">{ways}</div>
  <div class="pctas rv">
   <a class="btn solid" href="{LINKS["partner_call"]}" target="_blank" rel="noopener">{E(ctx.t("pa_cta1"))}</a>
   <a class="btn" href="{LINKS["catalogue"]}" target="_blank" rel="noopener">{E(ctx.t("pa_cta2"))}</a>
   <a class="btn" href="https://wa.me/{SALONS["ubud"]["wa"]}?text=Hello!%20I%20would%20like%20to%20join%20The%20Faces%20team" target="_blank" rel="noopener">{E(ctx.t("pa_w3h"))}</a>
  </div>
  <p class="legal">{E(ctx.t("pa_legal"))}</p>
 </div>
</section>'''


def b_waterfall(ctx):
    rows = []
    for k, r in enumerate(WF_RITUALS):
        dur = f'<span class="wf-min">{ctx.dur(r["min"])}</span>' if r["min"] else ""
        if r["steps"]:
            steps = "".join(f"<li>{E(s)}</li>" for s in ctx.pick(r["steps"]).split(" · "))
            body = f'<p>{E(ctx.pick(r["line"]))}</p><ul class="wf-steps">{steps}</ul><p class="wf-for"><b>{E(ctx.t("wf_for"))}</b> {E(ctx.pick(r["for"]))}</p>'
        else:
            body = f'<p>{E(ctx.pick(r["line"]))}</p><p class="wf-for"><b>{E(ctx.t("wf_soon"))}</b></p>'
        rows.append(f'<details{" open" if k == 0 else ""}><summary><span class="wf-k">{k + 1:02d} · {r["key"]}</span><span class="wf-n">{E(r["name"])}</span>{dur}</summary><div class="wf-b">{body}</div></details>')
    notify = "https://wa.me/" + SALONS["ubud"]["wa"] + "?text=Hello!%20Please%20let%20me%20know%20when%20THE%20FACES%20Waterfall%20Spa%20opens."
    return f'''<section class="wf sec" id="waterfall">
 <div class="wrap wf-grid">
  <div class="wf-left">
   <p class="eyebrow rv"><span class="n">✦</span>{E(ctx.t("wf_label"))}</p>
   <h2 class="h2 rv d1">{E(ctx.t("wf_h2"))}</h2>
   <p class="wf-motto rv d2">{E(ctx.t("wf_motto"))}</p>
   <p class="muted rv d2">{E(ctx.t("wf_intro"))}</p>
   <div class="wf-imgs">
    <div class="mask rv a"><img src="{ctx.asset("waterfall-3.webp")}" alt="{E(ctx.t("wf_alt1"))}" loading="lazy" width="768" height="1024"></div>
    <div class="mask rv d2 b" data-parallax="-0.08"><img src="{ctx.asset("waterfall.webp")}" alt="{E(ctx.t("wf_alt2"))}" loading="lazy"></div>
   </div>
  </div>
  <div class="wf-right">
   <p class="eyebrow rv">{E(ctx.t("wf_coll"))}</p>
   <div class="wf-list rv d1">{"".join(rows)}</div>
   <div class="pctas rv" style="margin-top:40px">
    <a class="btn darksolid" href="{notify}" target="_blank" rel="noopener">{E(ctx.t("wf_notify"))}</a>
    <a class="btn dark" href="{LINKS["projects"][2]}" target="_blank" rel="noopener">{E(ctx.t("wf_project"))}</a>
   </div>
   <p class="note">{E(ctx.t("wf_note"))}</p>
  </div>
 </div>
</section>'''


def b_journal(ctx):
    imgs = ["g03-face-s.webp", "g10-proc-s.webp", "g09-proc-s.webp"]
    posts = "".join(f'<a class="post rv d{k}" href="{E(ctx.url("journal"))}"><div class="ph"><img src="{ctx.asset(imgs[k])}" alt="" loading="lazy"></div><p class="d">{E(ctx.t(f"jo_c{k + 1}"))}</p><h3>{E(ctx.t(f"jo_t{k + 1}"))}</h3></a>' for k in range(3))
    return f'''<section class="sec" id="journal">
 <div class="wrap sec-head">
  <div>{label(ctx, 10, "jo_label")}<h2 class="h2 rv d1">{E(ctx.t("jo_h2"))}</h2></div>
  <div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><p class="muted rv d2" style="max-width:420px">{E(ctx.t("jo_intro"))}</p><a class="link rv d2" href="{E(ctx.url("journal"))}">{E(ctx.t("jo_all"))}</a></div>
 </div>
 <div class="wrap posts">{posts}</div>
</section>'''


def b_faq(ctx):
    qa = [(ctx.pick(q), ctx.pick(a)) for q, a in FAQ]
    det = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in qa)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": ctx.lang,
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}
    return f'''<section class="faq sec" id="faq">
 <div class="wrap faq-grid">
  <div>{label(ctx, 11, "fq_label")}<h2 class="h2 rv d1" style="margin-top:22px">{E(ctx.t("fq_h2"))}</h2></div>
  <div class="rv d2">{det}</div>
 </div>
 <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</section>'''


def jsonld_business(ctx):
    org = {"@type": "Organization", "@id": ctx.site + "/#org", "name": "THE FACES", "url": ctx.site + "/",
           "logo": ctx.asset("logo-black.png"), "email": LINKS["email"],
           "sameAs": [LINKS["instagram"], LINKS["tiktok"], LINKS["network"]],
           "founder": [{"@type": "Person", "name": "Anna Dubinin"}, {"@type": "Person", "name": "Evgenii Dubinin"}],
           "foundingDate": "2013"}
    spas = []
    for sid, s in SALONS.items():
        spas.append({"@type": "DaySpa", "@id": ctx.site + f"/{sid}#spa", "name": f"The Faces Spa {s['name']}",
                     "url": ctx.abs_url(sid), "telephone": s["tel"], "image": ctx.asset(s["img"]),
                     "priceRange": "IDR 200,000 – 3,800,000", "currenciesAccepted": "IDR",
                     "address": {"@type": "PostalAddress", "streetAddress": s["street"], "addressLocality": s["locality"],
                                 "addressRegion": "Bali", "postalCode": s["postal"], "addressCountry": "ID"},
                     "parentOrganization": {"@id": ctx.site + "/#org"}, "hasMap": s["maps"],
                     "potentialAction": {"@type": "ReserveAction", "target": s["online"]}})
    return json.dumps({"@context": "https://schema.org", "@graph": [org] + spas}, ensure_ascii=False)


def b_footer(ctx):
    legal = [("lg_cancel", "cancellation_policy"), ("lg_resched", "rescheduling_policy"), ("lg_privacy", "privacy_policy"),
             ("lg_cookies", "cookie_policy"), ("lg_terms", "terms_of_use"), ("lg_gift", "the_faces_gift_certificate_terms")]
    legal_h = "".join(f'<a href="{LINKS["legal"]}{p}">{E(ctx.t(k))}</a>' for k, p in legal)
    flangs = "".join(f'<a href="{E(ctx.url(ctx.slug, lang=l))}" hreflang="{l}" lang="{l}"{CUR if l == ctx.lang else ""}>{E(LANG_NAMES[l])}</a>' for l in LANGS)
    soc = (f'<a href="{LINKS["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram">{SOCIAL_SVG["instagram"]}</a>'
           f'<a href="{LINKS["tiktok"]}" target="_blank" rel="noopener" aria-label="TikTok">{SOCIAL_SVG["tiktok"]}</a>'
           f'<a href="https://wa.me/{SALONS["ubud"]["wa"]}" target="_blank" rel="noopener" aria-label="WhatsApp">{SOCIAL_SVG["whatsapp"]}</a>'
           f'<a href="mailto:{LINKS["email"]}" aria-label="Email">{SOCIAL_SVG["email"]}</a>')
    return f'''<footer class="foot">
 <div class="wrap">
  <div class="f-top">
   <div>
    <a href="{E(ctx.url())}" class="logo"><img src="{ctx.asset("logo-white.png")}" alt="THE FACES" loading="lazy" width="600" height="338"></a>
    <p style="margin-top:22px;opacity:.65;max-width:360px;font-size:14px">{E(ctx.t("ft_about"))}</p>
    <div class="social">{soc}</div>
    <form class="news"><input type="email" required placeholder="{E(ctx.t("ft_news_ph"))}" aria-label="Email"><button type="submit">{E(ctx.t("ft_join"))}</button></form>
    <div class="f-langs">{flangs}</div>
   </div>
   <div><h2>{E(ctx.t("ft_spa"))}</h2><ul>
    <li><a href="{E(ctx.url("five-elements"))}">{E(ctx.t("nav_elements"))}</a></li>
    <li><a href="{E(ctx.url("five-elements", "senses"))}">{E(ctx.t("nav_senses"))}</a></li>
    <li><a href="{E(ctx.url("menu"))}">{E(ctx.t("nav_menu"))}</a></li>
    <li><a href="{E(ctx.url("gift-certificates"))}">{E(ctx.t("nav_gifts"))}</a></li>
    <li><a href="{E(ctx.url("founders"))}">{E(ctx.t("nav_founders"))}</a></li>
    <li><a href="{E(ctx.url("journal"))}">{E(ctx.t("nav_journal"))}</a></li></ul></div>
   <div><h2>{E(ctx.t("nav_salons"))}</h2><ul>
    <li><a href="{E(ctx.url("ubud"))}">The Faces Ubud</a></li>
    <li><a href="tel:{SALONS["ubud"]["tel"].replace(" ", "")}">{SALONS["ubud"]["tel"]}</a></li>
    <li><a href="{E(ctx.url("sanur"))}">The Faces Sanur</a></li>
    <li><a href="tel:{SALONS["sanur"]["tel"].replace(" ", "")}">{SALONS["sanur"]["tel"]}</a></li>
    <li><a href="{SALONS["ubud"]["online"]}" target="_blank" rel="noopener">{E(ctx.t("ft_online"))}</a></li>
    <li><a href="mailto:{LINKS["email"]}">{LINKS["email"]}</a></li></ul></div>
   <div><h2>{E(ctx.t("ft_world"))}</h2><ul>
    <li><a href="{LINKS["network"]}" target="_blank" rel="noopener">{E(ctx.t("ft_network"))}</a></li>
    <li><a href="{E(ctx.url("partners"))}">{E(ctx.t("nav_partners"))}</a></li>
    <li><a href="{LINKS["catalogue"]}" target="_blank" rel="noopener">{E(ctx.t("pa_cta2"))}</a></li>
    <li><a href="{E(ctx.url("partners"))}">{E(ctx.t("ft_careers"))}</a></li></ul></div>
  </div>
  <div class="f-bot"><span>© 2026 THE FACES · Five Elements. Guided by Love.</span><nav aria-label="Legal">{legal_h}</nav></div>
 </div>
 <script type="application/ld+json">{jsonld_business(ctx)}</script>
</footer>
<div class="mbar"><a href="{E(ctx.url("menu"))}">{E(ctx.t("mb_menu"))}</a><button type="button" data-open-builder>{E(ctx.t("your_ritual"))} · <span data-count>0</span></button></div>
<div class="toast" role="status"><span class="msg"></span><a href="{E(ctx.url("menu", "menu"))}" data-open-builder>{E(ctx.t("toast_view"))}</a></div>
<div class="cookie" role="dialog" aria-label="Cookies"><p>{E(ctx.t("ck_text"))} <a href="{LINKS["legal"]}cookie_policy">{E(ctx.t("ck_more"))}</a></p>
 <div class="row"><button type="button" class="btn dark" data-consent="no">{E(ctx.t("ck_reject"))}</button><button type="button" class="btn darksolid" data-consent="yes">{E(ctx.t("ck_accept"))}</button></div></div>'''


def h1_of(title):
    return re.split(r"\s*[·｜|]\s*", title)[0]


def b_pageintro(ctx, page):
    title = ctx.pick(page["title"])
    h1 = h1_of(title)
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "THE FACES", "item": ctx.abs_url("")},
        {"@type": "ListItem", "position": 2, "name": h1, "item": ctx.abs_url(page["slug"])}]}
    return f'''<section class="pageintro" style="background:var(--ink);color:#fff;padding:clamp(140px,16vw,210px) 0 clamp(60px,7vw,100px)">
 <div class="wrap">
  <nav aria-label="Breadcrumb" class="eyebrow" style="opacity:.6"><a href="{E(ctx.url())}">THE FACES</a> <span aria-hidden="true">/</span> <span>{E(h1)}</span></nav>
  <h1 class="h2" style="margin:26px 0 22px;max-width:18ch">{E(h1)}</h1>
  <p class="lead" style="max-width:640px;opacity:.75">{E(ctx.pick(page["desc"]))}</p>
 </div>
 <script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False)}</script>
</section>'''


BLOCKS = {"01-header": b_header, "02-hero": b_hero, "03-philosophy": b_philosophy, "04-senses": b_senses,
          "05-elements": b_elements, "06-signatures": b_signatures, "07-menu-builder": b_menu, "08-gallery": b_gallery,
          "09-salons": b_salons, "10-founders": b_founders, "11-gifts": b_gifts, "12-partners": b_partners,
          "13-journal": b_journal, "16-waterfall": b_waterfall, "14-faq": b_faq, "15-footer": b_footer}


def wrap(ctx, name, inner):
    return f'<div class="tf" lang="{HTML_LANG[ctx.lang]}" data-block="{name}">\n{inner}\n</div>'


# ------------------------------------------------------------------ CSS scoping

def scope_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out, i = [], 0

    def scope_sel(sel):
        parts = []
        for p in sel.split(","):
            p = p.strip()
            parts.append(p if p.startswith(".tf") else ".tf " + p)
        return ",".join(parts)

    def parse(block):
        res, i = [], 0
        while i < len(block):
            j = block.find("{", i)
            if j < 0:
                break
            head = block[i:j].strip()
            depth, k = 1, j + 1
            while depth:
                depth += {"{": 1, "}": -1}.get(block[k], 0)
                k += 1
            body = block[j + 1:k - 1]
            if head.startswith("@keyframes"):
                res.append(f"{head}{{{body}}}")
            elif head.startswith("@media"):
                res.append(f"{head}{{{parse(body)}}}")
            else:
                res.append(f"{scope_sel(head)}{{{body.strip()}}}")
            i = k
        return "".join(res)
    return parse(css)


def minify_js(js):
    return js  # kept readable on purpose


# ------------------------------------------------------------------ heads

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600&family=Noto+Sans+JP:wght@200;300;400;500&family=Noto+Sans+Thai:wght@200;300;400;500&display=swap" rel="stylesheet">'

CONSENT_GTM = '''<script>
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500});
window.tfConsent=function(ok){var v=ok?'granted':'denied';gtag('consent','update',{ad_storage:v,ad_user_data:v,ad_personalization:v,analytics_storage:v});try{localStorage.setItem('tf_consent',v)}catch(e){}};
try{var c=localStorage.getItem('tf_consent');if(c)window.tfConsent(c==='granted')}catch(e){}
</script>
<!-- Google Tag Manager: replace GTM-XXXXXXX -->
<script>(function(w,d,s,l,i){if(i.indexOf('XXXX')>-1)return;w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>'''


def page_head(ctx, page):
    title, desc = ctx.pick(page["title"]), ctx.pick(page["desc"])
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{ctx.abs_url(page["slug"], l)}">' for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{ctx.abs_url(page["slug"], "en")}">'
    return f'''<!-- {page["slug"] or "home"} · {ctx.lang}. Tilda: Page settings > SEO: Title = "{title}" · Description = "{desc}"
     Page settings > Additional > HTML code for HEAD: paste the lines below. -->
{alts}
<meta property="og:locale" content="{OG_LOCALE[ctx.lang]}">
<meta property="og:image" content="{ctx.asset("og-1200x630.jpg")}">'''


# ------------------------------------------------------------------ build

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="https://thefacesworld.com")
    ap.add_argument("--assets-base", default=None)
    a = ap.parse_args()
    base_file = SRC / "assets_base.txt"
    assets_base = a.assets_base or (base_file.read_text().strip() if base_file.exists() else "https://YOUR-ASSETS-HOST/thefaces/assets/")
    map_file = SRC / "assets_map.json"
    assets_map = json.loads(map_file.read_text()) if map_file.exists() else {}

    css = scope_css((SRC / "site.css").read_text(encoding="utf-8"))
    js = (SRC / "site.js").read_text(encoding="utf-8")
    tdir, pdir = ROOT / "tilda", ROOT / "preview"

    (tdir).mkdir(exist_ok=True)
    (tdir / "00-site-head.html").write_text(
        "<!-- THE FACES · Tilda: Site settings > More > HTML code for the HEAD section. Paste once for the whole site. -->\n"
        + CONSENT_GTM + "\n" + FONTS + "\n<style>" + css + "</style>\n<script>" + js + "</script>\n", encoding="utf-8")

    seo_rows = []
    for lang in LANGS:
        ld = tdir / lang
        (ld / "pages").mkdir(parents=True, exist_ok=True)
        (ld / "head").mkdir(parents=True, exist_ok=True)
        home_ctx = Ctx(lang, "tilda", "", a.site, assets_base, assets_map)
        for name, fn in BLOCKS.items():
            (ld / f"{name}.html").write_text(f"<!-- THE FACES · {name} · {LANG_NAMES[lang]} · Tilda T123 block -->\n" + wrap(home_ctx, name, fn(home_ctx)) + "\n", encoding="utf-8")
        for page in PAGES:
            ctx = Ctx(lang, "tilda", page["slug"], a.site, assets_base, assets_map)
            key = page["slug"] or "home"
            (ld / "head" / f"{key}.html").write_text(page_head(ctx, page) + "\n", encoding="utf-8")
            if page["slug"]:
                (ld / "pages" / f"{key}-intro.html").write_text(
                    f"<!-- THE FACES · {key} page · H1 + breadcrumbs · {LANG_NAMES[lang]} · paste right after 01-header -->\n" + wrap(ctx, "intro", b_pageintro(ctx, page)) + "\n", encoding="utf-8")
                # header and footer language links point to the same page in other languages
                (ld / "pages" / f"{key}-01-header.html").write_text(wrap(ctx, "01-header", b_header(ctx)) + "\n", encoding="utf-8")
                (ld / "pages" / f"{key}-15-footer.html").write_text(wrap(ctx, "15-footer", b_footer(ctx)) + "\n", encoding="utf-8")
            title, desc = ctx.pick(page["title"]), ctx.pick(page["desc"])
            seo_rows.append((lang, ctx.url(page["slug"]) if True else "", title, desc, page["blocks"], page["slug"]))
            # preview
            pctx = Ctx(lang, "preview", page["slug"], a.site, assets_base, assets_map)
            body = []
            for name in page["blocks"]:
                body.append(wrap(pctx, name, BLOCKS[name](pctx)))
                if name == "01-header" and page["slug"]:
                    body.append(wrap(pctx, "intro", b_pageintro(pctx, page)))
            out = pdir / lang / page["slug"] / "index.html" if page["slug"] else pdir / lang / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{pctx.abs_url(page["slug"], l)}">' for l in LANGS)
            out.write_text(f'''<!doctype html>
<html lang="{HTML_LANG[lang]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:locale" content="{OG_LOCALE[lang]}">
{alts}
{FONTS}
<style>body{{margin:0;background:#fff}}{css}</style>
<script>window.tfConsent=function(ok){{try{{localStorage.setItem('tf_consent',ok?'granted':'denied')}}catch(e){{}}}};</script>
</head><body>
{chr(10).join(body)}
<script>{js}</script>
</body></html>''', encoding="utf-8")

    # language chooser at preview root
    links = "".join(f'<li><a href="{l}/index.html">{LANG_NAMES[l]}</a></li>' for l in LANGS)
    (pdir / "index.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>THE FACES · preview</title><style>body{{font-family:Montserrat,Arial,sans-serif;background:#0a0a0a;color:#fff;display:grid;place-items:center;min-height:100vh;margin:0}}a{{color:#fff;font-size:22px;line-height:2.2;text-decoration:none;border-bottom:1px solid #555}}ul{{list-style:none;padding:0;text-align:center}}</style></head><body><ul>{links}</ul></body></html>', encoding="utf-8")

    # SEO map
    lines = ["# THE FACES · Estructura del sitio y SEO (generado por src/build.py)", "",
             f"Dominio: {a.site} · Idiomas: " + ", ".join(f"{LANG_NAMES[l]} (`{'/' if l == 'en' else '/' + l + '/'}`)" for l in LANGS), "",
             "## Páginas y bloques", "", "| Página | URL (EN) | Bloques en Tilda, en orden |", "|---|---|---|"]
    for p in PAGES:
        blocks = list(p["blocks"])
        if p["slug"]:
            blocks.insert(1, f"pages/{p['slug']}-intro")
        lines.append(f"| {p['slug'] or 'home'} | `/{p['slug']}` | " + " → ".join(f"`{b}`" for b in blocks) + " |")
    lines += ["", "En las páginas interiores usa `pages/<página>-01-header.html` y `pages/<página>-15-footer.html` (sus enlaces de idioma apuntan a la misma página en otro idioma).", "",
              "## Títulos y descripciones por idioma", ""]
    for lang in LANGS:
        lines += [f"### {LANG_NAMES[lang]}", "", "| URL | Title | Description |", "|---|---|---|"]
        for (lg, url, title, desc, _, slug) in seo_rows:
            if lg == lang:
                path = ("/" if lang == "en" else f"/{lang}/") + slug
                lines.append(f"| `{path}` | {title} ({len(title)}) | {desc} ({len(desc)}) |")
        lines.append("")
    (ROOT / "SEO_ESTRUCTURA.md").write_text("\n".join(lines), encoding="utf-8")

    n = sum(1 for _ in tdir.rglob("*.html"))
    print(f"assets base: {assets_base}\nTilda files: {n}\nsite head: {(tdir / '00-site-head.html').stat().st_size} bytes\npreview pages: {sum(1 for _ in pdir.rglob('index.html'))}")


if __name__ == "__main__":
    main()
