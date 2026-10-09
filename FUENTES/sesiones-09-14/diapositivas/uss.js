// Plantilla USS · Protech XP para las diapositivas del curso Diseño Web.
// Reproduce el diseño de las sesiones 07 y 08: bandas CINFO, títulos, tarjetas,
// bloques de código y diapositivas fijas (espera, CINFO, descanso).
const pptxgen = require('pptxgenjs');
const path = require('path');

const M = (f) => path.join(__dirname, 'media', f);
const C = {
  teal: '177E89', ink: '1F2326', sub: '5F676C', body: '33393D', line: 'CFD5D9',
  soft: 'F3F5F6', white: 'FFFFFF', code: '2B2B2B', kw: '8FE1E8', codeTxt: 'E5E7EB',
  cmt: '9AA39E', num: '9AA2A7', red: 'A8402B', primary: '06B6C4',
};
const F = 'Calibri';
const MONO = 'Consolas';
const CATS = ['CONCEPTUAL', 'INSTRUMENTAL', 'NIVELADOR', 'FUNCIONAL', 'ORIENTADOR'];
const R = 0.1; // radio de las tarjetas, en pulgadas

// ---------- texto con formato: **negrita** y `código` ----------
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|`[^`]+`)/g;
  let last = 0; let m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push({ text: text.slice(last, m.index), options: { ...base } });
    const t = m[0];
    if (t.startsWith('**')) out.push({ text: t.slice(2, -2), options: { ...base, bold: true, color: base.strongColor || base.color } });
    else out.push({ text: t.slice(1, -1), options: { ...base, fontFace: MONO, color: base.codeColor || base.color } });
    last = m.index + t.length;
  }
  if (last < text.length) out.push({ text: text.slice(last), options: { ...base } });
  out.forEach((r) => { delete r.options.strongColor; delete r.options.codeColor; });
  return out;
}

// Varias líneas, cada una un párrafo; admite viñetas
function paras(lines, base = {}, bullet = false) {
  const out = [];
  lines.forEach((ln, i) => {
    const rs = runs(ln, base);
    rs.forEach((r, j) => {
      // pptxgenjs escribe las propiedades de párrafo en cada fragmento: la viñeta va en todos
      if (bullet) r.options.bullet = { indent: 14 };
      if (j === rs.length - 1 && i < lines.length - 1) r.options.breakLine = true;
    });
    out.push(...rs);
  });
  return out;
}

// ---------- resaltado del código ----------
// «texto» se pinta en cian y negrita; los comentarios, en gris; un selector CSS
// (línea que termina en «{») se pinta en cian.
function codeRuns(src, size) {
  const lines = src.replace(/^\n+|\n+$/g, '').split('\n');
  const out = [];
  lines.forEach((ln, i) => {
    const parts = [];
    const pushTxt = (t, hl) => {
      if (!t) return;
      const segs = t.split(/(«[^»]*»)/);
      segs.forEach((sg) => {
        if (!sg) return;
        if (sg.startsWith('«')) parts.push({ text: sg.slice(1, -1), options: { color: C.kw, bold: true } });
        else parts.push({ text: sg, options: { color: hl ? C.kw : C.codeTxt, bold: !!hl } });
      });
    };
    let code = ln; let comment = '';
    const ci = ln.search(/\/\*|<!--/);
    if (ci >= 0) { code = ln.slice(0, ci); comment = ln.slice(ci); }
    const sel = code.match(/^(\s*)([^{}:;]+?)(\s*\{\s*)$/);
    if (sel && !code.includes('«')) {
      pushTxt(sel[1]); pushTxt(sel[2], true); pushTxt(sel[3]);
    } else pushTxt(code);
    if (comment) parts.push({ text: comment, options: { color: C.cmt } });
    if (!parts.length) parts.push({ text: ' ', options: { color: C.codeTxt } });
    parts.forEach((p) => { p.options.fontFace = MONO; p.options.fontSize = size; });
    parts[parts.length - 1].options.breakLine = i < lines.length - 1;
    out.push(...parts);
  });
  return out;
}

class Deck {
  constructor({ title, subject }) {
    const p = new pptxgen();
    p.layout = 'LAYOUT_WIDE';
    p.author = 'Ing. Dagner Anibal Chuman Lluen';
    p.company = 'Centro de Informática USS · Protech XP';
    p.title = title;
    p.subject = subject || 'Curso de Diseño Web';
    p.theme = { headFontFace: F, bodyFontFace: F };
    this.p = p;
    this.builders = [];
    this.photo = 0;
    const W = 13.333;
    p.defineSlideMaster({ title: 'PORTADA', background: { color: C.white }, objects: [{ image: { path: M('band-portada.png'), x: 0, y: 0, w: W, h: 1.6 } }] });
    p.defineSlideMaster({ title: 'IMAGEN', background: { color: C.white } });
    CATS.forEach((cat) => {
      const band = { image: { path: M(`band-${cat.toLowerCase()}.jpg`), x: 0, y: 0, w: W, h: 1.3 } };
      p.defineSlideMaster({
        title: cat, background: { color: C.white },
        objects: [band, { placeholder: { options: { name: 'title', type: 'title', x: 0.7, y: 1.98, w: 11.95, h: 0.56, fontFace: F, fontSize: 28, bold: true, color: C.ink, align: 'left', valign: 'middle', margin: 0 }, text: '' } }],
      });
      p.defineSlideMaster({ title: `${cat}_LIBRE`, background: { color: C.white }, objects: [{ image: { path: M(`band-${cat.toLowerCase()}.jpg`), x: 0, y: 0, w: W, h: 1.3 } }] });
    });
  }

  add(master, fn, notes) { this.builders.push({ master, fn, notes }); }

  async save(file) {
    const total = this.builders.length;
    this.builders.forEach((b, i) => {
      const s = this.p.addSlide({ masterName: b.master });
      b.fn(s, this);
      const n = String(i + 1).padStart(2, '0');
      s.addText(`${n} / ${total}`, { x: 11.6, y: 7.06, w: 1.45, h: 0.24, fontFace: F, fontSize: 8, color: C.num, align: 'right', valign: 'middle', margin: 0, isTextBox: true });
      if (b.notes) s.addNotes(b.notes);
    });
    await this.p.writeFile({ fileName: file });
    return total;
  }

  // ---------- piezas básicas ----------
  text(s, t, o) {
    const base = { fontFace: o.font || F, fontSize: o.size || 12, color: o.color || C.body, bold: !!o.bold, codeColor: o.codeColor, strongColor: o.strongColor };
    const content = Array.isArray(t) ? paras(t, base, !!o.bullet) : runs(t, base);
    s.addText(content, { x: o.x, y: o.y, w: o.w, h: o.h, align: o.align || 'left', valign: o.valign || 'middle', margin: 0, isTextBox: true, lineSpacingMultiple: o.lineSpacing, paraSpaceAfter: o.paraAfter, charSpacing: o.charSpacing, fit: o.fit });
  }

  card(s, x, y, w, h, o = {}) {
    s.addShape(this.p.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: o.r != null ? o.r : R, fill: { color: o.fill || C.white }, line: { color: o.line || C.line, width: o.lineW || 1 } });
  }

  circle(s, x, y, d, label, o = {}) {
    s.addShape(this.p.shapes.OVAL, { x, y, w: d, h: d, fill: { color: o.fill || C.teal }, line: { color: o.fill || C.teal, width: 1 } });
    if (label != null) this.text(s, String(label), { x, y, w: d, h: d, size: o.size || 12, bold: true, color: C.white, align: 'center' });
  }

  header(s, kicker, title, sub) {
    this.text(s, kicker.toUpperCase(), { x: 0.7, y: 1.7, w: 11.95, h: 0.26, size: 10.5, bold: true, color: C.teal, charSpacing: 3 });
    s.addText(title, { placeholder: 'title' });
    if (sub) this.text(s, sub, { x: 0.7, y: 2.5, w: 11.95, h: 0.3, size: 12.5, color: C.sub });
  }

  code(s, x, y, w, h, src, o = {}) {
    s.addShape(this.p.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: R, fill: { color: C.code }, line: { color: C.code, width: 1 } });
    s.addText(codeRuns(src, o.size || 11), { x: x + 0.25, y: y + 0.18, w: w - 0.5, h: h - 0.36, valign: o.valign || 'top', margin: 0, isTextBox: true, lineSpacingMultiple: o.lineSpacing || 1.2 });
  }

  callout(s, y, h, lead, txt, o = {}) {
    const x = o.x != null ? o.x : 0.7; const w = o.w || 11.95;
    this.card(s, x, y, w, h, { fill: o.fill || C.soft });
    const parts = [{ text: lead + ' ', options: { fontFace: F, fontSize: o.size || 12, bold: true, color: o.leadColor || C.teal } }, ...runs(txt, { fontFace: F, fontSize: o.size || 12, color: C.body, codeColor: C.ink })];
    s.addText(parts, { x: x + 0.34, y, w: w - 0.68, h, valign: 'middle', margin: 0, isTextBox: true });
  }

  note(s, y, txt) { this.text(s, txt, { x: 0.7, y, w: 11.95, h: 0.28, size: 11.5, color: C.sub, align: 'center' }); }

  // Filas: [{a, b, c}] — a en monoespaciada cian, b descripción, c ejemplo opcional
  rows(s, items, o = {}) {
    const y0 = o.y || 2.86; const h = o.h || 0.62; const gap = o.gap != null ? o.gap : 0.09;
    const aw = o.aw || 1.7; const hasC = items.some((it) => it.c);
    const bw = hasC ? (o.bw || 5.02) : 11.95 - 0.3 - aw - 0.3;
    items.forEach((it, i) => {
      const y = y0 + i * (h + gap);
      this.card(s, 0.7, y, 11.95, h, { fill: it.fill });
      this.text(s, it.a, { x: 1.0, y, w: aw, h, size: o.asize || 13, bold: true, color: C.teal, font: o.amono === false ? F : MONO, codeColor: C.teal });
      this.text(s, it.b, { x: 1.0 + aw, y, w: bw, h, size: o.bsize || 12, color: C.body, codeColor: C.ink });
      if (hasC && it.c) {
        this.text(s, '→', { x: 1.0 + aw + bw, y, w: 0.35, h, size: 12, color: C.num, align: 'center' });
        this.text(s, it.c, { x: 1.4 + aw + bw, y, w: 11.95 - (1.1 + aw + bw), h, size: o.csize || 11.5, color: C.body, codeColor: C.body });
      }
    });
  }

  // Filas de traducción Figma → CSS
  mapRows(s, items, o = {}) {
    const y0 = o.y || 3.1; const h = o.h || 0.53; const gap = o.gap != null ? o.gap : 0.07;
    if (o.heads) {
      this.text(s, o.heads[0], { x: 0.98, y: y0 - 0.27, w: 4, h: 0.24, size: 9.5, bold: true, color: C.sub });
      this.text(s, o.heads[1], { x: 5.95, y: y0 - 0.27, w: 4, h: 0.24, size: 9.5, bold: true, color: C.sub });
    }
    items.forEach(([a, b], i) => {
      const y = y0 + i * (h + gap);
      this.card(s, 0.7, y, 11.95, h);
      this.text(s, a, { x: 0.98, y, w: 4.5, h, size: 12, bold: true, color: C.ink });
      this.text(s, '→', { x: 5.5, y, w: 0.4, h, size: 12, color: C.num, align: 'center' });
      s.addText(b, { x: 5.95, y, w: 6.5, h, fontFace: MONO, fontSize: o.csize || 12, bold: true, color: C.teal, valign: 'middle', margin: 0, isTextBox: true });
    });
  }

  // Tarjetas numeradas en rejilla
  numCards(s, items, o = {}) {
    const cols = o.cols || 3; const y0 = o.y || 2.86; const h = o.h || 1.72; const gapX = 0.2; const gapY = o.gapY || 0.18;
    const w = (11.95 - gapX * (cols - 1)) / cols;
    items.forEach((it, i) => {
      const x = 0.7 + (i % cols) * (w + gapX); const y = y0 + Math.floor(i / cols) * (h + gapY);
      this.card(s, x, y, w, h, { fill: it.fill });
      this.circle(s, x + 0.27, y + 0.25, 0.44, it.n != null ? it.n : i + 1);
      this.text(s, it.t, { x: x + 0.88, y: y + 0.25, w: w - 1.05, h: 0.44, size: 13, bold: true, color: C.ink });
      this.text(s, it.d, { x: x + 0.3, y: y + 0.84, w: w - 0.6, h: h - 0.98, size: o.dsize || 11.5, color: C.body, valign: 'top', codeColor: C.ink });
    });
  }

  // Pasos a la derecha de un bloque de código
  steps(s, items, o = {}) {
    const x = o.x || 7.8; const w = o.w || 4.85; const y0 = o.y || 2.86; const h = o.h || 0.58; const gap = o.gap != null ? o.gap : 0.075;
    const tw = o.tw || 1.05;
    items.forEach(([t, d], i) => {
      const y = y0 + i * (h + gap);
      this.card(s, x, y, w, h);
      this.circle(s, x + 0.18, y + (h - 0.36) / 2, 0.36, i + 1, { size: 10.5 });
      this.text(s, t, { x: x + 0.72, y, w: tw, h, size: 12.5, bold: true, color: C.ink });
      this.text(s, d, { x: x + 0.72 + tw, y, w: w - 0.85 - tw, h, size: 10.5, color: C.body, codeColor: C.ink });
    });
  }

  twoCards(s, left, right, o = {}) {
    const y = o.y || 2.86; const h = o.h || 2.1;
    [[left, 0.7, o.lfill || C.white], [right, 6.8, o.rfill || C.soft]].forEach(([c, x, fill]) => {
      this.card(s, x, y, 5.85, h, { fill });
      this.text(s, c.t, { x: x + 0.34, y: y + 0.22, w: 5.17, h: 0.34, size: 14, bold: true, color: c.color || C.ink, codeColor: c.color || C.ink });
      this.text(s, c.items, { x: x + 0.34, y: y + 0.62, w: 5.17, h: h - 0.8, size: 12, color: C.body, valign: 'top', bullet: c.bullet !== false, paraAfter: 4, codeColor: C.ink });
    });
  }

  image(s, file, x, y, w, h, o = {}) {
    if (o.frame !== false) this.card(s, x, y, w, h, { line: o.line || C.line, lineW: o.lineW || 1.5 });
    const pad = o.pad != null ? o.pad : 0.08;
    s.addImage({ path: file, x: x + pad, y: y + pad, w: w - 2 * pad, h: h - 2 * pad, altText: o.alt || '', sizing: o.sizing });
  }

  // ---------- diapositivas completas ----------
  waiting(sesion, texto) {
    this.add('PORTADA', (s) => {
      s.addImage({ path: M('espera.png'), x: 5.72, y: 1.9, w: 1.9, h: 1.9, altText: 'Indicador de espera' });
      this.card(s, 3.42, 3.98, 6.5, 0.92, { fill: C.teal, line: C.teal, r: 0.46 });
      this.text(s, 'ESPERANDO A LOS COMPAÑEROS', { x: 3.42, y: 3.98, w: 6.5, h: 0.92, size: 20, bold: true, color: C.white, align: 'center' });
      this.text(s, `Sesión ${sesion} · comenzamos en unos minutos`, { x: 1.5, y: 5.14, w: 10.33, h: 0.4, size: 16, color: C.ink, align: 'center' });
      this.text(s, texto, { x: 1.5, y: 5.6, w: 10.33, h: 0.34, size: 11.5, color: C.sub, align: 'center' });
      this.card(s, 5.16, 6.41, 3.02, 0.51, { line: C.line, r: 0.25 });
      this.text(s, 'CURSO DE DISEÑO WEB', { x: 5.16, y: 6.41, w: 3.02, h: 0.51, size: 10, bold: true, color: C.sub, align: 'center', charSpacing: 3 });
    });
  }

  title({ titulo, sesion, sub, code }) {
    this.add('PORTADA', (s) => {
      this.text(s, 'CURSO DE DISEÑO WEB', { x: 0.75, y: 2.24, w: 6, h: 0.28, size: 11, bold: true, color: C.teal, charSpacing: 3 });
      this.text(s, titulo, { x: 0.75, y: 2.66, w: 8.1, h: 1.0, size: 38, bold: true, color: C.ink, valign: 'middle' });
      this.card(s, 0.75, 3.9, 2.35, 0.5, { fill: C.teal, line: C.teal, r: 0.25 });
      this.text(s, `SESIÓN ${sesion}`, { x: 0.75, y: 3.9, w: 2.35, h: 0.5, size: 13, bold: true, color: C.white, align: 'center', charSpacing: 2 });
      this.text(s, sub, { x: 0.75, y: 4.66, w: 8.1, h: 0.3, size: 12.5, color: C.sub });
      this.text(s, 'DOCENTE', { x: 0.75, y: 5.26, w: 3, h: 0.26, size: 10, bold: true, color: C.sub, charSpacing: 2 });
      this.text(s, 'Ing. Dagner Anibal Chuman Lluen', { x: 0.75, y: 5.56, w: 6, h: 0.36, size: 15, bold: true, color: C.ink });
      this.code(s, 9.15, 2.5, 3.6, 1.85, code, { size: 12.5, valign: 'middle' });
    });
  }

  imageSlide(file, alt) {
    this.add('IMAGEN', (s) => { s.addImage({ path: M(file), x: 0, y: 0, w: 13.333, h: 7.5, altText: alt }); });
  }

  divider(cat, nombre, numero, items) {
    const foto = this.photo++ % 2 === 0 ? 'foto-bloque-a.jpg' : 'foto-bloque-b.jpg';
    this.add(`${cat}_LIBRE`, (s) => {
      s.addShape(this.p.shapes.ROUNDED_RECTANGLE, { x: -0.6, y: 1.66, w: 5.6, h: 1.12, rectRadius: 0.56, fill: { color: C.teal }, line: { color: C.teal, width: 1 } });
      this.text(s, nombre, { x: 0.3, y: 1.66, w: 4.6, h: 1.12, size: 20, bold: true, color: C.white, align: 'center' });
      this.text(s, `BLOQUE ${numero}`, { x: 0.3, y: 3.1, w: 4.7, h: 0.28, size: 11, bold: true, color: C.teal, align: 'center', charSpacing: 4 });
      this.text(s, 'En este bloque', { x: 0.75, y: 3.66, w: 4, h: 0.26, size: 10.5, bold: true, color: C.sub });
      items.forEach((it, i) => {
        const y = 4.0 + i * 0.6;
        this.card(s, 0.75, y, 6.1, 0.52);
        this.text(s, String(i + 1).padStart(2, '0'), { x: 0.98, y, w: 0.5, h: 0.52, size: 12, bold: true, color: C.teal });
        this.text(s, it, { x: 1.62, y, w: 5.1, h: 0.52, size: 12, color: C.body });
      });
      this.card(s, 7.4, 1.35, 5.65, 5.75);
      s.addImage({ path: M(foto), x: 7.55, y: 1.49, w: 5.35, h: 5.47, altText: 'Persona programando frente a un monitor' });
    });
  }

  breakSlide(texto) {
    this.add('CONCEPTUAL_LIBRE', (s) => {
      this.card(s, 3.42, 2.9, 6.5, 1.05, { fill: C.teal, line: C.teal, r: 0.52 });
      this.text(s, 'DESCANSO · 15 MINUTOS', { x: 3.42, y: 2.9, w: 6.5, h: 1.05, size: 20, bold: true, color: C.white, align: 'center' });
      s.addImage({ path: M('espera.png'), x: 6.07, y: 4.35, w: 1.2, h: 1.2, altText: 'Indicador de espera' });
      this.text(s, texto, { x: 1.5, y: 5.82, w: 10.33, h: 0.34, size: 12, color: C.sub, align: 'center' });
    });
  }

  agenda(items) {
    this.add('CONCEPTUAL', (s) => {
      this.header(s, 'Agenda', 'Cómo se reparten las 4 horas');
      const h = 0.46; const step = 0.515;
      items.forEach(([num, t, d, min], i) => {
        const y = 2.82 + i * step; const pausa = num === '—';
        this.card(s, 0.7, y, 11.95, h, { fill: pausa ? C.soft : C.white });
        this.circle(s, 1.05, y + 0.04, 0.38, num, { fill: pausa ? C.sub : C.teal, size: 10.5 });
        this.text(s, t, { x: 1.82, y, w: 3.9, h, size: 13, bold: true, color: pausa ? C.sub : C.ink });
        if (d) this.text(s, d, { x: 5.85, y, w: 5.3, h, size: 11, color: C.sub, codeColor: C.sub });
        this.text(s, `${min} min`, { x: 11.15, y, w: 1.3, h, size: 11, bold: true, color: pausa ? C.sub : C.teal, align: 'right' });
      });
    });
  }

  logros(items) {
    this.add('CONCEPTUAL', (s) => {
      this.header(s, 'Logros de aprendizaje', '¿Qué vas a lograr hoy?');
      items.forEach(([t, d], i) => {
        const y = 2.86 + i * 0.77;
        this.card(s, 0.7, y, 11.95, 0.68);
        this.circle(s, 1.07, y + 0.06, 0.56, i + 1, { size: 13 });
        this.text(s, t, { x: 1.85, y, w: 2.5, h: 0.68, size: 13.5, bold: true, color: C.teal });
        this.text(s, d, { x: 4.5, y, w: 7.85, h: 0.68, size: 12, color: C.body, codeColor: C.ink });
      });
    });
  }

  checklist(cat, items) {
    this.add(cat, (s) => {
      this.header(s, 'Nivelador', 'Autoevaluación', 'Marca mentalmente cada punto. Si dudas en alguno, pregunta ahora.');
      items.forEach((t, i) => {
        const y = 2.86 + i * 0.5;
        this.card(s, 0.7, y, 11.95, 0.44);
        s.addShape(this.p.shapes.ROUNDED_RECTANGLE, { x: 1.0, y: y + 0.08, w: 0.32, h: 0.28, rectRadius: 0.06, fill: { color: C.white }, line: { color: C.teal, width: 1.5 } });
        this.text(s, t, { x: 1.5, y, w: 10.85, h: 0.44, size: 12, color: C.body, codeColor: C.ink });
      });
    });
  }

  consultas(cat, cards, lead, txt) {
    this.add(cat, (s) => {
      this.header(s, 'Nivelador', 'Espacio de consultas', '¿Qué parte quedó menos clara?');
      cards.forEach(([t, d], i) => {
        const x = 0.7 + i * 3.03;
        this.card(s, x, 2.98, 2.88, 2.07, { fill: C.soft });
        this.text(s, t, { x: x + 0.2, y: 3.26, w: 2.48, h: 0.4, size: 16, bold: true, color: C.teal, align: 'center' });
        this.text(s, d, { x: x + 0.25, y: 3.78, w: 2.38, h: 0.9, size: 12, color: C.body, align: 'center', valign: 'top', codeColor: C.ink });
      });
      this.card(s, 0.7, 5.31, 11.95, 1.28);
      this.text(s, lead, { x: 1.04, y: 5.48, w: 11.27, h: 0.34, size: 14, bold: true, color: C.ink });
      this.text(s, txt, { x: 1.04, y: 5.88, w: 11.27, h: 0.61, size: 12, color: C.body, valign: 'top', codeColor: C.ink });
    });
  }

  tarea(consigna, entrega) {
    this.add('FUNCIONAL', (s) => {
      this.header(s, 'Actividad', 'Tarea de la sesión', 'Forma parte del 40 % de participación en clases [P].');
      this.card(s, 0.7, 2.86, 5.85, 3.73, { fill: C.soft });
      this.text(s, 'Consigna', { x: 1.04, y: 3.08, w: 5.17, h: 0.34, size: 15, bold: true, color: C.ink });
      this.text(s, consigna, { x: 1.04, y: 3.48, w: 5.17, h: 2.98, size: 11.5, color: C.body, valign: 'top', bullet: true, paraAfter: 3, codeColor: C.ink });
      this.card(s, 6.8, 2.86, 5.85, 3.73);
      this.text(s, 'Indicaciones de entrega', { x: 7.14, y: 3.08, w: 5.2, h: 0.34, size: 15, bold: true, color: C.teal });
      entrega.forEach((t, i) => {
        const y = 3.64 + i * 0.7;
        this.circle(s, 7.2, y, 0.42, i + 1, { size: 11.5 });
        this.text(s, t, { x: 7.8, y, w: 4.6, h: 0.42, size: 12, color: C.body });
      });
    });
  }

  resumen(items) {
    this.add('ORIENTADOR', (s) => {
      this.header(s, 'Resumen', 'Puntos clave de la sesión');
      items.forEach((t, i) => {
        const y = 2.9 + i * 0.48;
        this.circle(s, 0.87, y + 0.05, 0.36, '✓', { size: 11 });
        this.text(s, t, { x: 1.48, y, w: 10.95, h: 0.46, size: 12.5, color: C.body, codeColor: C.ink });
      });
    });
  }

  hacia(sub, hitos, cierre) {
    this.add('ORIENTADOR', (s) => {
      this.header(s, 'Orientador', 'Hacia dónde vamos', sub);
      s.addShape(this.p.shapes.LINE, { x: 1.15, y: 4.26, w: 11.05, h: 0, line: { color: C.line, width: 2.5 } });
      const w = 11.05 / hitos.length;
      hitos.forEach(([ses, t, d, actual], i) => {
        const x = 1.15 + i * w; const cx = x + w / 2;
        const dd = actual ? 0.26 : 0.17;
        s.addShape(this.p.shapes.OVAL, { x: cx - dd / 2, y: 4.26 - dd / 2, w: dd, h: dd, fill: { color: C.teal }, line: { color: C.teal, width: 1 } });
        this.text(s, ses, { x, y: 3.24, w, h: 0.26, size: 9.5, bold: true, color: C.sub, align: 'center', charSpacing: 2 });
        this.text(s, t, { x, y: 3.52, w, h: 0.4, size: 15, bold: true, color: actual ? C.teal : C.ink, align: 'center' });
        this.text(s, d, { x: x + 0.1, y: 4.52, w: w - 0.2, h: 0.62, size: 10.5, color: C.sub, align: 'center', valign: 'top' });
      });
      this.card(s, 0.7, 5.84, 11.95, 0.76, { fill: C.soft });
      this.text(s, cierre, { x: 1.04, y: 5.84, w: 11.27, h: 0.76, size: 12.5, color: C.body, codeColor: C.ink });
      this.text(s, 'Ing. Dagner Anibal Chuman Lluen', { x: 0.7, y: 6.76, w: 5, h: 0.26, size: 10.5, color: C.sub });
    });
  }
}

module.exports = { Deck, C, F, MONO, M, runs };
