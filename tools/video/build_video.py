#!/usr/bin/env python3
"""Vídeo de presentación de SeñalVal (≈78 s, 1920×1080, 30 fps, MP4 H.264).

Uso:  python3 tools/video/build_video.py
Salida: video/senalval-presentacion.mp4
La animación es una página HTML que se captura fotograma a fotograma con Playwright y se
codifica con ffmpeg. Fotos y logos se cargan desde senalval.es.
"""
import pathlib, re, subprocess, json, shutil, os
ROOT = pathlib.Path(__file__).resolve().parents[2]
WORK = pathlib.Path(os.environ.get('VIDEO_WORK', '/tmp/senalval-video'))
OUT = ROOT / 'video'; OUT.mkdir(exist_ok=True)
U = 'https://senalval.es/wp-content/uploads/'
LOGO = U + '2025/09/SenalVal-05-e1770365341698.png'
FPS = 30

# Logos de clientes: los mismos de la web (senalval.es o embebidos), sin los que dependen de Wikimedia
html = (ROOT / 'index.html').read_text(encoding='utf-8')
logos = [(alt, src) for src, alt in re.findall(r'<li class="logo" data-srcs="([^"]*)"><img alt="([^"]+)"', html)
         if src.startswith('data:') or 'senalval.es' in src]

P = {
 'hero': U + '2026/02/ROTULO-PLAZA-DE-CASTILLA.jpg',
 'escorial': U + '2026/04/SAN-LORENZO-DE-EL-ESCORIAL-1536x1152.jpg',
 'madrid': U + '2026/04/AVENIDA-DE-EUROPA-1536x1152.jpg',
 'navalcarnero': U + '2026/04/NAVALCARNERO-1536x1152.jpg',
 'valdemoro': U + '2026/04/VALDEMORO.jpg',
 'residencia': U + '2025/02/FOTO-ICONO-PUERTA-INTERIOR-ENTRADA-768x1024.jpg',
 'oficinas': U + '2026/04/FOTO-2-1024x768.jpg',
 'bus': U + '2025/02/FOTO-TRASERA-790x1024.jpg',
 'azotea': U + '2025/09/ROTULO-AZOTEA-2-1024x768.jpg',
 'salamanca': U + '2025/02/FOTO-DIRECTORIO-GENERAL-768x1024.jpg',
 'exterior': U + '2023/05/FOTO-VALLA-INSTALADA-1024x768.jpg',
 'maragall': U + '2026/02/ROTULO-POETA-JOAN-MARAGALL-A-MEDIAS.jpg',
 'clece': U + '2023/10/SAN-PEDRO-POVEDA-1024x768.jpg',
}

# (inicio, fin) de cada escena en segundos
S = dict(intro=(0, 6), hero=(5.4, 13), ciclo=(12.4, 21), sectores=(20.4, 34), proyectos=(33.4, 48.5),
         claves=(47.9, 56.5), licit=(55.9, 64), clientes=(63.4, 71.5), cierre=(70.9, 78.5))
DURATION = 78.5

def photo(key, extra=''):
    return f'<div class="ph" data-kb="{extra}"><img src="{P[key]}"></div>'

sector_slides = [('residencia', 'Residencias y sociosanitario'), ('oficinas', 'Corporativo y oficinas'), ('bus', 'Transporte y flotas'), ('maragall', 'Justicia y administración')]
proj_slides = [('escorial', 'Tribunal de Instancia', 'San Lorenzo de El Escorial · Comunidad de Madrid'),
               ('navalcarnero', 'Tribunal de Instancia', 'Navalcarnero · Comunidad de Madrid'),
               ('azotea', 'Rótulo de azotea', 'San Sebastián'),
               ('salamanca', 'Directorios en aluminio composite', 'Salamanca'),
               ('clece', 'Señalética para residencias Clece', 'Castilla y León')]

