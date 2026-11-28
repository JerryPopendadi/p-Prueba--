const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const f of JSON.parse(fs.readFileSync(process.argv[2]))){await p.goto('file://'+f);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:f.replace('.html','.png'),omitBackground:true});}
await b.close()})();
