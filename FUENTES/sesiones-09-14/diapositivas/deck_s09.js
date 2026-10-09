// Sesión 09 · CSS3: selectores, cascada y propiedades básicas
// Recupera la sesión 08 (feriado del 8 de octubre) y suma las propiedades de la 09.
const path = require('path');
const { Deck, C, F, MONO } = require('./uss.js');
const IMG = (f) => path.join(__dirname, 'img', f);
const out = process.argv[2] || path.join(__dirname, 'out', 'Sesion09-CSS3-Selectores-Cascada-y-Propiedades.pptx');

const d = new Deck({ title: 'Sesión 09 · CSS3: selectores, cascada y propiedades básicas' });

d.waiting('09', 'Abre tu carpeta mi-portafolio en Visual Studio Code y tu archivo de Figma. Hoy tu portafolio recibe sus primeros estilos.');
d.title({
  titulo: 'CSS3: selectores y propiedades',
  sesion: '09',
  sub: 'Sintaxis · selectores · cascada · unidades · color · tipografía · fondos y bordes',
  code: 'h2 {\n  color: #0B0F19;\n  font-size: 2.25rem;\n  border-bottom: 1px solid;\n}',
});
d.imageSlide('como-te-sientes.jpg', '¿Cómo te sientes hoy?');
d.imageSlide('que-es-cinfo.jpg', '¿Qué es CINFO? Conceptual, Instrumental, Nivelador, Funcional y Orientador');
d.imageSlide('conocimientos-previos.jpg', 'Conocimientos previos y definiciones clave');

// ---- Reajuste del calendario
d.add('CONCEPTUAL', (s) => {
  d.header(s, 'Antes de empezar', 'La sesión 08 fue feriado: así nos ponemos al día', 'Nada se pierde. Lo que tocaba el jueves 8 de octubre se reparte entre hoy y el jueves 15.');
  const cards = [
    ['SESIÓN 08 · JUE 08/10', 'Feriado', ['Sin clase.', 'Sus temas pasan a la 09 y la 10.'], C.soft, C.sub],
    ['SESIÓN 09 · HOY', 'CSS3 y propiedades', ['Sintaxis, selectores y cascada (de la 08).', 'Color, tipografía, fondos y bordes.', 'Figma: Pasos 10 y 11.'], C.white, C.teal],
    ['SESIÓN 10 · JUE 15/10', 'Maquetación', ['Modelo de caja, Flexbox y Grid.', 'El Hero Section (tarea de la 08).', 'Figma: Pasos 12 al 14.'], C.white, C.ink],
    ['SESIÓN 11 · MAR 20/10', 'Animaciones', ['Sin cambios: transiciones y transformaciones.'], C.white, C.ink],
  ];
  cards.forEach(([k, t, items, fill, col], i) => {
    const x = 0.7 + i * 3.03;
    d.card(s, x, 2.9, 2.88, 2.55, { fill, line: i === 1 ? C.teal : C.line, lineW: i === 1 ? 2 : 1 });
    d.text(s, k, { x: x + 0.2, y: 3.05, w: 2.5, h: 0.26, size: 9.5, bold: true, color: C.sub, charSpacing: 1 });
    d.text(s, t, { x: x + 0.2, y: 3.36, w: 2.5, h: 0.42, size: 16, bold: true, color: col });
    d.text(s, items, { x: x + 0.2, y: 3.86, w: 2.5, h: 1.45, size: 11.5, color: C.body, valign: 'top', bullet: true, paraAfter: 3 });
  });
  d.callout(s, 5.68, 0.82, 'Por qué el Hero pasa al jueves:', 'se construye con `display: flex`, que es el tema de la sesión 10. Así lo escribes entendiendo cada línea, no de memoria.');
}, 'Explicar el reajuste en dos minutos. Insistir en que el Hero no se pierde: se hace el jueves con Flexbox.');

// ---- Repaso
d.add('CONCEPTUAL', (s) => {
  d.header(s, 'Repaso', 'De dónde venimos', 'Tu portafolio tiene toda su estructura y su contenido. Le falta el aspecto que diseñaste en Figma.');
  d.twoCards(s, { t: 'Ya tienes', color: C.sub, items: ['Cuatro páginas HTML con estructura semántica.', 'Formulario de contacto, video, audio y controles propios.', 'En Figma, la cabecera y el Hero diseñados (Pasos 1 al 9).'] },
    { t: 'Hoy sumas', items: ['Escribir reglas CSS y conectarlas con `link`.', 'Elegir el selector y la unidad adecuados.', 'Dar color, letra, fondos y bordes a cada página.'] });
  d.callout(s, 5.18, 1.42, 'Lo que hace distinta a esta sesión', '\nHasta hoy tu HTML decía qué es cada cosa. Desde hoy el CSS dice cómo se ve. Van en archivos distintos por una razón: puedes cambiar todo el aspecto del sitio sin tocar una sola etiqueta.');
});

d.logros([
  ['Conectar', 'Enlazar hojas de estilo externas en el orden correcto.'],
  ['Seleccionar', 'Apuntar a la etiqueta exacta con selectores de tipo, clase, atributo y combinadores.'],
  ['Predecir', 'Saber qué regla gana por cascada, especificidad y herencia.'],
  ['Dar estilo', 'Aplicar color, tipografía, fondos y bordes con las unidades adecuadas.'],
  ['Traducir', 'Leer una medida en Figma y escribirla como declaración CSS.'],
]);

d.agenda([
  ['01', 'Qué es CSS y cómo se conecta', 'Tres formas de aplicar estilos y un archivo por función.', 20],
  ['02', 'Sintaxis y selectores', 'Reglas, declaraciones y cómo apuntar a cada etiqueta.', 30],
  ['03', 'Cascada, herencia y variables', 'Qué regla gana y qué pasa de padres a hijos.', 25],
  ['04', 'Unidades, color y tipografía', 'px, rem, em, %, colores y propiedades de texto.', 30],
  ['05', 'Fondos y bordes', 'background, border, border-radius, sombras y tablas.', 20],
  ['—', 'Descanso', '', 15],
  ['06', 'Figma: Pasos 10 y 11', 'Sobre mí, Proyectos y el diccionario de Figma a CSS.', 25],
  ['07', 'Del diseño al código', 'global.css, header.css y contenido.css en tu portafolio.', 50],
]);

