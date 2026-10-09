# -*- coding: utf-8 -*-
"""Guía de código · Sesión 13: Bootstrap y su sistema de grillas."""
import os
import sys
from guia import Doc, css_bloques, html_entre

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
P = os.path.join(REPO, 'SESION 13', 'mi-portafolio-dagner')
CSS = os.path.join(P, 'assets', 'css')
CU = os.path.join(P, 'cursos.html')
HD = os.path.join(CSS, 'header.css')
K = css_bloques(os.path.join(CSS, 'cursos.css'))
H = css_bloques(HD)


def regla(ruta, desde, n=1):
    return html_entre(ruta, desde, '\n}', ocurrencia_hasta=n)


d = Doc('Guía paso a paso: Bootstrap y su sistema de grillas en tu portafolio',
        'Guía paso a paso · Sesión 13: Bootstrap y su grilla',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 13',
        'Instalas Bootstrap 5.3 y construyes una página nueva, Cursos, con su grilla de 12 columnas: '
        'filas, columnas, puntos de quiebre, medianiles y desplazamientos.')

d.callout('Vienes de la sesión 12:', 'necesitas tu portafolio responsivo, con la etiqueta viewport y las media queries. '
          'Hoy no cambias lo que ya funciona: añades una quinta página que usa Bootstrap.')

d.h3('Qué vas a hacer')
d.p('Hasta ahora escribiste cada regla a mano. Un **framework** como Bootstrap trae miles de reglas ya escritas y '
    'probadas: tú las usas poniendo clases en el HTML. Hoy usas su pieza central, la **grilla**: un sistema de filas y '
    '12 columnas que se reacomoda solo según el ancho de la pantalla.')
d.tabla(['Archivo', 'Qué cambia hoy', 'En Figma'], [
    ['cursos.html (nuevo)', 'Bootstrap desde el CDN y cuatro secciones con `row` y `col-*`', 'El marco `mi-portafolio-cursos`'],
    ['assets/css/cursos.css (nuevo)', 'El aspecto de la página: la caja central, las tarjetas y los pasos', '`course-card`, `paso`'],
    ['assets/css/header.css', 'El bloque 6 deja la cabecera intacta junto al Reboot de Bootstrap; el menú puede bajar de línea en 360 px', '`Encabezado`'],
    ['Las cuatro páginas', 'El enlace **Cursos** en el menú y en el pie', '`nav-links`'],
], anchos=['26%', '48%', '26%'])

d.h3('Cómo se reparte')
d.tabla(['Momento', 'Pasos', 'Qué practicas'], [
    ['En clase, juntos', '0 al 2', 'Instalar Bootstrap, el orden de las hojas, el Reboot y la primera fila'],
    ['En clase, tú', '3 y 4', 'El catálogo en 1, 2 y 3 columnas; los pasos en 1, 2 y 4'],
    ['Tarea', '5 y 6', 'Filas anidadas, offset, el enlace del menú; validar y publicar'],
    ['En Figma', 'Guía de Figma', 'La cuadrícula de 12 columnas y el marco de la página Cursos'],
], anchos=['18%', '14%', '68%'])

d.h2('Antes de escribir: la cuadrícula de Figma es la grilla de Bootstrap')
d.p('En la guía de Figma de hoy pones una cuadrícula de 12 columnas sobre tu página. Cada dato de esa cuadrícula '
    'tiene su clase en Bootstrap:')
d.tabla(['En Figma', 'En Bootstrap', 'En tu página Cursos'], [
    ['Cuadrícula de 12 columnas', 'Una fila: `.row`, siempre de 12 columnas', 'Cada sección tiene su `row`'],
    ['Una tarjeta que ocupa 4 columnas', '`.col-lg-4`', 'Tres tarjetas por fila: 4 + 4 + 4 = 12'],
    ['Medianil (Gutter) 24', '`.g-4`: 1.5rem, es decir, 24px', '`<div class="row g-4">`'],
    ['Margen 80', 'El `padding` de la caja que hace de contenedor', '`main { padding: 6.25rem 5rem; }`'],
    ['Marco móvil de 4 columnas', 'Sin clase de punto de quiebre: `.col-12`', 'Una tarjeta por fila en el celular'],
], anchos=['30%', '36%', '34%'])
d.callout('Si no coinciden, manda Figma:', 'tus márgenes son de 80 y tu medianil de 24. Por eso la página Cursos usa tu '
          '`main` como contenedor y la clase `g-4`, que mide justo 24px.')

