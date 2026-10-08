const { chromium } = require('playwright');
const { routeFonts } = require('../herramientas/shot.js');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 628, height: 220 }, deviceScaleFactor: 2 });
  await routeFonts(ctx);
  const p = await ctx.newPage();
  for (const [src, out] of [['cinf.html', 'proyecto-cinf.jpg'], ['cert.html', 'proyecto-certificados.jpg']]) {
    await p.goto('file://' + __dirname + '/' + src, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: __dirname + '/' + out, type: 'jpeg', quality: 82 });
  }
  await b.close();
})();
