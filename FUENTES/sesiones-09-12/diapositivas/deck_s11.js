// Sesión 11 · Transiciones, transformaciones y animaciones CSS3
const path = require('path');
const { Deck, C, MONO } = require('./uss.js');
const { place } = require('./fit.js');
const IMG = (f) => path.join(__dirname, 'img', f);
const out = process.argv[2] || path.join(__dirname, 'out', 'Sesion11-Transiciones-y-Animaciones-CSS3.pptx');

const d = new Deck({ title: 'Sesión 11 · Transiciones, transformaciones y animaciones CSS3' });

// mezcla dos colores hex: t entre 0 y 1
const mezcla = (a, b, t) => [0, 2, 4].map((i) => Math.round(parseInt(a.substr(i, 2), 16) * (1 - t) + parseInt(b.substr(i, 2), 16) * t).toString(16).padStart(2, '0')).join('').toUpperCase();

d.waiting('11', 'Abre tu carpeta mi-portafolio y tu archivo de Figma. Hoy tu página responde al cursor.');
d.title({
  titulo: 'Transiciones y animaciones CSS3',
  sesion: '11',
  sub: 'Estados · transition · transform · @keyframes · el prototipo en Figma',
  code: '.btn {\n  transition: transform 0.2s;\n}\n.btn:hover {\n  transform: translateY(-2px);\n}',
});
d.imageSlide('como-te-sientes.jpg', '¿Cómo te sientes hoy?');
d.imageSlide('que-es-cinfo.jpg', '¿Qué es CINFO? Conceptual, Instrumental, Nivelador, Funcional y Orientador');
d.imageSlide('conocimientos-previos.jpg', 'Conocimientos previos y definiciones clave');

d.add('CONCEPTUAL', (s) => {
  d.header(s, 'Repaso', 'De dónde venimos', 'Tu portafolio ya tiene color, letra y distribución. Todavía está quieto.');
  d.twoCards(s, { t: 'Ya tienes', color: C.sub, items: ['Cuatro hojas de estilo con las variables de Figma.', 'El Hero, Sobre mí y Contacto con Flexbox; Proyectos y el formulario con Grid.', 'Tu diseño completo en Figma: Pasos 1 al 14.'] },
    { t: 'Hoy sumas', items: ['Estados: cómo se ve algo con el cursor encima.', 'Transiciones suaves entre un estado y otro.', 'Transformaciones y animaciones que arrancan solas.'] });
  d.callout(s, 5.18, 1.42, 'Lo que hace distinta a esta sesión', '\nHasta hoy cada regla describía un solo momento. Ahora describes dos (el normal y el que aparece con el cursor) y le dices al navegador cómo pasar de uno a otro, en cuánto tiempo y con qué ritmo.');
});

d.logros([
  ['Distinguir', 'Los estados `:hover`, `:active` y `:focus` de un elemento.'],
  ['Suavizar', 'Pasar de un estado a otro con `transition`: duración y curva.'],
  ['Mover', 'Desplazar, escalar y girar con `transform` sin empujar a los vecinos.'],
  ['Animar', 'Crear con `@keyframes` una animación que arranca sola.'],
  ['Prototipar', 'Hacer en Figma un botón con variante Hover y Animación inteligente.'],
]);

d.agenda([
  ['01', 'Estados', ':hover, :active y :focus; forzarlos en DevTools.', 20],
  ['02', 'Transiciones', 'transition, duración, curvas y qué se puede animar.', 40],
  ['03', 'Transformaciones', 'translate, scale y rotate en botones y tarjetas.', 35],
  ['04', 'Animaciones', '@keyframes, animation y el movimiento reducido.', 35],
  ['—', 'Descanso', '', 15],
  ['05', 'Figma: el prototipo', 'Componente, variante Hover y Animación inteligente.', 25],
  ['06', 'Práctica en tu portafolio', 'Menú, botones, tarjetas y la entrada del Hero.', 55],
]);

