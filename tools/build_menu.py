#!/usr/bin/env python3
"""Cabecera y pie globales de SeñalVal para insertar con WPCode en toda la web.

Salida (wordpress/menu/):
  wpcode-cabecera.html   Snippet HTML · ubicación «Site Wide Body» (justo después de <body>)
  wpcode-pie.html        Snippet HTML · ubicación «Site Wide Footer»
Y además wordpress/senalval-bloque-portada.html: la portada sin su menú propio (para no duplicarlo).

Todo el CSS va con prefijo .svh- / .svf- para no chocar con el tema Konte.
Uso: python3 tools/build_menu.py
"""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'wordpress' / 'menu'; OUT.mkdir(parents=True, exist_ok=True)
S = 'https://senalval.es/'
U = S + 'wp-content/uploads/'
LOGO = U + '2025/09/SenalVal-05-e1770365341698.png'
TEL, TEL_TXT, WA, MAIL = '+34665863597', '665 863 597', 'https://wa.me/34665863597?text=Hola%20Se%C3%B1alVal%2C%20quiero%20informaci%C3%B3n%20sobre%20un%20proyecto%20de%20se%C3%B1alizaci%C3%B3n.', 'luismi.olea@senalval.es'
G = U + '2026/11/'
GUIAS = [(G + 'guia-planificar-senalizacion-edificio-publico.pdf', 'Planificar la señalización de un edificio público', '1,6 MB'),
         (G + 'guia-senalizacion-accesible-criterios-normativa.pdf', 'Señalización accesible: criterios y normativa', '0,9 MB'),
         (G + 'guia-materiales-senalizacion.pdf', 'Materiales: qué elegir según uso y entorno', '1,1 MB')]

# ---------------- Contenido del menú ----------------
EMPRESA = [('senalval-empresa-de-senaletica', 'Quiénes somos', 'Empresa de señalética en Valladolid'),
           ('#socio', 'Por qué SeñalVal', 'De proveedor a socio'),
           ('#licitaciones', 'Licitaciones públicas', 'Documentación para el pliego'),
           ('portfolio', 'Portfolio', 'Trabajos realizados'),
           ('contactar', 'Contactar', 'Oficina y taller en Valladolid')]
SOL_TIPO = [('tipos-de-senaletica', 'Tipos de señalética'), ('category/senaletica-numeracion', 'Numeración y placas'),
            ('directorio-horario-senaletica', 'Directorios y horarios'), ('category/rotulos', 'Rótulos y letras corpóreas'),
            ('category/vinilos', 'Vinilos'), ('category/impresion-digital', 'Impresión digital'),
            ('category/senales-de-trafico', 'Señales de tráfico'), ('senal-vial-led', 'Señal vial LED'),
            ('category/senaletica-de-obligacion', 'Señalética de seguridad'), ('senaletica-especial', 'Señalética especial')]
SOL_MAT = [('senaletica-en-acero-inoxidable', 'Acero inoxidable'), ('senaletica-en-metacrilato', 'Metacrilato'),
           ('placas-en-material-cepillado', 'Material cepillado'), ('senaletica-en-vinilo', 'Vinilo'),
           ('senaletica-en-braile', 'Braille y altorrelieve'), ('senaletica-en-lamas-slatz', 'Lamas Slatz')]
SECTORES = [('category/senaletica-organismos-publicos', 'Organismos públicos', '⚖'),
            ('senaletica-y-senalizacion/letras-corporeas-tribunal-de-instancia', 'Sedes judiciales', '§'),
            ('senalizacion-hospitalaria', 'Hospitales y sanidad', '✚'),
            ('senalizacion-para-residencias-de-ancianos', 'Residencias', '⌂'),
            ('category/senaletica-colegios', 'Colegios', '✎'),
            ('category/senaletica-universidades', 'Universidades', '◎'),
            ('category/senaletica-en-centro-comercial', 'Centros comerciales', '◈'),
            ('top-10-tipos-de-senaletica-para-empresas', 'Empresas y oficinas', '▦')]
