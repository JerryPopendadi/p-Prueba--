"""Builds the-faces-waterfall-v2.src.html from the live v3 page (scratchpad wf_seg.html):
real THE FACES logo, Forminator 703 instead of the mailto form, PARTNERS wording, no prices."""
import re, os
D = os.path.dirname(os.path.abspath(__file__))
SEG = '/tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/peace2/wf_seg.html'
s = open(SEG, encoding='utf-8').read()
LOGO = 'https://thefacespeace.com/wp-content/uploads/2026/08/cropped-negro-logo-e1788874445128.png'
CAL = 'https://calendar.app.google/b7nddp1H5fBoGYT98'

def rep(old, new, count=1):
    global s
    assert s.count(old) >= 1, old[:80]
    s = s.replace(old, new) if count == 0 else s.replace(old, new, count)

# 1. split: markup + main script
i = s.rfind('<script>')
main_js = s[i + len('<script>'):s.rfind('</script>')]
s = s[:i]

# 2. old mailto form -> Forminator card
a = s.index('<div class="ap-f">') + len('<div class="ap-f">')
b = s.index('</script>\n</div>', a) + len('</script>\n</div>')
s = s[:a] + f'''
      <div class="fcard">
        <h3>Partnership request · WATERFALL</h3>
        <p class="small">About 1 minute. Confidential. Your details are never sold.</p>
        <div id="tf1-form-slot"><p class="fload">Loading the form…</p></div>
        <p class="fwait" id="tf1-form-wait" hidden><span>The form could not load. Write to us or book a call:</span> <a href="mailto:info@thefacespeace.com?subject=WATERFALL%20Bali%20partnership">info@thefacespeace.com</a> · <a href="{CAL}" target="_blank" rel="noopener" data-cal="missing">Book a private call</a></p>
        <ul class="trust"><li>Encrypted</li><li>Never sold</li><li>No obligation</li></ul>
        <div class="fdirect"><a data-tf="whatsapp" href="#tfw-contact">WhatsApp +62 823 2322 3433</a><a href="{CAL}" target="_blank" rel="noopener" data-cal="form">Prefer to book a call directly?</a></div>
      </div>''' + s[b:]

# 3. logo + PARTNERS wording, no INVEST
rep('<a href="#tfw-hero" class="brand">THE FACES<small>INVEST · WATERFALL</small></a>',
    f'<a href="#tfw-hero" class="brand"><img src="{LOGO}" alt="THE FACES" width="96" height="48"><small>PARTNERS · WATERFALL</small></a>')
rep('<span class="eb">THE FACES INVEST · WATERFALL</span>',
    f'<img class="cta-logo" src="{LOGO}" alt="THE FACES" width="150" height="75" loading="lazy"><span class="eb">THE FACES PARTNERS · WATERFALL</span>')
rep('<footer class="foot">\n  THE FACES INVEST · WATERFALL · BALI, INDONESIA',
    f'<footer class="foot">\n  <img class="foot-logo" src="{LOGO}" alt="THE FACES" width="110" height="55" loading="lazy"><br>THE FACES PARTNERS · WATERFALL · BALI, INDONESIA')
rep('<h3>THE FACES INVEST</h3>', '<h3>THE FACES PARTNERS</h3>')
rep('construction progress, founders and investor news', 'construction progress, founders and partner news', 0)
main_js = main_js.replace('construction progress, founders and investor news', 'construction progress, founders and partner news').replace('новости для инвесторов', 'новости для партнёров')
rep('discussed openly in the investor pack', 'discussed openly in the project pack')
rep('live video walkthroughs for investors abroad', 'live video walkthroughs for partners abroad')
rep('Investing involves risk, including possible loss of capital.', 'Any participation involves risk, including possible loss of capital.', 0)
rep('It is not a public offer, investment advice or a guarantee of returns. Investment terms are subject',
    'It is not a public offer, financial advice or a guarantee of returns. Partnership terms are subject')
rep('signed shareholder and investment agreements', 'signed shareholder and partnership agreements')
for w in ['$', 'USD', 'ROI', 'payback', '%</']:
    pass
rep('We do not publish investment amounts or returns.', 'We do not publish amounts or returns.')
main_js = main_js.replace('We do not publish investment amounts or returns.', 'We do not publish amounts or returns.')
# key numbers: 4 items -> 4 columns (was 5, left an empty column); market stats: 2 items -> 2 columns
rep('#tfw .kn-g{display:grid;grid-template-columns:repeat(5,1fr)}', '#tfw .kn-g{display:grid;grid-template-columns:repeat(4,1fr)}')
rep('<div class="g3">\n      <div class="stat"><b class="num">6.95M</b>', '<div class="g3 two">\n      <div class="stat"><b class="num">6.95M</b>')
# hero: second action books the call directly
rep('<a class="btn btn-ow" href="#tfw-project">See the project</a>',
    f'<a class="btn btn-ow" href="{CAL}" target="_blank" rel="noopener" data-cal="hero">Book a private call</a>')
