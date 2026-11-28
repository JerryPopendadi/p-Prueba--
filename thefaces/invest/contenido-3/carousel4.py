"""Same story as carousel3, in THE FACES PARTNERS style (dark, gold, Montserrat light). No prices. RU + EN."""
import os, json, html
D = os.path.dirname(os.path.abspath(__file__))
I = 'file://' + os.path.join(D, '_img') + '/'
FONTS = 'file:///tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/deck/fonts/fonts.css'

# kind, image, eyebrow, title, text
S = {
'ru': [
 ('photo', 'DSC03305-scaled.jpg', 'УБУД · БАЛИ', 'SPA, который\nуже работает', 'Не проект на бумаге. Реальные гости, реальная команда.'),
 ('photo', 'g01-face.jpg', '01', 'Представьте\nутро здесь', 'Тишина. Тёплые масла. И ритуал пяти стихий.'),
 ('photo', 'sense-touch.jpg', '02 · ПЯТЬ СТИХИЙ', 'Земля · Вода · Огонь\nВоздух · Любовь', 'Авторские ритуалы, которые нельзя скопировать.'),
 ('dark', None, '03 · ПАРТНЁРСТВО', 'Вы — партнёр.\nМы управляем SPA.', '4 SPA-проекта в Убуде и Сануре. Условия обсуждаются индивидуально.'),
 ('photo', 'g08-interior.jpg', '04', 'Всё ведёт\nнаша команда', 'Персонал, ритуалы, маркетинг, запись. Вы получаете ежемесячный отчёт.'),
 ('photo', 'founders.jpg', '05 · ОСНОВАТЕЛИ', 'С документами\nвсё прозрачно', 'Договор, отчёты и визит на объект — до любого решения. Анна и Евгений Дубинины.'),
 ('cta', None, 'ЗАИНТЕРЕСОВАЛИСЬ?', 'Напишите «SPA»\nв комментариях', 'и мы отправим вам подробную информацию'),
],
'en': [
 ('photo', 'DSC03305-scaled.jpg', 'UBUD · BALI', 'A spa that\nalready works', 'Not a project on paper. Real guests, a real team.'),
 ('photo', 'g01-face.jpg', '01', 'Imagine your\nmorning here', 'Silence. Warm oils. And a Five Elements ritual.'),
 ('photo', 'sense-touch.jpg', '02 · FIVE ELEMENTS', 'Earth · Water · Fire\nAir · Love', 'Signature rituals no one can copy.'),
 ('dark', None, '03 · PARTNERSHIP', 'You are the partner.\nWe run the spa.', '4 spa projects in Ubud and Sanur. Terms are agreed individually.'),
 ('photo', 'g08-interior.jpg', '04', 'Our team\nhandles everything', 'Staff, rituals, marketing, bookings. You receive a monthly report.'),
 ('photo', 'founders.jpg', '05 · THE FOUNDERS', 'The paperwork\nis clear', 'Agreement, reports and a site visit — before any decision. Anna & Evgenii Dubinin.'),
 ('cta', None, 'INTERESTED?', 'Comment «SPA»\nbelow', 'and we will send you the full details'),
]}

CSS = """*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Montserrat,sans-serif;background:#0b0b0a;color:#fff;position:relative;overflow:hidden}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.5) 0%,rgba(0,0,0,0) 24%,rgba(0,0,0,0) 42%,rgba(0,0,0,.85) 100%)}
.logo{position:absolute;left:50%;top:64px;transform:translateX(-50%);width:230px}
.ey{font-size:22px;font-weight:500;letter-spacing:.42em;color:#d9b45a;margin-bottom:30px}
h1{font-size:84px;font-weight:300;line-height:1.08;white-space:pre-line}
p{font-size:34px;font-weight:300;line-height:1.5;color:rgba(255,255,255,.88);max-width:880px}
.btm{position:absolute;left:90px;right:90px;bottom:120px}
.mid{position:absolute;left:90px;right:90px;top:50%;transform:translateY(-50%)}
.line{width:90px;height:2px;background:#d9b45a;margin:40px 0}
.foot{position:absolute;left:90px;right:90px;bottom:52px;display:flex;justify-content:space-between;font-size:18px;letter-spacing:.32em;color:rgba(255,255,255,.6)}
.dark{background:radial-gradient(120% 90% at 50% 0%,#1d1a12 0%,#0b0b0a 60%)}
.dark h1{color:#d9b45a}
.cta .mid{text-align:center}.cta .biglogo{width:560px;margin:0 auto 70px;display:block}.cta .line{margin:40px auto}.cta p{margin:0 auto}
.disc{position:absolute;left:90px;right:90px;bottom:70px;text-align:center;font-size:18px;color:rgba(255,255,255,.45);letter-spacing:.06em}"""

def page(i, sl, tot):
    k, img, ey, h, txt = sl; E = html.escape
    logo = f'<img class="logo" src="{I}logo-gold-transparent.png">'
    foot = f'<div class="foot"><span>THEFACESPEACE.COM</span><span>{i+1:02d} / {tot:02d}  →</span></div>'
    if k == 'photo':
        body = f'<div class="bg" style="background-image:url({I}{img})"></div><div class="sh"></div>{logo}<div class="btm"><p class="ey">{E(ey)}</p><h1>{E(h)}</h1><div class="line"></div><p>{E(txt)}</p></div>{foot}'; cls = ''
    elif k == 'dark':
        body = f'{logo}<div class="mid"><p class="ey">{E(ey)}</p><h1>{E(h)}</h1><div class="line"></div><p>{E(txt)}</p></div>{foot}'; cls = 'dark'
    else:
        body = f'<div class="mid"><img class="biglogo" src="{I}logo-gold-transparent.png"><p class="ey" style="letter-spacing:.3em">{E(ey)}</p><h1 style="font-size:66px">{E(h)}</h1><div class="line"></div><p>{E(txt)}</p></div><div class="disc">thefacespeace.com · Information only, not a public offer</div>'; cls = 'dark cta'
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head><body class="{cls}">{body}</body></html>'

jobs = []
for lang, slides in S.items():
    for i, sl in enumerate(slides):
        f = os.path.join(D, 'instagram', f'{lang}-{i+1:02d}.html'); open(f, 'w').write(page(i, sl, len(slides))); jobs.append(f)
json.dump(jobs, open('/tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/ig_jobs.json', 'w'))
print(len(jobs))