PROYECTOS = [('senaletica-y-senalizacion/letras-corporeas-tribunal-de-instancia', 'Sedes judiciales de Madrid', U + '2026/02/ROTULO-PLAZA-DE-CASTILLA-LEJOS.jpg'),
             ('senaletica-realizada-en-aluminio-composite-con-impresion-directa-para-un-cliente-de-salamanca', 'Directorios en Salamanca', U + '2025/02/FOTO-DIRECTORIO-GENERAL-768x1024.jpg'),
             ('unos-vinilos-instalados-en-una-residencia-de-clece-de-burgos', 'Residencia Clece · Burgos', U + '2025/02/FOTO-ICONO-PUERTA-INTERIOR-ENTRADA-768x1024.jpg'),
             ('senaletica-en-madrid-para-negocios-rotulos-vinilos-lonas-y-mas-senalval', 'Rotulación en San Sebastián', U + '2025/09/ROTULO-AZOTEA-2-1024x768.jpg'),
             ('unos-carteles-de-videovigilancia-realizados-en-aluminio-composite-para-la-fundacion-laboral-de-la-construccion', 'Fundación Laboral', U + '2025/02/FOTO-CARTEL-1-768x1024.jpg'),
             ('trabajos-de-rotulacion-y-vinilos-en-fachadas-autobuses-y-oficinas-senalval', 'Fachadas y autobuses', U + '2026/04/VINILOS-IMAGENES-ENTRADA-PRINCIPAL.jpg')]
ZONAS = [('soluciones-de-senaletica-en-madrid', 'Madrid'), ('senaletica-castilla-y-leon', 'Castilla y León'),
         ('senaletica-profesional-en-burgos', 'Burgos'), ('senaletica-zamora', 'Zamora'),
         ('senaletica-gallur-zaragoza', 'Zaragoza'), ('senaletica-profesional-en-espana', 'Toda España')]
RECURSOS = [('noticias-senalval', 'Blog y noticias'), ('category/que-es-senaletica-y-ejemplos', 'Qué es la señalética: ejemplos'),
            ('top-10-tipos-de-senaletica-para-empresas', 'Top 10 tipos de señalética'), ('#video', 'Vídeo de presentación')]

def url(path): return path if path.startswith('http') else S + path
I = {
 'phone': '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.6a1 1 0 0 1-.25 1L6.6 10.8Z" fill="currentColor"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.7"/>',
 'wa': '<path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2Zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 4.54 0 8.24 3.7 8.24 8.24 0 4.55-3.7 8.24-8.24 8.24Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.31-.02-.43-.06-.13-.56-1.35-.77-1.85-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28Z"/>',
 'dl': '<path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 19h14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
 'home': '<path d="M3 11.5 12 4l9 7.5M5.5 10v9.5h13V10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
 'grid': '<path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z" fill="none" stroke="currentColor" stroke-width="1.7"/>',
 'img': '<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m3 16 5-5 4 4 3-3 6 6" fill="none" stroke="currentColor" stroke-width="1.7"/>',
 'pin': '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="9.5" r="2.5" fill="none" stroke="currentColor" stroke-width="1.7"/>',
 'chev': '<path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.5"/>',
}
def ico(n, cls='svh-i', vb='0 0 24 24'): return f'<svg class="{cls}" viewBox="{vb}" aria-hidden="true">{I[n]}</svg>'
CHEV = ico('chev', 'svh-chev', '0 0 12 12')

def col(title, items, cls=''):
    return f'<div class="svh-col {cls}"><p class="svh-col__t">{title}</p>' + ''.join(f'<a href="{url(p)}">{t}</a>' for p, t in items) + '</div>'

panels = {
'Empresa': f'''<div class="svh-panel__grid svh-g-2">
  <div class="svh-col">{''.join(f'<a class="svh-rich" href="{url(p)}"><b>{t}</b><small>{d}</small></a>' for p, t, d in EMPRESA)}</div>
  <a class="svh-feature" href="{S}#video" style="--bg:url('{U}2026/02/ROTULO-PLAZA-DE-CASTILLA.jpg')"><span class="svh-feature__k">Vídeo · 1:18</span><b>SeñalVal en 1 minuto</b><small>Así trabajamos, de la primera visita al mantenimiento →</small></a>
</div>''',
'Soluciones': f'''<div class="svh-panel__grid svh-g-3">
  {col('Por tipo de señal', SOL_TIPO, 'svh-col--2')}
  {col('Por material', SOL_MAT)}
  <a class="svh-feature" href="{url(PROYECTOS[0][0])}" style="--bg:url('{U}2026/02/ROTULO-PLAZA-DE-CASTILLA.jpg')"><span class="svh-feature__k">Destacado</span><b>Letras corpóreas «Tribunal de Instancia»</b><small>Sedes judiciales de la Comunidad de Madrid →</small></a>
</div>''',
'Sectores': '<div class="svh-tiles">' + ''.join(f'<a class="svh-tile" href="{url(p)}"><span>{ic}</span><b>{t}</b></a>' for p, t, ic in SECTORES) + '</div>',
'Proyectos': '<div class="svh-thumbs">' + ''.join(f'<a class="svh-thumb" href="{url(p)}"><img src="{im}" alt="" loading="lazy"><b>{t}</b></a>' for p, t, im in PROYECTOS) + f'''</div>
<div class="svh-panel__foot"><a href="{S}#proyectos">Ver galerías en la portada</a><a href="{S}proyectos">Todos los proyectos</a><a href="{S}portfolio">Portfolio</a></div>''',
'Zonas': f'''<div class="svh-panel__grid svh-g-2">
  <div class="svh-zones">{''.join(f'<a href="{url(p)}">{ico("pin")}<b>{t}</b></a>' for p, t in ZONAS)}</div>
  <div class="svh-note"><b>Oficina y taller en Valladolid</b><p>Calle Oro 34, 1º F. Instalamos con equipos propios en toda España: sedes judiciales en Madrid, proyectos en Castilla y León, País Vasco y Aragón.</p><a href="{S}contactar">Cómo llegar →</a></div>
</div>''',
'Recursos': f'''<div class="svh-panel__grid svh-g-2">
  <div class="svh-guides"><p class="svh-col__t">Guías técnicas gratuitas (PDF)</p>{''.join(f'<a class="svh-guide" href="{u}" target="_blank" rel="noopener">{ico("dl")}<span><b>{t}</b><small>PDF · {s}</small></span></a>' for u, t, s in GUIAS)}</div>
  {col('Aprender y estar al día', RECURSOS)}
</div>''',
}

