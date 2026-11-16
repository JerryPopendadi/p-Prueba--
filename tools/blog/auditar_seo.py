#!/usr/bin/env python3
"""Auditoría SEO de las entradas, con los criterios de Yoast SEO (análisis SEO y de legibilidad).

Uso: python3 tools/blog/auditar_seo.py [--detalle]
"""
import re, sys, unicodedata, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from compose import compose

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')
def plain(md):
    md = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', md)
    md = re.sub(r'\*\*|^#+ |^> |^- ', '', md, flags=re.M)
    return md.replace('[[IMG2]]', '')

TRANS = ['además', 'también', 'asimismo', 'así', 'por eso', 'por ello', 'por tanto', 'por lo tanto', 'en consecuencia', 'sin embargo',
 'no obstante', 'en cambio', 'aunque', 'porque', 'ya que', 'puesto que', 'pues', 'dado que', 'por ejemplo', 'es decir', 'o sea',
 'primero', 'después', 'luego', 'antes', 'finalmente', 'por último', 'mientras', 'incluso', 'de hecho', 'en realidad', 'sobre todo',
 'especialmente', 'en definitiva', 'en resumen', 'a continuación', 'cuando', 'para que', 'de modo que', 'de manera que', 'a la vez',
 'al mismo tiempo', 'igualmente', 'del mismo modo', 'en concreto', 'concretamente', 'en particular', 'a su vez', 'además de', 'por otra parte',
 'por un lado', 'por otro lado', 'en primer lugar', 'en segundo lugar', 'por consiguiente', 'en cualquier caso', 'en general', 'normalmente',
  'aun así', 'por supuesto', 'en ese caso', 'en estos casos', 'en este caso', 'por lo general', 'de este modo', 'de esta forma']

STOP = {'de', 'la', 'el', 'los', 'las', 'en', 'para', 'y', 'del', 'a', 'un', 'una', 'que', 'qué', 'es', 'que', 'con', 'por'}
def kwwords(kw): return [w for w in re.findall(r'\w+', norm(kw)) if w not in {norm(x) for x in STOP}]
def has(kw, text):
    t = norm(text); return all(re.search(r'\b' + re.escape(w), t) for w in kwwords(kw))

def audit(p):
    md = p['body']; kw = norm(p['focus']); txt = plain(md)
    paras = [plain(l) for l in md.splitlines() if l.strip() and not l.startswith(('#', '- ', '[[', '> '))]
    first = norm(paras[0]) if paras else ''
    h2 = [norm(plain(l)) for l in md.splitlines() if l.startswith('## ')]
    words = re.findall(r'\w+', txt); n = len(words)
    occ = sum(1 for s_ in re.split(r'(?<=[.!?])\s+|\n+', txt) if has(kw, s_))
    sents = [s for s in re.split(r'(?<=[.!?:])\s+|\n+', txt) if len(re.findall(r'\w+', s)) > 3]
    longs = sum(1 for s in sents if len(re.findall(r'\w+', s)) > 20)
    trans = sum(1 for s in sents if any(re.search(r'\b' + re.escape(t) + r'\b', s.lower()) for t in TRANS))
    ext = len(re.findall(r'\]\(https?://(?!senalval\.es)', md))
    inner = len(re.findall(r'\]\(/', md))
    alt = p['img2_alt']
    blocks = re.split(r'\n## ', md); maxblock = max(len(re.findall(r'\w+', plain(b))) for b in blocks)
    slugkw = all(w.replace('ñ', 'n') in p['slug'] for w in kwwords(kw))
    checks = {
     'kw en título SEO': has(kw, p['seo_title']),
     'kw al inicio del título': norm(p['seo_title']).startswith(kw.split()[0]),
     'kw en descripción': has(kw, p['metadesc']),
     'kw en URL': slugkw,
     'kw en 1er párrafo': has(kw, first),
     'kw en un H2': any(has(kw, h) for h in h2),
     'kw en alt de imagen': has(kw, alt),
     f'densidad 0,5-3 % ({occ}×)': 0.5 <= 100 * occ / max(n, 1) <= 3,
     f'≥ 300 palabras, mínimo de Yoast ({n})': n >= 300,
     f'enlaces externos ({ext})': ext >= 1,
     f'enlaces internos ({inner})': inner >= 3,
     f'frases > 20 palabras ≤ 25 % ({100*longs//max(len(sents),1)} %)': longs / max(len(sents), 1) <= .25,
     f'palabras de transición ≥ 30 % ({100*trans//max(len(sents),1)} %)': trans / max(len(sents), 1) >= .30,
     f'≤ 300 palabras entre subtítulos ({maxblock})': maxblock <= 300,
     'descripción 120-156 car.': 120 <= len(p['metadesc']) <= 156,
     'título SEO ≤ 60 car.': len(p['seo_title']) <= 60,
    }
    return checks

if __name__ == '__main__':
    posts = compose(); tot = {}
    kws = [norm(p['focus']) for p in posts]
    dup = {k for k in kws if kws.count(k) > 1}
    for p in posts:
        c = audit(p); fails = [k for k, v in c.items() if not v]
        for k in c: tot.setdefault(re.sub(r' \(.*\)| \d.*', '', k), [0, 0]); tot[re.sub(r' \(.*\)| \d.*', '', k)][0 if c[k] else 1] += 1
        if '--detalle' in sys.argv and fails: print(f'{p["slug"][:45]:45} ✗ ' + ' · '.join(fails))
    print(f'\n{len(posts)} entradas · palabras clave repetidas: {sorted(dup) or "ninguna"}')
    for k, (ok, ko) in tot.items(): print(f'  {"✓" if not ko else "✗"} {k}: {ok}/{ok+ko}')
