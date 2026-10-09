// Capturas de la solución de la Parte B del examen final, a 1440 y a 390.
// La página completa va a la ficha técnica; la primera pantalla, a las diapositivas de la sesión 16.
// uso: node shot_ef.js <carpeta-solucion> <salida> [<carpeta-img-de-diapositivas>]
const { chromium } = require('playwright');
const path = require('path');
const { routeFonts, serve } = require('../herramientas/shot.js');
(async () => {
  const [dir, out, deck] = process.argv.slice(2);
  const srv = await serve(dir, 8995);
  const b = await chromium.launch();
  for (const [w, sc] of [[1440, 1], [390, 2]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: w === 390 ? 844 : 900 }, deviceScaleFactor: sc });
    await routeFonts(ctx);
    const p = await ctx.newPage();
    await p.goto('http://127.0.0.1:8995/index.html', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    await p.screenshot({ path: path.join(out, `ef-parte-b-${w}.png`), fullPage: true });
    if (deck) await p.screenshot({ path: path.join(deck, `s16-parte-b-${w}.png`) });
    console.log(w, 'scrollWidth', sw);
    await ctx.close();
  }
  await b.close(); srv.kill();
})();
