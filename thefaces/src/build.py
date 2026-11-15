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
from content_ui import UI, LANGS, DUR, LANG_NAMES, HTML_LANG, OG_LOCALE  # noqa: E402
from content_rich import SENSES, ELEMENTS, CATS, DESC, FAQ  # noqa: E402
from content_seo import PAGES  # noqa: E402
from menu import BOOK, MENU, SIGNATURES, GIFTS, SALONS, LINKS, GALLERY, ALTEGIO  # noqa: E402
from content_waterfall import WF_UI, WF_RITUALS  # noqa: E402
from content_posts import POSTS, P3_INTRO, EXCERPTS  # noqa: E402
UI.update(WF_UI)
from content_fr_uk import (UI_X, UI_ALL, SENSES_X, ELEMENTS_X, CATS_X, DESC_X, FAQ_X, PAGES_X, WF_X,  # noqa: E402
                           DUR_X, LANG_NAMES_X, OG_X)


def _merge_fr_uk():
    """Append French and Ukrainian to every list (lists keep the order of LANGS)."""
    LANGS.extend(["fr", "uk"])
    missing = [k for k in UI if k not in UI_X and k not in UI_ALL]
    assert not missing, f"missing fr/uk for: {missing}"
    for k, v in UI.items():
        if k in UI_X:
            v.extend(UI_X[k])
    UI.update(UI_ALL)
    for s in SENSES:
        for f in ("name", "line", "text"):
            s[f] = s[f] + SENSES_X[s["id"]][f]
    for e in ELEMENTS:
        for f in ("name", "t", "when", "inc"):
            e[f] = e[f] + ELEMENTS_X[e["id"]][f]
    CATS[:] = [(cid, names + CATS_X[cid]) for cid, names in CATS]
    for k in DESC:
        DESC[k] = DESC[k] + DESC_X[k]
    FAQ[:] = [(q + FAQ_X[i][0], a + FAQ_X[i][1]) for i, (q, a) in enumerate(FAQ)]
    for p in PAGES:
        p["title"] = p["title"] + PAGES_X[p["slug"]]["title"]
        p["desc"] = p["desc"] + PAGES_X[p["slug"]]["desc"]
    for r in WF_RITUALS:
        x = WF_X[r["key"]]
        r["line"] = r["line"] + x["line"]
        if r["steps"]:
            r["steps"] = r["steps"] + x["steps"]
            r["for"] = r["for"] + x["for"]
    DUR.update(DUR_X)
    LANG_NAMES.update(LANG_NAMES_X)
    HTML_LANG.update({"fr": "fr", "uk": "uk"})
    OG_LOCALE.update(OG_X)
    n = len(LANGS)
    bad = [k for k, v in UI.items() if len(v) != n]
    assert not bad, f"wrong length: {bad}"


_merge_fr_uk()
from content_elements import ELEMENTS_FIX  # noqa: E402
for _e in ELEMENTS:  # programs exactly as the founders describe them
    if _e["id"] in ELEMENTS_FIX:
        _e.update(ELEMENTS_FIX[_e["id"]])
from content_desc import DESC_FIX, LOVE_HEAD  # noqa: E402
DESC.update(DESC_FIX)  # menu descriptions as in the salon catalog
for _e in ELEMENTS:
    if _e["id"] == "el-love":
        _e["inc"] = [" · ".join(x.split(" · ")[:3] + [h]) for x, h in zip(_e["inc"], LOVE_HEAD)]
from content_landing import LANDINGS, LANDING_UI  # noqa: E402
from content_extra import (EXTRA_UI, JO_CATS, POST_CATKEY, CONTROLLER, PRIVACY, PAGE_PRIVACY, PAGE_CERTS,  # noqa: E402
                           TERMS, TERMS_HEAD, PAGE_TERMS)
UI.update(LANDING_UI)
UI.update(EXTRA_UI)
from content_extra import BLOG_UI  # noqa: E402
UI.update(BLOG_UI)
from content_privacy2 import COMPANY, CO_UI, WHO, CONTROLLER_LINE, EXTRA_SECTIONS  # noqa: E402
UI.update(CO_UI)
from content_seo2 import TITLES, HERO_H1, SALON_TXT, SEO2_UI  # noqa: E402
UI.update(SEO2_UI)
from content_salon import SALON_PAGE, SALON_UI, SALON_IMG, SALON_RIBBON  # noqa: E402
UI.update(SALON_UI)

EXPLORE_UI = {
 "ex_label": ["Discover", "Узнать больше", "Descubre", "Entdecken", "ค้นพบ", "Jelajahi", "もっと知る", "Découvrir", "Дізнатися більше"],
 "ex_h2": ["Everything about THE FACES.", "Всё о THE FACES.", "Todo sobre THE FACES.", "Alles über THE FACES.", "ทุกอย่างเกี่ยวกับ THE FACES", "Semua tentang THE FACES.", "THE FACESのすべて。", "Tout sur THE FACES.", "Усе про THE FACES."],
 "ex_menu": ["56 treatments with prices, from IDR 200,000", "56 процедур с ценами, от IDR 200 000", "56 tratamientos con precio, desde IDR 200.000", "56 Behandlungen mit Preisen, ab IDR 200.000", "56 ทรีตเมนต์พร้อมราคา เริ่ม IDR 200,000", "56 perawatan dengan harga, mulai IDR 200.000", "56の施術と料金、IDR 200,000から", "56 soins avec prix, dès IDR 200 000", "56 процедур з цінами, від IDR 200 000"],
 "ex_gifts": ["Give a ritual and get up to 25% bonus", "Подарите ритуал и получите бонус до 25%", "Regala un ritual y recibe hasta un 25 % de bonus", "Ein Ritual schenken, bis zu 25 % Bonus", "มอบพิธีกรรมเป็นของขวัญ รับโบนัสสูงสุด 25%", "Hadiahkan ritual, bonus hingga 25%", "リチュアルを贈って最大25%のボーナス", "Offrez un rituel, jusqu'à 25 % de bonus", "Подаруйте ритуал і отримайте бонус до 25%"],
 "ex_founders": ["Anna and Evgenii Dubinin, 20+ years in spa", "Анна и Евгений Дубинины, 20+ лет в спа", "Anna y Evgenii Dubinin, más de 20 años en spa", "Anna und Evgenii Dubinin, 20+ Jahre Spa", "แอนนาและเยฟเกนี ดูบินิน ประสบการณ์สปา 20+ ปี", "Anna dan Evgenii Dubinin, 20+ tahun di spa", "アンナ＆エフゲニー・ドゥビニン、スパ歴20年以上", "Anna et Evgenii Dubinin, plus de 20 ans de spa", "Анна та Євген Дубініни, 20+ років у спа"],
 "ex_partners": ["Franchise, hotels and the coming Waterfall Spa", "Франшиза, отели и скоро Waterfall Spa", "Franquicia, hoteles y el próximo Waterfall Spa", "Franchise, Hotels und das kommende Waterfall Spa", "แฟรนไชส์ โรงแรม และ Waterfall Spa ที่กำลังจะเปิด", "Waralaba, hotel, dan Waterfall Spa yang segera hadir", "フランチャイズ、ホテル、そして近日オープンのWaterfall Spa", "Franchise, hôtels et le futur Waterfall Spa", "Франшиза, готелі та незабаром Waterfall Spa"],
 "ex_certs": ["Registered trademark and author's concept", "Зарегистрированная марка и авторская концепция", "Marca registrada y concepto de autor", "Eingetragene Marke und Autorenkonzept", "เครื่องหมายการค้าจดทะเบียนและแนวคิดลิขสิทธิ์", "Merek terdaftar dan konsep hak cipta", "登録商標と著作権のあるコンセプト", "Marque déposée et concept d'auteur", "Зареєстрована марка та авторська концепція"],
 "ex_journal": ["Guides to face massage, head spa and rituals", "Гиды по массажу лица, хэд-спа и ритуалам", "Guías de masaje facial, head spa y rituales", "Ratgeber zu Gesichtsmassage, Head Spa und Ritualen", "คู่มือนวดหน้า เฮดสปา และพิธีกรรม", "Panduan pijat wajah, head spa, dan ritual", "フェイスマッサージ、ヘッドスパ、リチュアルのガイド", "Guides du massage du visage, head spa et rituels", "Гіди з масажу обличчя, хед-спа та ритуалів"],
}
UI.update(EXPLORE_UI)
from content_reviews import REVIEWS, REVIEWS_UI  # noqa: E402
UI.update(REVIEWS_UI)
UI["swipe"] = ["Swipe", "Листайте", "Desliza", "Wischen", "ปัดดู", "Geser", "スワイプ", "Faites glisser", "Гортайте"]
UI["hero_h1"] = HERO_H1
for _P in PAGES:  # one main search intent per page (no cannibalisation)
    if _P["slug"] in TITLES:
        _P.update({k: v for k, v in TITLES[_P["slug"]].items()})
    if _P["slug"] == "":  # short home: long sections live on their own pages, reached from the "Discover" tiles
        _P["blocks"] = ["01-header", "02-hero", "03-philosophy", "04-senses", "05-elements", "06-signatures", "07-menu-builder", "08-gallery",
                        "17-instagram", "09-salons", "23-reviews", "22-explore", "10-founders", "18-certificates", "11-gifts", "12-partners",
                        "16-waterfall", "13-journal", "14-faq", "15-footer"]
    elif _P["slug"] in ("ubud", "sanur"):
        _P["blocks"] = ["01-header", "salon-" + _P["slug"], "17-instagram", "15-footer"]
    elif _P["slug"] == "five-elements":
        _P["blocks"] = ["01-header", "04-senses", "05-elements", "06-signatures", "14-faq", "15-footer"]
    elif _P["slug"] == "founders":
        _P["blocks"] = ["01-header", "10-founders", "18-certificates", "03-philosophy", "15-footer"]
    elif _P["slug"] == "partners":
        _P["blocks"] = ["01-header", "12-partners", "16-waterfall", "15-footer"]
    elif _P["slug"] == "certificates":
        _P["blocks"] = ["01-header", "18-certificates", "15-footer"]
LANDING = {L["slug"]: L for L in LANDINGS}
for _P in PAGES:  # certificates after the founders; full journal list on the journal page
    if "10-founders" in _P["blocks"] and "18-certificates" not in _P["blocks"]:
        _P["blocks"].insert(_P["blocks"].index("10-founders") + 1, "18-certificates")
    if _P["slug"] == "journal":
        _P["blocks"] = ["01-header", "21-journal-all", "15-footer"]
PAGES.append({"slug": "certificates", "blocks": ["01-header", "18-certificates", "10-founders", "15-footer"],
              "title": PAGE_CERTS["title"], "desc": PAGE_CERTS["desc"]})
