# -*- coding: utf-8 -*-
"""
Genera ../lera-web/ — versión SEGURA para Netlify:
  • 0 scripts de terceros (sin payhip.js, sin CDN): los botones son enlaces directos a Payhip
  • fuentes alojadas en la propia web (sin Google Fonts → sin enviar IPs a Google)
  • QR de USDT generado como imagen estática
  • cabeceras de seguridad (_headers): CSP con hashes, anti-iframe, HSTS, nosniff, permisos…
Uso: python3 build_netlify.py   (requiere: pip install segno)
"""
import os, re, sys, json, base64, hashlib, shutil, subprocess, urllib.request
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, '..'); out = os.path.join(root, 'lera-web')
subprocess.run([sys.executable, os.path.join(here, 'build_site.py')], check=True, stdout=subprocess.DEVNULL)
idx = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
tpl = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
codes = dict(re.findall(r"(recipes|belly|bundle): '(\w+)'", re.search(r'payhip: \{[^}]*\}', tpl).group(0)))
address = re.search(r"address: '(\w*)'", tpl).group(1)

shutil.rmtree(out, ignore_errors=True)
for d in ('img', 'video', 'fonts'): os.makedirs(os.path.join(out, d))

# ---------- fuentes locales ----------
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
GF = 'https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap'
css = urllib.request.urlopen(urllib.request.Request(GF, headers={'User-Agent': UA})).read().decode()
keep = ('cyrillic-ext', 'cyrillic', 'latin-ext', 'latin')
blocks = re.findall(r'/\* ([\w-]+) \*/\s*(@font-face \{.*?\})', css, re.S)
local_css, got = [], {}
for subset, block in blocks:
    if subset not in keep: continue
    url = re.search(r'url\((https://[^)]+)\)', block).group(1)
    if url not in got:
        name = 'f%02d.woff2' % len(got)
        open(os.path.join(out, 'fonts', name), 'wb').write(urllib.request.urlopen(url).read())
        got[url] = name
    local_css.append('/* %s */\n' % subset + block.replace(url, got[url]))
open(os.path.join(out, 'fonts', 'fonts.css'), 'w').write('\n'.join(local_css))

# ---------- QR estático ----------
import segno
if address:
    segno.make(address, error='m').save(os.path.join(out, 'img', 'usdt-qr.svg'), scale=5, border=2, dark='#151A14')

# ---------- index.html seguro ----------
h = idx
h = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', h)
h = re.sub(r'<link href="https://fonts.googleapis.com[^>]*>', '<link rel="stylesheet" href="fonts/fonts.css">', h)
h = re.sub(r'<script src="https://payhip.com/payhip.js"></script>\s*', '', h)
h = re.sub(r'<script src="https://cdnjs[^"]*"></script>\s*', '', h)
h = re.sub(r'/\* Ocultar el WhatsApp/chat del sitio anfitrión.*?\*/', '', h, flags=re.S)
def buy(m):
    k = m.group(2); return f'<a class="{m.group(1)}" data-k="{k}" href="https://payhip.com/b/{codes[k]}" rel="noopener">'
h = re.sub(r'<a class="(btn(?: lime)?) payhip-buy-button" data-k="(\w+)" href="#" data-theme="none">', buy, h)
h = h.replace("if(C.crypto.address && window.QRCode){ new QRCode($('cQr'),{text:C.crypto.address,width:140,height:140}); }",
              "if(C.crypto.address){ $('cQr').innerHTML='<img src=\"img/usdt-qr.svg\" width=\"150\" height=\"150\" alt=\"QR USDT\">'; }")
h = h.replace("""  document.querySelectorAll('.payhip-buy-button').forEach(function(a){
    var code=C.payhip[a.dataset.k]||''; a.href='https://payhip.com/b/'+code; a.setAttribute('data-product',code);
  });""", "")
assert 'payhip.js' not in h and 'cdnjs' not in h and 'googleapis' not in h and 'domdiseno' not in h
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)

