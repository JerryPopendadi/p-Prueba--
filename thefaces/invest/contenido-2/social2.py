"""5 Instagram carousels (1080x1350) + LinkedIn texts + Instagram captions. Montserrat only, gold THE FACES PARTNERS logo."""
import os, json, html
D = os.path.dirname(os.path.abspath(__file__))
I = 'file://' + os.path.join(D, '_img') + '/'
FONTS = 'file:///tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/deck/fonts/fonts.css'
B = 'https://thefacespeace.com/'
def utm(slug, src, n): return f'{B}{slug}/?utm_source={src}&utm_medium=social&utm_campaign=blog_{n:02d}'

P = [
 dict(n=6, slug='bali-wellness-investment-destination-2026', t='Why Bali, why wellness', s=[
  ('photo', 'terraces-aerial.jpg', 'BALI · 2026', 'Where wellness\nis a way of life', ''),
  ('photo', 'terraces-flowers.jpg', '01', 'An island built\non ritual', 'Temples, rice terraces and ceremonies at sunset. Wellness was here long before it became an industry.'),
  ('stat', None, '02 · VISITORS', '6.95M', 'foreign visitors to Bali in 2025, +9.7% on 2024 · BPS Bali'),
  ('stat', None, '03 · THE MARKET', 'US$6.8T', 'global wellness economy in 2024, forecast near US$9.8T by 2029 · Global Wellness Institute'),
  ('photo', 'uluwatu-sunset.jpg', '04', 'Own a share\nof that feeling', 'Four THE FACES spa projects open to partners, from $250,000.'),
  ('cta', None, '', 'Read the full story', 'Link in bio'),
 ], li="""Bali has always been a place people visit to feel better.

Long before "wellness" became an industry, the island lived by ritual: offerings on temple steps, water through the rice terraces, ceremonies at sunset over Uluwatu.

Today that culture meets a global market:
• 6.95M foreign visitors to Bali in 2025, +9.7% (BPS Bali)
• US$6.8T global wellness economy in 2024, forecast near US$9.8T by 2029 (Global Wellness Institute)

That is why private investors are looking at Bali spas, and why we built THE FACES here.

Why Bali is becoming a wellness investment destination 👉 {url}

#Bali #WellnessInvestment #SpaBusiness #Hospitality #THEFACESPARTNERS"""),
 dict(n=7, slug='five-elements-spa-concept', t='The Five Elements', s=[
  ('photo', 'temple-dusk.jpg', 'THE FIVE ELEMENTS', 'Not a treatment.\nA ritual.', ''),
  ('list', None, 'THE ELEMENTS', 'Earth · Water · Fire\nAir · Love', 'Each one shapes the menu, the scent, the music and the colour of every room.'),
  ('photo', 'Screenshot-2026-11-10-at-09.35.15.jpg', '01', 'Guests remember\nhow they felt', 'A ritual is a journey: welcome, transition, care and return.'),
  ('text', None, '02 · FOR PARTNERS', 'Ritual is\na business advantage', 'A protected concept means a higher ticket, repeat guests and no price war with ordinary spas.'),
  ('photo', 'uluwatu-gate.jpg', '03', 'Protected\nin Indonesia', 'Registered trademark and a copyrighted Five Elements Concept.'),
  ('cta', None, '', 'Discover the concept', 'Link in bio'),
 ], li="""Any spa can buy massage tables and beautiful lamps.
What it cannot buy is a reason for guests to come back.

At THE FACES that reason is the Five Elements concept: Earth, Water, Fire, Air and Love shape every ritual, every room, every scent.

For a partner, that matters:
→ a signature product that avoids price wars
→ a higher average ticket
→ guests who return and recommend
→ a concept protected in Indonesia (registered trademark + copyright)

Why ritual is a business advantage 👉 {url}

#SpaConcept #WellnessBusiness #Bali #BrandBuilding #THEFACESPARTNERS"""),
 dict(n=8, slug='what-makes-a-spa-profitable', t='What makes a spa profitable', s=[
  ('photo', 'DSC03305-scaled.jpg', 'FOR INVESTORS', 'What makes a spa\nprofitable?', ''),
  ('num', None, '01', 'Utilisation', 'The share of treatment hours actually booked. The biggest lever on profit.'),
  ('num', None, '02', 'Average ticket', 'Signature rituals and couples programmes raise revenue per visit.'),
  ('num', None, '03', 'Repeat guests', 'Returning guests and packages bring revenue at almost no marketing cost.'),
  ('num', None, '04 · 05', 'Costs & break-even', 'Long leases make the biggest cost predictable. The lower the break-even, the stronger the spa.'),
  ('cta', None, '', 'Read the 5-number guide', 'Link in bio'),
 ], li="""A beautiful spa is not automatically a profitable one.

Behind the candles and the music, every spa runs on five numbers:
1️⃣ Utilisation: booked hours ÷ available hours
2️⃣ Average ticket: revenue per visit
3️⃣ Repeat guests: returning visitors and packages
4️⃣ Cost base: rent, team, products, fees
5️⃣ Break-even occupancy: how resilient the spa is in a quiet month

Learn to read them and you can judge any spa's accounts.

The simple guide 👉 {url}

#SpaBusiness #Investing #DueDiligence #Hospitality #THEFACESPARTNERS"""),
 dict(n=9, slug='hotel-spa-partnership-bali', t='A spa for your property', s=[
  ('photo', 'jungle-balcony.jpg', 'HOTEL & VILLA OWNERS', 'A spa your guests\nwill remember', ''),
  ('list', None, 'FOUR FORMATS', 'Spa development\nWellness management\nHotel & resort spa\nFranchise & licensing', ''),
  ('photo', 'the-faces-watefall-1.jpg', '01', 'Concept, design\nand launch', 'Signature rituals, interiors and a trained team.'),
  ('text', None, '02', 'We run it.\nYour guests enjoy it.', 'Team, standards, marketing, bookings and regular reporting.'),
  ('photo', 'terraces-flowers.jpg', '03', 'In Bali since 2013', 'And open to new destinations abroad.'),
  ('cta', None, '', 'Tell us about your property', 'Link in bio'),
 ], li="""Hotel, resort or villa owner?

Guests choose a property for the experience, and the spa is often the moment they remember. Running it well takes its own know-how.

THE FACES partners with owners in four ways:
• Spa development: concept, interiors, rituals, launch
• Wellness management: we run the spa for you
• Hotel & resort spa: a THE FACES spa inside your property
• Franchise & licensing: our formats in new markets

How a hotel spa partnership works 👉 {url}

#HotelSpa #Hospitality #Bali #ResortDevelopment #THEFACESPARTNERS"""),
 dict(n=10, slug='investor-trip-bali-3-days', t='A 3-day investor trip', s=[
  ('photo', 'uluwatu-sunset.jpg', 'INVESTOR TRIP', '3 days in Bali.\nDecide with facts.', ''),
  ('photo', 'terraces-aerial.jpg', 'DAY 1 · UBUD', 'Book a treatment.\nMeet the team.', 'See an operating spa as a guest, then review the numbers with the founders.'),
  ('photo', 'Screenshot-2026-11-10-at-09.35.15.jpg', 'DAY 2 · SANUR', 'Walk the street.\nCount the flow.', 'Two new projects, 10-year leases signed.'),
  ('photo', 'uluwatu-gate.jpg', 'DAY 3 · ULUWATU', 'Time to think.', 'Sunset on the cliffs, your notes, your questions.'),
  ('text', None, "CAN'T TRAVEL?", 'Visit online', 'Live video walkthroughs of every project, then a call with the founders.'),
  ('cta', None, '', 'Plan your visit', 'Link in bio'),
 ], li="""Numbers on a screen tell part of the story. Walking into the spa tells the rest.

A 3-day investor trip to Bali:
🌿 Day 1 · Ubud: book a treatment at an operating spa, meet the team, review the numbers
🌊 Day 2 · Sanur: walk the street opposite the Hyatt, see two new projects with 10-year leases
🌅 Day 3 · Uluwatu: sunset, notes and time to think

Can't travel? We run live video walkthroughs.

The full itinerary 👉 {url}

#InvestorTrip #Bali #SpaInvestment #DueDiligence #THEFACESPARTNERS"""),
]

