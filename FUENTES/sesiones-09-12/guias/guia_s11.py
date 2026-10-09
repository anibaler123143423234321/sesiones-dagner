# -*- coding: utf-8 -*-
"""Guía de código · Sesión 11: transiciones, transformaciones y animaciones."""
import os
import sys
from guia import Doc, css_bloques, html_entre

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
P = os.path.join(REPO, 'SESION 11', 'mi-portafolio-dagner')
CSS = os.path.join(P, 'assets', 'css')
G = os.path.join(CSS, 'global.css')
HD = os.path.join(CSS, 'header.css')
IX = os.path.join(CSS, 'index.css')
CO = os.path.join(CSS, 'contenido.css')
I = css_bloques(IX)


def regla(ruta, desde, n=1):
    """Desde la línea que contiene `desde` hasta el cierre de su n-ésima regla."""
    return html_entre(ruta, desde, '\n}', ocurrencia_hasta=n)


d = Doc('Guía paso a paso: transiciones, transformaciones y animaciones en tu portafolio',
        'Guía paso a paso · Sesión 11: transiciones y animaciones CSS3',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 11',
        'Tu portafolio responde al cursor: los enlaces, los botones y las tarjetas cambian con suavidad, y el Hero '
        'aparece al cargar la página. Es lo mismo que el prototipo de Figma, escrito en CSS.')

d.callout('Vienes de la sesión 10:', 'necesitas las cuatro hojas de estilo (`global.css`, `header.css`, `index.css` y '
          '`contenido.css`) con el Hero, Flexbox y Grid funcionando. Si te falta algo, compáralo con la carpeta resuelta '
          'de la sesión 10 antes de empezar. Hoy no cambia el HTML: todo se escribe en CSS.')

d.h3('Qué vas a hacer')
d.p('Hasta ahora cada regla describía un solo momento: cómo se ve la página quieta. Hoy describes dos momentos (el '
    'normal y el que aparece al pasar el cursor) y le dices al navegador cómo ir de uno a otro. Primero los estados, '
    'después las transiciones, las transformaciones y, por último, las animaciones con `@keyframes`.')
d.tabla(['Archivo', 'Qué cambia hoy', 'En Figma'], [
    ['global.css', 'Tres variables de movimiento y el color Hover del botón; el bloque 10 de movimiento reducido', 'Las medidas de la Animación inteligente'],
    ['header.css', 'El subrayado animado del menú, el botón de la cabecera y los enlaces del pie', '`nav-links`'],
    ['index.css', 'Los botones del Hero (`:hover` y `:active`), la entrada del Hero y el cursor que parpadea', 'El componente `btn-primary` y su variante Hover'],
    ['contenido.css', 'Enlaces, botones, campos y filas de la tabla; las tarjetas de proyecto y de contacto', '`project-card` y `contact-card`'],
], anchos=['20%', '52%', '28%'])

d.h3('Cómo se reparte')
d.tabla(['Momento', 'Pasos', 'Qué practicas'], [
    ['En clase, juntos', '0 al 3', 'Los estados en DevTools; las variables de movimiento; el menú y los botones con `transition`'],
    ['En clase, tú', '4 y 5', 'Las tarjetas con `transform`; el Hero con `@keyframes`'],
    ['Tarea', '6 y 7', 'El resto de los estados; el movimiento reducido; validar y publicar'],
    ['En Figma', 'Guía de Figma', 'El botón como componente, su variante Hover y el prototipo'],
], anchos=['18%', '14%', '68%'])

d.h3('Material del paquete')
d.lista(['**mi-portafolio-dagner/:** la carpeta resuelta de la sesión 11. El HTML es el mismo de la sesión 10.',
         '**Guía de Figma · Sesión 11:** el botón como componente, su variante Hover y el prototipo, clic por clic.',
         '**Esta guía:** cada paso indica qué archivo tocar, qué código escribir y cómo comprobarlo.'])

d.h2('Antes de escribir: el prototipo de Figma es una transición')
d.p('En la guía de Figma de hoy creas dos variantes del botón y las unes con una interacción. Cada pieza de esa '
    'interacción tiene su equivalente en CSS:')
