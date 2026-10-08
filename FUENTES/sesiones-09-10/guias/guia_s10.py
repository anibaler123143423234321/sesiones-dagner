# -*- coding: utf-8 -*-
"""Guía de código · Sesión 10: modelo de caja, Flexbox y Grid."""
import os
import sys
from guia import Doc, css_bloques, html_entre

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
P = os.path.join(REPO, 'SESION 10', 'mi-portafolio-dagner')
CSS = os.path.join(P, 'assets', 'css')
I = css_bloques(os.path.join(CSS, 'index.css'))
H = css_bloques(os.path.join(CSS, 'header.css'))
C = css_bloques(os.path.join(CSS, 'contenido.css'))

d = Doc('Guía paso a paso: modelo de caja, Flexbox y Grid en tu portafolio',
        'Guía paso a paso · Sesión 10: modelo de caja, Flexbox y Grid',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 10',
        'Las medidas de la Disposición automática de Figma pasan a CSS: el Hero Section con Flexbox y las páginas interiores a dos columnas con Flexbox y Grid.')

d.callout('Vienes de la sesión 09:', 'necesitas `global.css`, `header.css` y `contenido.css` funcionando y enlazados. '
          'Si te falta algo, compáralo con la carpeta resuelta de la sesión 09 antes de empezar. Hoy también construyes '
          'el Hero Section, que estaba previsto para la sesión 08 (feriado).')

d.h3('Qué vas a hacer')
d.p('Hasta ahora tu CSS decía cómo se ve cada cosa: color, letra, bordes. Hoy decide dónde va. Primero miras el modelo '
    'de caja en DevTools; después construyes el Hero de la portada con Flexbox y, por último, pasas las páginas '
    'interiores a las dos columnas de tu diseño con Flexbox y Grid.')
d.tabla(['Archivo', 'Qué cambia hoy', 'Capas en Figma'], [
    ['index.html', 'El marcado del Hero dentro de `<main>` y el enlace a `index.css`', '`hero-left` y `hero-right`'],
    ['index.css (nuevo)', 'El Hero a dos columnas, los botones y la tarjeta de código', '`hero-section` (Pasos 6 al 9)'],
    ['header.css', 'El pie de página pasa a Flexbox en columna', '`footer-wrapper` (Paso 13)'],
    ['contenido.css', 'La caja de 1440; Sobre mí y Contacto a dos columnas con Flexbox; Proyectos y el formulario en rejilla con Grid',
     '`about-content`, `projects-grid`, `contact-content`'],
    ['Las tres páginas interiores', 'Clases que conectan cada bloque con su capa de Figma', '—'],
    ['assets/img/', 'Dos imágenes de proyecto de 628 × 220', '`project-image` (Paso 14)'],
], anchos=['22%', '50%', '28%'])

d.h3('Cómo se reparte')
d.tabla(['Momento', 'Pasos', 'Qué practicas'], [
    ['En clase, juntos', '0 al 3', 'El modelo de caja en DevTools; Flexbox en el Hero; el pie en columna'],
    ['En clase, tú', '4 y 5', 'Grid en Proyectos; Flexbox en Sobre mí'],
    ['Tarea', '6 y 7', 'Contacto con Flexbox y el formulario con Grid; la multimedia en rejilla; validar y publicar'],
    ['En Figma', 'Guía de Figma', 'Pasos 12 al 14 del manual: Contacto, pie de página e imágenes'],
], anchos=['18%', '14%', '68%'])

d.h3('Material del paquete')
d.lista(['**mi-portafolio-dagner/:** la carpeta resuelta. Trae las dos imágenes de proyecto en `assets/img/`.',
         '**Guía de Figma · Sesión 10:** los Pasos 12 al 14 del manual, clic por clic.',
         '**Tu archivo de Figma:** con la cabecera, el Hero, Sobre mí y Proyectos terminados (Pasos 1 al 11).',
         '**Esta guía:** cada paso indica qué archivo tocar, qué código escribir y cómo comprobarlo.'])

