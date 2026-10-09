// Sesión 15 · Proyecto integrador: pruebas y despliegue
const path = require('path');
const { Deck, C, MONO } = require('./uss.js');
const { place } = require('./fit.js');
const IMG = (f) => path.join(__dirname, 'img', f);
const out = process.argv[2] || path.join(__dirname, 'out', 'Sesion15-Proyecto-Integrador-Pruebas-y-Despliegue.pptx');

const d = new Deck({ title: 'Sesión 15 · Proyecto integrador: pruebas y despliegue' });

// filas de tres columnas: [a, b, c, relleno]
const tres = (s, filas, o = {}) => {
  const y0 = o.y || 3.1; const h = o.h || 0.5; const gap = o.gap != null ? o.gap : 0.07; const w = o.w || [3.4, 3.6, 4.35];
  if (o.heads) o.heads.forEach((t, k) => d.text(s, t, { x: 0.95 + w.slice(0, k).reduce((a, b) => a + b, 0), y: y0 - 0.27, w: w[k], h: 0.24, size: 9.5, bold: true, color: C.sub }));
  filas.forEach((f, i) => {
    const y = y0 + i * (h + gap);
    d.card(s, 0.7, y, 11.95, h, { fill: f[3] || C.white });
    let x = 0.95;
    f.slice(0, 3).forEach((t, k) => {
      d.text(s, t, { x, y, w: w[k] - 0.15, h, size: o.size || 11.5, bold: k === 0, color: k === 0 ? C.ink : (k === 1 ? (o.mono === false ? C.body : C.teal) : C.body), font: k === 1 && o.mono !== false ? MONO : undefined, codeColor: C.ink });
      x += w[k];
    });
  });
};

d.waiting('15', 'Abre tu portafolio publicado y tu archivo de Figma. Hoy lo revisamos todo y lo dejamos listo para entregar.');
d.title({
  titulo: 'Proyecto integrador: pruebas y despliegue',
  sesion: '15',
  sub: 'Validadores · enlaces · <head> completo · teclado · 404 · Netlify Forms · Lighthouse',
  code: '<title>Sobre mí · Dagner Chuman</title>\n<link rel="icon" href="…" />\n<meta property="og:image"\n      content="https://…" />',
});
d.imageSlide('como-te-sientes.jpg', '¿Cómo te sientes hoy?');
d.imageSlide('que-es-cinfo.jpg', '¿Qué es CINFO? Conceptual, Instrumental, Nivelador, Funcional y Orientador');
d.imageSlide('conocimientos-previos.jpg', 'Conocimientos previos y definiciones clave');

d.add('CONCEPTUAL', (s) => {
  d.header(s, 'Repaso', 'De dónde venimos', 'El portafolio tiene sus cinco páginas, se adapta al celular y la página Cursos usa Bootstrap.');
  d.twoCards(s, { t: 'Ya tienes', color: C.sub, items: ['Cinco páginas con HTML semántico y CSS propio.', 'Diseño adaptable a 390, 820 y 1440 px.', 'Bootstrap con tu tema en la página Cursos.', 'El sitio publicado en Netlify.'] },
    { t: 'Hoy sumas', items: ['Pruebas: validadores, enlaces y teclado.', 'Un `<head>` completo: título, icono y vista previa.', 'Una página 404 y una de gracias.', 'Formularios que guardan los mensajes.', 'Lighthouse: medir antes de entregar.'] });
  d.callout(s, 5.18, 1.42, 'Lo que hace distinta a esta sesión', '\nNo aparece ninguna propiedad nueva de CSS. Hoy revisas tu sitio como lo haría un cliente, completas lo que falta para publicarlo bien y lo entregas como proyecto integrador.');
});

