# -*- coding: utf-8 -*-
"""Guía de código · Sesión 12: diseño responsivo."""
import os
import sys
from guia import Doc, css_bloques, html_entre

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
P = os.path.join(REPO, 'SESION 12', 'mi-portafolio-dagner')
CSS = os.path.join(P, 'assets', 'css')
G = os.path.join(CSS, 'global.css')
HD = os.path.join(CSS, 'header.css')
IX = os.path.join(CSS, 'index.css')
CO = os.path.join(CSS, 'contenido.css')
H = css_bloques(HD)
I = css_bloques(IX)
C = css_bloques(CO)


def regla(ruta, desde, n=1):
    """Desde la línea que contiene `desde` hasta el cierre de su n-ésima regla."""
    return html_entre(ruta, desde, '\n}', ocurrencia_hasta=n)


d = Doc('Guía paso a paso: diseño responsivo de tu portafolio',
        'Guía paso a paso · Sesión 12: diseño responsivo',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 12',
        'Tu portafolio se adapta al ancho de la pantalla: la etiqueta viewport, las media queries, las medidas fluidas '
        'con `clamp()`, la rejilla que decide sola sus columnas y la multimedia que conserva su proporción.')

d.callout('Vienes de la sesión 11:', 'necesitas tus cuatro hojas de estilo con las transiciones y animaciones. Desde la '
          'sesión 10 copiaste unas media queries «de anticipo»; hoy entiendes qué hacen, las ordenas y las completas. '
          'Hoy también es el Taller online TA2: esta guía es tu referencia para resolverlo.')

d.h3('Qué vas a hacer')
d.p('Hasta ahora tu portafolio se diseñó para una pantalla de 1440 px. Hoy lo pruebas en un celular de 390 px y en una '
    'tablet de 820 px, y corriges lo que no cabe. Hay dos herramientas: las **media queries**, que cambian reglas a '
    'partir de cierto ancho, y las **medidas fluidas**, que se adaptan solas sin media query.')
d.tabla(['Archivo', 'Qué cambia hoy', 'En Figma'], [
    ['global.css', 'Un comentario con los dos puntos de quiebre: 992 y 600', '—'],
    ['header.css', 'La cabecera y el pie en el celular (bloque 6)', '`Encabezado` y `footer-wrapper` móviles'],
    ['index.css', 'El título del Hero con `clamp()`; el Hero en tablet y celular (bloque 6)', '`hero-section` móvil'],
    ['contenido.css', 'Los títulos con `clamp()`; la rejilla con `auto-fit`; la imagen, el video y la tabla; las páginas interiores en una columna (bloque 14)', 'Las secciones del marco móvil'],
    ['mis-proyectos.html', 'La tabla dentro de una caja que se desplaza', '—'],
], anchos=['20%', '52%', '28%'])

d.h3('Cómo se reparte')
d.tabla(['Momento', 'Pasos', 'Qué practicas'], [
    ['En clase, juntos', '0 al 2', 'El modo dispositivo de DevTools; la etiqueta viewport; las media queries de la cabecera'],
    ['En clase, tú', '3 y 4', 'El Hero con `clamp()`; Proyectos con `auto-fit`'],
    ['Taller TA2', '5 al 7', 'Multimedia, tabla y páginas interiores; pruebas en el celular y publicación'],
    ['En Figma', 'Guía de Figma', 'El marco móvil `mi-portafolio-movil` de 390'],
], anchos=['18%', '14%', '68%'])

d.h2('Antes de escribir: tres anchos de prueba')
d.p('No se diseña para cada modelo de celular: se eligen unos pocos anchos y se revisa qué pasa entre ellos. El punto '
    'en el que el diseño se rompe y necesita una regla nueva se llama **punto de quiebre** (breakpoint).')