PAGES.append({"slug": "privacy", "blocks": ["01-header", "19-privacy", "15-footer"], "title": PAGE_PRIVACY["title"], "desc": PAGE_PRIVACY["desc"]})
PAGES.append({"slug": "terms", "blocks": ["01-header", "20-terms", "15-footer"], "title": PAGE_TERMS["title"], "desc": PAGE_TERMS["desc"]})
for _P in PAGES:  # Instagram preview right after the gallery
    if "08-gallery" in _P["blocks"] and "17-instagram" not in _P["blocks"]:
        _P["blocks"].insert(_P["blocks"].index("08-gallery") + 1, "17-instagram")
for _L in LANDINGS:  # one SEO page per treatment family, placed after the menu page
    PAGES.insert(2, {"slug": _L["slug"], "blocks": ["01-header", "landing", "06-signatures", "09-salons", "14-faq", "15-footer"],
                     "title": _L["title"], "desc": _L["desc"]})
# Order of the language switcher (codes in LANGS keep the order of the content lists).
SWITCH = ["en", "es", "fr", "de", "ru", "uk", "ja", "th", "id"]

E = lambda s: html.escape(str(s), quote=True)  # noqa: E731
LI = {l: i for i, l in enumerate(LANGS)}
GROUP = {"en": ",", "th": ",", "ja": ",", "ru": " ", "uk": " ", "fr": " ", "es": ".", "de": ".", "id": "."}


class Ctx:
    def __init__(self, lang, mode, slug, site, assets_base, assets_map):
        self.lang, self.mode, self.slug, self.site = lang, mode, slug, site
        self.assets_base, self.assets_map = assets_base, assets_map
        self.i = LI[lang]
        self.lang_urls = {}

    def lang_url(self, lang):
        return self.lang_urls.get(lang) or self.url(self.slug, lang=lang)

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
        if self.mode == "wp":
            return "{{TF_ASSETS}}" + name
        return self.assets_map.get(name) or self.assets_base.rstrip("/") + "/" + name

    def depth(self):  # preview/<lang>/<slug>/index.html -> 3 (or 2 for home); nested slugs add levels
        return 2 + (len(self.slug.split("/")) if self.slug else 0)

    def post_slug(self, pid, lang=None):
        lang = lang or self.lang
        base = ARTICLE[pid]["slug"]
        return base if lang == "en" else f"{base}-{lang}"

    def post_url(self, pid, lang=None):
        lang = lang or self.lang
        if self.mode == "wp":
            return "{{TF_HOME}}/" + self.post_slug(pid, lang) + "/"
        if self.mode == "preview":
            return self.url("journal/" + self.post_slug(pid, lang), lang=lang)
        return self.url("journal", lang=lang)

    def url(self, slug="", anchor="", lang=None):
        lang = lang or self.lang
        if self.mode == "preview":
            path = "../" * (self.depth() - 1) + lang + "/" + (slug + "/" if slug else "") + "index.html"
        elif self.mode == "wp":
            path = "{{TF_HOME}}" + ("/" if lang == "en" else f"/{lang}/") + (slug + "/" if slug else "")
        else:
            path = ("/" if lang == "en" else f"/{lang}/") + (slug if slug else "")
        return path + (("#" + anchor) if anchor else "")

    def abs_url(self, slug, lang=None):
        lang = lang or self.lang
        return self.site.rstrip("/") + ("/" if lang == "en" else f"/{lang}/") + slug


def label(ctx, n, key):
    num = f'<span class="n">{n:02d} —</span>' if n else ""
    return f'<p class="eyebrow rv">{num}{E(ctx.t(key))}</p>'


def book(where, item="", salon=None):
    """Attributes for every booking link: straight to Altegio. With a salon, its own booking page; otherwise the
    shared page where the guest chooses Ubud or Sanur."""
    return (f'href="{E(BOOK[salon]) if salon else ALTEGIO}" target="_blank" rel="noopener" data-book="{E(where)}"'
            + (f' data-item="{E(item)}"' if item else "") + (f' data-salon="{salon}"' if salon else ""))


def page_salon(ctx):
    return ctx.slug if ctx.slug in SALONS else None


ITEM = {m[1]: m for m in MENU}
CUR = ' aria-current="true"'
NO_INTRO = {"landing", "21-journal-all", "salon-ubud", "salon-sanur"}
ON = ' class="on"'

SOCIAL_SVG = {
 "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zm0 4.8a5 5 0 100 10 5 5 0 000-10zm0 8.2a3.2 3.2 0 110-6.4 3.2 3.2 0 010 6.4zm5.2-9.6a1.2 1.2 0 100 2.4 1.2 1.2 0 000-2.4z"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 11-.02 5 2.5 2.5 0 01.02-5zM3 9h4v12H3zM9.5 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.6c0-1.34-.03-3.06-1.86-3.06-1.87 0-2.15 1.46-2.15 2.96V21h-4z"/></svg>',
 "tiktok": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.6 5.8A4.3 4.3 0 0115.5 3h-3.1v12.4a2.6 2.6 0 11-2.6-2.6c.3 0 .5 0 .8.1V9.7a5.8 5.8 0 105 5.7V9.1a7.4 7.4 0 004.3 1.4V7.4a4.3 4.3 0 01-3.3-1.6z"/></svg>',
 "whatsapp": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.8 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.2.1-1.9-.1-.4-.1-1-.3-1.7-.6-3-1.3-4.9-4.3-5.1-4.5-.1-.2-1.2-1.6-1.2-3.1s.8-2.2 1-2.5c.3-.3.6-.4.8-.4h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.7 1.2 1.6 2 1.1 1 2 1.3 2.3 1.4.3.1.4.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.1.1.7-.1 1.4z"/></svg>',
 "email": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v14H3V5zm9 7L4.5 6.5v1.7L12 14l7.5-5.8V6.5L12 12z"/></svg>',
}

# ------------------------------------------------------------------ blocks

def b_header(ctx):
    T = {"lang": ctx.lang, "ft_thanks": ctx.t("ft_thanks")}
    def dd(label, entries, cls=""):
        li = "".join(f'<li><a href="{E(u)}"><img src="{ctx.asset(img)}" alt="" loading="lazy"><span>{E(t)}</span></a></li>' for t, u, img in entries)
        return (f'<div class="dd{cls}"><button type="button" aria-haspopup="true">{E(label)} <span aria-hidden="true">▾</span></button>'
                f'<ul class="dd-panel">{li}</ul></div>')
    treat = [(ctx.pick(L["nav"]), ctx.url(L["slug"]), L["img"]) for L in LANDINGS]
    treat += [(ctx.t("nav_elements"), ctx.url("five-elements"), "g12-proc-s.webp"), (ctx.t("nav_menu"), ctx.url("menu"), "g04-interior.webp")]
    salons = [("Ubud", ctx.url("ubud"), "g06-interior.webp"), ("Sanur", ctx.url("sanur"), "g07-interior-s.webp")]
    about = [(ctx.t("nav_founders"), ctx.url("founders"), "founders.webp"), (ctx.t("nav_senses"), ctx.url("five-elements", "senses"), "sense-hearing.webp"),
             (ctx.t("nav_certs"), ctx.url("certificates"), "cert-trademark.webp"), (ctx.t("nav_partners"), ctx.url("partners"), "waterfall-3.webp")]
    navh = (dd(ctx.t("nav_treat"), treat) + f'<a href="{E(ctx.url("menu"))}">{E(ctx.t("nav_menu"))}</a>'
            + dd(ctx.t("nav_salons"), salons, " dd-sm") + dd(ctx.t("nav_about"), about, " dd-r")
            + f'<a href="{E(ctx.url("gift-certificates"))}">{E(ctx.t("nav_gifts"))}</a><a href="{E(ctx.url("journal"))}">{E(ctx.t("nav_journal"))}</a>')
    page_slug = ctx.slug
    langs = "".join(f'<li><a href="{E(ctx.lang_url(l))}" hreflang="{l}" lang="{l}"{CUR if l == ctx.lang else ""}>{E(LANG_NAMES[l])}</a></li>' for l in SWITCH)
    mlangs = "".join(f'<a href="{E(ctx.lang_url(l))}" hreflang="{l}" lang="{l}"{CUR if l == ctx.lang else ""}>{E(LANG_NAMES[l])}</a>' for l in SWITCH)
    items = [("nav_menu", ctx.url("menu"), "g01-face.webp"),
             ("nav_elements", ctx.url("five-elements"), "g12-proc-s.webp"),
             ("nav_senses", ctx.url("five-elements", "senses"), "sense-hearing.webp"),
             ("nav_salons", ctx.url("ubud"), "g06-interior.webp"),
             ("nav_founders", ctx.url("founders"), "founders.webp"),
             ("nav_certs", ctx.url("certificates"), "cert-trademark.webp"),
             ("nav_gifts", ctx.url("gift-certificates"), "g08-interior.webp"),
             ("nav_partners", ctx.url("partners"), "waterfall-3.webp"),
             ("nav_journal", ctx.url("journal"), "g10-proc-s.webp")]
    mlinks = "".join(f'<li><a href="{E(u)}" data-img="{k}"><span class="i">{n + 1:02d}</span>{E(ctx.t(key))}</a></li>' for n, (key, u, k) in enumerate(items))
    mimgs = "".join(f'<img src="{ctx.asset(img)}" alt="" loading="lazy" data-for="{n}"{ON if n == 0 else ""}>' for n, (key, u, img) in enumerate(items))
    mnav = f'''<div class="mn-grid">
  <ol class="mn-links">{mlinks}</ol>
  <div class="mn-side"><div class="mn-img">{mimgs}</div>
   <p class="eyebrow">Five Elements. Guided by Love.</p>
   <a class="btn" {book("mobile-menu", salon=page_salon(ctx))}>{E(ctx.t("book_cta"))}</a>
   <p class="mn-treat">{"".join(f'<a href="{E(ctx.url(L["slug"]))}">{E(ctx.pick(L["nav"]))}</a>' for L in LANDINGS)}<a href="{E(ctx.url("ubud"))}">Ubud</a><a href="{E(ctx.url("sanur"))}">Sanur</a></p>
   <p class="mn-contact"><a href="https://wa.me/{SALONS["ubud"]["wa"]}">WhatsApp Ubud</a> · <a href="https://wa.me/{SALONS["sanur"]["wa"]}">WhatsApp Sanur</a> · <a href="{LINKS["instagram"]}">Instagram</a> · <a href="{LINKS["tiktok"]}">TikTok</a> · <a href="{LINKS["linkedin"]}">LinkedIn</a></p>
  </div>
 </div>'''
    return f'''<script type="application/json" id="tf-i18n">{json.dumps(T, ensure_ascii=False)}</script>
<header class="top">
 <div class="bar">
  <a href="{E(ctx.url())}" class="logo" aria-label="THE FACES"><img src="{ctx.asset("logo-white.png")}" alt="THE FACES" width="600" height="338"></a>
  <nav aria-label="Main">{navh}</nav>
  <div class="langsel"><button type="button" aria-expanded="false" aria-label="{E(ctx.t("language"))}">{ctx.lang.upper()} <span aria-hidden="true">▾</span></button><ul>{langs}</ul></div>
  <a class="btn book" {book("header", salon=page_salon(ctx))}>{E(ctx.t("book"))}</a>
  <button type="button" class="burger" aria-label="{E(ctx.t("open_menu"))}"><span></span><span></span><span></span></button>
 </div>
</header>
<div class="mnav" role="dialog" aria-label="{E(ctx.t("open_menu"))}">
 <div class="mn-top"><img src="{ctx.asset("logo-white.png")}" alt="THE FACES" width="600" height="338"><button type="button" class="close" aria-label="{E(ctx.t("close"))}">×</button></div>
 {mnav}
 <div class="langs">{mlangs}</div>
</div>'''


