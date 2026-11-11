#!/usr/bin/env python3
"""Genera las guías técnicas de SeñalVal en PDF (A4) con el logo y fotos de proyectos reales.

Uso:  python3 tools/guias/build_guias.py
Salida: guias/<slug>.pdf  (y guias/html/ con el HTML intermedio)
Requiere: Node + Playwright (Chromium) y pypdf.
"""
import json, pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from contenido import GUIAS
from pypdf import PdfReader, PdfWriter

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'guias'; HT = OUT / 'html'
HT.mkdir(parents=True, exist_ok=True)
LOGO = 'https://senalval.es/wp-content/uploads/2025/09/SenalVal-05-e1770365341698.png'
CONTACT = 'Calle Oro 34, 1º F (Valladolid) · 665 863 597 · luismi.olea@senalval.es · www.senalval.es'
EDICION = 'Edición noviembre 2026'

def ok(u):
    r = subprocess.run(['curl', '-sS', '-m', '25', '-o', '/dev/null', '-w', '%{http_code}|%{content_type}', u], capture_output=True, text=True).stdout
    return r.startswith('200') and 'image' in r
def img(u):
    for c in dict.fromkeys([u, re.sub(r'-\d+x\d+(\.\w+)$', r'\1', u)]):
        if ok(c): return c
    print('  ! imagen no disponible:', u); return None

