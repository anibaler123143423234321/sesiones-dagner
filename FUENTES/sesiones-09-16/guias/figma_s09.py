# -*- coding: utf-8 -*-
"""Guía de Figma · Sesión 09: Pasos 10 y 11 (Sobre mí y Proyectos)."""
import os
from guia import Doc
from figma_comun import (donde_estas, como_leer, seccion_base, titulo_seccion,
                         marco_envoltorio, texto_bloque, esquema)

d = Doc('Guía de Figma · Sesión 09: las secciones Sobre mí y Proyectos',
        'Guía de Figma · Sesión 09',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Pasos 10 y 11 del manual',
        'Empiezas la segunda mitad de la página: la sección Sobre mí, con su texto y su gráfico, y la cuadrícula de Proyectos.')

d.callout('Un reparto nuevo por el feriado:', 'los Pasos 10 al 14 estaban previstos para la sesión 08, que no se dictó. '
          'Ahora se reparten en dos días: los Pasos 10 y 11 hoy, y los Pasos 12, 13 y 14 en la sesión 10.')
donde_estas(d, 'Sesión 09')
como_leer(d)

d.h2('Antes de seguir · Revisa tu Hero', salto=True)
d.tabla(['Capa', 'Debe tener'], [
    ['`hero-left`', 'W **Ancho fijo** `696`, H **Ajustar al contenido**, Espacio `32` y la casilla Recortar contenido desmarcada'],
    ['`hero-actions`', 'Dentro de `hero-left`, debajo del párrafo. Espacio `16`'],
    ['`btn-primary` y `btn-secondary`', 'W y H en **Ajustar al contenido**, Espaciado `24` y `14`, Radio de esquina `8`. El primero mide 52 de alto; el segundo, 54 o 52'],
    ['`hero-right`', 'W **Ancho fijo** `520`, H **Altura fija** `404`, Radio de esquina `12`, Relleno `FFFFFF` al `100`, Trazo `E5E7EB` y la casilla Recortar contenido marcada'],
], negrita_primera=False, anchos=['30%', '70%'])
d.p('Si algo no coincide, corrígelo con la guía de Figma de la sesión 07 antes de continuar.')

d.h2('Lo que vas a construir hoy')
esquema(d, 's09')
d.callout('Las secciones empiezan igual:', '`about-section`, `projects-section` y, en la sesión 10, `contact-section` '
          'comparten Flujo, W y H, Espacio, Espaciado y Relleno. El bloque de valores es el mismo. Como tienen Espaciado, '
          'se dibujan primero con `F`: no se encogen aunque estén vacías.')

# ---------------- Paso 10
d.h2('Paso 10 · La sección «Sobre mí» (about-section)', salto=True)
d.pasos(['En Capas, haz clic en `mi-portafolio`.',
         'Presiona `F` y dibuja un marco en la zona vacía de `mi-portafolio`, debajo de `hero-section`.',
         'En Capas, haz doble clic sobre su nombre y escribe `about-section`.',
         'Comprueba en Capas que `about-section` tenga sangría bajo `mi-portafolio` y esté debajo de `hero-section`, a su mismo nivel. Si quedó dentro de otra capa o fuera, arrástralo ahí.',
         'Con `about-section` seleccionado, presiona `Shift + A`.'])
seccion_base(d, 'about-section', 'dentro de mi-portafolio, debajo de hero-section')

d.h3('10.1 · El título de la sección')
d.pasos(['Presiona `T`, haz clic dentro de `about-section` y escribe `Sobre mí`. Pulsa `Esc`.'])
titulo_seccion(d, 'Sobre mí', 'el título, dentro de about-section')