def b_hero(ctx):
    return f'''<section class="hero" aria-label="THE FACES">
 <video autoplay muted loop playsinline preload="metadata" poster="{ctx.asset("hero-poster-2.jpg")}"><source src="{ctx.asset("hero-854.mp4")}" type="video/mp4" media="(max-width: 760px)"><source src="{ctx.asset("hero-1280.mp4")}" type="video/mp4"></video>
 <button type="button" class="sound" data-off="{E(ctx.t("sound_off"))}" data-on="{E(ctx.t("sound_on"))}">{E(ctx.t("sound_off"))}</button>
 <div class="wrap in">
  <h1 class="eyebrow">{E(ctx.t("hero_h1"))}</h1>
  <p class="display" aria-hidden="true"><span class="line"><span>{E(ctx.t("hero_t1"))}</span></span><span class="line"><span>{E(ctx.t("hero_t2"))}</span></span></p>
  <p class="lead sub">{E(ctx.t("hero_sub"))}</p>
  <div class="ctas">
   <a class="btn solid" {book("hero")}>{E(ctx.t("book_cta"))}</a>
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
  <div class="sn-list">{items}</div><p class="swipe-hint wrap">{E(ctx.t("swipe"))}</p>
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
     <div class="meta"><span>{E(ctx.t("about3h"))} · {ctx.price(it[4])}</span><a class="btn" {book("element", it[2])}>{E(ctx.t("book_ritual"))}</a></div>
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
   <h3>{E(it[2])}</h3><p class="pr">{price_line(ctx, it)}</p><p>{E(desc)}</p>
   <a class="btn" {book("signature", it[2])}>{E(ctx.t("book"))}</a></article>''')
    return f'''<section class="sig sec" id="signature">
 <div class="wrap sec-head">
  <div>{label(ctx, 4, "sg_label")}<h2 class="h2 rv d1">{E(ctx.t("sg_h2"))}</h2></div>
  <div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><p class="muted rv d2" style="max-width:420px">{E(ctx.t("sg_intro"))}</p>
   <div class="railnav"><button type="button" class="prev" aria-label="{E(ctx.t("prev"))}">←</button><button type="button" class="next" aria-label="{E(ctx.t("next"))}">→</button></div></div>
 </div>
 <div class="rail">{"".join(cards)}</div>
</section>'''


def price_line(ctx, it):
    """Duration · price, with Sanur shown separately when Altegio has a different value."""
    cat, iid, name, d, p, only, diff = it
    base = (ctx.dur(d) + " · " if d else "") + ctx.price(p)
    if diff and "sanur" in diff:
        sd, sp = diff["sanur"]
        return f"Ubud {base} · Sanur " + (ctx.dur(sd) + " · " if sd else "") + ctx.price(sp)
    return base


CAT_IMG = {"face": "g01-face.webp", "air": "g12-proc-s.webp", "head": "g10-proc-s.webp", "skin": "g11-proc-s.webp",
           "prog": "sense-hearing.webp", "men": "g09-proc-s.webp", "pack": "g04-interior.webp", "two": "g02-face-s.webp",
           "body": "sense-touch.webp"}


def menu_rows(ctx, items):
    rows = []
    for m in items:
        cat, iid, nm, d, p, only, diff = m
        if only:
            badge = f'<span class="badge">{E(ctx.t("only_in", salon=", ".join(SALONS[x]["name"] for x in only)))}</span>'
        else:
            badge = '<span class="sal" title="Ubud · Sanur"><i>Ubud</i><i>Sanur</i></span>'
        ds = f'<p class="ds">{E(ctx.pick(DESC[iid]))}</p>' if iid in DESC else '<p class="ds"></p>'
        if diff and "sanur" in diff:
            sd, sp = diff["sanur"]
            du = (f'Ubud {ctx.dur(d)} · Sanur {ctx.dur(sd)}' if sd != d else ctx.dur(d))
            pc = (f'<span>Ubud {ctx.price(p)}</span><span>Sanur {ctx.price(sp)}</span>' if sp != p else ctx.price(p))
        else:
            du, pc = (ctx.dur(d) if d else ""), ctx.price(p)
        rows.append(f'<li class="item"><div class="l1"><p class="nm">{E(nm)}{badge}</p><span class="dots" aria-hidden="true"></span>'
                    f'<span class="pc">{pc}</span></div><div class="l2">{ds}<span class="du">{du}</span></div></li>')
    return "".join(rows)


def b_landing(ctx, page):
    """SEO landing page: H1, intro, clear booking CTA, the treatments of that family with prices, related pages."""
    L = LANDING[page["slug"]]
    h1 = h1_of(ctx.pick(L["title"]))
    cats = []
    offers = []
    for cid, names in CATS:
        if cid not in L["cats"]:
            continue
        items = [m for m in MENU if m[0] == cid]
        cats.append(f'<h3 class="ld-cat">{E(ctx.pick(names))}</h3><ul class="items">{menu_rows(ctx, items)}</ul>')
        offers += [{"@type": "Offer", "price": m[4], "priceCurrency": "IDR", "itemOffered": {"@type": "Service", "name": m[2]}} for m in items]
    explore = [(ctx.pick(o["nav"]), ctx.url(o["slug"])) for o in LANDINGS if o["slug"] != L["slug"]]
    explore += [(ctx.t("nav_elements"), ctx.url("five-elements")), (ctx.t("nav_menu"), ctx.url("menu")), (ctx.t("nav_gifts"), ctx.url("gift-certificates"))]
    chips = "".join(f'<a href="{E(u)}">{E(t)}</a>' for t, u in explore)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "THE FACES", "item": ctx.abs_url("")},
            {"@type": "ListItem", "position": 2, "name": h1, "item": ctx.abs_url(L["slug"])}]},
        {"@type": "OfferCatalog", "name": h1, "url": ctx.abs_url(L["slug"]), "itemListElement": offers}]}
    sid = L["slug"]
    return f'''<section class="ld-hero">
 <div class="wrap ld-grid">
  <div>
   <nav aria-label="Breadcrumb" class="eyebrow crumbs"><a href="{E(ctx.url())}">THE FACES</a> <span aria-hidden="true">/</span> <span>{E(ctx.pick(L["nav"]))}</span></nav>
   <h1 class="h2">{E(h1)}</h1>
   <p class="lead">{E(ctx.pick(L["p1"]))}</p>
   <div class="ld-cta">
    <a class="btn" {book("landing-" + sid, ctx.pick(L["nav"]))}>{E(ctx.t("book_cta"))}</a>
    <span class="ld-from">{E(ctx.t("chip_from", p=ctx.price(L["from"])))}</span>
   </div>
   <p class="ld-salons">Ubud · Sanur · Bali</p>
  </div>
  <figure class="ld-img mask rv"><img src="{ctx.asset(L["img"])}" alt="{E(h1)}" loading="eager"></figure>
 </div>
</section>
<section class="sec ld-body">
 <div class="wrap ld-cols">
  <div class="ld-text">
   <p class="eyebrow">{E(ctx.t("ld_prices"))}</p>
   <p class="lead">{E(ctx.pick(L["p2"]))}</p>
  </div>
  <div class="ld-menu">{"".join(cats)}</div>
 </div>
 <div class="wrap">
  <div class="menu-cta ld-final">
   <a class="btn darksolid" {book("landing-bottom-" + sid, ctx.pick(L["nav"]))}>{E(ctx.t("book_online"))} ↗</a>
   <p>{E(ctx.t("book_note"))}</p>
  </div>
  <div class="ld-explore"><p class="eyebrow">{E(ctx.t("ld_explore"))}</p><div class="chips2">{chips}</div></div>
 </div>
 <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</section>'''


def b_menu(ctx):
    tabs, cats = [], []
    total = len(CATS)
    for k, (cid, names) in enumerate(CATS):
        items = [m for m in MENU if m[0] == cid]
        name = ctx.pick(names)
        tabs.append(f'<button type="button" role="tab" data-tab="{cid}" aria-selected="{"true" if k == 0 else "false"}" aria-controls="cat-{cid}">'
                    f'<span class="i">{k + 1:02d}</span><span class="t">{E(name)}</span><span class="c">{len(items)}</span></button>')
        rows = [menu_rows(ctx, items)]
        cats.append(f'''<div class="cat" id="cat-{cid}" role="tabpanel"{"" if k == 0 else " hidden"}>
    <figure class="cat-head"><img src="{ctx.asset(CAT_IMG[cid])}" alt="" loading="lazy"><figcaption><span class="eyebrow">{k + 1:02d} / {total:02d}</span><h3>{E(name)}</h3></figcaption></figure>
    <ul class="items">{"".join(rows)}</ul>
   </div>''')
    return f'''<section class="menu-sec sec" id="menu">
 <div class="wrap sec-head">
  <div>{label(ctx, 5, "mn_label")}<h2 class="h2 rv d1">{E(ctx.t("mn_h2"))}</h2></div>
  <p class="muted rv d2">{E(ctx.t("mn_intro"))}</p>
 </div>
 <div class="wrap mn-layout">
  <div class="mn-cats tabs" role="tablist">{"".join(tabs)}</div>
  <div class="mn-panels">
   {"".join(cats)}
   <div class="menu-cta">
    <a class="btn darksolid" {book("menu")}>{E(ctx.t("book_online"))} ↗</a>
    <p>{E(ctx.t("book_note"))}</p>
   </div>
   <p class="note">{E(ctx.t("mn_note"))}</p>
  </div>
 </div>
</section>'''


