// Sesión 16 · Examen final: evaluación integradora (sesiones 1 a 16)
const path = require('path');
const { Deck, C, MONO } = require('./uss.js');
const { place } = require('./fit.js');
const IMG = (f) => path.join(__dirname, 'img', f);
const out = process.argv[2] || path.join(__dirname, 'out', 'Sesion16-Examen-Final-Evaluacion-Integradora.pptx');

const d = new Deck({ title: 'Sesión 16 · Examen final: evaluación integradora' });

// filas de tres columnas: [a, b, c, relleno]
const tres = (s, filas, o = {}) => {
  const y0 = o.y || 3.1; const h = o.h || 0.5; const gap = o.gap != null ? o.gap : 0.07; const w = o.w || [3.4, 3.6, 4.35];
  if (o.heads) o.heads.forEach((t, k) => d.text(s, t, { x: 0.95 + w.slice(0, k).reduce((a, b) => a + b, 0), y: y0 - 0.27, w: w[k], h: 0.24, size: 9.5, bold: true, color: C.sub }));
  filas.forEach((f, i) => {
    const y = y0 + i * (h + gap);
    d.card(s, 0.7, y, 11.95, h, { fill: f[3] || C.white });
    let x = 0.95;
    f.slice(0, 3).forEach((t, k) => {
      d.text(s, t, { x, y, w: w[k] - 0.15, h, size: o.size || 11.5, bold: k === 0 || (k === 2 && o.boldLast), color: k === 0 ? C.ink : (k === 1 ? (o.mono ? C.teal : C.body) : (o.boldLast ? C.teal : C.body)), font: k === 1 && o.mono ? MONO : undefined, codeColor: C.ink });
      x += w[k];
    });
  });
};

d.waiting('16', 'Ten a mano tu usuario y tu contraseña del Aula Virtual. Hoy es el examen final.');
d.title({
  titulo: 'Examen final: evaluación integradora',
  sesion: '16',
  sub: 'Sesiones 1 a 16 · Parte A: cuestionario · Parte B: caso práctico · 30 % del promedio',
  code: '<section class="examen">\n  <h1>Examen final</h1>\n  <p>Sesiones 1 a 16</p>\n</section>',
});
d.imageSlide('como-te-sientes.jpg', '¿Cómo te sientes hoy?');

d.add('CONCEPTUAL', (s) => {
  d.header(s, 'El curso', 'Todo lo que recorriste', 'Dieciséis sesiones, dos talleres y un portafolio publicado.');
  d.numCards(s, [
    { t: 'HTML5', d: 'Sesiones 01 a 07: estructura semántica, enlaces, imágenes, tablas, formularios, video y audio.' },
    { t: 'CSS3', d: 'Sesiones 08 a 12: selectores, variables, caja, Flexbox, Grid, transiciones y diseño responsivo.' },
    { t: 'Bootstrap y publicación', d: 'Sesiones 13 a 15: grilla, componentes, tema, pruebas y despliegue en Netlify.' },
    { t: 'Figma', d: 'Del Paso 1 al 14 del manual: Disposición automática, componentes, móvil y variables.' },
    { t: 'TA1 y TA2', d: 'Sesión 06: un sitio en HTML y Figma. Sesión 12: CSS3 y diseño responsivo.' },
    { t: 'Proyecto integrador', d: 'Sesión 15: tu portafolio completo, probado y publicado.' },
  ]);
});

d.agenda([
  ['01', 'Indicaciones', 'Cómo es el examen y sus normas.', 15],
  ['02', 'Repaso relámpago', 'HTML5, CSS3, Bootstrap y publicación.', 20],
  ['03', 'Parte A · Cuestionario', '20 preguntas en el Aula Virtual.', 40],
  ['—', 'Pausa', '', 10],
  ['04', 'Parte B · Caso práctico', 'La página Semana de la Informática 2026.', 80],
  ['05', 'Cierre del curso', 'Tu promedio y lo que viene.', 15],
], 'Cómo se reparte la sesión');

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Indicaciones', 'Cómo es el examen', 'Individual, en el Aula Virtual USS, jueves 05/11/2026. Vale el 30 % de tu promedio final.');
  d.twoCards(s, { t: 'Parte A · Cuestionario · 10 puntos', color: C.teal, items: ['20 preguntas de opción múltiple de las sesiones 1 a 16.', '0.5 puntos cada una.', '40 minutos y un solo intento.', 'Las preguntas y las opciones salen en orden aleatorio.'] },
    { t: 'Parte B · Caso práctico · 10 puntos', color: C.teal, items: ['Una página según su ficha técnica.', 'HTML semántico, CSS externo y diseño adaptable.', '80 minutos.', 'Se entrega `apellido-nombre-ef.zip` en el Aula Virtual.'] }, { h: 2.3 });
  d.callout(s, 5.4, 0.95, 'Para aprobar el curso:', 'promedio final de 11 o más y una asistencia mínima del 80 %.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '01 · Indicaciones', 'Las normas', 'Léelas antes de empezar. Valen para las dos partes.');
  d.numCards(s, [
    { t: 'Individual', d: 'No se permite comunicarse con otras personas durante el examen.' },
    { t: 'A tiempo', d: 'Cada parte se cierra a la hora indicada, aunque no hayas terminado.' },
    { t: 'Puedes consultar', d: 'Tu portafolio, las guías del curso, MDN y getbootstrap.com.' },
    { t: 'Si se corta', d: 'Vuelve a entrar de inmediato: el cuestionario guarda tus respuestas. Avisa al docente.' },
    { t: 'Originalidad', d: 'Los trabajos iguales entre sí o hechos por terceros se califican con cero.' },
    { t: 'Entrega', d: 'Revisa que el `.zip` tenga `index.html` en su raíz antes de subirlo.' },
  ]);
});