d.h3('10.2 · La columna izquierda (about-text)')
d.pasos(['Presiona `T` y haz clic en una zona vacía de `about-section`, debajo del título.',
         'Escribe, todo seguido: `Docente e Ingeniero enfocado en el desarrollo web y la formación tecnológica.` Pulsa `Esc`.',
         'Presiona `T` otra vez y haz clic en otra zona vacía de `about-section`, lejos de los otros textos.',
         'Escribe, todo seguido: `Desde mis primeros pasos en la informática, he estado fascinado por la capacidad de la tecnología para transformar ideas en realidad.` Pulsa `Esc`.',
         'En Capas, haz clic en el primero de esos dos textos y, con Shift pulsado, en el segundo: quedan los dos seleccionados. El título `Sobre mí` no debe quedar seleccionado.',
         'Presiona `Shift + A`. Figma crea un marco nuevo que contiene los dos textos.',
         'En Capas, haz doble clic sobre el nombre de ese marco y escribe `about-text`.'])
marco_envoltorio(d, 'about-text', 'el marco nuevo, dentro de about-section', 'v',
                 'Abre el menú y elige **Llenar el contenedor**', 'El punto de arriba a la izquierda', '`16` (sugerido)')
texto_bloque(d, 'Docente e Ingeniero…', 'el título secundario, dentro de about-text', 'llenar',
             '`Outfit` (sugerido)', '`Bold` (sugerido)', '`22`', '`0B0F19`', '`160%`, con el signo')
texto_bloque(d, 'Desde mis primeros pasos…', 'el párrafo, dentro de about-text', 'llenar',
             '`Geist`', '`Regular`', '`16`', '`374151`', '`160%`, con el signo (sugerido)')

d.h3('10.3 · La columna derecha (about-graphic)')
d.p('Tiene medida fija, así que se dibuja primero con `F`.')
d.pasos(['En Capas, haz clic en `about-section`.',
         'Presiona `F` y dibuja un marco pequeño dentro de `about-section`, en la franja vacía de abajo.',
         'En Capas, haz doble clic sobre su nombre y escribe `about-graphic`.',
         'Comprueba en Capas que `about-graphic` tenga sangría bajo `about-section` y esté debajo de `about-text`. Si quedó fuera, arrástralo ahí.',
         'Con `about-graphic` seleccionado, presiona `Shift + A`.'])
d.capa('about-graphic', 'dentro de about-section', [
    ('Disposición automática', [('Flujo', 'Vertical: el segundo icono, con la flecha ↓'), ('W (ancho)', '**Ancho fijo** `480`'),
                                ('H (alto)', '**Altura fija** `264`'), ('Alineación', 'El punto de arriba a la izquierda'),
                                ('Espacio', '`16`'), ('Espaciado › campo izquierdo', '`24` (horizontal)'),
                                ('Espaciado › campo derecho', '`24` (vertical)')]),
    ('Apariencia', [('Opacidad', '`100%`'), ('Radio de esquina', '`12`')]),
    ('Relleno', [('Color', '`FFFFFF`'), ('Porcentaje', '`100`')]),
    ('Trazo', [('Color', '`E5E7EB`'), ('Porcentaje', '`100`'), ('Peso', '`1`')]),
])
d.p('Dentro van cuatro bloques que simulan etiquetas semánticas. Construye uno y duplícalo:')
d.pasos(['En Capas, haz clic en `about-graphic`.',
         'Presiona `F` y dibuja un marco dentro de `about-graphic`.',
         'En Capas, haz doble clic sobre su nombre y escribe `tag-block`. Comprueba que tenga sangría bajo `about-graphic`.',
         'Con `tag-block` seleccionado, presiona `Shift + A`.'])