def b_gallery(ctx):
    alt = E(ctx.t("ga_alt"))
    row = lambda g: "".join(f'<img src="{ctx.asset(x + ".webp")}" alt="{alt if i < len(g) else ""}" loading="lazy">' for i, x in enumerate(g + g))  # noqa: E731
    g1, g2 = GALLERY[:7], GALLERY[6:] + GALLERY[:1]
    return f'''<section class="gal sec" aria-labelledby="tf-gal-h">
 <div class="wrap head"><div><p class="eyebrow rv">{E(ctx.t("ga_label"))}</p><h2 class="h2 rv d1" id="tf-gal-h" style="margin-top:18px">{E(ctx.t("ga_h2"))}</h2></div>
  <a class="link rv d2" href="{LINKS["instagram"]}" target="_blank" rel="noopener">Instagram @thefacesubud ↗</a></div>
 <div class="strip">{row(g1)}</div>
 <div class="strip rev">{row(g2)}</div>
</section>'''


IG_ACCOUNTS = [
    ("thefacesubud", "The Faces Ubud", "instagram", ["g01-face", "g04-interior", "g09-proc-s", "g02-face-s", "g06-interior", "g12-proc-s", "g10-proc-s", "g08-interior", "dsc"]),
    ("thefacesspaubud", "The Faces Spa Ubud", "instagram_spa", ["g03-face-s", "waterfall-3", "g11-proc-s", "sense-smell", "g05-interior-s", "founders", "sense-hearing", "g07-interior-s", "waterfall"]),
]


def b_instagram(ctx):
    cards = []
    for handle, name, key, imgs in IG_ACCOUNTS:
        url = LINKS[key]
        grid = "".join(f'<a href="{url}" target="_blank" rel="noopener" aria-label="@{handle}"><img src="{ctx.asset(i + ".webp")}" alt="" loading="lazy"></a>' for i in imgs)
        cards.append(f'''<article class="ig-card rv">
   <header><span class="ig-av"><img src="{ctx.asset("logo-white.png")}" alt=""></span>
    <div class="ig-id"><b>@{handle}</b><span>{name} · Bali</span></div>
    <a class="ig-follow" href="{url}" target="_blank" rel="noopener">{E(ctx.t("ig_follow"))}</a></header>
   <div class="ig-grid">{grid}</div>
   <a class="ig-more" href="{url}" target="_blank" rel="noopener">instagram.com/{handle} ↗</a>
  </article>''')
    return f'''<section class="ig sec" id="instagram">
 <div class="wrap sec-head">
  <div><p class="eyebrow rv">Instagram · TikTok · LinkedIn</p><h2 class="h2 rv d1" style="margin-top:22px">{E(ctx.t("ig_h2"))}</h2></div>
  <div><p class="muted rv d2">{E(ctx.t("ig_intro"))}</p>
   <div class="ig-social rv d2">
    <a href="{LINKS["tiktok"]}" target="_blank" rel="noopener">{SOCIAL_SVG["tiktok"]}<span>TikTok @thefaces.bali</span></a>
    <a href="{LINKS["linkedin"]}" target="_blank" rel="noopener">{SOCIAL_SVG["linkedin"]}<span>LinkedIn · THE FACES</span></a>
   </div></div>
 </div>
 <div class="wrap ig-cards">{"".join(cards)}</div>
</section>'''


def b_certificates(ctx):
    certs = [("cert-trademark.webp", "cert1_t", "cert1_d", 970, 1562), ("cert-copyright.webp", "cert2_t", "cert2_d", 1098, 1564)]
    cards = "".join(f'''<figure class="cert rv d{k}"><a href="{ctx.asset(img)}" target="_blank" rel="noopener" class="cert-img"><img src="{ctx.asset(img)}" alt="{E(ctx.t(t))} · {E(ctx.t(d))}" loading="lazy" width="{w}" height="{h}"></a>
   <figcaption><h3>{E(ctx.t(t))}</h3><p>{E(ctx.t(d))}</p><a class="link" href="{ctx.asset(img)}" target="_blank" rel="noopener">{E(ctx.t("cert_open"))} ↗</a></figcaption></figure>''' for k, (img, t, d, w, h) in enumerate(certs))
    return f'''<section class="certs sec" id="certificates">
 <div class="wrap sec-head">
  <div><p class="eyebrow rv">{E(ctx.t("cert_label"))}</p><h2 class="h2 rv d1">{E(ctx.t("cert_h2"))}</h2></div>
  <p class="muted rv d2">{E(ctx.t("cert_intro"))}</p>
 </div>
 <div class="wrap cert-grid">{cards}</div>
</section>'''


def b_privacy(ctx):
    secs = list(ctx.pick(PRIVACY))
    secs[0] = (secs[0][0], ctx.pick(WHO))
    secs = secs[:-1] + list(ctx.pick(EXTRA_SECTIONS)) + secs[-1:]
    email = COMPANY["email"]
    body = ""
    for n, (h, t) in enumerate(secs):
        anc = ' id="cookies"' if n == 2 else (' id="rights"' if n == len(secs) - 1 else "")
        txt = E(t.replace("{c}", CONTROLLER_LINE)).replace(E("{e}"), f'<a href="mailto:{email}">{email}</a>').replace("{e}", f'<a href="mailto:{email}">{email}</a>')
        body += f'<h2{anc}>{n + 1:02d}. {E(h)}</h2><p>{txt}</p>'
    salons = " · ".join(f'{v["name"]}: {v["addr"]}, {v["tel"]}' for v in SALONS.values())
    rows = [("co_controller", COMPANY["controller"]), ("co_trading", COMPANY["trading"]), ("co_tax", ctx.t("co_tax_v")),
            ("co_address", COMPANY["address"]), ("co_country", ctx.t("co_country_v")),
            ("co_email", f'<a href="mailto:{email}">{email}</a>'), ("co_holder", COMPANY["holder"]),
            ("co_salons", E(salons)), ("co_sites", COMPANY["sites"])]
    card = "".join(f'<div><dt>{E(ctx.t(k))}</dt><dd>{v if k in ("co_email", "co_salons") else E(v)}</dd></div>' for k, v in rows)
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "THE FACES", "email": email,
           "founder": {"@type": "Person", "name": COMPANY["controller"]},
           "address": {"@type": "PostalAddress", "streetAddress": "Jl. Bedugul No. 35, Sidakarya", "addressLocality": "Denpasar Selatan, Denpasar",
                       "addressRegion": "Bali", "addressCountry": "ID"}}
    return f'''<section class="legal-page"><div class="wrap post-body">
  <p class="eyebrow">{E(ctx.t("co_effective"))} · {E(ctx.t("pv_updated"))}</p>
  <div class="co-card"><p class="eyebrow">{E(ctx.t("co_h"))}</p><dl>{card}</dl></div>
  {body}
  <p><a class="link" href="{E(ctx.url("terms"))}">{E(ctx.t("lg_terms"))} →</a></p></div>
 <script type="application/ld+json">{json.dumps(org, ensure_ascii=False)}</script>
</section>'''


def b_terms(ctx):
    body = "".join(f'<h2 id="{anc}">{E(ctx.t(TERMS_HEAD[anc]))}</h2><p>{E(ctx.pick(txt).replace("{e}", LINKS["email"]))}</p>' for anc, txt in TERMS.items())
    return f'''<section class="legal-page"><div class="wrap post-body"><p class="eyebrow">{E(ctx.t("pv_updated"))}</p>{body}
  <p><a class="link" href="{E(ctx.url("privacy"))}">{E(ctx.t("lg_privacy"))} →</a></p>
  <div class="menu-cta" style="margin-top:40px"><a class="btn darksolid" {book("terms")}>{E(ctx.t("book_online"))} ↗</a><p>{E(ctx.t("book_note"))}</p></div></div></section>'''


# ------------------------------------------------------------------ journal articles

CAT_LABEL = {"elements": "jo_cat_elements", "story": "jo_cat_story", "news": "jo_cat_news"}
CAT_ORDER = ["face", "head", "rituals", "elements", "story", "news"]


def cat_name(ctx, key):
    return ctx.pick(JO_CATS[key]) if key in JO_CATS else ctx.t(CAT_LABEL[key])


def _art_written(pid, html_list, tkey):
    return {"title": lambda c: c.t(tkey), "excerpt": lambda c: c.pick(EXCERPTS[pid]), "body": lambda c: c.pick(html_list)}


def _art_elements_guide():
    def body(c):
        parts = [f"<p>{E(c.pick(P3_INTRO))}</p>"]
        for e in ELEMENTS:
            parts.append(f"<h2>{E(c.pick(e['name']))} · {E(c.pick(e['t']))}</h2><p>{E(c.pick(e['when']))}</p>"
                         f"<p><em>{E(c.t('el_inc'))}:</em> {E(c.pick(e['inc']))}</p>")
        return "\n".join(parts)
    return {"title": lambda c: c.t("jo_t3"), "excerpt": lambda c: c.pick(EXCERPTS["p3"]), "body": body}


def _art_element(e):
    item = next(m for m in MENU if m[1] == e["id"])

    def body(c):
        return (f"<p>{E(c.t('el_intro', p=c.price(item[4])))}</p>"
                f"<h2>{E(c.t('el_when'))}</h2><p>{E(c.pick(e['when']))}</p>"
                f"<h2>{E(c.t('el_inc'))}</h2><ul>" + "".join(f"<li>{E(x)}</li>" for x in c.pick(e["inc"]).split(" · ")) + "</ul>"
                f"<p><em>{E(c.t('about3h'))} · {c.price(item[4])}</em> · Ubud · Sanur</p>"
                f"<p>{E(c.t('se_intro'))}</p>")
    return {"title": lambda c: f"{c.pick(e['name'])}: {c.pick(e['t'])}", "excerpt": lambda c: c.pick(e["when"]), "body": body}


def _art_senses():
    def body(c):
        out = [f"<p>{E(c.t('se_intro'))}</p>"]
        for x in SENSES:
            out.append(f"<h2>{E(c.pick(x['name']))} · {E(c.pick(x['line']))}</h2><p>{E(c.pick(x['text']))}</p>")
        out.append(f"<p>{E(c.t('ph_p1'))}</p>")
        return "\n".join(out)
    return {"title": lambda c: c.t("se_h2").rstrip("."), "excerpt": lambda c: c.t("se_intro"), "body": body}


