// Capturas del portafolio con Playwright.
// uso: node shot.js <carpeta-portafolio> <salida-prefijo> [ancho] [pagina...]
// Las fuentes de Google se descargan con curl (respeta el proxy y su CA) y se sirven desde caché.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const { execFileSync, spawn } = require('child_process');
const CACHE = path.join(__dirname, '..', 'fontcache');
fs.mkdirSync(CACHE, { recursive: true });
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36';

async function routeFonts(ctx) {
  await ctx.route(/https:\/\/fonts\.(googleapis|gstatic)\.com\/.*/, async (route) => {
    const url = route.request().url();
    const f = path.join(CACHE, crypto.createHash('sha1').update(url).digest('hex'));
    if (!fs.existsSync(f)) execFileSync('curl', ['-sS', '-A', UA, '-o', f, '-D', f + '.h', url]);
    const h = fs.readFileSync(f + '.h', 'utf8');
    const ct = (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream';
    await route.fulfill({ status: 200, body: fs.readFileSync(f), contentType: ct, headers: { 'access-control-allow-origin': '*' } });
  });
  // cdn.jsdelivr.net/npm/<paquete>@<versión>/<ruta>: el mismo archivo, sacado del registro de npm
  // (jsDelivr sirve los paquetes de npm tal cual; el registro sí es accesible desde aquí)
  await ctx.route(/https:\/\/cdn\.jsdelivr\.net\/npm\/.*/, async (route) => {
    const m = route.request().url().match(/\/npm\/((?:@[^/]+\/)?[^@/]+)@([^/]+)\/([^?#]+)/);
    if (!m) return route.abort();
    const [, pkg, ver, rel] = m;
    const dir = path.join(CACHE, 'npm', `${pkg.replace('/', '__')}@${ver}`);
    if (!fs.existsSync(path.join(dir, 'package'))) {
      fs.mkdirSync(dir, { recursive: true });
      const tgz = execFileSync('npm', ['pack', `${pkg}@${ver}`, '--silent'], { cwd: dir }).toString().trim().split('\n').pop();
      execFileSync('tar', ['xzf', tgz], { cwd: dir });
    }
    const f = path.join(dir, 'package', rel);
    if (!fs.existsSync(f)) return route.fulfill({ status: 404, body: '' });
    const ext = path.extname(f);
    const ct = { '.css': 'text/css', '.js': 'application/javascript', '.woff2': 'font/woff2', '.woff': 'font/woff', '.map': 'application/json' }[ext] || 'application/octet-stream';
    await route.fulfill({ status: 200, body: fs.readFileSync(f), contentType: ct, headers: { 'access-control-allow-origin': '*' } });
  });
  // YouTube y demás recursos externos: respuesta vacía para no esperar a la red
  await ctx.route(/https:\/\/(www\.)?youtube\.com\/.*/, (r) => r.fulfill({ status: 200, contentType: 'text/html', body: '<body style="margin:0;background:#111;color:#bbb;font:16px sans-serif;display:grid;place-items:center;height:100vh">YouTube</body>' }));
}

async function serve(dir, port) {
  const srv = spawn('python3', ['-m', 'http.server', String(port), '--bind', '127.0.0.1', '--directory', dir], { stdio: 'ignore' });
  await new Promise((r) => setTimeout(r, 800));
  return srv;
}

module.exports = { routeFonts, serve };

if (require.main === module) {
  (async () => {
    const [dir, out, w = '1440', ...pages] = process.argv.slice(2);
    const list = pages.length ? pages : ['index.html', 'sobre-mi.html', 'mis-proyectos.html', 'contactame.html'];
    const port = 8700 + Math.floor(Math.random() * 200);
    const srv = await serve(dir, port);
    const browser = await chromium.launch();
    const ctx = await browser.newContext({ viewport: { width: +w, height: 900 }, deviceScaleFactor: 1 });
    await routeFonts(ctx);
    const page = await ctx.newPage();
    const errors = [];
    page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
    page.on('pageerror', (e) => errors.push(String(e)));
    for (const p of list) {
      await page.goto(`http://127.0.0.1:${port}/${p}`, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      const info = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, fonts: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight).join(', ') }));
      await page.screenshot({ path: `${out}-${w}-${p.replace('.html', '')}.png`, fullPage: true });
      console.log(p, 'scrollWidth', info.sw, '| fuentes:', info.fonts);
    }
    if (errors.length) console.log('ERRORES:', errors.join('\n'));
    await browser.close();
    srv.kill();
  })();
}
