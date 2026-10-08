# -*- coding: utf-8 -*-
"""Guía de Figma · Sesión 10: Pasos 12 al 14 (Contacto, pie de página e imágenes)."""
import os
from guia import Doc
from figma_comun import (donde_estas, como_leer, seccion_base, marco_envoltorio, texto_bloque, esquema)

d = Doc('Guía de Figma · Sesión 10: Contacto, pie de página e imágenes',
        'Guía de Figma · Sesión 10',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Pasos 12 al 14 del manual',
        'Terminas la página: la sección Contacto, el pie de página y las dos imágenes de los proyectos.')

donde_estas(d, 'Sesión 10')
como_leer(d)

d.h2('Antes de seguir · Revisa Sobre mí y Proyectos', salto=True)
d.tabla(['Capa', 'Debe tener'], [
    ['`about-section` y `projects-section`', 'Dentro de `mi-portafolio`, debajo de `hero-section`. W **Llenar el contenedor**, Espaciado `80` y `100`, Espacio `48`, Relleno `FFFFFF` al `100`'],
    ['`about-content`', 'Flujo horizontal, Espacio `64`, alineación al centro. Dentro, `about-text` en Llenar el contenedor y `about-graphic`'],
    ['`about-graphic`', 'W **Ancho fijo** `480`, H **Altura fija** `264`, Radio de esquina `12`, Trazo `E5E7EB` y cuatro `tag-block`'],
    ['`projects-grid`', 'Flujo horizontal, W **Llenar el contenedor**, Espacio `24`'],
    ['`project-card` (× 2)', 'W **Llenar el contenedor**, H **Altura fija** `475`, Radio de esquina `12` y la casilla Recortar contenido marcada'],
    ['`project-image` (× 2)', 'W Llenar el contenedor, H `220`. Hoy recibe la imagen en el Paso 14'],
], negrita_primera=False, anchos=['30%', '70%'])
d.p('Si algo no coincide, corrígelo con la guía de Figma de la sesión 09 antes de continuar.')

d.h2('Lo que vas a construir hoy')
esquema(d, 's10')
d.callout('La sección Contacto empieza igual que las otras dos:', 'mismo Flujo, W y H, Espacio, Espaciado y Relleno. '
          'Si quieres ir más rápido, selecciona `projects-section`, duplícala con `Ctrl + D`, borra su contenido y '
          'cámbiale el nombre; después revisa su bloque de valores.')

# ---------------- Paso 12
d.h2('Paso 12 · La sección «Contacto» (contact-section)', salto=True)
d.pasos(['En Capas, haz clic en `mi-portafolio`.',
         'Presiona `F` y dibuja un marco en la zona vacía de `mi-portafolio`, debajo de `projects-section`.',
         'En Capas, haz doble clic sobre su nombre y escribe `contact-section`.',
         'Comprueba en Capas que `contact-section` tenga sangría bajo `mi-portafolio` y esté debajo de `projects-section`, a su mismo nivel. Si quedó dentro de otra capa o fuera, arrástralo ahí.',
         'Con `contact-section` seleccionado, presiona `Shift + A`.'])
seccion_base(d, 'contact-section', 'dentro de mi-portafolio, debajo de projects-section')

d.h3('12.1 · El lado izquierdo (contact-text)')
d.pasos(['Presiona `T`, haz clic en una zona vacía dentro de `contact-section` y escribe `Contacto`. Pulsa `Esc`.',
         'Presiona `T` otra vez y haz clic en otra zona vacía de `contact-section`, lejos del texto anterior.',
         'Escribe: `Puedes contactarme a través de los siguientes canales:` Pulsa `Esc`.',
         'En Capas, haz clic en el primer texto y, con Shift pulsado, en el segundo: quedan los dos seleccionados.',
         'Presiona `Shift + A`. Figma crea un marco nuevo que contiene los dos textos.',
         'En Capas, haz doble clic sobre el nombre de ese marco y escribe `contact-text`.'])
