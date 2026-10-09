# -*- coding: utf-8 -*-
"""Guía de código · Sesión 09: CSS3, selectores, cascada y propiedades básicas."""
import os
import sys
from guia import Doc, css_bloques, html_entre

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
P = os.path.join(REPO, 'SESION 09', 'mi-portafolio-dagner')
CSS = os.path.join(P, 'assets', 'css')
G = css_bloques(os.path.join(CSS, 'global.css'))
H = css_bloques(os.path.join(CSS, 'header.css'))
C = css_bloques(os.path.join(CSS, 'contenido.css'))

d = Doc('Guía paso a paso: tu primer CSS con los colores, la tipografía y los bordes de Figma',
        'Guía paso a paso · Sesión 09: tu primer CSS',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 09',
        'Los primeros estilos del portafolio: selectores, cascada y propiedades básicas, sacados de tu diseño de Figma.')

d.callout('Hoy recuperamos la sesión 08.',
          'El jueves 8 de octubre fue feriado y la sesión 08 no se dictó. Esta guía junta lo que tocaba ese día '
          '(sintaxis, selectores, unidades y cascada) con lo que tocaba hoy (color, tipografía, fondos y bordes). '
          'El Hero Section, que era la tarea de la sesión 08, pasa a la sesión 10: allí aprenderás Flexbox, '
          'la herramienta con la que se construye.')

d.h3('Qué vas a hacer')
d.p('Tu portafolio ya tiene la estructura HTML de sus cuatro páginas (`index.html`, `sobre-mi.html`, '
    '`mis-proyectos.html` y `contactame.html`). Hoy escribes sus primeros estilos en tres archivos dentro de '
    '`assets/css/`: los tokens de Figma, la cabecera y el pie comunes, y la base de las páginas interiores con '
    'su color, su tipografía, sus fondos y sus bordes. Además completas la tabla que quedó pendiente de la sesión 05.')
d.tabla(['Archivo', 'Qué contiene al final', 'Capas en Figma', 'Se enlaza en'], [
    ['global.css', 'Tokens de diseño (`:root`), fuentes Outfit, Geist y Geist Mono, reset y estilos base', 'Colores, fuentes y radios de todo el diseño', 'Las cuatro páginas'],
    ['header.css', 'Cabecera con logotipo, menú y botón; pie de página común', '`Header` y `footer-wrapper`', 'Las cuatro páginas'],
    ['contenido.css', 'Tipografía, tarjetas, formulario, multimedia y tabla de las páginas interiores', '`about-section`, `projects-section` y `contact-section`', 'Las tres interiores'],
    ['mis-proyectos.html', 'La tabla de herramientas (pendiente de la sesión 05)', '—', '—'],
], anchos=['17%', '38%', '27%', '18%'])

d.h3('Cómo se reparte')
d.tabla(['Momento', 'Pasos', 'Qué practicas'], [
    ['En clase, juntos', '0 al 3', 'Enlazar hojas de estilo, variables, reset, selectores de tipo, agrupados, de atributo, de hijo y pseudo-clases'],
    ['En clase, tú', '4 y 5', 'Tipografía, color y bordes de las páginas interiores; unidades `rem`, `em` y `%`; la cascada en DevTools'],
    ['Tarea', '6 y 7', 'La tabla de la sesión 05 con bordes y fondos; validar y publicar'],
    ['En Figma', 'Guía de Figma', 'Pasos 10 y 11 del manual: Sobre mí y Proyectos. Lo que no termines en clase queda como tarea'],
], anchos=['18%', '14%', '68%'])

d.h3('Material del paquete')
d.lista(['**mi-portafolio-dagner/:** la carpeta resuelta, para comparar cuando termines.',
         '**Guía de Figma · Sesión 09:** los Pasos 10 y 11 del manual, clic por clic.',
         '**Tu archivo de Figma:** con la cabecera y el Hero terminados (Pasos 1 al 9). De ahí salen las medidas del CSS.',
         '**Esta guía:** cada paso indica qué archivo crear, qué código escribir y cómo comprobarlo.'])
