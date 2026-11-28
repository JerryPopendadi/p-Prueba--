"""Improve the WooCommerce product CSV: missing treatments, real descriptions, images, categories, Yoast meta."""
import csv, io, re, sys, contextlib
sys.path.insert(0, '/home/user/p-Prueba--/thefaces/src')
with contextlib.redirect_stdout(io.StringIO()):
    import build  # noqa: assembles DESC / ELEMENTS like the site
from menu import MENU

SRC = '/root/.claude/uploads/da6eeaca-3a38-54c2-b2cc-cd456339a57d/76067666-thefaces-woocommerce-productos.csv'
OUT = '/home/user/p-Prueba--/thefaces/woocommerce/thefaces-woocommerce-productos-v4.csv'
MEDIA = 'https://thefacesbali.com/wp-content/plugins/thefaces-spa/assets/media/'
IMG = {'face': 'g01-face.webp', 'air': 'g12-proc-s.webp', 'head': 'g10-proc-s.webp', 'skin': 'g02-face-s.webp',
       'prog': 'g09-proc-s.webp', 'pack': 'g11-proc-s.webp', 'men': 'g05-interior-s.webp', 'two': 'g08-interior.webp',
       'body': 'g04-interior.webp'}
SHOP = 'https://thefacesbali.com/wp-content/plugins/thefaces-shop/assets/img/'
PIMG = {
 'myo': 'g01-face.webp', 'sculpt': 'g03-face-s.webp', 'buccal': 'g02-face-s.webp', 'guasha': 'g12-proc-s.webp',
 'love-sig': 'sense-smell.webp', 'faces-sig': 'og-1200x630.jpg', 'author': 'g11-proc-s.webp', 'hydrolift': 'sense-touch.webp',
 'hydro-face': 'waterfall.webp', 'four-hands': 'S:oil-hands.jpg', 'candle': 'sense-sight.webp',
 'airkiss': 'S:foam-bowl.jpg', 'airkiss-sculpt': 'S:foam-face.jpg', 'foamy-back': 'S:foam-back.jpg', 'foamy-dream': 'S:foam-cloud.jpg',
 'water-spa': 'S:headspa-pool-2.jpg', 'ayur': 'sense-taste.webp', 'shiro': 'g10-proc-s.webp', 'shine': 'waterfall-3.webp',
 'hair-face': 'S:headspa-pool-1.jpg', 'detox-myo': 'g09-proc-s.webp', 'detox-sculpt': 'S:headspa-pool-3.jpg', 'kids': 'g06-interior.webp',
 'atraumatic': 'g12-proc-s.webp', 'vacuum': 'g11-proc-s.webp', 'ultra': 'g01-face.webp', 'combo': 'g02-face-s.webp',
 'hydra': 'sense-touch.webp', 'oxy': 'S:foam-face.jpg', 'cryo': 'g03-face-s.webp', 'lymph-glow': 'sense-intuition.webp',
 'el-air': 'S:rice-walk.jpg', 'el-fire': 'sense-sight.webp', 'el-water': 'sense-touch.webp', 'el-earth': 'sense-hearing.webp', 'el-love': 'sense-smell.webp',
 'before-flight': 'salon-sanur.jpg', 'water-airkiss': 'S:foam-bowl.jpg', '3in1': 'g09-proc-s.webp', 'beauty-detox': 'g10-proc-s.webp',
 'power': 'S:massage-men.jpg', 'stressfree': 'S:men-tea.jpg',
 'love-two': 'sense-intuition.webp', 'eternal': 'waterfall.webp', 'honeymoon': 'g07-interior-s.webp',
 'body60': 'S:oil-hands.jpg', 'body90': 'S:massage-hands.jpg', 'body120': 'g05-interior-s.webp', 'fire': 'sense-sight.webp', 'aqua': 'sense-touch.webp',
 'refl30': 'S:foam-legs.jpg', 'refl60': 'S:massage-hands.jpg', 'refl90': 'S:oil-hands.jpg',
 'leg30': 'S:foam-back.jpg', 'leg60': 'S:foam-legs.jpg', 'leg90': 'S:foam-cloud.jpg',
}

def img_url(mid, cat):
    f = PIMG.get(mid)
    if not f:
        return MEDIA + IMG_ID.get(mid, IMG[cat])
    return SHOP + f[2:] if f.startswith('S:') else MEDIA + f