marco_envoltorio(d, 'contact-text', 'el marco nuevo, dentro de contact-section', 'v',
                 'Abre el menú y elige **Llenar el contenedor**', 'El punto de arriba a la izquierda', '`16` (sugerido)')
texto_bloque(d, 'Contacto', 'el título, dentro de contact-text', 'llenar',
             '`Outfit` (sugerido)', '`ExtraBold` (sugerido)', '`36` (sugerido)', '`0B0F19` (sugerido)')
texto_bloque(d, 'Puedes contactarme…', 'el texto, dentro de contact-text', 'llenar',
             '`Geist` (sugerido)', '`Regular` (sugerido)', '`16` (sugerido)', '`374151` (sugerido)', '`160%`, con el signo (sugerido)')

d.h3('12.2 · La tarjeta de contacto (contact-card)')
d.p('Tiene medida fija, así que se dibuja primero con `F`.')
d.pasos(['En Capas, haz clic en `contact-section`.',
         'Presiona `F` y dibuja un marco pequeño dentro de `contact-section`, en la franja vacía de abajo.',
         'En Capas, haz doble clic sobre su nombre y escribe `contact-card`.',
         'Comprueba en Capas que `contact-card` tenga sangría bajo `contact-section` y esté debajo de `contact-text`. Si quedó fuera, arrástralo ahí.',
         'Con `contact-card` seleccionado, presiona `Shift + A`.'])
d.capa('contact-card', 'dentro de contact-section', [
    ('Disposición automática', [('Flujo', 'Horizontal: el tercer icono, con la flecha →'), ('W (ancho)', '**Ancho fijo** `520`'),
                                ('H (alto)', '**Altura fija** `84`'), ('Alineación', 'El punto central de la columna izquierda'),
                                ('Espacio', '`16`'), ('Espaciado › campo izquierdo', '`20` (horizontal)'),
                                ('Espaciado › campo derecho', '`20` (vertical)')]),
    ('Apariencia', [('Opacidad', '`100%`'), ('Radio de esquina', '`8`')]),
    ('Relleno', [('Color', '`FFFFFF`'), ('Porcentaje', '`100`')]),
    ('Trazo', [('Color', '`E5E7EB`'), ('Porcentaje', '`100`'), ('Peso', '`1`')]),
])
d.pasos(['Presiona `O` y dibuja un círculo pequeño dentro de `contact-card`. Será el icono.'])
d.capa('Ellipse 1', 'el icono; en Capas puede llamarse Elipse 1', [
    ('Disposición', [('W (ancho)', '`44` (sugerido)'), ('H (alto)', '`44` (sugerido)')]),
    ('Relleno', [('Color', '`06B6C4` (sugerido)'), ('Porcentaje', '`100`')]),
    ('Apariencia', [('Opacidad', '`100%`')]),
])
d.pasos(['Presiona `T`, haz clic dentro de `contact-card`, a la derecha del círculo, y escribe `dchuman@uss.edu.pe`. Pulsa `Esc`.'])
texto_bloque(d, 'dchuman@uss.edu.pe', 'el texto, dentro de contact-card', 'auto',
             '`Geist` (sugerido)', '`Medium` (sugerido)', '`16` (sugerido)', '`0B0F19` (sugerido)')
d.callout('Si prefieres iconos reales:', 'reemplaza el círculo por un icono de un plugin de iconos. El manual solo pide '
          '«un icono a la izquierda». En tu página web, el círculo lleva una letra: `@`, `in` o `GH`.')

d.h3('12.3 · La lista de tarjetas (contact-list)')
d.pasos(['En Capas, haz clic en `contact-card`.',
         'Presiona `Shift + A`. Figma crea un marco nuevo que lo envuelve.',
         'En Capas, haz doble clic sobre el nombre de ese marco y escribe `contact-list`.'])