d.callout('Regla de oro del curso:', 'organiza siempre tus estilos en archivos según su función. No coloques todo el '
          'código en un único archivo gigante ni uses atributos `style="..."` dentro de las etiquetas HTML.')

d.h2('Antes de escribir: de Figma a CSS')
d.p('Todo el CSS de esta guía sale de tu archivo de Figma. Selecciona una capa, mira el panel derecho de arriba abajo '
    'y traduce cada control con esta tabla. Hoy usas las filas de color, tipografía, fondos y bordes; las de '
    'Disposición automática llegan con Flexbox en la sesión 10.')
d.tabla(['En Figma', 'En CSS', 'Ejemplo del portafolio'], [
    ['Relleno de un marco', '`background-color`', '`background-color: var(--color-surface);`'],
    ['Relleno de un texto', '`color`', '`color: var(--color-text-primary);`'],
    ['Relleno de tipo Imagen', '`background-image` o una etiqueta `<img>`', 'Las imágenes de proyecto (sesión 10)'],
    ['Trazo: color y Peso', '`border`', '`border: 1px solid var(--color-border);`'],
    ['Trazo en un solo lado', '`border-bottom`, `border-top`', 'La línea inferior de la cabecera'],
    ['Radio de esquina', '`border-radius`', '`border-radius: var(--radius-md);`'],
    ['Tipografía: fuente', '`font-family`', '`font-family: var(--font-heading);`'],
    ['Tipografía: grosor de letra', '`font-weight`', 'Regular 400 · Medium 500 · SemiBold 600 · Bold 700 · ExtraBold 800'],
    ['Tipografía: tamaño', '`font-size`', '`font-size: 2.25rem;` (36 ÷ 16)'],
    ['Altura de la línea 160 %', '`line-height`', '`line-height: 1.6;`'],
    ['Espaciado (relleno interno)', '`padding`', '`padding: 1.5rem;` en las tarjetas'],
    ['Espacio entre elementos', '`margin` hoy; `gap` en la sesión 10', '`margin-bottom: 3rem;` entre secciones'],
], anchos=['30%', '30%', '40%'])
d.callout('Si no coinciden, manda Figma:', 'cuando una medida de tu CSS no sea igual a la de tu diseño, corrige el CSS. '
          'Y si tu Figma todavía tiene los fallos de la hoja de correcciones (cabecera de 160, menú de 1369 px), '
          'corrígelo antes de empezar.')
d.callout('Flexbox, por ahora de memoria:', '`display: flex`, `gap`, `align-items` y `justify-content` aparecen en la '
          'cabecera y en el menú. Hoy los escribes tal como están, sabiendo de qué control de Figma sale cada uno; '
          'el jueves, en la sesión 10, los estudias a fondo.')

d.h2('Paso 0 · Prepara la carpeta de estilos')
d.p('En el explorador de VS Code, dentro de tu carpeta `assets/`, crea una subcarpeta llamada `css/` y, dentro, tres archivos vacíos:')
d.code('''mi-portafolio-dagner/
├── assets/
│   ├── css/                    ← subcarpeta nueva para tus hojas de estilo
│   │   ├── global.css
│   │   ├── header.css
│   │   └── contenido.css
│   ├── img/
│   ├── js/
│   └── media/
├── index.html
├── sobre-mi.html
├── mis-proyectos.html
└── contactame.html''')
d.p('El cuarto archivo, `index.css`, llega en la sesión 10 junto con el Hero Section.')

d.h2('Paso 1 · Enlaza los estilos en el <head>')
d.p('Enlaza primero y escribe después: así ves cada cambio en el navegador en cuanto guardas. En el `<head>` de '
    '`index.html`, debajo de la etiqueta `<meta name="description">`, añade:')
