"""Descriptions of every product (by parent SKU) in the 9 site languages, for the shop page."""
import csv, io, json, sys, contextlib, re
sys.path.insert(0, '/home/user/p-Prueba--/thefaces/src')
sys.path.insert(0, '/home/user/p-Prueba--/thefaces/woocommerce')
with contextlib.redirect_stdout(io.StringIO()):
    import build
    import improve_csv as ic
LANGS = build.LANGS  # en, ru, es, de, th, id, ja, fr, uk
rows = [r for r in csv.DictReader(open(ic.OUT, encoding='utf-8')) if r['Type'] == 'variable']
out, missing = {}, []
for r in rows:
    m = ic.BY_NAME.get(ic.norm(r['Name'])) or next((x for x in ic.MENU if x[2].replace(' · ', ' ') == r['Name']), None)
    if not m:
        missing.append(r['Name']); continue
    mid = ic.ALIAS.get(m[1], m[1])
    d = {}
    if m[1] in ic.ELEM or mid in ic.ELEM:
        e = ic.ELEM.get(m[1]) or ic.ELEM[mid]
        for i, l in enumerate(LANGS):
            inc = e['inc'][i] if isinstance(e['inc'][i], str) else ' · '.join(e['inc'][i])
            d[l] = '%s. %s %s' % (e['t'][i].rstrip('.'), e['when'][i] if e.get('when') else '', inc)
    elif mid in build.DESC and mid not in ic.SKIP and m[1] not in ic.EXTRA_DESC:
        for i, l in enumerate(LANGS):
            d[l] = build.DESC[mid][i]
    else:
        d['en'] = ic.lead(m[1], r['Short description'])
    out[r['SKU']] = {k: re.sub(r'\s+', ' ', v).strip() for k, v in d.items()}
from shop_i18n_extra import X
for k, v in X.items():
    if k in out:
        out[k] = dict(zip(LANGS, v))
json.dump({'langs': LANGS, 'desc': out}, open('/home/user/p-Prueba--/thefaces/wordpress-plugin/thefaces-shop/assets/i18n.json', 'w'), ensure_ascii=False)
full = sum(1 for v in out.values() if len(v) == len(LANGS))
print(LANGS, len(out), 'products,', full, 'in all languages; missing:', missing)
print([k for k, v in out.items() if len(v) < len(LANGS)])