def _art_story():
    def body(c):
        return (f"<p>{E(c.t('fo_lead'))}</p><p>{E(c.t('fo_p1'))}</p><blockquote>{E(c.t('fo_quote'))}</blockquote>"
                f"<h2>{E(c.t('ph_h2'))}</h2><p>{E(c.t('ph_lead'))}</p><p>{E(c.t('ph_p1'))}</p>"
                f"<h2>2013 → Bali</h2><ul><li><strong>2013</strong> · {E(c.t('fo_t1'))}</li><li><strong>+5</strong> · {E(c.t('fo_t2'))}</li><li><strong>Bali</strong> · {E(c.t('fo_t3'))}</li></ul>"
                f"<h2>{E(c.t('cert_h2'))}</h2><p>{E(c.t('cert_intro'))}</p>")
    return {"title": lambda c: c.t("jo_story_t"), "excerpt": lambda c: c.t("fo_lead").split(". ")[0] + ".", "body": body}


def _art_waterfall():
    def body(c):
        out = [f"<p>{E(c.t('wf_intro'))}</p><p><em>{E(c.t('wf_motto'))}</em></p>"]
        for r in WF_RITUALS:
            out.append(f"<h2>{r['key'].title()} · {E(r['name'])}</h2><p>{E(c.pick(r['line']))}</p>")
            if r["steps"]:
                out.append("<ul>" + "".join(f"<li>{E(x)}</li>" for x in c.pick(r["steps"]).split(" · ")) + "</ul>")
        out.append(f"<p>{E(c.t('wf_note'))}</p>")
        return "\n".join(out)
    return {"title": lambda c: f"{c.t('wf_h2').rstrip('.')}: {c.t('wf_motto')}", "excerpt": lambda c: c.t("wf_intro").split(". ")[0] + ".", "body": body}


def _art_gifts():
    def body(c):
        rows = "".join(f"<li>{E(c.t('gi_pay', p=c.price(pay)))} → <strong>{c.price(get)}</strong> · {E(c.t('gi_bonus', n=round((get / pay - 1) * 100)))}</li>" for pay, get in GIFTS)
        return (f"<p>{E(c.t('gi_intro'))}</p><ul>{rows}</ul><h2>{E(c.t('lg_gift'))}</h2>"
                f"<p>{E(c.pick(TERMS['gift']))}</p><p>{E(c.t('mn_note'))}</p>")
    return {"title": lambda c: c.t("gi_h2"), "excerpt": lambda c: c.t("gi_intro"), "body": body}


CANON = {"p3": "five-elements", "el-air": "five-elements", "el-fire": "five-elements", "el-water": "five-elements", "el-earth": "five-elements",
         "el-love": "five-elements", "senses": "five-elements", "story": "founders", "gifts": "gift-certificates", "waterfall": "partners"}
SERVICE = {"p1": "face-massage", "p2": "head-spa", "el-love": "couples-spa"}


def article_service(art):
    return SERVICE.get(art["id"]) or CANON.get(art["id"]) or "menu"


def service_label(ctx, key):
    if key in LANDING:
        return ctx.pick(LANDING[key]["nav"])
    return h1_of(ctx.pick(next(P for P in PAGES if P["slug"] == key)["title"]))


def _build_articles():
    arts = []
    def add(pid, slug, cat, img, impl):
        impl.update({"id": pid, "slug": slug, "cat": cat, "img": img})
        arts.append(impl)
    add("p1", "myofascial-or-sculptural-face-massage", "face", "g01-face.webp", _art_written("p1", POSTS[0][5], "jo_t1"))
    add("p2", "shirodhara-hair-spa-ubud", "head", "g10-proc-s.webp", _art_written("p2", POSTS[1][5], "jo_t2"))
    add("p3", "five-elements-how-to-choose-your-ritual", "rituals", "g09-proc-s.webp", _art_elements_guide())
    imgs = {"el-air": "g10-proc-s.webp", "el-fire": "sense-sight.webp", "el-water": "g12-proc-s.webp", "el-earth": "g06-interior.webp", "el-love": "g02-face-s.webp"}
    for e in ELEMENTS:
        key = e["id"].split("-")[1]
        add(f"el-{key}", f"element-of-{key}-ritual", "elements", imgs[e["id"]], _art_element(e))
    add("senses", "five-senses-spa-ritual", "rituals", "sense-hearing.webp", _art_senses())
    add("story", "the-faces-story-anna-evgenii-dubinin", "story", "founders.webp", _art_story())
    add("waterfall", "the-faces-waterfall-spa-coming-soon", "news", "waterfall-3.webp", _art_waterfall())
    add("gifts", "spa-gift-certificates-bali", "news", "g08-interior.webp", _art_gifts())
    return arts


ARTICLES = []
ARTICLE = {}


def read_min(ctx, html_body):
    text = re.sub(r"<[^>]+>", " ", html_body)
    n = len(text) / 450 if ctx.lang in ("ja", "th") else len(text.split()) / 200
    return max(2, round(n))


def article_card(ctx, art, k=0, featured=False):
    title, ex = art["title"](ctx), art["excerpt"](ctx)
    mins = read_min(ctx, art["body"](ctx))
    cls = "post" + (" featured" if featured else "")
    return (f'<a class="{cls}" data-cat="{art["cat"]}" data-text="{E((title + " " + ex + " " + cat_name(ctx, art["cat"])).lower())}" href="{E(ctx.post_url(art["id"]))}">'
            f'<div class="ph"><img src="{ctx.asset(art["img"])}" alt="" loading="lazy"></div><div class="tx">'
            f'<p class="d"><span class="cat-tag">{E(cat_name(ctx, art["cat"]))}</span> {E(ctx.t("jo_read_min", n=mins))}</p>'
            f'<h3>{E(title)}</h3><p class="ex">{E(ex)}</p></div></a>')


def b_journal_all(ctx):
    counts = {k: sum(1 for a in ARTICLES if a["cat"] == k) for k in CAT_ORDER}
    chips = (f'<button type="button" class="on" data-jcat="">{E(ctx.t("jo_all_cat"))} <span>{len(ARTICLES)}</span></button>'
             + "".join(f'<button type="button" data-jcat="{k}">{E(cat_name(ctx, k))} <span>{counts[k]}</span></button>' for k in CAT_ORDER if counts[k]))
    cards = "".join(article_card(ctx, a, k, featured=(k == 0)) for k, a in enumerate(ARTICLES))
    h1 = h1_of(ctx.pick(next(P for P in PAGES if P["slug"] == "journal")["title"]))
    return f'''<section class="jo-all" data-count-tpl="{E(ctx.t("jo_count"))}">
 <div class="jo-hero"><div class="wrap">
  <nav aria-label="Breadcrumb" class="eyebrow crumbs"><a href="{E(ctx.url())}">THE FACES</a> <span aria-hidden="true">/</span> <span>{E(ctx.t("nav_journal"))}</span></nav>
  <h1 class="h2">{E(h1)}</h1><p class="lead">{E(ctx.t("jo_intro"))}</p>
  <div class="jo-tools">
   <label class="jo-search"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 2a8 8 0 105 14.3l5.4 5.4 1.4-1.4-5.4-5.4A8 8 0 0010 2zm0 2a6 6 0 110 12 6 6 0 010-12z"/></svg>
    <input type="search" placeholder="{E(ctx.t("jo_search"))}" aria-label="{E(ctx.t("jo_search"))}"></label>
  </div>
  <p class="eyebrow jo-bycat">{E(ctx.t("jo_by_cat"))}</p>
  <div class="jo-chips"><!--tf-chips-->{chips}<!--/tf-chips--></div>
 </div></div>
 <div class="wrap"><p class="jo-count" aria-live="polite"></p>
  <div class="posts jo-grid"><!--tf-posts-all-->{cards}<!--/tf-posts-all--></div>
  <p class="jo-none" hidden>{E(ctx.t("jo_none"))}</p>
 </div>
</section>'''


def salon_menu(ctx, sid):
    """Every treatment of one salon, grouped like the main menu, with that salon's duration and price."""
    out = []
    for n, (cid, names) in enumerate(CATS):
        rows = []
        for m in MENU:
            cat, iid, nm, du, pr, only, diff = m
            if cat != cid or (only and sid not in only):
                continue
            if diff and sid in diff:
                du, pr = diff[sid]
            here = f'<span class="badge">{E(ctx.t("sl_here"))}</span>' if only else ""
            ds = f'<small>{E(ctx.pick(DESC[iid]))}</small>' if iid in DESC else ""
            rows.append(f'<li><div><b>{E(nm)}</b>{here}{ds}</div><span>{(ctx.dur(du) + " · ") if du else ""}{ctx.price(pr)}</span></li>')
        if rows:
            out.append(f'<details class="sl-cat"{" open" if n < 2 else ""}><summary><span>{E(ctx.pick(names))}</span><em>{len(rows)}</em></summary><ul>{"".join(rows)}</ul></details>')
    return '<div class="sl-cats">' + "".join(out) + "</div>"