d.code(html_entre(os.path.join(P, 'index.html'), '<!-- 1. Tokens y Reset Global -->', 'href="assets/css/header.css" />'))
d.p('En `sobre-mi.html`, `mis-proyectos.html` y `contactame.html` van esos dos y uno más, la base de las páginas interiores:')
d.code(html_entre(os.path.join(P, 'mis-proyectos.html'), '<!-- 1. Tokens y Reset Global -->', 'href="assets/css/contenido.css" />'))
d.callout('El orden importa por la cascada:', '`global.css` va primero porque define las variables y las fuentes. '
          'Luego se cargan los componentes comunes y, al final, la hoja propia de la página. Cuando dos reglas con la '
          'misma fuerza chocan, gana la del archivo enlazado más abajo: por eso lo particular va al final.')

d.h2('Paso 2 · Variables de diseño y estilos base (assets/css/global.css)')
d.h3('2.1 · Importa las tipografías de Google Fonts')
d.code(G['1'])
d.p('`@import` tiene que ser la primera línea del archivo. Si lo pones más abajo, el navegador lo ignora y la página '
    'se ve con una fuente cualquiera.')
d.h3('2.2 · Declara los tokens de Figma como variables en :root')
d.p('Un token es un valor que se repite en todo el diseño. En Figma los encuentras en las secciones **Relleno** '
    '(colores), **Tipografía** (fuentes) y **Radio de esquina** de cualquier capa: el `#06B6C4` del botón azul, '
    'el `#E5E7EB` de todos los trazos, el radio 8 de los botones y el 12 de las tarjetas.')
d.code(G['2'])
d.callout('Por qué usar variables:', 'si mañana cambia el color de la marca, editas `--color-primary` en una sola línea '
          'y todo el sitio se actualiza. Se usan así: `color: var(--color-primary);`')
d.h3('2.3 · Reset universal y estilos base')
d.p('Al final de `global.css`, añade las reglas que quitan los márgenes del navegador y aplican la tipografía a toda la web:')
d.code(G['3'] + '\n\n' + G['4'] + '\n\n' + G['5'] + '\n\n' + G['6'] + '\n\n' + G['7'])
d.callout('Color y tipografía en una sola regla:', '`body` define el color del texto, la fuente, el tamaño y la altura '
          'de línea. Como esas propiedades se heredan, bajan solas a todos los párrafos de la página.')
d.h3('2.4 · El contorno del teclado y la fuente del código')
d.code(G['8'] + '\n\n' + G['9'])
d.p('**`outline` no es `border`:** el contorno se dibuja por fuera de la caja y no cambia su tamaño. Navega tu página '
    'con la tecla Tab: el enlace activo queda rodeado por el azul de Figma.')
d.tabla(['Selector', 'Tipo', 'A quién apunta'], [
    ['`:root`', 'Pseudo-clase', 'La raíz del documento. Las variables declaradas ahí se heredan en toda la página'],
    ['`*`', 'Universal', 'Todas las etiquetas'],
    ['`*::before, *::after`', 'Pseudo-elemento', 'El contenido que el CSS genera antes o después de cada etiqueta'],
    ['`body`', 'De tipo', 'La etiqueta `<body>`. Su color y su fuente bajan por herencia a todo el texto'],
    ['`h1, h2, h3, h4`', 'Agrupado', 'Varios selectores con las mismas declaraciones, separados por coma'],
    ['`:focus-visible`', 'Pseudo-clase', 'El elemento que tiene el foco cuando navegas con el teclado'],
], anchos=['26%', '18%', '56%'])
d.p('Fíjate en `a { color: inherit; }` y en `pre, code`: los enlaces, los botones y el código traen estilos propios del '
    'navegador (el azul de los enlaces, la letra Courier del código) y una regla directa siempre gana a lo heredado. '
    'Por eso hay que pedirles que usen los nuestros.')
d.comprueba('el fondo de tu página adopta el tono suave `#F9FAFB`, los textos se muestran con la familia Geist y '
            'ya no hay márgenes exteriores ni viñetas en las listas.')

