"""Generates the 5 Instagram carousels (1080x1350 PNG) and the LinkedIn / Instagram texts.
Run: python3 social.py  (needs the images in IMG and Playwright)."""
import json, os, subprocess, html
D = os.path.dirname(os.path.abspath(__file__))
IMG = '/tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/deck/use/'
SITE = '/home/user/p-Prueba--/thefaces/wordpress-plugin/thefaces-spa/assets/media/'
BLOG = 'https://thefacespeace.com/'
def utm(slug, src, n):
    return f'{BLOG}{slug}/?utm_source={src}&utm_medium=social&utm_campaign=blog_{n:02d}'

POSTS = [
 dict(n=1, slug='ubud-vs-sanur-where-to-own-a-spa-in-bali', title='Ubud vs Sanur: where to own a spa in Bali',
  slides=[
   ('cover', 'Ubud or Sanur?', 'Where to own a spa in Bali', IMG + 'DSC03305-scaled.jpg'),
   ('text', 'Two markets, 45 minutes apart', 'Ubud: wellness travellers, long stays, signature rituals.\nSanur: hotels, couples, street visibility, steady flow.', None),
   ('num', '6.95M', 'foreign visitors to Bali in 2025, +9.7% on 2024 (BPS Bali)', None),
   ('list', '4 real projects', 'THE FACES Ubud · operating · $300K\nWATERFALL · Ubud · $300K\nThe White Temple · Sanur · $250K\nTHE FACES SANUR · $450K · 50/50', None),
   ('img', 'Visit before you decide', 'Book a treatment as a guest. Walk the street. Meet the team.', IMG + 'Screenshot-2026-11-10-at-09.35.15.jpg'),
   ('cta', 'Read the full guide', 'Link in bio · thefacespeace.com', None)],
  li="""Ubud or Sanur: where should you own a spa in Bali?

They are only 45 minutes apart, but they are two different markets:
→ Ubud: wellness travellers, long stays, signature rituals
→ Sanur: hotels, couples, street visibility and steady tourist flow

Bali welcomed 6.95 million foreign visitors in 2025, +9.7% on 2024 (BPS Bali).

We compared both areas and our 4 projects open to partners, from $250,000:
• THE FACES Ubud · operating · $300K
• WATERFALL · Ubud · $300K
• The White Temple · Sanur · $250K
• THE FACES SANUR · opposite the Hyatt · $450K · 50/50

Full guide 👉 {url}

#Bali #SpaInvestment #WellnessBusiness #Ubud #Sanur #PrivateInvestment"""),
 dict(n=2, slug='how-a-spa-partnership-works-bali', title='How a spa partnership works',
  slides=[
   ('cover', 'You own a share.', 'We run the spa.', IMG + 'thefaces-invest-15.jpg'),
   ('steps', 'How it works', '1 · You invest in one specific spa\n2 · You become a shareholder\n3 · THE FACES runs the business\n4 · You are paid monthly', None),
   ('num', 'Up to 49%', 'of shares and up to 50% of profit · SANUR: 50/50', None),
   ('calc', 'Illustrative example', '$25,000 net profit / month\n× 50% share = $12,500 / month\n$250K recovered in ~1.7 years\nIllustration, not a forecast', None),
   ('img', 'Fully managed', 'Team, rituals, marketing, bookings and accounting.', IMG + 'DSC03255-scaled.jpg'),
   ('cta', 'How the model works', 'Link in bio · thefacespeace.com', None)],
  li="""How does a spa partnership actually work?

You own a share. We run the spa.

1️⃣ You invest in one specific spa, not a pooled fund
2️⃣ You become a shareholder, in writing
3️⃣ THE FACES runs the team, rituals, marketing, bookings and accounting
4️⃣ You receive your share of the profit every month, with a financial report

Typical terms: up to 49% of shares and up to 50% of profit. THE FACES SANUR: 50/50.

Illustration (not a forecast): $25,000 monthly net profit × 50% = $12,500 a month.

The full explanation, with the 4 projects and their tickets 👉 {url}

Profit is not guaranteed and capital can be lost.
#SpaBusiness #Bali #WellnessInvestment #PassiveIncome #Hospitality"""),
 dict(n=3, slug='can-foreigners-own-a-spa-in-bali-pt-pma', title='Can foreigners own a spa in Bali?',
  slides=[
   ('cover', 'Can foreigners own', 'a spa in Bali?', IMG + 'Screenshot-2026-11-10-at-09.34.53.jpg'),
   ('text', 'Yes. Structure matters.', 'Most foreign partners hold shares through a PT PMA: an Indonesian company with foreign shareholders.', None),
   ('list', 'Check before signing', 'Company deed & NIB\nSpa licences\nLease: length & transfer\nShareholder agreement\nTax in both countries', None),
   ('num', '10 years', 'signed leases: The White Temple and THE FACES SANUR', None),
   ('text', 'Notarised shares', 'Registered with the Ministry of Law (AHU): a shareholder, not a lender.', None),
   ('cta', 'The legal side, explained', 'Link in bio · thefacespeace.com', None)],
  li="""Can a foreigner own a share of a spa in Bali?

Yes, and the structure is what protects you.

Most foreign partners invest through a PT PMA, an Indonesian company with foreign shareholders, with:
✔ a notarised shareholding registered with the Ministry of Law (AHU)
✔ a shareholder agreement: profit share, reporting, veto rights, exit
✔ a management agreement with the operator

Before signing, check the company deed, licences, the lease (two of our projects have 10-year leases signed) and tax in both countries.

We explain it in plain words 👉 {url}

General information, not legal advice. Always confirm with Indonesian counsel.
#PTPMA #Indonesia #Bali #ForeignInvestment #SpaBusiness"""),
 dict(n=4, slug='spa-investment-due-diligence-checklist', title='Spa investment due diligence',
  slides=[
   ('cover', '12 documents', 'to request before investing in a spa', IMG + 'DSC03214-scaled.jpg'),
   ('list', 'Financial', 'Monthly management accounts\nBank statements\nBooking-system sales data\nTax filings', None),
   ('list', 'Operating', 'Menu & prices\nStaff & payroll\nUtilisation\nBreak-even occupancy', None),
   ('list', 'Legal', 'Lease agreement\nLicences & permits\nShareholder agreement\nManagement agreement', None),
   ('text', 'Facts before decisions', 'Headline percentages are easy to print and hard to verify.', None),
   ('cta', 'Get the full checklist', 'Link in bio · thefacespeace.com', None)],
  li="""Before you invest in a spa, ask for these 12 documents.

📊 Financial: monthly management accounts · bank statements · booking-system sales data · tax filings
⚙️ Operating: menu & prices · staff & payroll · utilisation · break-even occupancy
📑 Legal: lease · licences · shareholder agreement · management agreement

Headline percentages are easy to print and hard to verify. Serious investors look at booking data, bank statements and contracts.

The full checklist + 5 questions to ask the founders 👉 {url}

#DueDiligence #SpaInvestment #PrivateEquity #Bali #WellnessBusiness"""),
 dict(n=5, slug='operating-spa-vs-new-spa-project-investment', title='Operating spa vs new project',
  slides=[
   ('cover', 'Operating spa', 'or new project?', IMG + 'the-faces-watefall-6.jpg'),
   ('text', 'Operating spa', 'Real accounts to verify. Revenue from day one.\nTHE FACES Ubud · $300K', None),
   ('text', 'New project', 'Enter before the launch. Shape the opening.\nWhite Temple $250K · WATERFALL $300K · SANUR $450K', None),
   ('list', 'How new projects reduce risk', '10-year signed leases\nCapital in tranches\nAn experienced operator', None),
   ('img', 'Which one fits you?', 'Ask about both on the same call.', IMG + 'the-faces-watefall-1.jpg'),
   ('cta', 'Compare them side by side', 'Link in bio · thefacespeace.com', None)],
  li="""Operating spa or new project: which investment fits you?

🟢 Operating spa: real accounts to verify, revenue from day one.
THE FACES Ubud · $300,000

🟡 New project: enter before the launch, accept construction risk.
The White Temple · $250,000 · WATERFALL · $300,000 · THE FACES SANUR · $450,000 (50/50, 24-month target payback)

New projects reduce risk with signed 10-year leases, capital in tranches and an experienced operator.

Side-by-side comparison 👉 {url}

Targets are not guarantees. Capital at risk.
#SpaInvestment #Bali #Hospitality #RealAssets #WellnessBusiness"""),
]

