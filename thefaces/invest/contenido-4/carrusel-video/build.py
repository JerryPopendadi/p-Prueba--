import subprocess, glob, os, sys
from slides import SLIDES
U = '/root/.claude/uploads/da6eeaca-3a38-54c2-b2cc-cd456339a57d'
H = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else 'video'
os.makedirs(H + '/out', exist_ok=True)
for s in SLIDES:
    src = glob.glob(U + '/*' + s['video'] + '*')[0]
    dur = 10 if s['key'] == '06-how' else 8
    grade = 'eq=contrast=1.05:saturation=1.08,unsharp=5:5:0.6'
    base = ('[0:v]setpts=%s*PTS,scale=1080:-2:flags=lanczos,crop=1080:1350:0:%d,%s,fps=30[v];' % (s['speed'], s['y'], grade))
    for lang in ('en', 'ru'):
        ov = '%s/_ov/%s-%s.png' % (H, s['key'], lang)
        if mode == 'still':
            out = '%s/_ov/prev-%s-%s.jpg' % (H, s['key'], lang)
            cmd = ['ffmpeg','-v','error','-y','-ss',str(s['start']+1),'-i',src,'-i',ov,'-filter_complex',base+'[v][1:v]overlay=0:0','-frames:v','1','-q:v','3',out]
        else:
            out = '%s/out/TFP-%s-%s.mp4' % (H, lang.upper(), s['key'])
            cmd = ['ffmpeg','-v','error','-y','-ss',str(s['start']),'-i',src,'-loop','1','-i',ov,'-filter_complex',
                   base+'[1:v]format=rgba,fade=in:st=0.3:d=0.7:alpha=1[o];[v][o]overlay=0:0:shortest=1,fade=out:st=%s:d=0.4,format=yuv420p' % (dur-0.4),
                   '-t',str(dur),'-an','-c:v','libx264','-preset','slow','-crf','18','-profile:v','high','-movflags','+faststart',out]
        subprocess.run(cmd, check=True); print(out)