d.h2('Paso 3 · Estilos de la cabecera y el pie (assets/css/header.css)')
d.p('Cabecera y pie son iguales en las cuatro páginas, así que viven en un archivo común. Cada bloque usa un tipo de selector distinto.')
d.h4('En Figma: las medidas de la cabecera y del pie')
d.tabla(['Capa (paso del manual)', 'En Figma', 'En header.css'], [
    ['`Header` (Paso 2)', 'Altura fija 80; Relleno `#FFFFFF`; Trazo inferior `#E5E7EB`; Espacio Auto; Espaciado 0 · 80 · 0 · 80',
     '`height: 80px;` · `background-color` · `border-bottom` · `justify-content: space-between;` · `padding: 0 80px;`'],
    ['Texto Dagner Chuman (Paso 3)', 'Outfit Bold 18, `#0B0F19`', '`font-size: 18px;` · `font-weight: 700;`'],
    ['`nav-links` (Paso 4)', 'Espacio 32; textos Geist Medium 14, `#9CA3AF`', '`gap: 32px;` · `font-size: 14px;` · `font-weight: 500;`'],
    ['`btn-header` (Paso 5)', 'Espaciado 14 y 24; Radio 8; Trazo `#374151`; texto Geist Medium 15',
     '`padding: 14px 24px;` · `border-radius: var(--radius-sm);` · `border: 1px solid …`'],
    ['`footer-wrapper` (Paso 13)', 'Espaciado 48 y 80; Espacio 24; Trazo superior `#E5E7EB`; texto Geist Regular 13',
     '`padding: 48px 80px;` · `margin-bottom: 24px;` · `border-top` · `font-size: 13px;`'],
], anchos=['24%', '38%', '38%'])
d.h3('3.1 · Barra superior y logotipo')
d.code(H['1'] + '\n\n' + H['2'])
d.callout('Dos propiedades nuevas:', '`position: sticky; top: 0;` deja la barra pegada arriba cuando haces scroll, y '
          '`z-index: 100` la pone por encima del contenido que pasa por debajo. Las tres líneas de `display: flex` '
          'colocan logotipo, menú y botón en una fila: es el anticipo de la sesión 10.')
d.h3('3.2 · Menú de navegación horizontal')
d.code(H['3'])
d.h3('3.3 · Botón de contacto y pie de página')
d.code(H['4'] + '\n\n' + H['5'])
d.callout('Detalle de diseño:', 'el selector `header > a[href="contactame.html"]` apunta solo al botón de la derecha, '
          'sin afectar al enlace «Contacto» del menú. El signo `>` significa «hijo directo» y los corchetes, «que '
          'tenga este atributo con este valor».')
d.tabla(['Selector', 'Cómo se lee'], [
    ['`header`', 'De tipo: la etiqueta `<header>`'],
    ['`header h1 a`', 'Descendiente: el enlace que está dentro del `h1` que está dentro de `header`'],
    ['`nav[aria-label="Navegacion principal"] a`', 'De atributo + descendiente: los enlaces del menú principal, no los del pie'],
    ['`… a:hover`', 'Pseudo-clase: el mismo enlace, mientras el cursor está encima'],
    ['`header > a[href="contactame.html"]`', 'Hijo directo + atributo: solo el botón de la cabecera'],
    ['`footer nav ul`', 'Descendiente: la lista del menú del pie'],
], anchos=['44%', '56%'])
d.h3('3.4 · Cabecera y pie en pantallas estrechas')
d.p('Sin este bloque, el menú se desborda en un celular. Las media queries son tema de la sesión 12: por ahora cópialo tal cual al final de `header.css`.')
d.code(H['6'])
d.comprueba('en las cuatro páginas la cabecera muestra el logotipo a la izquierda, el menú al centro y el botón con '
            'borde a la derecha. Al pasar el cursor, los enlaces del menú se oscurecen y el botón se rellena.')

