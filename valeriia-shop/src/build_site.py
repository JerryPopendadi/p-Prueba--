# Genera ../index.html desde template.html + i18n.py  (python3 build_site.py)
import re, json, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from i18n import T
CODES = ['ru','en','uk','fr','de']
tpl = open(os.path.join(here,'template.html'), encoding='utf-8').read()
def spans(k):
    v = T[k]; return ''.join(f'<span data-{c}>{v[i]}</span>' for i,c in enumerate(CODES))
def by_lang(k): return json.dumps({c:T[k][i] for i,c in enumerate(CODES)}, ensure_ascii=False)
langs = ''.join(f'<button data-l="{c}">{"UA" if c=="uk" else c.upper()}</button>' for c in ['en','ru','uk','fr','de'])
mq = ''.join(f'<div class="it">{spans(k)}<i></i></div>' for k in ['mq1','mq2','mq3','mq4','mq5','t_instant','t_lang']) * 2
out = (tpl.replace('__LANGS__', langs).replace('__MQ__', mq)
          .replace('__N_RECIPES__', by_lang('r_title')).replace('__N_BELLY__', by_lang('b_title')).replace('__N_BUNDLE__', by_lang('bu_title'))
          .replace('__COPY__', by_lang('cm_copy')))
missing = set()
def rep(m):
    k = m.group(1)
    if k not in T: missing.add(k); return m.group(0)
    return spans(k)
out = re.sub(r'\{\{(\w+)\}\}', rep, out)
if missing: sys.exit('missing keys: %s' % missing)
open(os.path.join(here,'..','index.html'),'w',encoding='utf-8').write(out)
print('index.html', len(out))