d.h2('Antes de escribir: la Disposición automática es Flexbox')
d.p('Cada marco de Figma con **Disposición automática** se escribe en CSS con `display: flex`. Selecciona el marco, '
    'mira el panel derecho y traduce cada control con esta tabla:')
d.tabla(['En Figma', 'En CSS', 'Ejemplo del portafolio'], [
    ['Disposición automática (Shift + A)', '`display: flex`', '`header`, `.hero-section`'],
    ['Flujo: flecha derecha o flecha abajo', '`flex-direction: row` o `column`', '`.hero-left { flex-direction: column; }`'],
    ['Espacio (separación entre hijos)', '`gap`', '`gap: 64px;` en `.hero-section`'],
    ['Espacio: Auto', '`justify-content: space-between`', '`header`, `.code-header`'],
    ['Espaciado (relleno interno)', '`padding`', '`padding: 160px 80px 100px 80px;`'],
    ['Alineación', '`align-items` (y `justify-content`)', '`align-items: center;`'],
    ['Ancho fijo · Altura fija', '`width` · `height` (en un ítem flex, `flex: 0 0 480px`)', '`.about-content aside`'],
    ['Llenar el contenedor', '`flex: 1` (o `width: 100%`)', '`.hero-left { flex: 1; }`'],
    ['Ajustar al contenido', 'No necesita propiedad', 'Los botones del Hero'],
    ['Recortar contenido', '`overflow: hidden`', '`.code-card`, `.project-card`'],
    ['Relleno de tipo Imagen, modo Llenar', '`object-fit: cover`', '`.project-image`'],
], anchos=['32%', '34%', '34%'])
d.callout('¿Y Grid?', 'en Figma, `projects-grid` es un Flujo horizontal con dos tarjetas en Llenar el contenedor. En CSS '
          'ese resultado se consigue con Flexbox o con Grid. Usamos Grid cuando las piezas forman filas y columnas '
          'que deben medir lo mismo, como una cuadrícula de tarjetas o un formulario a dos columnas.')
d.callout('Si no coinciden, manda Figma:', 'cuando una medida de tu CSS no sea igual a la de tu diseño, corrige el CSS.')

d.h2('Paso 0 · El modelo de caja en DevTools')
d.p('Toda etiqueta es una caja con cuatro capas, de adentro hacia afuera: el **contenido**, el **padding** (relleno), '
    'el **border** (borde) y el **margin** (margen). Antes de maquetar, míralo en tu página:')
d.pasos(['Abre `sobre-mi.html` en el navegador, haz clic derecho sobre el texto y elige **Inspeccionar**.',
         'En el panel de elementos, haz clic en la etiqueta `<main>`.',
         'Abre la pestaña **Computed**. Arriba está el diagrama de la caja: el contenido en el centro, el padding de 24 a los lados y 100 arriba y abajo.',
         'Pasa el cursor por cada capa del diagrama: el navegador la pinta sobre la página.'])
d.p('Ahora prueba qué hace la regla `box-sizing: border-box` que escribiste en `global.css`:')
d.pasos(['Selecciona `<main>`. En la pestaña **Styles**, busca la regla `*, *::before, *::after`.',
         'Desmarca la casilla de `box-sizing: border-box`. La caja pasa de 800 a 848 px de ancho: el padding se suma por fuera.',
         'Vuelve a marcarla. Con `border-box`, el ancho que escribes incluye el padding y el borde: 800 son 800.'])
d.tabla(['Propiedad', 'Qué hace', 'Dónde lo usas'], [
    ['`display: block`', 'La caja ocupa todo el ancho y empieza en una línea nueva. Así son `div`, `p`, `section`', '`.project-image`, `.contact-card a`'],
    ['`display: inline`', 'La caja va dentro de la línea de texto y no acepta `width`, `height` ni padding vertical. Así son `a`, `span`, `img`', 'Los enlaces del menú'],
    ['`display: inline-block`', 'Va en la línea, pero sí acepta `width` y `height`', 'Los tres círculos `.dot`'],
    ['`display: flex` · `grid`', 'La caja ordena a sus hijos en fila, en columna o en rejilla', 'Hoy, en todo el portafolio'],
    ['`margin: 0 auto`', 'Reparte el espacio sobrante a los lados: centra una caja con ancho máximo', '`main`, `.hero-section`'],
    ['`max-width`', 'La caja crece hasta ese ancho, pero puede encogerse', '`main`, `.hero-left`'],
], anchos=['24%', '48%', '28%'])