CSS = '''
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&display=swap');
:root { --blue:#0B5CAD; --sky:#6FA8DC; --night:#0D1526; --ink:#0B0F19; --muted:#5B6475; --line:#E3E8EF; --soft:#F3F6FA; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: Montserrat, Arial, sans-serif; color: var(--ink); font-size: 9.6pt; line-height: 1.6; font-weight: 400; }
h1,h2,h3,h4 { margin: 0; letter-spacing: -.01em; }
b { font-weight: 600; }
/* ---------- Portada ---------- */
.cover { position: relative; width: 210mm; height: 297mm; overflow: hidden; color: #fff; background: var(--night); }
.cover__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.cover::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(13,21,38,.55) 0%, rgba(13,21,38,.35) 35%, rgba(13,21,38,.92) 72%, #0D1526 100%); }
.cover__in { position: absolute; inset: 0; z-index: 2; padding: 18mm 18mm 16mm; display: flex; flex-direction: column; }
.cover__logo { height: 11mm; width: auto; filter: brightness(0) invert(1); align-self: flex-start; }
.cover__kicker { margin-top: auto; font-size: 8pt; letter-spacing: .28em; text-transform: uppercase; color: var(--sky); display: flex; align-items: center; gap: 4mm; }
.cover__kicker::before { content: ""; width: 12mm; height: 1px; background: var(--sky); }
.cover__num { font-size: 64pt; font-weight: 300; line-height: 1; color: rgba(255,255,255,.18); margin: 4mm 0 -2mm; }
.cover h1 { font-size: 30pt; font-weight: 300; line-height: 1.12; max-width: 150mm; }
.cover__sub { margin-top: 6mm; font-size: 12pt; font-weight: 300; color: rgba(255,255,255,.82); max-width: 140mm; }
.cover__foot { margin-top: 14mm; padding-top: 5mm; border-top: 1px solid rgba(255,255,255,.2); display: flex; justify-content: space-between; font-size: 7.5pt; color: rgba(255,255,255,.65); }
.cover__cap { position: absolute; z-index: 2; top: 18mm; right: 18mm; max-width: 70mm; text-align: right; font-size: 7pt; color: rgba(255,255,255,.75); }
/* ---------- Interior ---------- */
.page { padding: 0 18mm; }
.intro { padding: 10mm 0 0; }
.intro .kick, .sec .kick { font-size: 7.5pt; letter-spacing: .24em; text-transform: uppercase; color: var(--blue); display: flex; align-items: center; gap: 3mm; margin-bottom: 4mm; }
.kick::before { content: ""; width: 10mm; height: 1px; background: var(--blue); }
.intro p.lead { font-size: 13pt; font-weight: 300; line-height: 1.55; color: var(--ink); }
.toc { margin: 6mm 0 0; padding: 6mm 7mm; background: var(--soft); border-radius: 4mm; columns: 2; column-gap: 10mm; }
.toc div { break-inside: avoid; display: flex; gap: 3mm; padding: 1.3mm 0; font-size: 9pt; }
.toc span { color: var(--blue); font-weight: 500; min-width: 6mm; }
.sec { padding-top: 9mm; break-inside: auto; }
.sec .kick, .sec h2 { break-after: avoid; }
.sec__head { break-inside: avoid; break-after: avoid; }
.sec h2 { font-size: 17pt; font-weight: 300; margin-bottom: 4mm; display: flex; align-items: baseline; gap: 4mm; }
.sec h2 em { font-style: normal; font-size: 10pt; font-weight: 500; color: var(--blue); }
.sec p { margin: 0 0 3mm; }
.t { width: 100%; border-collapse: collapse; margin: 3mm 0 4mm; font-size: 8.6pt; break-inside: avoid; }
.t th { text-align: left; font-weight: 500; font-size: 7.4pt; letter-spacing: .1em; text-transform: uppercase; color: #fff; background: var(--night); padding: 2.4mm 3mm; }
.t td { padding: 2.4mm 3mm; border-bottom: 1px solid var(--line); vertical-align: top; }
.t tr { break-inside: avoid; }
.t tbody tr:nth-child(even) td { background: #FAFBFD; }
.t--compact td { padding: 1.8mm 3mm; }
.t--mat { font-size: 8pt; } .t--mat td:nth-child(3), .t--mat td:nth-child(4), .t--mat th:nth-child(3), .t--mat th:nth-child(4) { text-align: center; color: var(--blue); }
.legend { font-size: 7.5pt; color: var(--muted); }
.note { padding: 3.5mm 5mm; border-left: 2px solid var(--blue); background: var(--soft); border-radius: 0 3mm 3mm 0; font-size: 8.8pt; break-inside: avoid; }
ul.check, ul.cols { list-style: none; padding: 0; margin: 2mm 0 4mm; }
ul.check li { position: relative; padding: 1.6mm 0 1.6mm 8mm; break-inside: avoid; }
ul.check li::before { content: ""; position: absolute; left: 0; top: 2.6mm; width: 4mm; height: 4mm; border-radius: 50%; background: var(--blue) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m4 8.5 2.5 2.5L12 5.5' fill='none' stroke='white' stroke-width='2'/%3E%3C/svg%3E") center/80% no-repeat; }
ul.cols { columns: 2; column-gap: 8mm; } ul.cols li { break-inside: avoid; padding: 0 0 3mm; }
ol.errors { counter-reset: e; list-style: none; padding: 0; margin: 2mm -2mm; font-size: 0; }
ol.errors li { display: inline-block; vertical-align: top; width: calc(50% - 4mm); margin: 0 2mm 3mm; font-size: 8.8pt; counter-increment: e; position: relative; padding: 3.5mm 4mm 3.5mm 13mm; border: 1px solid var(--line); border-radius: 3mm; break-inside: avoid; font-size: 8.8pt; }
ol.errors li::before { content: counter(e, decimal-leading-zero); position: absolute; left: 4mm; top: 3.2mm; font-size: 11pt; font-weight: 300; color: var(--blue); }
.steps { display: grid; gap: 3mm; margin: 2mm 0 4mm; }
.step { position: relative; display: grid; grid-template-columns: 12mm 1fr; column-gap: 4mm; padding: 4mm; border: 1px solid var(--line); border-radius: 3mm; break-inside: avoid; }
.step span { grid-row: 1 / 4; width: 10mm; height: 10mm; border-radius: 50%; background: var(--night); color: #fff; display: grid; place-items: center; font-weight: 500; }
.step h4 { font-size: 10.5pt; font-weight: 500; }
.step p { margin: 1mm 0 0; } .step .d { color: var(--blue); font-size: 8.2pt; }
.grid4, .grid2 { margin: 2mm -2mm 3mm; font-size: 0; }
.card { display: inline-block; vertical-align: top; width: calc(50% - 4mm); margin: 0 2mm 4mm; padding: 5mm; border: 1px solid var(--line); border-radius: 3mm; break-inside: avoid; font-size: 9.6pt; }
.card h4 { font-size: 10.5pt; font-weight: 500; margin-bottom: 1.5mm; color: var(--blue); }
.card p { margin: 0; font-size: 8.8pt; }
.sw { display: inline-block; width: 3.5mm; height: 3.5mm; border-radius: 1mm; vertical-align: -0.5mm; margin-right: 1.5mm; }

.keys { margin: 6mm 0 0; display: grid; gap: 3mm; }
.keys__t { font-size: 7.5pt; letter-spacing: .24em; text-transform: uppercase; color: var(--muted); margin: 0 0 1mm; }
.key { display: grid; grid-template-columns: 9mm 1fr; align-items: start; padding: 3.5mm 4mm; border-radius: 3mm; background: var(--night); color: #fff; }
.key span { width: 6.5mm; height: 6.5mm; border-radius: 50%; background: var(--blue); display: grid; place-items: center; font-size: 8pt; font-weight: 500; }
.key p { margin: 0; font-size: 9.2pt; font-weight: 300; line-height: 1.5; }
.ph1 { margin: 6mm 0 0; break-inside: avoid; }
.ph1 img { width: 100%; height: 44mm; object-fit: cover; border-radius: 3mm; }
.ph1 figcaption { font-size: 7.2pt; color: var(--muted); margin-top: 1.5mm; }
.intro + .sec { break-before: page; padding-top: 2mm; }
.bc { position: relative; width: 210mm; height: 297mm; background: radial-gradient(120% 80% at 100% 0%, #0B3F7A 0%, var(--night) 60%); color: #fff; overflow: hidden; }
.bc::before { content: ""; position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.04) 1px, transparent 1px); background-size: 12mm 12mm; }
.bc__in { position: relative; height: 100%; padding: 22mm 20mm; display: flex; flex-direction: column; }
.bc__logo { height: 13mm; width: auto; align-self: flex-start; filter: brightness(0) invert(1); }
.bc__kick { margin-top: auto; font-size: 8pt; letter-spacing: .24em; text-transform: uppercase; color: var(--sky); }
.bc h2 { font-size: 28pt; font-weight: 300; line-height: 1.15; margin: 4mm 0 5mm; max-width: 150mm; }
.bc__lead { font-size: 11.5pt; font-weight: 300; color: rgba(255,255,255,.82); max-width: 140mm; margin: 0 0 12mm; }
.bc__grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6mm 10mm; padding: 8mm 0; border-top: 1px solid rgba(255,255,255,.15); border-bottom: 1px solid rgba(255,255,255,.15); font-size: 11pt; }
.bc__grid span { display: block; font-size: 7pt; letter-spacing: .2em; text-transform: uppercase; color: var(--sky); margin-bottom: 1.5mm; }
.bc__cl { margin: 8mm 0 0; font-size: 7.6pt; line-height: 1.8; color: rgba(255,255,255,.6); }
/* Caso real */
.case { margin-top: 9mm; padding: 7mm; border-radius: 4mm; background: var(--night); color: #fff; break-inside: avoid; }
.case .kick { color: var(--sky); } .case .kick::before { background: var(--sky); }
.case h3 { font-size: 14pt; font-weight: 300; margin-bottom: 3mm; }
.case p { color: rgba(255,255,255,.85); margin: 0 0 5mm; }
.case .ph { display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; }
.case .ph img { width: 100%; height: 42mm; object-fit: cover; border-radius: 2mm; }
/* Checklist + fuentes + contraportada */
.final { padding-top: 9mm; }
.box { border: 1px solid var(--line); border-radius: 4mm; padding: 6mm 7mm; margin-bottom: 7mm; break-inside: avoid; }
.box h3 { font-size: 13pt; font-weight: 300; margin-bottom: 3mm; }
.cl { list-style: none; padding: 0; margin: 0; columns: 2; column-gap: 8mm; }
.cl li { break-inside: avoid; display: flex; gap: 3mm; padding: 1.6mm 0; font-size: 8.8pt; }
.cl li::before { content: ""; flex: 0 0 3.6mm; height: 3.6mm; margin-top: .6mm; border: 1.2px solid var(--blue); border-radius: .8mm; }
.src { padding-left: 5mm; margin: 0; font-size: 8pt; color: var(--muted); } .src li { padding: 1mm 0; }
.disc { font-size: 7.4pt; color: var(--muted); margin-top: 4mm; }
.back { margin-top: 2mm; padding: 8mm; border-radius: 4mm; background: linear-gradient(135deg, #0B3F7A 0%, var(--night) 70%); color: #fff; display: grid; grid-template-columns: 1fr auto; gap: 6mm; align-items: center; break-inside: avoid; }
.back img { height: 9mm; filter: brightness(0) invert(1); margin-bottom: 4mm; }
.back h3 { font-size: 15pt; font-weight: 300; margin-bottom: 2mm; }
.back p { margin: 0; color: rgba(255,255,255,.8); font-size: 8.6pt; }
.back .c { text-align: right; font-size: 8.6pt; line-height: 1.9; }
.back .c b { color: var(--sky); font-weight: 500; }
'''