# remove HTML comments (nothing bracket-like may reach Elementor)
s = re.sub(r'<!--.*?-->\n?', '', s, flags=re.S)

CSS = '''
#tfw .brand{display:inline-flex;align-items:center;gap:4px}
#tfw .brand img{height:40px;width:auto;display:block}
#tfw .cta-logo{display:block;height:64px;width:auto;margin:0 auto 26px;filter:invert(1)}
#tfw .foot-logo{height:46px;width:auto;margin:0 auto 14px;filter:invert(1);opacity:.9}
#tfw .g3.two{grid-template-columns:1fr 1fr;max-width:860px}
#tfw .fcard{background:#fff;border:1px solid var(--line);padding:clamp(22px,3vw,38px);box-shadow:0 20px 50px rgba(0,0,0,.08)}
#tfw .fcard h3{font-size:30px;margin:0 0 6px}
#tfw .fcard .small{font-size:13px;margin:0 0 20px}
#tfw #tf1-form-slot{min-height:120px}
#tfw #tf1-form-slot .forminator-ui.forminator-custom-form{margin:0!important;font-family:Montserrat,Arial,sans-serif!important}
#tfw #tf1-form-slot .forminator-row{margin-bottom:14px!important}
#tfw #tf1-form-slot .forminator-label{font-size:12px!important;font-weight:600!important;color:var(--ink)!important;margin-bottom:6px!important;letter-spacing:.3px}
#tfw #tf1-form-slot .forminator-input,#tfw #tf1-form-slot .forminator-textarea,#tfw #tf1-form-slot select,#tfw #tf1-form-slot .select2-selection{width:100%!important;min-height:50px!important;padding:12px 14px!important;border:1px solid var(--line)!important;border-radius:0!important;background:#fff!important;color:var(--ink)!important;font-size:16px!important;box-shadow:none!important}
#tfw #tf1-form-slot .forminator-input:focus,#tfw #tf1-form-slot .forminator-textarea:focus{border-color:var(--forest)!important;outline:2px solid rgba(38,58,48,.18)!important}
#tfw #tf1-form-slot .forminator-radio,#tfw #tf1-form-slot .forminator-checkbox{font-size:14px!important;color:var(--ink)!important}
#tfw #tf1-form-slot .forminator-button-submit{width:100%!important;min-height:56px!important;background:var(--forest)!important;border:0!important;color:#fff!important;border-radius:0!important;font:600 12px Montserrat,Arial,sans-serif!important;letter-spacing:.16em!important;text-transform:uppercase!important;cursor:pointer}
#tfw #tf1-form-slot .forminator-button-submit:hover{background:var(--forest2)!important}
#tfw #tf1-form-slot .forminator-error-message{font-size:12px!important;color:#b3261e!important}
#tfw #tf1-form-slot .forminator-response-message{font-size:14px!important}
#tfw .fload{display:flex;align-items:center;gap:10px;font-size:13px;color:var(--muted)}
#tfw .fload:before{content:"";width:18px;height:18px;border-radius:50%;border:2px solid var(--line);border-top-color:var(--forest);animation:tfwSpin 1s linear infinite}
@keyframes tfwSpin{to{transform:rotate(360deg)}}
#tfw .fwait{font-size:14px;color:var(--ink)}
#tfw .fwait a{text-decoration:underline}
#tfw .trust{list-style:none;padding:0;margin:16px 0 0;display:flex;flex-wrap:wrap;gap:8px 18px;font-size:12px;color:var(--muted)}
#tfw .trust li:before{content:"✓ ";color:var(--forest);font-weight:700}
#tfw .fdirect{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px 20px;margin-top:16px;padding-top:14px;border-top:1px solid var(--line);font-size:12.5px}
#tfw .fdirect a{border-bottom:1px solid var(--gold)}
#tfw .thanks{margin-top:16px;padding:22px;background:#E5EAE3;text-align:center}
#tfw .thanks p{color:var(--ink);margin:0 0 14px}
@media(max-width:600px){#tfw .g3.two{grid-template-columns:1fr}#tfw .brand img{height:34px}}
</style>'''
s = s.replace('</style>', CSS, 1)

