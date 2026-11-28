"""Carousel in the 'label boxes over photo' style (like the example), RU + EN, photos from thefacesbali.com."""
import os, json, html
D = os.path.dirname(os.path.abspath(__file__))
I = 'file://' + os.path.join(D, '_img') + '/'
FONTS = 'file:///tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/deck/fonts/fonts.css'

# (photo, position, [(text, style)])  style: b=bold label, n=normal label, g=gold label
S = {
'ru': [
 ('DSC03305-scaled.jpg', 'top', [('Ubud, Bali · Убуд', 'b'), ('SPA, КОТОРЫЙ УЖЕ РАБОТАЕТ', 'n')],
  'bot', [('ЭТО НЕ ПРОЕКТ НА БУМАГЕ.', 'n'), ('РЕАЛЬНЫЕ ГОСТИ.', 'n'), ('РЕАЛЬНАЯ КОМАНДА.', 'n'), ('THE FACES · Бали с 2013 года', 'g')]),
 ('g01-face.jpg', 'top', [('ПРЕДСТАВЬТЕ УТРО ЗДЕСЬ', 'n'), ('ТИШИНА.', 'n'), ('ТЁПЛЫЕ МАСЛА.', 'n'), ('И РИТУАЛ ПЯТИ СТИХИЙ.', 'n')], None, []),
 ('sense-touch.jpg', 'mid', [('ЗЕМЛЯ · ВОДА · ОГОНЬ', 'b'), ('ВОЗДУХ · ЛЮБОВЬ', 'b')], 'mid2', [('АВТОРСКИЕ РИТУАЛЫ,', 'n'), ('КОТОРЫЕ НЕЛЬЗЯ СКОПИРОВАТЬ.', 'n')]),
 ('g04-interior.jpg', 'top', [('4 SPA-ПРОЕКТА В УБУДЕ И САНУРЕ', 'n'), ('ПАРТНЁРСТВО ОТ $250 000', 'b'), ('ВЫ — ПАРТНЁР.', 'n'), ('МЫ УПРАВЛЯЕМ SPA.', 'n')], 'bot', [('ЧЕГО ЕЩЁ ЖЕЛАТЬ?', 'b')]),
 ('g08-interior.jpg', 'bot', [('ВСЁ ВЕДЁТ НАША КОМАНДА:', 'b'), ('ПЕРСОНАЛ, РИТУАЛЫ, МАРКЕТИНГ, ЗАПИСЬ.', 'n'), ('ВЫ ПОЛУЧАЕТЕ ЕЖЕМЕСЯЧНЫЙ ОТЧЁТ.', 'n')], None, []),
 ('founders.jpg', 'bot', [('И ДА, С ДОКУМЕНТАМИ', 'b'), ('ВСЁ ПРОЗРАЧНО.', 'b'), ('ДОГОВОР · ОТЧЁТЫ · ВИЗИТ', 'n'), ('ВСЁ — ДО ЛЮБОГО РЕШЕНИЯ.', 'n'), ('Анна и Евгений Дубинины, основатели', 'g')], None, []),
 ('END', None, ['ЗАИНТЕРЕСОВАЛИСЬ?', 'Напишите «SPA» в комментариях,', 'и мы отправим вам подробную', 'информацию.'], None, []),
],
'en': [
 ('DSC03305-scaled.jpg', 'top', [('Ubud, Bali', 'b'), ('A SPA THAT ALREADY WORKS', 'n')],
  'bot', [('NOT A PROJECT ON PAPER.', 'n'), ('REAL GUESTS.', 'n'), ('A REAL TEAM.', 'n'), ('THE FACES · Bali since 2013', 'g')]),
 ('g01-face.jpg', 'top', [('IMAGINE YOUR MORNING HERE', 'n'), ('SILENCE.', 'n'), ('WARM OILS.', 'n'), ('AND A FIVE ELEMENTS RITUAL.', 'n')], None, []),
 ('sense-touch.jpg', 'mid', [('EARTH · WATER · FIRE', 'b'), ('AIR · LOVE', 'b')], 'mid2', [('SIGNATURE RITUALS', 'n'), ('NO ONE CAN COPY.', 'n')]),
 ('g04-interior.jpg', 'top', [('4 SPA PROJECTS IN UBUD & SANUR', 'n'), ('PARTNERSHIP FROM $250,000', 'b'), ('YOU ARE THE PARTNER.', 'n'), ('WE RUN THE SPA.', 'n')], 'bot', [('WHAT MORE COULD YOU WANT?', 'b')]),
 ('g08-interior.jpg', 'bot', [('OUR TEAM HANDLES EVERYTHING:', 'b'), ('STAFF, RITUALS, MARKETING, BOOKINGS.', 'n'), ('YOU RECEIVE A MONTHLY REPORT.', 'n')], None, []),
 ('founders.jpg', 'bot', [('AND YES,', 'b'), ('THE PAPERWORK IS CLEAR.', 'b'), ('AGREEMENT · REPORTS · SITE VISIT', 'n'), ('ALL BEFORE ANY DECISION.', 'n'), ('Anna & Evgenii Dubinin, founders', 'g')], None, []),
 ('END', None, ['INTERESTED?', 'Comment «SPA» below', 'and we will send you', 'the full details.'], None, []),
]}