marco_envoltorio(d, 'contact-list', 'el marco nuevo, dentro de contact-section', 'v',
                 '**Ancho fijo** `520`', 'El punto de arriba a la izquierda', '`16`')
d.pasos(['En Capas, haz clic en `contact-card` y duplícala dos veces con `Ctrl + D`: necesitas tres. Las copias aparecen debajo, dentro de `contact-list`.',
         'Haz doble clic sobre el texto de la segunda y cámbialo a `linkedin.com/in/dagnerchuman`.',
         'Haz doble clic sobre el texto de la tercera y cámbialo a `github.com/dagnerchuman`.'])

d.h3('12.4 · Junta los dos lados (contact-content)')
d.pasos(['En Capas, haz clic en `contact-text` y, con Shift pulsado, en `contact-list`: quedan los dos seleccionados.',
         'Presiona `Shift + A`. Figma crea un marco nuevo que contiene a los dos.',
         'En Capas, haz doble clic sobre el nombre de ese marco y escribe `contact-content`.'])
marco_envoltorio(d, 'contact-content', 'el marco nuevo, dentro de contact-section', 'h',
                 'Abre el menú y elige **Llenar el contenedor**', 'El punto de arriba a la izquierda', '`64`')
d.pasos(['En Capas, haz clic en `contact-text` y comprueba que su campo W siga en **Llenar el contenedor**. Si cambió, vuelve a elegirlo.'])
d.comprueba('el título y el texto quedan a la izquierda. A la derecha, las tres filas miden 520 × 84 y están separadas por 16.')

# ---------------- Paso 13
d.h2('Paso 13 · El pie de página (footer-wrapper)', salto=True)
d.p('Tiene altura fija, así que se dibuja primero con `F`.')
d.pasos(['En Capas, haz clic en `mi-portafolio`.',
         'Presiona `F` y dibuja un marco en la zona vacía de `mi-portafolio`, debajo de `contact-section`.',
         'En Capas, haz doble clic sobre su nombre y escribe `footer-wrapper`.',
         'Comprueba en Capas que `footer-wrapper` tenga sangría bajo `mi-portafolio` y esté debajo de `contact-section`, a su mismo nivel. Si quedó dentro de otra capa o fuera, arrástralo ahí.',
         'Con `footer-wrapper` seleccionado, presiona `Shift + A`.'])
d.capa('footer-wrapper', 'dentro de mi-portafolio, al final', [
    ('Disposición automática', [('Flujo', 'Vertical: el segundo icono, con la flecha ↓'),
                                ('W (ancho)', 'Abre el menú y elige **Llenar el contenedor**'),
                                ('H (alto)', '**Altura fija** `182`'), ('Alineación', 'El punto del centro'),
                                ('Espacio', '`24`'), ('Espaciado › campo izquierdo', '`80` (horizontal)'),
                                ('Espaciado › campo derecho', '`48` (vertical)')]),
    ('Apariencia', [('Opacidad', '`100%`')]),
    ('Relleno', [('Color', '`FFFFFF`'), ('Porcentaje', '`100`')]),
    ('Trazo', [('Color', '`E5E7EB`'), ('Porcentaje', '`100`'), ('Peso', '`1`'),
               ('Lados', 'Pulsa el último icono de la fila de Peso (un cuadrado) y elige **Superior**')]),
])
d.pasos(['Presiona `T`, haz clic dentro de `footer-wrapper` y escribe: `© 2026 Dagner Chuman | Centro de Informática USS Protech XP.` Pulsa `Esc`.'])
texto_bloque(d, '© 2026 Dagner Chuman…', 'el texto, dentro de footer-wrapper', 'auto',
             '`Geist`', '`Regular`', '`13`', '`374151`', alineacion='Centrado: el segundo icono')