// ================= REPASO
d.divider('CONCEPTUAL', 'Repaso relámpago', '02', ['HTML5', 'CSS3 y diseño responsivo', 'Bootstrap y publicación']);

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Repaso', 'HTML5 en una diapositiva', 'La estructura que escribes al empezar la Parte B.');
  d.code(s, 0.7, 2.86, 6.9, 3.86, '<!doctype html>\n<html lang="es">\n<head>\n  <meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width,\n        initial-scale=1.0" />\n  <title>Semana de la Informática 2026</title>\n  <link rel="stylesheet" href="assets/css/estilos.css" />\n</head>\n<body>\n  <header> … <nav> … </nav> </header>\n  <main> <section> … </section> </main>\n  <footer> … </footer>\n</body>\n</html>', { size: 9.5 });
  d.steps(s, [['h1', 'Uno solo por página.'], ['alt', 'En cada imagen.'], ['label', 'for igual al id.'], ['name', 'Sin name no se envía.'], ['required', 'Campo obligatorio.'], ['Validar', 'validator.w3.org']], { tw: 1.1 });
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Repaso', 'CSS3: de Figma al código', 'Las equivalencias que más preguntas responden.');
  d.mapRows(s, [
    ['Flujo vertical', 'display: flex; flex-direction: column;'],
    ['Espacio 24 · Espacio Auto', 'gap: 24px; · justify-content: space-between;'],
    ['Espaciado 80 y 100', 'padding: 100px 80px;'],
    ['Tres columnas iguales', 'grid-template-columns: repeat(3, 1fr);'],
    ['Hover suave', 'transition: background-color 0.2s ease;'],
    ['En el celular', '@media (max-width: 600px) { … }'],
  ], { heads: ['En Figma o en el diseño', 'En CSS'], csize: 11.5 });
  d.note(s, 6.75, 'Especificidad: id > clase > etiqueta. Si empatan, gana la regla escrita después.');
});

d.add('CONCEPTUAL', (s) => {
  d.header(s, '02 · Repaso', 'Bootstrap y publicación', 'Lo esencial de las sesiones 13 a 15.');
  tres(s, [
    ['La grilla', 'container › row › col-12 col-md-6 col-lg-4', '1, 2 y 3 por fila; g-4 es un medianil de 24px'],
    ['Utilidades', 'mb-3 · p-4 · d-flex · text-center', 'Una propiedad por clase; usan !important'],
    ['Componentes', 'card · alert · accordion · modal · navbar', 'El JavaScript va al final del body'],
    ['Abrir y cerrar', 'data-bs-toggle · data-bs-target="#id"', 'El # apunta a un id'],
    ['El <head>', '<title> · description · rel="icon" · og:', 'Uno distinto por página'],
    ['Netlify', 'index.html en la raíz · 404 con / · data-netlify', 'Distingue mayúsculas'],
  ], { heads: ['Tema', 'Clave', 'Recuerda'], w: [2.3, 5.0, 4.65], h: 0.5, mono: true });
});

// ================= PARTE A
d.divider('INSTRUMENTAL', 'Parte A · Cuestionario', '03', ['20 preguntas, 0.5 puntos cada una', '40 minutos', 'Un solo intento']);

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '03 · Parte A', 'Paso a paso en el Aula Virtual', 'Lee cada pregunta completa antes de responder. No hay puntos en contra.');
  d.numCards(s, [
    { t: 'Entra', d: 'Aula Virtual USS › Diseño Web › **Examen final · Parte A**.' },
    { t: 'Comienza', d: 'Pulsa **Comenzar**. El tiempo corre desde ese momento.' },
    { t: 'Responde', d: 'Una opción por pregunta. Si dudas, márcala y vuelve al final.' },
    { t: 'Revisa', d: 'En el resumen, comprueba que no quede ninguna sin responder.' },
    { t: 'Envía', d: '**Enviar todo y terminar**. Confirma el envío.' },
    { t: 'Sigue', d: 'Al terminar, espera la indicación para empezar la Parte B.' },
  ]);
  d.note(s, 6.62, 'Los nombres de los botones pueden cambiar un poco según la versión del Aula Virtual.');
});

d.breakSlide('Al volver empieza la Parte B: ten lista una carpeta vacía para tu trabajo.', 'PAUSA · 10 MINUTOS');