d.tabla(['Pantalla', 'Ancho de prueba', 'Qué ves en tu portafolio', 'Regla que actúa'], [
    ['Escritorio', '1440 px', 'Tu diseño de Figma: dos columnas en el Hero, Sobre mí, Proyectos y Contacto', 'Ninguna media query'],
    ['Tablet', '820 px', 'Una sola columna, salvo Proyectos, que conserva dos tarjetas', '`@media (max-width: 992px)`'],
    ['Celular', '390 px', 'Todo en una columna; el menú bajo el nombre; los botones a todo el ancho', 'Además, `@media (max-width: 600px)`'],
], anchos=['14%', '16%', '42%', '28%'])
d.callout('Si no coinciden, manda Figma:', 'el marco móvil de la guía de Figma de hoy mide 390. Los márgenes, tamaños y '
          'columnas del celular salen de ese marco.')

d.h2('Paso 0 · Prueba tu página como si fuera un celular')
d.pasos(['Abre `index.html` en Chrome y pulsa `F12`.',
         'Pulsa `Ctrl + Shift + M` (o el icono del celular y la tablet, arriba a la izquierda de DevTools). Se activa el **modo dispositivo**.',
         'Arriba, en **Dimensions**, elige **Responsive** y escribe `390` de ancho. Recorre las cuatro páginas.',
         'Cambia a `820` y después a `1440`. Arrastra el borde derecho de la página para ver los anchos intermedios.',
         'Si aparece una barra de desplazamiento horizontal en algún ancho, anótalo: es lo que vas a corregir.'])
d.h3('0.1 · La etiqueta viewport')
d.p('Revisa que el `<head>` de tus cuatro páginas tenga esta línea desde la sesión 01:')
d.code(html_entre(os.path.join(P, 'index.html'), '<meta name="viewport"', '/>'))
d.p('Sin ella, el celular simula una pantalla de unos 980 px y muestra la página entera en miniatura: ninguna media '
    'query de 600 se activaría. `width=device-width` le dice que use su ancho real y `initial-scale=1.0`, que no la achique.')

d.h2('Paso 1 · Cómo se escribe una media query')
d.code('''@media (max-width: 992px) {
  /* estas reglas solo se aplican si la ventana mide 992px o menos */
  .hero-section {
    flex-direction: column;
  }
}''')
d.tabla(['Parte', 'Qué significa'], [
    ['`@media`', 'Empieza una regla condicional: lo que va entre sus llaves solo se aplica si se cumple la condición'],
    ['`(max-width: 992px)`', 'La condición: ancho de la ventana **hasta** 992 px. `min-width` sería **desde** ese ancho'],
    ['Las reglas de dentro', 'Selectores normales. Solo escribes las propiedades que cambian: las demás se heredan de la regla de fuera'],
    ['El lugar', 'Siempre después de las reglas que corrige: con la misma especificidad, gana la que está escrita más abajo'],
], anchos=['26%', '74%'])
d.h3('1.1 · Escritorio primero o celular primero')
d.tabla(['Enfoque', 'Cómo se escribe', 'Cuándo conviene'], [
    ['Escritorio primero (desktop first)', 'Las reglas normales son las del escritorio; `max-width` corrige hacia abajo', 'Cuando el diseño nace en un marco de escritorio, como tu Figma de 1440. Es el enfoque de tu portafolio'],
    ['Celular primero (mobile first)', 'Las reglas normales son las del celular; `min-width` añade columnas hacia arriba', 'Cuando la mayoría de visitas llega desde el celular. Es el enfoque de Bootstrap, que verás en la sesión 13'],
], anchos=['26%', '40%', '34%'])
d.h3('1.2 · Anota tus puntos de quiebre')
d.p('Una variable de `:root` no funciona dentro de la condición de `@media`: `@media (max-width: var(--tablet))` no hace '
    'nada. Por eso los anchos se escriben como número. Para no olvidarlos, anótalos al final de `:root` en `global.css`:')