def cover_html(g, cover):
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS} @page {{ size: A4; margin: 0; }}</style></head><body>
<section class="cover">{f'<img class="cover__img" src="{cover}">' if cover else ''}
<p class="cover__cap">{g["cover_caption"]}</p>
<div class="cover__in">
  <img class="cover__logo" src="{LOGO}" alt="SeñalVal">
  <p class="cover__kicker">Guía técnica SeñalVal</p>
  <p class="cover__num">{g["num"]}</p>
  <h1>{g["title"]}</h1>
  <p class="cover__sub">{g["subtitle"]}</p>
  <div class="cover__foot"><span>Gestión integral de proyectos de señalización de alta exigencia</span><span>{EDICION}</span></div>
</div></section></body></html>'''

def _split(body):
    # El título del apartado viaja siempre con su primer bloque (párrafo, tabla o lista)
    b = body.strip()
    m = re.match(r'(<(p|table|ul|ol|div)[\s>].*?</\2>)(.*)', b, re.S)
    return (m.group(1), m.group(3)) if m else (b, '')
def first(body): return _split(body)[0]
def rest(body): return _split(body)[1]

def back_html(g):
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS} @page {{ size: A4; margin: 0; }}</style></head><body>
<section class="bc"><div class="bc__in">
  <img class="bc__logo" src="{LOGO}" alt="SeñalVal">
  <p class="bc__kick">Gestión integral de proyectos de señalización de alta exigencia</p>
  <h2>¿Tiene un proyecto o una licitación de señalización?</h2>
  <p class="bc__lead">Le preparamos una propuesta de alcance con un único responsable: estudio, diseño, fabricación, instalación y mantenimiento.</p>
  <div class="bc__grid">
    <div><span>Dirección</span>Calle Oro 34, 1º F<br>Valladolid</div>
    <div><span>Teléfono y WhatsApp</span>665 863 597</div>
    <div><span>Email</span>luismi.olea@senalval.es</div>
    <div><span>Web</span>www.senalval.es</div>
  </div>
  <p class="bc__cl">Han confiado en SeñalVal: Aena · ADIF · Guardia Civil · Comunidad de Madrid · Junta de Castilla y León · Real Valladolid · Coca-Cola · Toyota · Mahou · Dragados · Clece · Fundación Laboral de la Construcción</p>
</div></section></body></html>'''

