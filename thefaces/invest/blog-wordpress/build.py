"""Wraps every blog article in a self-styled block for WordPress (Custom HTML block).
The site's global CSS turns paragraph text white; this scoped style forces readable colours.
No square brackets anywhere (the site runs shortcodes)."""
import re, os, glob
D = os.path.dirname(os.path.abspath(__file__))
SRC = sorted(glob.glob(os.path.join(D, '..', 'contenido', 'blog', '*.html')) + glob.glob(os.path.join(D, '..', 'contenido-2', 'blog', '*.html')))
CSS = """<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
.tfp{--ink:#1c1e1b;--muted:#4a5049;--gold:#b08d4a;--line:#e6e1d6;--sand:#faf7f0;max-width:780px;margin:0 auto;font-family:Montserrat,Arial,sans-serif!important;color:var(--ink)!important;font-size:17px;line-height:1.8}
.tfp *{box-sizing:border-box;font-family:inherit!important}
.tfp p,.tfp li,.tfp td,.tfp th,.tfp span,.tfp em,.tfp strong{color:var(--ink)!important}
.tfp p{margin:0 0 20px!important;font-size:17px!important;font-weight:400!important;line-height:1.8!important}
.tfp>p:first-child{font-size:20px!important;line-height:1.7!important;color:var(--ink)!important;border-left:3px solid var(--gold);padding-left:22px}
.tfp h2{font-size:28px!important;font-weight:500!important;line-height:1.3!important;color:var(--ink)!important;margin:48px 0 18px!important;letter-spacing:-.01em}
.tfp h2:before{content:"";display:block;width:44px;height:2px;background:var(--gold);margin-bottom:16px}
.tfp h3{font-size:19px!important;font-weight:600!important;color:var(--ink)!important;margin:26px 0 8px!important}
.tfp ul,.tfp ol{margin:0 0 24px 0!important;padding-left:24px!important}
.tfp li{margin:0 0 10px!important;font-size:17px!important;line-height:1.7!important}
.tfp li::marker{color:var(--gold)}
.tfp a{color:var(--gold)!important;text-decoration:underline!important;text-underline-offset:3px;font-weight:500}
.tfp table{width:100%!important;border-collapse:collapse!important;margin:10px 0 30px!important;font-size:15px!important;border:0!important}
.tfp th{background:var(--ink)!important;color:#fff!important;font-weight:500!important;text-align:left!important;padding:12px 14px!important;border:0!important;font-size:13px!important;letter-spacing:.06em;text-transform:uppercase}
.tfp td{padding:12px 14px!important;border:0!important;border-bottom:1px solid var(--line)!important;background:#fff!important}
.tfp tr:nth-child(even) td{background:var(--sand)!important}
.tfp .tfp-cta{background:#141513!important;border:0!important;border-radius:6px;padding:30px 30px 24px!important;margin:40px 0!important}
.tfp .tfp-cta p,.tfp .tfp-cta strong{color:#fff!important}
.tfp .tfp-cta a{display:inline-block;margin:8px 12px 0 0;padding:12px 22px;border:1px solid var(--gold);color:#e4c27a!important;text-decoration:none!important;font-size:14px;letter-spacing:.08em;text-transform:uppercase;border-radius:3px}
.tfp .tfp-cta a:first-of-type{background:var(--gold);color:#141513!important}
.tfp .tfp-note,.tfp .tfp-note em{font-size:13px!important;color:#7a7f78!important;line-height:1.6!important;border-top:1px solid var(--line);padding-top:18px;margin-top:40px!important}
@media(max-width:600px){.tfp{font-size:16px}.tfp p,.tfp li{font-size:16px!important}.tfp h2{font-size:24px!important}.tfp>p:first-child{font-size:18px!important}.tfp table{display:block;overflow-x:auto;white-space:nowrap}}
</style>"""
notes = []
for f in SRC:
    s = open(f, encoding='utf-8').read()
    m = re.match(r'\s*<!--(.*?)-->\s*', s, re.S)
    meta, body = (m.group(1).strip(), s[m.end():]) if m else ('', s)
    body = re.sub(r'<div style="border:[^"]*">', '<div class="tfp-cta">', body)
    body = re.sub(r'<p><em>(.*?)</em></p>\s*$', r'<p class="tfp-note"><em>\1</em></p>', body.strip(), flags=re.S)
    assert '[' not in body and ']' not in body, f
    out = CSS + '\n<div class="tfp">\n' + body + '\n</div>\n'
    name = os.path.basename(f)
    open(os.path.join(D, name), 'w', encoding='utf-8').write(out)
    notes.append('### ' + name + '\n' + meta.replace('SEO\n', '') + '\n')
open(os.path.join(D, 'DATOS-SEO.md'), 'w', encoding='utf-8').write('# Datos para WordPress y Yoast de cada artículo\n\n' + '\n'.join(notes))
print(len(SRC))
