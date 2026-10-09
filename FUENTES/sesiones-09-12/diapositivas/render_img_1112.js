// Imágenes de las diapositivas de las sesiones 11 y 12: demostraciones y capturas del portafolio.
// uso: node render_img_1112.js <repo>
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { execFileSync } = require('child_process');
const { routeFonts, serve } = require('../herramientas/shot.js');
const REPO = process.argv[2] || '/home/user/sesiones-dagner';
const OUT = path.join(__dirname, 'img');
const TMP = path.join(__dirname, 'img', 'tmp');
fs.mkdirSync(TMP, { recursive: true });
const im = (...a) => execFileSync('convert', a);
const P11 = path.join(REPO, 'SESION 11', 'mi-portafolio-dagner');
const P12 = path.join(REPO, 'SESION 12', 'mi-portafolio-dagner');

async function demos(b) {
  const ctx = await b.newContext({ viewport: { width: 1000, height: 800 }, deviceScaleFactor: 2 });
  await routeFonts(ctx);
  const p = await ctx.newPage();
  for (const d of ['curvas', 'transform', 'clamp', 'autofit']) {
    await p.goto('file://' + path.join(__dirname, 'demos', d + '.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const r = await p.evaluate(() => { const b = document.body.getBoundingClientRect(); return { w: Math.ceil(b.width), h: Math.ceil(document.body.scrollHeight) }; });
    await p.setViewportSize({ width: r.w, height: Math.max(r.h, 100) });
    await p.screenshot({ path: path.join(OUT, d + '.png'), clip: { x: 0, y: 0, width: r.w, height: r.h } });
    await p.setViewportSize({ width: 1000, height: 800 });
    console.log('demo', d, r);
  }
  await ctx.close();
}

async function pagina(b, dir, port, opts = {}) {
  const srv = await serve(dir, port);
  const ctx = await b.newContext({ viewport: { width: opts.w || 1280, height: opts.h || 720 }, deviceScaleFactor: opts.scale || 1.5, isMobile: !!opts.mobile, hasTouch: !!opts.mobile, reducedMotion: opts.reduce ? 'reduce' : 'no-preference' });
  await routeFonts(ctx);
  const p = await ctx.newPage();
  return { p, close: async () => { await ctx.close(); srv.kill(); }, url: (f) => `http://127.0.0.1:${port}/${f}` };
}

async function sesion11(b) {
  // 1. La entrada del Hero, fotograma a fotograma (animaciones en pausa)
  let s = await pagina(b, P11, 8931, { w: 1280, h: 900, scale: 1 });
  await s.p.goto(s.url('index.html'), { waitUntil: 'networkidle' });
  await s.p.evaluate(() => document.fonts.ready);
  const tiempos = [0, 150, 300, 1000];
  const frames = [];
  const zona = await s.p.evaluate(() => {
    const a = document.querySelector('.hero-left').getBoundingClientRect(); const b = document.querySelector('.hero-right').getBoundingClientRect();
    const x = Math.min(a.left, b.left) - 24; const y = Math.min(a.top, b.top) - 24;
    return { x, y, width: Math.max(a.right, b.right) + 24 - x, height: Math.max(a.bottom, b.bottom) + 24 - y };
  });
  for (const t of tiempos) {
    await s.p.evaluate((t) => document.getAnimations().forEach((a) => { a.pause(); if (a.animationName === 'aparecer') a.currentTime = t; }), t);
    const f = path.join(TMP, `hero-${t}.png`);
    await s.p.screenshot({ path: f, clip: zona });
    frames.push(f);
  }
  // tira de cinco fotogramas con su tiempo
  const lab = frames.map((f, i) => { const o = path.join(TMP, `hero-l-${i}.png`); im(f, '+repage', '-resize', '480x', '-background', 'white', '-gravity', 'north', '-splice', '0x40', '-font', 'DejaVu-Sans-Bold', '-pointsize', '24', '-fill', '#177E89', '-annotate', '+0+8', `${tiempos[i]} ms`, '-bordercolor', 'white', '-border', '8x0', o); return o; });
  im(...lab, '+append', '+repage', path.join(OUT, 's11-hero-tira.png'));
  execFileSync('montage', [...lab, '-tile', '2x2', '-geometry', '+6+6', '-background', 'white', path.join(OUT, 's11-hero-2x2.png')]);
  // GIF: el primer cuadro es el final (así se ve bien en el PDF); después la entrada en bucle
  const gif = [];
  for (let t = 0; t <= 1000; t += 50) {
    await s.p.evaluate((t) => document.getAnimations().forEach((a) => { a.pause(); if (a.animationName === 'aparecer') a.currentTime = t; }), t);
    const f = path.join(TMP, `g-${String(t).padStart(4, '0')}.png`);
    await s.p.screenshot({ path: f, clip: zona });
    gif.push(f);
  }
  im('-delay', '150', gif[gif.length - 1], '-delay', '4', ...gif, '-delay', '120', gif[gif.length - 1], '-resize', '960x', '-layers', 'Optimize', '-loop', '0', path.join(OUT, 's11-hero.gif'));
  await s.close();

  // 2. Los estados del botón: normal, hover y active
  s = await pagina(b, P11, 8932, { w: 1280, h: 900, scale: 2 });
  await s.p.goto(s.url('index.html'), { waitUntil: 'networkidle' });
  await s.p.evaluate(() => document.fonts.ready);
  await s.p.waitForTimeout(1300);
  const box = await s.p.locator('.btn-primary').boundingBox();
  const clip = { x: box.x - 14, y: box.y - 24, width: box.width + 26, height: box.height + 48 };
  await s.p.mouse.move(5, 5); await s.p.waitForTimeout(400);
  await s.p.screenshot({ path: path.join(TMP, 'b0.png'), clip });
  await s.p.mouse.move(box.x + box.width / 2, box.y + box.height / 2); await s.p.waitForTimeout(500);
  await s.p.screenshot({ path: path.join(TMP, 'b1.png'), clip });
  await s.p.mouse.down(); await s.p.waitForTimeout(400);
  await s.p.screenshot({ path: path.join(TMP, 'b2.png'), clip });
  await s.p.mouse.move(5, 5); await s.p.mouse.up();   // soltar fuera del botón: no navega
  await s.p.goto(s.url('index.html'), { waitUntil: 'networkidle' }); await s.p.waitForTimeout(1300);
  ['b0', 'b1', 'b2'].forEach((n, i) => im(path.join(TMP, n + '.png'), '+repage', '-background', 'white', '-gravity', 'north', '-splice', '0x50', '-font', 'DejaVu-Sans-Mono-Bold', '-pointsize', '26', '-fill', '#177E89', '-annotate', '+0+10', ['.btn-primary', ':hover', ':active'][i], path.join(TMP, n + 'l.png')));
  im(path.join(TMP, 'b0l.png'), path.join(TMP, 'b1l.png'), path.join(TMP, 'b2l.png'), '-gravity', 'center', '+append', path.join(OUT, 's11-boton-estados.png'));
  // el menú con el subrayado animado
  const nav = await s.p.locator('nav[aria-label="Navegacion principal"]').first().boundingBox();
  await s.p.hover('nav[aria-label="Navegacion principal"] a[href="sobre-mi.html"]'); await s.p.waitForTimeout(60);
  await s.p.screenshot({ path: path.join(TMP, 'n1.png'), clip: { x: nav.x - 16, y: nav.y - 14, width: nav.width + 32, height: nav.height + 28 } });
  await s.p.waitForTimeout(600);
  await s.p.screenshot({ path: path.join(TMP, 'n2.png'), clip: { x: nav.x - 16, y: nav.y - 14, width: nav.width + 32, height: nav.height + 28 } });
  await s.p.mouse.move(5, 5); await s.p.waitForTimeout(600);
  await s.p.screenshot({ path: path.join(TMP, 'n0.png'), clip: { x: nav.x - 16, y: nav.y - 14, width: nav.width + 32, height: nav.height + 28 } });
  im(path.join(TMP, 'n0.png'), path.join(TMP, 'n1.png'), path.join(TMP, 'n2.png'), '-background', 'white', '-splice', '0x10', '-append', path.join(OUT, 's11-menu.png'));
  // la tarjeta de código con el cursor
  await s.p.evaluate(() => document.getAnimations().forEach((a) => { if (a.animationName === 'parpadeo') { a.pause(); a.currentTime = 100; } }));
  const cc = await s.p.evaluate(() => { const r = document.querySelector('.code-card').getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height }; });
  await s.p.screenshot({ path: path.join(OUT, 's11-codigo.png'), clip: cc });
  await s.close();

  // 3. Tarjetas: proyecto y contacto, quietas y con el cursor encima
  s = await pagina(b, P11, 8933, { w: 1440, h: 900, scale: 1.5 });
  await s.p.goto(s.url('mis-proyectos.html'), { waitUntil: 'networkidle' });
  await s.p.evaluate(() => document.fonts.ready);
  await s.p.locator('.projects-grid').screenshot({ path: path.join(TMP, 'p0.png') });
  await s.p.hover('.project-card >> nth=0'); await s.p.waitForTimeout(700);
  const g = await s.p.locator('.projects-grid').boundingBox();
  await s.p.screenshot({ path: path.join(OUT, 's11-proyecto-hover.png'), clip: { x: g.x - 10, y: g.y - 20, width: g.width + 20, height: g.height + 50 } });
  await s.p.goto(s.url('contactame.html'), { waitUntil: 'networkidle' });
  await s.p.evaluate(() => document.fonts.ready);
  await s.p.hover('.contact-card >> nth=1'); await s.p.waitForTimeout(700);
  const cl = await s.p.locator('.contact-list').boundingBox();
  await s.p.screenshot({ path: path.join(OUT, 's11-contacto-hover.png'), clip: { x: cl.x - 10, y: cl.y - 10, width: cl.width + 30, height: cl.height + 20 } });
  await s.close();
}

async function sesion12(b) {
  // 1. La portada en tres anchos (lo que se ve en la pantalla)
  const anchos = [[1440, 900, 1, 's12-escritorio.png'], [820, 1180, 1, 's12-tablet.png'], [390, 844, 2, 's12-celular.png']];
  let port = 8940;
  for (const [w, h, sc, f] of anchos) {
    const s = await pagina(b, P12, ++port, { w, h, scale: sc });
    await s.p.goto(s.url('index.html'), { waitUntil: 'networkidle' });
    await s.p.evaluate(() => document.fonts.ready);
    await s.p.waitForTimeout(1200);
    await s.p.screenshot({ path: path.join(OUT, f) });
    await s.close();
  }
  // 2. El celular: cuatro páginas
  for (const [pg, f, sel] of [['index.html', 's12-m-index.png'], ['sobre-mi.html', 's12-m-sobre.png', '.media-grid'], ['mis-proyectos.html', 's12-m-proyectos.png'], ['contactame.html', 's12-m-contacto.png']]) {
    const s = await pagina(b, P12, ++port, { w: 390, h: 844, scale: 2 });
    await s.p.goto(s.url(pg), { waitUntil: 'networkidle' });
    await s.p.evaluate(() => document.fonts.ready);
    await s.p.waitForTimeout(1200);
    if (sel) await s.p.locator(sel).scrollIntoViewIfNeeded();
    await s.p.screenshot({ path: path.join(OUT, f) });
    await s.close();
  }
  // 3. La tabla que se desplaza en el celular
  let s = await pagina(b, P12, ++port, { w: 390, h: 844, scale: 2 });
  await s.p.goto(s.url('mis-proyectos.html'), { waitUntil: 'networkidle' });
  await s.p.evaluate(() => document.fonts.ready);
  await s.p.evaluate(() => { const t = document.querySelector('.tabla-scroll'); t.scrollIntoView({ block: 'center' }); t.scrollLeft = 90; });
  await s.p.waitForTimeout(300);
  await s.p.screenshot({ path: path.join(OUT, 's12-tabla.png') });
  await s.close();
  // 4. Proyectos a 820: dos columnas sin media query
  s = await pagina(b, P12, ++port, { w: 820, h: 1180, scale: 1.5 });
  await s.p.goto(s.url('mis-proyectos.html'), { waitUntil: 'networkidle' });
  await s.p.evaluate(() => document.fonts.ready);
  await s.p.locator('.projects-grid').screenshot({ path: path.join(OUT, 's12-proyectos-820.png') });
  await s.close();
  // 5. Con y sin la etiqueta viewport, en un celular simulado
  const sin = path.join(P12, 'index-sin-viewport.html');
  fs.writeFileSync(sin, fs.readFileSync(path.join(P12, 'index.html'), 'utf8').replace(/\s*<meta name="viewport"[^>]*>/, ''));
  try {
    for (const [pg, f] of [['index.html', 's12-con-viewport.png'], ['index-sin-viewport.html', 's12-sin-viewport.png']]) {
      s = await pagina(b, P12, ++port, { w: 390, h: 844, scale: 2, mobile: true });
      await s.p.goto(s.url(pg), { waitUntil: 'networkidle' });
      await s.p.evaluate(() => document.fonts.ready);
      await s.p.waitForTimeout(1200);
      await s.p.screenshot({ path: path.join(OUT, f) });
      await s.close();
    }
  } finally { fs.unlinkSync(sin); }
}

(async () => {
  const b = await chromium.launch();
  const solo = process.argv[3];
  if (!solo || solo === 'demos') await demos(b);
  if (!solo || solo === 's11') await sesion11(b);
  if (!solo || solo === 's12') await sesion12(b);
  await b.close();
  fs.rmSync(TMP, { recursive: true, force: true });
  console.log('listo');
})();