d.capa('tag-block', 'el primer bloque, dentro de about-graphic', [
    ('Disposición automática', [('Flujo', 'Horizontal: el tercer icono, con la flecha →'),
                                ('W (ancho)', 'Abre el menú y elige **Llenar el contenedor** (sugerido)'),
                                ('H (alto)', '**Llenar el contenedor** (sugerido)'),
                                ('Alineación', 'El punto central de la columna izquierda'),
                                ('Espaciado › campo izquierdo', '`12` (horizontal) (sugerido)'),
                                ('Espaciado › campo derecho', '`0` (vertical) (sugerido)'),
                                ('Recortar contenido', 'Casilla desmarcada')]),
    ('Apariencia', [('Opacidad', '`100%`'), ('Radio de esquina', '`8` (sugerido)')]),
    ('Relleno', [('Color', '`F9FAFB` (sugerido)'), ('Porcentaje', '`100`')]),
    ('Trazo', [('Color', '`E5E7EB` (sugerido)'), ('Porcentaje', '`100`'), ('Peso', '`1`')]),
])
d.pasos(['Presiona `T`, haz clic dentro de `tag-block` y escribe `<header>`. Pulsa `Esc`.'])
texto_bloque(d, '<header>', 'el texto, dentro de tag-block', 'auto', '`Geist Mono`', '`Regular`', '`14` (sugerido)', '`374151` (sugerido)')
d.pasos(['En Capas, haz clic en `tag-block` y duplícalo tres veces con `Ctrl + D`: necesitas cuatro.',
         'Haz doble clic sobre el texto de cada copia y cámbialo a `<main>`, `<section>` y `<footer>`.'])

d.h3('10.4 · Junta las dos columnas (about-content)')
d.pasos(['En Capas, haz clic en `about-text` y, con Shift pulsado, en `about-graphic`: quedan los dos seleccionados.',
         'Presiona `Shift + A`. Figma crea un marco nuevo que contiene a los dos.',
         'En Capas, haz doble clic sobre el nombre de ese marco y escribe `about-content`.'])
marco_envoltorio(d, 'about-content', 'el marco nuevo, dentro de about-section', 'h',
                 'Abre el menú y elige **Llenar el contenedor**', 'El punto central de la columna izquierda', '`64`')
d.pasos(['En Capas, haz clic en `about-text` y comprueba que su campo W siga en **Llenar el contenedor**. Si cambió, vuelve a elegirlo.'])
d.comprueba('la sección ocupa todo el ancho y tiene fondo blanco. El texto queda a la izquierda y el gráfico de 480 × 264 '
            'a la derecha, centrado en vertical, con sus cuatro bloques del mismo alto.')

# ---------------- Paso 11
d.h2('Paso 11 · La sección «Proyectos» (projects-section)', salto=True)
d.pasos(['En Capas, haz clic en `mi-portafolio`.',
         'Presiona `F` y dibuja un marco en la zona vacía de `mi-portafolio`, debajo de `about-section`.',
         'En Capas, haz doble clic sobre su nombre y escribe `projects-section`.',
         'Comprueba en Capas que `projects-section` tenga sangría bajo `mi-portafolio` y esté debajo de `about-section`, a su mismo nivel. Si quedó dentro de otra capa o fuera, arrástralo ahí.',
         'Con `projects-section` seleccionado, presiona `Shift + A`.'])
seccion_base(d, 'projects-section', 'dentro de mi-portafolio, debajo de about-section')
d.pasos(['Presiona `T`, haz clic dentro de `projects-section` y escribe `Proyectos`. Pulsa `Esc`.'])
titulo_seccion(d, 'Proyectos', 'el título, dentro de projects-section')

d.h3('11.1 · La tarjeta (project-card)')
d.p('Tiene altura fija, así que se dibuja primero con `F`.')
d.pasos(['En Capas, haz clic en `projects-section`.',
         'Presiona `F` y dibuja un marco pequeño dentro de `projects-section`, en la franja vacía de abajo.',
         'En Capas, haz doble clic sobre su nombre y escribe `project-card`.',
         'Comprueba en Capas que `project-card` tenga sangría bajo `projects-section` y esté debajo del título. Si quedó fuera, arrástralo ahí.',
         'Con `project-card` seleccionado, presiona `Shift + A`.'])
d.capa('project-card', 'dentro de projects-section', [
    ('Disposición automática', [('Flujo', 'Vertical: el segundo icono, con la flecha ↓'),
                                ('W (ancho)', 'Abre el menú y elige **Llenar el contenedor**'),
                                ('H (alto)', '**Altura fija** `475`'), ('Alineación', 'El punto de arriba a la izquierda'),
                                ('Espacio', '`0`'), ('Espaciado › campo izquierdo', '`0`'), ('Espaciado › campo derecho', '`0`'),
                                ('Recortar contenido', 'Casilla **marcada**')]),
    ('Apariencia', [('Opacidad', '`100%`'), ('Radio de esquina', '`12`')]),
    ('Relleno', [('Color', '`FFFFFF`'), ('Porcentaje', '`100`')]),
    ('Trazo', [('Color', '`E5E7EB`'), ('Porcentaje', '`100`'), ('Peso', '`1`')]),
])

