# -*- coding: utf-8 -*-
"""Une textos base, preguntas frecuentes y mejoras SEO en la versión final de cada entrada."""
import copy, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from posts_1 import POSTS as P1
from posts_2 import POSTS as P2
from posts_3 import POSTS as P3
from faqs import FAQS
from extras import EXTRAS

FAQ_TITLE = {'que-es-wayfinding': 'Preguntas frecuentes sobre el wayfinding',
             'precio-proyecto-senaletica-edificio': 'Preguntas frecuentes sobre el precio de la señalética'}

def compose():
    out = []
    for base in P1 + P2 + P3:
        p = copy.deepcopy(base); ex = EXTRAS[p['slug']]; old = p['slug']
        for k in ('focus', 'seo_title', 'metadesc', 'img2_alt', 'slug', 'title'):
            if k in ex: p[k] = ex[k]
        body = ex['intro'].strip() + '\n\n' + p['body'].strip()
        i = body.find('[[IMG2]]')
        body = body[:i] + ex['section'].strip() + '\n\n' + body[i:]
        faq = '\n## ' + FAQ_TITLE.get(old, ex['faq_title']) + '\n' + '\n'.join(f'### {a}\n{b}' for a, b in FAQS[old]) + '\n'
        j = body.rfind('\n> ')
        p['body'] = body[:j] + '\n' + faq + body[j:] + '\n'
        p['old_slug'] = old
        out.append(p)
    # Si alguna entrada cambió de slug, actualizar los enlaces internos que apuntan a ella
    ren = {p['old_slug']: p['slug'] for p in out if p['old_slug'] != p['slug']}
    for p in out:
        for a, b in ren.items(): p['body'] = p['body'].replace(f'](/{a})', f'](/{b})')
    return out