d.tabla(['En Figma', 'En CSS', 'En tu portafolio'], [
    ['Variante `Estado=Predeterminado`', 'La regla normal', '`.btn-primary { … }`'],
    ['Variante `Estado=Hover`', 'La misma regla con `:hover`', '`.btn-primary:hover { … }`'],
    ['Desencadenante: Mientras se pasa el cursor (While hovering)', 'La pseudo-clase `:hover`', 'Al salir el cursor, vuelve sola al estado normal'],
    ['Desencadenante: Mientras se presiona (While pressing)', 'La pseudo-clase `:active`', '`.btn:active { … }`'],
    ['Acción: Cambiar a (Change to)', 'El navegador pasa de una regla a la otra', '—'],
    ['Animación: Instantáneo (Instant)', 'Sin `transition`: el cambio es de golpe', 'Así estaba tu portafolio hasta hoy'],
    ['Animación: Animación inteligente (Smart animate)', '`transition`', 'Pasa por todos los valores intermedios'],
    ['Curva: Salida suave (Ease out)', '`ease-out` o `cubic-bezier(…)`', '`var(--ease-out)`'],
    ['Duración: 200 ms', '`0.2s` o `200ms`', '`var(--duration-fast)`'],
], anchos=['36%', '30%', '34%'])
d.callout('Si no coinciden, manda Figma:', 'el color de la variante Hover, la duración y la curva que pongas en tu '
          'prototipo son los que escribes en CSS.')

d.h2('Paso 0 · Los estados de un elemento')
d.p('Una pseudo-clase selecciona un elemento solo mientras está en cierto estado. Ya usaste `:nth-child` y '
    '`:focus-visible` en la sesión 09. Hoy usas las de interacción:')
d.tabla(['Pseudo-clase', 'Cuándo se aplica', 'Dónde la usas'], [
    ['`:hover`', 'Mientras el cursor está encima', 'Menú, botones, tarjetas, filas de la tabla'],
    ['`:active`', 'Mientras se mantiene presionado el botón del mouse o el dedo', '`.btn:active`'],
    ['`:focus`', 'Mientras el elemento tiene el foco: un campo en el que estás escribiendo', '`input:focus`'],
    ['`:focus-visible`', 'Con el foco puesto desde el teclado (Tab)', 'El contorno de `global.css`, desde la sesión 09'],
], anchos=['20%', '50%', '30%'])
d.p('Para estudiar un estado sin perseguirlo con el mouse, fuérzalo en DevTools:')
d.pasos(['Abre `index.html`, haz clic derecho sobre el botón «Ver Proyectos» y elige **Inspeccionar**.',
         'En la pestaña **Styles**, pulsa el botón **:hov**. Aparecen casillas con los estados.',
         'Marca `:hover`. El botón queda en su estado Hover y en Styles aparece la regla `.btn-primary:hover`.',
         'Desmárcala antes de seguir.'])
d.callout('Un estado se escribe sin espacio:', '`.btn:hover` es «el botón cuando tiene el cursor encima». '
          '`.btn :hover`, con espacio, sería «cualquier elemento con el cursor encima dentro del botón».')

d.h2('Paso 1 · Las variables de movimiento (assets/css/global.css)')
d.p('Al final de `:root`, debajo de los radios, añade tres variables. Así todas las transiciones del sitio usan la '
    'misma duración y la misma curva, como los estilos de Figma:')
d.code(html_entre(G, '/* Movimiento (sesión 11)', '\n}'))
d.p('Y debajo de `--color-border`, el color de la variante Hover del botón:')
d.code(html_entre(G, '--color-primary-hover', '*/'))
d.tabla(['Curva (timing function)', 'Cómo se mueve', 'Cuándo usarla'], [
    ['`linear`', 'A la misma velocidad de principio a fin', 'Giros continuos y barras de progreso'],
    ['`ease`', 'Arranca suave, acelera y frena (el valor por defecto)', 'Cambios de color'],
    ['`ease-in`', 'Arranca lento y termina rápido', 'Elementos que salen de la pantalla'],
    ['`ease-out`', 'Arranca rápido y frena al llegar', 'Respuestas al cursor: se sienten inmediatas'],
    ['`ease-in-out`', 'Lento al principio y al final', 'Movimientos largos de un lugar a otro'],
    ['`cubic-bezier(a, b, c, d)`', 'Una curva a medida, con cuatro números', '`--ease-out`: una salida suave más marcada'],
    ['`steps(n)`', 'Salta en n pasos, sin valores intermedios', 'El cursor que parpadea (Paso 5)'],
], anchos=['28%', '42%', '30%'])
d.callout('¿Cuánto debe durar?', 'entre 150 y 400 milisegundos. Menos de 100 no se percibe y más de 500 hace que la '
          'página parezca lenta. Los botones, rápidos (`0.2s`); las piezas grandes, como una tarjeta, un poco más (`0.4s`).')

