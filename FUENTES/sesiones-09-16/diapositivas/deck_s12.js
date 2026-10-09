// Sesión 12 · Diseño web responsivo + Taller online TA2
const path = require('path');
const { Deck, C, MONO } = require('./uss.js');
const { place } = require('./fit.js');
const IMG = (f) => path.join(__dirname, 'img', f);
const out = process.argv[2] || path.join(__dirname, 'out', 'Sesion12-Diseno-Responsivo-TA2.pptx');

const d = new Deck({ title: 'Sesión 12 · Diseño web responsivo y Taller TA2' });

d.waiting('12', 'Abre tu portafolio en Chrome con DevTools. Hoy lo pruebas en el celular. Al final: Taller TA2.');
d.title({
  titulo: 'Diseño web responsivo',
  sesion: '12',
  sub: 'viewport · media queries · clamp() · auto-fit · aspect-ratio · Taller TA2',
  code: '@media (max-width: 600px) {\n  .hero-actions {\n    flex-direction: column;\n  }\n}',
});
d.imageSlide('como-te-sientes.jpg', '¿Cómo te sientes hoy?');
d.imageSlide('que-es-cinfo.jpg', '¿Qué es CINFO? Conceptual, Instrumental, Nivelador, Funcional y Orientador');
d.imageSlide('conocimientos-previos.jpg', 'Conocimientos previos y definiciones clave');

d.add('CONCEPTUAL', (s) => {
  d.header(s, 'Repaso', 'De dónde venimos', 'Tu portafolio se ve como tu diseño de 1440. Falta que se vea bien en un celular.');
  d.twoCards(s, { t: 'Ya tienes', color: C.sub, items: ['Estilos, Flexbox y Grid con las medidas de Figma.', 'Transiciones, transform y la entrada del Hero.', 'Unas media queries «de anticipo» copiadas en la sesión 10.'] },
    { t: 'Hoy sumas', items: ['Probar tu página en tres anchos con DevTools.', 'Escribir y ordenar tus propias media queries.', 'Medidas fluidas que se adaptan sin media query.'] });
  d.callout(s, 5.18, 1.42, 'Hoy también es el Taller TA2', '\nLa última hora es el Taller online TA2 (15 % de la nota final): aplicar CSS y diseño responsivo a tu sitio del TA1 o a tu portafolio. Todo lo que veas hoy entra en el taller.');
});

d.logros([
  ['Probar', 'Revisar una página a 1440, 820 y 390 px con el modo dispositivo de DevTools.'],
  ['Condicionar', 'Escribir media queries con `max-width` y ponerlas en el lugar correcto.'],
  ['Fluir', 'Usar `clamp()`, `min()` y `vw` para que una medida crezca con la pantalla.'],
  ['Adaptar', 'Hacer una rejilla con `auto-fit` y multimedia que conserve su proporción.'],
  ['Diseñar', 'Construir en Figma la versión móvil de la página en un marco de 390.'],
]);

d.agenda([
  ['01', 'Qué es el diseño responsivo', 'Tres pantallas, la etiqueta viewport y DevTools.', 20],
  ['02', 'Media queries', '@media, puntos de quiebre y el orden de las reglas.', 40],
  ['03', 'Técnicas fluidas', 'clamp(), auto-fit, aspect-ratio y tablas.', 30],
  ['—', 'Descanso', '', 15],
  ['04', 'Figma: la versión móvil', 'El marco de 390 y los cambios de Flujo.', 25],
  ['05', 'Práctica en tu portafolio', 'El Hero, Proyectos, la tabla y el video.', 40],
  ['06', 'Taller online TA2', 'Actividad evaluada: 15 % de la nota final.', 50],
]);