d.callout('Para que coincida con tu HTML:', 'el pie de tus páginas tiene, encima de ese texto, una fila con los enlaces '
          'Inicio, Sobre mí, Proyectos y Contacto. Si quieres reflejarlo, escribe los cuatro textos dentro de '
          '`footer-wrapper` (Geist Regular de 13, Relleno `374151` al 100), selecciónalos y presiona `Shift + A`. Al marco '
          'nuevo ponle Flujo horizontal y Espacio 24. En Capas, déjalo arriba del texto del pie.')
d.comprueba('el pie ocupa todo el ancho, mide 182 de alto y solo tiene línea en el borde de arriba.')

# ---------------- Paso 14
d.h2('Paso 14 · Imágenes y recursos')
d.p('En todo el diseño del manual solo hay dos imágenes: las de las dos tarjetas de proyectos. La tarjeta de código y el '
    'gráfico de etiquetas se construyen con marcos y texto.')
d.pasos(['En Capas, haz clic en `project-image`, el rectángulo de la primera tarjeta.',
         'En el panel derecho, sección **Relleno**, haz clic en el recuadro de color.',
         'En la ventana que se abre, cambia el tipo de **Sólido** a **Imagen**.',
         'Pulsa **Elegir imagen** y sube la captura de tu proyecto.',
         'Elige el modo **Llenar** o **Recortar** para ajustarla.',
         'Cierra la ventana y comprueba que en Relleno el porcentaje siga en `100`.',
         'Repite con el `project-image` de la segunda tarjeta.'])
d.p('Para reemplazar una imagen más adelante: selecciona el rectángulo, abre Relleno, haz clic en la miniatura de la imagen y pulsa de nuevo **Elegir imagen**.')
d.callout('Si todavía no tienes capturas:', 'usa las dos imágenes de ejemplo de la carpeta resuelta de la sesión 10 '
          '(`assets/img/proyecto-cinf.jpg` y `assets/img/proyecto-certificados.jpg`, de 1256 × 440: el doble de 628 × 220), '
          'o deja los rectángulos con el Relleno `E5E7EB` al 100 y coloca las imágenes cuando tengas tus proyectos.')
d.callout('El modo Llenar también existe en CSS:', 'se escribe `object-fit: cover`. La imagen cubre toda la caja sin '
          'deformarse y lo que sobra se recorta. Lo usarás hoy en la guía de código.')

d.h2('Revisión final de la página')
d.p('`mi-portafolio` tiene Altura fija 2816. Con todas las secciones dentro, puede sobrar un hueco al final o quedar el pie recortado. Para comprobarlo:')
d.pasos(['En Capas, haz clic en `mi-portafolio`.',
         'En Disposición automática, abre el menú del campo H y elige **Ajustar al contenido**. El marco toma la altura real de tu diseño.',
         'Si esa altura queda cerca de 2816, vuelve a **Altura fija** y escribe `2816`.',
         'Si es muy distinta, revisa el Espaciado de cada sección (80 y 100) y las alturas fijas: tarjetas de 475, `hero-right` de 404 y pie de 182.'])

d.h2('Así deben quedar tus capas', salto=True)
d.code('''mi-portafolio
├── Encabezado
├── hero-section
│   ├── hero-left
│   └── hero-right
├── about-section
│   ├── Sobre mí
│   └── about-content
│       ├── about-text
│       └── about-graphic
│           └── tag-block (× 4)
├── projects-section
│   ├── Proyectos
│   └── projects-grid
│       ├── project-card
│       │   ├── project-image                  ← imagen del Paso 14
│       │   └── project-text
│       └── project-card
├── contact-section                            ← Paso 12
│   └── contact-content
│       ├── contact-text
│       └── contact-list
│           ├── contact-card
│           ├── contact-card
│           └── contact-card
└── footer-wrapper                             ← Paso 13''')
d.p('El manual nombra `about-section`, `projects-section`, `projects-grid`, `contact-section` y `footer-wrapper`. Los '
    'demás nombres son una propuesta, y en tu código de la sesión 10 son clases con el mismo nombre:')
