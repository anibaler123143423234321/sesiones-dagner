// Sesión 13 · Introducción a Bootstrap y su sistema de grillas
const path = require('path');
const { Deck, C, MONO } = require('./uss.js');
const { place } = require('./fit.js');
const IMG = (f) => path.join(__dirname, 'img', f);
const out = process.argv[2] || path.join(__dirname, 'out', 'Sesion13-Bootstrap-y-Sistema-de-Grillas.pptx');

const d = new Deck({ title: 'Sesión 13 · Introducción a Bootstrap y su sistema de grillas' });

d.waiting('13', 'Abre tu portafolio y tu archivo de Figma. Hoy le sumas una página hecha con Bootstrap.');
d.title({
  titulo: 'Bootstrap y su sistema de grillas',
  sesion: '13',
  sub: 'Framework · CDN · Reboot · container, row y col · puntos de quiebre · medianiles',
  code: '<div class="row g-4">\n  <div class="col-md-6 col-lg-4">\n    …\n  </div>\n</div>',
});
d.imageSlide('como-te-sientes.jpg', '¿Cómo te sientes hoy?');
d.imageSlide('que-es-cinfo.jpg', '¿Qué es CINFO? Conceptual, Instrumental, Nivelador, Funcional y Orientador');
d.imageSlide('conocimientos-previos.jpg', 'Conocimientos previos y definiciones clave');

d.add('CONCEPTUAL', (s) => {
  d.header(s, 'Repaso', 'De dónde venimos', 'Tu portafolio está completo: diseño, estilos, movimiento y versión móvil. Todo escrito a mano.');
  d.twoCards(s, { t: 'Ya tienes', color: C.sub, items: ['Cuatro páginas con su CSS propio, hecho regla por regla.', 'Flexbox y Grid para repartir columnas (sesión 10).', 'Media queries, `clamp()` y `auto-fit` (sesión 12).'] },
    { t: 'Hoy sumas', items: ['Un framework: Bootstrap 5.3, desde un CDN.', 'Su grilla de 12 columnas y sus puntos de quiebre.', 'Una quinta página, Cursos, hecha con esa grilla.'] });
  d.callout(s, 5.18, 1.42, 'Lo que hace distinta a esta sesión', '\nHasta hoy escribías cada regla. Con Bootstrap, miles de reglas ya están escritas y probadas: tú eliges cuáles usar poniendo clases en el HTML. Tu CSS sigue mandando en lo que lo hace tuyo.');
});

d.logros([
  ['Explicar', 'Qué es un framework de CSS y qué trae Bootstrap.'],
  ['Instalar', 'Enlazar Bootstrap desde un CDN, en el orden correcto.'],
  ['Convivir', 'Resolver los choques entre el Reboot de Bootstrap y tu CSS.'],
  ['Maquetar', 'Repartir una página en filas y 12 columnas con `row` y `col-*`.'],
  ['Adaptar', 'Cambiar las columnas según el ancho con `col-md-*` y `col-lg-*`.'],
]);

d.agenda([
  ['01', '¿Qué es un framework?', 'Bootstrap: qué trae, cuándo conviene.', 20],
  ['02', 'Instalar Bootstrap', 'El CDN, el orden de las hojas y el Reboot.', 30],
  ['03', 'La grilla', 'container, row y las 12 columnas.', 40],
  ['04', 'Puntos de quiebre y medianiles', 'col-md, col-lg, g-4, offset y anidar.', 35],
  ['—', 'Descanso', '', 15],
  ['05', 'Figma: la guía de columnas', '12 columnas, Margen 80 y Medianil 24.', 25],
  ['06', 'Práctica: la página Cursos', 'cursos.html y cursos.css con la grilla.', 55],
]);