CSS = """*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Montserrat,sans-serif;background:#0b0b0a;color:#fff;position:relative;overflow:hidden}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 45%,rgba(0,0,0,.82) 100%)}
.logo{position:absolute;left:50%;top:64px;transform:translateX(-50%);width:230px}
.ey{font-size:22px;font-weight:500;letter-spacing:.42em;color:#d9b45a;margin-bottom:30px}
h1{font-size:86px;font-weight:300;line-height:1.08;letter-spacing:-.01em;white-space:pre-line}
h2{font-size:72px;font-weight:300;line-height:1.1;white-space:pre-line;margin-bottom:34px}
p{font-size:34px;font-weight:300;line-height:1.5;color:rgba(255,255,255,.86);max-width:860px}
.btm{position:absolute;left:90px;right:90px;bottom:120px}
.mid{position:absolute;left:90px;right:90px;top:50%;transform:translateY(-50%)}
.line{width:90px;height:2px;background:#d9b45a;margin:40px 0}
.big{font-size:190px;font-weight:200;color:#d9b45a;line-height:1;letter-spacing:-.03em;margin-bottom:30px}
.foot{position:absolute;left:90px;right:90px;bottom:52px;display:flex;justify-content:space-between;font-size:18px;letter-spacing:.32em;color:rgba(255,255,255,.6)}
.dark{background:radial-gradient(120% 90% at 50% 0%,#1d1a12 0%,#0b0b0a 60%)}
.list h2{color:#fff}.gold{color:#d9b45a}
.cta{text-align:center}.cta .mid{text-align:center}.cta .biglogo{width:620px;margin:0 auto 60px;display:block}
.btn{display:inline-block;margin-top:46px;padding:26px 54px;border:2px solid #d9b45a;color:#d9b45a;font-size:26px;letter-spacing:.3em}
.disc{position:absolute;left:90px;right:90px;bottom:100px;text-align:center;font-size:18px;color:rgba(255,255,255,.45);letter-spacing:.06em}"""

