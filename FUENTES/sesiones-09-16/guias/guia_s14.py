# -*- coding: utf-8 -*-
"""Guía de código · Sesión 14: componentes, utilidades y tema de Bootstrap."""
import os
import sys
from guia import Doc, css_bloques, html_entre, leer

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
P = os.path.join(REPO, 'SESION 14', 'mi-portafolio-dagner')
CSS = os.path.join(P, 'assets', 'css')
CU = os.path.join(P, 'cursos.html')
TEMA = os.path.join(CSS, 'tema-bootstrap.css')
T = css_bloques(TEMA)
K = css_bloques(os.path.join(CSS, 'cursos.css'))
JS = leer(os.path.join(P, 'assets', 'js', 'inscripcion.js'))

d = Doc('Guía paso a paso: componentes, utilidades y tema de Bootstrap',
        'Guía paso a paso · Sesión 14: componentes y tema de Bootstrap',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 14',
        'La página Cursos pasa a componentes de Bootstrap (tarjetas, aviso, acordeón y ventana modal), se arma con '
        'utilidades y toma los colores, la letra y los radios de tu Figma.')

d.callout('Vienes de la sesión 13:', 'necesitas `cursos.html` con Bootstrap enlazado y la grilla funcionando. Hoy el '
          'HTML de la página crece y `cursos.css` se achica: de 189 líneas a 60.')

d.h3('Qué vas a hacer')
d.tabla(['Archivo', 'Qué cambia hoy', 'En Figma'], [
    ['cursos.html', 'Los iconos y el JavaScript de Bootstrap; tarjetas `card`, aviso `alert`, acordeón, ventana `modal` y utilidades', '`course-card` con sus variantes'],
    ['assets/css/tema-bootstrap.css (nuevo)', 'Las variables `--bs-*` con los colores, la letra y los radios de Figma', 'Las variables locales'],
    ['assets/css/cursos.css', 'Pierde las tarjetas, los pasos y el llamado: ahora son clases de Bootstrap', '—'],
    ['assets/js/inscripcion.js (nuevo, opcional)', 'Al abrir la ventana, el curso de la tarjeta queda elegido', '—'],
], anchos=['30%', '44%', '26%'])

d.h3('Cómo se reparte')
d.tabla(['Momento', 'Pasos', 'Qué practicas'], [
    ['En clase, juntos', '0 al 3', 'Iconos y JavaScript; utilidades; el tema; las tarjetas'],
    ['En clase, tú', '4 y 5', 'El aviso, el llamado y el acordeón de preguntas'],
    ['Tarea', '6 y 7', 'La ventana de inscripción con su formulario; validar y publicar'],
    ['En Figma', 'Guía de Figma', 'Las variables locales y el componente `course-card`'],
], anchos=['18%', '14%', '68%'])

d.h2('Antes de escribir: tres herramientas de Bootstrap')
d.tabla(['Herramienta', 'Qué es', 'Ejemplo'], [
    ['Utilidades', 'Clases de una sola propiedad: márgenes, colores, flex, bordes, sombras', '`mb-3` es `margin-bottom: 1rem`'],
    ['Componentes', 'Bloques de HTML con clases ya diseñadas; algunos necesitan JavaScript', '`card`, `alert`, `accordion`, `modal`'],
    ['Tema', 'Las variables `--bs-*` que usan las utilidades y los componentes', '`--bs-primary: #06B6C4`'],
], anchos=['20%', '48%', '32%'])
d.callout('Si no coinciden, manda Figma:', 'Bootstrap trae su propio azul (`#0D6EFD`), sus radios y su letra. El '
          'tema los cambia por los tuyos para que la página Cursos se vea como el resto del portafolio.')

d.h2('Paso 0 · Los iconos y el JavaScript')
d.p('En el `<head>`, después de Bootstrap, enlaza **Bootstrap Icons**, una colección de más de 2000 iconos que se '
    'usan como una letra. Después, la hoja del tema:')
d.code(html_entre(CU, '<!-- 0. Bootstrap 5.3.8 y sus iconos', 'href="assets/css/cursos.css" />'))
d.p('Al final del `<body>`, el JavaScript de Bootstrap. La versión **bundle** incluye Popper, la librería que '
    'coloca menús desplegables y globos de ayuda. Va al final para que el HTML ya exista cuando se ejecute:')
d.code(html_entre(CU, '<!-- El JavaScript de Bootstrap', '<script src="assets/js/inscripcion.js"></script>'))
d.p('Un icono se escribe con `<i>` y dos clases. Como es decorativo, `aria-hidden="true"` evita que el lector de '
    'pantalla lo anuncie:')
