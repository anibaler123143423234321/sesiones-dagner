// Imágenes del sitio publicado (sesión 15): favicon, icono del celular y vista previa Open Graph.
// uso: node render.js <carpeta-img-destino>
const { chromium } = require('playwright');
const path = require('path');
const { execFileSync } = require('child_process');
const { routeFonts } = require('../herramientas/shot.js');
const OUT = process.argv[2];
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1200, height: 630 } });
  await routeFonts(ctx);
  const p = await ctx.newPage();
  // icono: 512 px, después se reduce a 180 y a 32
  await p.goto('file://' + path.join(__dirname, 'icono.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const tmp = path.join(__dirname, 'icono-512.png');
  await p.locator('.i').screenshot({ path: tmp, omitBackground: true });
  execFileSync('convert', [tmp, '-resize', '32x32', path.join(OUT, 'favicon-32.png')]);
  // el icono del celular: cuadrado completo, sin esquinas transparentes (el sistema las redondea)
  await p.evaluate(() => document.querySelector('.i').style.setProperty('--r', '0'));
  await p.locator('.i').screenshot({ path: tmp });
  execFileSync('convert', [tmp, '-resize', '180x180', path.join(OUT, 'apple-touch-icon.png')]);
  // la vista previa al compartir: 1200 × 630
  await p.goto('file://' + path.join(__dirname, 'og.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: path.join(OUT, 'og-portafolio.png') });
  await b.close();
  console.log('listo');
})();