d.tabla(['Marco en Figma', 'En tu CSS', 'Con qué se maqueta'], [
    ['`hero-section`, `hero-left`', '`.hero-section`, `.hero-left`', 'Flexbox: fila y columna'],
    ['`about-content`', '`.about-content`', 'Flexbox: dos columnas, una de 480'],
    ['`projects-grid`', '`.projects-grid`', 'Grid: dos columnas de `1fr`'],
    ['`project-card`, `project-image`', '`.project-card`, `.project-image`', '`overflow: hidden` y `object-fit: cover`'],
    ['`contact-content`, `contact-list`', '`.contact-content`, `.contact-list`', 'Flexbox: fila y columna de 520'],
    ['`contact-card`', '`.contact-card`', 'Flexbox: icono y texto centrados'],
    ['`footer-wrapper`', '`footer`', 'Flexbox en columna'],
], negrita_primera=False, anchos=['34%', '34%', '32%'])

d.h2('Ampliación: lo que ya tiene tu HTML')
d.p('Estos dos elementos no están en el manual. Añádelos si quieres que tu diseño refleje tu página web:')
d.lista(['**Formulario, dentro de `contact-section`:** un marco con Flujo vertical y Espacio 16. Cada campo es un marco con '
         'W en Llenar el contenedor, Espaciado 16 y 12, Radio de esquina 8, Relleno `FFFFFF` al 100 y Trazo `E5E7EB`; '
         'encima, su etiqueta en Geist Medium de 14. Al final, un botón igual a `btn-primary` con el texto `Enviar mensaje`.',
         '**Video, dentro de `about-section`:** un rectángulo de 315 × 560 con Radio de esquina 12. En Relleno, cambia de '
         'Sólido a Imagen y elige tu `poster-presentacion.jpg`.'])

d.h2('Lista de comprobación')
d.check(['Las tres secciones tienen W en Llenar el contenedor, Espaciado 80 y 100, Espacio 48 y Relleno `FFFFFF` al 100.',
         'Los tres títulos de sección usan Outfit ExtraBold de 36.',
         'Las tres filas de contacto miden 520 × 84, con Radio de esquina 8 y Espacio 16 entre ellas.',
         'El pie mide 182 de alto y solo tiene Trazo en el borde superior.',
         'Las dos tarjetas de proyecto tienen su imagen en Relleno de tipo Imagen, al 100.',
         'Todos los rellenos y trazos están al 100 y ninguna capa tiene la Opacidad por debajo de 100%.',
         'Todas las capas están dentro de `mi-portafolio`, en el orden de la lista de capas.'])

d.h2('Errores frecuentes en Figma')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['Las tres filas de contacto quedan en horizontal', 'A `contact-list` le falta el Flujo vertical: el segundo icono, con la flecha ↓'],
    ['El círculo del icono se deforma', 'Su W y su H son distintos. Escribe `44` en los dos'],
    ['El texto de una fila de contacto se corta', 'La fila tiene Ancho fijo 520: el texto no cabe. Revisa que esté en Ajuste automático de ancho y que no tenga saltos de línea'],
    ['El pie tiene línea en los cuatro bordes', 'En Trazo, pulsa el último icono de la fila de Peso (un cuadrado) y elige solo Superior'],
    ['La imagen deja franjas vacías o se repite', 'En la ventana de Relleno, el modo está en Ajustar o en Mosaico. Elige Llenar'],
    ['Una sección nueva aparece dentro de otra', 'La soltaste dentro de la sección anterior. En Capas, arrástrala hasta que quede al nivel de `hero-section`'],
    ['Queda un hueco al final de la página', 'Las secciones suman menos que la altura fija del marco. Sigue la «Revisión final de la página»'],
], anchos=['36%', '64%'])
d.callout('Tu diseño está completo:', 'cada medida que escribiste en Figma tiene su propiedad en CSS. La guía de código '
          'de esta sesión los convierte en Flexbox y Grid, marco por marco.')

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Figma_Sesion10_Pasos_12_al_14.html'))
print('ok')