def slide(p, i, s):
    kind, img, ey, h, txt = s
    tot = len(p['s']); E = html.escape
    logo = f'<img class="logo" src="{I}logo-gold-transparent.png">'
    if kind == 'photo':
        body = f'<div class="bg" style="background-image:url({I}{img})"></div><div class="sh"></div>{logo}<div class="btm"><p class="ey">{E(ey)}</p><h1>{E(h)}</h1>' + (f'<div class="line"></div><p>{E(txt)}</p>' if txt else '') + '</div>'
        cls = ''
    elif kind in ('stat', 'num'):
        big = h if kind == 'stat' else ey
        sub = txt if kind == 'stat' else ''
        inner = (f'<p class="ey">{E(ey)}</p><div class="big">{E(h)}</div><p>{E(txt)}</p>' if kind == 'stat'
                 else f'<div class="big" style="font-size:150px">{E(ey)}</div><h2>{E(h)}</h2><div class="line"></div><p>{E(txt)}</p>')
        body = f'{logo}<div class="mid">{inner}</div>'; cls = 'dark'
    elif kind == 'list':
        body = f'{logo}<div class="mid list"><p class="ey">{E(ey)}</p><h2 class="gold" style="font-size:70px;line-height:1.35">{E(h)}</h2>' + (f'<div class="line"></div><p>{E(txt)}</p>' if txt else '') + '</div>'; cls = 'dark'
    elif kind == 'text':
        body = f'{logo}<div class="mid"><p class="ey">{E(ey)}</p><h2>{E(h)}</h2><div class="line"></div><p>{E(txt)}</p></div>'; cls = 'dark'
    else:
        body = f'<div class="mid"><img class="biglogo" src="{I}logo-gold-transparent.png"><p class="ey" style="letter-spacing:.3em">{E(p["t"].upper())}</p><h2 style="font-size:60px">{E(h)}</h2><span class="btn">{E(txt.upper())}</span></div><div class="disc">thefacespeace.com · Information only, not an offer · Capital at risk</div>'; cls = 'dark cta'
    foot = f'<div class="foot"><span>@THEFACESINVEST</span><span>{i+1:02d} / {tot:02d}{"  →" if i < tot-1 else ""}</span></div>' if kind != 'cta' else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head><body class="{cls}">{body}{foot}</body></html>'

if __name__ == '__main__':
    jobs = []
    for p in P:
        for i, s in enumerate(p['s']):
            f = os.path.join(D, 'instagram', f'{p["n"]:02d}-{i+1:02d}.html'); open(f, 'w').write(slide(p, i, s)); jobs.append(f)
    json.dump(jobs, open('/tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/ig_jobs.json', 'w'))
    li, ig = [], []
    for p in P:
        li.append(f'## {p["n"]}. {p["t"]}\n\n' + p['li'].format(url=utm(p['slug'], 'linkedin', p['n'])) + '\n')
        body = p['li'].replace('👉 {url}', '👉 link in bio')
        ig.append(f'## Carrusel {p["n"]} · {p["t"]}\nImágenes: {p["n"]:02d}-01.jpg … {p["n"]:02d}-06.jpg\nEnlace para la bio: {utm(p["slug"], "instagram", p["n"])}\n\n{body}\n')
    open(os.path.join(D, 'linkedin', 'linkedin-posts.md'), 'w').write('# LinkedIn · 5 publicaciones (cada una enlaza a su artículo del blog)\n\nPublica cada post el mismo día que su artículo. Los enlaces llevan UTM para medirlos en Analytics.\nImagen sugerida para cada post: la primera imagen de su carrusel (instagram/NN-01.jpg).\n\n' + '\n'.join(li))
    open(os.path.join(D, 'instagram', 'instagram-captions.md'), 'w').write('# Instagram · 5 carruseles\n\n' + '\n'.join(ig))
    print('ok', len(jobs))