d.code(html_entre(G, '/* Puntos de quiebre', '*/'))
d.h3('1.3 · No solo el ancho')
d.p('Una media query también puede preguntar por otras características de la pantalla o de la persona:')
d.tabla(['Condición', 'Se cumple cuando…'], [
    ['`(orientation: landscape)`', 'La pantalla es más ancha que alta: un celular girado'],
    ['`(hover: hover)`', 'Hay un mouse o un panel táctil que puede quedarse encima: en un celular no se cumple'],
    ['`(prefers-reduced-motion: reduce)`', 'La persona pidió menos animaciones. Ya lo usas en `global.css` (sesión 11)'],
    ['`(prefers-color-scheme: dark)`', 'La persona usa el modo oscuro en su sistema'],
    ['`print`', 'La página se está imprimiendo: `@media print { … }`'],
], anchos=['38%', '62%'])

d.h2('Paso 2 · La cabecera y el pie (assets/css/header.css)')
d.p('Reemplaza el bloque 6 de `header.css`:')
d.code(H['6'])
d.p('En la tablet solo se reducen los márgenes laterales de 80 a 24. En el celular, el nombre y el menú no caben en una '
    'fila de 80 de alto: la cabecera pierde su altura fija (`height: auto`), permite que sus hijos bajen de línea '
    '(`flex-wrap: wrap`) y los centra. El botón «Contacto» se oculta con `display: none` porque el menú ya tiene ese enlace.')
d.callout('`display: none` no es lo mismo que achicar:', 'el elemento desaparece por completo, también para los lectores '
          'de pantalla. Úsalo solo con lo que está repetido, como este botón.')
d.comprueba('a 390 px, el nombre queda centrado arriba y el menú debajo, en una fila; el botón de la cabecera no se ve.')

d.h2('Paso 3 · El Hero (assets/css/index.css)')
d.h3('3.1 · Un título fluido con clamp()')
d.p('Con una media query, el título del Hero tenía dos tamaños: 64 en escritorio y 40 desde los 600 px. Entre 600 y '
    '1440, un salto. `clamp()` lo hace crecer poco a poco. En el bloque 2, cambia el `font-size` de `.hero-title` y, '
    'en la media query de 600 del bloque 6, borra la línea `.hero-title { font-size: 40px; }`:')
d.code(regla(IX, '.hero-title {'))
d.p('`clamp(mínimo, preferido, máximo)` usa el valor preferido mientras quede entre el mínimo y el máximo. El preferido '
    'mezcla una medida fija con `vw`, que es el 1 % del ancho de la ventana:')
d.tabla(['Ancho de la ventana', '1.5rem + 4vw', 'Tamaño final'], [
    ['390 px (celular)', '24 + 15.6 = 39.6 px', '**40 px**: no baja del mínimo (2.5rem)'],
    ['600 px', '24 + 24 = 48 px', '48 px'],
    ['820 px (tablet)', '24 + 32.8 = 56.8 px', '56.8 px'],
    ['1000 px o más', '64 px o más', '**64 px**: no pasa del máximo (4rem), el tamaño de Figma'],
], anchos=['26%', '34%', '40%'])
d.callout('Por qué el mínimo y el máximo van en rem:', 'si la persona agranda la letra de su navegador, el título '
          'crece con ella. Con `vw` solo, el texto no respondería al zoom de texto.')
d.p('Haz lo mismo con los títulos de las páginas interiores, en el bloque 3 de `contenido.css`:')
d.code(regla(CO, 'main h2 {'))
d.h3('3.2 · El Hero en tablet y celular')
d.p('Reemplaza el bloque 6 de `index.css`:')
d.code(I['6'], corto=False)
d.p('En la tablet, las dos columnas se apilan con `flex-direction: column`, el mismo cambio que harás en Figma con el '
    'Flujo. En el celular, los botones también pasan a columna y `align-items: stretch` los estira a todo el ancho: un '
    'botón grande es más fácil de tocar con el dedo. La tarjeta de código achica su letra para que las líneas quepan.')