d.code('<i class="bi bi-code-slash fs-2 text-primary" aria-hidden="true"></i>')

d.h2('Paso 1 · Las utilidades')
d.p('Una utilidad aplica una sola propiedad. Se combinan en el HTML como piezas de construcción. Estas son las '
    'familias que usa la página:')
d.tabla(['Familia', 'Clases', 'Qué hacen'], [
    ['Espaciado', '`m-*` · `p-*` con `t`, `b`, `s`, `e`, `x`, `y` y un tamaño de 0 a 5', '`mb-3`: margen inferior de 1rem. `p-4`: relleno de 1.5rem. `px-2`: a izquierda y derecha'],
    ['Display y flex', '`d-flex` · `justify-content-between` · `align-items-center` · `gap-2`', 'Flexbox (sesión 10) sin escribir CSS'],
    ['Texto', '`text-center` · `fw-bold` · `fs-5` · `small`', 'Alineación, grosor y tamaño de la letra'],
    ['Color', '`text-primary` · `text-body-secondary` · `bg-white` · `text-bg-dark`', 'Color del texto y del fondo'],
    ['Bordes', '`border` · `border-top` · `border-4` · `border-primary` · `rounded-3`', 'Trazo y Radio de esquina'],
    ['Sombra y tamaño', '`shadow-sm` · `h-100` · `w-100`', 'Sombra suave; alto o ancho del 100 %'],
    ['Accesibilidad', '`visually-hidden`', 'Oculta un texto a la vista, pero el lector de pantalla lo lee'],
], anchos=['18%', '42%', '40%'])
d.p('Los tamaños de espaciado: `0` es 0, `1` es 4px, `2` es 8px, `3` es 16px, `4` es 24px y `5` es 48px. Como la '
    'grilla, las utilidades aceptan un punto de quiebre: `p-4 p-md-5` es 24px de relleno en el celular y 48px desde 768px.')
d.p('Reescribe la sección **Cómo trabajamos** solo con utilidades. Así queda cada paso:')
d.code(html_entre(CU, '<!-- SECCIÓN 3 · Figma: cursos-pasos', '</li>') + '\n          <!-- … tres pasos más … -->\n        </ol>\n      </section>')
d.callout('Las utilidades usan `!important`:', 'para que una clase como `mb-0` gane siempre, sin importar la '
          'especificidad. Por eso, si quieres cambiar algo que puso una utilidad, cambia la clase en el HTML.')
d.comprueba('borra el bloque 5 de `cursos.css` (`.pasos`, `.paso` y `.paso-num`). Los pasos se ven igual que antes, '
            'con un icono en lugar del número.')

d.h2('Paso 2 · El tema: Bootstrap con tus colores (tema-bootstrap.css)')
d.p('Bootstrap guarda sus colores, su letra y sus radios en variables de CSS que empiezan por `--bs-`. Si cambias su '
    'valor, cambian todas las utilidades y los componentes que las usan. Crea `assets/css/tema-bootstrap.css` y '
    'enlázalo **justo después** de Bootstrap.')
d.h3('2.1 · Las variables globales')
d.code(T['1'], corto=False)
d.p('`--bs-primary-rgb` repite el color en números porque las utilidades le añaden una opacidad: '
    '`rgba(var(--bs-primary-rgb), 0.5)`. Si cambias una, cambia la otra.')
d.h3('2.2 · Las variables de cada componente')
d.p('Algunos componentes tienen variables propias, definidas en su clase. Se cambian en esa misma clase:')
d.code(T['2'], corto=False)
d.h3('2.3 · Lo que no tiene variable')
d.p('Unas pocas reglas de Bootstrap tienen el color escrito directamente. Esas se reemplazan con una regla igual:')
d.code(T['3'])
d.comprueba('los botones `btn-primary` y el borde de las cifras se ven en el cian de Figma, no en el azul de Bootstrap.')

d.h2('Paso 3 · Las tarjetas: el componente card')
d.p('Cambia cada `article.curso` de la sesión 13 por el componente **card**. La grilla no cambia:')
d.code(html_entre(CU, '<!-- SECCIÓN 2 · Figma: cursos-grid', '</article>\n          </div>'), corto=False)
d.tabla(['Clase', 'Qué hace'], [
    ['`card`', 'La tarjeta: fondo blanco, borde y radio (12px, por el tema)'],
    ['`card-body` · `card-footer`', 'El cuerpo con relleno y el pie con una línea encima'],
    ['`card-title` · `card-text`', 'El título y el texto, con los márgenes de Bootstrap'],
    ['`h-100`', 'Alto del 100 %: todas las tarjetas de una fila miden lo mismo'],
    ['`badge rounded-pill`', 'La insignia del nivel. `bg-primary-subtle text-primary-emphasis`: fondo suave y texto oscuro'],
    ['`btn btn-primary btn-sm`', 'Botón principal, pequeño. Abre la ventana de inscripción (Paso 6)'],
], anchos=['32%', '68%'])
d.callout('Seis botones «Inscribirme»:', 'para un lector de pantalla, seis botones iguales no se distinguen. El '
          '`span` con `visually-hidden` completa el nombre: «Inscribirme en Diseño Web».')
