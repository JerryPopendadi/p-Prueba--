"""THE FACES PARTNERS · investor creative v2 (clear offer: buy a share, we run the business).

Formats: reel (1080x1920, text in the Reels safe zone) and feed (1080x1350).
Languages: en, ru. 6 scenes x 4.5 s (+1.5 s on the last) = 28.5 s.
Run: python3 investor.py overlays && node render2.js _ov2/jobs.json && python3 investor.py video
"""
import glob
import json
import os
import subprocess
import sys

H = os.path.dirname(os.path.abspath(__file__))
U = '/root/.claude/uploads/da6eeaca-3a38-54c2-b2cc-cd456339a57d'
OV = H + '/_ov2'
DUR = 4.5
FORMATS = {'reel': (1080, 1920), 'feed': (1080, 1350)}

SCENES = [
    dict(key='1', video='29d1cbad', start=0.0,
         en=dict(eye='FOR INVESTORS · BALI', title='Buy a share<br>of a Bali spa', body='We run the business. You own part of it.'),
         ru=dict(eye='ДЛЯ ИНВЕСТОРОВ · БАЛИ', title='Купите долю<br>спа на Бали', body='Бизнесом управляем мы. Вы — совладелец.')),
    dict(key='2', video='76f6e149', start=7.0,
         en=dict(eye='THE FACES UBUD · OPERATING', title='Up to 49% of<br>a working spa', body='Real guests every day. Not a plan on paper.'),
         ru=dict(eye='THE FACES UBUD · РАБОТАЕТ', title='До 49% в<br>работающем спа', body='Гости каждый день. Не проект на бумаге.')),
    dict(key='3', video='dc5df73d', start=2.0,
         en=dict(eye='UBUD & SANUR', title='4 spas.<br>Choose yours.', body='Operating · in renovation · in construction'),
         ru=dict(eye='УБУД И САНУР', title='4 спа.<br>Выберите свой.', body='Работает · ремонт · строительство')),
    dict(key='4', video='270d6a31', start=4.0,
         en=dict(eye='WE DO EVERYTHING', title='Our team<br>runs it daily', body='Staff · marketing · operations · accounting'),
         ru=dict(eye='ВСЁ ДЕЛАЕМ МЫ', title='Наша команда<br>управляет', body='Персонал · маркетинг · работа · бухгалтерия')),
    dict(key='5', video='54573c64', start=0.0,
         en=dict(eye='WHAT YOU RECEIVE', title='Your share<br>of the profit', body='Monthly financial report.<br>A vote on key decisions.'),
         ru=dict(eye='ЧТО ВЫ ПОЛУЧАЕТЕ', title='Вашу долю<br>прибыли', body='Финансовый отчёт каждый месяц.<br>Голос в ключевых решениях.')),
    dict(key='6', video='baf1356a', start=10.0,
         en=dict(eye='REGISTERED SHARES · NOTARY · PT PMA', title='Talk to<br>the founders', body='Anna & Evgenii, in Bali since 2013.<br>Visit the spa before you decide.',
                 cta='TAP “LEARN MORE”', legal='Not a public offer. Profit varies. Capital at risk.'),
         ru=dict(eye='ДОЛИ У НОТАРИУСА · PT PMA', title='Поговорите<br>с основателями', body='Анна и Евгений, на Бали с 2013 года.<br>Посетите спа до решения.',
                 cta='НАЖМИТЕ «УЗНАТЬ БОЛЬШЕ»', legal='Не публичная оферта. Прибыль меняется. Капитал под риском.')),
]


