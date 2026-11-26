"""THE FACES PARTNERS · QR cards for the salons (print-ready PDF + PNG preview).

Two formats, each in an Ubud and a Sanur version (the QR carries utm_content=ubud/sanur,
so the lead sheet shows which salon the person came from):
  - A6 table card, 105 x 148 mm (+3 mm bleed)
  - business card, 85 x 55 mm, front and back (+3 mm bleed)
Run:  python3 build.py  then  node render.js out/jobs.json
"""
import base64
import json
import os

import segno

H = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://thefacespeace.com/?utm_source=salon&utm_medium=qr&utm_campaign=partner_card&utm_content='
SITE = 'thefacespeace.com'
LOGO = 'data:image/png;base64,' + base64.b64encode(open(H + '/logo-gold.png', 'rb').read()).decode()
# Languages of the thefacespeace.com site switcher (EN, ES, FR, ID, RU, UA).
LANGS = 'English · Español · Français · Bahasa Indonesia · Русский · Українська'
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500'
         '&family=Montserrat:wght@300;400;500;600&display=swap&subset=cyrillic" rel="stylesheet">')
CSS = """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0F0D0B;--gold:#E9BE62;--cream:#F3EEE6;--txt:rgba(255,255,255,.88);--mut:rgba(255,255,255,.6)}
html,body{background:var(--bg)}
body{font-family:Montserrat,sans-serif;color:var(--txt);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{position:relative;overflow:hidden;background:var(--bg);page-break-after:always}
.frame{position:absolute;border:0.25mm solid rgba(233,190,98,.45)}
.eye{color:var(--gold);letter-spacing:.28em;font-weight:500;text-transform:uppercase}
h1{font-family:'Cormorant Garamond',serif;font-weight:400;color:#fff;line-height:1.05}
.qr{background:var(--cream);border-radius:2mm;display:flex;align-items:center;justify-content:center}
.qr svg{display:block;width:100%;height:100%}
.langs{color:var(--mut);letter-spacing:.02em}
.legal{color:rgba(255,255,255,.45)}
.line{background:var(--gold);opacity:.85}
.url{color:#fff;letter-spacing:.08em;font-weight:500}
"""


def qr(site):
    return segno.make(BASE + site, error='q').svg_inline(scale=1, border=2, omitsize=True, dark='#14110D', light=None)


def a6(site):
    return f"""<div class="pg" style="width:111mm;height:154mm">
<div class="frame" style="left:9mm;top:9mm;right:9mm;bottom:9mm"></div>
<div style="position:absolute;left:3mm;right:3mm;top:3mm;bottom:3mm;padding:11mm 11mm 11.5mm;display:flex;flex-direction:column;align-items:center;text-align:center">
<img src="{LOGO}" style="width:27mm;margin-top:1mm">
<div class="eye" style="font-size:2.2mm;margin-top:5mm">For business partners</div>
<h1 style="font-size:8.6mm;margin-top:2.8mm">Love this place?<br>You can co-own it.</h1>
<div class="line" style="width:12mm;height:.3mm;margin:3.6mm 0"></div>
<p style="font-size:2.85mm;line-height:1.48;font-weight:300;max-width:74mm">Become a shareholder in a THE FACES spa in Bali. Our team runs it every day. You receive a monthly report.</p>
<div class="qr" style="width:29mm;height:29mm;margin-top:4.5mm;padding:1mm">{qr(site)}</div>
<div style="font-size:2.45mm;letter-spacing:.16em;font-weight:600;color:var(--gold);margin-top:2.6mm;text-transform:uppercase">Scan to meet the founders</div>
<div class="url" style="font-size:2.7mm;margin-top:1.6mm">{SITE}</div>
<div style="margin-top:auto;width:100%">
<div style="font-size:1.95mm;color:var(--gold);letter-spacing:.12em;text-transform:uppercase;margin-bottom:1mm">Our website speaks your language</div>
<div class="langs" style="font-size:2.15mm;line-height:1.5">{LANGS}</div>
<div class="legal" style="font-size:1.65mm;margin-top:1.6mm">Information only, not a public offer. Terms are shared privately.</div>
</div></div></div>"""


def card(site):
    front = f"""<div class="pg" style="width:91mm;height:61mm">
<div class="frame" style="left:6.5mm;top:6.5mm;right:6.5mm;bottom:6.5mm"></div>
<div style="position:absolute;left:3mm;top:3mm;width:85mm;height:55mm;padding:7mm 7mm 6.5mm 8mm;display:flex;gap:5mm;align-items:center">
<div style="flex:1;display:flex;flex-direction:column;height:100%">
<img src="{LOGO}" style="width:21mm">
<div class="eye" style="font-size:1.65mm;margin-top:3.2mm">For business partners</div>
<h1 style="font-size:5.4mm;margin-top:1.6mm">Love this place?<br>You can co-own it.</h1>
<p style="font-size:2.05mm;line-height:1.45;font-weight:300;margin-top:auto">Our team runs the spa.<br>You receive a monthly report.</p>
</div>
<div style="display:flex;flex-direction:column;align-items:center">
<div class="qr" style="width:24mm;height:24mm;padding:.9mm">{qr(site)}</div>
<div class="url" style="font-size:1.75mm;margin-top:1.8mm">{SITE}</div>
</div></div></div>"""
    back = f"""<div class="pg" style="width:91mm;height:61mm">
<div class="frame" style="left:6.5mm;top:6.5mm;right:6.5mm;bottom:6.5mm"></div>
<div style="position:absolute;left:3mm;top:3mm;width:85mm;height:55mm;padding:7.5mm 9mm;display:flex;flex-direction:column;text-align:center;align-items:center">
<div class="eye" style="font-size:1.65mm">How it works</div>
<div style="font-size:2.35mm;line-height:1.75;margin-top:2.2mm;font-weight:300">
<span style="color:var(--gold)">1</span> Private call with the founders &nbsp; <span style="color:var(--gold)">2</span> Visit the spa<br>
<span style="color:var(--gold)">3</span> Review the documents &nbsp; <span style="color:var(--gold)">4</span> Sign at the notary</div>
<div class="line" style="width:9mm;height:.25mm;margin:2.6mm 0"></div>
<div style="font-size:1.6mm;color:var(--gold);letter-spacing:.12em;text-transform:uppercase">Our website speaks your language</div>
<div class="langs" style="font-size:1.95mm;line-height:1.55;margin-top:1mm">{LANGS}</div>
<div class="url" style="font-size:2.1mm;margin-top:auto">{SITE}</div>
<div class="legal" style="font-size:1.4mm;margin-top:.8mm">Not a public offer</div>
</div></div>"""
    return front + back


os.makedirs(H + '/out', exist_ok=True)
jobs = []
for site in ('ubud', 'sanur'):
    for kind, fn, w, h in (('A6-mesa', a6, '111mm', '154mm'), ('tarjeta-85x55', card, '91mm', '61mm')):
        f = '%s/out/THE-FACES-partners-%s-%s.html' % (H, kind, site)
        page = ('<!doctype html><html><head><meta charset="utf-8">' + FONTS + '<style>' + CSS
                + '@page{size:%s %s;margin:0}</style></head><body>%s</body></html>' % (w, h, fn(site)))
        open(f, 'w').write(page)
        jobs.append(dict(html=f, w=w, h=h))
json.dump(jobs, open(H + '/out/jobs.json', 'w'))
print(len(jobs), 'pages')
