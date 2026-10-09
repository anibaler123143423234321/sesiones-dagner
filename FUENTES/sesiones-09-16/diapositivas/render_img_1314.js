// Imágenes de las diapositivas de las sesiones 13 y 14: demostraciones de Bootstrap y capturas de la página Cursos.
// uso: node render_img_1314.js <repo> [demos|s13|s14]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { routeFonts, serve } = require('../herramientas/shot.js');
const REPO = process.argv[2] || '/home/user/sesiones-dagner';
const OUT = path.join(__dirname, 'img');
fs.mkdirSync(OUT, { recursive: true });
const P13 = path.join(REPO, 'SESION 13', 'mi-portafolio-dagner');
const P14 = path.join(REPO, 'SESION 14', 'mi-portafolio-dagner');
const demo = (f) => 'file://' + path.join(__dirname, 'demos', f);

async function ajustada(p, file, out) {
  await p.goto(demo(file), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => { const b = document.body.getBoundingClientRect(); return { w: Math.ceil(b.width), h: Math.ceil(document.body.scrollHeight) }; });
  await p.setViewportSize({ width: r.w, height: Math.max(r.h, 100) });
  await p.screenshot({ path: path.join(OUT, out), clip: { x: 0, y: 0, width: r.w, height: r.h } });
  console.log('demo', out, r);
}