FORM_JS = r'''
/* ---------- Forminator 703: move the site-wide copy of the form here and track the real conversion ---------- */
(function(){
  var root=document.getElementById('tfw');if(!root||root.dataset.formReady)return;root.dataset.formReady='1';
  var CFG={
    forminatorId:703,
    fields:{name:'name-1',email:'email-1',phone:'phone-1',country:'text-1',budget:'radio-1'},
    hidden:{lead_id:'hidden-1',language:'hidden-2',placement:'hidden-3',utm_source:'hidden-4',utm_medium:'hidden-5',utm_campaign:'hidden-6',gclid:'hidden-7',page:'hidden-8'},
    sheetUrl:'https://script.google.com/macros/s/AKfycbyPEJXBnZmt9cVSWmZcpf2ZONai3JsfcLjdKkD9bcdV3jdJDJnAtJ4Wg8id8qcQxXEBWQ/exec',
    calendar:'CALURL',
    interest:'project_waterfall'
  };
  var TX={
    en:{thanks:'Thank you! Your request has been received. You can already choose a time for your call:',book:'Book your call'},
    ru:{thanks:'Спасибо! Запрос получен. Уже сейчас можно выбрать время звонка:',book:'Записаться на звонок'},
    fr:{thanks:'Merci ! Votre demande a bien été reçue. Vous pouvez déjà choisir l’horaire de votre appel :',book:'Réserver mon appel'},
    id:{thanks:'Terima kasih! Permintaan Anda sudah kami terima. Anda sudah bisa memilih waktu panggilan:',book:'Jadwalkan panggilan'}
  };
  function lang(){return root.getAttribute('data-lang')||'en'}
  function tx(k){var l=TX[lang()]||TX.en;return l[k]||TX.en[k]}
  function q(s){return root.querySelector(s)}
  window.dataLayer=window.dataLayer||[];
  function track(ev,o){var d={event:ev,page:location.pathname,project:'waterfall'};for(var k in o)d[k]=o[k];window.dataLayer.push(d)}
  var attr={};
  try{var u=new URLSearchParams(location.search);['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','gbraid','wbraid'].forEach(function(k){var v=u.get(k);if(v)attr[k]=String(v).slice(0,150)});
    if(Object.keys(attr).length)sessionStorage.setItem('tf_attr',JSON.stringify(attr));else attr=JSON.parse(sessionStorage.getItem('tf_attr')||'{}')}catch(e){}
  var lastGo='';
  root.addEventListener('click',function(e){var a=e.target.closest?e.target.closest('a'):null;if(!a)return;
    if(a.hasAttribute('data-go'))lastGo=a.getAttribute('data-go');
    if(a.hasAttribute('data-cal'))track('thefaces_booking_click',{placement:a.getAttribute('data-cal'),link_url:CFG.calendar})},true);

  function findForm(){return document.querySelector('#tf-form-703-src form.forminator-custom-form')||document.querySelector('form.forminator-custom-form[data-form-id="'+CFG.forminatorId+'"]')||document.querySelector('#forminator-module-'+CFG.forminatorId)}
  function fEl(f,key){var n=CFG.fields[key]||CFG.hidden[key];if(!n||!f)return null;return f.querySelector('[name="'+n+'"]')||f.querySelector('[name^="'+n+'-"]')}
  function fVal(f,key){var el=fEl(f,key);if(!el)return '';
    if(el.type==='radio'||el.type==='checkbox'){var c=f.querySelector('[name="'+el.name+'"]:checked');return c?c.value:''}
    if(key==='name'){if(el.name!==CFG.fields.name)return [].map.call(f.querySelectorAll('[name^="'+CFG.fields.name+'-"]'),function(x){return x.value}).join(' ').trim()}
    return String(el.value||'').trim()}
  var pending=null,tries=0;
  var iv=setInterval(function(){var f=findForm();
    if(f){clearInterval(iv);var slot=q('#tf1-form-slot');slot.innerHTML='';slot.appendChild(f);wire(f)}
    else{tries++;if(tries>40){clearInterval(iv);var s=q('#tf1-form-slot');if(s)s.innerHTML='';var w=q('#tf1-form-wait');if(w)w.hidden=false;track('thefaces_form_missing',{form_id:CFG.forminatorId})}}},250);
  function wire(f){
    if(f.dataset.wfWired)return;f.dataset.wfWired='1';
    f.addEventListener('focusin',function(){if(!f.dataset.wfStart){f.dataset.wfStart='1';track('thefaces_form_start',{form_id:CFG.forminatorId,placement:'waterfall'})}});
    f.addEventListener('submit',function(){
      var em=fVal(f,'email'),nm=fVal(f,'name');
      if(!/^[^\s@<>"'()]+@[^\s@<>"'()]+\.[a-z]{2,}$/i.test(em)||nm.replace(/\s/g,'').length<2){track('thefaces_form_error',{field:em?'name':'email'});return}
      var id='lead-'+Date.now()+'-'+Math.random().toString(36).slice(2,8);
      var hv={lead_id:id,language:lang(),placement:'waterfall_'+(lastGo||'form'),page:location.href.split('#')[0].slice(0,250)};for(var k in attr)hv[k]=attr[k];
      Object.keys(CFG.hidden).forEach(function(k){var el=fEl(f,k);if(el){if(hv[k]!==undefined)el.value=hv[k]}});
      pending={lead_id:id,name:nm,email:em,phone:fVal(f,'phone'),country:fVal(f,'country'),budget:fVal(f,'budget'),hv:hv};
    },true);
    function done(){if(!pending)return;var d=pending;pending=null;
      /* the conversion: GTM trigger generate_lead -> Google Ads "Investor enquiry - Forminator 703" */
      track('generate_lead',{lead_id:d.lead_id,form_id:'forminator_'+CFG.forminatorId,lead_method:'forminator',interest:CFG.interest,budget:d.budget||'not_given',country:d.country||'',
        form_language:lang(),placement:d.hv.placement,page_path:location.pathname,value:0,currency:'USD'});
      /* the Google Sheet row */
      var F=CFG.fields,H=CFG.hidden,row={};
      row[F.name]=d.name;row[F.email]=d.email;if(d.phone)row[F.phone]=d.phone;if(d.country)row[F.country]=d.country;if(d.budget)row[F.budget]=d.budget;
      row['Interest']=CFG.interest;
      Object.keys(H).forEach(function(k){if(d.hv[k]!==undefined)row[H[k]]=d.hv[k]});
      try{fetch(CFG.sheetUrl,{method:'POST',mode:'no-cors',keepalive:true,body:new URLSearchParams(row)})}catch(x){}
      var slot=q('#tf1-form-slot');if(slot){if(!slot.querySelector('.thanks')){var th=document.createElement('div');th.className='thanks';
        th.innerHTML='<p></p><a class="btn" target="_blank" rel="noopener" data-cal="after_lead"></a>';th.querySelector('p').textContent=tx('thanks');
        var a=th.querySelector('a');a.href=CFG.calendar;a.textContent=tx('book');slot.appendChild(th)}}
    }
    if(window.jQuery){var J=window.jQuery;
      J(document).on('forminator:form:submit:success',function(e){if(e.target===f||J(e.target).closest(f).length)done()});
      J(document).on('forminator:form:submit:failed',function(e){if(e.target===f||J(e.target).closest(f).length){if(pending)track('thefaces_form_fail',{form_id:CFG.forminatorId});pending=null}})}
    try{new MutationObserver(function(){if(pending){if(f.querySelector('.forminator-response-message.forminator-success,.forminator-success'))done()}}).observe(f,{subtree:true,childList:true,attributes:true,attributeFilter:['class']})}catch(e){}
  }
})();
'''.replace('CALURL', CAL)

