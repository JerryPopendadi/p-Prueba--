"""Builds the paste-ready Ubud page. WordPress/Elementor can turn '&&' inside scripts into '&#038;&#038;',
which breaks the JavaScript; so the script is shipped base64-encoded (no '&', '<' or quotes for WordPress to touch).
Edit the-faces-ubud-invest-v2.src.html, then run: python3 build_ubud.py"""
import base64,re,os
d=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(d,'the-faces-ubud-invest-v2.src.html'),encoding='utf-8').read()
def enc(m):
    b=base64.b64encode(m.group(2).encode('utf-8')).decode()
    return m.group(1)+"(function(){var s=document.createElement('script');s.text=decodeURIComponent(escape(atob('"+b+"')));document.currentScript.parentNode.insertBefore(s,document.currentScript)})();</script>"
out,n=re.subn(r'(<script data-cfasync[^>]*>)(.*?)</script>',enc,s,flags=re.S)
assert n==1
open(os.path.join(d,'the-faces-ubud-invest-v2.html'),'w',encoding='utf-8').write(out)
print('built',len(out))