def b_salon(ctx, sid):
    """Own page for each salon: unique local text, photos, colours, exclusive treatments, map and FAQ."""
    sv = SALONS[sid]
    d = ctx.pick(SALON_PAGE[sid])
    imgs = SALON_IMG[sid]
    other = "sanur" if sid == "ubud" else "ubud"
    ov = SALONS[other]
    excl = []
    for m in MENU:
        cat, iid, nm, du, pr, only, diff = m
        if only == [sid]:
            excl.append((nm, du, pr, iid))
    rows = "".join(
        f'<li><div><b>{E(n)}</b>{("<small>" + E(ctx.pick(DESC[iid])) + "</small>") if iid in DESC else ""}</div>'
        f'<span>{(ctx.dur(du) + " · ") if du else ""}{ctx.price(pr)}</span></li>' for n, du, pr, iid in excl)
    tel = sv["tel"].replace(" ", "")
    wa = f'https://wa.me/{sv["wa"]}'
    q = sv["maps"].split("query=")[-1]
    hours = sv["opens"] + "–" + sv["closes"]
    ribbon = "".join(f'<figure><img src="{ctx.asset(i)}" alt="The Faces Spa {sv["name"]}" loading="lazy"></figure>' for i in SALON_RIBBON[sid])
    feats = "".join(f'<li class="rv"><span class="sl-n">0{i + 1}</span><h3>{E(t)}</h3><p>{E(x)}</p></li>' for i, (t, x) in enumerate(d["f"]))
    faq = "".join(f'<details><summary>{E(qq)}</summary><p>{E(aa)}</p></details>' for qq, aa in d["faq"])
    ld = {"@context": "https://schema.org", "@type": "DaySpa", "@id": ctx.abs_url(sid) + "#spa", "name": f"The Faces Spa {sv['name']}",
          "url": ctx.abs_url(sid), "telephone": sv["tel"], "image": [ctx.asset(i) for i in imgs], "priceRange": "IDR 200,000 – 3,800,000",
          "description": d["seo"][0], "parentOrganization": {"@type": "Organization", "name": "THE FACES"},
          "address": {"@type": "PostalAddress", "streetAddress": sv["street"], "addressLocality": sv["locality"], "addressRegion": "Bali",
                      "postalCode": sv["postal"], "addressCountry": "ID"},
          "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                         "opens": sv["opens"], "closes": sv["closes"]}],
          "hasMap": sv["maps"], "potentialAction": {"@type": "ReserveAction", "target": BOOK[sid]}}
    fq = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": qq, "acceptedAnswer": {"@type": "Answer", "text": aa}} for qq, aa in d["faq"]]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "THE FACES", "item": ctx.abs_url("")},
        {"@type": "ListItem", "position": 2, "name": f"The Faces Spa {sv['name']}", "item": ctx.abs_url(sid)}]}
    return f'''<div class="sl sl-{sid}">
<section class="sl-hero">
 <video class="sl-bg" autoplay muted loop playsinline preload="metadata" poster="{ctx.asset("salon-" + sid + ".jpg")}" aria-hidden="true">
  <source src="{ctx.asset("salon-" + sid + "-m.mp4")}" type="video/mp4" media="(max-width: 760px)"><source src="{ctx.asset("salon-" + sid + ".mp4")}" type="video/mp4"></video>
 <figure class="sl-float" aria-hidden="false"><img src="{ctx.asset(imgs[0])}" alt="{E(ctx.t(sv["alt"]))}" loading="eager" fetchpriority="high"><figcaption>The Faces Spa {sv["name"]}</figcaption></figure>
 <div class="wrap sl-hero-in">
  <nav aria-label="Breadcrumb" class="eyebrow crumbs"><a href="{E(ctx.url())}">THE FACES</a> <span aria-hidden="true">/</span> <span>{E(ctx.t("nav_salons"))}</span> <span aria-hidden="true">/</span> <span>{sv["name"]}</span></nav>
  <p class="eyebrow sl-eb">{E(d["eyebrow"])}</p>
  <h1>{E(d["h1"])}</h1>
  <p class="lead">{E(ctx.pick(SALON_TXT[sid]))}</p>
  <div class="ld-cta">
   <a class="btn" {book("salon-page-" + sid, sv["name"], salon=sid)}>{E(ctx.t("sa_book", salon=sv["name"]))}</a>
   <a class="btn ghost-l" href="{wa}" target="_blank" rel="noopener">WhatsApp</a>
  </div>
  <p class="sl-note">{E(ctx.t("sl_book_note"))}</p>
 </div>
 <dl class="wrap sl-facts">
  <div><dt>{E(ctx.t("sl_address"))}</dt><dd><a href="{sv["maps"]}" target="_blank" rel="noopener">{E(sv["addr"])}</a></dd></div>
  <div><dt>{E(ctx.t("sl_hours"))}</dt><dd>{E(ctx.t("sa_hours", h=hours))}</dd></div>
  <div><dt>{E(ctx.t("sl_phone"))}</dt><dd><a href="tel:{tel}">{sv["tel"]}</a></dd></div>
 </dl>
</section>
<section class="sl-ribbon" aria-label="The Faces Spa {sv["name"]}">
 <div class="sl-track">{ribbon}{ribbon}</div>
</section>
<section class="sec sl-why">
 <div class="wrap">
  <h2 class="h2 rv">{E(d["why_h"])}</h2>
  <ul class="sl-feats">{feats}</ul>
 </div>
</section>
<section class="sec sl-story">
 <div class="wrap sl-story-in">
  <div class="sl-copy rv">
   <h2 class="h2">{E(d["seo_h"])}</h2>
   <p>{E(d["seo"][0])}</p>
   <p>{E(d["seo"][1])}</p>
  </div>
  <div class="sl-pics">
   <div data-parallax="0.06"><figure class="mask rv"><img src="{ctx.asset(imgs[1])}" alt="The Faces Spa {sv["name"]}" loading="lazy"></figure></div>
   <div data-parallax="-0.08"><figure class="mask rv"><img src="{ctx.asset(imgs[2])}" alt="The Faces Spa {sv["name"]}" loading="lazy"></figure></div>
  </div>
 </div>
</section>
<section class="sec sl-only"><img class="sl-only-bg" src="{ctx.asset(imgs[3])}" alt="" aria-hidden="true" loading="lazy">
 <div class="wrap sl-only-in">
  <div>
   <p class="eyebrow">{E(ctx.t("sa_only_here"))}</p>
   <h2 class="h2">The Faces Spa {sv["name"]}</h2>
   <div class="ld-cta"><a class="btn" {book("salon-only-" + sid, sv["name"], salon=sid)}>{E(ctx.t("sa_book", salon=sv["name"]))}</a></div>
   <p style="margin-top:22px"><a class="link" href="{E(ctx.url("menu"))}">{E(ctx.t("sa_full_menu"))}</a></p>
  </div>
  <ul class="sl-list">{rows}</ul>
 </div>
</section>
<section class="sec sl-menu" id="menu-{sid}">
 <div class="wrap">
  <div class="sl-menu-head">
   <div><p class="eyebrow">{E(ctx.t("sl_menu_eb"))}</p><h2 class="h2">{E(ctx.t("sl_menu_h", salon=sv["name"]))}</h2></div>
   <p>{E(ctx.t("sl_menu_p", salon=sv["name"]))}</p>
  </div>
  {salon_menu(ctx, sid)}
  <div class="sl-menu-cta"><a class="btn darksolid" {book("salon-menu-" + sid, sv["name"], salon=sid)}>{E(ctx.t("sa_book", salon=sv["name"]))} ↗</a><p>{E(ctx.t("sl_book_note"))}</p></div>
 </div>
</section>
<section class="sec sl-go">
 <div class="wrap sl-go-in">
  <div class="rv">
   <h2 class="h2">{E(d["go_h"])}</h2>
   <p>{E(d["go"])}</p>
   <address>{E(sv["addr"])}<br><a href="tel:{tel}">{sv["tel"]}</a></address>
   <div class="ld-cta"><a class="btn dark" href="{sv["maps"]}" target="_blank" rel="noopener">{E(ctx.t("sa_dir"))}</a></div>
  </div>
  <div class="sd-map"><iframe title="{E(sv["addr"])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={q}&amp;output=embed"></iframe></div>
 </div>
</section>
{('<section class="sec sl-reviews"><div class="wrap">' + reviews_html(ctx, sid, head=False) + '<p class="swipe-hint">' + E(ctx.t("swipe")) + '</p></div></section>') if sid in REVIEWS else ""}
<section class="sec sl-faq">
 <div class="wrap sl-faq-in">
  <h2 class="h2">{E(d["faq_h"])}</h2>
  <div class="sl-qa">{faq}</div>
 </div>
</section>
<section class="sl-other">
 <a class="wrap sl-other-in" href="{E(ctx.url(other))}">
  <img src="{ctx.asset(SALON_IMG[other][0])}" alt="The Faces Spa {ov["name"]}" loading="lazy">
  <span class="eyebrow">{E(ctx.t("sl_visit_other"))}</span>
  <span class="sl-other-name">The Faces Spa {ov["name"]} →</span>
 </a>
</section>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(fq, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False)}</script>
</div>'''


def reviews_html(ctx, sid="sanur", n=None, head=True):
    """Real Google reviews (see content_reviews.py) with links to all reviews and to write one."""
    rv = REVIEWS[sid]
    dec = "." if ctx.lang in ("en", "th", "ja") else ","
    rating = f'{rv["rating"]:.1f}'.replace(".", dec)
    count = f'{rv["count"]:,}'.replace(",", GROUP[ctx.lang])
    star = lambda k: '<span class="rv-stars" aria-label="' + str(k) + '/5">' + "★" * k + '<i>' + "★" * (5 - k) + "</i></span>"
    note = ctx.t("rv_trans") if ctx.lang != rv["orig"] else ""
    cards = "".join(f'''<figure class="rv-card rv"><figcaption>{star(it["stars"])}<span class="rv-src">Google</span></figcaption>
   <blockquote>«{E(ctx.pick(it["text"]))}»</blockquote><p class="rv-who"><b>{E(it["name"])}</b>{(" · <small>" + E(note) + "</small>") if note else ""}</p></figure>''' for it in rv["items"][:n])
    top = f'''<div class="rv-head">
   <div>{label(ctx, 0, "rv_label") if head else ""}<h2 class="h2 rv d1">{E(ctx.t("rv_h2"))}</h2></div>
   <div class="rv-score"><b>{rating}</b><div>{star(5)}<p>{E(ctx.t("rv_count", n=count))} · {E(rv["place"])}</p></div></div>
  </div>'''
    return f'''{top}
  <div class="rv-grid">{cards}</div>
  <div class="rv-acts">
   <a class="btn dark" href="{rv["url"]}" target="_blank" rel="noopener" data-review="read">{E(ctx.t("rv_all"))} ↗</a>
   <a class="btn darksolid" href="{rv["url"]}" target="_blank" rel="noopener" data-review="write">★ {E(ctx.t("rv_write"))}</a>
   <p>{E(ctx.t("rv_write_note"))}</p>
  </div>'''


def b_reviews(ctx):
    return f'''<section class="reviews sec" id="reviews"><div class="wrap">{reviews_html(ctx)}<p class="swipe-hint">{E(ctx.t("swipe"))}</p></div></section>'''


def b_explore(ctx):
    """Short home: one row of image tiles to the pages that used to be long sections on the home page."""
    tiles = [("menu", "nav_menu", "ex_menu", "g01-face.webp"), ("gift-certificates", "nav_gifts", "ex_gifts", "g09-proc-s.webp"),
             ("founders", "nav_founders", "ex_founders", "founders.webp"), ("partners", "nav_partners", "ex_partners", "waterfall.webp"),
             ("certificates", "nav_certs", "ex_certs", "cert-trademark.webp"), ("journal", "nav_journal", "ex_journal", "g12-proc-s.webp")]
    cards = "".join(f'''<a class="ex-tile rv" href="{E(ctx.url(slug))}"><span class="ex-ph"><img src="{ctx.asset(img)}" alt="" loading="lazy"></span>
   <span class="ex-tx"><b>{E(ctx.t(t))}</b><small>{E(ctx.t(d))}</small></span><span class="ex-ar" aria-hidden="true">→</span></a>''' for slug, t, d, img in tiles)
    style = ('<style>@media (max-width:760px){[data-block="07-menu-builder"], [data-block="08-gallery"], [data-block="17-instagram"], [data-block="10-founders"], [data-block="18-certificates"], [data-block="11-gifts"], [data-block="12-partners"], [data-block="16-waterfall"], [data-block="13-journal"]{display:none!important}.eyebrow .n{display:none}}'
             '@media (min-width:761px){[data-block="22-explore"]{display:none!important}}</style>')
    return style + f'''<section class="explore sec" id="explore">
 <div class="wrap sec-head"><div>{label(ctx, 0, "ex_label")}<h2 class="h2 rv d1">{E(ctx.t("ex_h2"))}</h2></div></div>
 <div class="wrap"><div class="ex-grid">{cards}</div><p class="swipe-hint">{E(ctx.t("swipe"))}</p></div>
</section>'''


