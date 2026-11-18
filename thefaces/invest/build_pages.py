"""Builds the paste-ready pages. WordPress/Elementor can turn '&&' inside scripts into '&#038;&#038;',
which breaks the JavaScript; so each page script is shipped base64-encoded (no '&', '<' or quotes for WordPress to touch).
Edit the *.src.html file, then run: python3 build_pages.py"""
import base64,re,os
d=os.path.dirname(os.path.abspath(__file__))
PAGES=['the-faces-ubud-invest-v2','the-faces-hotels-v7','the-faces-invest-hub-v2','the-faces-invest-global-v2','the-faces-book-meeting-v2','the-faces-waterfall-v2','the-faces-partners-landing']
def enc(m):
    b=base64.b64encode(m.group(2).encode('utf-8')).decode()
    return m.group(1)+"(function(){var s=document.createElement('script');s.text=decodeURIComponent(escape(atob('"+b+"')));var c=document.currentScript;if(c){if(c.parentNode){c.parentNode.insertBefore(s,c);return}}(document.body||document.documentElement).appendChild(s)})();</script>"
for p in PAGES:
    s=open(os.path.join(d,p+'.src.html'),encoding='utf-8').read()
    out,n=re.subn(r'(<script data-cfasync[^>]*>)(.*?)</script>',enc,s,flags=re.S)
    assert n==1,p
    assert '&&' not in out,p
    open(os.path.join(d,p+'.html'),'w',encoding='utf-8').write(out)
    print('built',p,len(out))