def body_html(g, case_imgs):
    toc = ''.join(f'<div><span>{i+1:02d}</span>{s["h"]}</div>' for i, s in enumerate(g['sections'])) + f'<div><span>{len(g["sections"])+1:02d}</span>{g["case"]["title"].split(" · ")[0]}</div><div><span>{len(g["sections"])+2:02d}</span>Lista de comprobación y fuentes</div>'
    keys = ''.join(f'<div class="key"><span>{i+1}</span><p>{k}</p></div>' for i, k in enumerate(g['keys']))
    photo = f'<figure class="ph1"><img src="{g["_photo"]}"><figcaption>{g["photo_caption"]}</figcaption></figure>' if g.get('_photo') else ''
    secs = ''.join(f'<section class="sec"><div class="sec__head"><p class="kick">Apartado {i+1:02d}</p><h2>{s["h"]}</h2></div>{s["body"]}</section>' for i, s in enumerate(g['sections']))
    c = g['case']
    ph = ''.join(f'<img src="{u}">' for u in case_imgs)
    cl = ''.join(f'<li>{x}</li>' for x in g['checklist'])
    src = ''.join(f'<li>{x}</li>' for x in g['sources'])
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS} @page {{ size: A4; margin: 16mm 0 18mm; }}</style></head><body><div class="page">
<section class="intro"><p class="kick">Introducción</p><p class="lead">{g["intro"]}</p>
<div class="keys"><p class="keys__t">Claves de esta guía</p>{keys}</div>
<div class="toc">{toc}</div>
{photo}</section>
{secs}
<section class="case"><p class="kick">{c["title"].split(" · ")[0]}</p><h3>{c["title"].split(" · ", 1)[1]}</h3><p>{c["text"]}</p><div class="ph">{ph}</div></section>
<section class="final">
  <div class="box"><h3>Lista de comprobación</h3><ul class="cl">{cl}</ul></div>
  <div class="box"><h3>Fuentes y normativa citada</h3><ol class="src">{src}</ol>
  <p class="disc">Guía orientativa elaborada por SeñalVal. Las referencias normativas corresponden a la legislación y las normas técnicas vigentes en la fecha de edición; antes de redactar un proyecto o un pliego, compruebe la versión en vigor en el BOE y en UNE. Esta guía no sustituye al proyecto técnico ni a la dirección facultativa.</p></div>