d.h2('Paso 0 · Instala Bootstrap desde el CDN')
d.p('Un **CDN** (red de distribución de contenido) es un servidor que entrega archivos públicos muy rápido. No '
    'descargas nada: enlazas la hoja de estilos de Bootstrap con una etiqueta `<link>`. Crea `cursos.html` copiando la '
    'cabecera y el pie de `mis-proyectos.html`, y en el `<head>` escribe:')
d.code(html_entre(CU, '<!-- 0. Bootstrap 5.3.8', 'href="assets/css/cursos.css" />'))
d.tabla(['Atributo', 'Qué hace'], [
    ['`href`', 'La dirección del archivo: Bootstrap, versión 5.3.8, la hoja ya minificada (sin espacios ni comentarios)'],
    ['`integrity`', 'Una huella del archivo. Si alguien lo alterara en el servidor, el navegador no lo usaría'],
    ['`crossorigin="anonymous"`', 'Permite comprobar la huella de un archivo que viene de otro sitio'],
], anchos=['30%', '70%'])
d.callout('Copia el enlace completo de getbootstrap.com:', 'una sola letra distinta en `integrity` y el navegador no '
          'carga Bootstrap. Si no tienes internet en clase, descarga Bootstrap, guarda `bootstrap.min.css` en '
          '`assets/css/` y enlázalo con una ruta relativa, sin `integrity`.')
d.comprueba('abre `cursos.html` con DevTools, pestaña **Network** (Red), y recarga. `bootstrap.min.css` aparece con '
            'el estado `200`: está cargado.')

d.h2('Paso 1 · El orden de las hojas y el Reboot')
d.p('Bootstrap va **primero**. Tus hojas van después: con la misma especificidad gana la regla escrita al final, así '
    'que tu diseño puede ajustar a Bootstrap y no al revés.')
d.p('Bootstrap trae su propio reinicio de estilos, el **Reboot**. Pone margen a los títulos y los párrafos y '
    'sangría a las listas, con selectores de etiqueta como `h1` o `ul` (especificidad 0-0-1). Tu reinicio de '
    '`global.css` usa `*` (0-0-0) y pierde, aunque esté después. Por eso la cabecera se descuadra.')
d.p('Añade este bloque en `header.css`, antes de las media queries. Con `header h1` (0-0-2) le ganas al Reboot:')
d.code(H['6'])
d.callout('¿Y contenido.css?', 'la página Cursos no lo enlaza. Sus reglas de etiqueta (para `button`, `article` o '
          '`aside`) chocarían con los componentes de Bootstrap que usarás en la sesión 14. En su lugar, `cursos.css` '
          'trae solo lo que la página necesita.')

d.h2('Paso 2 · Contenedor, fila y columnas')
d.p('La grilla tiene tres piezas, siempre en este orden: un **contenedor** que limita el ancho, una **fila** '
    '(`.row`) y, dentro de ella, las **columnas** (`.col-*`). Una fila tiene 12 columnas: el número de la clase dice '
    'cuántas ocupa cada hijo.')
d.tabla(['Clase', 'Qué hace'], [
    ['`.container`', 'Una caja centrada con un ancho máximo para cada punto de quiebre (540, 720, 960, 1140 y 1320px)'],
    ['`.container-fluid`', 'Una caja que siempre ocupa todo el ancho'],
    ['`.row`', 'Una fila: es un contenedor flex que reparte sus hijos en 12 columnas'],
    ['`.col-6`', 'Ocupa 6 de las 12 columnas: la mitad'],
    ['`.col`', 'Sin número: las columnas de la fila se reparten el ancho en partes iguales'],
], anchos=['26%', '74%'])
d.p('En tu portafolio, `main` ya es un contenedor desde la sesión 10: ancho máximo de 1440 y márgenes de 80. Escríbelo '
    'en el bloque 1 de `cursos.css`:')
d.code(K['1'])
d.h3('2.1 · Los puntos de quiebre')
d.p('Bootstrap se escribe **celular primero**: una clase sin punto de quiebre vale para todos los anchos, y una con '
    'punto de quiebre vale desde ese ancho hacia arriba.')