def slides(items, scene, kind):
    a, b = S[scene]; n = len(items); d = (b - a) / n
    out = []
    for i, it in enumerate(items):
        s0, s1 = a + i * d, a + (i + 1) * d + 0.6
        if kind == 'sector':
            key, label = it
            out.append(f'<div class="slide" data-a="{s0:.2f}" data-b="{s1:.2f}">{photo(key)}<div class="shade"></div><div class="cap"><p class="k" data-in="0.3">Sector</p><h3 data-in="0.45">{label}</h3></div></div>')
        else:
            key, t, sub = it
            out.append(f'<div class="slide" data-a="{s0:.2f}" data-b="{s1:.2f}">{photo(key)}<div class="shade"></div><div class="cap"><p class="k" data-in="0.3">Proyecto SeñalVal</p><h3 data-in="0.45">{t}</h3><p class="sub" data-in="0.6">{sub}</p></div></div>')
    return '\n'.join(out)

logos_html = ''.join(f'<div class="lg" data-in="{0.5 + i * 0.07:.2f}"><img src="{src}" alt="{alt}"></div>' for i, (alt, src) in enumerate(logos))

page = f'''<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500&display=swap" rel="stylesheet">
<style>
:root {{ --blue:#0B5CAD; --sky:#6FA8DC; --night:#0D1526; }}
* {{ box-sizing: border-box; margin: 0; }}
html, body {{ width: 1920px; height: 1080px; overflow: hidden; background: var(--night); font-family: Montserrat, sans-serif; color: #fff; }}
.scene {{ position: absolute; inset: 0; opacity: 0; overflow: hidden; }}
.ph {{ position: absolute; inset: 0; overflow: hidden; }}
.ph img {{ width: 100%; height: 100%; object-fit: cover; transform-origin: 50% 50%; }}
.shade {{ position: absolute; inset: 0; background: linear-gradient(90deg, rgba(8,14,28,.92) 0%, rgba(13,21,38,.55) 45%, rgba(13,21,38,.15) 100%), linear-gradient(0deg, rgba(8,14,28,.7) 0%, transparent 40%); }}
.grid {{ position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.05) 1px, transparent 1px); background-size: 80px 80px; }}
.glow {{ position: absolute; width: 1400px; height: 1400px; right: -400px; top: -500px; border-radius: 50%; background: radial-gradient(circle, rgba(11,92,173,.55), transparent 65%); }}
.k {{ font-size: 22px; letter-spacing: .32em; text-transform: uppercase; color: var(--sky); display: flex; align-items: center; gap: 22px; }}
.k::before {{ content: ""; width: 70px; height: 2px; background: var(--sky); }}
h1, h2, h3 {{ font-weight: 300; letter-spacing: -.02em; }}
.wrap {{ position: absolute; left: 140px; right: 140px; top: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center; }}
/* intro */
.intro__logo {{ height: 150px; width: auto; filter: brightness(0) invert(1); }}
.intro .wrap {{ align-items: center; text-align: center; }}
.intro .line {{ width: 0; height: 2px; background: var(--sky); margin: 50px auto 40px; }}
.intro p {{ font-size: 34px; font-weight: 300; letter-spacing: .06em; color: rgba(255,255,255,.85); }}
/* hero */
.hero h1 {{ font-size: 104px; line-height: 1.06; max-width: 1300px; margin-top: 30px; }}
.hero h1 b {{ font-weight: 500; color: var(--sky); }}
.hero .sub {{ font-size: 32px; font-weight: 300; color: rgba(255,255,255,.82); margin-top: 40px; max-width: 1050px; line-height: 1.5; }}
/* ciclo */
.ciclo h2 {{ font-size: 76px; max-width: 1300px; margin: 28px 0 90px; line-height: 1.12; }}
.steps {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 28px; position: relative; }}
.steps .bar {{ position: absolute; top: 44px; left: 44px; height: 2px; background: rgba(255,255,255,.25); width: 0; }}
.step span {{ position: relative; display: grid; place-items: center; width: 88px; height: 88px; border-radius: 50%; background: var(--blue); font-size: 34px; font-weight: 400; margin-bottom: 30px; box-shadow: 0 0 0 10px var(--night); }}
.step h4 {{ font-size: 32px; font-weight: 400; }}
.step p {{ font-size: 21px; color: rgba(255,255,255,.7); margin-top: 10px; line-height: 1.5; }}
/* slides */
.slide {{ position: absolute; inset: 0; opacity: 0; }}
.cap {{ position: absolute; left: 140px; bottom: 150px; }}
.cap h3 {{ font-size: 86px; margin-top: 24px; max-width: 1300px; line-height: 1.08; }}
.cap .sub {{ font-size: 32px; font-weight: 300; color: rgba(255,255,255,.85); margin-top: 22px; }}
.tag {{ position: absolute; right: 140px; top: 110px; font-size: 22px; letter-spacing: .3em; text-transform: uppercase; color: rgba(255,255,255,.8); }}
/* claves */
.claves h2 {{ font-size: 76px; margin: 28px 0 80px; }}
.cards {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; }}
.c {{ padding: 50px 44px; border: 1px solid rgba(255,255,255,.16); border-radius: 26px; background: rgba(255,255,255,.04); }}
.c i {{ font-style: normal; font-size: 64px; font-weight: 200; color: var(--sky); }}
.c h4 {{ font-size: 40px; font-weight: 400; margin: 18px 0 16px; }}
.c p {{ font-size: 23px; color: rgba(255,255,255,.75); line-height: 1.5; }}
/* licitaciones */
.licit .wrap {{ display: grid; grid-template-columns: 1.05fr 1fr; gap: 100px; align-items: center; align-content: center; }}
.licit h2 {{ font-size: 84px; line-height: 1.08; margin-top: 28px; }}
.licit ul {{ list-style: none; padding: 0; display: grid; gap: 22px; }}
.licit li {{ display: flex; align-items: center; gap: 26px; padding: 28px 34px; border-radius: 20px; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.12); font-size: 30px; }}
.licit li::before {{ content: "✓"; flex: 0 0 48px; height: 48px; border-radius: 50%; background: var(--blue); display: grid; place-items: center; font-size: 24px; }}
/* clientes */
.clientes {{ background: #fff; color: #0B0F19; }}
.clientes .k {{ color: var(--blue); }} .clientes .k::before {{ background: var(--blue); }}
.clientes h2 {{ font-size: 72px; margin: 26px 0 70px; }}
.logos {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 34px 50px; align-items: center; }}
.lg {{ height: 120px; display: grid; place-items: center; }}
.lg img {{ max-height: 104px; max-width: 250px; object-fit: contain; mix-blend-mode: multiply; }}
/* cierre */
.cierre .wrap {{ align-items: flex-start; }}
.cierre img.logo {{ height: 120px; filter: brightness(0) invert(1); }}
.cierre h2 {{ font-size: 84px; line-height: 1.1; margin: 60px 0 70px; max-width: 1400px; }}
.cierre .ct {{ display: grid; grid-template-columns: repeat(4, auto); gap: 90px; padding-top: 44px; border-top: 1px solid rgba(255,255,255,.18); font-size: 32px; }}
.cierre .ct span {{ display: block; font-size: 18px; letter-spacing: .26em; text-transform: uppercase; color: var(--sky); margin-bottom: 12px; }}
[data-in] {{ opacity: 0; }}
</style></head><body>

<section class="scene intro" data-a="{S['intro'][0]}" data-b="{S['intro'][1]}"><div class="glow"></div><div class="grid"></div>
 <div class="wrap"><img class="intro__logo" data-in="0.4" src="{LOGO}" alt="SeñalVal"><div class="line" data-grow="1.2"></div><p data-in="1.7">Gestión integral de proyectos de señalización</p></div></section>

<section class="scene hero" data-a="{S['hero'][0]}" data-b="{S['hero'][1]}">{photo('hero')}<div class="shade" style="background:linear-gradient(90deg, rgba(8,14,28,.95) 0%, rgba(13,21,38,.8) 50%, rgba(13,21,38,.35) 100%), linear-gradient(0deg, rgba(8,14,28,.75) 0%, transparent 45%)"></div>
 <div class="wrap"><p class="k" data-in="0.5">Señalización · Señalética · Wayfinding</p>
 <h1 data-in="0.8">Gestionamos proyectos de señalización de <b>alta exigencia</b>.</h1>
 <p class="sub" data-in="1.6">Edificios públicos, sanitarios, educativos y corporativos que no admiten errores.</p></div></section>

<section class="scene ciclo" data-a="{S['ciclo'][0]}" data-b="{S['ciclo'][1]}"><div class="glow"></div><div class="grid"></div>
 <div class="wrap"><p class="k" data-in="0.4">El ciclo completo</p><h2 data-in="0.6">De la primera visita al mantenimiento, con un único responsable.</h2>
 <div class="steps"><div class="bar" data-bar="1.4"></div>
 <div class="step" data-in="1.4"><span>1</span><h4>Estudio</h4><p>Visita técnica y necesidades</p></div>
 <div class="step" data-in="1.9"><span>2</span><h4>Diseño</h4><p>Plan, planos y prototipos</p></div>
 <div class="step" data-in="2.4"><span>3</span><h4>Fabricación</h4><p>Control de calidad</p></div>
 <div class="step" data-in="2.9"><span>4</span><h4>Instalación</h4><p>Equipos propios, PRL y CAE</p></div>
 <div class="step" data-in="3.4"><span>5</span><h4>Mantenimiento</h4><p>Inventario y reposición</p></div>
 </div></div></section>

<section class="scene sectores" data-a="{S['sectores'][0]}" data-b="{S['sectores'][1]}">{slides(sector_slides, 'sectores', 'sector')}<p class="tag">Sectores</p></section>

<section class="scene proyectos" data-a="{S['proyectos'][0]}" data-b="{S['proyectos'][1]}">{slides(proj_slides, 'proyectos', 'proj')}<p class="tag">Proyectos reales</p></section>

<section class="scene claves" data-a="{S['claves'][0]}" data-b="{S['claves'][1]}"><div class="glow"></div><div class="grid"></div>
 <div class="wrap"><p class="k" data-in="0.4">De proveedor a socio</p><h2 data-in="0.6">No vendemos señales. Respondemos de un proyecto.</h2>
 <div class="cards">
 <div class="c" data-in="1.2"><i>01</i><h4>Solvencia</h4><p>Estructura técnica y documental para grandes proyectos.</p></div>
 <div class="c" data-in="1.6"><i>02</i><h4>Ejecución</h4><p>Instalación por fases en edificios en uso.</p></div>
 <div class="c" data-in="2.0"><i>03</i><h4>Trazabilidad</h4><p>Cada elemento inventariado: material, medidas, ubicación.</p></div>
 <div class="c" data-in="2.4"><i>04</i><h4>Continuidad</h4><p>Reposiciones con el mismo estándar, años después.</p></div>
 </div></div></section>

<section class="scene licit" data-a="{S['licit'][0]}" data-b="{S['licit'][1]}">{photo('madrid')}<div class="shade" style="background:rgba(8,14,28,.86)"></div>
 <div class="wrap"><div><p class="k" data-in="0.4">Licitaciones públicas</p><h2 data-in="0.6">Preparados para el pliego más exigente.</h2></div>
 <ul><li data-in="1.2">Memoria técnica y planificación</li><li data-in="1.6">Fichas técnicas de materiales</li><li data-in="2.0">Documentación PRL y CAE</li><li data-in="2.4">Garantías y plan de mantenimiento</li><li data-in="2.8">Inventario final de elementos</li></ul></div></section>

<section class="scene clientes" data-a="{S['clientes'][0]}" data-b="{S['clientes'][1]}">
 <div class="wrap"><p class="k" data-in="0.3">Clientes</p><h2 data-in="0.4">Han confiado en SeñalVal</h2><div class="logos">{logos_html}</div></div></section>

<section class="scene cierre" data-a="{S['cierre'][0]}" data-b="{S['cierre'][1]}"><div class="glow"></div><div class="grid"></div>
 <div class="wrap"><img class="logo" data-in="0.4" src="{LOGO}" alt="SeñalVal"><h2 data-in="0.8">¿Tiene un proyecto o una licitación de señalización? Hablemos.</h2>
 <div class="ct" data-in="1.5"><div><span>Teléfono · WhatsApp</span>665 863 597</div><div><span>Email</span>luismi.olea@senalval.es</div><div><span>Web</span>www.senalval.es</div><div><span>Oficina</span>Calle Oro 34 · Valladolid</div></div></div></section>

<script>
const ease = x => x <= 0 ? 0 : x >= 1 ? 1 : 1 - Math.pow(1 - x, 3);
const fade = (t, a, b, f = 0.6) => Math.min(ease((t - a) / f), ease((b - t) / f));
window.render = t => {{
  document.querySelectorAll('.scene').forEach(sc => {{
    const a = +sc.dataset.a, b = +sc.dataset.b, on = t >= a - .01 && t <= b + .01;
    sc.style.opacity = on ? fade(t, a, b) : 0; sc.style.visibility = on ? 'visible' : 'hidden';
    if (!on) return;
    const lt = t - a;
    sc.querySelectorAll(':scope > .ph img').forEach(im => {{ const p = (t - a) / (b - a); im.style.transform = `scale(${{1.14 - .12 * p}}) translateX(${{-1.5 + 3 * p}}%)`; }});
    sc.querySelectorAll('.slide').forEach(sl => {{
      const sa = +sl.dataset.a, sb = +sl.dataset.b, so = t >= sa && t <= sb;
      sl.style.opacity = so ? fade(t, sa, sb, 0.7) : 0;
      if (!so) return;
      const p = (t - sa) / (sb - sa);
      sl.querySelector('.ph img').style.transform = `scale(${{1.16 - .14 * p}}) translate(${{1.5 - 3 * p}}%, ${{-1 + 2 * p}}%)`;
      sl.querySelectorAll('[data-in]').forEach(el => {{ const q = ease((t - sa - +el.dataset.in) / 0.8); el.style.opacity = q; el.style.transform = `translateY(${{(1 - q) * 40}}px)`; }});
    }});
    sc.querySelectorAll('[data-in]').forEach(el => {{ if (el.closest('.slide')) return; const q = ease((lt - +el.dataset.in) / 0.9); el.style.opacity = q; el.style.transform = `translateY(${{(1 - q) * 46}}px)`; }});
    sc.querySelectorAll('[data-grow]').forEach(el => {{ el.style.width = (ease((lt - +el.dataset.grow) / 1) * 420) + 'px'; }});
    sc.querySelectorAll('[data-bar]').forEach(el => {{ el.style.width = (ease((lt - +el.dataset.bar) / 2.4) * 92) + '%'; }});
  }});
}};
</script></body></html>'''