desktop_nav = ''.join(f'''<div class="svh-item"><button type="button" class="svh-top" aria-expanded="false">{n} {CHEV}</button><div class="svh-panel" role="region" aria-label="{n}"><div class="svh-wrap">{panels[n]}</div></div></div>''' for n in panels)

def mob_group(n, items):
    return f'<details class="svh-acc"><summary>{n}</summary>' + ''.join(f'<a href="{url(p)}">{t}</a>' for p, t in items) + '</details>'
mobile = ''.join([
  mob_group('Empresa', [(p, t) for p, t, d in EMPRESA]),
  mob_group('Soluciones', SOL_TIPO + SOL_MAT),
  mob_group('Sectores', [(p, t) for p, t, i in SECTORES]),
  mob_group('Proyectos', [(p, t) for p, t, i in PROYECTOS] + [('proyectos', 'Todos los proyectos')]),
  mob_group('Zonas', ZONAS),
  mob_group('Recursos', [(u, f'Guía: {t}') for u, t, s in GUIAS] + RECURSOS),
])

CSS = r'''
.svh, .svh *, .svf, .svf *, .svt, .svt * { box-sizing: border-box; }
.svh, .svf, .svt { --b:#0B5CAD; --bh:#094D92; --sky:#6FA8DC; --n:#0D1526; --ink:#0B0F19; --mu:#5B6475; --ln:#E3E8EF; --so:#F3F6FA; --e:cubic-bezier(.2,.7,.2,1);
  font-family: Montserrat, system-ui, -apple-system, "Segoe UI", sans-serif; -webkit-font-smoothing: antialiased; line-height: 1.5; }
.svh a, .svf a, .svt a { text-decoration: none; }
.svh-wrap { width: min(1240px, 100% - 32px); margin-inline: auto; }
/* Oculta la cabecera y el pie del tema Konte */
#masthead, .header-mobile, .hamburger-fullscreen, #colophon, .fullscreen-footer { display: none !important; }
html { scroll-padding-top: 96px; }
/* Barra superior */
.svh { position: sticky; top: 0; z-index: 9990; }
.admin-bar .svh { top: 32px; }
.svh-topbar { background: var(--n); color: rgba(255,255,255,.75); font-size: 12.5px; transition: margin .3s var(--e); }
.svh-topbar .svh-wrap { display: flex; align-items: center; justify-content: space-between; gap: 16px; height: 36px; }
.svh-topbar a { color: rgba(255,255,255,.85); display: inline-flex; align-items: center; gap: 6px; }
.svh-topbar a:hover { color: #fff; }
.svh-topbar__r { display: flex; gap: 22px; }
.svh-topbar .svh-i { width: 14px; height: 14px; }
.svh-topbar .svh-hl { color: var(--sky); font-weight: 500; }
.svh.is-scrolled .svh-topbar { margin-top: -36px; }
/* Barra principal */
.svh-bar { background: rgba(255,255,255,.97); backdrop-filter: blur(14px); border-bottom: 1px solid var(--ln); transition: box-shadow .3s; }
.svh.is-scrolled .svh-bar { box-shadow: 0 12px 30px -22px rgba(0,0,0,.45); }
.svh-bar > .svh-wrap { display: flex; align-items: center; gap: 26px; height: 74px; transition: height .3s var(--e); }
.svh.is-scrolled .svh-bar > .svh-wrap { height: 64px; }
.svh-logo { margin-right: auto; display: flex; align-items: center; }
.svh-logo img { height: 38px; width: auto; display: block; }
.svh-nav { display: flex; align-items: center; gap: 4px; height: 100%; }
.svh-item { height: 100%; display: flex; align-items: center; }
.svh-top { display: inline-flex; align-items: center; gap: 6px; height: 40px; padding: 0 12px; border: 0; border-radius: 999px; background: none; font: inherit; font-size: 14px; color: var(--ink); cursor: pointer; transition: background .2s, color .2s; }
.svh-chev { width: 11px; height: 11px; transition: transform .25s var(--e); }
.svh-item:hover .svh-top, .svh-item.is-open .svh-top { background: var(--so); color: var(--b); }
.svh-item:hover .svh-chev, .svh-item.is-open .svh-chev { transform: rotate(180deg); }
.svh-actions { display: flex; align-items: center; gap: 10px; }
.svh-btn { display: inline-flex; align-items: center; gap: 8px; height: 44px; padding: 0 20px; border-radius: 999px; background: var(--b); color: #fff !important; font-size: 14px; font-weight: 500; box-shadow: 0 12px 26px -14px rgba(11,92,173,.9); transition: background .25s, transform .25s var(--e); }
.svh-btn:hover { background: var(--bh); transform: translateY(-1px); }
.svh-round { display: grid; place-items: center; width: 44px; height: 44px; border-radius: 50%; border: 1px solid var(--ln); color: var(--ink); background: #fff; transition: border-color .2s, color .2s; }
.svh-round:hover { border-color: var(--b); color: var(--b); }
.svh-round .svh-i { width: 20px; height: 20px; }
.svh-round--wa .svh-i { color: #25D366; }
/* Paneles desplegables (mega menú) */
.svh-panel { position: absolute; left: 0; right: 0; top: 100%; background: #fff; border-top: 1px solid var(--ln); box-shadow: 0 40px 70px -40px rgba(13,21,38,.45); opacity: 0; visibility: hidden; transform: translateY(-6px); transition: opacity .22s var(--e), transform .22s var(--e), visibility 0s .22s; }
.svh-item:hover .svh-panel, .svh-item.is-open .svh-panel, .svh-item:focus-within .svh-panel { opacity: 1; visibility: visible; transform: none; transition: opacity .22s var(--e), transform .22s var(--e); }
.svh-panel .svh-wrap { padding: 28px 0 32px; }
.svh-panel__grid { display: grid; gap: 36px; }
.svh-g-2 { grid-template-columns: 1.3fr 1fr; } .svh-g-3 { grid-template-columns: 1.6fr 1fr 1.1fr; }
.svh-col { display: grid; align-content: start; gap: 2px; }
.svh-col--2 { grid-template-columns: 1fr 1fr; column-gap: 20px; }
.svh-col--2 .svh-col__t { grid-column: 1 / -1; }
.svh-col__t { margin: 0 0 8px; font-size: 11px; letter-spacing: .2em; text-transform: uppercase; color: var(--mu); }
.svh-col a, .svh-panel__foot a { padding: 8px 10px; margin-left: -10px; border-radius: 8px; color: var(--ink); font-size: 14.5px; transition: background .2s, color .2s; }
.svh-col a:hover { background: var(--so); color: var(--b); }
.svh-rich { display: grid; gap: 1px; }
.svh-rich b { font-weight: 500; } .svh-rich small { color: var(--mu); font-size: 12.5px; }
.svh-feature { position: relative; min-height: 200px; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; gap: 4px; padding: 22px; color: #fff !important; background: linear-gradient(0deg, rgba(13,21,38,.92), rgba(13,21,38,.2)), var(--bg) center/cover; transition: transform .3s var(--e); }
.svh-feature:hover { transform: translateY(-3px); }
.svh-feature__k { font-size: 11px; letter-spacing: .2em; text-transform: uppercase; color: var(--sky); }
.svh-feature b { font-size: 18px; font-weight: 400; line-height: 1.3; } .svh-feature small { color: rgba(255,255,255,.8); }
.svh-tiles { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.svh-tile { display: flex; align-items: center; gap: 14px; padding: 16px; border: 1px solid var(--ln); border-radius: 14px; color: var(--ink); transition: border-color .2s, box-shadow .2s, transform .2s var(--e); }
.svh-tile span { display: grid; place-items: center; flex: 0 0 42px; height: 42px; border-radius: 10px; background: var(--so); color: var(--b); font-size: 18px; }
.svh-tile b { font-weight: 500; font-size: 14.5px; }
.svh-tile:hover { border-color: var(--b); box-shadow: 0 16px 30px -22px rgba(13,21,38,.5); transform: translateY(-2px); }
.svh-tile:hover span { background: var(--b); color: #fff; }
.svh-thumbs { display: grid; grid-template-columns: repeat(6, 1fr); gap: 14px; }
.svh-thumb { display: grid; gap: 8px; color: var(--ink); }
.svh-thumb img { width: 100%; aspect-ratio: 4/3; object-fit: cover; border-radius: 10px; transition: transform .4s var(--e); }
.svh-thumb b { font-weight: 500; font-size: 13.5px; line-height: 1.3; }
.svh-thumb:hover b { color: var(--b); } .svh-thumb:hover img { transform: scale(1.03); }
.svh-panel__foot { display: flex; gap: 22px; margin-top: 18px; padding-top: 14px; border-top: 1px solid var(--ln); }
.svh-panel__foot a { color: var(--b); font-weight: 500; }
.svh-zones { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.svh-zones a { display: flex; align-items: center; gap: 10px; padding: 14px; border-radius: 12px; background: var(--so); color: var(--ink); transition: background .2s, color .2s; }
.svh-zones a:hover { background: var(--b); color: #fff; }
.svh-zones .svh-i { width: 20px; height: 20px; flex: 0 0 20px; }
.svh-zones b { font-weight: 500; font-size: 14.5px; }
.svh-note { padding: 22px; border-radius: 16px; background: var(--n); color: rgba(255,255,255,.8); font-size: 14px; }
.svh-note b { display: block; color: #fff; font-weight: 500; font-size: 16px; margin-bottom: 6px; }
.svh-note p { margin: 0 0 12px; } .svh-note a { color: var(--sky); font-weight: 500; }
.svh-guides { display: grid; gap: 8px; align-content: start; }
.svh-guide { display: flex; align-items: center; gap: 14px; padding: 12px 14px; border: 1px solid var(--ln); border-radius: 12px; color: var(--ink); transition: border-color .2s, background .2s; }
.svh-guide .svh-i { width: 34px; height: 34px; flex: 0 0 34px; padding: 7px; border-radius: 50%; background: var(--b); color: #fff; }
.svh-guide b { display: block; font-weight: 500; font-size: 14px; } .svh-guide small { color: var(--mu); font-size: 12px; }
.svh-guide:hover { border-color: var(--b); background: var(--so); }
/* Móvil */
.svh-burger { display: none; width: 44px; height: 44px; border: 0; background: none; cursor: pointer; padding: 10px; }
.svh-burger span { display: block; height: 2px; background: var(--ink); margin: 5px 0; transition: transform .3s, opacity .3s; }
.svh-drawer { position: fixed; inset: 0; z-index: 9995; visibility: hidden; }
.svh-drawer::before { content: ""; position: absolute; inset: 0; background: rgba(5,8,14,.55); opacity: 0; transition: opacity .3s; }
.svh-drawer__in { position: absolute; top: 0; right: 0; bottom: 0; width: min(420px, 88vw); background: #fff; transform: translateX(100%); transition: transform .35s var(--e); display: flex; flex-direction: column; }
.svh-drawer.is-open { visibility: visible; } .svh-drawer.is-open::before { opacity: 1; } .svh-drawer.is-open .svh-drawer__in { transform: none; }
.svh-drawer__head { display: flex; align-items: center; justify-content: space-between; padding: 14px 18px; border-bottom: 1px solid var(--ln); }
.svh-drawer__head img { height: 32px; width: auto; }
.svh-close { width: 42px; height: 42px; border: 0; border-radius: 50%; background: var(--so); font-size: 24px; line-height: 1; cursor: pointer; color: var(--ink); }
.svh-drawer__body { flex: 1; overflow-y: auto; padding: 6px 18px 20px; }
.svh-acc { border-bottom: 1px solid var(--ln); }
.svh-acc summary { list-style: none; cursor: pointer; padding: 16px 2px; font-weight: 500; font-size: 16px; color: var(--ink); display: flex; justify-content: space-between; }
.svh-acc summary::-webkit-details-marker { display: none; }
.svh-acc summary::after { content: "+"; font-weight: 300; font-size: 22px; line-height: 1; color: var(--b); }
.svh-acc[open] summary::after { content: "−"; }
.svh-acc a { display: block; padding: 10px 2px 10px 14px; color: var(--mu); font-size: 15px; }
.svh-acc a:hover { color: var(--b); }
.svh-drawer__foot { display: grid; gap: 10px; padding: 16px 18px calc(16px + env(safe-area-inset-bottom)); border-top: 1px solid var(--ln); }
.svh-drawer__foot .svh-btn { justify-content: center; }
.svh-drawer__foot .svh-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.svh-ghost { display: inline-flex; align-items: center; justify-content: center; gap: 8px; height: 44px; border-radius: 999px; border: 1px solid var(--ln); color: var(--ink) !important; font-size: 14px; }
.svh-ghost .svh-i { width: 18px; height: 18px; } .svh-ghost--wa .svh-i { color: #25D366; }
html.svh-lock { overflow: hidden; }
@media (max-width: 1180px) { .svh-top { padding: 0 9px; font-size: 13.5px; } .svh-bar > .svh-wrap { gap: 14px; } }
@media (max-width: 1080px) {
  .svh-nav, .svh-actions .svh-btn, .svh-topbar__l { display: none; }
  .svh-burger { display: block; }
  .svh-topbar__r { width: 100%; justify-content: space-between; gap: 10px; }
  .svh-topbar__r .svh-mail { display: none; }
  .svh-bar > .svh-wrap { height: 64px; }
  .svh-logo img { height: 32px; }
}
/* Pie */
.svf { background: #0A1120; color: rgba(255,255,255,.66); font-size: 14.5px; }
.svf-cta { background: linear-gradient(120deg, #0B3F7A 0%, var(--n) 70%); }
.svf-cta .svh-wrap { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 20px; padding: 42px 0; }
.svf-cta p { margin: 0; color: #fff; font-size: clamp(20px, 2.4vw, 28px); font-weight: 300; max-width: 30ch; line-height: 1.3; }
.svf-cta div { display: flex; flex-wrap: wrap; gap: 12px; }
.svf-ghost { display: inline-flex; align-items: center; gap: 8px; height: 44px; padding: 0 20px; border-radius: 999px; border: 1px solid rgba(255,255,255,.4); color: #fff !important; font-size: 14px; }
.svf-ghost .svh-i { width: 18px; height: 18px; color: #25D366; }
.svf-main { display: grid; grid-template-columns: 1.3fr repeat(5, 1fr); gap: 34px; padding: 56px 0 40px; }
.svf-brand img { height: 34px; width: auto; filter: brightness(0) invert(1); margin-bottom: 16px; }
.svf-brand p { margin: 0 0 14px; }
.svf address { font-style: normal; line-height: 1.9; }
.svf a { color: rgba(255,255,255,.72); }
.svf a:hover { color: var(--sky); }
.svf-col { display: grid; align-content: start; gap: 9px; }
.svf-col p { margin: 0 0 8px; color: #fff; font-size: 12px; letter-spacing: .16em; text-transform: uppercase; }
.svf-bottom { border-top: 1px solid rgba(255,255,255,.08); }
.svf-bottom .svh-wrap { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 10px; padding: 20px 0; font-size: 13px; }
@media (max-width: 1080px) { .svf-main { grid-template-columns: 1fr 1fr; } .svf-brand { grid-column: 1 / -1; } }
@media (max-width: 560px) { .svf-main { grid-template-columns: 1fr; } }
/* Barra inferior en el móvil */
.svt { display: none; }
@media (max-width: 1080px) {
  .svt { position: fixed; left: 0; right: 0; bottom: 0; z-index: 9980; display: grid; grid-template-columns: repeat(5, 1fr); background: rgba(255,255,255,.97); backdrop-filter: blur(12px); border-top: 1px solid var(--ln); padding: 6px 4px calc(6px + env(safe-area-inset-bottom)); }
  .svt a, .svt button { display: grid; justify-items: center; gap: 3px; padding: 4px 0; border: 0; background: none; font: inherit; font-size: 11px; color: var(--ink); cursor: pointer; }
  .svt .svh-i { width: 22px; height: 22px; }
  .svt .svt-wa .svh-i { color: #25D366; }
  body { padding-bottom: 64px; }
}
'''