d.tabla(['Punto de quiebre', 'Desde', 'Clase de ejemplo', 'En tu portafolio'], [
    ['Sin nombre (xs)', '0px', '`.col-12`', 'El celular'],
    ['sm', '576px', '`.col-sm-6`', 'Celular girado'],
    ['md', '768px', '`.col-md-6`', 'Tablet vertical'],
    ['lg', '992px', '`.col-lg-4`', 'Tu punto de quiebre de tablet de la sesión 12'],
    ['xl', '1200px', '`.col-xl-3`', 'Laptop'],
    ['xxl', '1400px', '`.col-xxl-2`', 'Tu diseño de 1440'],
], anchos=['22%', '14%', '24%', '40%'])
d.h3('2.2 · La primera fila: la presentación')
d.p('Dentro de `<main>`, escribe la primera sección. En pantallas de 992px o más, el texto ocupa 7 columnas y las '
    'cifras 5 (7 + 5 = 12). En las más pequeñas, cada una ocupa la fila entera y se apilan:')
d.code(html_entre(CU, '<!-- SECCIÓN 1 · Figma: cursos-intro', '</section>'), corto=False)
d.tabla(['Clase', 'Qué hace'], [
    ['`.g-4`', 'El medianil: 24px entre columnas y entre filas. Va en la `row`, no en las columnas'],
    ['`.align-items-center`', 'Centra las columnas en vertical: la fila es un contenedor flex (sesión 10)'],
    ['`.row-cols-3`', 'En la fila anidada, cada hijo `.col` mide un tercio, sin escribir el número en cada uno'],
], anchos=['30%', '70%'])
d.comprueba('a 1440px, el título queda a la izquierda y la tarjeta de cifras a la derecha. Al estrechar la ventana '
            'por debajo de 992px, la tarjeta baja debajo del texto.')

d.h2('Paso 3 · El catálogo: 1, 2 y 3 columnas')
d.p('Una misma columna puede llevar varias clases, una por punto de quiebre. Se leen de izquierda a derecha, del '
    'celular al escritorio:')
d.code('''<div class="col-12 col-md-6 col-lg-4">
<!--  celular: 12 de 12 (una por fila)
      desde 768px: 6 de 12 (dos por fila)
      desde 992px: 4 de 12 (tres por fila) -->''')
d.p('Escribe la sección del catálogo con sus seis tarjetas. Aquí van las dos primeras; las demás siguen el mismo molde:')
d.code(html_entre(CU, '<!-- SECCIÓN 2 · Figma: cursos-grid', '</article>\n          </div>', ocurrencia_hasta=2) + '\n          <!-- … cuatro tarjetas más … -->\n        </div>\n      </section>', corto=False)
d.p('Bootstrap reparte las columnas; el aspecto de la tarjeta lo pones tú. Añade el bloque 4 en `cursos.css`:')
d.code(K['4'], corto=False)
d.callout('`height: 100%` iguala las tarjetas:', 'cada columna de una fila mide lo mismo que la más alta, porque la '
          'fila es flex. Si la tarjeta llena su columna, todas las de una fila quedan iguales.')
d.tabla(['Medianil', 'Mide', 'Medianil', 'Mide'], [
    ['`.g-0`', '0', '`.g-3`', '16px'],
    ['`.g-1`', '4px', '`.g-4`', '24px: tu Medianil de Figma'],
    ['`.g-2`', '8px', '`.g-5`', '48px'],
], negrita_primera=False, anchos=['18%', '32%', '18%', '32%'])
d.p('`gx-*` cambia solo la separación horizontal y `gy-*`, solo la vertical.')
d.comprueba('a 1440px ves dos filas de tres tarjetas; a 820px, tres filas de dos; a 390px, una tarjeta debajo de otra.')

d.h2('Paso 4 · Los pasos: una lista que también es fila')
d.p('Una fila no tiene que ser un `div`: cualquier etiqueta con la clase `row` funciona. Aquí, una lista ordenada con '
    'sus cuatro `li` como columnas: 1 por fila en el celular, 2 desde 576px y 4 desde 992px.')
d.code(html_entre(CU, '<!-- SECCIÓN 3 · Figma: cursos-pasos', '</li>') + '\n          <!-- … tres pasos más … -->\n        </ol>\n      </section>')
d.p('El Reboot le pone 2rem de sangría a las listas. El bloque 5 se la quita y le da forma a cada paso:')
d.code(K['5'], corto=False)

d.h2('Paso 5 · Filas anidadas y desplazamientos')
d.h3('5.1 · Una fila dentro de una columna')
d.p('Las cifras de la presentación son una **fila anidada**: una `row` dentro de una columna. Vuelve a tener 12 '
    'columnas, ahora contadas dentro de su columna padre. Su aspecto está en el bloque 3:')