def b_salons(ctx):
    cards = []
    for k, (sid, s) in enumerate(SALONS.items()):
        wa = f'https://wa.me/{s["wa"]}?text=' + html.escape(f'Hello! I would like to book at THE FACES {s["name"]}').replace(" ", "%20")
        cards.append(f'''<article class="salon rv{" d2" if k else ""}" id="salon-{sid}">
   <div class="ph"><img src="{ctx.asset(s["img"])}" alt="{E(ctx.t(s["alt"]))}" loading="lazy"></div>
   <h3><a href="{E(ctx.url(sid))}">{s["name"]}</a></h3>
   <address>{E(s["addr"])}</address>
   <p class="hours">{E(ctx.t("sa_hours", h=s["opens"] + "–" + s["closes"]))}</p>
   <div class="acts">
    <a class="btn darksolid" {book("salon-" + sid, salon=sid)}>{E(ctx.t("sa_book", salon=s["name"]))}</a>
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
 <div class="wrap"><div class="gifts">{"".join(cards)}</div><p class="swipe-hint">{E(ctx.t("swipe"))}</p></div>
</section>'''


def b_partners(ctx):
    names = ["The White Temple · Sanur", "THE FACES Ubud", "WATERFALL · Bali", "THE FACES SANUR"]
    proj = "".join(f'<div class="rv d{k}"><span class="st">{E(ctx.t(f"pa_s{k + 1}"))}</span><h3>{names[k]}</h3><p>{E(ctx.t(f"pa_d{k + 1}"))}</p></div>' for k in range(4))
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
   </div>
   <p class="note">{E(ctx.t("wf_note"))}</p>
  </div>
 </div>
</section>'''


def b_journal(ctx):
    posts = "".join(article_card(ctx, a, k) for k, a in enumerate(ARTICLES[:3]))
    return f'''<section class="sec" id="journal">
 <div class="wrap sec-head">
  <div>{label(ctx, 10, "jo_label")}<h2 class="h2 rv d1">{E(ctx.t("jo_h2"))}</h2></div>
  <div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><p class="muted rv d2" style="max-width:420px">{E(ctx.t("jo_intro"))}</p><a class="link rv d2" href="{E(ctx.url("journal"))}">{E(ctx.t("jo_all"))} ({len(ARTICLES)})</a></div>
 </div>
 <div class="wrap posts"><!--tf-posts-->{posts}<!--/tf-posts--></div><p class="swipe-hint wrap">{E(ctx.t("swipe"))}</p>
</section>'''


def related_html(ctx, art):
    same = [a for a in ARTICLES if a["id"] != art["id"] and a["cat"] == art["cat"]]
    rest = [a for a in ARTICLES if a["id"] != art["id"] and a not in same]
    pick = (same + rest)[:3]
    return "".join(article_card(ctx, a, k) for k, a in enumerate(pick))


def b_post(ctx, title, cat, excerpt, img_url, body, date="", related="", svc_url="", svc_label=""):
    """Article page layout (used by the preview and, with placeholders, by WordPress)."""
    return f'''<article class="post-page">
 <header class="post-hero">
  <div class="wrap">
   <a class="eyebrow back" href="{E(ctx.url("journal"))}">{E(ctx.t("jo_back"))}</a>
   <p class="eyebrow cat">{cat}{(" · " + date) if date else ""}</p>
   <h1 class="h2">{title}</h1>
   <p class="lead">{excerpt}</p>
  </div>
  <figure class="post-img mask in"><img src="{img_url}" alt=""></figure>
 </header>
 <div class="wrap post-body">{body}</div>
 <aside class="wrap post-cta"><div><p class="h3">{E(ctx.t("jo_cta_h"))}</p><p class="muted">{E(ctx.t("jo_cta_p"))}</p></div>
  <div class="row"><a class="btn darksolid" {book("article")}>{E(ctx.t("book_cta"))}</a><a class="btn dark" href="{svc_url or E(ctx.url("menu"))}">{svc_label or E(ctx.t("nav_menu"))}</a></div></aside>
 <section class="wrap post-related"><p class="eyebrow">{E(ctx.t("jo_related"))}</p><div class="posts"><!--tf-related-->{related}<!--/tf-related--></div>
  <p><a class="link" href="{E(ctx.url("journal"))}">{E(ctx.t("jo_all"))}</a></p></section>
</article>'''


def b_faq(ctx):
    qa = [(ctx.pick(q), ctx.pick(a)) for q, a in FAQ]
    det = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in qa)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": ctx.lang,
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}
    ld_html = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ctx.slug == "" else ""
    return f'''<section class="faq sec" id="faq">
 <div class="wrap faq-grid">
  <div>{label(ctx, 11, "fq_label")}<h2 class="h2 rv d1" style="margin-top:22px">{E(ctx.t("fq_h2"))}</h2></div>
  <div class="rv d2">{det}</div>
 </div>
 {ld_html}
</section>'''


def jsonld_business(ctx):
    org = {"@type": "Organization", "@id": ctx.site + "/#org", "name": "THE FACES", "url": ctx.site + "/",
           "logo": ctx.asset("logo-black.png"), "email": LINKS["email"],
           "sameAs": [LINKS["instagram"], LINKS["instagram_spa"], LINKS["tiktok"], LINKS["linkedin"], LINKS["network"]],
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
                     "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                                    "opens": s["opens"], "closes": s["closes"]}],
                     "potentialAction": {"@type": "ReserveAction", "target": s["online"]}})
    return json.dumps({"@context": "https://schema.org", "@graph": [org] + spas}, ensure_ascii=False)


def b_footer(ctx):
    legal = [("lg_cancel", "terms", "cancellation"), ("lg_resched", "terms", "rescheduling"), ("lg_privacy", "privacy", ""),
             ("lg_cookies", "privacy", "cookies"), ("lg_terms", "terms", "terms"), ("lg_gift", "terms", "gift")]
    _old_legal = [
             ("lg_cookies", "cookie_policy"), ("lg_terms", "terms_of_use"), ("lg_gift", "the_faces_gift_certificate_terms")]
    legal_h = "".join(f'<a href="{E(ctx.url(pg, anc))}">{E(ctx.t(k))}</a>' for k, pg, anc in legal)
    smap = []
    for P in PAGES:
        key = P["slug"]
        name = h1_of(ctx.pick(P["title"])) if key else "THE FACES"
        if key in LANDING:
            name = ctx.pick(LANDING[key]["nav"])
        smap.append(f'<li><a href="{E(ctx.url(key))}">{E(name)}</a></li>')
    sitemap_h = "".join(smap)
    flangs = "".join(f'<a href="{E(ctx.lang_url(l))}" hreflang="{l}" lang="{l}"{CUR if l == ctx.lang else ""}>{E(LANG_NAMES[l])}</a>' for l in SWITCH)
    soc = (f'<a href="{LINKS["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram">{SOCIAL_SVG["instagram"]}</a>'
           f'<a href="{LINKS["instagram_spa"]}" target="_blank" rel="noopener" aria-label="Instagram @thefacesspaubud">{SOCIAL_SVG["instagram"]}</a>'
           f'<a href="{LINKS["tiktok"]}" target="_blank" rel="noopener" aria-label="TikTok">{SOCIAL_SVG["tiktok"]}</a>'
           f'<a href="{LINKS["linkedin"]}" target="_blank" rel="noopener" aria-label="LinkedIn">{SOCIAL_SVG["linkedin"]}</a>'
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
    <p class="news-note"><a href="{E(ctx.url("privacy"))}">{E(ctx.t("news_consent"))}</a></p>
    <div class="f-langs">{flangs}</div>
   </div>
   <div><h2>{E(ctx.t("ft_spa"))}</h2><ul>
    {"".join(f'<li><a href="{E(ctx.url(L["slug"]))}">{E(ctx.pick(L["nav"]))}</a></li>' for L in LANDINGS)}
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
    <li><a {book("footer", salon=page_salon(ctx))}>{E(ctx.t("ft_online"))}</a></li>
    <li><a href="mailto:{LINKS["email"]}">{LINKS["email"]}</a></li></ul></div>
   <div><h2>{E(ctx.t("ft_world"))}</h2><ul>
    <li><a href="{LINKS["network"]}" target="_blank" rel="noopener">{E(ctx.t("ft_network"))}</a></li>
    <li><a href="{E(ctx.url("partners"))}">{E(ctx.t("nav_partners"))}</a></li>
    <li><a href="{E(ctx.url("partners"))}">{E(ctx.t("ft_careers"))}</a></li></ul></div>
  </div>
  <details class="f-map"><summary>{E(ctx.t("nav_sitemap"))} · {len(PAGES)}</summary><ul>{sitemap_h}</ul>{('<p class="xml"><a href="{{TF_HOME}}/wp-sitemap.xml">sitemap.xml</a></p>' if ctx.mode == "wp" else "")}</details>
  <div class="f-bot"><span>© 2026 THE FACES · Five Elements. Guided by Love.</span><nav aria-label="Legal">{legal_h}</nav></div>
 </div>
 <script type="application/ld+json">{jsonld_business(ctx)}</script>
</footer>
<a class="side-book" {book("side-tab", salon=page_salon(ctx))} aria-label="{E(ctx.t("book_online"))}">
 <span class="sb-ico" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 2v2H5a2 2 0 00-2 2v13a2 2 0 002 2h14a2 2 0 002-2V6a2 2 0 00-2-2h-2V2h-2v2H9V2H7zm-2 7h14v10H5V9zm2 2v2h2v-2H7zm4 0v2h2v-2h-2zm4 0v2h2v-2h-2zm-8 4v2h2v-2H7zm4 0v2h2v-2h-2z"/></svg></span>
 <span class="sb-txt">{E(ctx.t("ld_book_side"))}</span>
 <span class="sb-tip" aria-hidden="true">{E(ctx.t("book_online"))} <b>↗</b></span>
</a>
<div class="mbar"><a href="{E(ctx.url("menu"))}">{E(ctx.t("mb_menu"))}</a><a class="bk" {book("mobile-bar", salon=page_salon(ctx))}>{E(ctx.t("sa_book", salon=SALONS[page_salon(ctx)]["name"]) if page_salon(ctx) else ctx.t("book"))}</a></div>
<div class="toast" role="status"><span class="msg"></span></div>
<div class="cookie" role="dialog" aria-label="Cookies"><p>{E(ctx.t("ck_text"))} <a href="{E(ctx.url("privacy", "cookies"))}">{E(ctx.t("ck_more"))}</a></p>
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


ARTICLES[:] = _build_articles()
ARTICLE.update({a["id"]: a for a in ARTICLES})

BLOCKS = {"01-header": b_header, "02-hero": b_hero, "03-philosophy": b_philosophy, "04-senses": b_senses,
          "05-elements": b_elements, "06-signatures": b_signatures, "07-menu-builder": b_menu, "08-gallery": b_gallery,
          "09-salons": b_salons, "10-founders": b_founders, "11-gifts": b_gifts, "12-partners": b_partners,
          "13-journal": b_journal, "17-instagram": b_instagram, "18-certificates": b_certificates,
          "19-privacy": b_privacy, "20-terms": b_terms, "21-journal-all": b_journal_all, "16-waterfall": b_waterfall, "22-explore": b_explore, "23-reviews": b_reviews, "14-faq": b_faq, "15-footer": b_footer}


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

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Montserrat:wght@200;300;400;500;600&family=Noto+Sans+JP:wght@200;300;400;500&family=Noto+Sans+Thai:wght@200;300;400;500&display=swap" rel="stylesheet">'

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

def build_wordpress(css, js, autolang):
    """WordPress plugin: thefaces/wordpress-plugin/thefaces-spa (blocks + data + assets + PHP)."""
    import shutil
    plug = ROOT / "wordpress-plugin" / "thefaces-spa"
    for sub in ("blocks", "data", "assets"):
        shutil.rmtree(plug / sub, ignore_errors=True)
    (plug / "assets" / "media").mkdir(parents=True, exist_ok=True)
    (plug / "data").mkdir(parents=True, exist_ok=True)
    (plug / "assets" / "thefaces.css").write_text("/* THE FACES Spa · generated by thefaces/src/build.py */\n" + css, encoding="utf-8")
    (plug / "assets" / "thefaces.js").write_text(js, encoding="utf-8")
    (plug / "assets" / "thefaces-autolang.js").write_text(autolang, encoding="utf-8")
    for f in (ROOT / "assets").iterdir():
        if f.is_file():
            shutil.copy2(f, plug / "assets" / "media" / f.name)
    site = "{{TF_HOME}}"
    for lang in LANGS:
        ld = plug / "blocks" / lang
        (ld / "pages").mkdir(parents=True, exist_ok=True)
        home_ctx = Ctx(lang, "wp", "", site, "", {})
        for name, fn in BLOCKS.items():
            (ld / f"{name}.html").write_text(wrap(home_ctx, name, fn(home_ctx)), encoding="utf-8")
        for page in PAGES:
            ctx = Ctx(lang, "wp", page["slug"], site, "", {})
            key = page["slug"] or "home"
            (ld / "pages" / f"{key}-01-header.html").write_text(wrap(ctx, "01-header", b_header(ctx)), encoding="utf-8")
            (ld / "pages" / f"{key}-15-footer.html").write_text(wrap(ctx, "15-footer", b_footer(ctx)), encoding="utf-8")
            for bn in page["blocks"]:
                if bn.startswith("salon-"):
                    (ld / "pages" / f"{key}-salon.html").write_text(wrap(ctx, bn, b_salon(ctx, bn[6:])), encoding="utf-8")
            if "landing" in page["blocks"]:
                (ld / "pages" / f"{key}-landing.html").write_text(wrap(ctx, "landing", b_landing(ctx, page)), encoding="utf-8")
            elif page["slug"]:
                (ld / "pages" / f"{key}-intro.html").write_text(wrap(ctx, "intro", b_pageintro(ctx, page)), encoding="utf-8")
    posts = []
    for art in ARTICLES:
        rec = {"id": art["id"], "img": art["img"], "catkey": art["cat"], "canonical": CANON.get(art["id"], ""), "service": article_service(art), "service_label": {}, "catname": {}, "slug": {}, "title": {}, "cat": {}, "excerpt": {}, "html": {}}
        for lang in LANGS:
            c = Ctx(lang, "wp", "journal", site, "", {})
            rec["slug"][lang] = c.post_slug(art["id"])
            rec["title"][lang] = art["title"](c)
            rec["catname"][lang] = cat_name(c, art["cat"])
            rec["cat"][lang] = cat_name(c, art["cat"]) + " · " + c.t("jo_read_min", n=read_min(c, art["body"](c)))
            rec["excerpt"][lang] = art["excerpt"](c)
            rec["service_label"][lang] = service_label(c, article_service(art))
            rec["html"][lang] = art["body"](c)
        posts.append(rec)
    (plug / "data" / "posts.json").write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding="utf-8")
    for lang in LANGS:
        c = Ctx(lang, "wp", "journal", site, "", {})
        shell = b_post(c, "{{POST_TITLE}}", "{{POST_CAT}}", "{{POST_EXCERPT}}", "{{POST_IMG}}", "{{POST_CONTENT}}", "{{POST_DATE}}", "", "{{POST_SVC_URL}}", "{{POST_SVC_LABEL}}")
        (plug / "blocks" / lang / "post-shell.html").write_text(wrap(c, "post", shell), encoding="utf-8")
    pages = {(p["slug"] or "home"): p["blocks"] for p in PAGES}
    seo = {l: {(p["slug"] or "home"): {"title": p["title"][LI[l]], "desc": p["desc"][LI[l]]} for p in PAGES} for l in LANGS}
    aliases = {n.split("-", 1)[1]: n for n in BLOCKS}
    aliases.update({n: n for n in BLOCKS})
    (plug / "data" / "readmin.json").write_text(json.dumps({l: UI["jo_read_min"][LI[l]] for l in LANGS}, ensure_ascii=False), encoding="utf-8")
    (plug / "data" / "jocats.json").write_text(json.dumps({l: {k: cat_name(Ctx(l, "wp", "", site, "", {}), k) for k in CAT_ORDER} for l in LANGS}, ensure_ascii=False), encoding="utf-8")
    for name, obj in (("pages", pages), ("seo", seo), ("blocks", aliases), ("langs", {l: LANG_NAMES[l] for l in LANGS})):
        (plug / "data" / f"{name}.json").write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"WordPress plugin: {plug} ({sum(1 for _ in plug.rglob('*') if _.is_file())} files)")


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
    autolang = (SRC / "autolang.js").read_text(encoding="utf-8")
    tdir, pdir = ROOT / "tilda", ROOT / "preview"
    build_wordpress(css, js, autolang)

    (tdir).mkdir(exist_ok=True)
    (tdir / "00-site-head.html").write_text(
        "<!-- THE FACES · Tilda: Site settings > More > HTML code for the HEAD section. Paste once for the whole site. -->\n"
        + CONSENT_GTM + "\n<script>" + autolang + "</script>\n" + FONTS + "\n<style>" + css + "</style>\n<script>" + js + "</script>\n", encoding="utf-8")

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
            for bn in page["blocks"]:
                if bn.startswith("salon-"):
                    (ld / "pages" / f"{key}-salon.html").write_text(f"<!-- THE FACES · {key} salon page · {LANG_NAMES[lang]} · paste right after 01-header -->\n" + wrap(ctx, bn, b_salon(ctx, bn[6:])) + "\n", encoding="utf-8")
            if "landing" in page["blocks"]:
                (ld / "pages" / f"{key}-landing.html").write_text(
                    f"<!-- THE FACES · {key} landing page · H1, CTA, treatments and prices · {LANG_NAMES[lang]} · paste right after 01-header -->\n" + wrap(ctx, "landing", b_landing(ctx, page)) + "\n", encoding="utf-8")
            if page["slug"] and not (set(page["blocks"]) & NO_INTRO):
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
                if name == "landing":
                    body.append(wrap(pctx, "landing", b_landing(pctx, page)))
                    continue
                if name.startswith("salon-"):
                    body.append(wrap(pctx, name, b_salon(pctx, name[6:])))
                    continue
                body.append(wrap(pctx, name, BLOCKS[name](pctx)))
                if name == "01-header" and page["slug"] and not (set(page["blocks"]) & NO_INTRO):
                    body.append(wrap(pctx, "intro", b_pageintro(pctx, page)))
            out = pdir / lang / page["slug"] / "index.html" if page["slug"] else pdir / lang / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{pctx.url(page["slug"], lang=l)}">' for l in LANGS)
            out.write_text(f'''<!doctype html>
<html lang="{HTML_LANG[lang]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="canonical" href="{pctx.abs_url(page["slug"])}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:locale" content="{OG_LOCALE[lang]}">
{alts}
<script>{autolang}</script>
{FONTS}
<style>body{{margin:0;background:#fff}}{css}</style>
<script>window.tfConsent=function(ok){{try{{localStorage.setItem('tf_consent',ok?'granted':'denied')}}catch(e){{}}}};</script>
</head><body>
{chr(10).join(body)}
<script>{js}</script>
</body></html>''', encoding="utf-8")

    # preview: journal article pages
    for lang in LANGS:
        for art in ARTICLES:
            pid = art["id"]
            ctx = Ctx(lang, "preview", "journal/" + Ctx(lang, "preview", "", a.site, "", {}).post_slug(pid), a.site, assets_base, assets_map)
            ctx.lang_urls = {l: ctx.post_url(pid, l) for l in LANGS}
            title, ex, bd = art["title"](ctx), art["excerpt"](ctx), art["body"](ctx)
            cat = cat_name(ctx, art["cat"]) + " · " + ctx.t("jo_read_min", n=read_min(ctx, bd))
            body = [wrap(ctx, "01-header", b_header(ctx)),
                    wrap(ctx, "post", b_post(ctx, E(title), E(cat), E(ex), ctx.asset(art["img"]), bd, "", related_html(ctx, art),
                                             E(ctx.url(article_service(art))), E(service_label(ctx, article_service(art))))),
                    wrap(ctx, "15-footer", b_footer(ctx))]
            out = pdir / lang / ctx.slug / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{ctx.post_url(pid, l)}">' for l in LANGS)
            out.write_text(f'''<!doctype html>
<html lang="{HTML_LANG[lang]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} | The Faces</title><meta name="description" content="{E(ex)}">
<link rel="canonical" href="{(ctx.abs_url(CANON[pid]) if pid in CANON else ctx.site.rstrip('/') + '/' + ctx.post_slug(pid) + '/')}">
{alts}
<script>{autolang}</script>
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
        blocks = [f"pages/{p['slug']}-landing" if b == "landing" else (f"pages/{p['slug']}-salon" if b.startswith("salon-") else b) for b in p["blocks"]]
        if p["slug"] and not (set(p["blocks"]) & NO_INTRO):
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