d.p('Borra el bloque 4 de `cursos.css` (`.curso`, `.curso-nivel` y `.curso-meta`). Lo que queda en el archivo es lo que Bootstrap no trae: la caja central, el tamaño de los títulos, la letra de '
    'las cifras y el movimiento de las tarjetas (sesión 11):')
d.code(K['4'])

d.h2('Paso 4 · El aviso, las cifras y el llamado')
d.p('El componente **alert** destaca un mensaje. Va al inicio de `<main>`:')
d.code(html_entre(CU, '<!-- Componente alert', '</div>'))
d.p('La tarjeta de cifras también pasa a `card`. Las utilidades `border-top border-4 border-primary` dibujan la línea '
    'de arriba que antes escribías en CSS:')
d.code(html_entre(CU, '<aside class="card', '</aside>'))
d.p('Del bloque 3 de `cursos.css` solo queda la letra del número; el párrafo de la presentación usa `fs-5 mb-0` en '
    'lugar de `.cursos-intro p`:')
d.code(K['3'])
d.p('Borra el bloque 6 (`.llamado`): el llamado final ya no necesita CSS propio. `text-bg-dark` pone el fondo oscuro de Figma (por `--bs-dark-rgb`) '
    'con texto claro, y `btn-lg` agranda el botón:')
d.code(html_entre(CU, '<!-- SECCIÓN 5 · Figma: cursos-llamado', '</section>'))

d.h2('Paso 5 · El acordeón de preguntas frecuentes')
d.p('Un **acordeón** muestra una respuesta a la vez. Funciona con el JavaScript de Bootstrap y con atributos '
    '`data-bs-*`, sin escribir código. Así es cada pregunta:')
d.code(html_entre(CU, '<div class="accordion-item">', '</div>\n          </div>'), corto=False)
d.tabla(['Atributo o clase', 'Qué hace'], [
    ['`data-bs-toggle="collapse"`', 'El botón abre y cierra un bloque'],
    ['`data-bs-target="#faq-1"`', 'Cuál: el que tiene `id="faq-1"`. Lleva `#`, como un selector'],
    ['`collapse show`', 'El bloque se puede plegar; `show` lo deja abierto al cargar'],
    ['`data-bs-parent="#faq"`', 'Al abrir uno, cierra los demás del mismo acordeón'],
    ['`aria-expanded` · `aria-controls`', 'Le dicen al lector de pantalla si está abierto y qué controla. Bootstrap los actualiza'],
], anchos=['36%', '64%'])
d.comprueba('al hacer clic en la segunda pregunta, se abre su respuesta y se cierra la primera. Con el teclado, `Tab` '
            'llega a cada pregunta y `Enter` la abre.')

d.h2('Paso 6 · La ventana de inscripción: el componente modal')
d.p('Una ventana **modal** aparece sobre la página y oscurece el fondo. Se escribe al final de `<body>`, fuera de '
    '`<main>`, y queda oculta hasta que un botón la abre. El botón de cada tarjeta la llama así:')
d.code('<button type="button" class="btn btn-primary btn-sm"\n        data-bs-toggle="modal" data-bs-target="#inscripcion" data-curso="Git y GitHub">')
d.p('Y esta es la ventana, con un formulario hecho con las clases de Bootstrap:')
d.code(html_entre(CU, '<div class="modal fade" id="inscripcion"', '<div class="mb-3">', incluir_hasta=False) +
       '''              <div class="mb-3">
                <label for="ins-nombre" class="form-label">Nombre completo</label>
                <input type="text" class="form-control" id="ins-nombre" name="nombre" autocomplete="name" required />
              </div>
              <!-- … correo (form-control), curso (form-select) y modalidad (form-check) … -->
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cancelar</button>
              <button type="submit" class="btn btn-primary">Enviar inscripción</button>
            </div>
          </form>
        </div>
      </div>
    </div>''', corto=False)