WORK.mkdir(parents=True, exist_ok=True)
(WORK / 'video.html').write_text(page, encoding='utf-8')
if os.environ.get('PREVIEW'): raise SystemExit('html listo: ' + str(WORK / 'video.html'))
frames = WORK / 'frames'
if frames.exists(): shutil.rmtree(frames)
frames.mkdir()
js = r'''
const {chromium}=require('playwright');const [,,html,dir,dur,fps]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+html,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const bad=await p.$$eval('img',x=>x.filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src.slice(0,90)));
if(bad.length)console.log('IMAGENES SIN CARGAR',bad);
const n=Math.round(+dur*+fps);
for(let i=0;i<n;i++){await p.evaluate(t=>window.render(t),i/+fps);
  await p.screenshot({path:`${dir}/f${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});
  if(i%300===0)console.log('frame',i,'/',n);}
await b.close();})();'''
(WORK / 'render.js').write_text(js)
subprocess.run(['node', str(WORK / 'render.js'), str(WORK / 'video.html'), str(frames), str(DURATION), str(FPS)], check=True)
out = OUT / 'senalval-presentacion.mp4'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', str(frames / 'f%05d.jpg'),
                '-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out)], check=True)
print('->', out.relative_to(ROOT), round(out.stat().st_size / 1024 / 1024, 1), 'MB')