# ---------- legal.html ----------
lg = open(os.path.join(root, 'legal-payhip-page.html'), encoding='utf-8').read()
for a, b in [
  ('<p>This online store (Lera’s store on Payhip) is owned and operated by:</p>', '<p>This website and Lera’s online store are owned and operated by:</p>'),
  ('<p><b>Platform.</b> The store runs on Payhip (Payhip Ltd, United Kingdom), an e-commerce platform that hosts the pages and delivers the files on Lera’s behalf.</p>', '<p><b>Platforms.</b> The website is hosted on Netlify (Netlify, Inc., USA). Sales and file delivery run on Payhip (Payhip Ltd, United Kingdom) on Lera’s behalf; payments are processed by PayPal.</p>'),
  ('<li><b>Google</b> — fonts on this page; and, if used, Google Workspace/Sheets to manage requests and clients.</li>', '<li><b>Google</b> — if used, Google Workspace/Sheets to manage requests and clients.</li><li><b>Netlify</b> (USA) — website hosting; technical server logs.</li>'),
  ('<p>Этот онлайн-магазин (магазин Леры на Payhip) принадлежит и управляется:</p>', '<p>Этот сайт и онлайн-магазин Леры принадлежат и управляются:</p>'),
  ('<p><b>Платформа.</b> Магазин работает на Payhip (Payhip Ltd, Великобритания) — платформе, которая размещает страницы и выдаёт файлы от имени Леры.</p>', '<p><b>Платформы.</b> Сайт размещён на Netlify (Netlify, Inc., США). Продажи и выдача файлов — через Payhip (Payhip Ltd, Великобритания) от имени Леры; платежи обрабатывает PayPal.</p>'),
  ('<li><b>Google</b> — шрифты на странице; при использовании — Google Таблицы для учёта заявок и клиентов.</li>', '<li><b>Google</b> — при использовании Google Таблицы для учёта заявок и клиентов.</li><li><b>Netlify</b> (США) — хостинг сайта; технические журналы сервера.</li>'),
  ('<p>Esta tienda online (la tienda de Lera en Payhip) es propiedad de y está gestionada por:</p>', '<p>Este sitio web y la tienda online de Lera son propiedad de y están gestionados por:</p>'),
  ('<p><b>Plataforma.</b> La tienda funciona en Payhip (Payhip Ltd, Reino Unido), plataforma de comercio electrónico que aloja las páginas y entrega los archivos por cuenta de Lera.</p>', '<p><b>Plataformas.</b> La web está alojada en Netlify (Netlify, Inc., EE. UU.). Las ventas y la entrega de archivos funcionan con Payhip (Payhip Ltd, Reino Unido) por cuenta de Lera; los pagos los procesa PayPal.</p>'),
  ('<li><b>Google</b>: fuentes tipográficas y, si se usa, Google Workspace/Sheets para gestionar solicitudes y clientes.</li>', '<li><b>Google</b>: si se usa, Google Workspace/Sheets para gestionar solicitudes y clientes.</li><li><b>Netlify</b> (EE. UU.): alojamiento de la web; registros técnicos del servidor.</li>'),
]:
    assert a in lg, a[:50]; lg = lg.replace(a, b)
lg = re.sub(r'Google Fonts receives your IP address to deliver the fonts\.', 'Fonts are served from this website itself.', lg)
lg = re.sub(r'Google Fonts получает IP-адрес для загрузки шрифтов\.', 'Шрифты загружаются с самого сайта.', lg)
lg = re.sub(r'Google Fonts recibe tu IP para servir las fuentes\.', 'Las fuentes se sirven desde la propia web.', lg)
lg = lg.replace('<style>', '<link rel="stylesheet" href="fonts/fonts.css">\n<style>', 1)
open(os.path.join(out, 'legal.html'), 'w', encoding='utf-8').write(lg)

# ---------- assets ----------
for f in sorted(set(re.findall(r'img/([\w.-]+\.(?:jpg|png|svg))', h + lg))):
    src = os.path.join(root, 'img', f)
    if os.path.exists(src): shutil.copy(src, os.path.join(out, 'img', f))
shutil.copy(os.path.join(root, 'video', 'hero.mp4'), os.path.join(out, 'video', 'hero.mp4'))

# ---------- cabeceras de seguridad ----------
def hashes(html):
    return ["'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode('utf-8')).digest()).decode()
            for s in re.findall(r'<script>(.*?)</script>', html, re.S)]
sh = ' '.join(hashes(h) + hashes(lg))
csp = ("default-src 'self'; "
       f"script-src 'self' {sh}; "
       "style-src 'self' 'unsafe-inline'; "
       "img-src 'self' data:; font-src 'self'; media-src 'self'; "
       "connect-src 'self'; frame-src 'none'; object-src 'none'; worker-src 'none'; "
       "base-uri 'none'; form-action 'self'; frame-ancestors 'none'; upgrade-insecure-requests")
headers = f"""/*
  Content-Security-Policy: {csp}
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Cross-Origin-Opener-Policy: same-origin
  Cross-Origin-Resource-Policy: same-origin
  X-Permitted-Cross-Domain-Policies: none

/img/*
  Cache-Control: public, max-age=604800
/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/video/*
  Cache-Control: public, max-age=604800
"""
open(os.path.join(out, '_headers'), 'w').write(headers)
open(os.path.join(out, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nDisallow: /legal.html\n')
os.makedirs(os.path.join(out, '.well-known'), exist_ok=True)
open(os.path.join(out, '.well-known', 'security.txt'), 'w').write('Contact: https://wa.me/6287723434348\nPreferred-Languages: en, ru\nExpires: 2027-12-31T00:00:00.000Z\n')
print('lera-web OK ·', len(got), 'fuentes ·', 'QR' if address else 'sin QR', '· hashes', len(sh.split()))
