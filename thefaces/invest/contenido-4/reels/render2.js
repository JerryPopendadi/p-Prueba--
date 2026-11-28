const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();
for(const j of JSON.parse(fs.readFileSync(process.argv[2]))){const p=await b.newPage({viewport:{width:j.w,height:j.h}});await p.goto('file://'+j.html);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(250);
await p.screenshot({path:j.html.replace('.html','.png'),omitBackground:true});await p.close();}
await b.close()})();
