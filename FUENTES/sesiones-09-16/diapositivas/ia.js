// Extra de IA de las sesiones 11 a 15: cinco diapositivas con el contenido de ia_contenido.json
// (que sale de guias/ia_contenido.py). Uso, antes del bloque Nivelador: require('./ia.js').bloqueIA(d, '11');
const { C } = require('./uss.js');
const IA = require('./ia_contenido.json');

// los prompts se ven en un bloque de código: comillas rectas y saltos de línea cada ~76 caracteres
function partir(texto, ancho = 76) {
  const out = []; let linea = '';
  for (const p of texto.replace(/[«»]/g, '"').split(' ')) {
    if ((linea + ' ' + p).trim().length > ancho) { out.push(linea.trim()); linea = p; } else { linea += ' ' + p; }
  }
  if (linea.trim()) out.push(linea.trim());
  return out.join('\n');
}
const recorta = (s, n) => (s.length > n ? s.slice(0, n).replace(/\s+\S*$/, '') + '…' : s);

function bloqueIA(d, n) {
  const s = IA.sesiones[n];
  d.divider('INSTRUMENTAL', 'Extra · Codificar con IA', 'EXTRA', ['La fórmula del buen prompt', 'Mal prompt y buen prompt', 'Prompts de hoy', 'Figma con IA']);

  d.add('INSTRUMENTAL', (sl) => {
    d.header(sl, 'Extra · IA', 'La fórmula del buen prompt', 'Funciona con ChatGPT, Gemini, Claude o Copilot. Escríbelo en español y en un solo mensaje.');
    d.numCards(sl, [
      ...IA.formula.map(([t, q, e]) => ({ t, d: `${q}. ${e}` })),
      { t: 'Comprueba', d: 'Prueba la respuesta en el validador, en el navegador y contra tu Figma antes de usarla.' },
    ], { dsize: 11 });
  });

  d.add('INSTRUMENTAL', (sl) => {
    d.header(sl, 'Extra · IA', 'Mal prompt y buen prompt', `Sesión ${n} · ${s.tema}`);
    d.card(sl, 0.7, 2.86, 3.55, 2.6, { fill: 'FDECEC' });
    d.text(sl, 'Así no', { x: 0.95, y: 3.0, w: 3.1, h: 0.32, size: 14, bold: true, color: 'B42318' });
    d.text(sl, `«${s.malo}»`, { x: 0.95, y: 3.45, w: 3.1, h: 1.85, size: 14, color: C.ink, valign: 'top' });
    d.code(sl, 4.45, 2.86, 8.2, 2.6, partir(s.bueno), { size: 9.5 });
    d.text(sl, 'ASÍ SÍ', { x: 11.7, y: 2.9, w: 0.85, h: 0.25, size: 9, bold: true, color: '7DD3DB', align: 'right' });
    s.por_que.forEach((t, i) => {
      const x = 0.7 + i * 4.05;
      d.card(sl, x, 5.62, 3.85, 1.05, { fill: C.soft });
      d.circle(sl, x + 0.22, 5.62 + 0.31, 0.42, i + 1);
      d.text(sl, t, { x: x + 0.8, y: 5.62, w: 2.9, h: 1.05, size: 11, color: C.body, codeColor: C.ink });
    });
  });

  d.add('INSTRUMENTAL', (sl) => {
    d.header(sl, 'Extra · IA', 'Prompts de hoy', 'Cambia lo que está entre corchetes por tu código. Los prompts completos están en la guía Extra de IA.');
    d.rows(sl, s.prompts.map(([t, p]) => ({ a: t, b: recorta(p.replace(/[«»]/g, '"'), 150) })),
      { aw: 2.9, amono: false, h: 0.8, gap: 0.1, asize: 12.5, bsize: 10.5 });
  });

  d.add('INSTRUMENTAL', (sl) => {
    d.header(sl, 'Extra · IA', 'Figma con IA y la revisión final', 'La IA propone; tú decides con el manual y la guía de la sesión.');
    d.twoCards(sl,
      { t: 'Figma con IA', color: C.teal, items: s.figma.map(([t, x]) => `**${t}:** ${recorta(x, 165)}`) },
      { t: 'Antes de usar lo que te dio la IA', items: s.verifica },
      { h: 3.0 });
    d.callout(sl, 6.0, 0.68, 'Tu bitácora de prompts:', 'anota el prompt, lo que te dio, lo que corregiste y cómo lo comprobaste. Va en tu proyecto integrador.', { size: 11.5 });
  });
}

module.exports = { bloqueIA };