// ================= BLOQUE 01
d.divider('CONCEPTUAL', 'Estados', '01', ['Un elemento, varios momentos', ':hover, :active y :focus', 'Forzar un estado en DevTools', 'Dónde se escribe cada estado']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Estados', 'Un elemento, varios momentos', 'Una pseudo-clase selecciona un elemento solo mientras está en cierto estado.');
  place(d, s, IMG('s11-boton-estados.png'), 0.7, 2.86, 11.95, 2.1);
  d.rows(s, [
    { a: ':hover', b: 'Mientras el cursor está encima.', c: 'Menú, botones, tarjetas, filas de la tabla' },
    { a: ':active', b: 'Mientras se mantiene presionado.', c: '`.btn:active`: el botón se encoge' },
    { a: ':focus', b: 'Mientras el elemento tiene el foco.', c: 'El campo en el que escribes' },
  ], { y: 5.12, h: 0.5, gap: 0.07, aw: 1.7, bw: 4.4, asize: 12.5, bsize: 11.5, csize: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Estados', 'Forzar un estado en DevTools', 'Para estudiar un :hover sin perseguirlo con el mouse.');
  d.numCards(s, [
    { t: 'Inspecciona', d: 'Clic derecho sobre «Ver Proyectos» y elige **Inspeccionar**.' },
    { t: 'Pulsa :hov', d: 'En la pestaña **Styles**, arriba a la derecha. Aparecen casillas con los estados.' },
    { t: 'Marca :hover', d: 'El botón queda en su estado Hover y en Styles aparece la regla `.btn-primary:hover`.' },
  ], { h: 1.62 });
  d.code(s, 0.7, 4.75, 5.85, 1.75, '«.btn-primary» {               /* normal */\n  background-color: var(--color-primary);\n}\n«.btn-primary:hover» {         /* con el cursor */\n  background-color: var(--color-primary-hover);\n}', { size: 11 });
  d.callout(s, 4.75, 1.75, 'Sin espacio:', '`.btn:hover` es «el botón cuando tiene el cursor encima». Con espacio, `.btn :hover` sería «cualquier cosa con el cursor encima dentro del botón».', { x: 6.8, w: 5.85, size: 12 });
});

// ================= BLOQUE 02
d.divider('CONCEPTUAL', 'Transiciones', '02', ['Instantáneo o con transición', 'Las cuatro partes de transition', 'Duración y curva', 'Qué se puede animar', 'El subrayado del menú']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Transiciones', 'Instantáneo o con transición', 'El mismo :hover. La diferencia es si el navegador pasa por los valores intermedios.');
  const fila = (x, titulo, sub, n) => {
    d.card(s, x, 2.86, 5.85, 2.55, { fill: C.white });
    d.text(s, titulo, { x: x + 0.3, y: 2.98, w: 5.3, h: 0.32, size: 14, bold: true, color: C.ink });
    d.text(s, sub, { x: x + 0.3, y: 3.3, w: 5.3, h: 0.28, size: 11, color: C.sub, codeColor: C.ink });
    for (let i = 0; i < 6; i++) {
      const t = n === 2 ? (i < 3 ? 0 : 1) : i / 5;
      const bx = x + 0.3 + i * 0.88;
      d.card(s, bx, 3.8, 0.78, 0.78, { fill: mezcla('9CA3AF', '0B0F19', t), line: 'FFFFFF', r: 0.08 });
      d.text(s, `${i * 40} ms`, { x: bx - 0.05, y: 4.66, w: 0.88, h: 0.24, size: 9.5, color: C.sub, align: 'center' });
    }
    d.text(s, n === 2 ? 'El color salta de golpe.' : 'El color pasa por todos los tonos intermedios.', { x: x + 0.3, y: 4.96, w: 5.3, h: 0.3, size: 11.5, bold: true, color: n === 2 ? C.red : C.teal });
  };
  fila(0.7, 'Instantáneo (sin transition)', 'Así estaba tu portafolio hasta hoy.', 2);
  fila(6.8, 'Con transition: color 0.2s', 'En Figma: Animación inteligente.', 6);
  d.code(s, 0.7, 5.6, 11.95, 0.95, '«nav a» { color: #9CA3AF; transition: color 0.2s ease; }     /* la transición va en la regla normal */\n«nav a:hover» { color: #0B0F19; }', { size: 12, valign: 'middle' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Transiciones', 'Las cuatro partes de transition', 'Se escribe en la regla normal, no en :hover: así el cambio es suave al entrar y al salir.');
  d.code(s, 0.7, 2.86, 11.95, 0.85, 'transition:  «background-color»   «0.2s»   «ease-out»   «0s»;', { size: 18, valign: 'middle' });
  d.rows(s, [
    { a: 'propiedad', b: 'Qué se anima. Varias, separadas por comas.', c: '`background-color`, `transform`' },
    { a: 'duración', b: 'Cuánto tarda, en segundos o milisegundos.', c: '`0.2s` es lo mismo que `200ms`' },
    { a: 'curva', b: 'El ritmo: cómo se reparte el cambio en el tiempo.', c: '`ease`, `ease-out`, `cubic-bezier(…)`' },
    { a: 'retraso', b: 'Cuánto espera antes de empezar. Es opcional.', c: '`0.1s`' },
  ], { y: 3.9, h: 0.55, gap: 0.08, aw: 1.9, bw: 5.0, asize: 13, bsize: 11.5, csize: 11 });
  d.note(s, 6.38, 'Varias propiedades: transition: background-color 0.2s ease, transform 0.2s ease-out;');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Transiciones', 'La curva: el ritmo del cambio', 'Todas tardan lo mismo. Cambia cómo se reparte el avance en ese tiempo.');
  place(d, s, IMG('curvas.png'), 0.7, 2.86, 7.6, 3.9, { align: 'left', valign: 'top' });
  d.card(s, 8.5, 2.86, 4.15, 3.9, { fill: C.soft });
  d.text(s, 'Cuánto debe durar', { x: 8.75, y: 3.0, w: 3.7, h: 0.32, size: 13, bold: true, color: C.teal });
  d.text(s, ['Entre **150 y 400 ms**.', 'Menos de 100 ms no se nota.', 'Más de 500 ms hace lenta la página.', 'Botones y colores: `0.2s`.', 'Tarjetas e imágenes: `0.4s`.', 'Al cursor, `ease-out`: arranca rápido y la respuesta se siente inmediata.'], { x: 8.75, y: 3.4, w: 3.7, h: 3.25, size: 11.5, color: C.body, valign: 'top', bullet: true, paraAfter: 5, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Transiciones', 'Las variables de movimiento', 'Como los colores de Figma: se escriben una vez en :root y todo el sitio las usa.');
  d.code(s, 0.7, 2.86, 6.6, 2.5, ':root {\n  /* … colores, letras y radios … */\n  «--color-primary-hover»: #05A3B0;\n  «--duration-fast»: 0.2s;      /* botones y colores */\n  «--duration-base»: 0.4s;      /* tarjetas e imágenes */\n  «--ease-out»: cubic-bezier(0.22, 1, 0.36, 1);\n}', { size: 11.5 });
  d.code(s, 0.7, 5.5, 6.6, 1.0, '«.btn» {\n  transition: transform var(--duration-fast) var(--ease-out);\n}', { size: 11 });
  d.text(s, 'En Figma', { x: 7.6, y: 2.86, w: 2.4, h: 0.24, size: 9.5, bold: true, color: C.sub });
  d.text(s, 'En global.css', { x: 10.15, y: 2.86, w: 2.4, h: 0.24, size: 9.5, bold: true, color: C.sub });
  [['Relleno de la variante Hover', '--color-primary-hover'], ['Duración 200 ms', '--duration-fast'], ['Tarjetas: 400 ms', '--duration-base'], ['Curva Salida suave', '--ease-out']].forEach(([a, b], i) => {
    const y = 3.16 + i * 0.84;
    d.card(s, 7.5, y, 5.15, 0.74);
    d.text(s, a, { x: 7.7, y, w: 2.4, h: 0.74, size: 11.5, bold: true, color: C.ink });
    d.text(s, '→', { x: 9.95, y, w: 0.25, h: 0.74, size: 12, color: C.num, align: 'center' });
    d.text(s, b, { x: 10.2, y, w: 2.4, h: 0.74, size: 10.5, bold: true, color: C.teal, font: MONO });
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Transiciones', '¿Qué se puede animar?', 'Solo lo que tiene valores intermedios. Lo demás cambia de golpe aunque tenga transition.');
  d.twoCards(s, { t: 'Se anima', color: C.teal, items: ['Colores: `color`, `background-color`, `border-color`.', 'Medidas: `width`, `padding`, `background-size`.', '`opacity`, `box-shadow` y `transform`.'] },
    { t: 'Cambia de golpe', color: C.red, items: ['`display`: de `none` a `block` no hay mitad.', '`font-family` y otros valores con nombre.', 'Una altura en `auto`: el navegador no sabe hacia dónde va.'] }, { h: 2.3 });
  d.callout(s, 5.38, 1.12, 'Las más fluidas: transform y opacity.', 'El navegador las anima sin recalcular la página. Si algo debe moverse, usa `transform` y no `margin` ni `top`. Y nunca escribas `transition: all`: anima también lo que no querías.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Transiciones', 'El subrayado animado del menú', 'Un degradado de un solo color como imagen de fondo (sesión 09), que crece de 0 % a 100 %.');
  d.code(s, 0.7, 2.86, 6.9, 3.75, '«nav a» {\n  color: var(--color-text-muted);\n  padding-bottom: 4px;\n  background-image: linear-gradient(\n    var(--color-primary), var(--color-primary));\n  background-size: 0% 2px;          /* ancho 0 */\n  background-position: left bottom;\n  background-repeat: no-repeat;\n  transition: color var(--duration-fast) ease,\n    background-size var(--duration-base) var(--ease-out);\n}\n«nav a:hover» {\n  color: var(--color-text-primary);\n  background-size: 100% 2px;        /* ancho completo */\n}', { size: 10.5 });
  place(d, s, IMG('s11-menu.png'), 7.8, 2.86, 4.85, 2.6, { valign: 'top' });
  d.callout(s, 5.6, 1.01, 'De arriba abajo:', 'en reposo, a los 60 ms y a los 400 ms. Solo cambian el color del texto y el ancho del fondo.', { x: 7.8, w: 4.85, size: 11.5 });
});

// ================= BLOQUE 03
d.divider('CONCEPTUAL', 'Transformaciones', '03', ['translate, scale, rotate y skew', 'transform no empuja a los vecinos', 'Los botones del Hero', 'Las tarjetas de proyecto y contacto']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Transformaciones', 'Cuatro funciones de transform', 'La línea punteada es el lugar original. La caja se transforma después de colocarse en la página.');
  place(d, s, IMG('transform.png'), 0.7, 2.86, 11.95, 2.55, { valign: 'top' });
  d.rows(s, [
    { a: 'Varias a la vez', b: 'Separadas por espacios; se aplican en orden.', c: '`translateY(0) scale(0.98)`' },
    { a: 'transform-origin', b: 'El punto desde el que se escala o se gira.', c: 'Por defecto, el centro' },
  ], { y: 5.6, h: 0.5, gap: 0.08, aw: 2.4, bw: 4.7, asize: 12, bsize: 11.5, csize: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Transformaciones', 'transform no empuja a los vecinos', 'Por eso es la propiedad para mover algo al pasar el cursor.');
  const caso = (x, titulo, prop, mueve) => {
    d.card(s, x, 2.86, 5.85, 3.0, { fill: C.white });
    d.text(s, titulo, { x: x + 0.3, y: 2.98, w: 5.3, h: 0.32, size: 13, bold: true, color: mueve ? C.red : C.teal, font: MONO });
    d.card(s, x + 0.6, 3.5, 4.65, 0.5, { fill: C.soft, line: C.line });
    d.text(s, 'Párrafo', { x: x + 0.6, y: 3.5, w: 4.65, h: 0.5, size: 11, color: C.sub, align: 'center' });
    const off = mueve ? 0.0 : -0.12;
    s.addShape(d.p.shapes.ROUNDED_RECTANGLE, { x: x + 0.6, y: 4.2, w: 2.1, h: 0.56, rectRadius: 0.06, fill: { color: C.white }, line: { color: C.num, width: 1, dashType: 'dash' } });
    d.card(s, x + 0.6, 4.2 + off + (mueve ? 0.25 : 0), 2.1, 0.56, { fill: C.primary, line: C.primary, r: 0.06 });
    d.text(s, 'Botón A', { x: x + 0.6, y: 4.2 + off + (mueve ? 0.25 : 0), w: 2.1, h: 0.56, size: 11.5, bold: true, color: C.white, align: 'center' });
    d.card(s, x + 3.15, 4.2 + (mueve ? 0.25 : 0), 2.1, 0.56, { fill: C.white, line: C.ink, r: 0.06 });
    d.text(s, 'Botón B', { x: x + 3.15, y: 4.2 + (mueve ? 0.25 : 0), w: 2.1, h: 0.56, size: 11.5, bold: true, color: C.ink, align: 'center' });
    d.card(s, x + 0.6, 5.0 + (mueve ? 0.25 : 0), 4.65, 0.4, { fill: C.soft, line: C.line });
    d.text(s, 'Lo que sigue', { x: x + 0.6, y: 5.0 + (mueve ? 0.25 : 0), w: 4.65, h: 0.4, size: 10.5, color: C.sub, align: 'center' });
    d.text(s, prop, { x: x + 0.3, y: 5.9 - 0.02, w: 5.3, h: 0.3, size: 11, color: C.body, codeColor: C.ink });
  };
  caso(0.7, 'margin-top: 4px', '', true);
  caso(6.8, 'transform: translateY(-2px)', '', false);
  d.text(s, 'Con margin, el botón empuja al otro botón y a todo lo que sigue.', { x: 0.7, y: 6.0, w: 5.85, h: 0.3, size: 11.5, color: C.red, align: 'center' });
  d.text(s, 'Con transform, solo se mueve el botón: lo demás no se entera.', { x: 6.8, y: 6.0, w: 5.85, h: 0.3, size: 11.5, color: C.teal, align: 'center' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Transformaciones', 'Los botones del Hero', 'transition en la regla normal; el cambio en :hover; el clic en :active.');
  d.code(s, 0.7, 2.86, 6.9, 3.75, '«.btn» {\n  transition: background-color var(--duration-fast) ease,\n              box-shadow var(--duration-fast) ease,\n              transform var(--duration-fast) var(--ease-out);\n}\n«.btn-primary:hover» {\n  background-color: var(--color-primary-hover);\n  box-shadow: 0 4px 14px rgba(6, 182, 196, 0.35);\n  transform: translateY(-2px);      /* sube 2 px */\n}\n«.btn:active» {                     /* después de :hover */\n  transform: translateY(0) scale(0.98);\n}', { size: 10.5 });
  place(d, s, IMG('s11-boton-estados.png'), 7.8, 2.86, 4.85, 1.7, { valign: 'top' });
  d.callout(s, 4.75, 1.86, 'El orden importa:', '`.btn:active` y `.btn-primary:hover` tienen la misma especificidad (0-2-0). Al presionar se cumplen las dos, y gana la que está escrita después. Por eso `:active` va al final.', { x: 7.8, w: 4.85, size: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Transformaciones', 'Las tarjetas: sube, se acerca, gira', 'Un :hover en la tarjeta puede cambiar a sus hijos: selector de :hover + descendiente.');
  place(d, s, IMG('s11-proyecto-hover.png'), 0.7, 2.86, 6.6, 2.55, { align: 'left', valign: 'top' });
  d.code(s, 0.7, 5.55, 6.6, 1.05, '«.project-card:hover» { transform: translateY(-6px); }\n«.project-card:hover .project-image» { transform: scale(1.05); }', { size: 10.5, valign: 'middle' });
  place(d, s, IMG('s11-contacto-hover.png'), 7.5, 2.86, 5.15, 2.55, { valign: 'top' });
  d.code(s, 7.5, 5.55, 5.15, 1.05, '«.contact-card:hover» { transform: translateX(4px); }\n«.contact-card:hover .contact-icon» {\n  transform: rotate(-10deg) scale(1.08); }', { size: 10, valign: 'middle' });
});

// ================= BLOQUE 04
d.divider('CONCEPTUAL', 'Animaciones', '04', ['Transición o animación', 'Los fotogramas clave', 'Las partes de animation', 'Movimiento reducido']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Animaciones', 'Transición o animación', 'Las dos mueven cosas. Cambia qué las pone en marcha.');
  d.twoCards(s, { t: 'transition', color: C.teal, items: ['Necesita un cambio de estado: el cursor entra o sale.', 'Va de un valor a otro: solo dos puntos.', 'En tu portafolio: menú, botones y tarjetas.'] },
    { t: 'animation + @keyframes', color: C.ink, items: ['Arranca sola, al cargar la página.', 'Puede tener varios puntos intermedios y repetirse.', 'En tu portafolio: la entrada del Hero y el cursor del código.'] }, { h: 2.3 });
  d.callout(s, 5.38, 1.12, 'Úsalas con medida:', 'una animación al cargar llama la atención una vez. Si todo se mueve todo el tiempo, nada destaca y la página cansa. En tu portafolio solo se anima la entrada del Hero y un cursor de 8 px.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Animaciones', 'Los fotogramas clave', '@keyframes describe la animación con un nombre. animation la aplica a un elemento.');
  d.code(s, 0.7, 2.86, 5.4, 2.55, '«@keyframes aparecer» {\n  from {                 /* 0 % */\n    opacity: 0;\n    transform: translateY(24px);\n  }\n  to {                   /* 100 % */\n    opacity: 1;\n    transform: translateY(0);\n  }\n}', { size: 11 });
  d.code(s, 0.7, 5.55, 5.4, 1.0, '«.hero-left» { animation: aparecer 0.8s var(--ease-out) both; }\n«.hero-right» { animation: aparecer 0.8s var(--ease-out) 0.2s both; }', { size: 9.5, valign: 'middle' });
  place(d, s, IMG('s11-hero-2x2.png'), 6.3, 2.86, 6.35, 2.95, { valign: 'top' });
  d.callout(s, 5.92, 0.68, 'Entre from y to', 'puedes poner los porcentajes que quieras: `0%`, `50%`, `100%`.', { x: 6.3, w: 6.35, size: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Animaciones', 'Las partes de animation', 'Se escriben en una línea. Solo el nombre y la duración son obligatorios.');
  d.code(s, 0.7, 2.86, 11.95, 0.8, 'animation:  «aparecer»  «0.8s»  «var(--ease-out)»  «0.2s»  «1»  «normal»  «both»;', { size: 15, valign: 'middle' });
  d.rows(s, [
    { a: 'nombre', b: 'El de `@keyframes`, escrito igual.', c: '`aparecer`' },
    { a: 'duración', b: 'Cuánto dura una vuelta. Sin ella dura 0 s.', c: '`0.8s`' },
    { a: 'curva y retraso', b: 'Como en `transition`.', c: '`var(--ease-out)` · `0.2s`' },
    { a: 'repeticiones', b: 'Cuántas veces; `infinite`, sin fin.', c: '`1` por defecto · el cursor: `infinite`' },
    { a: 'dirección', b: '`normal`, `reverse` o `alternate`: ida y vuelta.', c: '`normal`' },
    { a: 'relleno', b: 'Qué muestra antes de empezar y al terminar.', c: '`both`: el `from` al esperar, el `to` al final' },
  ], { y: 3.82, h: 0.42, gap: 0.06, aw: 2.2, bw: 4.65, asize: 12, bsize: 11, csize: 10.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Animaciones', 'El cursor que parpadea', 'Un pseudo-elemento ::after al final del código, sin tocar el HTML.');
  d.code(s, 0.7, 2.86, 6.3, 3.0, '«.code-body code::after» {\n  content: "";              /* sin content no hay caja */\n  display: inline-block;\n  width: 8px;\n  height: 1.1em;\n  background-color: var(--color-primary);\n  animation: parpadeo 1s steps(1) infinite;\n}\n«@keyframes parpadeo» {\n  50% { opacity: 0; }\n}', { size: 11 });
  place(d, s, IMG('s11-codigo.png'), 7.2, 2.86, 5.45, 3.0, { valign: 'top' });
  d.callout(s, 6.05, 0.6, 'steps(1):', 'sin valores intermedios. El cursor se apaga y se enciende de golpe, como en un editor de código.', { size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Animaciones', 'La entrada del Hero', 'En PowerPoint la imagen se reproduce en bucle. Al recargar tu portada, la ves una sola vez.');
  place(d, s, IMG('s11-hero.gif'), 0.7, 2.86, 11.95, 4.0);
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Animaciones', 'Movimiento reducido', 'Algunas personas se marean con las animaciones y lo piden en su sistema. Tu página debe respetarlo.');
  d.code(s, 0.7, 2.86, 6.9, 2.15, '«@media (prefers-reduced-motion: reduce)» {\n  *, *::before, *::after {\n    animation-duration: 0.01ms !important;\n    animation-iteration-count: 1 !important;\n    transition-duration: 0.01ms !important;\n  }\n}', { size: 11.5 });
  d.steps(s, [['Windows', 'Configuración › Accesibilidad › Efectos visuales.'], ['DevTools', 'Ctrl + Shift + P › escribe rendering › Show Rendering.'], ['Emula', 'prefers-reduced-motion: reduce y recarga.'], ['Resultado', 'El Hero aparece ya en su sitio y nada se desliza.']], { tw: 1.15, h: 0.5 });
  d.callout(s, 5.2, 1.35, '!important es la excepción:', 'gana a cualquier regla, sin importar la especificidad ni el orden. No lo uses para arreglar una regla que no se aplica. Aquí sí tiene sentido: este bloque debe ganar a todas las transiciones del sitio.', { w: 6.9, size: 11.5 });
});

d.breakSlide('Al volver hacemos el prototipo del botón en Figma y llevamos todo al portafolio. Ten abiertos tu carpeta y tu archivo de Figma.');

// ================= INSTRUMENTAL
d.imageSlide('cinfo-03-instrumental.jpg', 'Instrumental: aplicación del conocimiento con ejercicios y demostraciones');

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Figma', 'En Figma hoy: el botón con estados', 'Ampliación del manual, después del Paso 14. Cada clic está en la Guía de Figma de la sesión.');
  d.numCards(s, [
    { t: 'Saca una copia', d: 'Duplica `btn-primary` y arrástralo fuera de `mi-portafolio`, al lienzo gris.' },
    { t: 'Componente', d: '`Ctrl + Alt + K`. El icono cambia a cuatro rombos morados.' },
    { t: 'Variante', d: '**Añadir variante (Add variant)**. Renómbralas `Estado=Predeterminado` y `Estado=Hover`.' },
    { t: 'La variante Hover', d: 'Relleno `05A3B0` y Sombra paralela: Y 4, Desenfoque 14, `06B6C4` al 35.' },
    { t: 'Prototipo', d: 'Mientras se pasa el cursor › Cambiar a › Hover. Animación inteligente, Salida suave, 200 ms.' },
    { t: 'Instancia y prueba', d: 'Pega una instancia en `hero-actions` con `Ctrl + Shift + R` y pulsa **Presentar**.' },
  ]);
  d.note(s, 6.62, 'Si tu Figma está en inglés: While hovering, Change to, Smart animate y Ease out.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Figma', 'Del prototipo al código', 'Cada pieza de la interacción de Figma tiene su propiedad en CSS.');
  d.mapRows(s, [
    ['Variante Estado=Predeterminado', '.btn-primary { … }'],
    ['Variante Estado=Hover', '.btn-primary:hover { … }'],
    ['Mientras se pasa el cursor', ':hover (vuelve sola al salir)'],
    ['Animación inteligente', 'transition'],
    ['Salida suave · 200 ms', 'var(--duration-fast) var(--ease-out)'],
    ['Relleno 05A3B0', 'background-color: var(--color-primary-hover);'],
    ['Sombra paralela Y 4 · Desenfoque 14 · 35 %', 'box-shadow: 0 4px 14px rgba(6, 182, 196, 0.35);'],
  ], { heads: ['En Figma', 'En CSS'], csize: 11.5, h: 0.48 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Construimos juntos: las variables y el menú', 'global.css y header.css. Pasos 1 y 2 de la guía de código.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '/* global.css, al final de :root */\n«--color-primary-hover»: #05A3B0;\n«--duration-fast»: 0.2s;\n«--duration-base»: 0.4s;\n«--ease-out»: cubic-bezier(0.22, 1, 0.36, 1);\n\n/* header.css, el botón de la cabecera */\n«header > a[href="contactame.html"]» {\n  transition: background-color var(--duration-fast) ease,\n              color var(--duration-fast) ease;\n}\n«footer a» { transition: color var(--duration-fast) ease; }', { size: 10.5 });
  d.steps(s, [['Variables', 'Tres de movimiento y el color Hover.'], ['Menú', 'El fondo de 0 % y su transition.'], [':hover', 'Color oscuro y fondo al 100 %.'], ['Cabecera', 'El botón Contacto se rellena.'], ['Pie', 'Los enlaces cambian a azul.'], ['Prueba', 'Pasa el cursor y fuerza :hover en DevTools.']], { tw: 1.15 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Construimos juntos: los botones del Hero', 'index.css, bloque 3. Paso 3 de la guía de código.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '«.btn» {\n  /* … lo de la sesión 10 … */\n  transition: background-color var(--duration-fast) ease,\n              border-color var(--duration-fast) ease,\n              box-shadow var(--duration-fast) ease,\n              transform var(--duration-fast) var(--ease-out);\n}\n«.btn-primary:hover» {\n  background-color: var(--color-primary-hover);\n  border-color: var(--color-primary-hover);\n  box-shadow: 0 4px 14px rgba(6, 182, 196, 0.35);\n  transform: translateY(-2px);\n}\n«.btn-secondary:hover» { background-color: rgba(11, 15, 25, 0.05); }\n«.btn:active» { transform: translateY(0) scale(0.98); }', { size: 10 });
  d.steps(s, [['Transition', 'En .btn: cuatro propiedades.'], ['Primario', 'Color Hover, sombra y sube 2 px.'], ['Secundario', 'Un gris casi transparente.'], ['Active', 'Al final: se encoge al 98 %.'], ['Compara', 'Con el prototipo de Figma.'], ['Revisa', 'Que nada empuje a los vecinos.']], { tw: 1.15 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Ahora tú: tarjetas, Hero y movimiento reducido', 'Tienes 30 minutos. Pasos 4 al 7 de la guía de código.');
  d.numCards(s, [
    { t: 'Proyectos', d: '`.project-card:hover` sube 6 px con sombra; su imagen hace `scale(1.05)`.' },
    { t: 'Contacto', d: 'La fila se desplaza 4 px y su círculo gira `-10deg`.' },
    { t: '@keyframes', d: 'Escribe `aparecer` y `parpadeo` antes de las media queries.' },
    { t: 'El Hero', d: 'Las dos columnas con `animation`; la derecha, con 0.2 s de retraso y `both`.' },
    { t: 'El resto', d: 'transition en enlaces, botones del formulario, campos y filas de la tabla.' },
    { t: 'Movimiento reducido', d: 'El bloque 10 de `global.css`. Pruébalo con Show Rendering.' },
  ]);
  d.note(s, 6.62, 'Si terminas antes: haz en Figma la variante Hover de project-card con su Sombra paralela.');
});

// ================= NIVELADOR
d.imageSlide('cinfo-04-nivelador.jpg', 'Nivelador: nivel de comprensión del estudiante');
d.checklist('NIVELADOR', [
  'Sé qué hacen :hover, :active y :focus, y puedo forzarlos en DevTools.',
  'Escribo transition en la regla normal, no en la de :hover.',
  'Puedo nombrar las cuatro partes de transition: propiedad, duración, curva y retraso.',
  'Sé por qué ease-out es la curva para responder al cursor.',
  'Muevo con transform, no con margin: así no empujo a los vecinos.',
  'Distingo una transición de una animación con @keyframes.',
  'Sé qué hace animation-fill-mode: both.',
  'Mi página respeta prefers-reduced-motion.',
]);
d.consultas('NIVELADOR', [['¿No se anima?', 'Escribí transition y el cambio sigue de golpe.'], ['¿Solo al entrar?', 'Es suave al entrar y brusco al salir.'], ['¿Parpadea?', 'El Hero aparece, desaparece y vuelve.'], ['¿En el celular?', '¿Cómo funciona :hover sin cursor?']],
  'Cuando el movimiento no sale', 'Revisa en este orden: que `transition` esté en la regla normal, que nombre la misma propiedad que cambia en `:hover`, que esa propiedad se pueda animar, y que el nombre de `animation` sea igual al de `@keyframes`. En el celular, `:hover` se activa al tocar.');

// ================= FUNCIONAL
d.imageSlide('cinfo-05-funcional.jpg', 'Funcional: aplicar lo aprendido');
d.tarea([
  'Añade los estados con transition al menú, los botones y los enlaces.',
  'Haz que las tarjetas de proyecto y de contacto respondan al cursor con transform.',
  'Escribe la entrada del Hero con @keyframes y el bloque de movimiento reducido.',
  'En Figma: el componente btn-primary con su variante Hover y el prototipo.',
  'Valida el CSS sin errores y publica en Netlify.',
], ['Subir la URL publicada al Aula Virtual.', 'Adjuntar el enlace de Figma con el prototipo.', 'El envío es obligatorio dentro del plazo establecido.', 'Se registra en ClassDojo como participación en clase.']);

// ================= ORIENTADOR
d.imageSlide('cinfo-06-orientador.jpg', 'Orientador: conclusión del tema');
d.resumen([
  'Una pseudo-clase como `:hover` o `:active` selecciona un elemento en un estado.',
  '`transition` va en la regla normal y suaviza el cambio al entrar y al salir.',
  'Duración entre 150 y 400 ms; `ease-out` para responder al cursor.',
  'Se animan los valores con intermedios: colores, medidas, `opacity`, `transform`.',
  '`transform` mueve, escala y gira sin empujar a los vecinos.',
  '`@keyframes` y `animation` crean movimientos que arrancan solos.',
  '`prefers-reduced-motion` respeta a quien pidió menos animaciones.',
  'La Animación inteligente de Figma es una `transition` en CSS.',
]);
d.hacia('Tu portafolio ya responde al cursor. Lo que viene.', [
  ['SESIÓN 10', 'Maquetación', 'Modelo de caja, Flexbox y Grid.'],
  ['SESIÓN 11', 'Animaciones', 'Transiciones, transform y @keyframes.', true],
  ['SESIÓN 12', 'Responsive', 'Media queries y el Taller TA2.'],
  ['SESIÓN 13', 'Bootstrap', 'Introducción y su sistema de grillas.'],
  ['SESIÓN 14', 'Bootstrap', 'Componentes y utilidades.'],
], 'El jueves 22 es el Taller TA2 (15 %): diseño responsivo con CSS. Trae tu sitio del TA1 o tu portafolio publicado y tu Figma con el marco de escritorio terminado.');

require('fs').mkdirSync(path.dirname(out), { recursive: true });
d.save(out).then((n) => console.log('ok', n, 'diapositivas →', out));