// ================= BLOQUE 01
d.divider('CONCEPTUAL', 'Diseño responsivo', '01', ['Una página, muchas pantallas', 'La etiqueta viewport', 'Probar en DevTools', 'Los puntos de quiebre']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Diseño responsivo', 'Una página, tres pantallas', 'El mismo HTML y el mismo CSS. Cambia el ancho de la ventana y el diseño se acomoda.');
  const H = 3.3; const L = [['s12-escritorio.png', 'Escritorio · 1440 px', 1440 / 900, 'Tu diseño de Figma tal cual.'], ['s12-tablet.png', 'Tablet · 820 px', 820 / 1180, 'Una columna, salvo Proyectos.'], ['s12-celular.png', 'Celular · 390 px', 390 / 844, 'El menú bajo el nombre.']];
  const ws = L.map(([, , r]) => (H - 0.16) * r + 0.16);
  let x = 0.7 + (11.95 - ws.reduce((a, b) => a + b) - 0.6) / 2;
  L.forEach(([f, t, , dsc], i) => {
    d.image(s, IMG(f), x, 2.86, ws[i], H, { alt: t });
    d.text(s, t, { x: x - 0.3, y: 6.24, w: ws[i] + 0.6, h: 0.28, size: 11.5, bold: true, color: C.ink, align: 'center' });
    d.text(s, dsc, { x: x - 0.4, y: 6.52, w: ws[i] + 0.8, h: 0.26, size: 10.5, color: C.sub, align: 'center' });
    x += ws[i] + 0.3;
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Diseño responsivo', 'La etiqueta viewport', 'Sin ella, el celular finge una pantalla de unos 980 px y muestra la página en miniatura.');
  const H = 3.75; const w = (H - 0.16) * (390 / 844) + 0.16;
  d.image(s, IMG('s12-sin-viewport.png'), 0.7, 2.86, w, H, { alt: 'Portada en un celular sin la etiqueta viewport' });
  d.text(s, 'Sin viewport', { x: 0.7, y: 6.66, w, h: 0.26, size: 11, bold: true, color: C.red, align: 'center' });
  d.image(s, IMG('s12-con-viewport.png'), 0.95 + w, 2.86, w, H, { alt: 'Portada en un celular con la etiqueta viewport' });
  d.text(s, 'Con viewport', { x: 0.95 + w, y: 6.66, w, h: 0.26, size: 11, bold: true, color: C.teal, align: 'center' });
  const x = 1.3 + 2 * w;
  d.code(s, x, 2.86, 12.65 - x, 1.05, '<meta «name="viewport"»\n  content="width=device-width, initial-scale=1.0" />', { size: 11.5, valign: 'middle' });
  [['width=device-width', 'Usa el ancho real del celular.'], ['initial-scale=1.0', 'Sin zoom inicial: la página no se achica.']].forEach(([a, b], i) => {
    const y = 4.08 + i * 0.63;
    d.card(s, x, y, 12.65 - x, 0.55);
    d.text(s, a, { x: x + 0.22, y, w: 2.5, h: 0.55, size: 12, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: x + 2.8, y, w: 12.65 - x - 3.0, h: 0.55, size: 11.5, color: C.body });
  });
  d.callout(s, 5.45, 1.15, 'Ya la tienes:', 'está en el `<head>` de tus cuatro páginas desde la sesión 01. Sin ella, ninguna media query de 600 px se activaría en un celular.', { x, w: 12.65 - x, size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Diseño responsivo', 'Prueba tu página como si fuera un celular', 'El modo dispositivo de DevTools: la herramienta de toda la sesión.');
  d.numCards(s, [
    { t: 'Abre DevTools', d: 'En Chrome, `F12` sobre tu `index.html`.' },
    { t: 'Modo dispositivo', d: '`Ctrl + Shift + M` o el icono del celular, arriba a la izquierda.' },
    { t: 'Responsive', d: 'En **Dimensions**, elige Responsive y escribe `390` de ancho.' },
    { t: 'Tres anchos', d: 'Recorre las cuatro páginas a `390`, `820` y `1440`.' },
    { t: 'Arrastra', d: 'Mueve el borde de la página de 1440 a 320: el diseño cambia sin cortes.' },
    { t: 'Busca la barra', d: 'Si aparece desplazamiento horizontal, algo sobresale: anótalo.' },
  ]);
  d.note(s, 6.62, 'Al final, abre la página publicada en tu propio celular: es la prueba definitiva.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Diseño responsivo', 'Los puntos de quiebre', 'No se diseña para cada celular. Se eligen unos anchos y se corrige donde el diseño se rompe.');
  const x0 = 0.7; const W = 11.95; const X = (v) => x0 + (v / 1440) * W;
  [[0, 600, 'Celular', 'hasta 600 px', C.teal], [600, 992, 'Tablet', '601 a 992 px', '4FA3AC'], [992, 1440, 'Escritorio', 'más de 992 px', C.ink]].forEach(([a, b, t, r, col]) => {
    d.card(s, X(a) + 0.03, 2.95, X(b) - X(a) - 0.06, 0.72, { fill: col, line: col, r: 0.08 });
    d.text(s, t, { x: X(a), y: 2.95, w: X(b) - X(a), h: 0.42, size: 14, bold: true, color: C.white, align: 'center' });
    d.text(s, r, { x: X(a), y: 3.33, w: X(b) - X(a), h: 0.3, size: 10.5, color: C.white, align: 'center' });
  });
  [600, 992].forEach((v) => {
    s.addShape(d.p.shapes.LINE, { x: X(v), y: 2.8, w: 0, h: 1.05, line: { color: C.red, width: 2, dashType: 'dash' } });
    d.text(s, `${v}px`, { x: X(v) - 0.6, y: 3.86, w: 1.2, h: 0.26, size: 11, bold: true, color: C.red, align: 'center', font: MONO });
  });
  const col = (a, b, items) => d.text(s, items, { x: X(a) + 0.12, y: 4.3, w: X(b) - X(a) - 0.24, h: 1.6, size: 10.5, color: C.body, valign: 'top', bullet: true, paraAfter: 3, codeColor: C.ink });
  col(0, 600, ['El menú baja bajo el nombre.', 'Los botones del Hero, a todo el ancho.', 'Márgenes de 16 px.']);
  col(600, 992, ['Una columna en Sobre mí y Contacto.', 'Proyectos sigue en dos.', 'Márgenes de 24 px.']);
  col(992, 1440, ['Tu diseño de Figma tal cual.', 'Ninguna media query actúa.']);
  d.callout(s, 6.0, 0.7, 'Anótalos en global.css:', 'una variable no funciona dentro de `@media`; por eso 992 y 600 se escriben como número en cada hoja.', { size: 11.5 });
});

// ================= BLOQUE 02
d.divider('CONCEPTUAL', 'Media queries', '02', ['Cómo se escribe @media', 'Escritorio primero o celular primero', 'El orden de las reglas', 'Más allá del ancho']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Media queries', 'Cómo se escribe una media query', 'Una regla condicional: lo que va entre sus llaves solo se aplica si se cumple la condición.');
  d.code(s, 0.7, 2.86, 5.6, 2.3, '«@media (max-width: 992px)» {\n  /* solo si la ventana mide\n     992px o menos */\n  .hero-section {\n    flex-direction: column;\n  }\n}', { size: 12.5 });
  d.rows(s, [
    { a: '@media', b: 'Empieza la regla condicional.' },
    { a: 'max-width', b: 'Hasta ese ancho. `min-width`: desde ese ancho.' },
    { a: 'Lo de dentro', b: 'Solo las propiedades que cambian. El resto viene de la regla de fuera.' },
    { a: 'Dónde va', b: 'Al final de la hoja, después de las reglas que corrige.' },
  ], { y: 5.32, h: 0.38, gap: 0.05, aw: 1.9, asize: 11.5, bsize: 11 });
  place(d, s, IMG('s12-tablet.png'), 6.5, 2.86, 6.15, 2.3, { valign: 'top' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Media queries', 'Escritorio primero o celular primero', 'Las dos funcionan. Cambia cuál es el punto de partida.');
  d.card(s, 0.7, 2.86, 5.85, 3.1, { fill: C.white });
  d.text(s, 'Escritorio primero · max-width', { x: 1.0, y: 2.98, w: 5.3, h: 0.32, size: 13.5, bold: true, color: C.teal });
  d.code(s, 1.0, 3.4, 5.25, 1.5, '«.projects-grid» { /* dos columnas */ }\n\n«@media (max-width: 600px)» {\n  .projects-grid { /* una */ }\n}', { size: 10.5 });
  d.text(s, 'La regla normal es la del escritorio. Es el enfoque de tu portafolio, porque tu diseño nació en un marco de 1440.', { x: 1.0, y: 5.0, w: 5.25, h: 0.85, size: 11, color: C.body, valign: 'top' });
  d.card(s, 6.8, 2.86, 5.85, 3.1, { fill: C.soft });
  d.text(s, 'Celular primero · min-width', { x: 7.1, y: 2.98, w: 5.3, h: 0.32, size: 13.5, bold: true, color: C.ink });
  d.code(s, 7.1, 3.4, 5.25, 1.5, '«.projects-grid» { /* una columna */ }\n\n«@media (min-width: 600px)» {\n  .projects-grid { /* dos */ }\n}', { size: 10.5 });
  d.text(s, 'La regla normal es la del celular y se añaden columnas al crecer. Es el enfoque de Bootstrap: lo verás en la sesión 13.', { x: 7.1, y: 5.0, w: 5.25, h: 0.85, size: 11, color: C.body, valign: 'top' });
  d.callout(s, 6.12, 0.62, 'No las mezcles:', 'elige un enfoque por proyecto. En el TA2 puedes usar cualquiera de los dos.', { size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Media queries', 'El orden de las reglas', 'Una media query no tiene más especificidad: gana por estar escrita después.');
  d.card(s, 0.7, 2.86, 5.85, 3.0, { fill: C.white });
  d.text(s, '✗  La media query arriba', { x: 1.0, y: 2.98, w: 5.3, h: 0.32, size: 13.5, bold: true, color: C.red });
  d.code(s, 1.0, 3.4, 5.25, 1.7, '«@media (max-width: 600px)» {\n  .hero-title { font-size: 40px; }\n}\n«.hero-title» {\n  font-size: 64px;   /* gana siempre */\n}', { size: 10.5 });
  d.text(s, 'En el celular sigue midiendo 64: la regla de abajo la pisa.', { x: 1.0, y: 5.2, w: 5.25, h: 0.5, size: 11, color: C.body, valign: 'top' });
  d.card(s, 6.8, 2.86, 5.85, 3.0, { fill: C.soft });
  d.text(s, '✓  La media query al final', { x: 7.1, y: 2.98, w: 5.3, h: 0.32, size: 13.5, bold: true, color: C.teal });
  d.code(s, 7.1, 3.4, 5.25, 1.7, '«.hero-title» {\n  font-size: 64px;\n}\n«@media (max-width: 600px)» {\n  .hero-title { font-size: 40px; }\n}', { size: 10.5 });
  d.text(s, 'En el celular mide 40; en el escritorio, 64.', { x: 7.1, y: 5.2, w: 5.25, h: 0.5, size: 11, color: C.body, valign: 'top' });
  d.callout(s, 6.05, 0.62, 'Otro error común:', 'olvidar la llave de cierre de `@media`. Todo lo que sigue queda dentro de la condición.', { size: 11.5, leadColor: C.red });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Media queries', 'Más allá del ancho', 'Una media query también pregunta por la pantalla y por las preferencias de la persona.');
  d.rows(s, [
    { a: '(max-width: 600px)', b: 'La ventana mide 600 px o menos.', c: 'Tus dos puntos de quiebre' },
    { a: '(orientation: landscape)', b: 'La pantalla es más ancha que alta.', c: 'Un celular girado' },
    { a: '(hover: hover)', b: 'Hay un puntero que puede quedarse encima.', c: 'En un celular no se cumple' },
    { a: '(prefers-reduced-motion)', b: 'La persona pidió menos animaciones.', c: 'Ya lo usas: sesión 11' },
    { a: '(prefers-color-scheme: dark)', b: 'La persona usa el modo oscuro.', c: 'Un tema oscuro para tu sitio' },
    { a: 'print', b: 'La página se está imprimiendo.', c: '`@media print { … }`' },
  ], { aw: 3.4, bw: 4.3, asize: 11.5, bsize: 11.5, csize: 11, h: 0.56, gap: 0.08 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Media queries', 'La cabecera y el pie en el celular', 'header.css, bloque 6. El nombre y el menú ya no caben en una fila de 80.');
  d.code(s, 0.7, 2.86, 6.9, 3.75, '«@media (max-width: 992px)» {\n  header { padding: 0 24px; }\n  footer { padding: 48px 24px; }\n}\n\n«@media (max-width: 600px)» {\n  header {\n    height: auto;          /* pierde la altura fija */\n    flex-wrap: wrap;       /* el menú baja de línea */\n    justify-content: center;\n    gap: 12px;\n    padding: 16px;\n  }\n  header > a[href="contactame.html"] { display: none; }\n  footer { padding: 48px 16px; }\n}', { size: 10.5 });
  const H = 3.75; const w = (H - 0.16) * (390 / 844) + 0.16;
  d.image(s, IMG('s12-m-contacto.png'), 7.8, 2.86, w, H, { alt: 'La cabecera en un celular' });
  d.callout(s, 2.86, 3.75, 'display: none', '\nquita el elemento por completo, también para los lectores de pantalla. Úsalo solo con lo que está repetido: el botón Contacto ya está en el menú.', { x: 8.0 + w, w: 12.65 - 8.0 - w, size: 11 });
});

// ================= BLOQUE 03
d.divider('CONCEPTUAL', 'Técnicas fluidas', '03', ['Unidades relativas', 'clamp(): un tamaño que crece', 'auto-fit y minmax()', 'aspect-ratio', 'Tablas e iframes']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Técnicas fluidas', 'Unidades relativas', 'Una medida fluida se adapta sola, sin media query. Ya usas varias.');
  d.rows(s, [
    { a: '%', b: 'Del ancho del contenedor.', c: '`max-width: 100%` en imágenes y video' },
    { a: 'vw · vh', b: 'El 1 % del ancho o del alto de la ventana.', c: '`4vw` dentro de `clamp()`' },
    { a: 'rem', b: 'Del tamaño de letra de la página: 1rem = 16 px.', c: '`padding: 3rem 1rem`' },
    { a: 'em', b: 'Del tamaño de letra del propio elemento.', c: '`letter-spacing: -0.02em`' },
    { a: 'ch', b: 'El ancho del carácter «0».', c: '`max-width: 70ch` en párrafos' },
    { a: 'fr', b: 'Una fracción del espacio libre de una rejilla.', c: '`minmax(360px, 1fr)`' },
  ], { aw: 1.6, bw: 5.0, h: 0.56, gap: 0.08, asize: 14 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Técnicas fluidas', 'clamp(): un tamaño que crece con la pantalla', 'clamp(mínimo, preferido, máximo). Usa el preferido mientras quede entre los dos límites.');
  place(d, s, IMG('clamp.png'), 0.7, 2.86, 7.3, 3.85, { align: 'left', valign: 'top' });
  d.code(s, 8.2, 2.86, 4.45, 1.5, '«.hero-title» {\n  font-size: clamp(\n    2.5rem, 1.5rem + 4vw, 4rem);\n}', { size: 11 });
  d.text(s, ['A 390 px: 24 + 15.6 = 39.6 → **40**, el mínimo.', 'A 820 px: 24 + 32.8 = **56.8**.', 'Desde 1000 px: **64**, el máximo de Figma.', 'Mínimo y máximo en `rem`: respetan el zoom de texto del navegador.'], { x: 8.25, y: 4.5, w: 4.4, h: 2.2, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 5, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Técnicas fluidas', 'auto-fit: una rejilla que decide sus columnas', 'Tantas columnas de al menos 360 px como quepan. Sin media query.');
  place(d, s, IMG('autofit.png'), 0.7, 2.86, 7.4, 3.85, { align: 'left', valign: 'top' });
  d.code(s, 8.3, 2.86, 4.35, 1.5, '«.projects-grid» {\n  display: grid;\n  grid-template-columns: repeat(\n    auto-fit,\n    minmax(min(100%, 360px), 1fr));\n}', { size: 10 });
  d.text(s, ['`auto-fit`: tantas columnas como quepan; si sobran, estira las tarjetas.', '`minmax(360px, 1fr)`: mínimo 360, máximo una fracción.', '`min(100%, 360px)`: en pantallas de menos de 360 no se desborda.', '`auto-fill` deja las columnas vacías.'], { x: 8.35, y: 4.5, w: 4.3, h: 2.25, size: 10.5, color: C.body, valign: 'top', bullet: true, paraAfter: 4, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Técnicas fluidas', 'aspect-ratio: la proporción en lugar del alto', 'Con un alto fijo, la imagen se recorta en el celular. Con una proporción, se achica entera.');
  place(d, s, IMG('s12-proyectos-820.png'), 0.7, 2.86, 6.6, 2.6, { align: 'left', valign: 'top' });
  d.text(s, 'Proyectos a 820 px: dos columnas sin media query y la imagen completa.', { x: 0.7, y: 5.55, w: 6.6, h: 0.3, size: 10.5, color: C.sub, align: 'center' });
  d.code(s, 7.5, 2.86, 5.15, 1.6, '«.project-image» {\n  width: 100%;\n  height: auto;\n  aspect-ratio: 628 / 220;  /* Figma */\n}', { size: 11 });
  d.code(s, 7.5, 4.6, 5.15, 1.6, '«iframe» {\n  width: 100%;\n  max-width: 560px;\n  height: auto;\n  aspect-ratio: 16 / 9;\n}', { size: 11 });
  d.callout(s, 6.0, 0.62, 'El iframe lo necesita:', 'una imagen conserva su proporción con `height: auto`; un iframe no.', { size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Técnicas fluidas', 'Una tabla que se desplaza dentro de su caja', 'Las columnas de una tabla no se pueden apilar. Si no cabe, se desplaza ella, no la página.');
  const H = 3.8; const w = (H - 0.16) * (390 / 844) + 0.16;
  d.image(s, IMG('s12-tabla.png'), 0.7, 2.86, w, H, { alt: 'La tabla de herramientas desplazada en un celular' });
  const x = 0.95 + w;
  d.code(s, x, 2.86, 12.65 - x, 1.35, '<div «class="tabla-scroll"» role="region"\n     aria-label="Tabla de herramientas" tabindex="0">\n  <table> … </table>\n</div>', { size: 11 });
  d.code(s, x, 4.35, 12.65 - x, 1.35, '«.tabla-scroll» { overflow-x: auto; }\n«.tabla-scroll table» {\n  min-width: 32rem;   /* por debajo, ilegible */\n}', { size: 11 });
  d.callout(s, 5.85, 0.8, 'tabindex="0":', 'la caja recibe el foco con Tab y se mueve con las flechas. `role` y `aria-label` le dicen al lector de pantalla qué es.', { x, w: 12.65 - x, size: 11 });
});

d.breakSlide('Al volver hacemos la versión móvil en Figma y la llevamos al código. Después empieza el Taller TA2.');

// ================= INSTRUMENTAL
d.imageSlide('cinfo-03-instrumental.jpg', 'Instrumental: aplicación del conocimiento con ejercicios y demostraciones');

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '04 · Figma', 'En Figma hoy: la versión móvil', 'Ampliación del manual. Cada clic está en la Guía de Figma de la sesión.');
  d.numCards(s, [
    { t: 'Duplica la página', d: '`Ctrl + D` sobre `mi-portafolio`. Renombra la copia `mi-portafolio-movil`.' },
    { t: 'Ancho fijo 390', d: 'El ancho de un iPhone 13 o 14. Lo que tenga Ancho fijo se saldrá: lo corriges.' },
    { t: 'Flujo vertical', d: '`Encabezado`, `hero-section`, `about-content`, `projects-grid` y `contact-content`.' },
    { t: 'Llenar el contenedor', d: 'Lo que medía 480, 520 o 696, y los dos botones del Hero.' },
    { t: 'Espaciado 16 y 48', d: 'En las secciones. Títulos de sección a 28; el título del Hero a 40.' },
    { t: 'Ajustar al contenido', d: 'El alto del marco, del pie y de las tarjetas. Después, **Presentar**.' },
  ]);
  d.note(s, 6.62, 'Trabaja solo en la copia: antes de cambiar un valor, mira en Capas que la capa esté dentro de mi-portafolio-movil.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '04 · Figma', 'Del marco móvil a las media queries', 'Cada cambio que haces en el marco de 390 es una regla dentro de @media.');
  d.mapRows(s, [
    ['hero-section · Flujo vertical', '.hero-section { flex-direction: column; }'],
    ['hero-actions · Flujo vertical; botones en Llenar', 'flex-direction: column; align-items: stretch;'],
    ['about-graphic, contact-list · Llenar el contenedor', 'flex-basis: auto;'],
    ['projects-grid · Flujo vertical', 'auto-fit: una columna sin media query'],
    ['Título del Hero · 40', 'clamp(2.5rem, 1.5rem + 4vw, 4rem)'],
    ['Secciones · Espaciado 16 y 48', 'main { padding: 3rem 1rem; }'],
    ['project-image · H 125', 'aspect-ratio: 628 / 220;'],
  ], { heads: ['En Figma móvil', 'En CSS'], csize: 11.5, h: 0.48 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Práctica', 'Construimos juntos: el Hero', 'index.css: el título con clamp() y el bloque 6. Paso 3 de la guía de código.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '«@media (max-width: 992px)» {\n  .hero-section {\n    flex-direction: column;\n    padding: 60px 24px;\n    text-align: center;\n  }\n  .hero-actions { justify-content: center; }\n  .hero-right { width: 100%; }\n  .code-body { text-align: left; overflow-x: auto; }\n}\n«@media (max-width: 600px)» {\n  .hero-section { padding: 48px 16px; }\n  .hero-actions {\n    flex-direction: column;\n    align-items: stretch;\n  }\n  .code-body { padding: 16px; font-size: 12px; }\n}', { size: 9.5 });
  const H = 3.86; const w = (H - 0.16) * (390 / 844) + 0.16;
  d.image(s, IMG('s12-celular.png'), 7.8, 2.86, w, H, { alt: 'El Hero en un celular' });
  d.text(s, ['`clamp()` en `.hero-title`; borra su regla de 600.', 'Tablet: las columnas se apilan y se centran.', 'Celular: botones a todo el ancho.', 'El código, a 12 px: cabe sin desplazarse.'], { x: 8.0 + w, y: 2.95, w: 12.65 - 8.0 - w, h: 3.7, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 8, codeColor: C.ink });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Práctica', 'Construimos juntos: Proyectos, video y tabla', 'contenido.css. Pasos 4 y 5 de la guía de código.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '«.projects-grid» {\n  display: grid;\n  grid-template-columns:\n    repeat(auto-fit, minmax(min(100%, 360px), 1fr));\n  gap: 24px;\n}\n«.project-image» {\n  height: auto;\n  aspect-ratio: 628 / 220;\n}\n«iframe» {\n  width: 100%; max-width: 560px;\n  height: auto; aspect-ratio: 16 / 9;\n}\n«.tabla-scroll» { overflow-x: auto; }\n«.tabla-scroll table» { min-width: 32rem; }', { size: 10 });
  d.steps(s, [['Rejilla', 'auto-fit en .projects-grid.'], ['Media query', 'Quita .projects-grid del bloque 14.'], ['Imagen', 'aspect-ratio en vez de 220.'], ['Video', 'El iframe en 16:9.'], ['Tabla', 'El div .tabla-scroll en el HTML.'], ['Prueba', 'A 390 no hay barra horizontal.']], { tw: 1.15 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Práctica', 'Ahora tú: las páginas interiores', 'Tienes 20 minutos. Pasos 6 y 7 de la guía de código.');
  d.numCards(s, [
    { t: 'Títulos fluidos', d: '`main h2` con `clamp(1.75rem, 1.25rem + 2vw, 2.25rem)`.' },
    { t: 'Tablet', d: 'Bloque 14: Sobre mí y Contacto en columna; la multimedia y el formulario en `1fr`.' },
    { t: 'Celular', d: 'Una media query de 600: `main` con `padding: 3rem 1rem`.' },
    { t: 'Formulario', d: 'En el celular, los botones uno debajo del otro.' },
    { t: 'Puntos de quiebre', d: 'Anota 992 y 600 en un comentario de `global.css`.' },
    { t: 'Prueba y publica', d: 'Las cuatro páginas a 390, 820 y 1440. Valida y sube a Netlify.' },
  ]);
  d.note(s, 6.62, 'Lo que no termines ahora entra en el Taller TA2: aplica lo mismo a tu sitio.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Práctica', 'Compruébalo en el celular', 'Modo dispositivo a 390 px. Ninguna página debe desplazarse hacia los lados.');
  const H = 3.6; const w = (H - 0.16) * (390 / 844) + 0.16;
  [['s12-m-index.png', 'Inicio'], ['s12-m-sobre.png', 'Sobre mí: el video'], ['s12-m-proyectos.png', 'Proyectos'], ['s12-m-contacto.png', 'Contacto']].forEach(([f, t], i) => {
    const x = 0.7 + i * (w + 0.3);
    d.image(s, IMG(f), x, 2.86, w, H, { alt: t, pad: 0.05 });
    d.text(s, t, { x: x - 0.1, y: 6.52, w: w + 0.2, h: 0.28, size: 10.5, bold: true, color: C.sub, align: 'center' });
  });
  const x = 0.7 + 4 * (w + 0.3);
  d.card(s, x, 2.86, 12.65 - x, H, { fill: C.soft });
  d.text(s, 'Si algo sobresale', { x: x + 0.22, y: 3.0, w: 12.65 - x - 0.44, h: 0.32, size: 13, bold: true, color: C.teal });
  d.text(s, ['Un ancho fijo en px sin `max-width: 100%`.', 'Una línea de código o una URL larga.', 'Una tabla sin su caja con `overflow-x: auto`.', 'En DevTools, busca el elemento que pasa del borde derecho.'], { x: x + 0.22, y: 3.42, w: 12.65 - x - 0.44, h: 2.9, size: 10.5, color: C.body, valign: 'top', bullet: true, paraAfter: 6, codeColor: C.ink });
});

// ================= EXTRA · CODIFICAR CON IA (ia.js, contenido en ia_contenido.json)
require('./ia.js').bloqueIA(d, '12');

// ================= NIVELADOR
d.imageSlide('cinfo-04-nivelador.jpg', 'Nivelador: nivel de comprensión del estudiante');
d.checklist('NIVELADOR', [
  'Sé para qué sirve la etiqueta viewport y dónde va.',
  'Pruebo mi página en el modo dispositivo de DevTools a 390, 820 y 1440.',
  'Escribo una media query con max-width y la pongo al final de la hoja.',
  'Distingo escritorio primero (max-width) de celular primero (min-width).',
  'Sé leer clamp(mínimo, preferido, máximo).',
  'Puedo hacer una rejilla que cambie de columnas sin media query.',
  'Sé por qué un iframe necesita aspect-ratio y una tabla, overflow-x.',
  'Tengo claro qué se evalúa en el Taller TA2.',
]);
d.consultas('NIVELADOR', [['¿No cambia?', 'Escribí la media query y no pasa nada.'], ['¿Qué ancho?', '¿Cuáles son los puntos de quiebre correctos?'], ['¿Barra lateral?', 'En el celular la página se mueve a los lados.'], ['¿Cómo entrego?', '¿Qué debo subir para el TA2?']],
  'Cuando la media query no funciona', 'Revisa en este orden: la etiqueta viewport, que la media query esté al final de la hoja, que todas sus llaves cierren y que el selector de dentro sea el mismo de fuera. En DevTools, la regla aparece tachada cuando otra le gana.');

// ================= FUNCIONAL · TALLER TA2
d.imageSlide('cinfo-05-funcional.jpg', 'Funcional: aplicar lo aprendido');

d.add('FUNCIONAL', (s) => {
  d.header(s, 'Taller online · TA2', 'Taller TA2: CSS3 y diseño responsivo', 'Actividad evaluada: vale el 15 % de tu nota final del curso. Jueves 22/10/2026 · 4 horas.');
  d.card(s, 0.7, 2.86, 5.85, 3.95, { fill: C.soft });
  d.text(s, 'Consigna', { x: 1.04, y: 3.0, w: 5.17, h: 0.34, size: 15, bold: true, color: C.ink });
  d.text(s, [
    'Aplica CSS3 a tu **sitio del TA1** (o a tu portafolio) para que reproduzca tu Figma en escritorio y en celular.',
    '**Figma:** marco de escritorio y marco móvil de 390, con un componente con variante Hover y su prototipo.',
    '**CSS externo** en `assets/css/`, con variables en `:root` y sin estilos en línea.',
    '**Flexbox y Grid:** al menos un contenedor de cada uno.',
    '**Responsivo:** viewport, media queries para tablet y celular y una medida fluida.',
    '**Movimiento:** `:hover` con `transition`, un `transform` y un `@keyframes`, con `prefers-reduced-motion`.',
  ], { x: 1.04, y: 3.42, w: 5.17, h: 3.3, size: 11.5, color: C.body, valign: 'top', bullet: true, paraAfter: 5, codeColor: C.ink });
  d.card(s, 6.8, 2.86, 5.85, 3.95);
  d.text(s, 'Indicaciones de entrega', { x: 7.14, y: 3.0, w: 5.2, h: 0.34, size: 15, bold: true, color: C.teal });
  ['Sube al Aula Virtual la URL de Netlify y el enlace de Figma con los dos marcos.', 'HTML y CSS validados en el W3C sin errores.', 'A 390 px ninguna página se desplaza hacia los lados.', 'Entrega individual dentro del plazo que confirme el docente.'].forEach((t, i) => {
    const y = 3.52 + i * 0.78;
    d.circle(s, 7.2, y + 0.04, 0.42, i + 1, { size: 11.5 });
    d.text(s, t, { x: 7.8, y, w: 4.6, h: 0.5, size: 11.5, color: C.body });
  });
});

d.add('FUNCIONAL', (s) => {
  d.header(s, 'Taller online · TA2', 'Rúbrica de evaluación', 'Seis criterios. Es la misma rúbrica del documento del taller.');
  [
    ['Diseño en Figma', 'Escritorio y móvil de 390; componente con variante Hover y prototipo.', '15 %'],
    ['Arquitectura CSS', 'Hojas externas, variables en :root, clases legibles, sin estilos en línea.', '15 %'],
    ['Flexbox y Grid', 'Reproducen el Flujo, el Espacio, el Espaciado y la alineación del diseño.', '20 %'],
    ['Diseño responsivo', 'viewport, media queries, medidas fluidas y sin barra horizontal a 390 px.', '25 %'],
    ['Transiciones y animaciones', ':hover con transition, transform, @keyframes y movimiento reducido.', '10 %'],
    ['Validación y despliegue', 'HTML y CSS sin errores en el W3C; sitio funcional en Netlify.', '15 %'],
  ].forEach(([t, dsc, p], i) => {
    const y = 2.86 + i * 0.58;
    d.card(s, 0.7, y, 11.95, 0.5);
    d.circle(s, 0.95, y + 0.07, 0.36, i + 1, { size: 10.5 });
    d.text(s, t, { x: 1.5, y, w: 3.3, h: 0.5, size: 12.5, bold: true, color: C.ink });
    d.text(s, dsc, { x: 4.85, y, w: 6.6, h: 0.5, size: 11, color: C.body });
    d.text(s, p, { x: 11.4, y, w: 1.05, h: 0.5, size: 13, bold: true, color: C.teal, align: 'right' });
  });
  d.note(s, 6.45, '100 % de esta rúbrica equivale al 15 % de tu nota final del curso.');
});

// ================= ORIENTADOR
d.imageSlide('cinfo-06-orientador.jpg', 'Orientador: conclusión del tema');
d.resumen([
  'Sin la etiqueta viewport, el celular muestra la página en miniatura.',
  'Una media query aplica reglas solo si se cumple una condición, como `max-width: 600px`.',
  'Las media queries van al final: ganan por orden, no por especificidad.',
  'Escritorio primero usa `max-width`; celular primero, `min-width`.',
  '`clamp()` hace crecer una medida entre un mínimo y un máximo.',
  '`repeat(auto-fit, minmax(…))` decide las columnas sin media query.',
  '`aspect-ratio` conserva la proporción de imágenes e iframes.',
  'Cada cambio del marco móvil de Figma es una regla dentro de `@media`.',
]);
d.hacia('Tu portafolio ya se adapta a cualquier pantalla. Lo que viene.', [
  ['SESIÓN 11', 'Animaciones', 'Transiciones, transform y @keyframes.'],
  ['SESIÓN 12', 'Responsive', 'Media queries y el Taller TA2.', true],
  ['SESIÓN 13', 'Bootstrap', 'Introducción y su sistema de grillas.'],
  ['SESIÓN 14', 'Bootstrap', 'Componentes y utilidades.'],
  ['SESIÓN 15', 'Proyecto', 'El proyecto integrador.'],
], 'Recuerda confirmar en el Aula Virtual la fecha límite del Taller TA2. En la sesión 13 llega Bootstrap: una grilla responsiva escrita con celular primero.');

require('fs').mkdirSync(path.dirname(out), { recursive: true });
d.save(out).then((n) => console.log('ok', n, 'diapositivas →', out));
