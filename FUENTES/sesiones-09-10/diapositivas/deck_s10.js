// Sesión 10 · Maquetación con CSS: modelo de caja, Flexbox y Grid
// Incluye el Hero Section, que era la tarea de la sesión 08 (feriado).
const path = require('path');
const { Deck, C, F, MONO } = require('./uss.js');
const IMG = (f) => path.join(__dirname, 'img', f);
const out = process.argv[2] || path.join(__dirname, 'out', 'Sesion10-Modelo-de-Caja-Flexbox-y-Grid.pptx');

const d = new Deck({ title: 'Sesión 10 · Maquetación: modelo de caja, Flexbox y Grid' });

d.waiting('10', 'Abre tu carpeta mi-portafolio y tu archivo de Figma. Hoy cada bloque de tu diseño se coloca en su lugar.');
d.title({
  titulo: 'Modelo de caja, Flexbox y Grid',
  sesion: '10',
  sub: 'Modelo de caja · display · Flexbox · Grid · el Hero Section',
  code: '.hero-section {\n  display: flex;\n  align-items: center;\n  gap: 64px;\n}',
});
d.imageSlide('como-te-sientes.jpg', '¿Cómo te sientes hoy?');
d.imageSlide('que-es-cinfo.jpg', '¿Qué es CINFO? Conceptual, Instrumental, Nivelador, Funcional y Orientador');
d.imageSlide('conocimientos-previos.jpg', 'Conocimientos previos y definiciones clave');

d.add('CONCEPTUAL', (s) => {
  d.header(s, 'Repaso', 'De dónde venimos', 'Tu portafolio ya tiene colores, letra y bordes. Le falta la distribución de tu diseño.');
  d.twoCards(s, { t: 'Ya tienes', color: C.sub, items: ['`global.css`, `header.css` y `contenido.css` enlazados.', 'Color, tipografía, fondos y bordes de Figma en variables.', 'En Figma, Sobre mí y Proyectos (Pasos 10 y 11).'] },
    { t: 'Hoy sumas', items: ['Leer el modelo de caja en DevTools.', 'Construir el Hero con Flexbox.', 'Pasar las páginas interiores a dos columnas con Flexbox y Grid.'] });
  d.callout(s, 5.18, 1.42, 'Lo que hace distinta a esta sesión', '\nHasta ahora tu CSS decía cómo se ve cada cosa. Hoy decide dónde va. La Disposición automática que usas en Figma desde el primer paso es Flexbox: hoy aprendes a escribirla.');
});

d.logros([
  ['Medir', 'Leer el contenido, el padding, el borde y el margen de una caja.'],
  ['Decidir', 'Elegir entre display block, inline e inline-block.'],
  ['Alinear', 'Ordenar elementos en fila o en columna con Flexbox.'],
  ['Cuadricular', 'Repartir tarjetas en columnas iguales con Grid.'],
  ['Traducir', 'Escribir cada Disposición automática de Figma como display: flex.'],
]);

d.agenda([
  ['01', 'El modelo de caja', 'Contenido, padding, borde, margen y display.', 30],
  ['02', 'Flexbox', 'Ejes, justify-content, align-items, gap y flex.', 45],
  ['03', 'Grid', 'Columnas, la unidad fr, repeat() y grid-column.', 30],
  ['—', 'Descanso', '', 15],
  ['04', 'Figma: Pasos 12 al 14', 'Contacto, pie de página e imágenes.', 25],
  ['05', 'El Hero con Flexbox', 'index.html e index.css, la tarea de la sesión 08.', 35],
  ['06', 'Las páginas interiores', 'Proyectos con Grid, Sobre mí y Contacto con Flexbox.', 40],
]);

