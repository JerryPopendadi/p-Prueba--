import json, sys, subprocess, os
from slides import SLIDES
H = os.path.dirname(os.path.abspath(__file__))
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:transparent}
.c{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:Montserrat,sans-serif;color:#fff}
.top{position:absolute;left:0;right:0;top:0;height:260px;background:linear-gradient(rgba(8,6,4,.55),rgba(8,6,4,0))}
.logo{position:absolute;left:64px;top:58px;width:150px;opacity:.92}
.bot{position:absolute;left:0;right:0;bottom:0;height:760px;background:linear-gradient(rgba(10,8,6,0),rgba(10,8,6,.62) 38%,rgba(10,8,6,.9))}
.t{position:absolute;left:72px;right:72px;bottom:84px}
.eye{font-size:23px;letter-spacing:.24em;font-weight:500;color:#F2C45C;margin-bottom:22px}
h1{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:84px;line-height:1.02;letter-spacing:.01em;text-transform:uppercase;margin-bottom:26px}
.line{width:96px;height:2px;background:#F2C45C;margin-bottom:26px;opacity:.9}
p{font-size:31px;line-height:1.42;font-weight:300;color:rgba(255,255,255,.92);margin-bottom:38px}
.btn{display:inline-block;background:#F1ECE3;color:#14110D;font-size:22px;letter-spacing:.16em;font-weight:600;padding:24px 40px;border-radius:4px}
.btn b{font-weight:600;margin-left:12px}
ol{list-style:none;margin:0 0 26px}
ol li{font-size:30px;font-weight:300;line-height:1.3;padding:13px 0;border-top:1px solid rgba(255,255,255,.18);display:flex;gap:22px}
ol li span{color:#F2C45C;font-weight:500;width:28px}
.how h1{font-size:68px}
.how .bot{height:1150px;background:linear-gradient(rgba(10,8,6,0),rgba(10,8,6,.78) 30%,rgba(10,8,6,.93))}
.legal{font-size:17px;color:rgba(255,255,255,.62);margin-top:22px;letter-spacing:.02em}
.ru h1{font-size:72px}.ru.how h1{font-size:56px}
"""
def html(s, lang):
    t = s[lang]
    steps = ''.join('<li><span>%d</span>%s</li>' % (i+1, x) for i, x in enumerate(t.get('steps', [])))
    cls = 'c ' + lang + (' how' if steps else '')
    body = '<p>%s</p>' % t['body'] if t.get('body') else ''
    return ('<!doctype html><html><head><meta charset="utf-8">'
      '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Montserrat:wght@300;500;600&display=swap&subset=cyrillic" rel="stylesheet">'
      '<style>%s</style></head><body><div class="%s"><div class="top"></div><img class="logo" src="file://%s/logo-white.png"><div class="bot"></div>'
      '<div class="t"><div class="eye">%s</div><h1>%s</h1><div class="line"></div>%s%s'
      '<div class="btn">%s<b>→</b></div>%s</div></div></body></html>') % (
      CSS, cls, H, t['eye'], t['title'], ('<ol>%s</ol>' % steps) if steps else '', body, t['btn'],
      ('<div class="legal">%s</div>' % t['legal']) if t.get('legal') else '')
os.makedirs(H + '/_ov', exist_ok=True)
jobs = []
for s in SLIDES:
    for lang in ('en', 'ru'):
        f = '%s/_ov/%s-%s.html' % (H, s['key'], lang)
        open(f, 'w').write(html(s, lang)); jobs.append(f)
json.dump(jobs, open(H + '/_ov/jobs.json', 'w'))