header = f'''<!-- SeñalVal · Cabecera global (WPCode · Site Wide Body) -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
<header class="svh" id="svh">
  <div class="svh-topbar"><div class="svh-wrap">
    <span class="svh-topbar__l">Señalización de alta exigencia · Proyectos en toda España</span>
    <div class="svh-topbar__r">
      <a href="tel:{TEL}">{ico('phone')}{TEL_TXT}</a>
      <a href="{WA}" target="_blank" rel="noopener">{ico('wa')}WhatsApp</a>
      <a class="svh-mail" href="mailto:{MAIL}">{ico('mail')}{MAIL}</a>
      <a class="svh-hl" href="{S}#recursos">{ico('dl')}Guías técnicas gratis</a>
    </div>
  </div></div>
  <div class="svh-bar"><div class="svh-wrap">
    <a class="svh-logo" href="{S}" aria-label="SeñalVal, inicio"><img src="{LOGO}" alt="SeñalVal" width="260" height="39"></a>
    <nav class="svh-nav" aria-label="Menú principal">{desktop_nav}</nav>
    <div class="svh-actions">
      <a class="svh-round svh-round--wa" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ico('wa')}</a>
      <a class="svh-btn" href="{S}#contacto">Pedir presupuesto</a>
      <button type="button" class="svh-burger" aria-label="Abrir menú" aria-controls="svh-drawer" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div></div>
</header>
<div class="svh svh-drawer" id="svh-drawer" aria-hidden="true">
  <div class="svh-drawer__in" role="dialog" aria-label="Menú">
    <div class="svh-drawer__head"><img src="{LOGO}" alt="SeñalVal"><button type="button" class="svh-close" aria-label="Cerrar menú">×</button></div>
    <div class="svh-drawer__body"><a class="svh-acc-home" href="{S}" style="display:block;padding:16px 2px;border-bottom:1px solid var(--ln);font-weight:500;color:var(--ink)">Inicio</a>{mobile}</div>
    <div class="svh-drawer__foot">
      <a class="svh-btn" href="{S}#contacto">Pedir presupuesto</a>
      <div class="svh-row"><a class="svh-ghost" href="tel:{TEL}">{ico('phone')}Llamar</a><a class="svh-ghost svh-ghost--wa" href="{WA}" target="_blank" rel="noopener">{ico('wa')}WhatsApp</a></div>
    </div>
  </div>
</div>
<script>
(function () {{
  var h = document.getElementById('svh'), d = document.getElementById('svh-drawer');
  if (!h || !d) return;
  // Sube la cabecera al principio del <body> por si el tema la coloca dentro de otro contenedor
  if (document.body.firstElementChild !== h) {{ document.body.insertBefore(d, document.body.firstChild); document.body.insertBefore(h, document.body.firstChild); }}
  var onS = function () {{ h.classList.toggle('is-scrolled', window.scrollY > 40); }};
  onS(); window.addEventListener('scroll', onS, {{ passive: true }});
  // Desplegables: ratón (CSS) + clic/teclado
  var items = h.querySelectorAll('.svh-item');
  items.forEach(function (it) {{
    var b = it.querySelector('.svh-top');
    b.addEventListener('click', function (e) {{
      var open = !it.classList.contains('is-open');
      items.forEach(function (o) {{ o.classList.remove('is-open'); o.querySelector('.svh-top').setAttribute('aria-expanded', 'false'); }});
      if (open) {{ it.classList.add('is-open'); b.setAttribute('aria-expanded', 'true'); }}
    }});
    it.addEventListener('mouseleave', function () {{ it.classList.remove('is-open'); b.setAttribute('aria-expanded', 'false'); }});
  }});
  document.addEventListener('click', function (e) {{ if (!h.contains(e.target)) items.forEach(function (o) {{ o.classList.remove('is-open'); }}); }});
  // Menú lateral (móvil)
  var burger = h.querySelector('.svh-burger');
  var setD = function (open) {{ d.classList.toggle('is-open', open); d.setAttribute('aria-hidden', String(!open)); burger.setAttribute('aria-expanded', String(open)); document.documentElement.classList.toggle('svh-lock', open); }};
  burger.addEventListener('click', function () {{ setD(true); }});
  d.querySelector('.svh-close').addEventListener('click', function () {{ setD(false); }});
  d.addEventListener('click', function (e) {{ if (e.target === d) setD(false); if (e.target.closest('a')) setD(false); }});
  document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape') {{ setD(false); items.forEach(function (o) {{ o.classList.remove('is-open'); }}); }} }});
  window.svhOpenMenu = function () {{ setD(true); }};
}})();
</script>
'''