// ================= BLOQUE 01
d.divider('CONCEPTUAL', 'El modelo de caja', '01', ['Las cuatro capas de una caja', 'box-sizing', 'margin y padding', 'display: block, inline e inline-block', 'Ancho máximo y centrado']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Modelo de caja', 'Toda etiqueta es una caja', 'Cuatro capas, de adentro hacia afuera. DevTools las pinta con estos mismos colores.');
  const L = [['margin', 0.7, 2.86, 6.6, 3.7, 'F9CC9D'], ['border', 1.1, 3.2, 5.8, 3.02, 'FDDD9B'], ['padding', 1.45, 3.55, 5.1, 2.32, 'C3D08B'], ['', 2.15, 4.1, 3.7, 1.25, '8CB6C0']];
  L.forEach(([t, x, y, w, h, col]) => {
    s.addShape(d.p.shapes.RECTANGLE, { x, y, w, h, fill: { color: col }, line: { color: t === 'margin' ? 'E0A86B' : col, width: 1, dashType: t === 'margin' ? 'dash' : 'solid' } });
    if (t) d.text(s, t, { x: x + 0.1, y: y + 0.03, w: 1.5, h: 0.24, size: 10.5, bold: true, color: C.ink, font: MONO });
  });
  d.text(s, 'contenido\n300 × 120', { x: 2.15, y: 4.1, w: 3.7, h: 1.25, size: 13, bold: true, color: C.ink, align: 'center' });
  [['contenido', 'El texto o la imagen. Mide width × height.', 'Lo que hay dentro del marco'], ['padding', 'El relleno entre el contenido y el borde.', 'Espaciado'], ['border', 'La línea que rodea al padding.', 'Trazo'], ['margin', 'El espacio por fuera del borde, hacia los vecinos.', 'Espacio (gap) entre hermanos']].forEach(([a, b, c], i) => {
    const y = 2.86 + i * 0.95;
    d.card(s, 7.55, y, 5.1, 0.85);
    d.text(s, a, { x: 7.78, y: y + 0.06, w: 4.7, h: 0.28, size: 12, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 7.78, y: y + 0.34, w: 4.7, h: 0.24, size: 10.5, color: C.body });
    d.text(s, 'En Figma: ' + c, { x: 7.78, y: y + 0.57, w: 4.7, h: 0.22, size: 9.5, color: C.sub });
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Modelo de caja', 'box-sizing: dónde se cuenta el ancho', 'La misma regla da dos tamaños distintos según box-sizing.');
  const draw = (x, total, label, sub) => {
    d.card(s, x, 2.86, 5.85, 2.4, { fill: C.white });
    d.text(s, label, { x: x + 0.3, y: 2.98, w: 5.3, h: 0.32, size: 13, bold: true, color: C.ink, font: MONO });
    const scale = 0.0135; const wTot = total * scale;
    s.addShape(d.p.shapes.RECTANGLE, { x: x + 0.3, y: 3.5, w: wTot, h: 1.15, fill: { color: 'FDDD9B' }, line: { color: 'C9A84F', width: 1 } });
    s.addShape(d.p.shapes.RECTANGLE, { x: x + 0.3 + 0.015, y: 3.515, w: wTot - 0.03, h: 1.12, fill: { color: 'C3D08B' }, line: { color: 'C3D08B', width: 0 } });
    const cw = (total - 50) * scale;
    s.addShape(d.p.shapes.RECTANGLE, { x: x + 0.3 + 25 * scale, y: 3.5 + 0.32, w: cw, h: 0.5, fill: { color: '8CB6C0' }, line: { color: '8CB6C0', width: 0 } });
    d.text(s, `${total - 50} de contenido`, { x: x + 0.3 + 25 * scale, y: 3.82, w: cw, h: 0.5, size: 10.5, bold: true, color: C.ink, align: 'center' });
    d.text(s, `Mide ${total} px en total`, { x: x + 0.3, y: 4.75, w: 5.3, h: 0.3, size: 12.5, bold: true, color: C.teal });
    d.text(s, sub, { x: x + 0.3, y: 5.02, w: 5.3, h: 0.22, size: 10, color: C.sub });
  };
  draw(0.7, 350, 'content-box (por defecto)', '300 + 24 + 24 de padding + 1 + 1 de borde.');
  draw(6.8, 300, 'border-box (tu reset)', 'El padding y el borde se cuentan dentro de los 300.');
  d.code(s, 0.7, 5.45, 11.95, 0.72, '.tarjeta { width: 300px; padding: 24px; border: 1px solid; }      /* el mismo CSS en las dos */', { size: 12, valign: 'middle' });
  d.note(s, 6.3, 'Por eso tu global.css empieza con box-sizing: border-box: las medidas que escribes son las que ves, como en Figma.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Modelo de caja', 'margin y padding: uno, dos o cuatro valores', 'Se leen en el sentido de las agujas del reloj, empezando arriba. Igual que el Espaciado de Figma.');
  d.rows(s, [
    { a: 'padding: 24px', b: 'Los cuatro lados iguales.', c: 'Las tarjetas: Espaciado 24' },
    { a: 'padding: 0 80px', b: 'Arriba y abajo · derecha e izquierda.', c: 'La cabecera: Espaciado 0 · 80' },
    { a: 'padding: 160px 80px 100px 80px', b: 'Arriba · derecha · abajo · izquierda.', c: 'El Hero: 160 · 80 · 100 · 80' },
    { a: 'margin: 0 auto', b: 'Sin margen arriba; a los lados, lo que sobre.', c: 'Centra una caja con max-width' },
    { a: 'margin-bottom: 3rem', b: 'Un solo lado.', c: 'Separación entre secciones' },
  ], { aw: 3.75, bw: 4.0, asize: 11.5, bsize: 11.5, csize: 11 });
  d.note(s, 6.45, 'padding está dentro del borde y toma el fondo de la caja; margin está fuera y siempre es transparente.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Modelo de caja', 'display: block, inline e inline-block', 'Cada etiqueta trae un display por defecto. Cambiarlo cambia cómo ocupa el espacio.');
  d.image(s, IMG('display.png'), 0.7, 2.86, 7.0, 3.72, { alt: 'Una caja block, una inline y una inline-block dentro de un párrafo' });
  [['block', '`div`, `p`, `section`, `h2`', 'Ocupa todo el ancho.'], ['inline', '`a`, `span`, `img`, `strong`', 'Va en la línea de texto.'], ['inline-block', 'Los puntos `.dot` del Hero', 'En línea, con ancho y alto.'], ['none', 'Oculta la caja', 'No ocupa espacio.']].forEach(([a, b, c], i) => {
    const y = 2.86 + i * 0.95;
    d.card(s, 7.9, y, 4.75, 0.85);
    d.text(s, a, { x: 8.12, y: y + 0.06, w: 4.4, h: 0.28, size: 12, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 8.12, y: y + 0.34, w: 4.4, h: 0.24, size: 10.5, color: C.body, codeColor: C.ink });
    d.text(s, c, { x: 8.12, y: y + 0.57, w: 4.4, h: 0.22, size: 10, color: C.sub });
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Modelo de caja', 'Ancho máximo y centrado', 'Tres líneas que usas en main, en el Hero y en las tarjetas.');
  d.code(s, 0.7, 2.86, 6.4, 2.25, '«main» {\n  max-width: 1440px;      /* el ancho del marco de Figma */\n  margin: 0 auto;         /* centra la caja */\n  padding: 6.25rem 5rem;  /* Espaciado 100 y 80 */\n}\n«main section > p» { max-width: 70ch; }', { size: 11.5 });
  [['max-width', 'Crece hasta ese ancho, pero puede encogerse. Mejor que width para pantallas pequeñas.'], ['margin: 0 auto', 'Reparte a los lados el espacio que sobra.'], ['ch', 'El ancho del carácter 0: 70ch son unas 70 letras por línea.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.77;
    d.card(s, 7.3, y, 5.35, 0.68);
    d.text(s, a, { x: 7.52, y, w: 1.55, h: 0.68, size: 11.5, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 9.1, y, w: 3.45, h: 0.68, size: 10.5, color: C.body });
  });
  d.card(s, 0.7, 5.35, 11.95, 1.2, { fill: C.soft });
  d.text(s, 'Míralo en DevTools', { x: 1.04, y: 5.45, w: 11.3, h: 0.32, size: 13, bold: true, color: C.teal });
  d.text(s, 'Inspecciona `<main>` y abre la pestaña **Computed**: arriba está el diagrama de la caja. Desmarca `box-sizing: border-box` en el reset: la caja se ensancha, porque el padding pasa a sumarse por fuera.', { x: 1.04, y: 5.8, w: 11.3, h: 0.65, size: 11.5, color: C.body, valign: 'top', codeColor: C.ink });
});

// ================= BLOQUE 02
d.divider('CONCEPTUAL', 'Flexbox', '02', ['Contenedor e ítems', 'Los dos ejes', 'justify-content y align-items', 'gap, flex-wrap y flex: 1', 'La Disposición automática es Flexbox']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Flexbox', 'Contenedor e ítems', 'display: flex se escribe en el padre. Los que se ordenan son sus hijos directos.');
  d.code(s, 0.7, 2.86, 5.6, 2.5, '«header» {                         /* contenedor */\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n}\n\n/* ítems: h1, nav y el botón */', { size: 11.5 });
  d.card(s, 6.5, 2.86, 6.15, 2.5, { fill: C.soft });
  d.text(s, 'header', { x: 6.72, y: 2.95, w: 2, h: 0.26, size: 10.5, bold: true, color: C.teal, font: MONO });
  s.addShape(d.p.shapes.ROUNDED_RECTANGLE, { x: 6.75, y: 3.35, w: 5.65, h: 1.0, rectRadius: 0.08, fill: { color: C.white }, line: { color: C.teal, width: 1.5, dashType: 'dash' } });
  [['h1', 6.95, 1.3], ['nav', 8.85, 1.55], ['a (botón)', 10.85, 1.35]].forEach(([t, x, w]) => {
    d.card(s, x, 3.55, w, 0.6, { fill: C.primary, line: C.primary, r: 0.06 });
    d.text(s, t, { x, y: 3.55, w, h: 0.6, size: 12, bold: true, color: C.white, align: 'center', font: MONO });
  });
  d.text(s, 'Los tres hijos quedan en fila, centrados en vertical y separados hacia los extremos.', { x: 6.75, y: 4.5, w: 5.65, h: 0.7, size: 11, color: C.body, valign: 'top' });
  d.callout(s, 5.62, 0.8, 'Error frecuente:', 'escribir `display: flex` en los hijos en vez del padre. La propiedad ordena a los hijos de quien la lleva, no a la etiqueta misma.', { fill: C.white, leadColor: C.red });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Flexbox', 'Los dos ejes', 'El eje principal sigue el Flujo. El eje cruzado es el otro.');
  const box = (x, dir, titulo, mainLbl, crossLbl) => {
    d.card(s, x, 2.86, 5.85, 3.2);
    d.text(s, titulo, { x: x + 0.3, y: 2.98, w: 5.3, h: 0.3, size: 13, bold: true, color: C.ink, font: MONO });
    const cx = x + 0.6; const cy = 3.55;
    s.addShape(d.p.shapes.RECTANGLE, { x: cx, y: cy, w: 4.6, h: 2.2, fill: { color: 'F3F4F6' }, line: { color: '9CA3AF', width: 1, dashType: 'dash' } });
    ['A', 'B', 'C'].forEach((t, i) => {
      const bx = dir === 'row' ? cx + 0.25 + i * 0.85 : cx + 0.25; const by = dir === 'row' ? cy + 0.25 : cy + 0.2 + i * 0.62;
      d.card(s, bx, by, 0.7, 0.5, { fill: C.primary, line: C.primary, r: 0.06 });
      d.text(s, t, { x: bx, y: by, w: 0.7, h: 0.5, size: 12, bold: true, color: C.white, align: 'center' });
    });
    if (dir === 'row') {
      s.addShape(d.p.shapes.LINE, { x: cx + 0.25, y: cy + 1.25, w: 4.0, h: 0, line: { color: C.teal, width: 2.5, endArrowType: 'triangle' } });
      d.text(s, mainLbl, { x: cx + 0.25, y: cy + 1.3, w: 4.0, h: 0.28, size: 10.5, bold: true, color: C.teal });
      s.addShape(d.p.shapes.LINE, { x: cx + 4.3, y: cy + 0.15, w: 0, h: 1.9, line: { color: C.red, width: 2, endArrowType: 'triangle' } });
      d.text(s, crossLbl, { x: cx + 2.2, y: cy + 1.75, w: 2.0, h: 0.28, size: 10.5, bold: true, color: C.red, align: 'right' });
    } else {
      s.addShape(d.p.shapes.LINE, { x: cx + 1.2, y: cy + 0.2, w: 0, h: 1.85, line: { color: C.teal, width: 2.5, endArrowType: 'triangle' } });
      d.text(s, mainLbl, { x: cx + 1.3, y: cy + 0.9, w: 2.0, h: 0.28, size: 10.5, bold: true, color: C.teal });
      s.addShape(d.p.shapes.LINE, { x: cx + 0.25, y: cy + 2.05, w: 4.1, h: 0, line: { color: C.red, width: 2, endArrowType: 'triangle' } });
      d.text(s, crossLbl, { x: cx + 2.2, y: cy + 1.7, w: 2.1, h: 0.28, size: 10.5, bold: true, color: C.red, align: 'right' });
    }
  };
  box(0.7, 'row', 'flex-direction: row  (Flujo →)', 'eje principal: justify-content', 'eje cruzado: align-items');
  box(6.8, 'column', 'flex-direction: column  (Flujo ↓)', 'eje principal', 'eje cruzado: align-items');
  d.callout(s, 6.22, 0.62, 'La regla:', '`justify-content` siempre trabaja en el eje principal y `align-items` en el cruzado. Si cambias el Flujo, cambian de dirección.', { size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Flexbox', 'justify-content: el reparto en el eje principal', 'Cinco valores, el mismo contenedor. El más usado en tu portafolio: space-between.');
  d.image(s, IMG('justify.png'), 0.7, 2.86, 5.6, 4.02, { alt: 'Cinco valores de justify-content' });
  [['flex-start', 'Al inicio. Es el valor por defecto.'], ['center', 'Al centro: el menú del pie.'], ['flex-end', 'Al final.'], ['space-between', 'Hacia los extremos: el Espacio Auto de Figma. La cabecera y la barra de la tarjeta de código.'], ['space-around', 'El mismo espacio alrededor de cada uno.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.8;
    d.card(s, 6.5, y, 6.15, 0.72);
    d.text(s, a, { x: 6.72, y, w: 1.85, h: 0.72, size: 11.5, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 8.6, y, w: 3.9, h: 0.72, size: 10.5, color: C.body });
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Flexbox', 'align-items: la alineación en el eje cruzado', 'En una fila, align-items decide la posición vertical. Es la Alineación de Figma.');
  d.image(s, IMG('align.png'), 0.7, 2.86, 7.6, 3.6, { alt: 'Cuatro valores de align-items' });
  [['stretch', 'Por defecto: los ítems se estiran al alto de la fila.'], ['flex-start', 'Arriba. Contacto: el texto y la lista empiezan arriba.'], ['center', 'Al centro: la cabecera, el Hero y cada tarjeta de contacto.'], ['flex-end', 'Abajo.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.92;
    d.card(s, 8.5, y, 4.15, 0.82);
    d.text(s, a, { x: 8.72, y: y + 0.06, w: 3.8, h: 0.28, size: 11.5, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 8.72, y: y + 0.34, w: 3.8, h: 0.44, size: 10, color: C.body, valign: 'top' });
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Flexbox', 'flex: 1, anchos fijos y flex-wrap', 'Las propiedades de los ítems: cuánto crecen, cuánto miden y si bajan de línea.');
  d.image(s, IMG('flex1.png'), 0.7, 2.86, 7.3, 4.0, { alt: 'Ítems con flex: 1, ancho fijo y columna' });
  d.image(s, IMG('wrap.png'), 8.2, 2.86, 4.45, 2.6, { alt: 'Un menú sin flex-wrap y con flex-wrap' });
  d.card(s, 8.2, 5.62, 4.45, 1.24, { fill: C.soft });
  d.text(s, ['`flex: 1` → Llenar el contenedor', '`flex: 0 0 480px` → Ancho fijo 480', 'Sin `flex` → Ajustar al contenido'], { x: 8.42, y: 5.72, w: 4.1, h: 1.05, size: 11, color: C.body, valign: 'top', paraAfter: 3, codeColor: C.teal });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Flexbox', 'La Disposición automática es Flexbox', 'Cada control del panel derecho de Figma tiene su propiedad en CSS.');
  const L = [['Disposición automática', 'display: flex'], ['Flujo → o ↓', 'flex-direction'], ['Espacio', 'gap'], ['Espacio: Auto', 'justify-content: space-between'], ['Espaciado', 'padding'], ['Alineación', 'align-items']];
  const Rr = [['Ancho fijo · Altura fija', 'width · height'], ['Llenar el contenedor', 'flex: 1'], ['Ajustar al contenido', 'nada: es lo normal'], ['Relleno', 'background-color'], ['Recortar contenido', 'overflow: hidden'], ['Imagen en modo Llenar', 'object-fit: cover']];
  [L, Rr].forEach((col, k) => col.forEach(([a, b], i) => {
    const x = 0.7 + k * 6.1; const y = 2.86 + i * 0.6;
    d.card(s, x, y, 5.85, 0.52);
    d.text(s, a, { x: x + 0.22, y, w: 2.45, h: 0.52, size: 11.5, bold: true, color: C.ink });
    d.text(s, '→', { x: x + 2.62, y, w: 0.35, h: 0.52, size: 12, color: C.num, align: 'center' });
    d.text(s, b, { x: x + 3.0, y, w: 2.8, h: 0.52, size: 10.5, bold: true, color: C.teal, font: MONO });
  }));
  d.note(s, 6.55, 'Un marco con Disposición automática dentro de otro es un contenedor flex dentro de otro: un ítem que también es contenedor.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Flexbox', 'El Hero: flex dentro de flex', 'Los mismos marcos que tienes en Figma, ahora como contenedores flex.');
  const nodes = [
    [0, '.hero-section', 'fila · gap 64 · centro'],
    [1, '.hero-left', 'flex: 1 · columna · gap 32'],
    [2, '.hero-actions', 'fila · gap 16'],
    [1, '.hero-right', 'flex: 1 · max-width 520'],
    [2, '.code-header', 'fila · space-between'],
    [3, '.window-controls', 'fila · gap 8'],
  ];
  nodes.forEach(([lvl, n, dsc], i) => {
    const x = 0.7 + lvl * 0.55; const y = 2.86 + i * 0.6;
    d.card(s, x, y, 5.6 - lvl * 0.55, 0.52, { fill: lvl === 0 ? C.soft : C.white });
    d.text(s, n, { x: x + 0.2, y, w: 2.3, h: 0.52, size: 11.5, bold: true, color: C.teal, font: MONO });
    d.text(s, dsc, { x: x + 2.45, y, w: 3.0 - lvl * 0.55 + 0.5, h: 0.52, size: 10.5, color: C.body });
  });
  d.image(s, IMG('hero.png'), 6.55, 2.86, 6.1, 3.43, { alt: 'El Hero Section terminado' });
  d.note(s, 6.5, 'Cada fila es un marco con Disposición automática en tu Figma (Pasos 6 al 9).');
});

// ================= BLOQUE 03
d.divider('CONCEPTUAL', 'Grid', '03', ['Filas y columnas', 'La unidad fr y repeat()', 'grid-column', '¿Flexbox o Grid?']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Grid', 'Grid: filas y columnas', 'display: grid ordena a los hijos en una rejilla. Tú decides las columnas.');
  d.code(s, 0.7, 2.86, 5.3, 2.1, '«.projects-grid» {\n  display: grid;\n  grid-template-columns: repeat(2, 1fr);\n  gap: 24px;            /* Espacio 24 */\n}', { size: 12 });
  d.image(s, IMG('proyectos.png'), 6.2, 2.86, 6.45, 2.4, { alt: 'Proyectos en dos columnas iguales' });
  [['grid-template-columns', 'Cuántas columnas y cuánto mide cada una.'], ['gap', 'La separación entre columnas y entre filas.'], ['los hijos', 'Se colocan solos, celda por celda, de izquierda a derecha.']].forEach(([a, b], i) => {
    const y = 5.15 + i * 0.5;
    d.card(s, 0.7, y, 5.3, 0.44);
    d.text(s, a, { x: 0.92, y, w: 2.3, h: 0.44, size: 10.5, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 3.2, y, w: 2.7, h: 0.44, size: 10, color: C.body });
  });
  d.callout(s, 5.45, 1.1, 'Las dos tarjetas miden lo mismo', 'aunque una tenga más texto: la rejilla reparte el ancho, no el contenido.', { x: 6.2, w: 6.45, size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Grid', 'La unidad fr y repeat()', 'fr es una fracción del espacio libre. Se puede mezclar con medidas fijas.');
  d.image(s, IMG('gridfr.png'), 0.7, 2.86, 6.1, 3.78, { alt: 'Cuatro rejillas con distintas columnas' });
  [['1fr 1fr', 'Dos columnas iguales.'], ['repeat(2, 1fr)', 'Lo mismo, sin repetir. Proyectos y el formulario.'], ['315px 1fr', 'Una fija y otra con todo lo que sobra. La multimedia de Sobre mí.'], ['2fr 1fr', 'La primera mide el doble que la segunda.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.95;
    d.card(s, 7.0, y, 5.65, 0.85);
    d.text(s, a, { x: 7.22, y: y + 0.06, w: 5.2, h: 0.3, size: 12, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 7.22, y: y + 0.38, w: 5.2, h: 0.42, size: 10.5, color: C.body, valign: 'top' });
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Grid', 'grid-column: que un hijo ocupe varias columnas', 'Las líneas de la rejilla se numeran desde 1. La última también se llama -1.');
  d.image(s, IMG('gridform.png'), 0.7, 2.86, 6.9, 2.7, { alt: 'Formulario en rejilla con los botones ocupando las dos columnas' });
  d.code(s, 7.8, 2.86, 4.85, 2.7, '«.form-grid» {\n  display: grid;\n  grid-template-columns:\n    repeat(2, 1fr);\n  gap: 24px;\n}\n«.form-actions» {\n  grid-column: 1 / -1;\n}', { size: 11.5 });
  d.callout(s, 5.8, 0.75, 'grid-column: 1 / -1', 'se lee «desde la primera línea hasta la última»: el párrafo de los botones ocupa toda la fila, tenga la rejilla dos o tres columnas.', { size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Grid', '¿Flexbox o Grid?', 'Los dos conviven en la misma página. Elige según la forma del problema.');
  d.twoCards(s, { t: 'Flexbox: una dimensión', color: C.teal, items: ['Una fila o una columna de elementos.', 'Cada uno mide lo que su contenido, o crece con `flex: 1`.', 'En tu portafolio: cabecera, menú, Hero, botones, tarjetas de contacto y pie.'] },
    { t: 'Grid: dos dimensiones', color: C.ink, items: ['Filas y columnas que deben alinearse.', 'Las columnas se definen en el padre, con `fr`.', 'En tu portafolio: la cuadrícula de proyectos, el formulario y la multimedia.'] }, { h: 2.4, lfill: C.white, rfill: C.soft });
  d.callout(s, 5.5, 0.9, 'Pregunta rápida:', '¿El diseño es una sola fila o columna de cosas? Flexbox. ¿Es una cuadrícula de piezas iguales? Grid. Si dudas, empieza con Flexbox: es lo que hace Figma.');
});

d.breakSlide('Al volver terminamos el diseño en Figma (Pasos 12 al 14) y construimos el Hero. Ten abiertos tu carpeta y tu archivo de Figma.');

// ================= INSTRUMENTAL
d.imageSlide('cinfo-03-instrumental.jpg', 'Instrumental: aplicación del conocimiento con ejercicios y demostraciones');

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '04 · Figma', 'En Figma hoy: Contacto, pie e imágenes (Pasos 12 al 14)', 'Cada paso está en la Guía de Figma de la sesión. Con esto tu diseño queda completo.');
  d.numCards(s, [
    { t: 'contact-section', d: 'Los mismos valores que Sobre mí y Proyectos: Flujo vertical, Espaciado 80 y 100, Espacio 48.' },
    { t: 'contact-text', d: 'Título Contacto en Outfit ExtraBold 36 y el texto, en un marco en Llenar el contenedor.' },
    { t: 'contact-card × 3', d: 'Filas de 520 × 84, Espaciado 20, Espacio 16, Radio 8 y un círculo de 44 × 44.' },
    { t: 'contact-content', d: 'Junta los dos lados con Flujo horizontal y Espacio 64.' },
    { t: 'footer-wrapper', d: 'Altura fija 182, Espaciado 80 y 48, Espacio 24 y Trazo solo superior.' },
    { t: 'Paso 14 · Imágenes', d: 'En Relleno, Sólido pasa a Imagen en modo Llenar. Solo las dos tarjetas de proyectos.' },
  ]);
  d.note(s, 6.62, 'Revisión final: mi-portafolio en Ajustar al contenido para ver su altura real, y de vuelta a Altura fija 2816.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '04 · Figma', 'Contacto y pie: del panel al código', 'Selecciona cada marco y lee su Disposición automática.');
  d.mapRows(s, [['contact-content · Flujo →, Espacio 64', 'display: flex;  gap: 64px;'], ['contact-list · Flujo ↓, Ancho fijo 520, Espacio 16', 'flex: 0 0 520px;  flex-direction: column;'], ['contact-card · Espaciado 20, Alineación centro', 'padding: 20px;  align-items: center;'], ['Icono 44 × 44, Relleno 06B6C4', 'width: 44px;  border-radius: 50%;'], ['footer-wrapper · Flujo ↓, centro, Espacio 24', 'flex-direction: column;  gap: 24px;'], ['Imagen en modo Llenar', 'object-fit: cover;']], { heads: ['En Figma', 'En CSS'], csize: 11.5 });
});

// ================= El Hero
d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · El Hero', 'El Hero: las medidas que usarás', 'Pasos 6 al 9 del manual. Si tu CSS no coincide con tu Figma, manda Figma.');
  d.mapRows(s, [['hero-section · Espacio 64', 'gap: 64px;'], ['hero-section · Espaciado 160 · 80 · 100 · 80', 'padding: 160px 80px 100px 80px;'], ['hero-left · Ancho 696 y Espacio 32', 'max-width: 696px;   gap: 32px;'], ['Título · Outfit ExtraBold 64, altura 110 %', 'font-size: 64px;   line-height: 1.1;'], ['Botón · Espaciado 14 y 24, Radio 8', 'padding: 14px 24px;   border-radius: 8px;'], ['hero-right · Ancho 520, Radio 12, Recortar', 'max-width: 520px;   overflow: hidden;']], { heads: ['En Figma', 'En index.css'] });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · El Hero', 'Construimos juntos: el HTML del Hero', 'Dentro de <main> de index.html. Cada div tiene el nombre de su capa en Figma.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<section «class="hero-section"»>\n  <div «class="hero-left"»>\n    <h2 class="hero-title">Formando a la próxima…</h2>\n    <p class="hero-description">Docente e Ingeniero…</p>\n    <div «class="hero-actions"»>\n      <a href="mis-proyectos.html" class="btn btn-primary">…</a>\n      <a href="contactame.html" class="btn btn-secondary">…</a>\n    </div>\n  </div>\n  <div «class="hero-right"»>\n    <div class="code-card">\n      <div class="code-header"> … </div>\n      <pre class="code-body"><code>…</code></pre>\n    </div>\n  </div>\n</section>', { size: 10.5 });
  d.steps(s, [['Enlaza', 'index.css, después de global y header.'], ['Sección', 'section.hero-section dentro de main.'], ['Izquierda', 'Título h2, párrafo y botones.'], ['Botones', 'Dos enlaces con la clase btn.'], ['Derecha', 'La tarjeta de código.'], ['Revisa', 'El texto completo está en la guía, Paso 1.']], { tw: 1.1 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · El Hero', 'Construimos juntos: index.css', 'Primero las dos columnas; después la columna izquierda y los botones.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '«.hero-section» {\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  gap: 64px;\n  padding: 160px 80px 100px 80px;\n  max-width: 1440px;\n  margin: 0 auto;\n}\n«.hero-left» {\n  flex: 1;\n  max-width: 696px;\n  display: flex;\n  flex-direction: column;\n  gap: 32px;\n}\n«.hero-actions» { display: flex; gap: 16px; }', { size: 10 });
  d.steps(s, [['Fila', '.hero-section: display flex y gap 64.'], ['Centro', 'align-items: center alinea las columnas.'], ['Espaciado', 'padding con los cuatro valores de Figma.'], ['Columna', '.hero-left: flex 1 y flex-direction column.'], ['Botones', '.hero-actions en fila con gap 16.'], ['Estilo', '.btn, .btn-primary y .btn-secondary.']], { tw: 1.1 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · El Hero', 'La tarjeta de código: tres flex anidados', 'Los mismos valores del Paso 9 del manual.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '«.code-card» {\n  border: 1px solid var(--color-border);\n  border-radius: var(--radius-md);\n  overflow: hidden;           /* Recortar contenido */\n}\n«.code-header» {\n  display: flex;\n  align-items: center;\n  justify-content: space-between;   /* Espacio Auto */\n  padding: 12px 16px;\n}\n«.window-controls» { display: flex; gap: 8px; }\n«.dot» {\n  width: 10px; height: 10px;\n  border-radius: 50%;\n  display: inline-block;      /* un span no acepta width */\n}', { size: 10 });
  d.image(s, IMG('hero.png'), 7.8, 2.86, 4.85, 2.73, { alt: 'El Hero Section terminado' });
  d.callout(s, 5.75, 0.97, 'En el celular:', 'una media query cambia `flex-direction` a `column` y las dos columnas se apilan. Lo verás a fondo en la sesión 12.', { x: 7.8, w: 4.85, size: 11 });
});

// ================= Páginas interiores
d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Páginas interiores', 'Sobre mí y Proyectos', 'Primero la caja de 1440; después las dos columnas.');
  d.code(s, 0.7, 2.86, 5.85, 3.98, '«main» {\n  max-width: 1440px;\n  margin: 0 auto;\n  padding: 6.25rem 5rem;\n}\n«.about-content» {\n  display: flex;\n  align-items: center;\n  gap: 64px;\n}\n«.about-text» { flex: 1; }\n«.about-content aside» { flex: 0 0 480px; }\n\n«.projects-grid» {\n  display: grid;\n  grid-template-columns: repeat(2, 1fr);\n  gap: 24px;\n}', { size: 10 });
  d.image(s, IMG('about.png'), 6.75, 2.86, 5.9, 1.9, { alt: 'Sobre mí a dos columnas' });
  d.image(s, IMG('proyectos.png'), 6.75, 4.88, 5.9, 2.1, { alt: 'Proyectos en rejilla' });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Páginas interiores', 'La tarjeta de proyecto', 'Una imagen de borde a borde y el texto con Espaciado 24.');
  d.code(s, 0.7, 2.86, 6.4, 3.5, '«.project-card» {\n  padding: 0;             /* gana a «article»: es una clase */\n  overflow: hidden;       /* Recortar contenido */\n}\n«.project-image» {\n  display: block;         /* sin hueco debajo */\n  width: 100%;\n  height: 220px;\n  object-fit: cover;      /* modo Llenar */\n  border-radius: 0;\n}\n«.project-text» { padding: 24px; }', { size: 10.5 });
  [['overflow: hidden', 'La imagen respeta las esquinas redondeadas de la tarjeta.'], ['object-fit: cover', 'Llena la caja de 220 sin deformarse: lo que sobra se recorta.'], ['display: block', 'Una imagen es inline y deja un hueco de unos píxeles debajo.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.9;
    d.card(s, 7.3, y, 5.35, 0.8);
    d.text(s, a, { x: 7.52, y: y + 0.06, w: 4.9, h: 0.28, size: 11.5, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 7.52, y: y + 0.36, w: 4.9, h: 0.4, size: 10.5, color: C.body, valign: 'top' });
  });
  d.callout(s, 5.62, 0.74, 'Imágenes del paquete:', 'dos vistas de ejemplo de 1256 × 440. Cámbialas por capturas de tus proyectos cuando las tengas.', { x: 7.3, w: 5.35, size: 10.5 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Páginas interiores', 'Ahora tú: Contacto y el formulario', 'Tienes 25 minutos. Sigue el Paso 6 de la guía de código.');
  d.numCards(s, [
    { t: 'Las clases', d: 'contact-section, contact-content, contact-text, contact-list y contact-card en el HTML.' },
    { t: 'Dos lados', d: '.contact-content con display: flex y gap: 64px; .contact-text con flex: 1.' },
    { t: 'La lista', d: '.contact-list: flex 0 0 520px, en columna, gap 16.' },
    { t: 'Cada fila', d: '.contact-card en fila, centrada, padding 20, borde y radio 8.' },
    { t: 'El círculo', d: '44 × 44, border-radius 50% y flex para centrar la letra.' },
    { t: 'El formulario', d: '.form-grid con dos columnas y .form-actions con grid-column: 1 / -1.' },
  ]);
  d.note(s, 6.62, 'Si terminas antes: la rejilla de la multimedia en Sobre mí, con grid-template-columns: 315px 1fr.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Páginas interiores', 'Compruébalo en el celular', 'En DevTools, pulsa Ctrl + Shift + M y elige un teléfono. Ninguna página debe desplazarse hacia los lados.');
  [['movil-index.png', 'Inicio: el Hero se apila'], ['movil-proyectos.png', 'Proyectos: una columna'], ['movil-contacto.png', 'Contacto: la lista debajo']].forEach(([f, t], i) => {
    const x = 0.95 + i * 2.35;
    d.image(s, IMG(f), x, 2.86, 2.05, 3.55, { alt: t, pad: 0.05 });
    d.text(s, t, { x: x - 0.1, y: 6.45, w: 2.25, h: 0.28, size: 10.5, bold: true, color: C.sub, align: 'center' });
  });
  d.card(s, 8.1, 2.86, 4.55, 3.55, { fill: C.soft });
  d.text(s, 'Por qué ya funciona', { x: 8.35, y: 3.0, w: 4.1, h: 0.32, size: 13, bold: true, color: C.teal });
  d.text(s, ['Las media queries de la guía cambian `flex-direction` a `column` y las rejillas a `1fr`.', 'Las medidas usan `max-width`, no `width`: las cajas pueden encogerse.', 'Las imágenes y los videos tienen `max-width: 100%`.'], { x: 8.35, y: 3.42, w: 4.1, h: 2.85, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 6, codeColor: C.ink });
});

// ================= NIVELADOR
d.imageSlide('cinfo-04-nivelador.jpg', 'Nivelador: nivel de comprensión del estudiante');
d.checklist('NIVELADOR', [
  'Distingo contenido, padding, borde y margen en DevTools.',
  'Sé por qué box-sizing: border-box hace que las medidas sean las de Figma.',
  'Sé cuándo un elemento es block, inline o inline-block.',
  'Escribo display: flex en el contenedor, no en los hijos.',
  'Sé qué hacen justify-content y align-items en una fila y en una columna.',
  'Puedo hacer que una columna llene el espacio y otra tenga ancho fijo.',
  'Puedo repartir tarjetas en columnas iguales con Grid y fr.',
  'Puedo leer una Disposición automática de Figma y escribirla en CSS.',
]);
d.consultas('NIVELADOR', [['¿Flex o Grid?', '¿Cuál uso para mis tarjetas?'], ['¿No se alinea?', 'Escribí justify-content y no pasa nada.'], ['¿margin o gap?', '¿Cuál separa mejor los elementos?'], ['¿Se desborda?', 'En el celular aparece una barra lateral.']],
  'Cuando la maquetación no sale', 'Revisa en este orden: que `display: flex` o `grid` esté en el padre, la dirección del eje (`flex-direction`), los anchos fijos sin `max-width` y, al final, la caja en DevTools: el modo de inspección resalta flex y grid con etiquetas.');

// ================= FUNCIONAL
d.imageSlide('cinfo-05-funcional.jpg', 'Funcional: aplicar lo aprendido');
d.tarea([
  'Termina el Hero (index.html e index.css) y Proyectos con Grid.',
  'Pasa Sobre mí y Contacto a dos columnas; el formulario, a rejilla.',
  'Comprueba en DevTools que ninguna página se desplace hacia los lados en el celular.',
  'En Figma: Pasos 12 al 14 y la revisión final de la página.',
  'Valida el HTML y el CSS sin errores y publica en Netlify.',
], ['Subir la URL publicada al Aula Virtual.', 'Adjuntar captura del validador W3C sin errores.', 'El envío es obligatorio dentro del plazo establecido.', 'Se registra en ClassDojo como participación en clase.']);

// ================= ORIENTADOR
d.imageSlide('cinfo-06-orientador.jpg', 'Orientador: conclusión del tema');
d.resumen([
  'Toda etiqueta es una caja: contenido, padding, borde y margen.',
  'Con `box-sizing: border-box` el ancho incluye el padding y el borde, como en Figma.',
  '`display` decide si una caja ocupa la línea entera, va en el texto o ordena a sus hijos.',
  'Flexbox ordena en una dimensión: `justify-content` en el eje principal y `align-items` en el cruzado.',
  '`flex: 1` es Llenar el contenedor; `flex: 0 0 480px`, un Ancho fijo.',
  'Grid ordena en dos dimensiones con `grid-template-columns` y la unidad `fr`.',
  'Cada Disposición automática de Figma se escribe como `display: flex`.',
  'Tu diseño está completo en Figma y tu portafolio ya tiene su distribución.',
]);
d.hacia('Tu portafolio ya tiene estructura, estilos y distribución. Lo que viene.', [
  ['SESIÓN 09', 'CSS3', 'Selectores, cascada, color y bordes.'],
  ['SESIÓN 10', 'Maquetación', 'Modelo de caja, Flexbox y Grid.', true],
  ['SESIÓN 11', 'Animaciones', 'Transformaciones y transiciones.'],
  ['SESIÓN 12', 'Responsive', 'Media queries y el Taller TA2.'],
  ['SESIÓN 13', 'Bootstrap', 'Introducción y su sistema de grillas.'],
], 'Para la sesión 11: trae tu portafolio publicado con el Hero y las dos columnas. Le daremos movimiento con transiciones. Ojo: el jueves 22 es el Taller TA2, sobre diseño responsivo.');

require('fs').mkdirSync(path.dirname(out), { recursive: true });
d.save(out).then((n) => console.log('ok', n, 'diapositivas →', out));
