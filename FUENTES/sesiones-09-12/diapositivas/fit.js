// Coloca una imagen dentro de una caja sin deformarla: la ajusta y la centra.
const fs = require('fs');

function dims(file) {
  const b = fs.readFileSync(file);
  if (b.toString('ascii', 1, 4) === 'PNG') return [b.readUInt32BE(16), b.readUInt32BE(20)];
  if (b.toString('ascii', 0, 3) === 'GIF') return [b.readUInt16LE(6), b.readUInt16LE(8)];
  throw new Error('Formato no reconocido: ' + file);
}

// o.align: 'left' | 'center' (por defecto); o.valign: 'top' | 'middle' (por defecto)
function place(d, s, file, x, y, w, h, o = {}) {
  const [iw, ih] = dims(file);
  const pad = o.pad != null ? o.pad : 0.08;
  const r = iw / ih;
  let w2 = w - 2 * pad; let h2 = w2 / r;
  if (h2 > h - 2 * pad) { h2 = h - 2 * pad; w2 = h2 * r; }
  const W = w2 + 2 * pad; const H = h2 + 2 * pad;
  const X = o.align === 'left' ? x : x + (w - W) / 2;
  const Y = o.valign === 'top' ? y : y + (h - H) / 2;
  d.image(s, file, X, Y, W, H, o);
  return { x: X, y: Y, w: W, h: H };
}

module.exports = { dims, place };
