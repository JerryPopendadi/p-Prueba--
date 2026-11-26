// Renders out/*.html to print PDF (exact size with bleed) and PNG previews.
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ deviceScaleFactor: 3 });
  for (const j of JSON.parse(fs.readFileSync(process.argv[2]))) {
    await p.goto('file://' + j.html);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(500);
    await p.pdf({ path: j.html.replace('.html', '.pdf'), width: j.w, height: j.h, printBackground: true });
    const els = await p.$$('.pg');
    for (let i = 0; i < els.length; i++) {
      const suffix = els.length > 1 ? (i ? '-back' : '-front') : '';
      await els[i].screenshot({ path: j.html.replace('.html', suffix + '.png') });
    }
  }
  await b.close();
})();