d.h2('Paso 2 · El menú con transition (assets/css/header.css)')
d.p('`transition` se escribe en la regla **normal**, no en la de `:hover`. Así el cambio es suave al entrar y también '
    'al salir el cursor.')
d.tabla(['Propiedad', 'Qué indica', 'Ejemplo'], [
    ['`transition-property`', 'Qué propiedad se anima', '`color`'],
    ['`transition-duration`', 'Cuánto dura', '`0.2s`'],
    ['`transition-timing-function`', 'Con qué curva', '`ease-out`'],
    ['`transition-delay`', 'Cuánto espera antes de empezar (opcional)', '`0.1s`'],
    ['`transition` (abreviada)', 'Las cuatro en una línea; varias propiedades se separan con comas', '`color 0.2s ease, transform 0.4s ease-out`'],
], anchos=['30%', '38%', '32%'])
d.p('Reemplaza la regla de los enlaces del menú (bloque 3) y añade su `:hover`:')
d.code(regla(HD, 'nav[aria-label="Navegacion principal"] a {', 2))
d.p('El subrayado es una imagen de fondo: un degradado de un solo color (sesión 09). En reposo mide `0%` de ancho y 2 px '
    'de alto; con el cursor encima, `100%`. Como `background-size` es una medida, se puede animar.')
d.callout('No todo se puede animar:', 'se animan las propiedades que tienen valores intermedios: colores, medidas, '
          '`opacity`, `transform`, `box-shadow`. `display` o `font-family` cambian de golpe aunque tengan `transition`.')
d.p('Haz lo mismo con el botón de la cabecera (bloque 4) y los enlaces del pie (bloque 5):')
d.code(regla(HD, 'header > a[href="contactame.html"] {', 2))
d.code(regla(HD, 'footer a {', 2))
d.comprueba('al pasar el cursor por el menú, el texto se oscurece y una línea azul crece de izquierda a derecha. '
            'Al retirarlo, la línea se recoge.')

d.h2('Paso 3 · Los botones del Hero: transition y transform (assets/css/index.css)')
d.p('`transform` mueve, escala o gira un elemento **después** de colocarlo en la página. Sus vecinos no se enteran: '
    'no se empujan ni se recolocan. Por eso es la mejor propiedad para animar.')
d.tabla(['Función', 'Qué hace', 'Ejemplo'], [
    ['`translateX(n)` · `translateY(n)` · `translate(x, y)`', 'Desplaza en horizontal, en vertical o en los dos ejes', '`translateY(-2px)`: sube 2 px'],
    ['`scale(n)`', 'Agranda o achica; `1` es el tamaño normal', '`scale(1.05)`: un 5 % más grande'],
    ['`rotate(n)`', 'Gira en grados (`deg`); negativo, al revés del reloj', '`rotate(-10deg)`'],
    ['`skew(n)`', 'Inclina', '`skewX(-8deg)`'],
    ['Varias funciones', 'Se escriben separadas por espacios y se aplican en orden', '`translateY(0) scale(0.98)`'],
    ['`transform-origin`', 'El punto desde el que se escala o se gira; por defecto, el centro', '`transform-origin: left;`'],
], anchos=['36%', '38%', '26%'])
d.p('Reemplaza el bloque 3 de `index.css`:')
d.code(I['3'], corto=False)
d.callout('El orden importa:', '`.btn:active` y `.btn-primary:hover` tienen la misma especificidad (0-2-0). Si las dos '
          'se cumplen (el cursor está encima y además presionas), gana la que está escrita después. Por eso `:active` va al final.')
d.callout('¿Por qué no `margin-top: -2px`?', 'porque `margin` sí empuja a los vecinos: el párrafo de arriba y el otro '
          'botón se moverían con él. `transform` mueve solo al botón.')
d.comprueba('con el cursor encima, «Ver Proyectos» se oscurece, sube 2 px y proyecta una sombra azul. Al presionarlo, '
            'se encoge un poco. «Contáctame» se rellena con un gris muy claro.')