d.tabla(['Clase o atributo', 'Qué hace'], [
    ['`modal fade`', 'La ventana, con una transición de opacidad al abrir y cerrar'],
    ['`modal-dialog-centered`', 'La centra en vertical'],
    ['`data-bs-dismiss="modal"`', 'El botón cierra la ventana. También se cierra con `Esc` o con un clic en el fondo'],
    ['`role="dialog"` · `aria-labelledby`', 'Le dicen al lector de pantalla que es una ventana y que su nombre es el título'],
    ['`form-label` · `form-control` · `form-select`', 'Etiquetas, campos y listas con el estilo de Bootstrap'],
    ['`form-check` · `form-check-inline`', 'Botones de opción y casillas, uno junto al otro'],
], anchos=['40%', '60%'])
d.h3('6.1 · Opcional: el curso elegido')
d.p('Con un poco de JavaScript, el curso de la tarjeta queda elegido en el formulario. Bootstrap lanza el evento '
    '`show.bs.modal` al abrir la ventana y le pasa el botón que la abrió. Crea `assets/js/inscripcion.js`:')
d.code(JS)
d.comprueba('al pulsar «Inscribirme» en Git y GitHub, la ventana se abre con ese curso elegido. `Esc` la cierra.')

d.h2('Paso 7 · Validación, teclado y publicación')
d.pasos(['Valida `cursos.html` en **validator.w3.org** y tus hojas, incluida `tema-bootstrap.css`, en **jigsaw.w3.org/css-validator**.',
         'Recorre la página solo con el teclado: `Tab` hasta un botón «Inscribirme», `Enter` para abrir, `Tab` por los campos y `Esc` para cerrar.',
         'Revisa la página a 390, 820 y 1440 px.',
         'Publica en Netlify. El JavaScript y los iconos llegan desde el CDN: si no se ven, revisa los enlaces y su `integrity`.'])

d.h2('Ampliación: la barra de navegación de Bootstrap')
d.p('Tu portafolio conserva su propia cabecera. Para un proyecto nuevo, el componente **navbar** trae el menú '
    'que se pliega en un botón de tres rayas (hamburguesa) en el celular:')
d.code('''<nav class="navbar navbar-expand-lg bg-white border-bottom">
  <div class="container">
    <a class="navbar-brand fw-bold" href="index.html">Mi sitio</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
            data-bs-target="#menu" aria-controls="menu" aria-expanded="false"
            aria-label="Abrir el menú">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="menu">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link active" aria-current="page" href="index.html">Inicio</a></li>
        <li class="nav-item"><a class="nav-link" href="cursos.html">Cursos</a></li>
      </ul>
    </div>
  </div>
</nav>''')
d.p('`navbar-expand-lg` muestra el menú completo desde 992px; por debajo, solo el botón. `ms-auto` empuja la lista a '
    'la derecha, como el Espacio Auto de Figma.')

d.h2('Lista de comprobación')
d.check(['Los iconos y el JavaScript de Bootstrap están enlazados, con `integrity` y `crossorigin`.',
         '`tema-bootstrap.css` va justo después de Bootstrap y antes de `global.css`.',
         'Los botones, los bordes y las insignias usan el cian de Figma.',
         'Las seis tarjetas son `card` con `h-100` y su botón tiene un texto `visually-hidden`.',
         'El acordeón abre una pregunta a la vez.',
         'La ventana de inscripción se abre, se cierra con `Esc` y su formulario usa las clases `form-*`.',
         '`cursos.css` ya no tiene reglas para tarjetas, pasos ni el llamado.',
         'El HTML y tus hojas pasan los validadores del W3C sin errores.'])

d.h2('Errores frecuentes en esta sesión')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['La ventana o el acordeón no se abren', 'Falta el JavaScript de Bootstrap al final del `body`, o `data-bs-target` no lleva `#` o no coincide con el `id`'],
    ['Se abren varias preguntas a la vez', 'Falta `data-bs-parent="#faq"` en cada bloque `accordion-collapse`'],
    ['Los iconos se ven como cuadros', 'Falta el enlace de Bootstrap Icons o el nombre del icono está mal escrito'],
    ['Los botones siguen azules', '`tema-bootstrap.css` está enlazado antes que Bootstrap, o falta la regla `.btn-primary` del tema'],
    ['Una utilidad no hace nada', 'El nombre está mal (`mb3` sin guion) o el tamaño no existe: van de 0 a 5'],
    ['Cambié el CSS y la utilidad sigue ganando', 'Las utilidades usan `!important`: cambia la clase en el HTML'],
    ['La ventana aparece detrás de la cabecera', 'La cabecera tiene un `z-index` mayor que 1050. El de tu portafolio es 100'],
], anchos=['36%', '64%'])

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Sesion14_Componentes_Utilidades_y_Tema_de_Bootstrap.html'))
print('ok')