d.h2('Paso 4 · Tipografía, color y bordes de las páginas interiores (assets/css/contenido.css)')
d.p('Después del reset, Sobre mí, Proyectos y Contacto quedaron pegadas al borde y sin separación. Este archivo les da '
    'una base de lectura con las propiedades de hoy: tipografía, color, fondos y bordes, medidas en `px`, `rem`, `em` y `%`.')
d.callout('Diseño de una página, sitio de cuatro:', 'tu Figma es una sola página larga de 1440 px con las secciones a dos '
          'columnas; tu sitio tiene cuatro páginas. Por ahora las páginas interiores usan una columna de lectura de 800 px '
          'con los mismos tamaños de texto, tarjetas y espaciados del diseño. Las dos columnas llegan con Flexbox y Grid en la sesión 10.')
d.tabla(['En Figma (Pasos 10 al 12 del manual)', 'En contenido.css'], [
    ['Secciones: Espaciado superior e inferior 100', '`padding: 6.25rem 1.5rem;` en `main` (100 ÷ 16 = 6.25)'],
    ['Secciones: Espacio 48', '`margin-bottom: 3rem;` en `main section`'],
    ['Título de sección: Outfit ExtraBold 36', '`font-size: 2.25rem;` · `font-weight: 800;`'],
    ['Título secundario: 22', '`font-size: 1.375rem;` en `aside h2`'],
    ['Título de tarjeta: Outfit Bold 24', '`font-size: 1.5rem;` en `main h3`'],
    ['Tarjetas: Relleno `#FFFFFF`, Trazo `#E5E7EB`, Radio 12, Espaciado 24',
     '`background-color` · `border` · `border-radius: var(--radius-md);` · `padding: 1.5rem;`'],
], anchos=['46%', '54%'])
d.h3('4.1 · Caja de lectura, títulos y enlaces')
d.code(C['1'] + '\n\n' + C['2'] + '\n\n' + C['3'] + '\n\n' + C['4'])
d.tabla(['Unidad', 'Se calcula a partir de', 'En este archivo'], [
    ['`px`', 'Nada: es una medida fija', '`max-width: 800px;` · `text-underline-offset: 3px;`'],
    ['`rem`', 'El tamaño de letra de la raíz: 16 px', '`2.25rem` son 36 px; `6.25rem`, 100 px'],
    ['`em`', 'El tamaño de letra de la propia etiqueta', '`letter-spacing: -0.01em;` acerca las letras un 1 % de su tamaño'],
    ['`%`', 'La medida del contenedor', '`max-width: 100%;` en imágenes y videos'],
], anchos=['12%', '40%', '48%'])
d.p('Los enlaces del contenido recuperan el subrayado, ahora con el color de la marca: `text-decoration-color` pinta '
    'solo la línea y `text-underline-offset` la separa del texto.')
d.h3('4.2 · Tarjetas con borde y radio')
d.code(C['5'])
d.callout('Cascada en un mismo archivo:', '`main h2` y `aside h2` tienen la misma especificidad (dos etiquetas). El título '
          '«En resumen» cumple las dos reglas y gana `aside h2` porque está escrita más abajo.')
d.h3('4.3 · Listas, multimedia y la foto de perfil')
d.code(C['6'] + '\n\n' + C['7'])
d.p('Para que la regla `.foto-perfil` se aplique, añade la clase a la imagen de `sobre-mi.html`:')
d.code(html_entre(os.path.join(P, 'sobre-mi.html'), '<img\n            class="foto-perfil"', 'loading="lazy"\n          />'))
d.p('**`border-radius: 50%`** redondea cada esquina la mitad del lado: una caja cuadrada se vuelve un círculo. Si tu foto no es '
    'cuadrada, el resultado es un óvalo.')