// ================= BLOQUE 01
d.divider('CONCEPTUAL', 'Frameworks', '01', ['Qué es un framework', 'Qué trae Bootstrap', 'Cuándo conviene y cuándo no']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Frameworks', '¿Qué es un framework?', 'Un conjunto de código ya escrito y probado que usas como base para no empezar de cero.');
  d.twoCards(s, { t: 'Sin framework (sesiones 09 a 12)', color: C.sub, items: ['Escribes cada regla: colores, columnas, botones.', 'Todo es tuyo y sabes por qué está ahí.', 'Lleva más tiempo y hay que probar cada pantalla.'] },
    { t: 'Con un framework', color: C.teal, items: ['Usas clases ya hechas: `row`, `col-lg-4`, `btn`.', 'Responsivo y probado en muchos navegadores.', 'Escribes menos CSS; tu trabajo es combinar y ajustar.'] }, { h: 2.3 });
  d.callout(s, 5.38, 1.12, 'Bootstrap', 'nació en Twitter en 2011 y hoy es el framework de CSS más conocido. Es gratuito y de código abierto. Usamos la versión 5.3, que no necesita jQuery.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Frameworks', 'Qué trae Bootstrap', 'Seis piezas. Hoy usas las dos primeras; la sesión 14, las demás.');
  d.numCards(s, [
    { t: 'Reboot', d: 'Su propio reinicio de estilos: márgenes, letra y listas parecidos en todos los navegadores.' },
    { t: 'Grilla', d: 'Filas de 12 columnas que cambian según el ancho. **Hoy.**' },
    { t: 'Utilidades', d: 'Clases de una sola propiedad: `mb-3`, `text-center`, `d-flex`.' },
    { t: 'Componentes', d: 'Tarjetas, botones, avisos, acordeones, ventanas y menús ya diseñados.' },
    { t: 'JavaScript', d: 'Hace funcionar los componentes que se abren y se cierran.' },
    { t: 'Iconos', d: 'Bootstrap Icons: una colección aparte, de más de 2000 iconos.' },
  ]);
  d.note(s, 6.62, 'Todo está documentado en getbootstrap.com, con ejemplos que puedes copiar.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Frameworks', '¿Cuándo conviene?', 'Un framework es una herramienta, no una obligación.');
  d.twoCards(s, { t: 'A favor', color: C.teal, items: ['Rapidez: una página responsiva en minutos.', 'Un equipo entero escribe con las mismas clases.', 'Documentación y ejemplos para casi todo.'] },
    { t: 'En contra', color: C.red, items: ['Muchos sitios con Bootstrap se parecen entre sí.', 'Pesa: unos 230 KB de CSS (31 KB comprimidos).', 'Trae su estilo: a veces hay que ganarle a sus reglas.'] }, { h: 2.3 });
  d.callout(s, 5.38, 1.12, 'Por eso aprendiste CSS primero:', 'para entender qué hace cada clase de Bootstrap y poder cambiarla. `col-lg-4` es Flexbox; `g-4` es `gap`; un punto de quiebre es una media query.');
});