CSS = """*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Montserrat,Arial,sans-serif;background:#f6f4ee;color:#1b1f1b;position:relative;overflow:hidden}
.ser{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400}.lg{position:absolute;left:80px;top:70px;height:44px}.pg{position:absolute;right:80px;top:80px;font-size:22px;letter-spacing:.2em;color:#9a7b4f}
.bot{position:absolute;left:80px;right:80px;bottom:70px;display:flex;justify-content:space-between;font-size:20px;letter-spacing:.24em;text-transform:uppercase;color:#8a908a}
.mid{position:absolute;left:80px;right:80px;top:300px}
h1{font-size:110px;line-height:1;letter-spacing:-.01em}h1 em{font-style:italic;color:#9a7b4f}
h2{font-size:84px;line-height:1.02;margin-bottom:48px}p{font-size:40px;line-height:1.45;color:#3f473f;white-space:pre-line}
.ey{font-size:22px;letter-spacing:.3em;text-transform:uppercase;color:#9a7b4f;margin-bottom:34px}
.dark{background:#18201a;color:#fff}.dark p{color:#d6ddd4}.dark .bot{color:#9aa69a}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,16,11,.15) 30%,rgba(10,16,11,.85) 100%)}
.onimg{color:#fff}.onimg p{color:#eef2ec}.onimg .bot{color:#e6ebe4}.onimg .pg{color:#e2c891}
.num{font-size:200px;line-height:1;color:#9a7b4f;margin-bottom:40px}
ul{list-style:none}li{font-size:44px;padding:22px 0;border-bottom:2px solid #dcd8cc}li:before{content:"— ";color:#9a7b4f}
.dark li{border-color:#334033}
.cta{display:inline-block;margin-top:50px;padding:30px 48px;background:#1a73e8;color:#fff;font-size:30px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.disc{position:absolute;left:80px;right:80px;bottom:130px;font-size:20px;color:#8a908a;line-height:1.4}"""