// ================= PARTE B
d.divider('INSTRUMENTAL', 'Parte B · Caso práctico', '04', ['La página y su ficha técnica', 'Lo que se califica', 'La entrega']);

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '04 · Parte B', 'Semana de la Informática 2026', 'Una página de una sola vista. Los textos, los colores y las medidas están en la ficha técnica.');
  place(d, s, IMG('s16-parte-b-1440.png'), 0.7, 2.86, 8.6, 3.9, { align: 'left', valign: 'top' });
  const H = 3.9; const w = (H - 0.16) * (390 / 844) + 0.16;
  d.image(s, IMG('s16-parte-b-390.png'), 12.65 - w, 2.86, w, H, { alt: 'La página del caso práctico en un celular' });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '04 · Parte B', 'Lo que se califica', 'Cinco criterios de 2 puntos: logrado (2), en proceso (1) o no logrado (0).');
  tres(s, [
    ['Estructura semántica', 'header, nav, main, section, article y footer; un solo h1; sin errores en el validador', '2'],
    ['Estilos y variables', 'CSS externo, los valores de la ficha como variables en :root, las dos fuentes', '2'],
    ['Maquetación', 'Cabecera con Flexbox; charlas con grid o con la grilla de Bootstrap', '2'],
    ['Diseño adaptable', 'viewport y una media query: charlas en una columna, sin barra horizontal a 390px', '2'],
    ['Interacción y formulario', 'Hover con transition; campos con label, name y required; type="email"', '2'],
    ['Total de la Parte B', '', '10', 'E6F8FA'],
  ], { heads: ['Criterio', 'Logrado', 'Puntos'], w: [3.0, 8.0, 0.95], h: 0.5, boldLast: true });
});

d.add('INSTRUMENTAL', (s) => {
  d.header(s, '04 · Parte B', 'Cómo repartir los 80 minutos', 'Deja los últimos 5 minutos solo para comprimir y subir.');
  tres(s, [
    ['0 a 10', 'La carpeta e index.html con toda la estructura y los textos', 'Estructura'],
    ['10 a 40', 'Variables, reset, cabecera, presentación, botón y charlas', 'Estilos y maquetación'],
    ['40 a 55', 'El formulario y el pie', 'Formulario'],
    ['55 a 65', 'La media query del celular; prueba a 390px con F12', 'Adaptable'],
    ['65 a 75', 'Valida el HTML y el CSS en el W3C y corrige', 'Sin errores'],
    ['75 a 80', 'Comprime apellido-nombre-ef y súbela al Aula Virtual', 'Entrega', 'E6F8FA'],
  ], { heads: ['Minutos', 'Qué haces', 'Criterio'], w: [1.6, 7.3, 3.05], h: 0.5 });
});

// ================= CIERRE
d.imageSlide('cinfo-06-orientador.jpg', 'Orientador: conclusión del curso');

d.add('ORIENTADOR', (s) => {
  d.header(s, '05 · Cierre', 'Cómo se calcula tu promedio final', 'Cada nota va de 0 a 20.');
  tres(s, [
    ['Participación en aula [PA]', 'Tus intervenciones en cada clase', '40 %'],
    ['Taller online 1 [TA1]', 'Sesión 06 · 01/10', '15 %'],
    ['Taller online 2 [TA2]', 'Sesión 12 · 22/10', '15 %'],
    ['Examen final [EF]', 'Sesión 16 · 05/11', '30 %', 'E6F8FA'],
  ], { w: [3.6, 6.4, 1.95], h: 0.5, boldLast: true });
  d.callout(s, 5.35, 1.3, 'Un ejemplo:', 'PA 16, TA1 14, TA2 15 y EF 13 dan `0.40 × 16 + 0.15 × 14 + 0.15 × 15 + 0.30 × 13 = 14.65`. Para aprobar: 11 o más y al menos el 80 % de asistencia.');
});

d.resumen([
  'Escribes una página con HTML5 semántico que pasa el validador.',
  'Diseñas en Figma con Disposición automática, componentes y variables.',
  'Traduces un diseño a CSS con variables, Flexbox y Grid.',
  'Animas con transiciones, transformaciones y `@keyframes`.',
  'Adaptas un sitio al celular con media queries y medidas fluidas.',
  'Armas páginas con la grilla y los componentes de Bootstrap.',
  'Pruebas un sitio con el teclado, los validadores y Lighthouse.',
  'Publicas en Netlify, con una 404 y un formulario que guarda mensajes.',
]);
d.hacia('El curso termina. Tu portafolio sigue.', [
  ['SESIÓN 15', 'Proyecto', 'Pruebas y despliegue.'],
  ['SESIÓN 16', 'Examen', 'Evaluación integradora.', true],
  ['DESPUÉS', 'JavaScript', 'El comportamiento de tu sitio.'],
  ['SIEMPRE', 'Tu portafolio', 'Publicado y al día.'],
], '¡Gracias por este ciclo! Tu portafolio ya está publicado: compártelo en tu CV y en LinkedIn, y súmale cada proyecto nuevo.');

require('fs').mkdirSync(path.dirname(out), { recursive: true });
d.save(out).then((n) => console.log('ok', n, 'diapositivas →', out));