// ================= BLOQUE 02
d.divider('CONCEPTUAL', 'Instalar Bootstrap', '02', ['El enlace desde el CDN', 'integrity y crossorigin', 'El orden de las hojas', 'El Reboot y tu cabecera']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Instalar Bootstrap', 'El enlace desde el CDN', 'Un CDN entrega archivos públicos muy rápido. No descargas nada: lo enlazas.');
  d.code(s, 0.7, 2.86, 11.95, 1.55, '<link rel="stylesheet"\n  href="«https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css»"\n  integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB"\n  crossorigin="anonymous" />', { size: 12 });
  d.rows(s, [
    { a: 'href', b: 'Bootstrap 5.3.8, la hoja minificada: sin espacios ni comentarios.', c: 'Cópialo de getbootstrap.com' },
    { a: 'integrity', b: 'La huella del archivo. Si alguien lo alterara, el navegador no lo usa.', c: 'Una letra distinta y no carga' },
    { a: 'crossorigin', b: 'Permite comprobar la huella de un archivo de otro sitio.', c: 'Siempre `anonymous`' },
  ], { y: 4.6, h: 0.55, gap: 0.08, aw: 1.7, bw: 6.0, asize: 12, bsize: 11.5, csize: 11 });
  d.note(s, 6.55, 'Sin internet en clase: descarga Bootstrap, guarda bootstrap.min.css en assets/css/ y enlázalo con una ruta relativa.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Instalar Bootstrap', 'Bootstrap va primero', 'Con la misma especificidad gana la regla escrita al final: así tu diseño ajusta a Bootstrap.');
  s.addShape(d.p.shapes.LINE, { x: 1.05, y: 3.5, w: 0, h: 2.4, line: { color: C.num, width: 2, endArrowType: 'triangle' } });
  [['bootstrap.min.css', 'Reboot, grilla, utilidades y componentes', C.sub], ['global.css', 'Tus tokens de Figma, tu reinicio y tu letra', C.teal], ['header.css', 'Tu cabecera y tu pie', C.teal], ['cursos.css', 'Lo propio de la página Cursos', C.teal]].forEach(([f, dsc, col], i) => {
    const y = 2.9 + i * 0.86;
    d.circle(s, 0.8, y + 0.12, 0.5, i + 1, { fill: col, size: 13 });
    d.card(s, 1.5, y, 5.6, 0.72, { fill: i === 0 ? C.soft : C.white });
    d.text(s, f, { x: 1.75, y, w: 2.4, h: 0.72, size: 13, bold: true, color: col === C.sub ? C.ink : C.teal, font: MONO });
    d.text(s, dsc, { x: 4.15, y, w: 2.85, h: 0.72, size: 10.5, color: C.body });
  });
  d.card(s, 7.4, 2.9, 5.25, 3.3, { fill: C.soft });
  d.text(s, 'Las tres páginas, tres combinaciones', { x: 7.65, y: 3.02, w: 4.8, h: 0.32, size: 13, bold: true, color: C.teal });
  d.text(s, ['**index.html:** global, header, index.', '**Páginas interiores:** global, header, contenido.', '**cursos.html:** Bootstrap, global, header, cursos.', 'La página Cursos no enlaza `contenido.css`: sus reglas para `button` o `article` chocarían con los componentes de la sesión 14.'], { x: 7.65, y: 3.45, w: 4.8, h: 2.65, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 6, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Instalar Bootstrap', 'El Reboot descuadra tu cabecera', 'Bootstrap le da margen al h1 y sangría a las listas con selectores de etiqueta (0-0-1).');
  place(d, s, IMG('s13-cabecera-reboot.png'), 0.7, 2.86, 6.1, 1.25, { align: 'left', valign: 'top' });
  d.text(s, 'Con el Reboot: el nombre y el menú suben y el menú se corre.', { x: 0.7, y: 4.15, w: 6.1, h: 0.28, size: 10.5, color: C.red });
  place(d, s, IMG('s13-cabecera-bien.png'), 0.7, 4.55, 6.1, 1.25, { align: 'left', valign: 'top' });
  d.text(s, 'Con el bloque 6 de header.css: centrados en la línea, como en Figma.', { x: 0.7, y: 5.84, w: 6.1, h: 0.28, size: 10.5, color: C.teal });
  d.code(s, 7.0, 2.86, 5.65, 1.95, '/* header.css · bloque 6 */\n«header h1»,\n«header ul»,\n«footer ul»,\n«footer p» {\n  margin: 0;\n  padding: 0;\n}', { size: 11 });
  d.callout(s, 4.98, 1.15, '¿Por qué no basta tu reinicio con *?', 'el reinicio de `global.css` usa `*` (0-0-0) y pierde contra `h1` (0-0-1), aunque esté después. `header h1` (0-0-2) sí gana.', { x: 7.0, w: 5.65, size: 11 });
});

// ================= BLOQUE 03
d.divider('CONCEPTUAL', 'La grilla', '03', ['Contenedor, fila y columnas', 'Las 12 columnas', 'Columnas automáticas', 'Más de 12: baja de línea']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · La grilla', 'Contenedor, fila y columnas', 'Siempre en este orden. Una fila tiene 12 columnas: el número de la clase dice cuántas ocupa cada hijo.');
  d.code(s, 0.7, 2.86, 4.6, 2.5, '<div class="«container»">\n  <div class="«row»">\n    <div class="«col-8»">…</div>\n    <div class="«col-4»">…</div>\n  </div>\n</div>', { size: 12 });
  d.text(s, ['`container`: limita el ancho y centra.', '`row`: una fila flex de 12 columnas.', '`col-*`: cuántas columnas ocupa.'], { x: 0.75, y: 5.5, w: 4.55, h: 1.2, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 4, codeColor: C.ink });
  place(d, s, IMG('bs-grilla.png'), 5.5, 2.86, 7.15, 4.0, { valign: 'top' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · La grilla', 'Tres tipos de contenedor', 'El contenedor es la caja que envuelve a las filas. Sin él, la fila sobresale 12px por cada lado.');
  place(d, s, IMG('bs-container.png'), 0.7, 2.86, 11.95, 2.0, { valign: 'top' });
  d.rows(s, [
    { a: '.container', b: 'Un ancho máximo para cada punto de quiebre: 540, 720, 960, 1140 y 1320px.', c: 'Un proyecto nuevo' },
    { a: '.container-fluid', b: 'Siempre todo el ancho de la ventana.', c: 'Un panel o un mapa' },
    { a: '.container-lg', b: 'Todo el ancho hasta 992px; desde ahí, como `.container`.', c: 'Mezcla de los dos' },
  ], { y: 5.0, h: 0.5, gap: 0.07, aw: 2.3, bw: 6.6, asize: 12, bsize: 11, csize: 10.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · La grilla', 'En tu portafolio, main es el contenedor', 'Tus márgenes de Figma son 80. Bootstrap usaría 60 a 1440px. Manda Figma.');
  d.code(s, 0.7, 2.86, 6.1, 2.45, '/* cursos.css · bloque 1 */\n«main» {\n  max-width: 1440px;\n  margin: 0 auto;\n  padding: 6.25rem 5rem;     /* 100 y 80 de Figma */\n}\n\n/* y adentro, directamente, cada row */', { size: 11.5 });
  d.card(s, 7.0, 2.86, 5.65, 2.45, { fill: C.soft });
  d.text(s, 'Por qué funciona', { x: 7.25, y: 2.98, w: 5.2, h: 0.32, size: 13, bold: true, color: C.teal });
  d.text(s, ['Una `row` tiene márgenes de −12px a cada lado.', 'Sus columnas, 12px de relleno: el texto vuelve a quedar en el borde.', 'El `padding` de 80 de `main` absorbe esos 12px: nada sobresale.'], { x: 7.25, y: 3.38, w: 5.2, h: 1.85, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 5, codeColor: C.ink });
  d.callout(s, 5.5, 1.0, 'En un proyecto nuevo, usa .container.', 'En tu portafolio, `main` ya hace ese trabajo desde la sesión 10, con los márgenes de tu diseño.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · La grilla', 'La primera fila: 7 + 5 = 12', 'Desde 992px, el texto ocupa 7 columnas y las cifras 5. En pantallas menores, cada una ocupa la fila entera.');
  d.code(s, 0.7, 2.86, 6.1, 3.0, '<div class="«row g-4 align-items-center»">\n  <div class="«col-lg-7»">\n    <h2>Cursos y talleres</h2>\n    <p>Formación práctica…</p>\n  </div>\n  <div class="«col-lg-5»">\n    <aside class="cifras">\n      <div class="«row row-cols-3 g-3»"> … </div>\n    </aside>\n  </div>\n</div>', { size: 11 });
  place(d, s, IMG('s13-intro.png'), 7.0, 2.86, 5.65, 1.6, { valign: 'top' });
  d.text(s, ['`align-items-center`: la fila es flex; centra en vertical.', '`row-cols-3`: una fila anidada; cada `col` mide un tercio.', '`g-4`: el medianil de 24px.'], { x: 7.05, y: 4.6, w: 5.6, h: 1.4, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 5, codeColor: C.ink });
});

// ================= BLOQUE 04
d.divider('CONCEPTUAL', 'Puntos de quiebre y medianiles', '04', ['Celular primero', 'sm, md, lg, xl y xxl', 'Varias clases en una columna', 'Los medianiles g-*', 'offset, row-cols y order']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Puntos de quiebre', 'Seis tamaños, celular primero', 'Una clase sin punto de quiebre vale siempre. Con punto de quiebre, vale desde ese ancho hacia arriba.');
  d.rows(s, [
    { a: '(sin nombre)', b: 'Desde 0px · `col-12`', c: 'El celular' },
    { a: 'sm', b: 'Desde 576px · `col-sm-6`', c: 'Celular girado' },
    { a: 'md', b: 'Desde 768px · `col-md-6`', c: 'Tablet vertical' },
    { a: 'lg', b: 'Desde 992px · `col-lg-4`', c: 'Tu punto de quiebre de tablet (sesión 12)', fill: 'E6F8FA' },
    { a: 'xl', b: 'Desde 1200px · `col-xl-3`', c: 'Laptop' },
    { a: 'xxl', b: 'Desde 1400px · `col-xxl-2`', c: 'Tu diseño de 1440' },
  ], { aw: 2.0, bw: 4.6, h: 0.52, gap: 0.07, asize: 13, bsize: 12, csize: 11.5 });
  d.note(s, 6.5, 'Es una media query con min-width (sesión 12): por eso Bootstrap es celular primero.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Puntos de quiebre', 'Varias clases en una columna', 'Se leen de izquierda a derecha, del celular al escritorio.');
  d.code(s, 0.7, 2.86, 11.95, 0.62, '<div class="«col-12» «col-md-6» «col-lg-4»">   <!-- 1 por fila · 2 desde 768px · 3 desde 992px -->', { size: 12.5, valign: 'middle' });
  const H = 3.0;
  const L = [['s13-cat-1440.png', '1440 px · 3 por fila', 1440 / 900], ['s13-cat-820.png', '820 px · 2 por fila', 820 / 1180], ['s13-cat-390.png', '390 px · 1 por fila', 390 / 844]];
  const ws = L.map(([, , r]) => (H - 0.16) * r + 0.16);
  let x = 0.7 + (11.95 - ws.reduce((a, b) => a + b) - 0.6) / 2;
  L.forEach(([f, t], i) => {
    d.image(s, IMG(f), x, 3.62, ws[i], H, { alt: t });
    d.text(s, t, { x: x - 0.3, y: 6.68, w: ws[i] + 0.6, h: 0.28, size: 11, bold: true, color: C.sub, align: 'center' });
    x += ws[i] + 0.3;
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Medianiles', 'Los medianiles: g-0 a g-5', 'La separación entre columnas y entre filas. Va en la row, no en las columnas.');
  place(d, s, IMG('bs-gutters.png'), 0.7, 2.86, 6.4, 3.95, { align: 'left', valign: 'top' });
  [['g-0', '0'], ['g-1', '4px'], ['g-2', '8px'], ['g-3', '16px'], ['g-4', '24px: tu Medianil de Figma'], ['g-5', '48px'], ['gx-* · gy-*', 'Solo horizontal o solo vertical']].forEach(([c, v], i) => {
    const y = 2.86 + i * 0.57;
    d.card(s, 7.3, y, 5.35, 0.49, { fill: c === 'g-4' ? 'E6F8FA' : C.white });
    d.text(s, c, { x: 7.52, y, w: 1.7, h: 0.49, size: 12, bold: true, color: C.teal, font: MONO });
    d.text(s, v, { x: 9.25, y, w: 3.3, h: 0.49, size: 11.5, color: C.body });
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Más herramientas', 'offset, row-cols y order', 'Para dejar columnas vacías, repartir sin números y cambiar el orden visual.');
  place(d, s, IMG('bs-offset.png'), 0.7, 2.86, 7.3, 3.7, { align: 'left', valign: 'top' });
  d.text(s, ['`offset-lg-2`: deja 2 columnas vacías a la izquierda. El llamado de tu página: `col-lg-8 offset-lg-2`.', '`row-cols-3`: cada `col` de la fila mide un tercio. Tus cifras.', '`order-lg-1`: cambia el orden visual. El teclado y el lector de pantalla siguen el HTML.'], { x: 8.2, y: 2.95, w: 4.45, h: 3.6, size: 11.5, color: C.body, valign: 'top', bullet: true, paraAfter: 10, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Comparación', 'Tu CSS Grid o la grilla de Bootstrap', 'Los dos resuelven lo mismo. Cambia dónde se escribe.');
  d.card(s, 0.7, 2.86, 5.85, 3.0, { fill: C.white });
  d.text(s, 'Sesión 12 · CSS', { x: 1.0, y: 2.98, w: 5.3, h: 0.32, size: 13.5, bold: true, color: C.ink });
  d.code(s, 1.0, 3.42, 5.25, 1.3, '«.projects-grid» {\n  display: grid;\n  grid-template-columns:\n    repeat(auto-fit, minmax(min(100%, 360px), 1fr));\n}', { size: 10 });
  d.text(s, 'Las columnas se deciden en el CSS, por el ancho mínimo de cada tarjeta.', { x: 1.0, y: 4.85, w: 5.25, h: 0.8, size: 11, color: C.body, valign: 'top' });
  d.card(s, 6.8, 2.86, 5.85, 3.0, { fill: C.soft });
  d.text(s, 'Sesión 13 · Bootstrap', { x: 7.1, y: 2.98, w: 5.3, h: 0.32, size: 13.5, bold: true, color: C.teal });
  d.code(s, 7.1, 3.42, 5.25, 1.3, '<div class="«row g-4»">\n  <div class="«col-12 col-md-6 col-lg-4»">\n    …\n  </div>\n</div>', { size: 10 });
  d.text(s, 'Las columnas se deciden en el HTML, por el punto de quiebre de la pantalla.', { x: 7.1, y: 4.85, w: 5.25, h: 0.8, size: 11, color: C.body, valign: 'top' });
  d.callout(s, 6.05, 0.62, 'Por dentro, Bootstrap es Flexbox:', 'una `row` es `display: flex` con `flex-wrap: wrap`, y `col-lg-4` es un ancho de 33.33 %.', { size: 11.5 });
});

d.breakSlide('Al volver ponemos la guía de 12 columnas en Figma y construimos la página Cursos.');

// ================= INSTRUMENTAL
d.imageSlide('cinfo-03-instrumental.jpg', 'Instrumental: aplicación del conocimiento con ejercicios y demostraciones');

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Figma', 'En Figma hoy: la guía de columnas y la página Cursos', 'Ampliación del manual. Cada clic está en la Guía de Figma de la sesión.');
  d.numCards(s, [
    { t: 'Guía de 12 columnas', d: 'En `mi-portafolio`: Columnas, Estirar, Margen `80` y Medianil `24`.' },
    { t: 'Guía de 4 columnas', d: 'En `mi-portafolio-movil`: Margen `16` y Medianil `24`.' },
    { t: 'Cursos en el menú', d: 'Duplica el texto Proyectos en `nav-links` y escribe Cursos.' },
    { t: 'El marco nuevo', d: 'Duplica la página, llámala `mi-portafolio-cursos` y deja solo cabecera y pie.' },
    { t: 'course-card', d: 'Diseña una tarjeta, hazla componente y pega 6 instancias en dos filas.' },
    { t: 'Comprueba', d: 'Cada tarjeta ocupa 4 columnas; el llamado, 8 centradas.' },
  ]);
  d.note(s, 6.62, 'Mostrar u ocultar la guía: Ctrl + Shift + 4 (en Mac, Ctrl + G).');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Figma', 'Cada tarjeta ocupa 4 columnas', 'La guía de Figma sobre tu página publicada: las columnas rojas coinciden con las tarjetas.');
  place(d, s, IMG('s13-columnas.png'), 0.7, 2.86, 11.95, 3.75, { valign: 'top' });
  d.note(s, 6.7, '4 columnas + 3 medianiles = 410.67. Es col-lg-4: tres tarjetas por fila.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Figma', 'De la guía de columnas a las clases', 'Cuenta columnas en Figma y escribe el número en la clase.');
  d.mapRows(s, [
    ['Guía de 12 columnas, Margen 80', 'main como contenedor + una .row por sección'],
    ['Medianil 24 · Espacio 24 entre tarjetas', '.row.g-4'],
    ['intro-text de 7 columnas · cifras de 5', '.col-lg-7 · .col-lg-5'],
    ['course-card de 4 columnas, 3 por fila', '.col-12.col-md-6.col-lg-4'],
    ['paso de 3 columnas, 4 por fila', '.col-12.col-sm-6.col-lg-3'],
    ['llamado de 8 columnas, centrado', '.col-lg-8.offset-lg-2'],
    ['Guía de 4 columnas del marco móvil', 'col-12: todo a lo ancho en el celular'],
  ], { heads: ['En Figma', 'En Bootstrap'], csize: 11.5, h: 0.48 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Construimos juntos: el head y la primera fila', 'cursos.html. Pasos 0 al 2 de la guía de código.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<head>\n  …\n  <link rel="stylesheet" href="«https://cdn.jsdelivr.net/…/bootstrap.min.css»"\n        integrity="sha384-…" crossorigin="anonymous" />\n  <link rel="stylesheet" href="assets/css/global.css" />\n  <link rel="stylesheet" href="assets/css/header.css" />\n  <link rel="stylesheet" href="assets/css/cursos.css" />\n</head>\n\n<main>\n  <section class="cursos-intro">\n    <div class="«row g-4 align-items-center»">\n      <div class="«col-lg-7»"> … </div>\n      <div class="«col-lg-5»"> … </div>\n    </div>\n  </section>', { size: 10 });
  d.steps(s, [['Copia', 'La cabecera y el pie de mis-proyectos.'], ['Enlaza', 'Bootstrap primero, desde el CDN.'], ['Reboot', 'El bloque 6 de header.css.'], ['main', 'El bloque 1 de cursos.css.'], ['Fila', 'col-lg-7 y col-lg-5 con g-4.'], ['Prueba', 'Estrecha la ventana bajo 992px.']], { tw: 1.0 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Construimos juntos: el catálogo', 'Seis tarjetas, tres por fila. Paso 3 de la guía de código.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<section aria-labelledby="titulo-catalogo">\n  <h2 id="titulo-catalogo">Catálogo</h2>\n  <div class="«row g-4»">\n    <div class="«col-12 col-md-6 col-lg-4»">\n      <article class="curso">\n        <p class="curso-nivel">Básico</p>\n        <h3>Diseño Web</h3>\n        <p>HTML5, CSS3, Flexbox, Grid y Bootstrap…</p>\n        <p class="curso-meta">16 sesiones · 4 h cada una</p>\n      </article>\n    </div>\n    <!-- … cinco tarjetas más … -->\n  </div>\n</section>', { size: 10 });
  d.steps(s, [['Fila', 'Una sola row con g-4.'], ['Columnas', 'col-12 col-md-6 col-lg-4.'], ['Tarjeta', 'article.curso con su CSS.'], ['Alto', 'height: 100% iguala la fila.'], ['Copia', 'Seis tarjetas, una por curso.'], ['Prueba', '1440, 820 y 390 px.']], { tw: 1.0 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Ahora tú: pasos, cifras y llamado', 'Tienes 25 minutos. Pasos 4 al 6 de la guía de código.');
  d.numCards(s, [
    { t: 'Los pasos', d: 'Un `ol` con `row g-4` y cuatro `li` con `col-12 col-sm-6 col-lg-3`.' },
    { t: 'Sin sangría', d: 'El bloque 5 de `cursos.css`: `padding-left: 0` en `.pasos`.' },
    { t: 'Las cifras', d: 'Una fila anidada `row row-cols-3 g-3` con tres `col`.' },
    { t: 'El llamado', d: '`col-lg-8 offset-lg-2`: 8 columnas centradas.' },
    { t: 'El menú', d: 'El enlace Cursos en las cinco páginas, en la cabecera y en el pie.' },
    { t: 'Valida', d: 'cursos.html y cursos.css en el W3C. Publica en Netlify.' },
  ]);
  d.note(s, 6.62, 'Si terminas antes: prueba order-lg-2 en una fila y mira qué pasa al estrechar la ventana.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Compruébalo con las columnas encima', '4 pasos de 3 columnas y un llamado de 8, con 2 vacías a cada lado.');
  place(d, s, IMG('s13-columnas-pasos.png'), 0.7, 2.86, 11.95, 1.9, { valign: 'top' });
  place(d, s, IMG('s13-columnas-llamado.png'), 0.7, 4.85, 11.95, 1.95, { valign: 'top' });
});

// ================= NIVELADOR
d.imageSlide('cinfo-04-nivelador.jpg', 'Nivelador: nivel de comprensión del estudiante');
d.checklist('NIVELADOR', [
  'Sé explicar qué es un framework y qué trae Bootstrap.',
  'Enlazo Bootstrap desde el CDN con integrity y crossorigin.',
  'Sé por qué Bootstrap va antes que mis hojas de estilo.',
  'Sé por qué el Reboot descuadró la cabecera y cómo lo resolví.',
  'Pongo cada col-* dentro de una row, y la row dentro de un contenedor.',
  'Sé leer col-12 col-md-6 col-lg-4 del celular al escritorio.',
  'Sé que g-4 mide 24px y va en la row.',
  'Puedo centrar un bloque con offset y anidar una fila.',
]);
d.consultas('NIVELADOR', [['¿No carga?', 'Enlacé Bootstrap y no cambia nada.'], ['¿Una debajo?', 'Las columnas quedan apiladas en escritorio.'], ['¿Barra lateral?', 'Aparece desplazamiento horizontal.'], ['¿Y mi CSS?', '¿Bootstrap reemplaza todo lo que hice?']],
  'Cuando la grilla no sale', 'Revisa en este orden: que Bootstrap cargue (pestaña Network), que cada `col-*` esté dentro de una `row`, que la clase esté bien escrita (`col-lg-4`, con guiones) y que la `row` esté dentro de un contenedor con `padding`.');

// ================= FUNCIONAL
d.imageSlide('cinfo-05-funcional.jpg', 'Funcional: aplicar lo aprendido');
d.tarea([
  'Crea cursos.html con Bootstrap desde el CDN y la cabecera de tu portafolio.',
  'Arma la presentación (7 + 5) y el catálogo en 1, 2 y 3 columnas.',
  'Agrega los pasos, las cifras anidadas y el llamado con offset.',
  'Añade el enlace Cursos en las cinco páginas.',
  'En Figma: la guía de 12 columnas y el marco mi-portafolio-cursos.',
], ['Subir la URL publicada al Aula Virtual.', 'Adjuntar captura del validador W3C sin errores.', 'El envío es obligatorio dentro del plazo establecido.', 'Se registra en ClassDojo como participación en clase.']);

// ================= ORIENTADOR
d.imageSlide('cinfo-06-orientador.jpg', 'Orientador: conclusión del tema');
d.resumen([
  'Un framework trae código probado: Bootstrap 5.3 da Reboot, grilla, utilidades y componentes.',
  'Bootstrap se enlaza desde un CDN, con `integrity` y `crossorigin`, antes que tus hojas.',
  'Su Reboot puede ganarle a tu reinicio: `header h1` (0-0-2) lo resuelve.',
  'La grilla: contenedor › `row` › `col-*`, con 12 columnas por fila.',
  'Celular primero: `col-12 col-md-6 col-lg-4` se lee del celular al escritorio.',
  'El medianil `g-4` mide 24px, como el de tu guía de Figma.',
  '`offset-*` deja columnas vacías; `row-cols-*` reparte sin números.',
  'La guía de columnas de Figma te dice el número de cada clase `col-*`.',
]);
d.hacia('Tu portafolio ya usa un framework. Lo que viene.', [
  ['SESIÓN 12', 'Responsive', 'Media queries y el Taller TA2.'],
  ['SESIÓN 13', 'Bootstrap', 'Introducción y su sistema de grillas.', true],
  ['SESIÓN 14', 'Bootstrap', 'Componentes, utilidades y tema.'],
  ['SESIÓN 15', 'Proyecto', 'El proyecto integrador.'],
  ['SESIÓN 16', 'Examen', 'Examen final (30 %).'],
], 'Para la sesión 14: trae cursos.html funcionando. Le pondremos tarjetas, un acordeón, una ventana de inscripción y los colores de tu Figma.');

require('fs').mkdirSync(path.dirname(out), { recursive: true });
d.save(out).then((n) => console.log('ok', n, 'diapositivas →', out));
