#!/usr/bin/env python3
"""Genera la portada de SeñalVal en un solo archivo, lista para WordPress.

Salida (carpeta wordpress/):
  senalval-portada.html   Página completa (se puede abrir directamente en el navegador).
  senalval-bloque.html    Solo el contenido (<style> + HTML + <script>) para pegar en un
                          widget HTML de Elementor o en un bloque "HTML personalizado".

Todas las imágenes y logos se cargan desde senalval.es (y algunos logos públicos desde
Wikimedia Commons), así que no hay que subir ningún archivo aparte.

Uso:  python3 tools/build_wordpress.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'wordpress'
OUT.mkdir(exist_ok=True)

html = (ROOT / 'index.html').read_text(encoding='utf-8')
css = (ROOT / 'css' / 'styles.css').read_text(encoding='utf-8')
js = (ROOT / 'js' / 'main.js').read_text(encoding='utf-8')

if 'assets/' in html:
    raise SystemExit('index.html todavía referencia archivos locales en assets/')

full = html.replace('<link rel="stylesheet" href="css/styles.css">', '<style>\n' + css + '\n</style>')
full = full.replace('<script src="js/main.js" defer></script>', '<script>\n' + js + '\n</script>')
(OUT / 'senalval-portada.html').write_text(full, encoding='utf-8')

# Fragmento para pegar dentro de WordPress: fuentes + estilos + datos estructurados + cuerpo + script
fonts = '\n'.join(re.findall(r'<link rel="preconnect"[^>]*>|<link href="https://fonts\.googleapis\.com[^>]*>', html))
ldjson = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.S).group(0)
body = re.search(r'<body>(.*)</body>', html, re.S).group(1)
body = body.replace('<script src="js/main.js" defer></script>', '')
block = f'''<!-- SeñalVal · Portada. Pegar en un widget HTML de Elementor (plantilla "Elementor Canvas")
     o en un bloque "HTML personalizado" de una página con plantilla en blanco. -->
{fonts}
<style>
{css}
</style>
{ldjson}
{body.strip()}
<script>
{js}
</script>
'''
(OUT / 'senalval-bloque.html').write_text(block, encoding='utf-8')
for f in ('senalval-portada.html', 'senalval-bloque.html'):
    print(f, round((OUT / f).stat().st_size / 1024), 'KB')