d.h2('Paso 4 · Las tarjetas con transform (assets/css/contenido.css)')
d.h3('4.1 · Las tarjetas de proyecto')
d.p('En el bloque 13.3, añade `transition` a `.project-card` y a `.project-image`, y escribe sus `:hover`:')
d.code(regla(CO, '/* Figma: project-card', 4), corto=False)
d.p('El selector `.project-card:hover .project-image` se lee «la imagen que está dentro de una tarjeta que tiene el '
    'cursor encima». El cursor puede estar sobre el texto de la tarjeta, no sobre la imagen, y aun así la imagen se acerca. '
    'El `overflow: hidden` de la sesión 10 recorta lo que sobra: la imagen crece dentro de su marco.')
d.h3('4.2 · Las tarjetas de contacto')
d.p('En el bloque 13.4, añade `transition` a `.contact-card` y a `.contact-icon` y sus reglas `:hover`:')
d.code(regla(CO, '/* Figma: contact-card', 2))
d.code(regla(CO, '/* El círculo de 44', 2), corto=False)
d.comprueba('en Proyectos, la tarjeta sube 6 px con una sombra y su imagen se acerca. En Contacto, la fila se desplaza '
            '4 px a la derecha, su borde se vuelve azul y el círculo gira un poco.')

d.h2('Paso 5 · Animaciones con @keyframes (assets/css/index.css)')
d.p('Una transición necesita un cambio de estado: el cursor entra o sale. Una **animación** arranca sola, al cargar la '
    'página, y puede repetirse. Se escribe en dos partes: los fotogramas clave, con un nombre, y la propiedad `animation` '
    'que los usa.')
d.h3('5.1 · Los fotogramas clave')
d.p('Al final de `index.css`, antes de las media queries, crea el bloque 5:')
d.code(I['5'])
d.p('`from` es el 0 % de la animación y `to`, el 100 %. Entre los dos puedes poner los porcentajes que quieras, como '
    'el `50%` de `parpadeo`. Las propiedades que no se escriben en un fotograma conservan su valor normal.')
d.h3('5.2 · La entrada del Hero')
d.p('En el bloque 2, añade la animación a `.hero-left`, y en el bloque 4, a `.hero-right` con 0.2 s de retraso:')
d.code(regla(IX, '.hero-left {'))
d.code(regla(IX, '.hero-right {'))
d.tabla(['Propiedad', 'Qué indica', 'En `aparecer`'], [
    ['`animation-name`', 'Qué `@keyframes` usar', '`aparecer`'],
    ['`animation-duration`', 'Cuánto dura una vuelta', '`0.8s`'],
    ['`animation-timing-function`', 'Con qué curva', '`var(--ease-out)`'],
    ['`animation-delay`', 'Cuánto espera antes de empezar', '`0.2s` en `.hero-right`'],
    ['`animation-iteration-count`', 'Cuántas veces se repite; `infinite`, sin fin', '`1` (por defecto)'],
    ['`animation-direction`', '`normal`, `reverse` o `alternate` (ida y vuelta)', '`normal`'],
    ['`animation-fill-mode`', 'Qué valores muestra antes de empezar y al terminar', '`both`'],
], anchos=['30%', '44%', '26%'])
d.callout('¿Para qué sirve `both`?', 'sin él, la columna derecha se vería quieta durante los 0.2 s de espera y después '
          'saltaría a `opacity: 0` para empezar a aparecer. Con `both`, muestra el fotograma `from` mientras espera y '
          'se queda en el `to` al terminar.')
d.h3('5.3 · El cursor que parpadea')
d.p('En el bloque 4, después de `.code-body`, añade un pseudo-elemento al final del código:')
d.code(regla(IX, '/* El cursor que parpadea'))
d.p('`::after` crea una caja vacía al final del `<code>`: no hace falta tocar el HTML. `steps(1)` hace que cambie de '
    'golpe, sin pasar por la mitad de la opacidad: se enciende y se apaga como el cursor de un editor.')
d.comprueba('al recargar la portada, la columna de texto sube y aparece, y la tarjeta de código la sigue un instante '
            'después. Al final del código parpadea un cursor azul.')