d.h2('Paso 1 · Maqueta el Hero Section en index.html')
d.p('Abre `index.html`. En el `<head>`, debajo de los dos enlaces de la sesión 09, añade la hoja propia de la portada:')
d.code(html_entre(os.path.join(P, 'index.html'), '<!-- 1. Tokens y Reset Global -->', 'href="assets/css/index.css" />'))
d.p('Dentro de la etiqueta `<main>`, escribe la sección de presentación con sus dos columnas (`hero-left` y `hero-right`):')
d.code(html_entre(os.path.join(P, 'index.html'), '<main>', '</main>'), corto=False)
d.callout('Detalle semántico:', 'cada página lleva un solo `<h1>`, y el tuyo ya está en la cabecera: es tu nombre. Por eso '
          'el título del Hero es un `<h2>`; su tamaño lo decide la clase `hero-title`, no la etiqueta. Usamos `<pre><code>` '
          'para respetar exactamente los espacios del código, y el signo & se escribe `&amp;`.')

d.h2('Paso 2 · El Hero con Flexbox (assets/css/index.css)')
d.p('Un contenedor flex tiene dos ejes. El **eje principal** sigue el Flujo: horizontal con `row`, vertical con `column`. '
    'El **eje cruzado** es el otro. `justify-content` reparte los hijos en el eje principal y `align-items` los alinea en el cruzado.')
d.tabla(['Propiedad', 'Se escribe en', 'Qué hace'], [
    ['`display: flex`', 'El contenedor', 'Sus hijos directos pasan a ser ítems flex y se colocan en fila'],
    ['`flex-direction`', 'El contenedor', '`row` (fila, por defecto) o `column` (columna)'],
    ['`gap`', 'El contenedor', 'La separación entre ítems: el Espacio de Figma'],
    ['`justify-content`', 'El contenedor', 'Reparte en el eje principal: `flex-start`, `center`, `space-between`…'],
    ['`align-items`', 'El contenedor', 'Alinea en el eje cruzado: `stretch` (por defecto), `center`, `flex-start`…'],
    ['`flex-wrap: wrap`', 'El contenedor', 'Si no caben, los ítems bajan a otra línea'],
    ['`flex: 1`', 'Un ítem', 'El ítem crece para tomar el espacio que sobra: Llenar el contenedor'],
    ['`flex: 0 0 480px`', 'Un ítem', 'No crece, no se encoge y mide 480: Ancho fijo'],
], anchos=['24%', '20%', '56%'])
d.h4('En Figma: las medidas del Hero')
d.tabla(['Capa (paso del manual)', 'En Figma', 'En index.css'], [
    ['`hero-section` (Paso 6)', 'Flujo horizontal; Espacio 64; Espaciado 160 · 80 · 100 · 80', '`display: flex;` · `gap: 64px;` · `padding: 160px 80px 100px 80px;`'],
    ['`hero-left` (Paso 7)', 'Flujo vertical; Ancho fijo 696; Espacio 32', '`flex-direction: column;` · `max-width: 696px;` · `gap: 32px;`'],
    ['Título (Paso 7)', 'Outfit ExtraBold 64, altura de línea 110 %', '`font-size: 64px;` · `font-weight: 800;` · `line-height: 1.1;`'],
    ['Botones (Paso 8)', 'Espacio 16; Espaciado 14 y 24; Radio 8; Geist SemiBold 15', '`gap: 16px;` · `padding: 14px 24px;` · `border-radius: var(--radius-sm);`'],
    ['`hero-right` (Paso 9)', 'Ancho fijo 520; Radio 12; Trazo `#E5E7EB`; Recortar contenido', '`max-width: 520px;` · `border-radius: var(--radius-md);` · `overflow: hidden;`'],
    ['Código (Paso 9)', 'Geist Mono 14, altura de línea 160 %; Espaciado 24', '`font-size: 14px;` · `line-height: 1.6;` · `padding: 24px;`'],
], anchos=['22%', '38%', '40%'])
d.callout('Dos diferencias a propósito:', 'en Figma, `hero-left` tiene Ancho fijo y `hero-right` Altura fija 404. En CSS '
          'usamos `max-width` y dejamos que el contenido decida la altura, para que el Hero pueda encogerse en pantallas pequeñas.')
