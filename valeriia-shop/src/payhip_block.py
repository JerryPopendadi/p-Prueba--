# Genera ../lera-payhip-bloque.html: la web dentro de un Shadow DOM (aislada del CSS de Payhip).
# Uso: python3 payhip_block.py <commit_sha>
import re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
sha = sys.argv[1]
CDN = f'https://cdn.jsdelivr.net/gh/JerryPopendadi/p-Prueba--@{sha}/valeriia-shop/'
src = open(os.path.join(here, '..', 'index.html'), encoding='utf-8').read()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
body = re.search(r'<body>(.*)</body>', src, re.S).group(1)
config = re.search(r'(<script>\s*/\* =+.*?</script>)', src, re.S).group(1)

# --- CSS: html/body/:root -> :host / .lb
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
css = css.replace(':root{', ':host{')
css = re.sub(r'html\[lang=(\w+)\] ', r':host([data-lang=\1]) ', css)
css = css.replace('html [data-', '[data-')
css = css.replace('html{scroll-behavior:smooth}', '')
css = re.sub(r'(^|\n|\})body\{', r'\1.lera-body{', css)
css = css.replace('header{position:sticky;', 'header{position:relative;')
css = ':host{all:initial;display:block}\n' + css

# --- HTML: separar scripts, rutas al CDN
scripts = re.findall(r'<script[^>]*>.*?</script>', body, re.S)
html = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.S)
html = re.sub(r'(src|poster)="(img|video)/', lambda m: f'{m.group(1)}="{CDN}{m.group(2)}/', html)
html = re.sub(r"url\((img)/", f"url({CDN}img/", html)
html = re.sub(r'<p style="margin-top:6px;font-size:12px">.*?</p>', '', html, flags=re.S)
html = html.replace('href="legal.html"', 'href="#" id="legalLink"')
html = html.replace('class="btn payhip-buy-button"', 'class="btn buyLink"').replace('class="btn lime payhip-buy-button"', 'class="btn lime buyLink"')

main = [s for s in scripts if 'var C=window.CONFIG' in s][0]
main = re.sub(r'^<script>|</script>$', '', main.strip())
main = main.replace("'img/", "'" + CDN + "img/")
main = main.replace("html=document.documentElement", "html=HOST")
main = main.replace("html.lang=lang;", "html.setAttribute('data-lang',lang);")
main = main.replace("document.getElementById(", "R.getElementById(").replace("document.querySelectorAll(", "R.querySelectorAll(").replace("document.querySelector(", "R.querySelector(")
main = main.replace("""  document.querySelectorAll('.payhip-buy-button')""", "X")
main = main.replace("""  R.querySelectorAll('.payhip-buy-button').forEach(function(a){
    var code=C.payhip[a.dataset.k]||''; a.href='https://payhip.com/b/'+code; a.setAttribute('data-product',code);
  });""", """  R.querySelectorAll('.buyLink').forEach(function(a){ a.href='https://payhip.com/b/'+(C.payhip[a.dataset.k]||''); });
  if(C.legalUrl){ var lg=R.getElementById('legalLink'); if(lg){ lg.href=C.legalUrl; lg.target='_blank'; } }""")
main = main.replace("var hdr=$('hdr'), st=$('sticky');", "var hdr=$('hdr'), st=$('sticky'); hdr.classList.add('solid');")
# anclas internas (#guides…) dentro del shadow
main = main.replace("})();", """  R.querySelectorAll('a[href^="#"]').forEach(function(a){ var id=a.getAttribute('href').slice(1); if(!id||a.id==='legalLink') return; a.addEventListener('click',function(e){ var t=R.getElementById(id); if(t){ e.preventDefault(); t.scrollIntoView({behavior:'smooth'}); } }); });
})();""")
assert 'document.getElementById' not in main

cfg = config.replace("  apiUrl: ''", "  legalUrl: '',   // enlace a la página de privacidad/condiciones de Lera en Payhip\n  apiUrl: ''")
qr = '<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>'
fonts = '<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
out = f'''<!-- LERA · bloque para Payhip: Store → editar página → Add block → Embed code → pegar TODO -->
{fonts}
{cfg}
{qr}
<div id="lera-host" data-lang="en"></div>
<template id="lera-tpl"><style>{css}</style><div class="lera-body">{html}</div></template>
<script>
(function(){{
  var HOST=document.getElementById('lera-host'); if(!HOST||HOST.shadowRoot) return;
  var R=HOST.attachShadow({{mode:'open'}}); R.appendChild(document.getElementById('lera-tpl').content.cloneNode(true));
{main}
}})();
</script>
'''
open(os.path.join(here, '..', 'lera-payhip-bloque.html'), 'w', encoding='utf-8').write(out)
print('lera-payhip-bloque.html', len(out))