def slide(p, i, s):
    kind, a, b, img = s
    tot = len(p['slides'])
    logo = 'logo.jpg'
    cls, inner = '', ''
    if kind == 'cover':
        cls = 'onimg'
        inner = f'<div class="bg" style="background-image:url(file://{img})"></div><div class="shade"></div><div class="mid" style="top:auto;bottom:220px"><p class="ey" style="color:#e2c891">THE FACES INVEST · Bali</p><h1 class="ser">{html.escape(a)}<br><em>{html.escape(b)}</em></h1></div>'
    elif kind == 'img':
        cls = 'onimg'
        inner = f'<div class="bg" style="background-image:url(file://{img})"></div><div class="shade"></div><div class="mid" style="top:auto;bottom:220px"><h2 class="ser">{html.escape(a)}</h2><p>{html.escape(b)}</p></div>'
    elif kind == 'num':
        inner = f'<div class="mid"><div class="num ser">{html.escape(a)}</div><p>{html.escape(b)}</p></div>'
    elif kind in ('list', 'steps'):
        li = ''.join(f'<li>{html.escape(x)}</li>' for x in b.split('\n'))
        cls = 'dark' if kind == 'steps' else ''
        inner = f'<div class="mid" style="top:260px"><h2 class="ser">{html.escape(a)}</h2><ul>{li}</ul></div>'
    elif kind == 'calc':
        cls = 'dark'
        lines = b.split('\n')
        inner = f'<div class="mid"><p class="ey" style="color:#e2c891">{html.escape(a)}</p>' + ''.join(f'<h2 class="ser" style="font-size:76px;margin-bottom:26px">{html.escape(x)}</h2>' for x in lines[:-1]) + f'</div><div class="disc" style="color:#9aa69a">{html.escape(lines[-1])}. Profit varies and is not guaranteed.</div>'
    elif kind == 'text':
        inner = f'<div class="mid"><h2 class="ser">{html.escape(a)}</h2><p>{html.escape(b)}</p></div>'
    elif kind == 'cta':
        cls = 'dark'
        inner = f'<div class="mid"><p class="ey" style="color:#e2c891">{html.escape(p["title"])}</p><h2 class="ser">{html.escape(a)}</h2><p>{html.escape(b)}</p><span class="cta">Read on the blog</span></div><div class="disc" style="color:#9aa69a">Information only. Not an offer. Capital at risk.</div>'
    filt = 'filter:brightness(0) invert(1);' if cls in ('dark', 'onimg') else ''
    return (f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file:///tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/deck/fonts/fonts.css"><style>{CSS}</style></head>'
            f'<body class="{cls}">{inner}<img class="lg" style="{filt}" src="file://{IMG}{logo}"><span class="pg">{i+1:02d} / {tot:02d}</span>'
            f'<div class="bot"><span>thefacespeace.com</span><span>{"Swipe →" if i < tot-1 else "@thefacesinvest"}</span></div></body></html>')

if __name__ == '__main__':
    jobs = []
    for p in POSTS:
        for i, s in enumerate(p['slides']):
            f = os.path.join(D, 'instagram', f'{p["n"]:02d}-{i+1:02d}.html')
            open(f, 'w').write(slide(p, i, s)); jobs.append(f)
    json.dump(jobs, open('/tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/ig_jobs.json', 'w'))
    li_out, ig_out = [], []
    for p in POSTS:
        li_out.append(f'## {p["n"]}. {p["title"]}\n\n' + p['li'].format(url=utm(p['slug'], 'linkedin', p['n'])) + '\n')
        ig_out.append(f'## Carrusel {p["n"]} · {p["title"]}\nImágenes: instagram/{p["n"]:02d}-01.jpg … {p["n"]:02d}-{len(p["slides"]):02d}.jpg\nEnlace para la bio (Linktree o similar): {utm(p["slug"], "instagram", p["n"])}\n\nTexto:\n'
                      + p['li'].split('\n\n')[0] + '\n\n' + '\n'.join(p['li'].split('\n\n')[1:-1]).replace('{url}', 'link in bio').replace('👉 link in bio', '👉 link in bio') + '\n\n🔗 Link in bio · @thefacesinvest\n' + p['li'].split('\n\n')[-1] + '\n')
    open(os.path.join(D, 'linkedin', 'linkedin-posts.md'), 'w').write('# LinkedIn · 5 publicaciones (cada una enlaza a su artículo)\n\nPublicar cuando el artículo esté en línea. Los enlaces llevan UTM para medir en Analytics.\n\n' + '\n\n'.join(li_out))
    open(os.path.join(D, 'instagram', 'instagram-captions.md'), 'w').write('# Instagram · 5 carruseles\n\n' + '\n\n'.join(ig_out))
    print('ok', len(jobs))
