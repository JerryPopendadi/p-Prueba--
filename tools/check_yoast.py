#!/usr/bin/env python3
"""Aproximación local a tres comprobaciones de legibilidad de Yoast SEO (español):
- Palabras de transición: % de frases que contienen alguna (Yoast pide ≥ 30 %).
- Frases consecutivas: 3 o más frases seguidas que empiezan por la misma palabra.
- Distribución de subtítulos: bloques de más de 300 palabras sin un H2–H6.

Uso: python3 tools/check_yoast.py [archivo.html]
"""
import re, sys, html as H
from html.parser import HTMLParser

TRANSICION = ['además', 'también', 'asimismo', 'así', 'así como', 'así que', 'por eso', 'por ello', 'por tanto', 'por lo tanto',
  'por consiguiente', 'en consecuencia', 'sin embargo', 'no obstante', 'en cambio', 'aunque', 'porque', 'ya que', 'puesto que',
  'pues', 'dado que', 'debido a', 'gracias a', 'por ejemplo', 'es decir', 'o sea', 'en primer lugar', 'en segundo lugar',
  'primero', 'después', 'luego', 'antes', 'finalmente', 'por último', 'al final', 'mientras', 'mientras que', 'incluso',
  'de hecho', 'en realidad', 'sobre todo', 'en especial', 'especialmente', 'en definitiva', 'en resumen', 'en conclusión',
  'a continuación', 'desde', 'hasta', 'cuando', 'para que', 'de modo que', 'de manera que', 'en cuanto', 'a la vez', 'al mismo tiempo',
  'igualmente', 'del mismo modo', 'en otras palabras', 'en concreto', 'concretamente', 'en particular', 'a su vez', 'además de']

class P(HTMLParser):
    BLOCK = {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'dd', 'dt', 'summary', 'figcaption', 'blockquote', 'td', 'th', 'div', 'a', 'span', 'button', 'small', 'b', 'label', 'option'}
    def __init__(s):
        super().__init__(); s.out = []; s.skip = 0
    def handle_starttag(s, tag, a):
        if tag in ('script', 'style', 'svg', 'select'): s.skip += 1
        if tag in ('h2', 'h3', 'h4', 'h5', 'h6'): s.out.append(('H', ''))
    def handle_endtag(s, tag):
        if tag in ('script', 'style', 'svg', 'select'): s.skip -= 1
    def handle_data(s, d):
        if not s.skip and d.strip(): s.out.append(('T', d))

src = open(sys.argv[1] if len(sys.argv) > 1 else 'index.html', encoding='utf-8').read()
body = re.search(r'<body[^>]*>(.*)</body>', src, re.S)
body = body.group(1) if body else src
p = P(); p.feed(body)

# Texto corrido (como lo ve el editor de WordPress) y bloques entre subtítulos
text = ''; blocks = [0]
for kind, d in p.out:
    if kind == 'H': blocks.append(0); continue
    d = re.sub(r'\s+', ' ', H.unescape(d)).strip()
    text += ' ' + d
    blocks[-1] += len(re.findall(r'\w+', d))
sents = [x.strip() for x in re.split(r'(?<=[.!?…])\s+', text) if len(re.findall(r'\w+', x)) >= 1]
low = lambda x: ' ' + re.sub(r'[^\wáéíóúñü ]', ' ', x.lower()) + ' '
with_t = [x for x in sents if any(f' {w} ' in low(x) for w in TRANSICION)]
pct = 100 * len(with_t) / max(1, len(sents))
first = [re.findall(r'\w+', x.lower())[0] if re.findall(r'\w+', x) else '' for x in sents]
runs = []; i = 0
while i < len(first):
    j = i
    while j + 1 < len(first) and first[j + 1] == first[i] and first[i]: j += 1
    if j - i + 1 >= 3: runs.append((first[i], j - i + 1, sents[i][:60]))
    i = j + 1
print(f'Frases: {len(sents)} · con palabras de transición: {len(with_t)} ({pct:.1f} %) {"OK" if pct >= 30 else "BAJO"}')
print(f'Series de 3+ frases con el mismo inicio: {len(runs)}')
for r in runs: print('   ', r)
print(f'Palabras antes del primer subtítulo: {blocks[0]} {"OK" if blocks[0] <= 300 else "DEMASIADAS"} · bloque más largo: {max(blocks)}')