d.code(K['3'])
d.h3('5.2 · Centrar con offset')
d.p('`offset-lg-2` deja 2 columnas vacías a la izquierda desde 992px. Con 8 de ancho, el bloque queda centrado: '
    '2 + 8 + 2 = 12.')
d.code(html_entre(CU, '<!-- SECCIÓN 4 · Figma: cursos-llamado', '</section>'))
d.code(K['6'], corto=False)
d.h3('5.3 · Ampliación: cambiar el orden')
d.p('`order-*` cambia el orden visual de las columnas sin tocar el HTML. Por ejemplo, para que una imagen vaya a la '
    'izquierda en escritorio pero debajo del texto en el celular:')
d.code('''<div class="row g-4">
  <div class="col-lg-6 order-lg-2">Texto: primero en el HTML y en el celular</div>
  <div class="col-lg-6 order-lg-1">Imagen: a la izquierda desde 992px</div>
</div>''')
d.callout('Cuidado con el orden visual:', 'quien navega con el teclado o con un lector de pantalla sigue el orden del '
          'HTML. Usa `order-*` solo cuando el contenido se entienda en los dos órdenes.')

d.h2('Paso 6 · El enlace en el menú, validación y publicación')
d.p('En las cinco páginas, añade **Cursos** al menú de la cabecera y al del pie, entre Proyectos y Contacto:')
d.code('''<li><a href="mis-proyectos.html">Proyectos</a></li>
<li><a href="cursos.html">Cursos</a></li>
<li><a href="contactame.html">Contacto</a></li>''')
d.p('Con cinco enlaces, el menú ya no cabe en una fila en un celular de 360px. En `header.css`, dentro de la media '
    'query de 600px, deja que baje de línea:')
d.code(html_entre(HD, '  nav[aria-label="Navegacion principal"] ul {\n    flex-wrap', '\n  }'))
d.pasos(['En DevTools, revisa la página Cursos a 390, 820 y 1440 px: 1, 2 y 3 tarjetas por fila.',
         'Pasa el cursor por el borde de una columna en el panel Elements: DevTools muestra la etiqueta **flex** en cada `.row`.',
         'Valida `cursos.html` en **validator.w3.org** y `cursos.css` en **jigsaw.w3.org/css-validator**. El validador de CSS no revisa Bootstrap: solo tus archivos.',
         'Publica en Netlify y abre la página en tu celular.'])

d.h2('Lista de comprobación')
d.check(['`cursos.html` enlaza Bootstrap antes que `global.css`, `header.css` y `cursos.css`.',
         'El enlace de Bootstrap tiene `integrity` y `crossorigin` completos.',
         'La cabecera de la página Cursos se ve igual que en las demás páginas.',
         'Cada `.col-*` está dentro de una `.row`, y las columnas de una fila suman 12 o menos.',
         'El catálogo muestra 1, 2 y 3 tarjetas por fila según el ancho.',
         'El medianil `g-4` está en la fila, no en las columnas.',
         'Las cinco páginas tienen el enlace Cursos en el menú y en el pie.',
         'Ninguna página se desplaza hacia los lados a 360 px.',
         'El HTML y tu CSS pasan los validadores del W3C sin errores.'])

d.h2('Errores frecuentes en esta sesión')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['Bootstrap no se aplica', 'El `integrity` está incompleto o mal copiado, o la URL tiene un error. Cópialo otra vez de getbootstrap.com'],
    ['Bootstrap le gana a tu diseño', 'Lo enlazaste después de tus hojas. Bootstrap va primero'],
    ['La cabecera se descuadra en la página Cursos', 'Falta el bloque 6 de `header.css`: el Reboot le dio margen al `h1` y sangría al menú'],
    ['Las columnas quedan una debajo de otra en escritorio', 'Falta la `row` alrededor, o la clase dice `col-lg4` sin guion'],
    ['Aparece desplazamiento horizontal', 'Una `row` está fuera de un contenedor con `padding`: sus márgenes negativos sobresalen 12px'],
    ['La cuarta tarjeta queda sola en una fila', 'Es lo esperado: si las columnas suman más de 12, la siguiente baja a otra línea'],
    ['No hay separación entre tarjetas', 'Escribiste `g-4` en las columnas. Va en la `row`'],
], anchos=['36%', '64%'])

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Sesion13_Bootstrap_y_su_Sistema_de_Grillas.html'))
print('ok')
