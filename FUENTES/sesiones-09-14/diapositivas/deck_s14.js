// Sesión 14 · Bootstrap avanzado: utilidades, componentes y tema
const path = require('path');
const { Deck, C, MONO } = require('./uss.js');
const { place } = require('./fit.js');
const IMG = (f) => path.join(__dirname, 'img', f);
const out = process.argv[2] || path.join(__dirname, 'out', 'Sesion14-Bootstrap-Componentes-Utilidades-y-Tema.pptx');

const d = new Deck({ title: 'Sesión 14 · Bootstrap: componentes, utilidades y tema' });

// filas de tres columnas: [a, b, c]
const tres = (s, filas, o = {}) => {
  const y0 = o.y || 3.1; const h = o.h || 0.5; const gap = o.gap != null ? o.gap : 0.07; const w = o.w || [3.4, 3.6, 4.35];
  if (o.heads) o.heads.forEach((t, k) => d.text(s, t, { x: 0.95 + w.slice(0, k).reduce((a, b) => a + b, 0), y: y0 - 0.27, w: w[k], h: 0.24, size: 9.5, bold: true, color: C.sub }));
  filas.forEach((f, i) => {
    const y = y0 + i * (h + gap);
    d.card(s, 0.7, y, 11.95, h, { fill: f[3] || C.white });
    let x = 0.95;
    f.slice(0, 3).forEach((t, k) => {
      d.text(s, t, { x, y, w: w[k] - 0.15, h, size: o.size || 11.5, bold: k === 0, color: k === 0 ? C.ink : (k === 1 ? C.teal : C.body), font: k === 1 ? MONO : undefined, codeColor: C.ink });
      x += w[k];
    });
  });
};

d.waiting('14', 'Abre tu portafolio y tu archivo de Figma. Hoy la página Cursos recibe componentes y tus colores.');
d.title({
  titulo: 'Componentes y tema de Bootstrap',
  sesion: '14',
  sub: 'Utilidades · card · alert · accordion · modal · navbar · variables --bs-*',
  code: '<article class="card">\n  <div class="card-body">\n    …\n  </div>\n</article>',
});
d.imageSlide('como-te-sientes.jpg', '¿Cómo te sientes hoy?');
d.imageSlide('que-es-cinfo.jpg', '¿Qué es CINFO? Conceptual, Instrumental, Nivelador, Funcional y Orientador');
d.imageSlide('conocimientos-previos.jpg', 'Conocimientos previos y definiciones clave');

d.add('CONCEPTUAL', (s) => {
  d.header(s, 'Repaso', 'De dónde venimos', 'La página Cursos ya usa la grilla de Bootstrap. Su aspecto todavía sale de cursos.css.');
  d.twoCards(s, { t: 'Ya tienes', color: C.sub, items: ['Bootstrap enlazado desde el CDN, antes que tus hojas.', 'La grilla: `row`, `col-*`, `g-4` y `offset-*`.', 'La guía de 12 columnas en Figma.'] },
    { t: 'Hoy sumas', items: ['Utilidades: clases de una sola propiedad.', 'Componentes: tarjetas, aviso, acordeón y ventana.', 'Un tema: Bootstrap con los colores de tu Figma.'] });
  d.callout(s, 5.18, 1.42, 'Lo que hace distinta a esta sesión', '\nEl HTML de la página crece y tu CSS se achica: `cursos.css` pasa de 189 líneas a 60. Lo que queda en tu CSS es lo que hace tuyo el diseño.');
});

d.logros([
  ['Combinar', 'Armar una sección con utilidades de espaciado, flex, color y bordes.'],
  ['Componer', 'Usar los componentes card, badge, alert, accordion y modal.'],
  ['Activar', 'Hacer funcionar el acordeón y la ventana con el JavaScript de Bootstrap.'],
  ['Personalizar', 'Cambiar las variables `--bs-*` para que Bootstrap use tu Figma.'],
  ['Conectar', 'Guardar los colores de Figma como variables y aplicarlos.'],
]);

d.agenda([
  ['01', 'Utilidades', 'Espaciado, flex, texto, color, bordes y !important.', 35],
  ['02', 'Componentes', 'card, badge, iconos y alert.', 35],
  ['03', 'Componentes con JavaScript', 'Acordeón, ventana modal, formularios y navbar.', 40],
  ['04', 'El tema', 'Las variables --bs-* con tus colores.', 25],
  ['—', 'Descanso', '', 15],
  ['05', 'Figma: variables y componente', 'Variables locales y course-card con variantes.', 25],
  ['06', 'Práctica en la página Cursos', 'Tema, tarjetas, acordeón e inscripción.', 45],
]);

