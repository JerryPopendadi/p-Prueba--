#!/usr/bin/env python3
"""Aplica las mejoras de SEO (Seobility) y velocidad (PageSpeed) sobre el código de la portada.

Uso: python3 tools/optimizar_portada.py ENTRADA.html SALIDA.html
ENTRADA es el bloque HTML de la portada tal como está publicado (widget HTML de Elementor).
"""
import re, sys, json

src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
log = []
def rep(a, b, n=1, need=True):
    global t
    c = t.count(a)
    if need: assert c >= 1, 'NO ENCONTRADO: ' + a[:90]
    t = t.replace(a, b, n if n else c)
    log.append(f'{c}× {a[:60]!r}')
def sub(p, b, flags=re.S, need=True):
    global t
    t, n = re.subn(p, b, t, flags=flags)
    if need: assert n, 'SIN COINCIDENCIAS: ' + p[:90]
    log.append(f'{n}× /{p[:60]}/')

# ---------------------------------------------------------------- 0. Atributos repetidos que añade WordPress
def dedupe(m):
    tag = m.group(0); seen = set(); out = []
    for a in re.finditer(r'\s+([\w-]+)(?:="[^"]*")?', tag[4:-1]):
        k = a.group(1)
        if k in seen: continue
        seen.add(k); out.append(a.group(0))
    return '<img' + ''.join(out) + '>'
t = re.sub(r'<img\s[^>]*>', dedupe, t)

# ---------------------------------------------------------------- 1. Texto ALT en todas las imágenes
def alt_mega(m):
    tag, name = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
    tag = tag.replace('alt=""', f'alt="{name} · SeñalVal"')
    tag = re.sub(r'\ssrc="', ' data-src="', tag, count=1)          # se cargan al abrir el menú
    tag = re.sub(r'\s(loading|decoding)="[^"]*"', '', tag)
    return tag + '<span><span class="mega__name">' + m.group(2) + '</span>'
sub(r'(<img[^>]*alt=""[^>]*>)<span><b>(.*?)</b>', alt_mega)
def alt_sector(m):
    return m.group(1).replace('alt=""', f'alt="Señalización para {m.group(3).lower()} · proyecto de SeñalVal"') + m.group(2)
sub(r'(<img class="sector__bg"[^>]*>)(<span class="sector__i">[^<]*</span>)<h3>([^<]+)</h3>', lambda m: alt_sector(m) + f'<h3>{m.group(3)}</h3>')
rep('<img class="pmodal__img" alt="">', '<img class="pmodal__img" alt="Foto del proyecto">')
rep("""<div class="media">${p.img ? '<img loading="lazy" alt="">' : ''}</div>""", """<div class="media">${p.img ? '<img loading="lazy" alt="Imagen del artículo">' : ''}</div>""")
rep("""b.innerHTML = '<img loading="lazy" alt="">'; $('img', b).src = u;""", """b.innerHTML = '<img loading="lazy" alt="Miniatura">'; $('img', b).src = u; $('img', b).alt = `${cfg.title} · miniatura ${k + 1}`;""")

# ---------------------------------------------------------------- 2. Encabezados: sin vacíos y en proporción al texto
# Ventana de proyecto: el título se rellena al abrirla -> no es un encabezado vacío en el código
rep('<h3 class="h3" id="pmodal-title"></h3>', '<p class="h3 pmodal__title" id="pmodal-title" role="heading" aria-level="2"></p>')
# Plantillas JS: el encabezado se crea al vuelo, nunca vacío en el código
rep("""            <span class="post__meta"></span>
            <h3></h3>
            <p></p>""", """            <span class="post__meta"></span>
            <span class="post__slot"></span>
            <p></p>""")
rep("""        $('h3', a).textContent = p.title;""", """        const h = document.createElement('h3'); const ha = document.createElement('a');
        ha.href = p.link; ha.textContent = p.title; h.appendChild(ha); $('.post__slot', a).replaceWith(h);""")