async function demos(b) {
  const ctx = await b.newContext({ viewport: { width: 1000, height: 800 }, deviceScaleFactor: 2 });
  await routeFonts(ctx);
  const p = await ctx.newPage();
  for (const f of ['bs-grilla', 'bs-gutters', 'bs-offset', 'bs-espaciado']) {
    await p.setViewportSize({ width: 1000, height: 800 });
    await ajustada(p, f + '.html', f + '.png');
  }
  await p.setViewportSize({ width: 1200, height: 300 });
  await p.goto(demo('bs-container.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const h = await p.evaluate(() => document.body.scrollHeight);
  await p.screenshot({ path: path.join(OUT, 'bs-container.png'), clip: { x: 0, y: 0, width: 1200, height: h } });
  await ctx.close();
  // la barra de navegación: celular cerrada, celular abierta y escritorio
  for (const [w, abrir, out] of [[390, false, 'bs-navbar-cerrada.png'], [390, true, 'bs-navbar-abierta.png'], [1200, false, 'bs-navbar-escritorio.png']]) {
    const c = await b.newContext({ viewport: { width: w, height: 300 }, deviceScaleFactor: 2 });
    await routeFonts(c);
    const pg = await c.newPage();
    await pg.goto(demo('bs-navbar.html'), { waitUntil: 'networkidle' });
    await pg.evaluate(() => document.fonts.ready);
    if (abrir) { await pg.click('.navbar-toggler'); await pg.waitForTimeout(600); }
    const alto = await pg.evaluate(() => Math.ceil(document.querySelector('nav').getBoundingClientRect().bottom) + 12);
    await pg.screenshot({ path: path.join(OUT, out), clip: { x: 0, y: 0, width: w, height: alto } });
    await c.close();
  }
}

async function pagina(b, dir, port, o = {}) {
  const srv = await serve(dir, port);
  const ctx = await b.newContext({ viewport: { width: o.w || 1440, height: o.h || 900 }, deviceScaleFactor: o.scale || 1.5 });
  await routeFonts(ctx);
  if (o.sinTema) await ctx.route(/tema-bootstrap\.css$/, (r) => r.fulfill({ status: 200, contentType: 'text/css', body: '' }));
  const p = await ctx.newPage();
  await p.goto(`http://127.0.0.1:${port}/cursos.html`, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  return { p, close: async () => { await ctx.close(); srv.kill(); } };
}

const caja = (p, sel) => p.evaluate((sel) => { const r = document.querySelector(sel).getBoundingClientRect(); return { x: r.x, y: r.y + window.scrollY, width: r.width, height: r.height }; }, sel);
const seccion = (id) => `section[aria-labelledby="${id}"]`;

// las 12 columnas de la guía de Figma sobre la página: Margen 80, Medianil 24
async function columnas(p) {
  await p.addStyleTag({ content: `.guia12{position:absolute;left:0;right:0;top:0;pointer-events:none;z-index:50;display:flex;gap:24px;padding:0 80px;max-width:1440px;margin:0 auto}
    .guia12 span{flex:1;background:rgba(255,0,0,.10);border-left:1px solid rgba(255,0,0,.25);border-right:1px solid rgba(255,0,0,.25)}` });
  await p.evaluate(() => { const g = document.createElement('div'); g.className = 'guia12'; g.style.height = document.body.scrollHeight + 'px'; for (let i = 0; i < 12; i++) g.appendChild(document.createElement('span')); document.body.appendChild(g); });
}

async function sesion13(b) {
  let port = 8950;
  let s = await pagina(b, P13, ++port, { w: 1440, h: 900, scale: 1 });
  await s.p.screenshot({ path: path.join(OUT, 's13-cursos-1440.png') });
  await s.p.screenshot({ path: path.join(OUT, 's13-intro.png'), clip: await caja(s.p, seccion('titulo-cursos')) });
  await columnas(s.p);
  const cat = await caja(s.p, seccion('titulo-catalogo'));
  await s.p.screenshot({ path: path.join(OUT, 's13-columnas.png'), clip: { x: 0, y: cat.y - 20, width: 1440, height: cat.height + 40 }, fullPage: true });
  const ll = await caja(s.p, seccion('titulo-llamado'));
  await s.p.screenshot({ path: path.join(OUT, 's13-columnas-llamado.png'), clip: { x: 0, y: ll.y - 20, width: 1440, height: ll.height + 40 }, fullPage: true });
  const pa = await caja(s.p, seccion('titulo-pasos'));
  await s.p.screenshot({ path: path.join(OUT, 's13-columnas-pasos.png'), clip: { x: 0, y: pa.y - 20, width: 1440, height: pa.height + 40 }, fullPage: true });
  await s.close();

  // el catálogo en tres anchos: lo que se ve en la pantalla
  for (const [w, h, sc, out] of [[1440, 900, 1, 's13-cat-1440.png'], [820, 1180, 1, 's13-cat-820.png'], [390, 844, 2, 's13-cat-390.png']]) {
    s = await pagina(b, P13, ++port, { w, h, scale: sc });
    await s.p.evaluate(() => document.querySelector('#titulo-catalogo').scrollIntoView());
    await s.p.evaluate(() => window.scrollBy(0, -100));
    await s.p.waitForTimeout(200);
    await s.p.screenshot({ path: path.join(OUT, out) });
    await s.close();
  }

  // la cabecera con el Reboot de Bootstrap encima y con el bloque 6 de header.css
  s = await pagina(b, P13, ++port, { w: 1440, h: 300, scale: 2 });
  // una línea guía a la mitad de la cabecera: con el Reboot, el nombre y el menú se salen de ella
  await s.p.addStyleTag({ content: 'body::after{content:"";position:absolute;left:0;right:0;top:40px;border-top:1px dashed #E11D48;z-index:200}' });
  await s.p.screenshot({ path: path.join(OUT, 's13-cabecera-bien.png'), clip: { x: 0, y: 0, width: 980, height: 82 } });
  await s.p.addStyleTag({ content: 'header h1{margin-bottom:.5rem!important} header ul{padding-left:2rem!important;margin-bottom:1rem!important}' });
  await s.p.screenshot({ path: path.join(OUT, 's13-cabecera-reboot.png'), clip: { x: 0, y: 0, width: 980, height: 82 } });
  await s.close();
}

async function sesion14(b) {
  let port = 8970;
  let s = await pagina(b, P14, ++port, { w: 1440, h: 900, scale: 1 });
  await s.p.screenshot({ path: path.join(OUT, 's14-cursos-1440.png') });
  await s.close();

  s = await pagina(b, P14, ++port, { w: 1440, h: 900, scale: 2 });
  const shot = async (sel, out, pad = 0) => { const r = await caja(s.p, sel); await s.p.screenshot({ path: path.join(OUT, out), clip: { x: r.x - pad, y: r.y - pad, width: r.width + 2 * pad, height: r.height + 2 * pad }, fullPage: true }); };
  await shot('.row.g-4 > div:nth-child(1) .card', 's14-card.png', 6);
  await shot('.row.g-4 > div:nth-child(4) .card', 's14-card-intermedio.png', 6);
  await shot('.alert', 's14-alert.png', 6);
  await shot('aside.card', 's14-cifras.png', 6);
  await shot(seccion('titulo-pasos'), 's14-pasos.png', 4);
  await shot('#faq', 's14-faq.png', 6);
  await shot(seccion('titulo-llamado') + ' .text-bg-dark', 's14-llamado.png', 6);
  const cat = await caja(s.p, seccion('titulo-catalogo'));
  await s.p.screenshot({ path: path.join(OUT, 's14-catalogo.png'), clip: { x: cat.x - 6, y: cat.y - 6, width: cat.width + 12, height: cat.height + 12 }, fullPage: true });
  // la ventana de inscripción abierta desde Git y GitHub
  await s.p.setViewportSize({ width: 1440, height: 900 });
  await s.p.click('button[data-curso="Git y GitHub"]');
  await s.p.waitForSelector('#inscripcion.show'); await s.p.waitForTimeout(500);
  await s.p.screenshot({ path: path.join(OUT, 's14-modal.png') });
  await s.close();

  // antes y después del tema: la misma zona sin tema-bootstrap.css
  for (const [sinTema, out] of [[true, 's14-sin-tema.png'], [false, 's14-con-tema.png']]) {
    s = await pagina(b, P14, ++port, { w: 1440, h: 900, scale: 1.5, sinTema });
    const r = await caja(s.p, seccion('titulo-catalogo') + ' .row > div:nth-child(1)');
    const r3 = await caja(s.p, seccion('titulo-catalogo') + ' .row > div:nth-child(3)');
    await s.p.screenshot({ path: path.join(OUT, out.replace('.png', '-cards.png')), clip: { x: r.x - 4, y: r.y - 4, width: r3.x + r3.width - r.x + 8, height: r.height + 8 }, fullPage: true });
    await s.p.click('button[data-bs-target="#faq-2"]'); await s.p.waitForTimeout(700);
    const f = await caja(s.p, '#faq');
    await s.p.screenshot({ path: path.join(OUT, out.replace('.png', '-faq.png')), clip: { x: f.x - 4, y: f.y - 4, width: f.width + 8, height: Math.min(f.height, 260) + 8 }, fullPage: true });
    await s.close();
  }

  // el celular
  s = await pagina(b, P14, ++port, { w: 390, h: 844, scale: 2 });
  await s.p.evaluate(() => { document.querySelector('#titulo-catalogo').scrollIntoView(); window.scrollBy(0, -90); });
  await s.p.waitForTimeout(200);
  await s.p.screenshot({ path: path.join(OUT, 's14-movil.png') });
  await s.close();
}

(async () => {
  const b = await chromium.launch();
  const solo = process.argv[3];
  if (!solo || solo === 'demos') await demos(b);
  if (!solo || solo === 's13') await sesion13(b);
  if (!solo || solo === 's14') await sesion14(b);
  await b.close();
  console.log('listo');
})();