d.comprueba('a 390 px, el título mide 40 px y no se corta; los dos botones ocupan todo el ancho, uno debajo del otro; el '
            'código se lee sin desplazarse.')

d.h2('Paso 4 · Proyectos sin media query (assets/css/contenido.css)')
d.h3('4.1 · Una rejilla que decide sus columnas')
d.p('En la sesión 10, la rejilla tenía siempre dos columnas y una media query la pasaba a una. Reemplaza la regla '
    '`.projects-grid` del bloque 13.3:')
d.code(regla(CO, '/* 13.3 Proyectos'))
d.tabla(['Pieza', 'Qué hace'], [
    ['`repeat(auto-fit, …)`', 'Crea tantas columnas como quepan, en lugar de un número fijo'],
    ['`minmax(360px, 1fr)`', 'Cada columna mide como mínimo 360 px y como máximo una fracción del espacio libre'],
    ['`min(100%, 360px)`', 'El menor de los dos valores: en una pantalla de menos de 360 px, la columna mide el 100 % y no se desborda'],
    ['`auto-fit` o `auto-fill`', 'Con dos tarjetas y espacio para tres columnas, `auto-fit` estira las dos tarjetas; `auto-fill` deja la tercera columna vacía'],
], anchos=['30%', '70%'])
d.p('A 1440 px caben dos tarjetas de 628, como en Figma. A 820 caben dos de 374. A 390 solo cabe una. Si mañana añades '
    'un tercer proyecto, el escritorio mostrará tres columnas sin tocar el CSS.')
d.h3('4.2 · Una imagen que conserva su proporción')
d.p('Con una altura fija de 220, la imagen se recortaba por los lados en el celular. Cambia la altura por una proporción:')
d.code(regla(CO, '.project-image {'))
d.p('`aspect-ratio: 628 / 220` es la relación entre el ancho y el alto del rectángulo de Figma. El navegador calcula '
    'el alto a partir del ancho: 220 a 628 de ancho, unos 125 a 356.')
d.comprueba('a 820 px, Proyectos muestra dos tarjetas; a 390, una. En los dos casos la imagen se ve entera.')

d.h2('Paso 5 · El video de YouTube y la tabla', salto=True)
d.h3('5.1 · El iframe en 16:9')
d.p('Una imagen conserva su proporción con `height: auto`, pero un `iframe` no: mantiene los 315 px de alto de su '
    'atributo aunque se angoste. En el bloque 7 de `contenido.css`, después de la regla de `img, video, iframe`, añade:')
d.code(regla(CO, '/* Sesión 12: el iframe'))
d.h3('5.2 · Una tabla que se desplaza dentro de su caja')
d.p('Las tarjetas se pueden apilar; las columnas de una tabla, no. Si la tabla no cabe, lo correcto es que se desplace '
    'dentro de su propia caja y que la página no se ensanche. En `mis-proyectos.html`, envuelve la tabla en un `div`:')
d.code('''<div class="tabla-scroll" role="region" aria-label="Tabla de herramientas" tabindex="0">
  <table>
    <caption>Tecnologías con las que construí este portafolio</caption>
    …
  </table>
</div>''')
d.p('`tabindex="0"` hace que la caja reciba el foco con Tab y se pueda mover con las flechas del teclado; `role` y '
    '`aria-label` le dicen al lector de pantalla qué es. En el bloque 12 de `contenido.css`, antes de la regla `table`:')
d.code(regla(CO, '/* Sesión 12: una tabla no', 2))
d.comprueba('a 390 px, la tabla se desplaza con el dedo dentro de su caja y el resto de la página no se mueve a los lados. '
            'El video de YouTube mide 358 × 201.')