IMG_ID = {'sculpt': 'g03-face-s.webp', 'airkiss-sculpt': 'g11-proc-s.webp', 'shiro': 'g10-proc-s.webp',
          'beauty-detox': 'g09-proc-s.webp', 'myo': 'g01-face.webp'}
CATNAME = {'face': 'Face massage', 'air': 'Air kiss & foam', 'head': 'Head spa & hair', 'skin': 'Cleansing & care',
           'prog': 'Five elements', 'pack': 'Packages', 'men': 'For men', 'two': 'For couples', 'body': 'Body, feet & legs'}
PREPAID = ('Prepaid treatment. After payment you receive a confirmation email with a link to choose your date and time '
           'in the selected salon. Valid for 6 months.')

def norm(s):
    s = s.lower().replace('signature massage', 'signature').replace('signature technique:', '').replace('lymphatic drainage / relaxing leg massage', 'lymphatic leg massage')
    s = s.replace('water spa therapy with detox hair spa + airkiss detox ritual', 'water spa + detox hair spa + airkiss detox ritual')
    s = s.replace('·', ' ').replace('(add-on)', '').replace('candle treatment', 'candle treatment')
    return re.sub(r'[^a-z0-9]', '', s)

BY_NAME = {norm(m[2]): m for m in MENU}
ELEM = {e['id']: e for e in build.ELEMENTS}

def dur(mins):
    if not mins:
        return ''
    h, m = divmod(mins, 60)
    return ('%d h' % h if h else '') + (' %d min' % m if m else '') if h else '%d min' % m

def fmt(p):
    return '{:,}'.format(p).replace(',', ' ')

ALIAS = {'before-flight': 'jetlag'}
SKIP = {'water-airkiss'}
EXTRA_DESC = {
 'body60': 'Full body massage: back, legs, arms, neck and shoulders, with pressure adapted to you. A relaxing classic after a day of exploring Bali.',
 'body90': 'Full body massage: back, legs, arms, neck and shoulders, with pressure adapted to you. Ninety minutes give the therapist time for the areas that need it most.',
 'body120': 'Full body massage: back, legs, arms, neck and shoulders, with pressure adapted to you. Our longest body massage, for deep, unhurried relaxation.',
 'power': 'A programme designed for men to recover energy after travel, sport or demanding work. Available in Ubud.',
 'stressfree': 'A programme designed for men who arrive in Bali tired and want to switch off. Available in Ubud.',
 'aqua': 'A signature body ritual of THE FACES Sanur.',
 'foamy-dream': 'Our signature foam ritual: the body is wrapped in warm, airy foam during a long, deeply relaxing treatment.',
 'lymph-glow': 'A lymphatic glow facial for a fresher, de-puffed and luminous face. Available in Ubud.',
 'shine': 'A hair spa ritual focused on the beauty and shine of hair tired by sun, sea and humidity. Available in Ubud.',
 'hair-face': 'Water detox hair spa combined with a face massage in one session.',
 'detox-myo': 'Detox hair spa combined with a myofascial facial massage. Available in Sanur.',
 'detox-sculpt': 'Detox hair spa combined with a sculptural face massage. Available in Sanur.',
 '3in1': 'Head massage, face massage and hair spa combined in one session (Ubud 3 h · Sanur 1 h 30 min).',
 'love-two': 'The Element of Love ritual for two people, side by side in the same room.',
 'eternal': 'A ritual for couples, side by side in the same room.',
}

def lead(mid, fallback):
    if mid in EXTRA_DESC:
        return EXTRA_DESC[mid]
    mid = ALIAS.get(mid, mid)
    if mid in ELEM:
        e = ELEM[mid]
        inc = e['inc'][0] if isinstance(e['inc'][0], str) else ' · '.join(e['inc'][0])
        return '%s. %s Includes: %s.' % (e['t'][0].rstrip('.'), e['when'][0] if e.get('when') else '', inc)
    if mid in build.DESC and mid not in SKIP:
        return build.DESC[mid][0]
    return fallback

def dur_m(m):
    cat, mid, name, mins, price, only, diff = m
    if diff and any(v[0] and v[0] != mins for v in diff.values()):
        parts = ['Ubud %s' % dur(mins)] + ['%s %s' % (k.capitalize(), dur(v[0])) for k, v in diff.items()]
        return ' · '.join(parts)
    return dur(mins)