def fcol(title, items): return f'<nav class="svf-col" aria-label="{title}"><p>{title}</p>' + ''.join(f'<a href="{url(p)}">{t}</a>' for p, t in items) + '</nav>'
footer = f'''<!-- SeñalVal · Pie global (WPCode · Site Wide Footer) -->
<footer class="svf" id="svf">
  <div class="svf-cta"><div class="svh-wrap">
    <p>¿Tiene un proyecto o una licitación de señalización?</p>
    <div><a class="svh-btn" href="{S}#contacto">Solicitar estudio del proyecto</a><a class="svf-ghost" href="{WA}" target="_blank" rel="noopener">{ico('wa')}WhatsApp {TEL_TXT}</a></div>
  </div></div>
  <div class="svh-wrap svf-main">
    <div class="svf-brand">
      <a href="{S}" aria-label="SeñalVal, inicio"><img src="{LOGO}" alt="SeñalVal" width="220" height="33" loading="lazy"></a>
      <p>Gestión integral de proyectos de señalización y señalética de alta exigencia.</p>
      <address>Calle Oro 34, 1º F (Valladolid)<br><a href="tel:{TEL}">{TEL_TXT}</a> · <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><br><a href="mailto:{MAIL}">{MAIL}</a><br><a href="{S}">www.senalval.es</a></address>
    </div>
    {fcol('Soluciones', SOL_TIPO[:6] + [('senaletica-especial', 'Señalética especial')])}
    {fcol('Materiales', SOL_MAT)}
    {fcol('Sectores', [(p, t) for p, t, i in SECTORES])}
    {fcol('Zonas', ZONAS)}
    {fcol('Empresa', [('senalval-empresa-de-senaletica', 'Quiénes somos'), ('proyectos', 'Proyectos'), ('portfolio', 'Portfolio'), ('noticias-senalval', 'Blog'), (S + '#recursos', 'Guías técnicas (PDF)'), ('contactar', 'Contactar')])}
  </div>
  <div class="svf-bottom"><div class="svh-wrap">
    <span>© <span class="svf-y">2026</span> SeñalVal. Todos los derechos reservados.</span>
    <span><a href="{S}aviso-legal">Aviso legal</a> · <a href="{S}politica-de-privacidad">Privacidad</a> · <a href="{S}politica-de-cookies-2">Cookies</a></span>
  </div></div>
</footer>
<nav class="svt" aria-label="Accesos rápidos">
  <a href="{S}">{ico('home')}<span>Inicio</span></a>
  <button type="button" onclick="window.svhOpenMenu && window.svhOpenMenu()">{ico('grid')}<span>Menú</span></button>
  <a href="{S}#proyectos">{ico('img')}<span>Proyectos</span></a>
  <a href="tel:{TEL}">{ico('phone')}<span>Llamar</span></a>
  <a class="svt-wa" href="{WA}" target="_blank" rel="noopener">{ico('wa')}<span>WhatsApp</span></a>
</nav>
<script>(function(){{var y=document.querySelector('.svf-y');if(y)y.textContent=new Date().getFullYear();}})();</script>
'''
(OUT / 'wpcode-cabecera.html').write_text(header, encoding='utf-8')
(OUT / 'wpcode-pie.html').write_text(footer, encoding='utf-8')
combo = '<!-- SeñalVal · Menú completo (cabecera + pie). WPCode: HTML Snippet · Auto Insert · Site Wide Footer.\n     La cabecera se coloca sola arriba de la página. -->\n' + header + '\n' + footer
(OUT / 'wpcode-menu-completo.html').write_text(combo, encoding='utf-8')
assert '<?' not in combo
(OUT / 'wpcode-menu-php.txt').write_text('''/*
 * SeñalVal · Menú global (cabecera + pie)
 * WPCode: tipo «PHP Snippet» · Insertion: Auto Insert · Location: Run Everywhere.
 * Pega TODO este texto tal cual. No añadas «<?php» al principio: WPCode lo pone solo.
 */
add_action( 'wp_footer', function () {
?>
''' + combo + '''
<?php
}, 5 );
''', encoding='utf-8')