rep('<h3 class="story__title"></h3>', '<p class="story__title"></p>')
rep('<div class="story__img"><img alt=""></div>', '<div class="story__img"><img alt="Imagen del artículo"></div>')
# Pasos del ciclo, pilares, recursos y títulos del pie: estilo de título sin ser encabezado
sub(r'(<li><span>\d</span>)<h3>([^<]+)</h3>', r'\1<p class="cycle__t">\2</p>')
sub(r'(<span class="pillar__num">\d+</span>\s*<svg class="pillar__icon".*?</svg>\s*)<h3>([^<]+)</h3>', r'\1<p class="pillar__t">\2</p>')
sub(r'(<span class="res__type">[^<]+</span>\s*)<h3>([^<]+)</h3>', r'\1<p class="res__t">\2</p>')
sub(r'(<nav aria-label="[^"]+">\s*)<h3>([^<]+)</h3>', r'\1<p class="footer__t">\2</p>')

# ---------------------------------------------------------------- 3. Negritas repetidas
rep('<li><b>Inventario final</b> de todos los elementos instalados.</li>', '<li><b>Inventario codificado</b> de todos los elementos instalados.</li>')

# ---------------------------------------------------------------- 4. Enlaces: textos ancla cortos y no repetidos
# Tarjetas del blog: el enlace es solo el título (antes era la tarjeta entera = ancla demasiado larga)
def post_static(m):
    href, inner = m.group(1), m.group(2)
    inner = re.sub(r'<h3>(.*?)</h3>', lambda h: f'<h3><a href="{href}">{h.group(1)}</a></h3>', inner, count=1)
    inner = inner.replace('<span class="post__more">Leer artículo →</span>', '<span class="post__more" aria-hidden="true">Leer artículo →</span>')
    return f'<article class="post post--static">{inner}</article>'
sub(r'<a class="post post--static" href="([^"]+)">(.*?)</a>(?=\s*(?:<a class="post post--static"|</div>))', post_static)
rep("""        const a = document.createElement('a');
        a.className = 'post';
        a.href = p.link;""", """        const a = document.createElement('article');
        a.className = 'post';""")
rep('<span class="post__more">Leer artículo →</span>', '<span class="post__more" aria-hidden="true">Leer artículo →</span>')
rep('>Top 10 tipos de señalética para empresas</a>', '>Top 10 de señalética</a>', need=False)
rep('>Señalética profesional en España</a>', '>Señalética en toda España</a>', need=False)
rep('>Letras corpóreas para sedes judiciales</a>', '>Letras para sedes judiciales</a>', need=False)
# Pie: textos distintos a los del menú y la portada
rep('<a href="#video">Vídeo de presentación</a>', '<a href="#video">Ver el vídeo (1 min)</a>', need=False)
rep('>Quiénes somos</a>\n        <a href="#video">', '>Sobre SeñalVal</a>\n        <a href="#video">', need=False)
sub(r'(<div class="wrap footer__cta">.*?class="btn btn--accent">)Solicitar estudio del proyecto', r'\1Pedir presupuesto sin compromiso', need=False)
sub(r'(<br>\s*<a href="https://senalval\.es/">)senalval\.es(</a>\s*</address>)', r'\1Web de SeñalVal\2', need=False)
# Menú del móvil: se genera a partir del menú principal (evita repetir todos los enlaces en el código)
sub(r'(<div class="mobile-menu" id="mobile-menu" hidden(?:="")?>).*?(<a href="#contacto" class="btn btn--accent">)', r'\1\n      <div class="mobile-menu__groups"></div>\n      \2')