</section>
</div></body></html>'''

FOOT = '<div style="width:100%;font-family:Arial,sans-serif;font-size:7px;color:#5B6475;padding:0 18mm;display:flex;justify-content:space-between;"><span>SeñalVal · TITLE</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
HEAD = '<div style="width:100%;font-family:Arial,sans-serif;font-size:7px;color:#0B5CAD;padding:0 18mm;letter-spacing:2px;text-transform:uppercase;">Guía técnica NUM</div>'

jobs = []
for g in GUIAS:
    print('Guía', g['num'], g['title'])
    cover = img(g['cover'])
    g['_photo'] = img(g['photo'])
    case_imgs = [x for x in (img(u) for u in g['case']['imgs']) if x]
    (HT / f'{g["slug"]}-portada.html').write_text(cover_html(g, cover), encoding='utf-8')
    (HT / f'{g["slug"]}-contra.html').write_text(back_html(g), encoding='utf-8')
    (HT / f'{g["slug"]}-cuerpo.html').write_text(body_html(g, case_imgs), encoding='utf-8')
    jobs.append(dict(slug=g['slug'], foot=FOOT.replace('TITLE', g['title']), head=HEAD.replace('NUM', g['num'])))

js = r'''
const {chromium}=require('playwright');const jobs=JSON.parse(process.argv[2]);const dir=process.argv[3];
(async()=>{const b=await chromium.launch();
for(const j of jobs){
  for(const part of ['portada','cuerpo','contra']){
    const p=await b.newPage();await p.goto('file://'+dir+'/'+j.slug+'-'+part+'.html',{waitUntil:'networkidle'});
    await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
    const opt={path:dir+'/'+j.slug+'-'+part+'.pdf',format:'A4',printBackground:true,preferCSSPageSize:true};
    if(part==='cuerpo'){opt.displayHeaderFooter=true;opt.headerTemplate=j.head;opt.footerTemplate=j.foot;}
    await p.pdf(opt);await p.close();}
}
await b.close();})();'''
(HT / 'render.js').write_text(js)
subprocess.run(['node', str(HT / 'render.js'), json.dumps(jobs), str(HT)], check=True)

for j in jobs:
    w = PdfWriter()
    for part in ('portada', 'cuerpo', 'contra'):
        for pg in PdfReader(str(HT / f'{j["slug"]}-{part}.pdf')).pages: w.add_page(pg)
    w.add_metadata({'/Title': next(g['title'] for g in GUIAS if g['slug'] == j['slug']), '/Author': 'SeñalVal', '/Subject': 'Guía técnica SeñalVal'})
    out = OUT / f'{j["slug"]}.pdf'
    with open(out, 'wb') as f: w.write(f)
    print(' ->', out.relative_to(ROOT), len(w.pages), 'páginas', round(out.stat().st_size / 1024), 'KB')