// ================= BLOQUE 01
d.divider('CONCEPTUAL', 'Utilidades', '01', ['Una clase, una propiedad', 'Espaciado', 'Flex, texto y color', 'Bordes, sombras y tamaños', 'Responsivas y !important']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Utilidades', 'Una clase, una propiedad', 'Una utilidad aplica una sola propiedad de CSS. Se combinan en el HTML como piezas.');
  d.card(s, 0.7, 2.86, 5.85, 2.9, { fill: C.white });
  d.text(s, 'Sesión 13 · tu CSS', { x: 1.0, y: 2.98, w: 5.3, h: 0.32, size: 13.5, bold: true, color: C.ink });
  d.code(s, 1.0, 3.4, 5.25, 2.2, '«.paso» {\n  height: 100%;\n  background-color: #FFFFFF;\n  border: 1px solid var(--color-border);\n  border-radius: 12px;\n  padding: 1.5rem;\n}', { size: 10.5 });
  d.card(s, 6.8, 2.86, 5.85, 2.9, { fill: C.soft });
  d.text(s, 'Sesión 14 · utilidades', { x: 7.1, y: 2.98, w: 5.3, h: 0.32, size: 13.5, bold: true, color: C.teal });
  d.code(s, 7.1, 3.4, 5.25, 2.2, '<div class="«h-100 bg-white border»\n            «rounded-3 p-4»">\n  …\n</div>\n\n<!-- el mismo resultado,\n     sin una línea de CSS -->', { size: 10.5 });
  d.callout(s, 5.95, 0.72, '¿Cuándo usarlas?', 'para ajustes comunes: márgenes, alineación, colores. Si una combinación se repite mucho o es muy tuya, escríbela en tu CSS.', { size: 11.5 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Utilidades', 'Espaciado: m y p', 'Propiedad + lado + tamaño. Los tamaños van de 0 a 5.');
  place(d, s, IMG('bs-espaciado.png'), 0.7, 2.86, 6.6, 1.6, { align: 'left', valign: 'top' });
  d.rows(s, [
    { a: 'm · p', b: 'margin · padding', c: '`p-4`: relleno de 24px' },
    { a: 't b s e', b: 'arriba, abajo, inicio (izquierda), fin (derecha)', c: '`mb-3`: margen inferior de 16px' },
    { a: 'x · y', b: 'izquierda y derecha · arriba y abajo', c: '`px-2 py-1`' },
    { a: '0 1 2 3 4 5', b: '0 · 4px · 8px · 16px · 24px · 48px', c: '`gap-2`: también en flex' },
  ], { y: 4.62, h: 0.5, gap: 0.07, aw: 2.0, bw: 5.2, asize: 12, bsize: 11.5, csize: 11 });
  d.card(s, 7.5, 2.86, 5.15, 1.6, { fill: C.soft });
  d.text(s, ['`s` y `e` (start y end) en vez de left y right: así Bootstrap también sirve para idiomas que se leen de derecha a izquierda.'], { x: 7.72, y: 2.95, w: 4.75, h: 1.45, size: 11, color: C.body, valign: 'middle', codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Utilidades', 'Flex, texto y color', 'Lo que escribiste en CSS desde la sesión 09, ahora como clases.');
  tres(s, [
    ['Flex', 'd-flex justify-content-between', 'display: flex; justify-content: space-between'],
    ['Alinear y separar', 'align-items-center gap-2', 'align-items: center; gap: 8px'],
    ['Texto', 'text-center fw-bold fs-5 small', 'Alineación, grosor, tamaño y letra pequeña'],
    ['Color de texto', 'text-primary text-body-secondary', 'El color principal y el gris de los textos'],
    ['Fondo', 'bg-white bg-primary-subtle', 'Fondo blanco o un cian muy claro'],
    ['Texto y fondo', 'text-bg-dark', 'Fondo oscuro con el texto claro que le corresponde'],
    ['Listas', 'list-unstyled', 'Sin viñetas ni sangría'],
  ], { heads: ['Para', 'Clases', 'Equivale a'], w: [2.6, 4.3, 4.85], h: 0.47 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Utilidades', 'Bordes, sombras, tamaños y accesibilidad', 'Trazo, Radio y Sombra de Figma, también como clases.');
  tres(s, [
    ['Borde', 'border border-top border-4', 'Trazo en los cuatro lados, solo arriba o de 4px'],
    ['Color del borde', 'border-primary border-primary-subtle', 'El cian de la marca o uno claro'],
    ['Radio', 'rounded-3 rounded-pill', 'Radio de 8px · extremos redondos'],
    ['Sombra', 'shadow-sm shadow', 'Una Sombra paralela suave o media'],
    ['Tamaño', 'h-100 w-100', 'Alto o ancho del 100 %'],
    ['Oculto a la vista', 'visually-hidden', 'No se ve, pero el lector de pantalla lo lee', 'E6F8FA'],
  ], { heads: ['Para', 'Clases', 'Qué hace'], w: [2.6, 4.3, 4.85], h: 0.5 });
  d.note(s, 6.5, 'Seis botones «Inscribirme» iguales: un span visually-hidden completa cada uno, «en Diseño Web».');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Utilidades', 'Responsivas y con !important', 'Como la grilla, una utilidad acepta un punto de quiebre: vale desde ese ancho hacia arriba.');
  d.rows(s, [
    { a: 'p-4 p-md-5', b: 'Relleno de 24px en el celular y 48px desde 768px.', c: 'El llamado de tu página' },
    { a: 'd-none d-lg-block', b: 'Oculto en el celular; visible desde 992px.', c: 'Algo que no cabe en el celular' },
    { a: 'text-center text-lg-start', b: 'Centrado en el celular; a la izquierda desde 992px.', c: 'Un título' },
  ], { aw: 3.2, bw: 5.0, h: 0.6, gap: 0.08, asize: 12, bsize: 11.5, csize: 11 });
  d.callout(s, 5.15, 1.3, 'Las utilidades usan !important', '\npara ganar siempre, sin importar la especificidad. Si una utilidad no te deja cambiar algo desde tu CSS, cambia la clase en el HTML. Es una de las pocas veces en que `!important` tiene sentido (sesión 11).');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Utilidades', '«Cómo trabajamos», solo con utilidades', 'La misma sección de la sesión 13. cursos.css pierde el bloque de los pasos.');
  d.code(s, 0.7, 2.86, 6.3, 3.0, '<ol class="«row g-4 list-unstyled»">\n  <li class="col-12 col-sm-6 col-lg-3">\n    <div class="«h-100 bg-white border rounded-3 p-4»">\n      <i class="bi bi-pencil-square «fs-3 text-primary»"\n         aria-hidden="true"></i>\n      <h3 class="«fs-6 fw-bold mt-3 mb-2»">1. Diseñas</h3>\n      <p class="«small mb-0»">Cada proyecto empieza…</p>\n    </div>\n  </li>\n</ol>', { size: 10 });
  place(d, s, IMG('s14-pasos.png'), 7.2, 2.86, 5.45, 3.0, { valign: 'top' });
  d.note(s, 6.15, 'Antes: 50 líneas de CSS para .pasos, .paso y .paso-num. Ahora: ninguna.');
});

// ================= BLOQUE 02
d.divider('CONCEPTUAL', 'Componentes', '02', ['Qué es un componente', 'card: la tarjeta', 'badge e iconos', 'alert: el aviso']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Componentes', 'Qué es un componente', 'Un bloque de HTML con sus clases ya diseñadas. Copias el modelo de la documentación y lo adaptas.');
  d.numCards(s, [
    { t: 'card', d: 'Una tarjeta con cuerpo, título, texto y pie. **Hoy.**' },
    { t: 'badge', d: 'Una insignia pequeña: el nivel del curso. **Hoy.**' },
    { t: 'alert', d: 'Un aviso destacado con su color. **Hoy.**' },
    { t: 'accordion', d: 'Preguntas que se abren y se cierran. Necesita JavaScript. **Hoy.**' },
    { t: 'modal', d: 'Una ventana sobre la página. Necesita JavaScript. **Hoy.**' },
    { t: 'navbar', d: 'Un menú que se pliega en el celular. Necesita JavaScript. Ampliación.' },
  ]);
  d.note(s, 6.62, 'Es la misma idea que un componente de Figma (sesión 11): un diseño que se repite con distintos contenidos.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Componentes', 'card: la tarjeta de curso', 'Reemplaza al article.curso de la sesión 13. La grilla no cambia.');
  d.code(s, 0.7, 2.86, 7.0, 3.86, '<article class="«card h-100 shadow-sm»">\n  <div class="«card-body»">\n    <div class="d-flex justify-content-between align-items-center mb-3">\n      <i class="bi bi-code-slash fs-2 text-primary" aria-hidden="true"></i>\n      <span class="«badge rounded-pill» bg-primary-subtle …">Básico</span>\n    </div>\n    <h3 class="«card-title» fs-5">Diseño Web</h3>\n    <p class="«card-text»">HTML5, CSS3, Flexbox…</p>\n  </div>\n  <div class="«card-footer» d-flex justify-content-between align-items-center">\n    <small class="text-body-secondary">16 sesiones</small>\n    <button class="btn btn-primary btn-sm" …>Inscribirme</button>\n  </div>\n</article>', { size: 9.5 });
  place(d, s, IMG('s14-card.png'), 7.9, 2.86, 4.75, 2.75, { valign: 'top' });
  d.text(s, ['`h-100`: todas las tarjetas de una fila miden lo mismo.', '`card-footer`: el pie, con una línea encima.'], { x: 7.95, y: 5.75, w: 4.7, h: 1.0, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 4, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Componentes', 'Insignias e iconos', 'Dos niveles, dos estilos de insignia. Los iconos llegan con Bootstrap Icons.');
  place(d, s, IMG('s14-card.png'), 0.7, 2.86, 3.9, 2.3, { valign: 'top' });
  place(d, s, IMG('s14-card-intermedio.png'), 4.8, 2.86, 3.9, 2.3, { valign: 'top' });
  d.code(s, 0.7, 5.3, 8.0, 1.4, '<span class="«badge rounded-pill bg-primary-subtle text-primary-emphasis»">Básico</span>\n<span class="«badge rounded-pill text-bg-dark»">Intermedio</span>\n\n<i class="«bi bi-git»" aria-hidden="true"></i>   <!-- decorativo: el lector no lo anuncia -->', { size: 10 });
  d.card(s, 8.9, 2.86, 3.75, 3.84, { fill: C.soft });
  d.text(s, 'Por qué no text-bg-primary', { x: 9.12, y: 3.0, w: 3.35, h: 0.32, size: 12.5, bold: true, color: C.teal });
  d.text(s, 'El blanco sobre cian tiene poco contraste para una letra tan pequeña. La versión subtle usa un fondo claro y un texto oscuro: se lee mejor.', { x: 9.12, y: 3.4, w: 3.35, h: 1.8, size: 11, color: C.body, valign: 'top' });
  d.text(s, 'Bootstrap Icons: más de 2000 iconos. Busca el nombre en icons.getbootstrap.com.', { x: 9.12, y: 5.3, w: 3.35, h: 1.2, size: 11, color: C.body, valign: 'top' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Componentes', 'alert y la tarjeta de cifras', 'Un aviso al inicio de la página y las cifras de la sesión 13, ahora como card.');
  place(d, s, IMG('s14-alert.png'), 0.7, 2.86, 11.95, 0.75, { valign: 'top' });
  d.code(s, 0.7, 3.75, 11.95, 0.85, '<div class="«alert alert-primary d-flex align-items-center gap-2» mb-5">\n  <i class="bi bi-calendar-check" aria-hidden="true"></i> <span><strong>Inscripciones abiertas</strong> para el próximo ciclo.</span></div>', { size: 10.5, valign: 'middle' });
  place(d, s, IMG('s14-cifras.png'), 0.7, 4.75, 5.0, 1.95, { align: 'left', valign: 'top' });
  d.code(s, 5.9, 4.75, 6.75, 1.95, '<aside class="«card border-0 border-top border-4»\n              «border-primary shadow-sm»">\n  <div class="card-body">\n    <div class="row row-cols-3 g-3 text-center"> … </div>\n  </div>\n</aside>', { size: 10 });
});

// ================= BLOQUE 03
d.divider('CONCEPTUAL', 'Componentes con JavaScript', '03', ['El JavaScript de Bootstrap', 'El acordeón', 'La ventana modal', 'Formularios', 'La barra de navegación']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · JavaScript', 'El JavaScript de Bootstrap', 'Se enlaza una vez, al final del body. Después, los componentes se activan con atributos data-bs-*.');
  d.code(s, 0.7, 2.86, 11.95, 1.25, '<script src="«https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js»"\n        integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"\n        crossorigin="anonymous"></script>', { size: 11.5 });
  d.rows(s, [
    { a: 'bundle', b: 'Incluye Popper, la librería que coloca menús y globos de ayuda.', c: 'Un solo archivo' },
    { a: 'al final del body', b: 'Cuando se ejecuta, el HTML ya existe.', c: 'Como el reproductor (sesión 07)' },
    { a: 'data-bs-toggle', b: 'Qué hace el botón: `collapse`, `modal`…', c: 'Sin escribir JavaScript' },
    { a: 'data-bs-target', b: 'Sobre qué elemento: su `id`, con `#`.', c: '`#faq-1`, `#inscripcion`' },
  ], { y: 4.3, h: 0.52, gap: 0.07, aw: 2.4, bw: 5.6, asize: 12, bsize: 11.5, csize: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · JavaScript', 'El acordeón de preguntas', 'Una respuesta abierta a la vez. Bootstrap actualiza aria-expanded por ti.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<div class="«accordion»" id="faq">\n  <div class="«accordion-item»">\n    <h3 class="«accordion-header»">\n      <button class="«accordion-button»" type="button"\n              data-bs-toggle="«collapse»"\n              data-bs-target="«#faq-1»"\n              aria-expanded="true" aria-controls="faq-1">\n        ¿Necesito saber programar?\n      </button>\n    </h3>\n    <div id="faq-1" class="«accordion-collapse collapse show»"\n         data-bs-parent="«#faq»">\n      <div class="accordion-body">No para los cursos…</div>\n    </div>\n  </div>\n</div>', { size: 9.5 });
  place(d, s, IMG('s14-faq.png'), 7.8, 2.86, 4.85, 2.6, { valign: 'top' });
  d.text(s, ['`show`: abierta al cargar.', '`data-bs-parent`: al abrir una, cierra las demás.'], { x: 7.85, y: 5.6, w: 4.8, h: 1.1, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 4, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · JavaScript', 'La ventana modal de inscripción', 'Va al final del body, oculta. Cada botón «Inscribirme» la abre.');
  d.code(s, 0.7, 2.86, 6.2, 3.86, '<button class="btn btn-primary btn-sm"\n        data-bs-toggle="«modal»"\n        data-bs-target="«#inscripcion»">Inscribirme</button>\n\n<div class="«modal fade»" id="inscripcion" tabindex="-1"\n     role="dialog" aria-labelledby="inscripcion-titulo">\n  <div class="«modal-dialog modal-dialog-centered»">\n    <div class="«modal-content»">\n      <div class="modal-header"> título y «btn-close» </div>\n      <div class="modal-body"> el formulario </div>\n      <div class="modal-footer"> Cancelar · Enviar </div>\n    </div>\n  </div>\n</div>', { size: 9.5 });
  place(d, s, IMG('s14-modal.png'), 7.1, 2.86, 5.55, 3.2, { valign: 'top' });
  d.text(s, 'Se cierra con la X, con Cancelar (`data-bs-dismiss`), con `Esc` o con un clic en el fondo.', { x: 7.1, y: 6.15, w: 5.55, h: 0.55, size: 11, color: C.body, valign: 'top', codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · JavaScript', 'Formularios con las clases de Bootstrap', 'El mismo HTML de la sesión 06, con clases que le dan forma.');
  d.code(s, 0.7, 2.86, 6.6, 3.86, '<div class="«mb-3»">\n  <label for="ins-nombre" class="«form-label»">Nombre completo</label>\n  <input type="text" class="«form-control»" id="ins-nombre"\n         name="nombre" autocomplete="name" required />\n</div>\n<select class="«form-select»" id="ins-curso" name="curso" required>\n  <option value="">Elige un curso</option> …\n</select>\n<div class="«form-check form-check-inline»">\n  <input class="«form-check-input»" type="radio" name="modalidad"\n         id="ins-virtual" value="virtual" />\n  <label class="«form-check-label»" for="ins-virtual">Virtual</label>\n</div>', { size: 9.5 });
  d.card(s, 7.5, 2.86, 5.15, 3.86, { fill: C.soft });
  d.text(s, 'Opcional: el curso ya elegido', { x: 7.72, y: 2.98, w: 4.75, h: 0.32, size: 13, bold: true, color: C.teal });
  d.code(s, 7.72, 3.4, 4.7, 2.1, '«modalInscripcion».addEventListener(\n  «\'show.bs.modal\'», (evento) => {\n    const boton = evento.relatedTarget;\n    selectCurso.value =\n      boton.dataset.curso;\n  });', { size: 9.5 });
  d.text(s, 'Bootstrap avisa al abrir la ventana y dice qué botón la abrió. El botón guarda su curso en `data-curso`.', { x: 7.72, y: 5.6, w: 4.75, h: 1.0, size: 10.5, color: C.body, valign: 'top', codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '03 · JavaScript', 'Ampliación: la barra de navegación', 'Tu portafolio conserva su cabecera. Para un proyecto nuevo, navbar trae el menú plegable.');
  place(d, s, IMG('bs-navbar-cerrada.png'), 0.7, 2.86, 3.7, 1.1, { valign: 'top' });
  d.text(s, 'Celular: el botón de tres rayas', { x: 0.7, y: 4.0, w: 3.7, h: 0.26, size: 10.5, bold: true, color: C.sub, align: 'center' });
  place(d, s, IMG('bs-navbar-abierta.png'), 0.7, 4.35, 3.7, 2.4, { valign: 'top' });
  place(d, s, IMG('bs-navbar-escritorio.png'), 4.6, 2.86, 8.05, 0.75, { valign: 'top' });
  d.text(s, 'Desde 992px (navbar-expand-lg): el menú completo', { x: 4.6, y: 3.66, w: 8.05, h: 0.26, size: 10.5, bold: true, color: C.sub, align: 'center' });
  d.code(s, 4.6, 4.05, 8.05, 2.7, '<nav class="«navbar navbar-expand-lg» bg-white border-bottom">\n  <div class="container">\n    <a class="«navbar-brand»" href="index.html">Mi sitio</a>\n    <button class="«navbar-toggler»" data-bs-toggle="collapse"\n            data-bs-target="«#menu»" aria-label="Abrir el menú"> … </button>\n    <div class="«collapse navbar-collapse»" id="menu">\n      <ul class="«navbar-nav ms-auto»"> … nav-item y nav-link … </ul>\n    </div>\n  </div>\n</nav>', { size: 9.5 });
});

// ================= BLOQUE 04
d.divider('CONCEPTUAL', 'El tema', '04', ['Antes y después', 'Las variables --bs-*', 'Variables de cada componente', 'Lo que no tiene variable', 'El orden de las hojas']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · El tema', 'Bootstrap con tus colores', 'La misma página, sin y con tema-bootstrap.css. No cambió ni una clase del HTML.');
  const r1 = place(d, s, IMG('s14-sin-tema-cards.png'), 0.7, 2.86, 5.85, 1.75, { valign: 'top' });
  d.text(s, 'Sin tema: el azul #0D6EFD de Bootstrap', { x: 0.7, y: r1.y + r1.h + 0.06, w: 5.85, h: 0.26, size: 10.5, bold: true, color: C.red, align: 'center' });
  place(d, s, IMG('s14-con-tema-cards.png'), 6.8, 2.86, 5.85, 1.75, { valign: 'top' });
  d.text(s, 'Con tema: el cian 06B6C4 de tu Figma', { x: 6.8, y: r1.y + r1.h + 0.06, w: 5.85, h: 0.26, size: 10.5, bold: true, color: C.teal, align: 'center' });
  const yf = r1.y + r1.h + 0.45;
  place(d, s, IMG('s14-sin-tema-faq.png'), 0.7, yf, 5.85, 6.85 - yf, { valign: 'top' });
  place(d, s, IMG('s14-con-tema-faq.png'), 6.8, yf, 5.85, 6.85 - yf, { valign: 'top' });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · El tema', 'Las variables --bs-*', 'Bootstrap guarda su tema en variables de CSS. Si cambias su valor, cambian las utilidades y los componentes.');
  d.code(s, 0.7, 2.86, 7.1, 3.86, '/* tema-bootstrap.css · bloque 1 */\n:root {\n  «--bs-primary»: #06B6C4;\n  «--bs-primary-rgb»: 6, 182, 196;\n  «--bs-primary-bg-subtle»: #E6F8FA;\n  «--bs-primary-text-emphasis»: #035F66;\n  «--bs-dark-rgb»: 11, 15, 25;\n  «--bs-body-font-family»: \'Geist\', sans-serif;\n  «--bs-body-color»: #374151;\n  «--bs-border-color»: #E5E7EB;\n  «--bs-border-radius»: 8px;\n  «--bs-border-radius-lg»: 12px;\n}', { size: 10.5 });
  d.card(s, 8.0, 2.86, 4.65, 3.86, { fill: C.soft });
  d.text(s, '¿Por qué el color dos veces?', { x: 8.22, y: 2.98, w: 4.25, h: 0.32, size: 13, bold: true, color: C.teal });
  d.text(s, ['`--bs-primary-rgb` es el mismo color en números.', 'Las utilidades le suman una opacidad: `rgba(var(--bs-primary-rgb), 0.5)`.', 'Si cambias una, cambia la otra.'], { x: 8.22, y: 3.4, w: 4.25, h: 3.2, size: 11, color: C.body, valign: 'top', bullet: true, paraAfter: 6, codeColor: C.ink });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · El tema', 'Variables de componente y reglas fijas', 'Algunos componentes guardan sus colores en variables propias. Otros, en la regla.');
  d.code(s, 0.7, 2.86, 5.85, 3.86, '/* bloque 2: en la clase del componente */\n«.btn-primary» {\n  --bs-btn-bg: #06B6C4;\n  --bs-btn-border-color: #06B6C4;\n  --bs-btn-hover-bg: #05A3B0;   /* sesión 11 */\n  …\n}\n«.card» {\n  --bs-card-border-radius: 12px;\n}\n«.accordion» {\n  --bs-accordion-active-bg: #E6F8FA;\n  …\n}', { size: 10 });
  d.code(s, 6.8, 2.86, 5.85, 2.3, '/* bloque 3: color escrito en la regla */\n«.form-control:focus»,\n«.form-select:focus» {\n  border-color: #06B6C4;\n  box-shadow: 0 0 0 0.25rem\n    rgba(6, 182, 196, 0.25);\n}', { size: 10 });
  d.callout(s, 5.3, 1.42, 'Cómo saberlo:', 'en DevTools, inspecciona el componente. Si en Styles ves `var(--bs-…)`, cambia la variable. Si ves un color escrito, reemplaza la regla.', { x: 6.8, w: 5.85, size: 11 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '04 · El tema', 'Seis hojas, en este orden', 'Bootstrap, sus iconos y tu tema primero. Después, tus hojas de siempre.');
  [['bootstrap.min.css', 'Reboot, grilla, utilidades y componentes', C.sub], ['bootstrap-icons.min.css', 'Los iconos', C.sub], ['tema-bootstrap.css', 'Las variables --bs-* con tu Figma: nuevo', C.teal], ['global.css', 'Tus tokens, tu reinicio y tu letra', C.teal], ['header.css', 'Tu cabecera y tu pie', C.teal], ['cursos.css', 'La caja central, los títulos y el movimiento', C.teal]].forEach(([f, dsc, col], i) => {
    const y = 2.86 + i * 0.62;
    d.circle(s, 0.8, y + 0.07, 0.42, i + 1, { fill: col, size: 11.5 });
    d.card(s, 1.4, y, 11.25, 0.54, { fill: f === 'tema-bootstrap.css' ? 'E6F8FA' : C.white });
    d.text(s, f, { x: 1.62, y, w: 3.6, h: 0.54, size: 12.5, bold: true, color: col === C.sub ? C.ink : C.teal, font: MONO });
    d.text(s, dsc, { x: 5.3, y, w: 7.2, h: 0.54, size: 11.5, color: C.body });
  });
  d.note(s, 6.75, 'Y al final del body: bootstrap.bundle.min.js y, si lo usas, inscripcion.js.');
});

d.breakSlide('Al volver guardamos los colores de Figma como variables y armamos la página con componentes.');

// ================= INSTRUMENTAL
d.imageSlide('cinfo-03-instrumental.jpg', 'Instrumental: aplicación del conocimiento con ejercicios y demostraciones');

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Figma', 'En Figma hoy: variables y el componente de curso', 'Ampliación del manual. Cada clic está en la Guía de Figma de la sesión.');
  d.numCards(s, [
    { t: 'La colección', d: 'Sin nada seleccionado: **Variables locales** › **Abrir variables**. Llámala `tokens`.' },
    { t: '8 colores', d: '`color-primary`, `color-primary-hover`, `color-border`… con los códigos de Figma.' },
    { t: '3 números', d: '`radius-sm` 8, `radius-md` 12 y `gutter` 24.' },
    { t: 'Aplícalas', d: 'En Relleno, el icono de cuatro puntos; en un campo numérico, el icono de variable.' },
    { t: 'Dos niveles', d: '`course-card` con las variantes `Nivel=Básico` y `Nivel=Intermedio`.' },
    { t: 'Prueba', d: 'Cambia `color-primary`: cambian todos los botones. Deshaz con `Ctrl + Z`.' },
  ]);
  d.note(s, 6.62, 'Si tu Figma está en inglés: Local variables, Open variables, Create variable, Apply variable.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '05 · Figma', 'Una variable, tres lugares', 'El mismo nombre en Figma, en tu CSS y en el tema de Bootstrap.');
  tres(s, [
    ['color-primary · 06B6C4', '--color-primary', '--bs-primary · --bs-btn-bg'],
    ['color-primary-hover · 05A3B0', '--color-primary-hover', '--bs-btn-hover-bg'],
    ['color-primary-subtle · E6F8FA', '(solo en el tema)', '--bs-primary-bg-subtle'],
    ['color-text-primary · 0B0F19', '--color-text-primary', '--bs-dark-rgb'],
    ['color-text-secondary · 374151', '--color-text-secondary', '--bs-body-color'],
    ['color-border · E5E7EB', '--color-border', '--bs-border-color'],
    ['radius-md · 12', '--radius-md', '--bs-card-border-radius'],
  ], { heads: ['Variable en Figma', 'En global.css', 'En tema-bootstrap.css'], w: [3.9, 3.6, 4.25], h: 0.47, size: 11 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Construimos juntos: el tema y las tarjetas', 'Pasos 0 al 3 de la guía de código.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<!-- head: después de bootstrap.min.css -->\n<link rel="stylesheet" href="«…/bootstrap-icons.min.css»" … />\n<link rel="stylesheet" href="«assets/css/tema-bootstrap.css»" />\n\n<!-- cada tarjeta del catálogo -->\n<article class="«card h-100 shadow-sm»">\n  <div class="«card-body»"> icono, insignia, título, texto </div>\n  <div class="«card-footer» d-flex justify-content-between\n              align-items-center">\n    <small class="text-body-secondary">16 sesiones</small>\n    <button class="btn btn-primary btn-sm" …>Inscribirme</button>\n  </div>\n</article>', { size: 10 });
  d.steps(s, [['Enlaza', 'Iconos y tema; el JS al final.'], ['Tema', 'Los tres bloques de variables.'], ['Card', 'article.card con body y footer.'], ['Insignia', 'badge subtle o text-bg-dark.'], ['Borra', 'El bloque .curso de cursos.css.'], ['Prueba', 'Botones cian, no azules.']], { tw: 1.0 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Construimos juntos: el acordeón', 'Paso 5 de la guía de código. Cuatro preguntas, una abierta a la vez.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<div class="row">\n  <div class="«col-lg-8»">\n    <h2 id="titulo-faq">Preguntas frecuentes</h2>\n    <div class="«accordion»" id="«faq»">\n      <div class="accordion-item"> … pregunta 1, con show … </div>\n      <div class="accordion-item"> … pregunta 2 … </div>\n      <div class="accordion-item"> … pregunta 3 … </div>\n      <div class="accordion-item"> … pregunta 4 … </div>\n    </div>\n  </div>\n</div>', { size: 10.5 });
  d.steps(s, [['Contenedor', 'div.accordion con id="faq".'], ['Pregunta', 'Un button en un h3.'], ['Respuesta', 'collapse con su id.'], ['Enlaza', 'data-bs-target="#faq-2".'], ['Uno a la vez', 'data-bs-parent="#faq".'], ['Teclado', 'Tab y Enter la abren.']], { tw: 1.2 });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Ahora tú: aviso, pasos, llamado e inscripción', 'Tienes 25 minutos. Pasos 1, 4, 6 y 7 de la guía de código.');
  d.numCards(s, [
    { t: 'El aviso', d: '`alert alert-primary` con un icono, al inicio de `main`.' },
    { t: 'Los pasos', d: 'Solo utilidades: `h-100 bg-white border rounded-3 p-4`.' },
    { t: 'El llamado', d: '`text-bg-dark rounded-3 p-4 p-md-5` y un `btn btn-primary btn-lg`.' },
    { t: 'La ventana', d: 'El `modal` al final del body; los botones con `data-bs-target`.' },
    { t: 'El formulario', d: '`form-label`, `form-control`, `form-select` y `form-check`.' },
    { t: 'Valida y prueba', d: 'W3C sin errores. Abre y cierra la ventana solo con el teclado.' },
  ]);
  d.note(s, 6.62, 'Si terminas antes: inscripcion.js, para que la ventana se abra con el curso ya elegido.');
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '06 · Práctica', 'Compruébalo', 'La página Cursos terminada, en escritorio y en el celular.');
  place(d, s, IMG('s14-cursos-1440.png'), 0.7, 2.86, 8.6, 3.9, { align: 'left', valign: 'top' });
  const H = 3.9; const w = (H - 0.16) * (390 / 844) + 0.16;
  d.image(s, IMG('s14-movil.png'), 12.65 - w, 2.86, w, H, { alt: 'La página Cursos en un celular' });
});

// ================= NIVELADOR
d.imageSlide('cinfo-04-nivelador.jpg', 'Nivelador: nivel de comprensión del estudiante');
d.checklist('NIVELADOR', [
  'Sé qué es una utilidad y leo mb-3, p-md-5 o d-lg-block.',
  'Sé por qué las utilidades usan !important y cómo cambiar una.',
  'Armo una tarjeta con card, card-body, card-title y card-footer.',
  'Enlazo el JavaScript de Bootstrap al final del body.',
  'Conecto un botón con su acordeón o su ventana con data-bs-target.',
  'Sé qué hace data-bs-parent en un acordeón.',
  'Cambio el color de Bootstrap con --bs-primary y --bs-primary-rgb.',
  'Mis colores de Figma están guardados como variables.',
]);
d.consultas('NIVELADOR', [['¿No abre?', 'La ventana o el acordeón no hacen nada.'], ['¿Sigue azul?', 'Cambié --bs-primary y el botón sigue azul.'], ['¿Cuadros?', 'Los iconos se ven como cuadros vacíos.'], ['¿Utilidad o CSS?', '¿Cuándo escribo mi propio CSS?']],
  'Cuando un componente no responde', 'Revisa en este orden: que el JavaScript de Bootstrap esté al final del body, que `data-bs-target` lleve `#` y coincida con el `id`, que el tema esté después de Bootstrap y que el botón azul tenga su regla `.btn-primary` en el tema.');

// ================= FUNCIONAL
d.imageSlide('cinfo-05-funcional.jpg', 'Funcional: aplicar lo aprendido');
d.tarea([
  'Crea tema-bootstrap.css y enlázalo justo después de Bootstrap.',
  'Pasa las tarjetas a card y los pasos y el llamado a utilidades.',
  'Agrega el aviso, el acordeón de preguntas y la ventana de inscripción.',
  'En Figma: las variables locales y course-card con dos variantes.',
  'Valida y publica en Netlify; prueba la página solo con el teclado.',
], ['Subir la URL publicada al Aula Virtual.', 'Adjuntar el enlace de Figma con las variables.', 'El envío es obligatorio dentro del plazo establecido.', 'Se registra en ClassDojo como participación en clase.']);

// ================= ORIENTADOR
d.imageSlide('cinfo-06-orientador.jpg', 'Orientador: conclusión del tema');
d.resumen([
  'Una utilidad aplica una sola propiedad: `mb-3`, `d-flex`, `text-center`.',
  'Las utilidades aceptan punto de quiebre (`p-md-5`) y usan `!important`.',
  'Un componente es HTML con clases ya diseñadas: card, badge, alert.',
  'El acordeón y la ventana funcionan con el JavaScript de Bootstrap y `data-bs-*`.',
  '`data-bs-target` apunta a un `id` con `#`; `data-bs-parent` deja una respuesta abierta.',
  'El tema cambia las variables `--bs-*` para que Bootstrap use tu Figma.',
  'Lo que no tiene variable se reemplaza con una regla en el tema.',
  'Las variables de Figma, de `global.css` y del tema llevan los mismos nombres.',
]);
d.hacia('Tu portafolio está completo. Lo que viene.', [
  ['SESIÓN 12', 'Responsive', 'Media queries y el Taller TA2.'],
  ['SESIÓN 13', 'Bootstrap', 'Introducción y su sistema de grillas.'],
  ['SESIÓN 14', 'Bootstrap', 'Componentes, utilidades y tema.', true],
  ['SESIÓN 15', 'Proyecto', 'El proyecto integrador.'],
  ['SESIÓN 16', 'Examen', 'Examen final (30 %).'],
], 'Para la sesión 15: trae tu portafolio publicado y tu Figma completo. Es el proyecto integrador: junta todo lo del curso antes del examen final.');

require('fs').mkdirSync(path.dirname(out), { recursive: true });
d.save(out).then((n) => console.log('ok', n, 'diapositivas →', out));