# ---------------------------------------------------------------- 5. Redes sociales y compartir
SH = 'https://senalval.es/'
from urllib.parse import quote
msg = quote('SeñalVal · Proyectos de señalización de alta exigencia')
share = f'''
    <div class="wrap footer__social">
      <p class="footer__t">Síguenos y comparte</p>
      <div class="social">
        <a href="https://www.instagram.com/senalval/" target="_blank" rel="noopener" aria-label="SeñalVal en Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="17.5" cy="6.5" r="1.1" fill="currentColor"/></svg>Instagram</a>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url={quote(SH)}" target="_blank" rel="noopener nofollow" aria-label="Compartir en LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.75h4v11H3v-11Zm6.5 0h3.8v1.5h.06c.53-1 1.82-2.06 3.75-2.06 4 0 4.74 2.64 4.74 6.07v5.99h-4v-5.31c0-1.27-.02-2.9-1.77-2.9-1.77 0-2.04 1.38-2.04 2.81v5.4h-4v-11Z"/></svg>LinkedIn</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u={quote(SH)}" target="_blank" rel="noopener nofollow" aria-label="Compartir en Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.87.25-1.46 1.5-1.46H16.6V4.46A21 21 0 0 0 14.3 4.3c-2.3 0-3.8 1.4-3.8 3.95v2.25H8v3h2.5V21h3Z"/></svg>Facebook</a>
        <a href="https://twitter.com/intent/tweet?url={quote(SH)}&amp;text={msg}" target="_blank" rel="noopener nofollow" aria-label="Compartir en X"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M17.8 3h3.1l-6.8 7.8L22 21h-6.2l-4.9-6.4L5.3 21H2.2l7.3-8.3L2 3h6.3l4.4 5.8L17.8 3Zm-1.1 16.2h1.7L7.4 4.7H5.6l11.1 14.5Z"/></svg>X</a>
        <a href="https://wa.me/?text={msg}%20{quote(SH)}" target="_blank" rel="noopener nofollow" aria-label="Compartir por WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2Zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 4.54 0 8.24 3.7 8.24 8.24 0 4.55-3.7 8.24-8.24 8.24Z"/></svg>WhatsApp</a>
        <a href="mailto:?subject={msg}&amp;body={quote(SH)}" aria-label="Compartir por email"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>Email</a>
      </div>
    </div>
'''
sub(r'(\n\s*<div class="wrap footer__bottom">)', share + r'\1')
# Perfil de Instagram en los datos estructurados de la empresa
if '"sameAs"' not in t:
    sub(r'("@id": "https://senalval.es/#empresa",)', r'\1\n        "sameAs": ["https://www.instagram.com/senalval/"],', need=False)

# ---------------------------------------------------------------- 6. Velocidad
# Fotos de Wikimedia a 640 px (antes 1280 px)
sub(r'(upload\.wikimedia\.org/wikipedia/commons/thumb/[^"\s]+?/)1280px-', r'\g<1>640px-', need=False)
# Fotos 2-5 de la portada: no se descargan hasta justo antes de mostrarlas
def hero_lazy(m):
    tag = m.group(0)
    if 'is-active' in tag: return tag
    tag = re.sub(r'\ssrc="', ' data-src="', tag, count=1)
    tag = re.sub(r'\ssrcset="', ' data-srcset="', tag, count=1)
    return re.sub(r'\s(loading|decoding|fetchpriority)="[^"]*"', '', tag)
sub(r'<img[^>]*class="hero__slide[^"]*"[^>]*>', hero_lazy)

CSS = '''
/* --- Optimización SEO / velocidad --- */
.cycle__t { font-size: 1.05rem; font-weight: 500; color: var(--navy); margin-bottom: 6px; line-height: 1.3; }
.pillar__t { font-size: 1.35rem; font-weight: 500; color: var(--navy); margin-bottom: 12px; line-height: 1.25; }
.res__t { font-size: 1.1rem; font-weight: 500; color: var(--navy); line-height: 1.3; }
.res--dossier .res__t { color: var(--white); flex: 1; }
.footer__t { color: var(--white); font-size: .82rem; text-transform: uppercase; letter-spacing: .14em; margin-bottom: 16px; font-weight: 500; }
.mega__name { display: block; font-weight: 500; font-size: .86rem; line-height: 1.3; }
.mega__item:hover .mega__name { color: var(--blue); }
.pmodal__title { margin: 0 0 8px; padding-right: 40px; }
.post { position: relative; }
.post h3 a { color: inherit; text-decoration: none; }
.post h3 a::after { content: ""; position: absolute; inset: 0; z-index: 1; }
.post:hover h3 a { color: var(--blue); }
.post:focus-within { outline: 3px solid var(--blue-bright); outline-offset: 3px; }
.footer__social { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 14px 24px; padding: 26px 0; border-bottom: 1px solid rgba(255,255,255,.08); }
.footer__social .footer__t { margin: 0; }
.social { display: flex; flex-wrap: wrap; gap: 10px; }
.social a { display: inline-flex; align-items: center; gap: 8px; padding: 9px 14px; border-radius: 999px; border: 1px solid rgba(255,255,255,.18); color: rgba(255,255,255,.85); font-size: .85rem; }
.social a:hover { border-color: var(--blue-bright); color: #fff; }
.social svg { width: 17px; height: 17px; }
.mobile-menu__groups { display: grid; gap: 0; }
'''
rep('</style>', CSS + '</style>')