d.logros([
  ['Probar', 'Validar el HTML y el CSS y revisar enlaces, imágenes y nombres de archivo.'],
  ['Completar', 'Escribir un `<head>` con título, descripción, icono y Open Graph.'],
  ['Incluir', 'Navegar todo el sitio con el teclado y revisar el contraste.'],
  ['Publicar', 'Desplegar en Netlify con una 404 propia y un formulario que guarda mensajes.'],
  ['Medir', 'Leer un informe de Lighthouse y corregir lo que marca.'],
]);

d.agenda([
  ['01', 'Probar el sitio', 'La lista de pruebas, los validadores y los nombres de archivo.', 25],
  ['02', 'El <head> completo', 'Título, descripción, icono y vista previa al compartir.', 30],
  ['03', 'El teclado', 'Saltar al contenido, la página actual y el contraste.', 25],
  ['04', 'Aviso y formularios', 'La 404, la página de gracias y Netlify Forms.', 30],
  ['—', 'Descanso', '', 15],
  ['05', 'Figma: revisión final', 'Nombres, el icono, la vista previa y el enlace de solo lectura.', 25],
  ['06', 'Publicar y medir', 'Netlify, Lighthouse y el proyecto integrador.', 45],
]);

// ================= BLOQUE 01
d.divider('CONCEPTUAL', 'Probar el sitio', '01', ['La lista de pruebas', 'Los validadores del W3C', 'Enlaces y nombres de archivo']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Probar', 'La lista de pruebas', 'Antes de entregar, recorre el sitio con esta lista. Cada prueba toma pocos minutos.');
  tres(s, [
    ['HTML válido', 'validator.w3.org', 'Las siete páginas sin errores'],
    ['CSS válido', 'jigsaw.w3.org/css-validator', 'Las seis hojas sin errores'],
    ['Enlaces', 'Clic en cada enlace', 'Ninguno lleva a una página en blanco'],
    ['Imágenes', 'Revisa cada <img>', 'alt, width y height; menos de 300 KB'],
    ['Teclado', 'Tab · Shift + Tab · Enter · Esc', 'Llegas a todo y siempre ves el foco'],
    ['Pantallas', 'F12 › icono del celular', 'A 390, 820 y 1440 px sin barra horizontal'],
    ['Lighthouse', 'F12 › Lighthouse', 'Accesibilidad y SEO de 90 o más', 'E6F8FA'],
  ], { heads: ['Prueba', 'Con qué', 'Pasa si…'], w: [2.6, 4.3, 4.85], h: 0.47 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Probar', 'Los validadores del W3C', 'Sube cada archivo y corrige los errores en orden: arreglar el primero suele borrar los siguientes.');
  d.rows(s, [
    { a: 'End tag … open elements', b: 'Falta cerrar una etiqueta antes de esa línea.' },
    { a: 'Duplicate ID', b: 'Dos elementos tienen el mismo `id`: cada `id` es único en la página.' },
    { a: 'img … alt attribute', b: 'A una imagen le falta el texto alternativo `alt`.' },
    { a: 'for attribute of label', b: 'El `for` de una etiqueta no coincide con el `id` de su campo.' },
    { a: 'Parse Error (CSS)', b: 'Falta una llave, un punto y coma o los dos puntos.' },
  ], { aw: 3.6, h: 0.55, gap: 0.08, asize: 11.5, bsize: 12 });
  d.note(s, 6.55, 'En cursos.html se valida tu HTML y tus hojas (también tema-bootstrap.css), no el CSS de Bootstrap.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Probar', 'Netlify distingue mayúsculas', 'En tu computadora, Foto.JPG y foto.jpg pueden ser el mismo archivo. En el servidor, no.');
  tres(s, [
    ['foto-carnet.jpg', 'src="assets/img/foto-carnet.jpg"', 'Se ve'],
    ['Foto-Carnet.jpg', 'src="assets/img/foto-carnet.jpg"', 'Imagen rota: la mayúscula no coincide', 'FDECEC'],
    ['mis proyectos.html', 'href="mis proyectos.html"', 'A veces: el espacio pasa a %20', 'FFF7E6'],
    ['diseño.png', 'src="diseño.png"', 'Puede fallar: evita la ñ y las tildes', 'FFF7E6'],
  ], { heads: ['En tu carpeta', 'En el HTML', 'En Netlify'], w: [3.0, 4.6, 4.35], h: 0.55 });
  d.callout(s, 5.75, 0.8, 'La regla del curso, desde la sesión 01:', 'nombres en minúsculas, con guiones y sin espacios ni tildes. Y cada `href="#…"` con su `id` en la página.');
});

// ================= BLOQUE 02
d.divider('CONCEPTUAL', 'El <head> completo', '02', ['Un título por página', 'La descripción', 'El icono', 'La vista previa al compartir']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · El <head>', 'Un título distinto en cada página', 'Primero lo propio de la página y después tu nombre. Es el texto de la pestaña y del enlace en Google.');
  place(d, s, IMG('s15-pestana.png'), 0.7, 2.86, 11.95, 3.25, { valign: 'top' });
  d.note(s, 6.32, 'Hasta la sesión 14, cuatro páginas se llamaban «Portafolio - Dagner Chuman»: con varias pestañas no se distinguían.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · El <head>', 'Así queda el <head> de index.html', 'No se ve en la página, pero decide cómo aparece tu sitio en la pestaña, en Google y al compartirlo.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<title>«Dagner Chuman · Docente e Ingeniero Web»</title>\n<meta name="«description»" content="Portafolio de …" />\n\n<link rel="«icon»" type="image/png" sizes="32x32"\n      href="assets/img/favicon-32.png" />\n<link rel="«apple-touch-icon»"\n      href="assets/img/apple-touch-icon.png" />\n\n<meta property="«og:title»" content="Dagner Chuman · …" />\n<meta property="«og:description»" content="Portafolio de …" />\n<meta property="«og:image»"\n      content="«https://mi-portafolio-dagner.netlify.app»/…png" />\n<meta property="«og:url»" content="https://…netlify.app/" />', { size: 9.5 });
  d.steps(s, [['title', 'Distinto en cada página.'], ['description', 'Unos 150 caracteres.'], ['icon', 'La pestaña: 32 × 32.'], ['apple-touch', 'El celular: 180 × 180.'], ['og:', 'La tarjeta al compartir.'], ['og:image', 'Con la dirección completa.']], { tw: 1.3 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · El <head>', 'Open Graph: la vista previa al compartir', 'WhatsApp, LinkedIn y Facebook leen las etiquetas og: y arman una tarjeta con imagen, título y texto.');
  place(d, s, IMG('s15-compartir.png'), 0.7, 2.86, 7.6, 3.9, { align: 'left', valign: 'top' });
  d.card(s, 8.55, 2.86, 4.1, 3.9, { fill: C.soft });
  d.text(s, 'Tres reglas', { x: 8.8, y: 3.0, w: 3.6, h: 0.34, size: 14, bold: true, color: C.teal });
  d.text(s, ['La imagen mide **1200 × 630**.', '`og:image` y `og:url` llevan la dirección completa, con `https://`: la aplicación no está en tu sitio.', 'Si tu sitio se llama distinto en Netlify, cambia el nombre en las dos.'], { x: 8.8, y: 3.45, w: 3.6, h: 3.1, size: 11.5, color: C.body, valign: 'top', bullet: true, paraAfter: 6, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · El <head>', 'Tres imágenes nuevas en assets/img', 'Las tres salen de marcos de tu Figma (bloque 05).');
  d.rows(s, [
    { a: 'favicon-32.png', b: '32 × 32 · la pestaña del navegador y los marcadores', c: 'Sin él, el navegador pide /favicon.ico y da un 404' },
    { a: 'apple-touch-icon.png', b: '180 × 180 · el acceso directo en el celular', c: 'Sin esquinas redondas: las pone el celular' },
    { a: 'og-portafolio.png', b: '1200 × 630 · la tarjeta al compartir el enlace', c: 'Menos de 600 KB' },
  ], { aw: 3.0, bw: 4.6, h: 0.72, gap: 0.1, asize: 11.5, bsize: 11.5, csize: 11 });
  place(d, s, IMG('s15-og.png'), 0.7, 5.35, 11.95, 1.45, { valign: 'top' });
});

// ================= BLOQUE 03
d.divider('CONCEPTUAL', 'El teclado', '03', ['Saltar al contenido', 'La página actual: aria-current', 'El contraste']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · El teclado', 'Saltar al contenido', 'Con el teclado, cada página empieza por el menú. Un enlace escondido lleva directo al contenido.');
  place(d, s, IMG('s15-saltar.png'), 0.7, 2.86, 11.95, 1.15, { valign: 'top' });
  d.code(s, 0.7, 4.15, 5.85, 2.6, '<body>\n  <a class="«saltar»" href="«#contenido»">\n    Saltar al contenido\n  </a>\n  <header> … </header>\n  <main id="«contenido»"> … </main>', { size: 10.5 });
  d.code(s, 6.8, 4.15, 5.85, 2.6, '.saltar {\n  position: absolute;\n  «top: -100px;»   /* fuera de la vista */\n  z-index: 200;\n  …\n}\n.saltar«:focus» { «top: 16px;» }', { size: 10.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · El teclado', 'La página actual: aria-current', 'Marca el enlace de la página en la que estás. El lector de pantalla dice «Sobre mí, página actual».');
  place(d, s, IMG('s15-actual.png'), 0.7, 2.86, 11.95, 1.1, { valign: 'top' });
  d.code(s, 0.7, 4.15, 5.85, 2.6, '<!-- en sobre-mi.html, en la cabecera\n     y en el pie -->\n<li>\n  <a href="sobre-mi.html"\n     «aria-current="page"»>Sobre mí</a>\n</li>', { size: 10.5 });
  d.code(s, 6.8, 4.15, 5.85, 2.6, '/* el mismo subrayado del hover */\nnav a:hover,\nnav a«[aria-current="page"]» {\n  color: var(--color-text-primary);\n  background-size: 100% 2px;\n}', { size: 10.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · El teclado', 'El contraste: lo que marca Lighthouse', 'La norma WCAG pide 4.5 a 1 para el texto normal y 3 a 1 para el texto grande (24px, o 18.66px en negrita).');
  const filas = [
    ['06B6C4', 'FFFFFF', 'Blanco sobre el cian del manual', '2.47', false],
    ['FFFFFF', '9CA3AF', 'El menú en reposo sobre blanco', '2.54', false],
    ['06B6C4', '0B0F19', 'Texto oscuro sobre el mismo cian', '7.75', true],
    ['0E7490', 'FFFFFF', 'Blanco sobre un cian más oscuro', '5.36', true],
    ['FFFFFF', '6B7280', 'El menú con un gris más oscuro', '4.83', true],
  ];
  filas.forEach(([bg, fg, t, r, ok], i) => {
    const y = 2.86 + i * 0.6;
    d.card(s, 0.7, y, 11.95, 0.52);
    d.card(s, 0.85, y + 0.07, 2.2, 0.38, { fill: bg, line: bg === 'FFFFFF' ? C.line : bg, r: 0.06 });
    d.text(s, 'Ver Proyectos', { x: 0.85, y: y + 0.07, w: 2.2, h: 0.38, size: 12, bold: true, color: fg, align: 'center' });
    d.text(s, t, { x: 3.3, y, w: 4.4, h: 0.52, size: 12, color: C.ink });
    d.text(s, `${fg} sobre ${bg}`, { x: 7.7, y, w: 2.6, h: 0.52, size: 10.5, color: C.sub, font: MONO });
    d.text(s, `${r} a 1`, { x: 10.3, y, w: 1.3, h: 0.52, size: 13, bold: true, color: ok ? C.teal : 'B42318' });
    d.text(s, ok ? 'Pasa' : 'No pasa', { x: 11.55, y, w: 1.0, h: 0.52, size: 11, bold: true, color: ok ? C.teal : 'B42318' });
  });
  d.callout(s, 5.95, 0.78, 'Manda el manual:', 'el portafolio del curso conserva sus colores. En un proyecto tuyo, elige una opción que pase y cámbiala en la variable de CSS y en la de Figma.', { size: 11.5 });
});

// ================= BLOQUE 04
d.divider('CONCEPTUAL', 'Aviso y formularios', '04', ['La página 404', 'Rutas desde la raíz', 'La página de gracias', 'Netlify Forms']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Aviso', 'La página 404', 'Si alguien escribe mal una dirección, Netlify muestra el 404.html de la raíz del sitio.');
  place(d, s, IMG('s15-p-404.png'), 0.7, 2.86, 8.6, 3.9, { align: 'left', valign: 'top' });
  const H = 3.9; const w = (H - 0.16) * (390 / 844) + 0.16;
  d.image(s, IMG('s15-m-404.png'), 12.65 - w, 2.86, w, H, { alt: 'La página 404 en un celular' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Aviso', 'Rutas desde la raíz', 'La 404 puede aparecer en cualquier carpeta. Por eso sus rutas empiezan con /.');
  d.twoCards(s, { t: 'assets/css/global.css', color: 'B42318', items: ['Desde `/proyectos/viejo.html` busca `/proyectos/assets/css/global.css`.', 'Esa carpeta no existe: la 404 se ve sin estilos.'] },
    { t: '/assets/css/global.css', color: C.teal, items: ['La `/` inicial empieza siempre desde la raíz del sitio.', 'Funciona en cualquier carpeta.', 'Va en todas las rutas de la 404: CSS, imágenes y enlaces.'] }, { h: 1.9 });
  d.code(s, 0.7, 4.95, 7.2, 1.8, '<meta name="«robots»" content="«noindex»" />\n<link rel="stylesheet" href="«/»assets/css/global.css" />\n<a href="«/»index.html">Volver al inicio</a>', { size: 10.5 });
  d.callout(s, 4.95, 1.8, 'Con doble clic se ve sin estilos:', 'en tu computadora, `/` es la raíz del disco. Pruébala publicada.', { x: 8.1, w: 4.55, size: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Aviso', 'La página de gracias', 'Aparece después de enviar un formulario. Comparte el estilo con la 404.');
  place(d, s, IMG('s15-p-gracias.png'), 0.7, 2.86, 6.4, 3.9, { align: 'left', valign: 'top' });
  d.code(s, 7.3, 2.86, 5.35, 3.9, '<body class="«pagina-aviso»">\n\n/* el pie queda abajo */\n.pagina-aviso {\n  min-height: 100vh;\n  display: flex;\n  flex-direction: column;\n}\n.pagina-aviso main {\n  «flex: 1;»\n}', { size: 10.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · Formularios', 'Netlify Forms: mensajes sin servidor', 'Tres atributos en <form> y un name en cada campo. Netlify guarda cada mensaje en su panel.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<form class="form-grid"\n      «name="contacto"»\n      «action="/gracias.html"»\n      «method="post"»\n      «data-netlify="true"»>\n\n  <input type="text" id="nombre"\n         «name="nombre»" required />\n  <input type="email" id="correo"\n         «name="correo»" required />\n  …\n</form>', { size: 10.5 });
  d.steps(s, [['name', 'El nombre en el panel.'], ['data-netlify', 'Netlify lo detecta al publicar.'], ['method', 'post: datos ocultos.'], ['action', 'La página de gracias, con /.'], ['Campos', 'Sin name, no se guarda.'], ['Activa', 'Forms › Enable form detection.']], { tw: 1.35 });
});

d.breakSlide('Al volver revisamos el Figma completo, publicamos la versión final y la medimos con Lighthouse.');

// ================= INSTRUMENTAL
d.imageSlide('cinfo-03-instrumental.jpg', 'Instrumental: aplicación del conocimiento con ejercicios y demostraciones');

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Figma', 'En Figma hoy: revisión final y entrega', 'Cada clic está en la Guía de Figma de la sesión 15.');
  d.numCards(s, [
    { t: 'Los nombres', d: 'Ninguna capa se llama `Frame 12` o `Rectangle 3`. Sin capas ocultas ni vacías.' },
    { t: 'Compara', d: 'Pega una captura de tu sitio sobre `mi-portafolio` con Opacidad `50%`.' },
    { t: 'favicon', d: 'Marco de 512 × 512 con `DC`. Exporta `32w` con sufijo `-32`.' },
    { t: 'apple-touch-icon', d: 'Copia sin Radio de esquina. Exporta `180w`.' },
    { t: 'og-portafolio', d: 'Marco de 1200 × 630 con el Hero en pequeño. Exporta `1x`.' },
    { t: 'Comparte', d: '**Cualquier persona con el enlace** y **puede ver**. Después, **Presentar**.' },
  ]);
  d.note(s, 6.62, 'Si tu Figma está en inglés: Export, Share, Anyone with the link, can view, Copy link, Present.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Publicar', 'Publica la versión final en Netlify', 'Dos caminos. Los dos dejan el sitio en la misma dirección.');
  d.twoCards(s, { t: 'A · Arrastrar la carpeta', items: ['Abre tu sitio en **app.netlify.com** › **Deploys**.', 'Arrastra la carpeta que tiene `index.html` directamente dentro.', 'Espera a que diga **Published**.'] },
    { t: 'B · Desde GitHub', items: ['**Add new project** › **Import an existing project** › **GitHub**.', 'En **Publish directory**, la carpeta de `index.html`.', 'Desde ahí, cada `git push` publica solo.'] }, { h: 2.2 });
  d.callout(s, 5.3, 1.1, 'El nombre del sitio:', 'Netlify inventa uno como `funny-panda-12ab34`. Cámbialo con **Change site name** (en el panel nuevo, **Change project name**) y usa ese mismo nombre en `og:image` y `og:url`.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Medir', 'Lighthouse: cuatro notas de 0 a 100', 'F12 › Lighthouse › Mobile › Analyze page load. Hazlo en una ventana de incógnito.');
  place(d, s, IMG('s15-lighthouse.png'), 0.7, 2.86, 11.95, 1.2, { valign: 'top' });
  tres(s, [
    ['Performance', 'Rendimiento', 'Cuánto tarda en verse y en responder'],
    ['Accessibility', 'Accesibilidad', 'Contraste, alt, etiquetas, orden de los títulos'],
    ['Best Practices', 'Buenas prácticas', 'HTTPS, errores en la consola, imágenes'],
    ['SEO', 'Buscadores', '<title>, description, lang, enlaces con texto'],
  ], { y: 4.3, h: 0.5, w: [2.8, 3.0, 6.15], mono: false });
  d.note(s, 6.55, 'Las notas cambian unos puntos entre mediciones. Lee sobre todo la lista de fallas debajo de cada una.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Construimos juntos: el <head> y el teclado', 'Pasos 3 y 4 de la guía de código, en las cinco páginas.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<head>\n  …\n  <title>«Sobre mí · Dagner Chuman»</title>\n  <meta name="description" content="…" />\n  <link rel="icon" … href="assets/img/favicon-32.png" />\n  <meta property="og:title" content="Sobre mí · …" />\n  …\n</head>\n<body>\n  <a class="«saltar»" href="#contenido">Saltar al contenido</a>\n  … <a href="sobre-mi.html" «aria-current="page"»>Sobre mí</a> …\n  <main «id="contenido"»>', { size: 9.5 });
  d.steps(s, [['Título', 'Uno por página.'], ['Descripción', 'Unos 150 caracteres.'], ['Iconos', 'icon y apple-touch-icon.'], ['og:', 'Con la dirección completa.'], ['Saltar', 'Enlace y bloque 11.'], ['Actual', 'aria-current en menú y pie.']], { tw: 1.2 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Ahora tú: aviso, formularios y publicación', 'Tienes 30 minutos. Pasos 5 al 8 de la guía de código.');
  d.numCards(s, [
    { t: '404.html', d: 'Copia de `sobre-mi.html` con rutas que empiezan con `/` y `noindex`.' },
    { t: 'gracias.html', d: 'Rutas normales, `noindex` y el mensaje de gracias.' },
    { t: 'Formularios', d: '`name`, `method="post"`, `action="/gracias.html"` y `data-netlify="true"`.' },
    { t: 'Publica', d: 'Arrastra la carpeta en **Deploys**. Activa la detección en **Forms**.' },
    { t: 'Prueba', d: 'Envía un mensaje; escribe `/hola` y aparece tu 404.' },
    { t: 'Mide', d: 'Lighthouse en incógnito. Guarda la captura para la entrega.' },
  ]);
  d.note(s, 6.62, 'Si terminas antes: valida las siete páginas y recorre todo el sitio solo con el teclado.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Compruébalo', 'El sitio completo, publicado, en escritorio y en el celular.');
  place(d, s, IMG('s15-p-index.png'), 0.7, 2.86, 8.6, 3.9, { align: 'left', valign: 'top' });
  const H = 3.9; const w = (H - 0.16) * (390 / 844) + 0.16;
  d.image(s, IMG('s15-m-index.png'), 12.65 - w, 2.86, w, H, { alt: 'La página de inicio en un celular' });
});

// ================= PROYECTO INTEGRADOR
d.add('INSTRUMENTAL', (s) => {
  d.header(s, 'Proyecto integrador', 'Qué entregas', 'Tu portafolio reúne todo el curso. Lo presentas en la sesión 16: es la Parte B del examen final.');
  d.numCards(s, [
    { t: 'La dirección', d: '`https://tu-nombre.netlify.app`, con las cinco páginas, la 404 y la de gracias.' },
    { t: 'El Figma', d: 'El enlace con permiso **puede ver**.' },
    { t: 'La carpeta', d: 'En `.zip`, con el nombre `apellido-nombre-portafolio.zip`.' },
    { t: 'Lighthouse', d: 'Una captura de `index.html` publicado, en modo Mobile, con las cuatro notas.' },
    { t: 'La bitácora', d: 'Tres prompts o más: qué pediste, qué te dio la IA, qué corregiste y cómo lo comprobaste.' },
    { t: 'Sube todo', d: 'A la tarea **Proyecto integrador** del Aula Virtual, antes de la sesión 16.' },
  ]);
  d.note(s, 6.62, 'La fecha de entrega la indica tu docente en el Aula Virtual.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, 'Proyecto integrador', 'Lo que se revisa', 'Se califica al presentarlo en la sesión 16, con la pauta de presentación (10 puntos).');
  tres(s, [
    ['Estructura', 'HTML semántico, un solo h1 y las siete páginas sin errores en el validador', '02 a 07'],
    ['Fidelidad al diseño', 'Colores, letra, medidas y espacios iguales a Figma', '09 y 10'],
    ['Diseño adaptable', '390, 820 y 1440 px sin barra horizontal ni imágenes deformadas', '12'],
    ['Interacción', 'Hover, transiciones, acordeón y ventana; con mouse y con teclado', '11 y 14'],
    ['Accesibilidad y pruebas', 'alt, foco visible, saltar al contenido, aria-current; Lighthouse 90+', '15'],
    ['Publicación', 'Netlify, enlaces, 404 propia, formulario que guarda, icono y vista previa', '15'],
    ['Uso de la IA', 'Bitácora con 3 prompts o más; sabes explicar todo tu código', 'Extra IA', 'E6F8FA'],
  ], { heads: ['Criterio', 'Logrado', 'Sesiones'], w: [2.9, 7.65, 1.4], h: 0.47, mono: false, size: 11 });
});

// ================= EXTRA · CODIFICAR CON IA (ia.js, contenido en ia_contenido.json)
require('./ia.js').bloqueIA(d, '15');

// ================= NIVELADOR
d.imageSlide('cinfo-04-nivelador.jpg', 'Nivelador: nivel de comprensión del estudiante');
d.checklist('NIVELADOR', [
  'Valido mis páginas y mis hojas en los validadores del W3C.',
  'Sé por qué una imagen se ve en mi computadora y no en Netlify.',
  'Cada página tiene su propio título y su descripción.',
  'Sé qué hacen las etiquetas og: y por qué og:image lleva https://.',
  'El primer Tab muestra «Saltar al contenido».',
  'Marco la página actual con aria-current="page".',
  'Sé por qué la 404 usa rutas que empiezan con /.',
  'Mi formulario guarda los mensajes en Netlify.',
]);
d.consultas('NIVELADOR', [['¿Sin estilos?', 'Mi 404 se ve en blanco y negro.'], ['¿Sin mensajes?', 'Envío el formulario y Forms está vacío.'], ['¿Sin imagen?', 'WhatsApp no muestra la vista previa.'], ['¿Page not found?', 'Netlify no encuentra mi página de inicio.']],
  'Cuando algo falla solo en Netlify', 'Revisa en este orden: mayúsculas y tildes en los nombres de archivo, que `index.html` esté en la raíz de lo que subiste, las rutas con `/` de la 404 y que la detección de formularios esté activa antes de publicar.');

// ================= FUNCIONAL
d.imageSlide('cinfo-05-funcional.jpg', 'Funcional: aplicar lo aprendido');
d.tarea([
  'Completa el <head> de las cinco páginas: título, descripción, iconos y og:.',
  'Agrega «Saltar al contenido» y aria-current en el menú y el pie.',
  'Crea 404.html y gracias.html; conecta los dos formularios con Netlify.',
  'En Figma: revisa los nombres y exporta el icono y la vista previa.',
  'Publica, prueba el formulario y mide con Lighthouse.',
], ['Entregar el proyecto integrador: dirección, Figma, .zip, captura y bitácora.', 'Subirlo al Aula Virtual antes de la sesión 16.', 'El envío es obligatorio dentro del plazo establecido.', 'Se registra en ClassDojo como participación en clase.']);

// ================= ORIENTADOR
d.imageSlide('cinfo-06-orientador.jpg', 'Orientador: conclusión del tema');
d.resumen([
  'Antes de entregar: validadores, enlaces, imágenes, teclado, pantallas y Lighthouse.',
  'Netlify distingue mayúsculas: nombres en minúsculas, con guiones, sin tildes.',
  'Cada página tiene su `<title>` y su `description`.',
  'El icono va con `rel="icon"` y `rel="apple-touch-icon"`; la tarjeta, con `og:`.',
  '`og:image` y `og:url` llevan la dirección completa.',
  '«Saltar al contenido» y `aria-current` hacen el sitio usable con el teclado.',
  'La 404 usa rutas desde la raíz, con `/`, y `noindex`.',
  'Netlify Forms guarda los mensajes con `data-netlify="true"` y un `name` por campo.',
]);
d.hacia('El curso termina. Lo que viene.', [
  ['SESIÓN 13', 'Bootstrap', 'Introducción y su sistema de grillas.'],
  ['SESIÓN 14', 'Bootstrap', 'Componentes, utilidades y tema.'],
  ['SESIÓN 15', 'Proyecto', 'Pruebas y despliegue.', true],
  ['SESIÓN 16', 'Examen', 'Cuestionario y presentación del proyecto (30 %).'],
], 'Para la sesión 16: el cuestionario de las sesiones 1 a 16 y la presentación de tu proyecto. Resuelve el simulacro y ensaya tu guion de 5 minutos.');

require('fs').mkdirSync(path.dirname(out), { recursive: true });
d.save(out).then((n) => console.log('ok', n, 'diapositivas →', out));