d.h3('2.1 · El contenedor a dos columnas')
d.code(I['1'])
d.h3('2.2 · La columna izquierda: un flex dentro de otro')
d.code(I['2'])
d.p('`.hero-left` es a la vez un **ítem** de `.hero-section` (por eso lleva `flex: 1`) y un **contenedor** de su título, '
    'su párrafo y sus botones (por eso lleva `display: flex` y `flex-direction: column`). Es lo mismo que en Figma: un '
    'marco con Disposición automática dentro de otro.')
d.comprueba('la columna izquierda mide como máximo 696 px, y entre el título, el párrafo y los botones hay 32 px de separación.')
d.h3('2.3 · Los botones')
d.code(I['3'])
d.p('Un enlace es `inline`: ignora el padding vertical al calcular su línea. Con `display: inline-flex` se comporta como '
    'una caja y además centra su texto. Los botones no llevan ancho: miden lo que su texto más el Espaciado, como '
    '**Ajustar al contenido** en Figma.')
d.h3('2.4 · La tarjeta de código')
d.code(I['4'], corto=False)
d.p('Cuenta los contenedores flex de la tarjeta: `.hero-right` centra la tarjeta, `.code-header` separa los círculos del '
    'nombre del archivo con `space-between` (el Espacio Auto de Figma) y `.window-controls` pone los tres círculos en fila con 8 px.')
d.h3('2.5 · El Hero en pantallas estrechas')
d.p('Las media queries son tema de la sesión 12; por ahora copia este bloque al final de `index.css`. Fíjate en la idea: '
    'basta cambiar `flex-direction` a `column` para que las dos columnas se apilen.')
d.code(I['5'])
d.comprueba('el título y los botones quedan a la izquierda y la tarjeta de código a la derecha, centradas en vertical. Al '
            'estrechar la ventana, la tarjeta baja debajo del texto sin desbordar.')

d.h2('Paso 3 · El pie de página en columna (assets/css/header.css)')
d.p('En Figma, `footer-wrapper` es un marco con Flujo vertical, Alineación al centro y Espacio 24. Reemplaza el bloque 5 de `header.css`:')
d.code(H['5'])
d.p('El `gap: 24px` del pie reemplaza al `margin-bottom: 24px` que tenía el menú en la sesión 09: en un contenedor flex, la '
    'separación entre hijos la pone el padre. Y `flex-wrap: wrap` deja que los enlaces bajen de línea en un celular.')

d.h2('Paso 4 · Proyectos con Grid (mis-proyectos.html y contenido.css)')
d.h3('4.1 · La caja de 1440')
d.p('Las dos columnas no caben en la caja de lectura de 800 px. En `contenido.css`, reemplaza el bloque 1 por este, '
    'con el ancho y el Espaciado de las secciones de Figma:')
d.code(C['1'])
d.p('La unidad `ch` mide el ancho del carácter «0» de la fuente: 70 caracteres por línea es una medida cómoda para leer. '
    'El selector `main section > p` solo afecta a los párrafos que son hijos directos de una sección.')
d.h3('4.2 · El marcado de las tarjetas')
d.p('Copia las dos imágenes del paquete (`proyecto-cinf.jpg` y `proyecto-certificados.jpg`) en tu carpeta `assets/img/`, '
    'o usa capturas de tus propios proyectos de 1256 × 440 px. En `mis-proyectos.html`, reemplaza la sección de proyectos por esta:')