d.h3('4.4 · Botones y formulario')
d.code(C['8'] + '\n\n' + C['9'])
d.tabla(['Selector o valor', 'Qué hace'], [
    ['`button[type="submit"]`', 'De atributo: solo el botón que envía; el de limpiar conserva el estilo base'],
    ['`rgba(6, 182, 196, 0.35)`', 'El azul `#06B6C4` escrito en rojo, verde y azul, con 35 % de opacidad: una sombra suave del mismo color'],
    ['`input:focus`', 'Pseudo-clase: el campo en el que está el cursor en ese momento'],
    ['`input[type="checkbox"]`', 'De atributo: la casilla, para que no ocupe todo el ancho como los demás campos'],
    ['`accent-color`', 'Pinta los controles nativos (casilla y barra de avance) con el color que le des'],
], anchos=['34%', '66%'])
d.callout('Herencia, con una excepción:', 'los botones y los campos de formulario no heredan la letra de la página: el '
          'navegador les pone la suya. `font: inherit` les pide que usen la del resto del sitio.')
d.h3('4.5 · El video y la transcripción')
d.code(C['10'] + '\n\n' + C['11'])
d.comprueba('en Sobre mí, el texto ocupa una columna centrada de 800 px como máximo, la foto es un círculo con borde azul '
            'y «En resumen» es una tarjeta blanca con borde. En Contacto, los campos ocupan todo el ancho de su tarjeta '
            'y el botón «Enviar mensaje» es azul.')
d.h3('Reto opcional · Fondos con imagen y degradado')
d.p('Tu diseño de Figma usa fondos planos, pero `background` sabe hacer más. Pruébalo en DevTools, sin tocar tus archivos: '
    'inspecciona `<body>`, y en la pestaña **Styles** añade estas declaraciones una por una.')
d.code('''background-image: linear-gradient(180deg, #FFFFFF 0%, var(--color-bg) 600px);
background-image: url("assets/img/poster-presentacion.jpg");
background-size: cover;          /* la imagen cubre toda la caja */
background-position: center;     /* y se centra */
background-repeat: no-repeat;    /* sin repetirse en mosaico */''')
d.p('Al recargar la página, todo vuelve a su estado. Si alguna vez usas una imagen de fondo con texto encima, '
    'comprueba que el texto se siga leyendo.')

d.h2('Paso 5 · Comprueba la cascada en DevTools')
d.p('Abre `contactame.html`, haz clic derecho sobre el correo y elige **Inspeccionar**. En la pestaña **Styles** verás '
    'las reglas que afectan a ese enlace, ordenadas de mayor a menor prioridad:')
d.code('''main a {                                   contenido.css
  color: var(--color-text-primary);
  text-decoration: underline;
  …
}
a {                                        global.css
  text-decoration: none;          ← tachada: perdió
  color: inherit;                 ← tachada: perdió
}''')
d.lista(['**Por qué gana `main a`:** tiene dos etiquetas en el selector (especificidad 0-0-2) y `a` solo una (0-0-1).',
         'Baja por el panel hasta **Inherited from body**: ahí están el color y la fuente que el enlace recibió por herencia.',
         'Abre la pestaña **Computed** sobre un título `h2`: el `2.25rem` aparece convertido a `36px`.',
         'Desmarca una casilla junto a cualquier declaración para ver la página sin ella. DevTools no cambia tus archivos: al recargar, todo vuelve.'])
d.callout('Para la tarea:', 'toma una captura de este panel con una declaración tachada y explica en una línea por qué perdió.')

d.h2('Paso 6 · La tabla pendiente de la sesión 05')
d.p('En la sesión 05 aprendiste a construir tablas accesibles; tu portafolio todavía no tenía una. Abre `mis-proyectos.html` '
    'y, dentro de `<main>`, debajo de la sección de proyectos, escribe esta sección:')
d.code(html_entre(os.path.join(P, 'mis-proyectos.html'), '<!-- SECCIÓN: Tabla de datos', '</section>'))
d.p('Repasa lo de la sesión 05: `<caption>` describe la tabla, `scope="col"` y `scope="row"` dicen a quién encabeza cada '
    '`<th>`, y `colspan="3"` une las tres celdas del pie. Ahora, al final de `contenido.css`, dale bordes, fondos y tipografía:')