d.h2('Paso 6 · Las páginas interiores (bloque 14 de contenido.css)')
d.p('Reemplaza el bloque 14 de `contenido.css`. Ya no incluye `.projects-grid`, porque `auto-fit` se encarga de ella:')
d.code(C['14'], corto=False)
d.p('Cada regla de la tablet es un cambio de Flujo en Figma: las filas (`row`) pasan a columna y los anchos fijos de '
    '480 y 520 se sueltan con `flex-basis: auto`. En el celular, los márgenes bajan a 16 px, como en el marco móvil.')
d.comprueba('a 820 y a 390 px, Sobre mí, el video y Contacto quedan en una sola columna; los botones del formulario, uno '
            'debajo del otro en el celular.')

d.h2('Paso 7 · Pruebas y publicación')
d.pasos(['En el modo dispositivo de DevTools, recorre las cuatro páginas a `390`, `820` y `1440`. En ningún ancho debe aparecer desplazamiento horizontal.',
         'Arrastra el borde de la página desde 1440 hasta 320 sin soltar: el diseño debe cambiar sin piezas cortadas ni superpuestas.',
         'Valida las cuatro páginas en **validator.w3.org** y las cuatro hojas en **jigsaw.w3.org/css-validator**: cero errores.',
         'Publica en Netlify y abre la URL en tu celular. Gíralo en horizontal y vuelve a recorrer las páginas.',
         'Opcional: en DevTools, pestaña **Lighthouse**, marca **Mobile** y pulsa **Analyze page load**. Revisa la sección de accesibilidad.'])

d.h2('Lista de comprobación')
d.check(['Las cuatro páginas tienen la etiqueta `<meta name="viewport">`.',
         'Las media queries están al final de cada hoja, después de las reglas que corrigen.',
         'Solo hay dos puntos de quiebre, 992 y 600, anotados en `global.css`.',
         'El título del Hero y los títulos de sección usan `clamp()` con mínimo y máximo en `rem`.',
         'Proyectos usa `repeat(auto-fit, minmax(min(100%, 360px), 1fr))` y no aparece en ninguna media query.',
         'La imagen de proyecto usa `aspect-ratio` y se ve entera en el celular.',
         'El video de YouTube conserva la proporción 16:9 en todos los anchos.',
         'La tabla se desplaza dentro de `.tabla-scroll`; la página no se ensancha.',
         'A 390 px no hay desplazamiento horizontal en ninguna página.',
         'El HTML y el CSS pasan los validadores del W3C sin errores.'])

d.h2('Errores frecuentes en esta sesión')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['En el celular la página se ve en miniatura y ninguna media query funciona', 'Falta `<meta name="viewport" content="width=device-width, initial-scale=1.0">` en el `<head>`'],
    ['La media query no cambia nada', 'Está escrita antes de la regla que debe corregir. Las media queries van al final de la hoja'],
    ['Las reglas de 600 no se aplican a 390', 'Falta cerrar la llave de la media query anterior: todo lo que sigue quedó dentro de ella'],
    ['`@media (max-width: var(--tablet))` no hace nada', 'Las variables no funcionan en la condición. Escribe el número: `992px`'],
    ['Aparece desplazamiento horizontal a 390', 'Un ancho fijo en px sin `max-width: 100%`, una línea de código o una tabla sin su caja con `overflow-x: auto`. En DevTools, busca el elemento que sobresale por la derecha'],
    ['El título queda enorme en el celular', 'Se escribió `font-size: 10vw` sin `clamp()`: no tiene mínimo ni máximo'],
    ['Las tarjetas de proyecto nunca pasan a una columna', 'Falta `min(100%, 360px)` o la pantalla es más ancha que dos columnas de 360 más el `gap`'],
    ['El video de YouTube queda aplastado', 'Falta `aspect-ratio: 16 / 9` o `height: auto` en el iframe'],
], anchos=['36%', '64%'])

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Sesion12_Diseno_Responsivo.html'))
print('ok')
