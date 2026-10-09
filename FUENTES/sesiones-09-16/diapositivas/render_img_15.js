// Imágenes de las diapositivas de la sesión 15: el sitio completo, la 404, el aviso de envío,
// el enlace para saltar al contenido, el icono, la vista previa al compartir y Lighthouse.
// uso: node render_img_15.js <repo> <informe-lighthouse.html>
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { routeFonts, serve } = require('../herramientas/shot.js');
const REPO = process.argv[2] || '/home/user/sesiones-dagner';
const LH = process.argv[3];
const OUT = path.join(__dirname, 'img');
fs.mkdirSync(OUT, { recursive: true });
const P15 = path.join(REPO, 'SESION 15', 'mi-portafolio-dagner');
const demo = (f) => 'file://' + path.join(__dirname, 'demos', f);

async function contexto(b, w, h, scale) {
  const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: scale });
  await routeFonts(ctx);
  return ctx;
}
async function ir(p, url) {
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
}

(async () => {
  // la imagen para compartir, tal como está en el sitio
  fs.copyFileSync(path.join(P15, 'assets', 'img', 'og-portafolio.png'), path.join(OUT, 's15-og.png'));
  const b = await chromium.launch();
  const port = 8990;
  const srv = await serve(P15, port);
  const url = (f) => `http://127.0.0.1:${port}/${f}`;

  // las cinco páginas a 1440 y a 390
  let ctx = await contexto(b, 1440, 900, 1);
  let p = await ctx.newPage();
  for (const f of ['index', 'sobre-mi', 'mis-proyectos', 'cursos', 'contactame', '404', 'gracias']) {
    await ir(p, url(f + '.html'));
    await p.screenshot({ path: path.join(OUT, `s15-p-${f}.png`) });
  }
  await ctx.close();

  // la página actual del menú, con escala 2
  ctx = await contexto(b, 1440, 300, 2);
  p = await ctx.newPage();
  await ir(p, url('sobre-mi.html'));
  const nav = await p.evaluate(() => { const r = document.querySelector('header').getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height }; });
  await p.screenshot({ path: path.join(OUT, 's15-actual.png'), clip: { x: 420, y: 0, width: 1020, height: nav.height } });
  // el enlace «Saltar al contenido»: aparece con el primer Tab
  await p.keyboard.press('Tab');
  await p.waitForTimeout(300);
  await p.screenshot({ path: path.join(OUT, 's15-saltar.png'), clip: { x: 0, y: 0, width: 1440, height: nav.height + 40 } });
  await ctx.close();

  ctx = await contexto(b, 390, 844, 2);
  p = await ctx.newPage();
  for (const f of ['index', '404']) {
    await ir(p, url(f + '.html'));
    await p.screenshot({ path: path.join(OUT, `s15-m-${f}.png`) });
  }
  await ctx.close();
  srv.kill();

  // demostraciones: la pestaña y la vista previa al compartir
  ctx = await contexto(b, 1100, 800, 2);
  p = await ctx.newPage();
  for (const f of ['pestana', 'compartir']) {
    await ir(p, demo(f + '.html'));
    const r = await p.evaluate(() => ({ w: Math.ceil(document.body.getBoundingClientRect().width), h: Math.ceil(document.body.scrollHeight) }));
    await p.screenshot({ path: path.join(OUT, `s15-${f}.png`), clip: { x: 0, y: 0, width: r.w, height: r.h } });
  }
  await ctx.close();

  // las cuatro notas de Lighthouse, del informe HTML real
  if (LH) {
    ctx = await b.newContext({ viewport: { width: 1000, height: 900 }, deviceScaleFactor: 2 });
    p = await ctx.newPage();
    await p.goto('file://' + path.resolve(LH), { waitUntil: 'load' });
    await p.waitForSelector('.lh-scores-header');
    await p.waitForTimeout(1500);
    await p.locator('.lh-scores-header').first().screenshot({ path: path.join(OUT, 's15-lighthouse.png') });
    await ctx.close();
  }
  await b.close();
  console.log('listo');
})();