def describe(m, prices, fallback):
    cat, mid, name, mins, price, only, diff = m
    text = lead(mid, fallback).strip()
    d = dur_m(m)
    p = ' · '.join('%s: %s IDR' % (s.capitalize(), fmt(v)) for s, v in prices)
    html = '<p>%s</p>' % text
    if d:
        html += '<p><strong>Duration:</strong> %s</p>' % d
    html += '<p><strong>Salons and prices:</strong> %s</p>' % p
    html += '<h3>How it works</h3><ol><li>Choose the salon and pay online.</li><li>You receive a confirmation email with a link to choose your date and time.</li><li>Come to THE FACES and enjoy your treatment. The voucher is valid for 6 months.</li></ol>'
    html += '<p>Prefer to ask first? Write to us on WhatsApp: Ubud +62 822 6699 9965 · Sanur +62 813 3770 9190.</p>'
    short = '%s%s' % (text if len(text) < 220 else text[:217].rsplit(' ', 1)[0] + '…', (' Duration: %s.' % d) if d else '')
    meta = ('Prepay %s at THE FACES Bali (%s). %sFrom IDR %s. Choose your date after payment.' % (
        name, ' & '.join(s.capitalize() for s, _ in prices), ('%s. ' % d) if d else '', fmt(min(v for _, v in prices))))[:158]
    return html, short, meta

def prices_for(m):
    cat, mid, name, mins, price, only, diff = m
    salons = only or ['sanur', 'ubud']
    return [(s, (diff[s][1] if diff and s in diff else price)) for s in sorted(salons)]

rows = list(csv.DictReader(open(SRC, encoding='utf-8')))
fields = list(rows[0].keys()) + ['Images', 'Meta: _yoast_wpseo_metadesc']
out, seen = [], set()
for r in rows:
    if r['Type'] == 'variable':
        m = BY_NAME.get(norm(r['Name']))
        if not m:
            print('no menu match:', r['Name'])
        else:
            seen.add(m[1])
            html, short, meta = describe(m, prices_for(m), r['Short description'].split(' Duration')[0])
            r['Description'], r['Short description'] = html, short
            r['Images'] = img_url(m[1], m[0])
            r['Meta: _yoast_wpseo_metadesc'] = meta
            r['Categories'] = 'Prepaid treatments > ' + CATNAME[m[0]]
    if r['Type'] == 'variation':
        r['Visibility in catalog'] = 'visible'
    out.append(r)

def sku(name):
    return 'TF-' + re.sub(r'[^A-Z0-9]+', '-', name.upper()).strip('-')[:40]

added = []
for m in MENU:
    if m[1] in seen:
        continue
    cat, mid, name, mins, price, only, diff = m
    name = name.replace(' · ', ' ')
    pr = prices_for(m)
    html, short, meta = describe(m, pr, name)
    base = {k: '' for k in fields}
    s = sku(name)
    parent = dict(base, **{'Type': 'variable', 'SKU': s, 'Name': name, 'Published': '1', 'Visibility in catalog': 'visible',
                  'Short description': short, 'Description': html, 'Tax status': 'none', 'In stock?': '1',
                  'Categories': 'Prepaid treatments > ' + CATNAME[cat], 'Attribute 1 name': 'Salon',
                  'Attribute 1 value(s)': ', '.join(x.capitalize() for x, _ in pr), 'Attribute 1 visible': '1', 'Attribute 1 global': '1',
                  'Attribute 2 name': 'Duration', 'Attribute 2 value(s)': dur(mins) if dur_m(m) == dur(mins) else '', 'Attribute 2 visible': '1' if dur_m(m) == dur(mins) and mins else '0',
                  'Attribute 2 global': '0', 'Virtual': '1', 'Sold individually?': '0',
                  'Images': img_url(mid, cat), 'Meta: _yoast_wpseo_metadesc': meta})
    out.append(parent)
    for salon, p in pr:
        out.append(dict(base, **{'Type': 'variation', 'SKU': s + '-' + salon[:3].upper(), 'Name': '%s — %s' % (name, salon.capitalize()),
                       'Published': '1', 'Visibility in catalog': 'visible', 'Tax status': 'none', 'In stock?': '1', 'Regular price': str(p), 'Parent': s,
                       'Attribute 1 name': 'Salon', 'Attribute 1 value(s)': salon.capitalize(), 'Attribute 1 global': '1', 'Virtual': '1'}))
    added.append(name)

with open(OUT, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(out)
print('added:', added)
print('products:', sum(1 for r in out if r['Type'] == 'variable'), 'variations:', sum(1 for r in out if r['Type'] == 'variation'))