d.h3('11.2 · El área de la imagen (project-image)')
d.pasos(['Presiona `R` y dibuja un rectángulo dentro de `project-card`.',
         'En Capas, haz doble clic sobre su nombre y escribe `project-image`. Comprueba que tenga sangría bajo `project-card`.'])
d.capa('project-image', 'el rectángulo, dentro de project-card', [
    ('Disposición', [('W (ancho)', 'Abre el menú y elige **Llenar el contenedor**'), ('H (alto)', '`220`')]),
    ('Relleno', [('Color', '`E5E7EB` (sugerido)'), ('Porcentaje', '`100`')]),
    ('Apariencia', [('Opacidad', '`100%`')]),
])
d.p('El gris es provisional: la imagen se coloca en el Paso 14, en la sesión 10.')

d.h3('11.3 · El área de texto (project-text)')
d.pasos(['Presiona `T` y haz clic en una zona vacía de `project-card`, debajo del rectángulo.',
         'Escribe `Ecosistema CINF USS` y pulsa `Esc`.',
         'Presiona `T` otra vez y haz clic en otra zona vacía de `project-card`, lejos del texto anterior.',
         'Escribe, todo seguido: `Plataforma para la gestión académica y proyectos estudiantiles del Centro de Informática.` Pulsa `Esc`.',
         'En Capas, haz clic en el primero de esos dos textos y, con Shift pulsado, en el segundo. El rectángulo no debe quedar seleccionado.',
         'Presiona `Shift + A`. Figma crea un marco nuevo que contiene los dos textos.',
         'En Capas, haz doble clic sobre el nombre de ese marco y escribe `project-text`.'])
d.capa('project-text', 'el marco nuevo, dentro de project-card', [
    ('Disposición automática', [('Flujo', 'Vertical: el segundo icono, con la flecha ↓'),
                                ('W (ancho)', 'Abre el menú y elige **Llenar el contenedor**'),
                                ('H (alto)', '**Ajustar al contenido**'), ('Alineación', 'El punto de arriba a la izquierda'),
                                ('Espacio', '`8` (sugerido)'), ('Espaciado › campo izquierdo', '`24` (horizontal)'),
                                ('Espaciado › campo derecho', '`24` (vertical)')]),
    ('Apariencia', [('Opacidad', '`100%`')]),
    ('Relleno', [('Color', 'Ninguno: si hay uno, quítalo con −')]),
])
texto_bloque(d, 'Ecosistema CINF USS', 'el título, dentro de project-text', 'llenar', '`Outfit`', '`Bold`', '`24`', '`0B0F19`')
texto_bloque(d, 'Plataforma para la gestión…', 'la descripción, dentro de project-text', 'llenar',
             '`Geist`', '`Regular`', '`16`', '`374151`', '`160%`, con el signo (sugerido)')

d.h3('11.4 · La cuadrícula (projects-grid)')
d.pasos(['En Capas, haz clic en `project-card`.',
         'Presiona `Shift + A`. Figma crea un marco nuevo que lo envuelve.',
         'En Capas, haz doble clic sobre el nombre de ese marco y escribe `projects-grid`.'])
marco_envoltorio(d, 'projects-grid', 'el marco nuevo, dentro de projects-section', 'h',
                 'Abre el menú y elige **Llenar el contenedor**', 'El punto de arriba a la izquierda', '`24`')
d.pasos(['En Capas, haz clic en `project-card` y comprueba que su campo W siga en **Llenar el contenedor**. Si cambió, vuelve a elegirlo.'])