d.code(C['12'])
d.tabla(['Propiedad o selector', 'Qué hace en la tabla'], [
    ['`border-collapse: collapse`', 'Une los bordes de celdas vecinas en una sola línea. Sin ella, cada celda dibuja el suyo y aparecen líneas dobles'],
    ['`border-bottom` en `th, td`', 'Una línea fina bajo cada fila, como el Trazo inferior de la cabecera en Figma'],
    ['`text-transform: uppercase`', 'Escribe los encabezados en mayúsculas sin cambiar el HTML'],
    ['`letter-spacing: 0.06em`', 'Separa las letras un 6 % de su tamaño: las mayúsculas pequeñas se leen mejor'],
    ['`tbody tr:nth-child(even)`', 'Pseudo-clase: las filas pares. Les da el fondo de la página para alternar los colores'],
    ['`caption-side: top`', 'Coloca el título de la tabla encima'],
], anchos=['34%', '66%'])
d.comprueba('en Proyectos aparece la tabla con su título, los encabezados en mayúsculas sobre un fondo gris, filas '
            'alternas y una sola línea entre fila y fila.')

d.h2('Paso 7 · Valida y publica')
d.pasos(['Valida cada página en **validator.w3.org** (pestaña *Validate by File Upload*): cero errores.',
         'Valida tus tres hojas de estilo en **jigsaw.w3.org/css-validator** (pestaña *By file upload*).',
         'Publica la carpeta en Netlify, como en las sesiones anteriores, y abre la URL en tu celular.'])
d.callout('Si el validador de CSS marca @import o las variables como advertencia:', 'es normal; lo que no puede haber son '
          'errores. Un error típico es una llave sin cerrar o un punto y coma de menos.')

d.h2('Lista de comprobación')
d.p('Revisa cada punto antes de dar por terminada la práctica:')
d.check(['La carpeta `assets/css/` contiene `global.css`, `header.css` y `contenido.css`.',
         'Las cuatro páginas enlazan `global.css` y `header.css`, en ese orden; las tres interiores, además, `contenido.css`.',
         'Todos los colores, fuentes y radios provienen de variables `var(--nombre)` declaradas en `:root`.',
         'Las medidas de la cabecera coinciden con las de tu archivo de Figma.',
         'Los títulos de sección miden 36 px (`2.25rem`) y usan Outfit ExtraBold.',
         'Las tarjetas tienen fondo blanco, borde `#E5E7EB` y radio 12.',
         'La tabla de herramientas tiene `caption`, `thead`, `tbody`, `tfoot` y una sola línea entre filas.',
         'Ninguna etiqueta lleva el atributo `style` ni hay etiquetas `<style>` en el HTML.',
         'El HTML y el CSS pasan los validadores del W3C sin errores.'])

d.h2('Errores frecuentes en esta sesión')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['No se aplica ningún estilo', 'La ruta del `<link>` está mal. Escribe `assets/css/global.css` (ruta relativa) y revisa en DevTools › Network que el archivo responda 200, no 404'],
    ['Una regla no hace nada', 'Falta un punto y coma en la línea anterior o el selector está mal escrito. Revisa también si otra regla la vence: en DevTools aparece tachada'],
    ['La fuente Outfit no se ve', 'La regla `@import` no está en la primera línea de `global.css`'],
    ['El menú principal no toma estilos', 'El valor de `aria-label` en el CSS debe coincidir letra por letra con el del HTML: `Navegacion principal`, sin tilde'],
    ['La tabla tiene líneas dobles', 'Falta `border-collapse: collapse;` en `table`'],
    ['La foto de perfil no es un círculo', 'Falta la clase `foto-perfil` en la etiqueta `<img>`, o la foto no es cuadrada'],
    ['Las páginas interiores se ven pegadas al borde', 'Falta enlazar `contenido.css` en esa página'],
], anchos=['32%', '68%'])

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Sesion09_CSS3_Selectores_Cascada_y_Propiedades.html'))
print('ok')