# main script: remove the && (Elementor turns them into entities); it is base64-shipped anyway
main_js = main_js.replace("if(n.parentNode.closest && n.parentNode.closest('#tff')) return NodeFilter.FILTER_REJECT;",
                          "if(n.parentNode.closest){ if(n.parentNode.closest('#tf1-form-slot')) return NodeFilter.FILTER_REJECT; }")
main_js = main_js.replace("if(fab && hero) fab.classList", "if(fab) if(hero) fab.classList")
main_js = main_js.replace('emailSubject: "WATERFALL Bali — partnership enquiry"', 'emailSubject: "WATERFALL Bali - partnership enquiry"')
main_js = re.sub(r'(adsConversion:\s*\{[^}]*\})', r'\1', main_js)

s = s.rstrip() + '\n\n<script data-cfasync="false" data-no-optimize="1" data-no-defer="1" data-nowprocket data-noptimize="1">\n' + main_js.strip() + '\n' + FORM_JS + '</script>\n'
open(os.path.join(D, 'the-faces-waterfall-v2.src.html'), 'w', encoding='utf-8').write(s)
markup = s[:s.index('<script data-cfasync')]
print('ok', len(s), 'invest words in markup:', re.findall(r'[^\n]{0,40}\b[Ii]nvest\w*[^\n]{0,30}', markup))
print('prices:', re.findall(r'\$\s?\d[\d,.]*\s?[KkMm]?', markup))