d.h2('Paso 6 · El resto de los estados (assets/css/contenido.css)')
d.p('Repasa las páginas interiores y añade `transition` donde ya había un cambio de estado de la sesión 09:')
d.code(regla(CO, '/* 4. Enlaces del contenido', 2))
d.code(regla(CO, '/* 8. Botones', 4), corto=False)
d.code('''/* en la regla de input, select y textarea (bloque 9), al final */
  transition: border-color var(--duration-fast) ease;

''' + regla(CO, 'input:focus,'))
d.code(regla(CO, 'tbody tr {', 2))
d.comprueba('los enlaces, los botones del formulario, los campos al hacer clic en ellos y las filas de la tabla cambian '
            'con suavidad.')

d.h2('Paso 7 · Movimiento reducido, validación y publicación')
d.h3('7.1 · Respeta a quien pidió menos movimiento')
d.p('Algunas personas se marean con las animaciones y lo indican en su sistema operativo (en Windows: **Configuración › '
    'Accesibilidad › Efectos visuales › Efectos de animación**). La media query `prefers-reduced-motion` lo detecta. '
    'Añade el bloque 10 al final de `global.css`:')
d.code(html_entre(G, '/* 10. Movimiento reducido', '\n}'))
d.p('Las duraciones pasan a 0.01 ms: todo cambia de golpe y las animaciones terminan en cuanto empiezan, así que el '
    'Hero aparece directamente en su sitio. No se escribe `0` porque algunos navegadores entonces no avisan del final de '
    'la animación.')
d.callout('`!important` es la excepción:', 'gana a cualquier otra regla, sin importar la especificidad ni el orden. '
          'No lo uses para arreglar una regla que no se aplica; aquí sí tiene sentido, porque este bloque debe ganar a '
          'todas las transiciones del sitio.')
d.p('Para probarlo sin cambiar tu sistema: en DevTools pulsa `Ctrl + Shift + P`, escribe **rendering** y elige '
    '**Show Rendering**. En la pestaña que se abre, en **Emulate CSS media feature prefers-reduced-motion**, elige '
    '`reduce` y recarga la página.')
d.h3('7.2 · Valida y publica')
d.pasos(['Valida tus cuatro hojas de estilo en **jigsaw.w3.org/css-validator**: cero errores.',
         'Valida las cuatro páginas en **validator.w3.org**: como el HTML no cambió, deben seguir sin errores.',
         'Recorre las cuatro páginas solo con el teclado (Tab): cada enlace y botón muestra su contorno.',
         'Publica en Netlify y prueba los efectos en tu celular: allí no hay cursor, así que `:hover` se activa al tocar.'])

d.h2('Lista de comprobación')
d.check(['`:root` tiene `--duration-fast`, `--duration-base`, `--ease-out` y `--color-primary-hover`.',
         'Cada `transition` está en la regla normal, no en la de `:hover`.',
         'Ninguna transición usa `all`: cada una nombra las propiedades que cambian.',
         'Los movimientos usan `transform`, no `margin` ni `top`.',
         'El botón principal se oscurece con el mismo color que la variante Hover de tu Figma.',
         '`.btn:active` está escrito después de los `:hover`.',
         'El Hero aparece al cargar la portada y el cursor del código parpadea.',
         'Con `prefers-reduced-motion: reduce`, la página se ve quieta.',
         'El CSS pasa el validador del W3C sin errores.'])

d.h2('Errores frecuentes en esta sesión')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['El cambio es suave al entrar y brusco al salir', 'La `transition` está en la regla `:hover`. Muévela a la regla normal'],
    ['No hay transición aunque está escrita', 'El nombre de la propiedad no coincide (`background` en una y `background-color` en la otra) o la propiedad no se puede animar, como `display`'],
    ['Al pasar el cursor, los elementos de al lado se mueven', 'Se usó `margin` o `top` para mover. Cámbialo por `transform: translateY(…)`'],
    ['`:active` no hace nada', 'Está escrito antes que el `:hover` con la misma especificidad. Pásalo debajo'],
    ['La animación no arranca', 'El nombre de `animation` no es igual al de `@keyframes` (mayúsculas, tildes) o falta la duración: sin ella dura 0 s'],
    ['El Hero parpadea antes de aparecer', 'Falta `both` en la columna con retraso: espera visible y después salta a `opacity: 0`'],
    ['La imagen de la tarjeta se sale al acercarse', 'Falta `overflow: hidden;` en `.project-card`'],
    ['El cursor del código no se ve', 'Al `::after` le falta `content: ""` o `display: inline-block`: sin ellos no hay caja que pintar'],
], anchos=['36%', '64%'])

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Sesion11_Transiciones_Transformaciones_y_Animaciones.html'))
print('ok')