JS_BEFORE_YEAR = r'''
  /* ---- Velocidad: imágenes del menú solo al abrirlo; fotos de portada una a una ---- */
  const loadMega = item => $$('img[data-src]', item).forEach(im => { im.src = im.dataset.src; im.removeAttribute('data-src'); });
  $$('.nav__item').forEach(it => ['pointerenter', 'focusin', 'touchstart'].forEach(ev => it.addEventListener(ev, () => loadMega(it), { once: true, passive: true })));

  /* ---- Menú del móvil generado desde el menú principal ---- */
  const groups = $('.mobile-menu__groups');
  if (groups) {
    $$('.nav__links > .nav__item, .nav__links > a').forEach(el => {
      if (el.tagName === 'A') { const a = document.createElement('a'); a.href = el.getAttribute('href'); a.textContent = el.textContent.trim(); groups.appendChild(a); return; }
      const top = $('.nav__top', el); const d = document.createElement('details'); const s = document.createElement('summary');
      s.textContent = top.textContent.trim(); d.appendChild(s);
      $$('.mega a', el).forEach(src => { const a = document.createElement('a'); a.href = src.getAttribute('href'); if (src.dataset.project) a.dataset.project = src.dataset.project; a.textContent = ($('.mega__name', src) || src).textContent.trim(); d.appendChild(a); });
      groups.appendChild(d);
    });
    $$('a', groups).forEach(a => a.addEventListener('click', () => { const b = $('.nav__burger'); if (b && b.getAttribute('aria-expanded') === 'true') b.click(); }));
  }
'''
rep("  const y = $('#year');", JS_BEFORE_YEAR + "\n  const y = $('#year');")

# Portada: cargar la foto siguiente justo antes de mostrarla
rep("""      slides.forEach((s, k) => s.classList.toggle('is-active', k === cur));""",
    """      const prime = im => { if (im && im.dataset.src) { if (im.dataset.srcset) im.srcset = im.dataset.srcset; im.src = im.dataset.src; im.removeAttribute('data-src'); } };
      prime(slides[cur]); prime(slides[(cur + 1) % slides.length]);
      slides.forEach((s, k) => s.classList.toggle('is-active', k === cur));""")
# Las fotos aún sin cargar no deben contarse como rotas
rep("""      if (img.complete && img.naturalWidth === 0) fail();
      img.addEventListener('error', fail);
    });""", """      if (img.getAttribute('src') && img.complete && img.naturalWidth === 0) fail();
      img.addEventListener('error', fail);
    });""")

# Blog y logos: después de que la página haya cargado (no compiten con la portada)
rep("  const EMAIL = 'luismi.olea@senalval.es';", """  const EMAIL = 'luismi.olea@senalval.es';
  const afterLoad = new Promise(r => { const go = () => setTimeout(r, 400); if (document.readyState === 'complete') go(); else window.addEventListener('load', go, { once: true }); });""")
rep("  const blog = (() => {", "  const blog = afterLoad.then(() => {")
rep("  })();\n\n  if (posts) {", "  });\n\n  if (posts) {")
rep("    Promise.all($$('.logo', track).map(load)).then(() => {", "    afterLoad.then(() => Promise.all($$('.logo', track).map(load))).then(() => {")
open(dst, 'w', encoding='utf-8').write(t)
print('\n'.join(log))
