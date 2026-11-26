"""THE FACES PARTNERS · Instagram/Facebook Reels ad (9:16, 1080x1920), EN + RU.

One ~27 s video per language: 6 scenes, text kept inside the Reels safe zone
(top ~250 px and bottom ~650 px are covered by the Instagram UI).
Run: python3 reel.py overlays && node ../carrusel-video/render.js _ov/jobs.json && python3 reel.py video
"""
import glob
import json
import os
import subprocess
import sys

H = os.path.dirname(os.path.abspath(__file__))
U = '/root/.claude/uploads/da6eeaca-3a38-54c2-b2cc-cd456339a57d'
DUR = 4.5

# video id, start second, speed, crop y in the 1080x1974 frame
SCENES = [
    dict(key='1', video='29d1cbad', start=0.0, speed=1.0, y=30,
         en=dict(eye='THE FACES · BALI SINCE 2013', title='Own part of<br>a spa in Bali', body='Without running it yourself.'),
         ru=dict(eye='THE FACES · НА БАЛИ С 2013 ГОДА', title='Доля в спа<br>на Бали', body='Без необходимости управлять самому.')),
    dict(key='2', video='76f6e149', start=7.0, speed=1.0, y=40,
         en=dict(eye='THE FACES UBUD · OPERATING', title='Already open.<br>Real guests.', body='Guests every day, an experienced team.'),
         ru=dict(eye='THE FACES UBUD · РАБОТАЕТ', title='Уже работает.<br>Реальные гости.', body='Гости каждый день, опытная команда.')),
    dict(key='3', video='dc5df73d', start=2.0, speed=1.0, y=40,
         en=dict(eye='THE WHITE TEMPLE · SANUR', title='Steam. Foam.<br>Light. Silence.', body='Our ritual spa, renovation under way.'),
         ru=dict(eye='THE WHITE TEMPLE · САНУР', title='Пар. Пена.<br>Свет. Тишина.', body='Ритуальный спа, идёт ремонт.')),
    dict(key='4', video='54573c64', start=0.0, speed=1.0, y=40,
         en=dict(eye='WATERFALL · UBUD', title='Join at the<br>build stage', body='Carved stone rooms by the jungle.'),
         ru=dict(eye='WATERFALL · УБУД', title='Вход на этапе<br>строительства', body='Залы из резного камня у джунглей.')),
    dict(key='5', video='270d6a31', start=4.0, speed=1.0, y=60,
         en=dict(eye='HOW IT WORKS', title='We run it.<br>You own it.', body='Monthly reports. A vote on key decisions.'),
         ru=dict(eye='КАК ЭТО РАБОТАЕТ', title='Мы управляем.<br>Вы владеете.', body='Отчёт каждый месяц. Голос в ключевых решениях.')),
    dict(key='6', video='baf1356a', start=10.0, speed=1.0, y=40,
         en=dict(eye='UP TO 49% · SHARES AT A NOTARY', title='Meet the<br>founders first', body='Visit the spa. See the documents.<br>Then decide.',
                 cta='TAP “LEARN MORE”', legal='Information only, not a public offer. Capital at risk.'),
         ru=dict(eye='ДОЛЯ ДО 49% · У НОТАРИУСА', title='Сначала<br>познакомимся', body='Посетите спа. Посмотрите документы.<br>Потом решайте.',
                 cta='НАЖМИТЕ «УЗНАТЬ БОЛЬШЕ»', legal='Только информация, не публичная оферта. Капитал под риском.')),
]

CSS = """*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;background:transparent}
.c{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Montserrat,sans-serif;color:#fff}
.shade{position:absolute;inset:0;background:linear-gradient(rgba(8,6,4,.55) 0%,rgba(8,6,4,.15) 18%,rgba(8,6,4,.55) 34%,rgba(8,6,4,.78) 52%,rgba(8,6,4,.55) 68%,rgba(8,6,4,.3) 100%)}
.logo{position:absolute;left:50%;transform:translateX(-50%);top:270px;width:190px;opacity:.95}
.t{position:absolute;left:80px;right:80px;top:640px;text-align:center}
.eye{font-size:30px;letter-spacing:.22em;font-weight:500;color:#F2C45C;margin-bottom:34px}
h1{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:112px;line-height:1.02;text-transform:uppercase;text-shadow:0 2px 24px rgba(0,0,0,.35)}
.line{width:120px;height:3px;background:#F2C45C;margin:40px auto}
p{font-size:42px;line-height:1.4;font-weight:300}
.cta{display:inline-block;margin-top:52px;background:#F1ECE3;color:#14110D;font-size:32px;letter-spacing:.14em;font-weight:600;padding:30px 52px;border-radius:6px}
.legal{font-size:22px;color:rgba(255,255,255,.7);margin-top:30px}
.ru h1{font-size:96px}
"""


def page(s, lang):
    t = s[lang]
    extra = ''
    if t.get('cta'):
        extra = '<div class="cta">%s →</div><div class="legal">%s</div>' % (t['cta'], t['legal'])
    return ('<!doctype html><html><head><meta charset="utf-8">'
            '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Montserrat:wght@300;500;600&display=swap&subset=cyrillic" rel="stylesheet">'
            '<style>%s</style></head><body><div class="c %s"><div class="shade"></div><img class="logo" src="file://%s/logo-white.png">'
            '<div class="t"><div class="eye">%s</div><h1>%s</h1><div class="line"></div><p>%s</p>%s</div></div></body></html>') % (
        CSS, lang, H, t['eye'], t['title'], t['body'], extra)


def overlays():
    os.makedirs(H + '/_ov', exist_ok=True)
    jobs = []
    for s in SCENES:
        for lang in ('en', 'ru'):
            f = '%s/_ov/%s-%s.html' % (H, s['key'], lang)
            open(f, 'w').write(page(s, lang))
            jobs.append(f)
    json.dump(jobs, open(H + '/_ov/jobs.json', 'w'))


def video():
    os.makedirs(H + '/out', exist_ok=True)
    for lang in ('en', 'ru'):
        parts = []
        for s in SCENES:
            src = glob.glob(U + '/*' + s['video'] + '*')[0]
            ov = '%s/_ov/%s-%s.png' % (H, s['key'], lang)
            out = '%s/_ov/scene-%s-%s.mp4' % (H, s['key'], lang)
            dur = DUR + (1.5 if s['key'] == '6' else 0)
            vf = ('[0:v]setpts=%s*PTS,scale=1080:-2:flags=lanczos,crop=1080:1920:0:%d,eq=contrast=1.05:saturation=1.08,unsharp=5:5:0.6,fps=30[v];'
                  '[1:v]format=rgba,fade=in:st=0.15:d=0.5:alpha=1[o];[v][o]overlay=0:0:shortest=1,'
                  'fade=in:st=0:d=0.2,fade=out:st=%s:d=0.25,format=yuv420p') % (s['speed'], s['y'], dur - 0.25)
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(s['start']), '-i', src, '-loop', '1', '-i', ov,
                            '-filter_complex', vf, '-t', str(dur), '-an', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', out], check=True)
            parts.append(out)
        lst = '%s/_ov/list-%s.txt' % (H, lang)
        open(lst, 'w').write(''.join("file '%s'\n" % p for p in parts))
        final = '%s/out/THE-FACES-PARTNERS-reel-%s.mp4' % (H, lang.upper())
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst,
                        '-c', 'copy', '-movflags', '+faststart', final], check=True)
        print(final)


if __name__ == '__main__':
    {'overlays': overlays, 'video': video}[sys.argv[1]]()