d.code(html_entre(os.path.join(P, 'mis-proyectos.html'), '<!-- SECCIÓN: Proyectos · Figma: projects-section -->', '</section>'), corto=False)
d.h3('4.3 · La rejilla')
d.p('Crea al final de `contenido.css` el bloque 13 de maquetación, con este comentario de título y la rejilla de proyectos:')
d.code('/* ==========================================================\n   13. Maquetación (sesión 10): Flexbox y Grid\n   Cada bloque sale de un marco con Disposición automática en Figma\n   ========================================================== */\n\n' + C['13.3'], corto=False)
d.tabla(['Propiedad o valor', 'Qué hace'], [
    ['`display: grid`', 'La caja ordena a sus hijos en filas y columnas'],
    ['`grid-template-columns: repeat(2, 1fr)`', 'Dos columnas. `fr` es una fracción del espacio libre: dos de `1fr` miden lo mismo'],
    ['`gap: 24px`', 'La separación entre columnas y entre filas: el Espacio 24 de `projects-grid`'],
    ['`overflow: hidden`', 'Recortar contenido: la imagen no se sale por las esquinas redondeadas de la tarjeta'],
    ['`object-fit: cover`', 'La imagen llena su caja de 220 de alto sin deformarse; lo que sobra se recorta'],
    ['`display: block` en la imagen', 'Una imagen es `inline` y deja un hueco de unos píxeles debajo, el espacio de la línea de texto'],
], anchos=['40%', '60%'])
d.callout('Especificidad en acción:', 'en la sesión 09 escribiste `img { border-radius: var(--radius-md); }` y `article { padding: 1.5rem; }`. '
          '`.project-image` y `.project-card` son clases (0-1-0) y ganan a esas reglas de tipo (0-0-1): por eso '
          '`border-radius: 0` y `padding: 0` se aplican.')
d.comprueba('las dos tarjetas miden lo mismo, la imagen va de borde a borde y respeta las esquinas redondeadas, y entre '
            'las tarjetas hay 24 px.')

d.h2('Paso 5 · Sobre mí a dos columnas con Flexbox')
d.p('En Figma, `about-content` pone el texto a la izquierda y el gráfico de 480 × 264 a la derecha, con Espacio 64. '
    'En `sobre-mi.html`, envuelve la foto y el párrafo en `about-text`, y ese bloque y el `aside` en `about-content`:')
d.code(html_entre(os.path.join(P, 'sobre-mi.html'), '<!-- SECCIÓN: Sobre mí · Figma: about-section -->', '</section>'), corto=False)
d.p('Añade el bloque 13.1 en `contenido.css`, antes del 13.3:')
d.code(C['13.1'])
d.comprueba('«En resumen» queda a la derecha con 480 px de ancho, centrado en vertical respecto de la foto y el párrafo.')

d.h2('Paso 6 · Contacto: Flexbox en la lista y Grid en el formulario')
d.h3('6.1 · Las tarjetas de contacto')
d.p('En `contactame.html`, reemplaza la primera sección por esta:')
d.code(html_entre(os.path.join(P, 'contactame.html'), '<!-- SECCIÓN: Contacto · Figma: contact-section -->', '</section>'), corto=False)
d.p('Y en `contenido.css`, después del 13.3:')
d.code(C['13.4'], corto=False)
d.callout('El truco para centrar:', 'un contenedor con `display: flex`, `align-items: center` y `justify-content: center` '
          'centra a su hijo en los dos ejes. Así quedan las letras dentro del círculo de 44 × 44.')
d.h3('6.2 · El formulario en rejilla')
d.p('En el mismo archivo HTML, añade la clase `form-grid` al `<form>` y la clase `form-actions` al párrafo de los botones:')
d.code('''<form class="form-grid" action="contactame.html" method="get">
  <fieldset> … Tus datos … </fieldset>
  <fieldset> … Tu mensaje … </fieldset>

  <!-- Ocupa las dos columnas de la rejilla -->
  <p class="form-actions">
    <button type="submit">Enviar mensaje</button>
    <button type="reset">Limpiar</button>
  </p>
</form>''')
d.p('En `contenido.css`, después del 13.4:')
d.code(C['13.5'])
d.p('`grid-column: 1 / -1` se lee «desde la primera línea de la rejilla hasta la última»: el párrafo de los botones '
    'ocupa las dos columnas. Las líneas de una rejilla de dos columnas son tres: 1, 2 y 3; el `-1` es siempre la última.')