def css(fmt):
    w, h = FORMATS[fmt]
    if fmt == 'reel':
        logo_top, text_top, title, ru_title, body, eye = 270, 620, 112, 96, 42, 30
    else:
        logo_top, text_top, title, ru_title, body, eye = 70, 330, 96, 80, 36, 26
    return """*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%dpx;height:%dpx;background:transparent}
.c{position:relative;width:%dpx;height:%dpx;overflow:hidden;font-family:Montserrat,sans-serif;color:#fff}
.shade{position:absolute;inset:0;background:linear-gradient(rgba(8,6,4,.6) 0%%,rgba(8,6,4,.3) 18%%,rgba(8,6,4,.72) 38%%,rgba(8,6,4,.82) 60%%,rgba(8,6,4,.55) 80%%,rgba(8,6,4,.35) 100%%)}
.logo{position:absolute;left:50%%;transform:translateX(-50%%);top:%dpx;width:180px;opacity:.95}
.t{position:absolute;left:70px;right:70px;top:%dpx;text-align:center}
.eye{font-size:%dpx;letter-spacing:.2em;font-weight:600;color:#F2C45C;margin-bottom:30px}
h1{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:%dpx;line-height:1.02;text-transform:uppercase;text-shadow:0 2px 24px rgba(0,0,0,.4)}
.ru h1{font-size:%dpx}
.line{width:120px;height:3px;background:#F2C45C;margin:34px auto}
p{font-size:%dpx;line-height:1.42;font-weight:400}
.cta{display:inline-block;margin-top:44px;background:#F2C45C;color:#14110D;font-size:30px;letter-spacing:.12em;font-weight:700;padding:28px 50px;border-radius:6px}
.legal{font-size:21px;color:rgba(255,255,255,.75);margin-top:26px}
""" % (w, h, w, h, logo_top, text_top, eye, title, ru_title, body)


def page(s, lang, fmt):
    t = s[lang]
    extra = ''
    if t.get('cta'):
        extra = '<div class="cta">%s →</div><div class="legal">%s</div>' % (t['cta'], t['legal'])
    return ('<!doctype html><html><head><meta charset="utf-8">'
            '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500&family=Montserrat:wght@400;600;700&display=swap&subset=cyrillic" rel="stylesheet">'
            '<style>%s</style></head><body><div class="c %s"><div class="shade"></div><img class="logo" src="file://%s/logo-white.png">'
            '<div class="t"><div class="eye">%s</div><h1>%s</h1><div class="line"></div><p>%s</p>%s</div></div></body></html>') % (
        css(fmt), lang, H, t['eye'], t['title'], t['body'], extra)


def overlays():
    os.makedirs(OV, exist_ok=True)
    jobs = []
    for fmt, (w, h) in FORMATS.items():
        for s in SCENES:
            for lang in ('en', 'ru'):
                f = '%s/%s-%s-%s.html' % (OV, fmt, s['key'], lang)
                open(f, 'w').write(page(s, lang, fmt))
                jobs.append(dict(html=f, w=w, h=h))
    json.dump(jobs, open(OV + '/jobs.json', 'w'))


def video():
    os.makedirs(H + '/out2', exist_ok=True)
    for fmt, (w, h) in FORMATS.items():
        for lang in ('en', 'ru'):
            parts = []
            for s in SCENES:
                src = glob.glob(U + '/*' + s['video'] + '*')[0]
                ov = '%s/%s-%s-%s.png' % (OV, fmt, s['key'], lang)
                out = '%s/scene-%s-%s-%s.mp4' % (OV, fmt, s['key'], lang)
                dur = DUR + (1.5 if s['key'] == '6' else 0)
                vf = ('[0:v]scale=%d:-2:flags=lanczos,crop=%d:%d,eq=contrast=1.05:saturation=1.08,unsharp=5:5:0.6,fps=30[v];'
                      '[1:v]format=rgba,fade=in:st=0.15:d=0.5:alpha=1[o];[v][o]overlay=0:0:shortest=1,'
                      'fade=in:st=0:d=0.2,fade=out:st=%s:d=0.25,format=yuv420p') % (w, w, h, dur - 0.25)
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(s['start']), '-i', src, '-loop', '1', '-i', ov,
                                '-filter_complex', vf, '-t', str(dur), '-an', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', out], check=True)
                parts.append(out)
            lst = '%s/list-%s-%s.txt' % (OV, fmt, lang)
            open(lst, 'w').write(''.join("file '%s'\n" % p for p in parts))
            final = '%s/out2/TFP-investors-%s-%s.mp4' % (H, fmt, lang.upper())
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo',
                            '-map', '0:v', '-map', '1:a', '-shortest', '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.1', '-pix_fmt', 'yuv420p',
                            '-r', '30', '-b:v', '6M', '-maxrate', '8M', '-bufsize', '16M', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', final], check=True)
            print(final)


if __name__ == '__main__':
    {'overlays': overlays, 'video': video}[sys.argv[1]]()