CSS = """*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Montserrat,sans-serif;background:#111}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.grp{position:absolute;left:0;right:0;display:flex;flex-direction:column;align-items:center;gap:14px;padding:0 60px}
.top{top:70px}.bot{bottom:80px}.mid{top:430px}.mid2{top:640px}
.l{background:#fff;color:#111;border-radius:16px;padding:12px 26px 13px;font-size:42px;line-height:1.15;font-weight:500;letter-spacing:-.005em;text-align:center;box-shadow:0 6px 22px rgba(0,0,0,.18)}
.l.b{font-weight:700}
.l.g{background:#b08d4a;color:#fff;font-weight:600;font-size:36px}
.num{position:absolute;right:40px;top:40px;background:rgba(0,0,0,.45);color:#fff;font-size:24px;padding:8px 16px;border-radius:30px}
.end{background:radial-gradient(110% 80% at 50% 30%,#1f2230 0%,#12141c 70%)}
.end .logo{position:absolute;left:50%;top:330px;transform:translateX(-50%);width:600px}
.end .t{position:absolute;left:80px;right:80px;top:720px;text-align:center;color:#fff}
.end .t div{font-size:46px;line-height:1.45;font-weight:400}.end .t div:first-child{font-weight:600;margin-bottom:14px;letter-spacing:.02em}
.end .w{position:absolute;bottom:70px;left:0;right:0;text-align:center;color:rgba(255,255,255,.5);font-size:22px;letter-spacing:.3em}"""

def lab(items):
    return ''.join(f'<div class="l {s}">{html.escape(t)}</div>' for t, s in items)

def page(lang, i, sl, tot):
    img, p1, l1, p2, l2 = sl
    if img == 'END':
        body = f'<div class="end" style="position:absolute;inset:0"></div><img class="logo" src="{I}logo-gold-transparent.png"><div class="t">' + ''.join(f'<div>{html.escape(x)}</div>' for x in l1) + '</div><div class="w">THEFACESPEACE.COM</div>'
    else:
        body = f'<div class="bg" style="background-image:url({I}{img})"></div><div class="grp {p1}">{lab(l1)}</div>' + (f'<div class="grp {p2}">{lab(l2)}</div>' if p2 else '')
    cls = 'end' if img == 'END' else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head><body class="{cls}">{body}<div class="num">{i+1}/{tot}</div></body></html>'

jobs = []
for lang, slides in S.items():
    for i, sl in enumerate(slides):
        f = os.path.join(D, 'instagram', f'{lang}-{i+1:02d}.html'); open(f, 'w').write(page(lang, i, sl, len(slides))); jobs.append(f)
json.dump(jobs, open('/tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/ig_jobs.json', 'w'))
print(len(jobs))