d.comprueba('a la derecha del título hay tres filas iguales con un círculo azul; debajo, «Tus datos» y «Tu mensaje» '
            'quedan lado a lado y los botones ocupan todo el ancho.')

d.h2('Paso 7 · La multimedia en rejilla, las pantallas estrechas y la publicación')
d.h3('7.1 · Una columna fija y otra flexible')
d.p('En `sobre-mi.html`, dentro de la sección «Mi presentación», envuelve el contenido en dos niveles: un `div` con la '
    'clase `media-grid` y, dentro, la figura del video y un `div` con todo lo demás:')
d.code('''<div class="media-grid">
  <figure> … video propio, controles y figcaption … </figure>

  <div>
    <figure> … iframe de YouTube … </figure>
    <figure> … audio … </figure>
    <details> … transcripción … </details>
  </div>
</div>''')
d.p('Y en `contenido.css`, el bloque 13.2, después del 13.1:')
d.code(C['13.2'])
d.p('`315px 1fr` mezcla una medida fija con una fracción: la primera columna mide lo que el video vertical y la segunda '
    'toma todo el espacio que queda.')
d.h3('7.2 · Todo a una columna en pantallas estrechas')
d.p('Copia este bloque al final de `contenido.css`. En la sesión 12 escribirás tus propias media queries:')
d.code(C['14'])
d.h3('7.3 · Valida y publica')
d.pasos(['Valida las cuatro páginas en **validator.w3.org** y tus cuatro hojas de estilo en **jigsaw.w3.org/css-validator**: cero errores.',
         'Estrecha la ventana del navegador hasta el ancho de un celular: no debe aparecer barra de desplazamiento horizontal.',
         'Publica en Netlify y abre la URL en tu celular.'])

d.h2('Lista de comprobación')
d.check(['`index.html` enlaza `global.css`, `header.css` e `index.css`, en ese orden.',
         'El Hero tiene dos columnas centradas en vertical, con 64 px entre ellas y el Espaciado 160 · 80 · 100 · 80.',
         'Cada contenedor flex o grid del CSS corresponde a un marco con Disposición automática en tu Figma.',
         'Las tarjetas de proyecto miden lo mismo y la imagen respeta sus esquinas.',
         'Sobre mí y Contacto tienen dos columnas en escritorio y una en el celular.',
         'Los botones del formulario ocupan las dos columnas de la rejilla.',
         'Ninguna página tiene desplazamiento horizontal al estrecharla.',
         'El HTML y el CSS pasan los validadores del W3C sin errores.'])

d.h2('Errores frecuentes en esta sesión')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['`display: flex` no hace nada', 'Está en el hijo y no en el padre. Flexbox y Grid se escriben en el contenedor; los hijos directos son los que se ordenan'],
    ['Un elemento no se mueve con `justify-content`', 'Ese eje no es el que crees. Con `flex-direction: column`, `justify-content` trabaja en vertical y `align-items` en horizontal'],
    ['Las dos columnas no miden lo que deberían', 'Falta `flex: 1` en la columna que debe llenar el espacio, o `flex: 0 0 480px` en la de ancho fijo'],
    ['La imagen deja un hueco debajo', 'Falta `display: block;` en `.project-image`'],
    ['La imagen sale deformada', 'Falta `object-fit: cover;` o se escribió `height` sin `width: 100%`'],
    ['La imagen tapa las esquinas redondeadas', 'Falta `overflow: hidden;` en `.project-card`'],
    ['Los botones del formulario quedan en una sola columna', 'Falta la clase `form-actions` en el párrafo o `grid-column: 1 / -1;` en su regla'],
    ['Aparece desplazamiento horizontal en el celular', 'Falta el bloque 14 (media queries) o un ancho fijo en px no tiene su `max-width: 100%`'],
], anchos=['36%', '64%'])

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Sesion10_Modelo_de_Caja_Flexbox_y_Grid.html'))
print('ok')
