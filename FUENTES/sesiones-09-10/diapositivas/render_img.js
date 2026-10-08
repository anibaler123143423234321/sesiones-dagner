// Renderiza las demostraciones de CSS y las capturas del portafolio usadas en las diapositivas.
const { chromium } = require('playwright');
const path = require('path');
const { routeFonts, serve } = require('../herramientas/shot.js');
const REPO = process.argv[2] || '/home/user/sesiones-dagner';
const OUT = path.join(__dirname, 'img');

(async () => {
  const fs = require('fs');
  fs.mkdirSync(OUT, { recursive: true });
  const poster = path.join(__dirname, 'demos', 'poster-presentacion.jpg');
  if (!fs.existsSync(poster)) fs.copyFileSync(path.join(REPO, 'SESION 09', 'mi-portafolio-dagner', 'assets', 'img', 'poster-presentacion.jpg'), poster);
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1000, height: 800 }, deviceScaleFactor: 2 });
  await routeFonts(ctx);
  const p = await ctx.newPage();
  // 1. demostraciones
  for (const d of ['escala', 'fondos', 'bordes', 'sombra', 'display', 'justify', 'align', 'flex1', 'wrap', 'gridfr', 'gridform']) {
    await p.goto('file://' + path.join(__dirname, 'demos', d + '.html'), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const r = await p.evaluate(() => { const b = document.body.getBoundingClientRect(); return { w: Math.ceil(b.width), h: Math.ceil(document.body.scrollHeight) }; });
    await p.setViewportSize({ width: r.w, height: Math.max(r.h, 100) });
    await p.screenshot({ path: path.join(OUT, d + '.png'), clip: { x: 0, y: 0, width: r.w, height: r.h } });
    await p.setViewportSize({ width: 1000, height: 800 });
    console.log('demo', d, r);
  }
  await ctx.close();

  // 2. capturas del portafolio
  const shots = [
    { ses: 'SESION 07', page: 'sobre-mi.html', out: 'sin-css.png', w: 1280, h: 720 },
    { ses: 'SESION 09', page: 'sobre-mi.html', out: 'con-css.png', w: 1280, h: 720 },
    { ses: 'SESION 09', page: 'mis-proyectos.html', out: 'tabla.png', w: 1440, sel: 'table' },
    { ses: 'SESION 10', page: 'index.html', out: 'hero.png', w: 1280, h: 720 },
    { ses: 'SESION 10', page: 'mis-proyectos.html', out: 'proyectos.png', w: 1440, sel: '.projects-section' },
    { ses: 'SESION 10', page: 'sobre-mi.html', out: 'about.png', w: 1440, sel: '.about-section' },
    { ses: 'SESION 10', page: 'contactame.html', out: 'contacto.png', w: 1440, sel: '.contact-section' },
    { ses: 'SESION 10', page: 'contactame.html', out: 'formulario.png', w: 1440, sel: '.form-grid' },
    { ses: 'SESION 10', page: 'index.html', out: 'movil-index.png', w: 390, h: 844, scale: 2 },
    { ses: 'SESION 10', page: 'mis-proyectos.html', out: 'movil-proyectos.png', w: 390, h: 844, scale: 2 },
    { ses: 'SESION 10', page: 'contactame.html', out: 'movil-contacto.png', w: 390, h: 844, scale: 2 },
  ];
  let port = 8900;
  for (const s of shots) {
    const srv = await serve(path.join(REPO, s.ses, 'mi-portafolio-dagner'), ++port);
    const c = await b.newContext({ viewport: { width: s.w, height: s.h || 900 }, deviceScaleFactor: s.scale || 1.5 });
    await routeFonts(c);
    const pg = await c.newPage();
    await pg.goto(`http://127.0.0.1:${port}/${s.page}`, { waitUntil: 'networkidle' });
    await pg.evaluate(() => document.fonts.ready);
    if (s.sel) await pg.locator(s.sel).first().screenshot({ path: path.join(OUT, s.out) });
    else await pg.screenshot({ path: path.join(OUT, s.out) });
    await c.close(); srv.kill();
    console.log('shot', s.out);
  }
  await b.close();
})();