# ---- Portada sin su menú propio (la cabecera y el pie globales los sustituyen) ----
blk = (ROOT / 'wordpress' / 'senalval-bloque.html').read_text(encoding='utf-8')
for a, b in [(r'\s*<a class="skip".*?</a>', ''), (r'\s*<!-- =+ CABECERA =+ -->\s*<header class="nav".*?</header>', ''),
             (r'\s*<!-- =+ PIE =+ -->\s*<footer class="footer">.*?</footer>', ''), (r'\s*<nav class="tabbar".*?</nav>', ''),
             (r'\s*<a href="https://wa\.me/[^"]*" class="float-cta".*?</a>', '')]:
    blk, n = re.subn(a, b, blk, count=1, flags=re.S)
    assert n == 1, a
blk = blk.replace('</style>', '''
/* Portada con la cabecera global de SeñalVal (WPCode) */
.hero { padding-top: 24px; min-height: calc(100svh - 118px); }
@media (max-width: 1080px) { .hero { min-height: calc(100svh - 100px); } }
</style>''', 1)
(ROOT / 'wordpress' / 'senalval-bloque-portada.html').write_text(blk, encoding='utf-8')
for f in ('menu/wpcode-cabecera.html', 'menu/wpcode-pie.html', 'senalval-bloque-portada.html'):
    print(f, round((ROOT / 'wordpress' / f).stat().st_size / 1024), 'KB')