d.h3('11.5 · La segunda tarjeta')
d.pasos(['En Capas, haz clic en `project-card` y duplícala con `Ctrl + D`. La copia aparece a su derecha, dentro de `projects-grid`.',
         'En la copia, haz doble clic sobre el título y cámbialo a `Generador de Certificados Web`.',
         'Haz doble clic sobre la descripción y cámbiala a: `Aplicación para automatizar la emisión y validación de certificados digitales.`'])
d.comprueba('las dos tarjetas miden 628 × 475, tienen las esquinas redondeadas y el rectángulo de la imagen no sobresale por arriba.')
d.callout('De dónde sale el 628:', '`mi-portafolio` mide 1440 y la sección tiene 80 de Espaciado a cada lado: quedan 1280. '
          'Menos los 24 de Espacio entre tarjetas, 1256. Dividido entre dos, 628 por tarjeta.')

d.h2('Así deben quedar tus capas')
d.code('''mi-portafolio
├── Encabezado
├── hero-section
│   ├── hero-left
│   └── hero-right
├── about-section                              ← Paso 10
│   ├── Sobre mí
│   └── about-content
│       ├── about-text
│       └── about-graphic
│           └── tag-block (× 4)
└── projects-section                           ← Paso 11
    ├── Proyectos
    └── projects-grid
        ├── project-card
        │   ├── project-image
        │   └── project-text
        └── project-card''')
d.p('El manual nombra `about-section`, `projects-section` y `projects-grid`. Los demás nombres son una propuesta: en la '
    'sesión 10 los usarás como clases en tu CSS (`.about-content`, `.project-card`, `.project-image`, `.project-text`).')
d.callout('Tu entrega:', 'sigue trabajando en el archivo que dejaste en la carpeta de entregas de la clase en la sesión 07. '
          'El docente ve tu avance en el momento, sin que le envíes enlaces ni capturas.')

d.h2('Lista de comprobación')
d.check(['`about-section` y `projects-section` tienen W en Llenar el contenedor, Espaciado 80 y 100, Espacio 48 y Relleno `FFFFFF` al 100.',
         'Los dos títulos de sección usan Outfit ExtraBold de 36.',
         'El gráfico de «Sobre mí» mide 480 × 264, tiene Radio de esquina 12 y cuatro bloques del mismo alto.',
         'Las dos tarjetas de proyecto miden 628 × 475, con el rectángulo de 220 de alto arriba y Recortar contenido marcado.',
         'Todos los rellenos y trazos están al 100 y ninguna capa tiene la Opacidad por debajo de 100%.',
         'Todas las capas están dentro de `mi-portafolio`, en el orden de la lista de capas.'])

d.h2('Errores frecuentes en Figma')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['Un texto ocupa una altura enorme', 'La altura de línea quedó en píxeles. Escribe el valor con el signo: `160%`'],
    ['Un texto no se parte en líneas y se sale de su marco', 'Está en Ajuste automático de ancho, o se pegó con saltos de línea. En el campo W elige Llenar el contenedor y borra los saltos'],
    ['Una sección no ocupa todo el ancho', 'Su W está en Ancho fijo o en Ajustar al contenido. Cámbiala a Llenar el contenedor'],
    ['Una columna de texto quedó estrecha después de envolverla', 'Su W cambió al crear el marco que la contiene. Selecciónala y vuelve a elegir Llenar el contenedor'],
    ['La imagen sobresale de la tarjeta por las esquinas', 'Falta marcar Recortar contenido en `project-card`'],
    ['Una sección nueva aparece dentro de otra', 'La soltaste dentro de la sección anterior. En Capas, arrástrala hasta que quede al nivel de `hero-section`'],
    ['Un marco no se ve', 'En Relleno, el porcentaje está en 0 o el ojo está tachado. O su marco padre tiene Altura fija y Recortar contenido marcado, y lo está cortando'],
], anchos=['36%', '64%'])
d.callout('Lo que sigue:', 'en la sesión 10 terminas la página (Contacto, pie de página e imágenes) y, en el código, '
          'conviertes estos marcos en Flexbox y Grid: cada Disposición automática que hiciste hoy tiene su `display: flex`.')

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Figma_Sesion09_Pasos_10_y_11.html'))
print('ok')