// ================= BLOQUE 01
d.divider('CONCEPTUAL', 'Qué es CSS y cómo se conecta', '01', ['Contenido y presentación', 'Tres formas de aplicar CSS', 'La etiqueta link', 'Un archivo por función']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Qué es CSS', 'El mismo HTML, con y sin CSS', 'HTML dice qué es cada cosa. CSS dice cómo se ve.');
  d.image(s, IMG('sin-css.png'), 0.7, 2.86, 5.85, 3.39, { alt: 'Sobre mí sin CSS: solo la estructura' });
  d.text(s, 'Sin CSS: solo la estructura', { x: 0.7, y: 6.34, w: 5.85, h: 0.3, size: 12.5, bold: true, color: C.sub, align: 'center' });
  d.image(s, IMG('con-css.png'), 6.8, 2.86, 5.85, 3.39, { line: C.teal, alt: 'Sobre mí con los estilos de esta sesión' });
  d.text(s, 'Con CSS: los colores y la letra de Figma', { x: 6.8, y: 6.34, w: 5.85, h: 0.3, size: 12.5, bold: true, color: C.teal, align: 'center' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Qué es CSS', 'Tres formas de aplicar CSS', 'Las tres funcionan. Solo una se mantiene bien cuando el sitio crece.');
  const cols = [
    ['En línea', '<p style="color: red">\n  Hola\n</p>', 'En el atributo style de cada etiqueta. Mezcla contenido y presentación, y no se reutiliza.', 'Evítala', C.red, C.white],
    ['Interna', '<style>\n  p { color: red; }\n</style>', 'En una etiqueta style dentro del head. Solo sirve para esa página.', 'Solo para pruebas', C.sub, C.white],
    ['Externa', '<link rel="stylesheet"\n  href="assets/css/global.css" />', 'En un archivo .css aparte. Un mismo archivo da estilo a todas las páginas.', 'La que usamos', C.ink, C.soft],
  ];
  cols.forEach(([t, code, desc, tag, col, fill], i) => {
    const x = 0.7 + i * 4.05;
    d.card(s, x, 2.86, 3.85, 3.05, { fill });
    d.text(s, t, { x: x + 0.28, y: 3.02, w: 3.29, h: 0.36, size: 15, bold: true, color: col });
    d.code(s, x + 0.25, 3.46, 3.35, 1.0, code, { size: 10, valign: 'middle' });
    d.text(s, desc, { x: x + 0.28, y: 4.58, w: 3.29, h: 0.8, size: 11.5, color: C.body, valign: 'top' });
    d.text(s, tag, { x: x + 0.28, y: 5.44, w: 3.29, h: 0.3, size: 12.5, bold: true, color: col });
  });
  d.callout(s, 6.08, 0.62, 'Regla de oro del curso:', 'los estilos van en archivos .css organizados por función. Nada de `style="…"` dentro de las etiquetas.', { fill: C.white, leadColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Qué es CSS', '<link>: conectar la hoja de estilos', 'Va dentro del <head>, una línea por cada archivo.');
  d.code(s, 0.7, 2.86, 7.0, 2.75, '«<head>»\n  …\n  <!-- 1. Tokens y Reset Global -->\n  «<link» rel="stylesheet" href="assets/css/global.css" />\n  <!-- 2. Componentes comunes (Header / Footer) -->\n  «<link» rel="stylesheet" href="assets/css/header.css" />\n  <!-- 3. Base de las páginas interiores -->\n  «<link» rel="stylesheet" href="assets/css/contenido.css" />\n«</head>»', { size: 11 });
  [['rel="stylesheet"', 'Dice que el archivo enlazado es una hoja de estilos.', MONO], ['href', 'La ruta del archivo: relativa, como las de tus imágenes.', MONO], ['El orden', 'De lo general a lo particular. La razón está en la cascada.', F]].forEach(([a, b, f], i) => {
    const y = 2.86 + i * 0.97;
    d.card(s, 7.9, y, 4.75, 0.81);
    d.text(s, a, { x: 8.2, y, w: 1.75, h: 0.81, size: 11, bold: true, color: C.teal, font: f });
    d.text(s, b, { x: 9.95, y, w: 2.5, h: 0.81, size: 10.5, color: C.body });
  });
  d.callout(s, 5.86, 0.74, 'Si no se aplica ningún estilo:', 'casi siempre es la ruta del href. Compruébala en DevTools › Network: el archivo .css debe responder 200, no 404.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Qué es CSS', 'Un archivo por función', 'Cada página carga solo lo que necesita.');
  d.code(s, 0.7, 2.86, 3.9, 3.6, 'mi-portafolio-dagner/\n├── assets/\n│   ├── «css/»\n│   │   ├── «global.css»\n│   │   ├── «header.css»\n│   │   └── «contenido.css»\n│   ├── img/\n│   ├── js/\n│   └── media/\n├── index.html\n├── sobre-mi.html\n├── mis-proyectos.html\n└── contactame.html', { size: 10.5 });
  const filas = [
    ['global.css', 'Tokens, fuentes, reset y estilos base.', 'Todas las páginas', C.white],
    ['header.css', 'Cabecera y pie de página.', 'Todas las páginas', C.white],
    ['contenido.css', 'Base de las páginas interiores.', 'Sobre mí, Proyectos y Contacto', C.white],
    ['index.css', 'El Hero Section de la portada.', 'Llega en la sesión 10', C.soft],
  ];
  filas.forEach(([a, b, c, fill], i) => {
    const y = 2.86 + i * 0.7;
    d.card(s, 4.8, y, 7.85, 0.6, { fill });
    d.text(s, a, { x: 5.05, y, w: 1.6, h: 0.6, size: 11.5, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 6.7, y, w: 3.2, h: 0.6, size: 11, color: C.body });
    d.text(s, '→ ' + c, { x: 9.9, y, w: 2.65, h: 0.6, size: 10.5, color: C.sub });
  });
  d.callout(s, 5.72, 0.74, 'En Figma,', 'cada archivo sale de unas capas: header.css de Encabezado y footer-wrapper; contenido.css de las secciones Sobre mí, Proyectos y Contacto.', { x: 4.8, w: 7.85, size: 11 });
});

// ================= BLOQUE 02
d.divider('CONCEPTUAL', 'Sintaxis y selectores', '02', ['Anatomía de una regla', 'Selectores básicos', 'Clase o id', 'Atributo y combinadores', 'Pseudo-clases']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Sintaxis', 'Anatomía de una regla', 'Un selector y, entre llaves, una lista de declaraciones.');
  d.code(s, 0.7, 2.86, 5.12, 1.95, '«header» {\n  «height»: «80px»;\n  background-color: #FFFFFF;\n}', { size: 15, valign: 'middle' });
  d.code(s, 0.7, 4.95, 5.12, 0.66, '/* Así se escribe un comentario en CSS */', { size: 11, valign: 'middle' });
  [['Selector', 'header: a qué etiquetas se aplica la regla.'], ['Propiedad', 'height: la característica que cambias.'], ['Valor', '80px: cuánto o cómo. Va después de los dos puntos.'], ['Declaración', 'Propiedad y valor juntos, cerrados con punto y coma.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.7;
    d.card(s, 6.1, y, 6.55, 0.56);
    d.text(s, a, { x: 6.35, y, w: 1.55, h: 0.56, size: 12, bold: true, color: C.teal });
    d.text(s, b, { x: 7.9, y, w: 4.6, h: 0.56, size: 11.5, color: C.body });
  });
  d.callout(s, 5.86, 0.66, 'Error frecuente:', 'olvidar un punto y coma. La declaración siguiente deja de funcionar y el navegador no avisa.', { fill: C.white, leadColor: C.red });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Sintaxis', 'Selectores básicos', 'Cinco formas de decir a quién se aplica la regla.');
  d.rows(s, [
    { a: '*', b: 'Universal: todas las etiquetas.', c: '`* { margin: 0; }`' },
    { a: 'h2', b: 'De tipo: todas las etiquetas con ese nombre.', c: '`h2 { line-height: 1.2; }`' },
    { a: '.btn', b: 'De clase: las que tengan class="btn".', c: '`.btn { font-weight: 600; }`' },
    { a: '#tiempo', b: 'De id: la única con id="tiempo".', c: '`#tiempo { font-size: 14px; }`' },
    { a: 'h1, h2, h3', b: 'Agrupado: varias a la vez, separadas por coma.', c: '`h1, h2, h3 { color: #0B0F19; }`' },
  ]);
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Sintaxis', 'Clase o id: cuál usar', 'Los dos se escriben en el HTML. Cambia cuántas veces pueden aparecer.');
  d.twoCards(s, { t: '`class`', items: ['Se repite en todas las etiquetas que quieras.', 'Una etiqueta puede llevar varias, separadas por espacio.', 'En CSS se escribe con punto: `.foto-perfil`'] },
    { t: '`id`', color: C.teal, items: ['Es único: una sola etiqueta por página.', 'Lo usan los enlaces internos, las etiquetas label y JavaScript.', 'En CSS se escribe con numeral: `#tiempo`'] }, { lfill: C.soft, h: 1.95 });
  d.code(s, 0.7, 5.0, 11.95, 0.82, '<img «class»="foto-perfil" src="assets/img/images-perfil.png" alt="Foto de Dagner Chuman" />', { size: 12, valign: 'middle' });
  d.note(s, 6.1, 'Para dar estilo, usa clases. Los id que creaste en la sesión 07 siguen siendo para el script del video.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Sintaxis', 'Atributo y combinadores', 'Tu cabecera tiene dos enlaces a Contacto. ¿Cómo le damos estilo solo al botón?');
  d.code(s, 0.7, 2.86, 6.9, 2.1, '<header>\n  <h1><a href="index.html">Dagner Chuman</a></h1>\n  <nav aria-label="Navegacion principal">\n    <ul>\n      <li><a href="contactame.html">Contacto</a></li>\n    </ul>\n  </nav>\n  «<a href="contactame.html">Contacto</a>»\n</header>', { size: 10.5 });
  [['header h1 a', 'Descendiente (espacio): el enlace que está dentro del h1 de la cabecera, a cualquier profundidad.'], ['header > a', 'Hijo directo (>): solo el enlace que cuelga de header. El del menú queda fuera.'], ['a[href="contactame.html"]', 'De atributo: los enlaces con ese valor exacto en href.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.72;
    d.card(s, 7.8, y, 4.85, 0.64);
    d.text(s, a, { x: 8.02, y: y + 0.04, w: 4.5, h: 0.24, size: 10.5, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 8.02, y: y + 0.28, w: 4.5, h: 0.34, size: 9.5, color: C.body, valign: 'top' });
  });
  d.code(s, 0.7, 5.18, 11.95, 0.66, '«header > a[href="contactame.html"]» { … }        /* solo el botón de la derecha */', { size: 12, valign: 'middle' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Sintaxis', 'Pseudo-clases y pseudo-elementos', 'Seleccionan un estado o una parte de la etiqueta, no la etiqueta entera.');
  d.rows(s, [
    { a: ':hover', b: 'Mientras el cursor está encima.', c: '`a:hover { color: #0B0F19; }`' },
    { a: ':focus-visible', b: 'Cuando navegas con la tecla Tab.', c: '`:focus-visible { outline: … }`' },
    { a: ':nth-child(even)', b: 'Los hijos pares: una fila sí y otra no.', c: '`tbody tr:nth-child(even)`' },
    { a: ':root', b: 'La raíz del documento. Ahí viven tus variables.', c: '`:root { --radius-sm: 8px; }`' },
    { a: '::before', b: 'Pseudo-elemento: contenido que añade el CSS.', c: '`*::before { margin: 0; }`' },
  ], { aw: 2.3, bw: 4.6, asize: 12.5, bsize: 11.5 });
  d.note(s, 6.45, 'Un signo de dos puntos (:) indica un estado. Dos seguidos (::) indican una parte de la etiqueta.');
});

// ================= BLOQUE 03
d.divider('CONCEPTUAL', 'Cascada, herencia y variables', '03', ['Cuando dos reglas chocan', 'Especificidad', 'El orden de los archivos', 'Herencia', 'Variables CSS']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Cascada', 'Cuando dos reglas chocan, gana una', 'El navegador decide en este orden. Solo pasa al siguiente criterio si hay empate.');
  [['Origen', 'Tus estilos ganan a los que el navegador trae por defecto.'], ['Especificidad', 'Gana el selector más preciso: un id pesa más que una clase, y una clase más que una etiqueta.'], ['Orden', 'Si todo lo anterior empata, gana la regla que aparece más abajo.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.69;
    d.card(s, 0.7, y, 11.95, 0.6);
    d.circle(s, 1.05, y + 0.08, 0.44, i + 1);
    d.text(s, a, { x: 1.75, y, w: 2.2, h: 0.6, size: 13, bold: true, color: C.ink });
    d.text(s, b, { x: 4.0, y, w: 8.45, h: 0.6, size: 12, color: C.body });
  });
  d.code(s, 0.7, 5.05, 11.95, 1.05, 'a      { color: inherit; }                          /* global.css */\nmain a { color: var(--color-text-primary); }        /* contenido.css: gana por especificidad */', { size: 12, valign: 'middle' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Cascada', 'Especificidad: el marcador de cada selector', 'Tres casillas: id, clases y etiquetas. Se compara de izquierda a derecha.');
  ['id', 'clase', 'etiqueta'].forEach((t, j) => d.text(s, t, { x: 4.72 + j * 0.74, y: 2.84, w: 0.68, h: 0.24, size: 9.5, bold: true, color: C.sub, align: 'center' }));
  const filas = [['a', [0, 0, 1], 'Una etiqueta.'], ['main a', [0, 0, 2], 'Dos etiquetas.'], ['.foto-perfil', [0, 1, 0], 'Una clase gana a cualquier cantidad de etiquetas.'], ['tbody tr:nth-child(even)', [0, 1, 2], 'Las pseudo-clases y los atributos cuentan como clases.'], ['#tiempo', [1, 0, 0], 'Un id gana a cualquier cantidad de clases.']];
  filas.forEach(([sel, v, txt], i) => {
    const y = 3.12 + i * 0.63;
    d.card(s, 0.7, y, 11.95, 0.55);
    d.text(s, sel, { x: 1.0, y, w: 3.6, h: 0.55, size: 12, bold: true, color: C.teal, font: MONO });
    v.forEach((n, j) => {
      const on = n > 0;
      d.card(s, 4.72 + j * 0.74, y + 0.09, 0.68, 0.37, { fill: on ? C.teal : C.white, line: on ? C.teal : C.line, r: 0.07 });
      d.text(s, String(n), { x: 4.72 + j * 0.74, y: y + 0.09, w: 0.68, h: 0.37, size: 13, bold: true, color: on ? C.white : C.num, align: 'center', font: MONO });
    });
    d.text(s, txt, { x: 7.2, y, w: 5.2, h: 0.55, size: 12, color: C.body });
  });
  d.callout(s, 6.3, 0.55, 'Fuera del marcador:', '`style="…"` gana a todos los selectores y `!important` se salta las reglas. Evita los dos.', { fill: C.white, leadColor: C.red });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Cascada', 'Por eso global.css va primero', 'Con la misma especificidad gana la regla que llega al final: en el mismo archivo o en uno enlazado más abajo.');
  [['global.css', 'Lo general', 'Tokens, reset y base de todo el sitio.'], ['header.css', 'Lo común', 'Cabecera y pie, iguales en cada página.'], ['contenido.css', 'Lo particular', 'Lo que solo tienen las páginas interiores.']].forEach(([f, t, txt], i) => {
    const x = 0.7 + i * 4.25;
    d.card(s, x, 2.86, 3.45, 1.65, { fill: i === 2 ? C.soft : C.white });
    d.circle(s, x + 0.25, 3.08, 0.44, i + 1);
    d.text(s, f, { x: x + 0.85, y: 3.08, w: 2.45, h: 0.44, size: 14, bold: true, color: C.teal, font: MONO });
    d.text(s, t, { x: x + 0.28, y: 3.66, w: 2.95, h: 0.3, size: 12.5, bold: true, color: C.ink });
    d.text(s, txt, { x: x + 0.28, y: 3.96, w: 2.95, h: 0.42, size: 11, color: C.body, valign: 'top' });
    if (i < 2) d.text(s, '→', { x: x + 3.45, y: 2.86, w: 0.8, h: 1.65, size: 26, bold: true, color: C.num, align: 'center' });
  });
  d.code(s, 0.7, 4.78, 11.95, 1.08, 'main h2  { font-size: 2.25rem; }      /* dos etiquetas: 0-0-2 */\naside h2 { font-size: 1.375rem; }     /* también 0-0-2, pero está más abajo en contenido.css: gana */', { size: 11.5, valign: 'middle' });
  d.note(s, 6.15, 'El orden solo decide cuando la especificidad empata. Lo general va primero para que lo particular pueda ajustarlo.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Cascada', 'Herencia: lo que pasa de padres a hijos', 'Algunas propiedades bajan solas a las etiquetas que están dentro. Otras no.');
  d.card(s, 0.7, 2.86, 5.85, 1.35);
  d.text(s, 'Se heredan: las de texto', { x: 1.0, y: 3.0, w: 5.3, h: 0.34, size: 13, bold: true, color: C.ink });
  d.text(s, 'color · font-family · font-size\nline-height · text-align · letter-spacing', { x: 1.0, y: 3.4, w: 5.3, h: 0.7, size: 11.5, color: C.body, font: MONO, valign: 'top' });
  d.card(s, 6.8, 2.86, 5.85, 1.35);
  d.text(s, 'No se heredan: las de caja', { x: 7.1, y: 3.0, w: 5.3, h: 0.34, size: 13, bold: true, color: C.red });
  d.text(s, 'margin · padding · border\nbackground · width · height', { x: 7.1, y: 3.4, w: 5.3, h: 0.7, size: 11.5, color: C.body, font: MONO, valign: 'top' });
  d.code(s, 0.7, 4.42, 5.85, 1.9, '«body» {\n  color: var(--color-text-secondary);\n  font-family: var(--font-body);\n  line-height: 1.6;\n}', { size: 11.5, valign: 'middle' });
  d.card(s, 6.8, 4.42, 5.85, 1.9, { fill: C.soft });
  d.text(s, 'Tres excepciones', { x: 7.1, y: 4.55, w: 5.3, h: 0.34, size: 13, bold: true, color: C.teal });
  d.text(s, 'Los enlaces, los botones, los campos y el código traen estilos propios del navegador, y una regla directa gana a lo heredado. Hay que pedírselo: `color: inherit` en los enlaces, `font: inherit` en botones y campos, y `font-family` en `pre` y `code`.', { x: 7.1, y: 4.95, w: 5.3, h: 1.25, size: 11, color: C.body, valign: 'top', codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · Cascada', 'Variables CSS: los tokens de Figma en el código', 'Se declaran una vez en :root y, como se heredan, sirven en toda la página.');
  d.code(s, 0.7, 2.86, 6.9, 3.5, '«:root» {\n  --color-primary: #06B6C4;\n  --color-text-primary: #0B0F19;\n  --font-heading: \'Outfit\', sans-serif;\n  --radius-sm: 8px;\n}\n\n«button[type="submit"]» {\n  background-color: «var(--color-primary)»;\n  border-radius: «var(--radius-sm)»;\n}', { size: 12 });
  [['--nombre', 'Se declara con dos guiones delante.'], ['var(--nombre)', 'Se usa en el valor de cualquier propiedad.'], [':root', 'La raíz: todas las etiquetas heredan de ella.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.68;
    d.card(s, 7.8, y, 4.85, 0.58);
    d.text(s, a, { x: 8.05, y, w: 1.75, h: 0.58, size: 11, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 9.8, y, w: 2.7, h: 0.58, size: 10.5, color: C.body });
  });
  d.card(s, 7.8, 4.98, 4.85, 1.38, { fill: C.soft });
  d.text(s, 'Por qué vale la pena', { x: 8.05, y: 5.08, w: 4.4, h: 0.34, size: 13, bold: true, color: C.ink });
  d.text(s, 'Si cambia el color de la marca, editas una línea y se actualiza todo el sitio.', { x: 8.05, y: 5.45, w: 4.4, h: 0.8, size: 11.5, color: C.body, valign: 'top' });
});

// ================= BLOQUE 04
d.divider('CONCEPTUAL', 'Unidades, color y tipografía', '04', ['Fijas y relativas', 'rem y em en tu portafolio', 'Formas de escribir un color', 'Las propiedades de texto', 'De la Tipografía de Figma al CSS']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Unidades', 'Unidades: fijas y relativas', 'Una unidad relativa se calcula a partir de otra medida. Por eso se adapta.');
  d.rows(s, [
    { a: 'px', b: 'Píxel. Medida fija: no depende de nada.', c: 'Bordes, radios y medidas de Figma' },
    { a: 'rem', b: 'Relativa a la letra de la raíz: 16px por defecto.', c: 'Textos y espaciados' },
    { a: 'em', b: 'Relativa a la letra de la propia etiqueta.', c: '`letter-spacing`, el tamaño de `code`' },
    { a: '%', b: 'Relativa a la medida del contenedor.', c: 'Anchos fluidos: `max-width: 100%`' },
    { a: 'vw · vh', b: 'Relativa al ancho o al alto de la ventana.', c: 'Secciones a pantalla completa' },
    { a: 'sin unidad', b: 'Un multiplicador. Solo en algunas propiedades.', c: '`line-height: 1.6`' },
  ], { h: 0.54, gap: 0.08, bw: 5.0, csize: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Unidades', 'rem y em en tu portafolio', 'Las dos multiplican un tamaño de letra. Cambia cuál.');
  d.code(s, 0.7, 2.86, 7.0, 1.9, 'body        { font-size: 16px; }\nmain h2     { font-size: «2.25rem»; }       /* 36px de Figma ÷ 16 */\naside h2    { font-size: «1.375rem»; }      /* 22px de Figma ÷ 16 */\nmain        { padding: «6.25rem» 1.5rem; }  /* 100px y 24px */\nmain h2     { letter-spacing: «-0.01em»; }  /* 1 % de su letra */', { size: 11, valign: 'middle' });
  [['rem', 'Mira siempre a la raíz. Vale lo mismo en toda la página.'], ['em', 'Mira a su propia etiqueta. Si la letra crece, crece con ella.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.99;
    d.card(s, 7.9, y, 4.75, 0.9, { fill: C.soft });
    d.text(s, a, { x: 8.15, y: y + 0.08, w: 4.3, h: 0.3, size: 13, bold: true, color: C.ink, font: MONO });
    d.text(s, b, { x: 8.15, y: y + 0.4, w: 4.3, h: 0.44, size: 11, color: C.body, valign: 'top' });
  });
  d.card(s, 0.7, 5.0, 11.95, 1.4);
  d.text(s, 'Figma te da píxeles', { x: 1.04, y: 5.12, w: 11.3, h: 0.34, size: 13, bold: true, color: C.teal });
  d.text(s, 'Para pasarlos a rem, divide entre 16: el título de cada sección mide 36 px en Figma, y 36 ÷ 16 = 2.25rem. En el portafolio usamos px en la cabecera y en el Hero, tal como vienen del diseño, y rem en las páginas interiores.', { x: 1.04, y: 5.5, w: 11.3, h: 0.8, size: 12, color: C.body, valign: 'top' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Color', 'Colores: los tokens de tu diseño', 'Un color se puede escribir de varias formas. Figma te lo entrega en hexadecimal.');
  const rows = [['#06B6C4', 'Hexadecimal: rojo, verde y azul en pares, de 00 a FF.'], ['rgb(6, 182, 196)', 'El mismo color en números del 0 al 255.'], ['rgba(6, 182, 196, 0.35)', 'Con 35 % de opacidad. Lo usa la sombra del botón azul.'], ['transparent', 'Palabra clave: sin color.']];
  rows.forEach(([a, b], i) => {
    const y = 2.86 + i * 0.5;
    d.card(s, 0.7, y, 11.95, 0.44);
    d.text(s, a, { x: 1.0, y, w: 3.1, h: 0.44, size: 12.5, bold: true, color: C.teal, font: MONO });
    d.text(s, b, { x: 4.1, y, w: 8.25, h: 0.44, size: 12, color: C.body });
  });
  const sw = [['--color-primary', '06B6C4'], ['--color-bg', 'F9FAFB'], ['--color-surface', 'FFFFFF'], ['--color-text-primary', '0B0F19'], ['--color-text-secondary', '374151'], ['--color-text-muted', '9CA3AF'], ['--color-border', 'E5E7EB']];
  sw.forEach(([n, hex], i) => {
    const x = 0.7 + i * 1.733;
    d.card(s, x, 4.95, 1.55, 0.86, { fill: hex });
    d.text(s, n, { x: x - 0.05, y: 5.87, w: 1.65, h: 0.26, size: 8.5, bold: true, color: C.ink, align: 'center', font: MONO });
    d.text(s, '#' + hex, { x, y: 6.13, w: 1.55, h: 0.24, size: 9.5, color: C.sub, align: 'center', font: MONO });
  });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Tipografía', 'Las propiedades de texto', 'Todas se heredan: escríbelas en el padre y bajan a sus hijos.');
  d.rows(s, [
    { a: 'font-family', b: 'La fuente, con una de respaldo.', c: '`var(--font-heading)`' },
    { a: 'font-size', b: 'El tamaño de la letra.', c: '`2.25rem` · `18px`' },
    { a: 'font-weight', b: 'El grosor: 400 Regular … 800 ExtraBold.', c: '`font-weight: 800;`' },
    { a: 'line-height', b: 'La altura de cada línea.', c: '`1.6` = 160 % de Figma' },
    { a: 'letter-spacing', b: 'La separación entre letras.', c: '`0.06em` en mayúsculas pequeñas' },
    { a: 'text-transform', b: 'Mayúsculas sin cambiar el HTML.', c: '`uppercase` en la tabla' },
    { a: 'text-decoration', b: 'Subrayado: color y separación propios.', c: '`text-underline-offset: 3px`' },
  ], { h: 0.47, gap: 0.07, aw: 2.25, bw: 4.4, asize: 12, bsize: 11.5, csize: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Tipografía', 'La escala tipográfica de tu portafolio', 'Ocho tamaños, dos fuentes. Todos salen de la sección Tipografía de Figma.');
  d.image(s, IMG('escala.png'), 0.7, 2.86, 7.45, 3.74, { alt: 'Escala tipográfica del portafolio: de 64 a 13 píxeles' });
  d.card(s, 8.4, 2.86, 4.25, 3.74, { fill: C.soft });
  d.text(s, 'De Figma a CSS', { x: 8.65, y: 3.0, w: 3.8, h: 0.34, size: 13, bold: true, color: C.teal });
  d.text(s, ['Fuente Outfit → `var(--font-heading)`', 'Grosor ExtraBold → `font-weight: 800`', 'Tamaño 36 → `font-size: 2.25rem`', 'Altura de línea 160 % → `line-height: 1.6`', 'Relleno del texto 374151 → `color`'], { x: 8.65, y: 3.42, w: 3.85, h: 3.0, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 6, codeColor: C.ink });
});

// ================= BLOQUE 05
d.divider('CONCEPTUAL', 'Fondos y bordes', '05', ['Fondos: color, imagen y degradado', 'Bordes y sus lados', 'Radio de esquina', 'Sombras y contorno', 'Tablas con bordes']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '05 · Fondos', 'background: color, imagen y degradado', 'El Relleno de un marco en Figma es el background de una caja en CSS.');
  d.code(s, 0.7, 2.86, 5.3, 3.55, '«.tarjeta» {\n  background-color: var(--color-surface);\n}\n\n«.portada» {\n  background-image: url("assets/img/poster.jpg");\n  background-size: cover;      /* cubre la caja */\n  background-position: center;\n  background-repeat: no-repeat;\n}\n\n«.banda» {\n  background-image: linear-gradient(#06B6C4, #0B0F19);\n}', { size: 10 });
  d.image(s, IMG('fondos.png'), 6.2, 2.86, 6.45, 2.62, { alt: 'Tres fondos: color plano, degradado e imagen' });
  d.callout(s, 5.65, 0.75, 'Tu diseño usa fondos planos:', '`#F9FAFB` en la página y `#FFFFFF` en cabecera, tarjetas y tabla. Los degradados y las imágenes de fondo quedan como reto en DevTools.', { x: 6.2, w: 6.45, size: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '05 · Bordes', 'border y border-radius', 'El Trazo y el Radio de esquina de Figma. Un borde tiene grosor, estilo y color.');
  d.code(s, 0.7, 2.86, 4.6, 2.9, '/* grosor  estilo  color */\nborder: 1px solid var(--color-border);\n\n/* un solo lado: Trazo inferior */\nborder-bottom: 1px solid #E5E7EB;\n\nborder-radius: 8px;   /* botones */\nborder-radius: 12px;  /* tarjetas */\nborder-radius: 50%;   /* círculo */', { size: 10.5 });
  d.image(s, IMG('bordes.png'), 5.5, 2.86, 7.15, 2.9, { alt: 'Estilos de borde y radios de esquina' });
  d.callout(s, 5.98, 0.66, 'border-radius: 50%', 'redondea cada esquina la mitad del lado: una caja cuadrada se vuelve círculo. Así queda tu foto de perfil con la clase `.foto-perfil`.', { size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '05 · Bordes', 'Sombras y contorno', 'Dos líneas que no cambian el tamaño de la caja.');
  d.rows(s, [
    { a: 'box-shadow', b: 'Sombra: desplazamiento x e y, desenfoque y color.', c: '`0 10px 25px rgba(0,0,0,.05)`' },
    { a: 'outline', b: 'Contorno por fuera de la caja; no la agranda.', c: '`2px solid var(--color-primary)`' },
    { a: 'outline-offset', b: 'Separa el contorno del borde.', c: '`outline-offset: 2px;`' },
  ], { h: 0.55, gap: 0.08, aw: 2.1, bw: 4.6, asize: 12, bsize: 11.5, csize: 11 });
  d.image(s, IMG('sombra.png'), 0.7, 4.85, 7.3, 1.78, { alt: 'Sombra, sombra con el color de la marca y contorno de foco' });
  d.card(s, 8.2, 4.85, 4.45, 1.78, { fill: C.soft });
  d.text(s, 'Accesibilidad', { x: 8.45, y: 4.97, w: 4.0, h: 0.32, size: 13, bold: true, color: C.teal });
  d.text(s, 'Quien navega con el teclado necesita ver dónde está. `:focus-visible` dibuja el contorno solo al usar la tecla Tab.', { x: 8.45, y: 5.33, w: 4.0, h: 1.2, size: 11, color: C.body, valign: 'top', codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '05 · Bordes', 'La tabla pendiente de la sesión 05', 'Una tabla de datos con bordes, fondos y tipografía.');
  d.code(s, 0.7, 2.86, 5.0, 3.75, '«table» {\n  width: 100%;\n  border-collapse: collapse;\n  border: 1px solid var(--color-border);\n}\n«th, td» {\n  padding: 0.75rem 1rem;\n  border-bottom: 1px solid var(--color-border);\n}\n«thead th» {\n  background-color: #F3F4F6;\n  text-transform: uppercase;\n  letter-spacing: 0.06em;\n}\n«tbody tr:nth-child(even)» {\n  background-color: var(--color-bg);\n}', { size: 10 });
  d.image(s, IMG('tabla.png'), 5.9, 2.86, 6.75, 2.92, { alt: 'Tabla de herramientas del portafolio' });
  d.callout(s, 5.95, 0.66, 'border-collapse: collapse', 'une los bordes de celdas vecinas. Sin ella aparecen líneas dobles.', { x: 5.9, w: 6.75, size: 11.5 });
});

d.breakSlide('Al volver abrimos Figma para los Pasos 10 y 11, y después escribimos el CSS. Ten abiertos tu carpeta y tu archivo de Figma.');

// ================= BLOQUE 06 · INSTRUMENTAL
d.imageSlide('cinfo-03-instrumental.jpg', 'Instrumental: aplicación del conocimiento con ejercicios y demostraciones');

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Figma', 'En Figma hoy: Sobre mí y Proyectos (Pasos 10 y 11)', 'Cada paso está en la Guía de Figma de la sesión. Los Pasos 12 al 14 van el jueves.');
  d.numCards(s, [
    { t: 'Las secciones', d: 'Flujo vertical, W Llenar el contenedor, Espaciado 80 y 100, Espacio 48 y Relleno FFFFFF.' },
    { t: 'Paso 10 · Sobre mí', d: 'Título Outfit ExtraBold 36 y, debajo, about-content con Espacio 64.' },
    { t: 'about-text y gráfico', d: 'Texto en Llenar el contenedor; about-graphic de 480 × 264 con cuatro tag-block.' },
    { t: 'Paso 11 · Proyectos', d: 'projects-section con los mismos valores que Sobre mí y su título.' },
    { t: 'project-card', d: 'Altura fija 475, Radio 12, Recortar contenido. Rectángulo de 220 y texto con Espaciado 24.' },
    { t: 'projects-grid', d: 'Flujo horizontal, Espacio 24 y dos tarjetas de 628 de ancho.' },
  ]);
  d.note(s, 6.62, 'Lo que no termines en clase queda como tarea.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Figma', 'Diccionario: de Figma a CSS', 'Hoy usas las filas de color, letra y bordes. La Disposición automática llega el jueves.');
  const L = [['Relleno de un marco', 'background-color'], ['Relleno de un texto', 'color'], ['Trazo: color y Peso', 'border'], ['Trazo en un lado', 'border-bottom · border-top'], ['Radio de esquina', 'border-radius'], ['Espaciado', 'padding']];
  const Rr = [['Fuente', 'font-family'], ['Grosor de letra', 'font-weight'], ['Tamaño', 'font-size'], ['Altura de la línea', 'line-height'], ['Espacio', 'margin hoy · gap el jueves'], ['Disposición automática', 'display: flex (sesión 10)']];
  [L, Rr].forEach((col, k) => col.forEach(([a, b], i) => {
    const x = 0.7 + k * 6.1; const y = 2.86 + i * 0.6;
    d.card(s, x, y, 5.85, 0.52, { fill: k === 1 && i >= 4 ? C.soft : C.white });
    d.text(s, a, { x: x + 0.22, y, w: 2.3, h: 0.52, size: 11.5, bold: true, color: C.ink });
    d.text(s, '→', { x: x + 2.5, y, w: 0.35, h: 0.52, size: 12, color: C.num, align: 'center' });
    d.text(s, b, { x: x + 2.9, y, w: 2.85, h: 0.52, size: 11, bold: true, color: C.teal, font: MONO });
  }));
  d.note(s, 6.55, 'Si tu CSS no coincide con tu Figma, manda Figma.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Figma', 'La cabecera: del panel al código', 'Selecciona la capa Encabezado (Paso 2 del manual) y lee el panel derecho de arriba abajo.');
  d.mapRows(s, [['H: Altura fija 80', 'height: 80px;'], ['Relleno FFFFFF', 'background-color: var(--color-surface);'], ['Trazo inferior E5E7EB, grosor 1', 'border-bottom: 1px solid var(--color-border);'], ['Texto Dagner Chuman: Outfit Bold 18', 'font-size: 18px;   font-weight: 700;'], ['Menú: Geist Medium 14, 9CA3AF', 'color: var(--color-text-muted);'], ['Espaciado 0 · 80 · 0 · 80', 'padding: 0 80px;']], { heads: ['En Figma', 'En header.css'] });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Figma', 'Las tarjetas: del panel al código', 'Selecciona about-graphic o project-card. Son las tarjetas de tus páginas interiores.');
  d.mapRows(s, [['Relleno FFFFFF', 'background-color: var(--color-surface);'], ['Trazo E5E7EB, Peso 1', 'border: 1px solid var(--color-border);'], ['Radio de esquina 12', 'border-radius: var(--radius-md);'], ['Espaciado 24', 'padding: 1.5rem;'], ['Título: Outfit Bold 24', 'font-size: 1.5rem;   font-weight: 700;'], ['Descripción: Geist Regular 16, 374151', 'color: var(--color-text-secondary);']], { heads: ['En Figma', 'En contenido.css'] });
});

// ================= BLOQUE 07 · PRÁCTICA
d.add('INSTRUMENTAL', (s) => {
  d.header(s, '07 · Práctica', 'Construimos juntos: global.css', 'Escríbelo conmigo, línea por línea. No lo copies y pegues.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '@import url(\'https://fonts.googleapis.com/…\');\n\n«:root» {\n  --color-bg: #F9FAFB;\n  /* …el resto de los tokens */\n}\n\n«*, *::before, *::after» {\n  box-sizing: border-box;\n  margin: 0;\n  padding: 0;\n}\n\n«body» {\n  background-color: var(--color-bg);\n  font-family: var(--font-body);\n}', { size: 10.5 });
  d.steps(s, [['Carpeta', 'Crea assets/css y, dentro, global.css.'], ['Fuentes', '@import siempre en la primera línea.'], ['Tokens', ':root con las variables de Figma.'], ['Reset', 'Sin márgenes ni rellenos por defecto.'], ['Base', 'body, títulos, enlaces, listas y código.'], ['Enlaza', 'link en el head y comprueba el fondo.']]);
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '07 · Práctica', 'Construimos juntos: header.css', 'Cada regla usa un selector distinto de los que acabas de aprender.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '«header» {\n  height: 80px;\n  background-color: var(--color-surface);\n  border-bottom: 1px solid var(--color-border);\n  display: flex;            /* anticipo de la sesión 10 */\n  align-items: center;\n  justify-content: space-between;\n  padding: 0 80px;\n  position: sticky;\n  top: 0;\n}\n\nheader h1 a { … }\nnav[aria-label="Navegacion principal"] a { … }\nnav[aria-label="Navegacion principal"] a:hover { … }\nheader > a[href="contactame.html"] { … }\nfooter nav ul { … }', { size: 10 });
  d.steps(s, [['Barra', 'header: alto, fondo y borde inferior.'], ['Logotipo', 'header h1 a: descendiente.'], ['Menú', 'nav[aria-label]: de atributo.'], ['Hover', 'a:hover: pseudo-clase.'], ['Botón', 'header > a: hijo directo.'], ['Pie', 'footer y footer nav ul.']]);
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '07 · Práctica', 'Ahora tú: contenido.css', 'Tienes 30 minutos. Sigue el Paso 4 de la guía de código.');
  d.numCards(s, [
    { t: 'Enlaza', d: 'global.css, header.css y contenido.css, en ese orden, en las tres páginas interiores.' },
    { t: 'Caja de lectura', d: 'main con max-width: 800px, margin: 0 auto y padding: 6.25rem 1.5rem.' },
    { t: 'Títulos y enlaces', d: 'main h2 a 2.25rem y 800. Los enlaces del contenido, subrayados con el azul de Figma.' },
    { t: 'Tarjetas', d: 'aside, article y fieldset: fondo blanco, borde E5E7EB y radio 12. Foto de perfil redonda.' },
    { t: 'Formulario', d: 'Botones y campos con font: inherit. El botón de envío, azul, con button[type="submit"].' },
    { t: 'Tabla (tarea)', d: 'La tabla de herramientas en mis-proyectos.html: border-collapse y filas alternas.' },
  ]);
  d.note(s, 6.62, 'Si terminas antes: prueba el reto de fondos de la guía, solo en DevTools.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '07 · Práctica', 'Comprueba la cascada en DevTools', 'Clic derecho sobre un enlace del contenido › Inspeccionar › pestaña Styles.');
  d.code(s, 0.7, 2.86, 6.3, 3.2, '«main a» {                       contenido.css\n  color: var(--color-text-primary);\n  text-decoration: underline;\n}\n\n«a» {                            global.css\n  text-decoration: none;     ← tachada\n  color: inherit;            ← tachada\n}\n\nInherited from body\n  font-family: var(--font-body);', { size: 11 });
  [['Arriba, la que gana', 'Las reglas salen ordenadas de mayor a menor prioridad.'], ['Tachado', 'Una declaración vencida por otra más específica o posterior.'], ['Inherited from', 'Lo que la etiqueta recibió por herencia.'], ['Computed', 'Los valores finales: 2.25rem aparece como 36px.']].forEach(([a, b], i) => {
    const y = 2.86 + i * 0.82;
    d.card(s, 7.2, y, 5.45, 0.72);
    d.text(s, a, { x: 7.45, y, w: 1.75, h: 0.72, size: 11.5, bold: true, color: C.teal });
    d.text(s, b, { x: 9.2, y, w: 3.3, h: 0.72, size: 10.5, color: C.body });
  });
  d.note(s, 6.35, 'DevTools no modifica tus archivos: al recargar la página todo vuelve a su estado.');
});

// ================= NIVELADOR
d.imageSlide('cinfo-04-nivelador.jpg', 'Nivelador: nivel de comprensión del estudiante');
d.checklist('NIVELADOR', [
  'Sé enlazar una hoja de estilos externa y en qué orden van.',
  'Distingo selector, propiedad, valor y declaración.',
  'Sé leer un selector con espacio, con > y con [atributo].',
  'Puedo predecir qué regla gana contando su especificidad.',
  'Sé qué propiedades se heredan y cuáles no.',
  'Sé cuándo usar px, rem, em y %.',
  'Puedo escribir un color en hexadecimal y en rgba.',
  'Puedo pasar el Trazo, el Radio y la Tipografía de Figma a CSS.',
]);
d.consultas('NIVELADOR', [['¿Clase o id?', '¿Cuándo conviene crear una clase nueva?'], ['¿px o rem?', '¿Cuál uso para el tamaño de un título?'], ['¿No se aplica?', 'Escribí la regla y la página no cambia.'], ['¿border u outline?', '¿Cuál uso para resaltar un campo?']],
  'Cuando una regla no se aplica', 'Revisa en este orden: la ruta del link, el punto y coma de la línea anterior, el nombre del selector y, al final, si otra regla más específica la está venciendo. DevTools te la muestra tachada.');

// ================= FUNCIONAL
d.imageSlide('cinfo-05-funcional.jpg', 'Funcional: aplicar lo aprendido');
d.tarea([
  'Termina contenido.css y la tabla de herramientas (Pasos 4 y 6 de la guía).',
  'Usa variables var(--…) para todos los colores, fuentes y radios.',
  'Captura DevTools con una declaración tachada y explica en una línea por qué perdió.',
  'En Figma: Pasos 10 y 11 con la Guía de Figma de la sesión.',
  'Valida el HTML y el CSS sin errores y publica en Netlify.',
], ['Subir la URL publicada al Aula Virtual.', 'Adjuntar captura del validador W3C sin errores.', 'El envío es obligatorio dentro del plazo establecido.', 'Se registra en ClassDojo como participación en clase.']);

// ================= ORIENTADOR
d.imageSlide('cinfo-06-orientador.jpg', 'Orientador: conclusión del tema');
d.resumen([
  'HTML define qué es cada contenido; CSS define cómo se ve, en archivos aparte.',
  'Una regla es un selector más una lista de declaraciones del tipo `propiedad: valor;`',
  'Cuando dos reglas chocan deciden la especificidad y, si empatan, el orden.',
  'Las propiedades de texto se heredan; las de caja, no.',
  'px es una medida fija; rem, em y % se calculan a partir de otra medida.',
  'Los colores, las fuentes y los radios de Figma se guardan como variables en `:root`.',
  'background pinta el fondo; border, border-radius y box-shadow dibujan el contorno.',
  'Cada control de Figma tiene su propiedad en CSS: si no coinciden, manda Figma.',
]);
d.hacia('Tu portafolio ya tiene sus colores, su letra y sus bordes. Lo que viene.', [
  ['SESIÓN 08', 'Feriado', 'Sus temas, repartidos en la 09 y la 10.'],
  ['SESIÓN 09', 'CSS3', 'Selectores, cascada, color, tipografía y bordes.', true],
  ['SESIÓN 10', 'Maquetación', 'Modelo de caja, Flexbox, Grid y el Hero.'],
  ['SESIÓN 11', 'Animaciones', 'Transformaciones y transiciones.'],
  ['SESIÓN 12', 'Responsive', 'Media queries y el Taller TA2.'],
], 'Para el jueves (sesión 10): trae tu contenido.css terminado y tu Figma con los Pasos 10 y 11. Con Flexbox y Grid construiremos el Hero y las dos columnas de tu diseño.');

require('fs').mkdirSync(path.dirname(out), { recursive: true });
d.save(out).then((n) => console.log('ok', n, 'diapositivas →', out));
