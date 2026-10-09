# -*- coding: utf-8 -*-
"""Guía de Figma · Sesión 13: la guía de 12 columnas y la página Cursos."""
import os
from guia import Doc
from figma_comun import asi_queda, donde_estas, como_leer, seccion_base, titulo_seccion, marco_envoltorio, texto_bloque

V = 'Vertical: el segundo icono, con la flecha ↓'
HZ = 'Horizontal: el tercer icono, con la flecha →'
LLENAR = 'Abre el menú y elige **Llenar el contenedor**'
AJUSTAR = '**Ajustar al contenido**'

d = Doc('Guía de Figma · Sesión 13: la guía de columnas y la página Cursos',
        'Guía de Figma · Sesión 13',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Ampliación del manual, después del Paso 14',
        'Pones sobre tu página una guía de 12 columnas, la misma grilla de Bootstrap, y diseñas con ella la página Cursos.')

donde_estas(d, 'Sesión 13')
d.callout('El manual termina en el Paso 14:', 'esta guía es una ampliación. Los valores salen de tu código de hoy: '
          '12 columnas, márgenes de 80 y un medianil de 24, como la clase `g-4` de Bootstrap.')
como_leer(d)

d.h2('Tres palabras nuevas', salto=True)
d.tabla(['En Figma', 'Qué es', 'En Bootstrap'], [
    ['Columnas (Columns)', 'Franjas verticales de color que se ven sobre el marco y no se exportan: solo sirven para alinear', 'Las 12 columnas de cada `.row`'],
    ['Medianil (Gutter)', 'La separación entre dos columnas', '`.g-4`: 24px'],
    ['Margen (Margin)', 'La distancia entre el borde del marco y la primera columna', 'El `padding` del contenedor: 80'],
], anchos=['24%', '50%', '26%'])
d.callout('Sobre el nombre de la sección:', 'en Figma se llama **Guía de diseño (Layout guide)**. En versiones anteriores se '
          'llamaba **Cuadrícula de diseño (Layout grid)**. Es la misma sección, en el panel derecho, debajo de Apariencia y Relleno.')

d.h3('Lo que vas a construir hoy')
d.code('''mi-portafolio            ← + guía de 12 columnas y el enlace Cursos en el menú
mi-portafolio-movil      ← + guía de 4 columnas y el enlace Cursos
mi-portafolio-cursos     ← marco nuevo: la página Cursos
├── Encabezado
├── cursos-intro         ← texto (7 columnas) y cifras (5 columnas)
├── catalogo-section     ← 6 tarjetas course-card, 3 por fila (4 columnas cada una)
├── pasos-section        ← 4 pasos (3 columnas cada uno)
├── llamado-section      ← un bloque de 8 columnas, centrado
└── footer-wrapper''')

# ---------------- Parte 1
d.h2('Parte 1 · La guía de 12 columnas en mi-portafolio', salto=True)
d.pasos(['En Capas, haz clic en `mi-portafolio`.',
         'En el panel derecho, busca la sección **Guía de diseño (Layout guide)** y pulsa **+**. Figma pone una cuadrícula de cuadros pequeños.',
         'Haz clic en el icono que está a la izquierda de su nombre: se abre la ventana de opciones.',
         'En el primer menú, cambia **Cuadrícula (Grid)** por **Columnas (Columns)** y escribe los valores del bloque siguiente.'])
d.capa('mi-portafolio', 'ventana de la Guía de diseño', [
    ('Columnas (Columns)', [('Cantidad (Count)', '`12`'), ('Color', '`FF0000`, porcentaje `10`: un rojo muy suave'),
                            ('Tipo (Type)', '**Estirar (Stretch)**: las columnas llenan el ancho entre los márgenes'),
                            ('Ancho (Width)', 'Automático: Figma lo calcula'),
                            ('Margen (Margin)', '`80`'), ('Medianil (Gutter)', '`24`')]),
])
d.p('Para mostrar u ocultar la guía: `Ctrl + Shift + 4` (en Mac, `Ctrl + G`). No se ve al presentar ni al exportar.')
d.comprueba('el borde izquierdo de `hero-left`, de los títulos de sección y del nombre en el `Encabezado` coincide con el '
            'borde de la primera columna roja. Cada columna mide unos 84.7.')

d.h3('1.1 · La guía de 4 columnas en el marco móvil')
d.p('Repite con `mi-portafolio-movil`. En un celular, Bootstrap usa una sola columna de ancho completo (`col-12`), '
    'así que bastan 4 columnas para alinear:')
d.capa('mi-portafolio-movil', 'ventana de la Guía de diseño', [
    ('Columnas (Columns)', [('Cantidad (Count)', '`4`'), ('Color', '`FF0000`, porcentaje `10`'),
                            ('Tipo (Type)', '**Estirar (Stretch)**'), ('Margen (Margin)', '`16`'), ('Medianil (Gutter)', '`24`')]),
])

d.h3('1.2 · El enlace Cursos en el menú')
d.pasos(['En `mi-portafolio`, abre `Encabezado` › `nav-links` y haz clic en el texto `Proyectos`.',
         'Presiona `Ctrl + D`. Aparece una copia junto a él, dentro de `nav-links`.',
         'Haz doble clic sobre la copia y escribe `Cursos`. Como es un duplicado, conserva la letra y el color.',
         'En Capas, comprueba que `Cursos` quede entre `Proyectos` y `Contacto`; si no, arrástralo.',
         'Repite en el `Encabezado` de `mi-portafolio-movil`.'])

# ---------------- Parte 2
d.h2('Parte 2 · El marco de la página Cursos', salto=True)
d.pasos(['En Capas, haz clic en `mi-portafolio` y presiona `Ctrl + D`. Arrastra la copia a un espacio libre del lienzo.',
         'Haz doble clic sobre su nombre y escribe `mi-portafolio-cursos`.',
         'Dentro de la copia, selecciona `hero-section`, `about-section`, `projects-section` y `contact-section` con Shift y presiona `Supr`. Quedan el `Encabezado` y `footer-wrapper`.',
         'Con `mi-portafolio-cursos` seleccionado, en Disposición automática, pon el campo H en **Ajustar al contenido**.'])
d.p('La guía de 12 columnas viene con la copia. Cada sección nueva se crea como en la sesión 10: un marco con `F` '
    'entre el `Encabezado` y el pie, con estos valores:')
seccion_base(d, 'cursos-intro · catalogo-section · pasos-section · llamado-section', 'las cuatro secciones, dentro de mi-portafolio-cursos')

d.h3('2.1 · La presentación (cursos-intro): 7 y 5 columnas')
d.pasos(['Dentro de `cursos-intro`, escribe con `T` el título `Cursos y talleres` y, en otro texto, el párrafo: `Formación práctica en desarrollo web y herramientas digitales en el Centro de Informática USS. Cada curso termina con un proyecto publicado.`',
         'Selecciona los dos textos con Shift, presiona `Shift + A` y llama al marco nuevo `intro-text`.'])
marco_envoltorio(d, 'intro-text', 'dentro de cursos-intro', 'v', '**Ancho fijo** `737`: 7 columnas y 6 medianiles',
                 'El punto de arriba a la izquierda', '`16`')
texto_bloque(d, 'Cursos y talleres', 'el título, dentro de intro-text', 'llenar', '`Outfit`', '`ExtraBold`', '`36`', '`0B0F19`')
texto_bloque(d, 'Formación práctica…', 'el párrafo, dentro de intro-text', 'llenar', '`Geist`', '`Regular`', '`18`', '`374151`', '`160%`, con el signo')
d.pasos(['Escribe tres pares de textos: `6` y `cursos`, `4 h` y `por sesión`, `1` y `proyecto por curso`.',
         'Selecciona cada par con Shift y presiona `Shift + A`: son tres marcos `cifra`, con Flujo vertical, Alineación al centro y Espacio `4`.',
         'Selecciona los tres marcos `cifra`, presiona `Shift + A` y llama al marco nuevo `cifras`.'])
d.capa('cifras', 'dentro de cursos-intro', [
    ('Disposición automática', [('Flujo', HZ), ('W (ancho)', LLENAR + ': las 5 columnas que quedan'), ('H (alto)', AJUSTAR),
                                ('Espacio', '`24`'), ('Espaciado › campo izquierdo', '`24`'), ('Espaciado › campo derecho', '`24`')]),
    ('Apariencia', [('Radio de esquina', '`12`')]),
    ('Relleno', [('Color', '`FFFFFF`'), ('Porcentaje', '`100`')]),
    ('Trazo', [('Color', '`E5E7EB`'), ('Porcentaje', '`100`'), ('Peso', '`1`')]),
])
d.p('Los números van en Outfit ExtraBold de `32`, color `0B0F19`; las etiquetas, en Geist Regular de `14`, color `374151`. '
    'Cada `cifra` va en **Llenar el contenedor** para repartirse el ancho, como `row-cols-3`.')
d.pasos(['Selecciona `intro-text` y `cifras` con Shift, presiona `Shift + A` y llama al marco nuevo `intro-content`: Flujo horizontal, W en Llenar el contenedor, Espacio `24` y Alineación al centro.'])
d.comprueba('con la guía visible, el texto ocupa las 7 primeras columnas y las cifras las 5 últimas.')

# ---------------- Parte 3
d.h2('Parte 3 · El catálogo: el componente course-card', salto=True)
d.p('Una tarjeta se diseña una vez, se convierte en componente (sesión 11) y se repite con instancias.')
d.pasos(['Dentro de `catalogo-section`, escribe el título `Catálogo` (Outfit ExtraBold `36`).',
         'Escribe cuatro textos: `BÁSICO`, `Diseño Web`, `HTML5, CSS3, Flexbox, Grid y Bootstrap: de un diseño en Figma a un sitio publicado.` y `16 sesiones · 4 h cada una`.',
         'Selecciona `BÁSICO` y presiona `Shift + A`: es la insignia. Llama al marco `curso-nivel`.',
         'Selecciona `16 sesiones…` y presiona `Shift + A`. Llama al marco `curso-meta`.',
         'Selecciona `curso-nivel`, los dos textos y `curso-meta` con Shift, presiona `Shift + A` y llama al marco nuevo `course-card`.'])
d.capa('curso-nivel', 'la insignia, dentro de course-card', [
    ('Disposición automática', [('W y H', AJUSTAR), ('Espaciado › campo izquierdo', '`12`'), ('Espaciado › campo derecho', '`4`')]),
    ('Apariencia', [('Radio de esquina', '`100`: los extremos quedan redondos')]),
    ('Relleno', [('Color', '`E6F8FA` (sugerido): el azul de la marca, muy claro'), ('Porcentaje', '`100`')]),
])
d.p('Su texto `BÁSICO` va en Geist SemiBold de `12`, color `0B0F19`. El título, en Outfit Bold de `22`; la descripción, '
    'en Geist Regular de `16`, color `374151`, con W en Llenar el contenedor; `16 sesiones…`, en Geist Regular de `14`.')
d.capa('curso-meta', 'dentro de course-card, al final', [
    ('Disposición automática', [('W (ancho)', LLENAR), ('Espaciado › campo derecho', '`12` (arriba y abajo)')]),
    ('Trazo', [('Color', '`E5E7EB`'), ('Porcentaje', '`100`'), ('Peso', '`1`'),
               ('Lados', 'Pulsa el último icono de la fila de Peso y elige **Superior**')]),
])
d.capa('course-card', 'dentro de catalogo-section', [
    ('Disposición automática', [('Flujo', V), ('W (ancho)', LLENAR), ('H (alto)', AJUSTAR),
                                ('Espacio', '`12`'), ('Espaciado › campo izquierdo', '`24`'), ('Espaciado › campo derecho', '`24`')]),
    ('Apariencia', [('Radio de esquina', '`12`')]),
    ('Relleno', [('Color', '`FFFFFF`'), ('Porcentaje', '`100`')]),
    ('Trazo', [('Color', '`E5E7EB`'), ('Porcentaje', '`100`'), ('Peso', '`1`')]),
])
d.pasos(['Con `course-card` seleccionado, presiona `Ctrl + Alt + K`: es un componente (en Mac, `Cmd + Option + K`).',
         'Presiona `Ctrl + C` para copiarlo. Después, arrástralo fuera de `mi-portafolio-cursos`, al lienzo gris, como el botón de la sesión 11: el componente principal se guarda fuera de la página.',
         'En Capas, haz clic en `catalogo-section` y presiona `Ctrl + V`. Pegar un componente crea una **instancia**: aparece dentro de la sección, debajo del título.',
         'Con la instancia seleccionada, presiona `Shift + A` y llama al marco nuevo `cursos-fila`: Flujo horizontal, W en Llenar el contenedor y Espacio `24`. La instancia, en W Llenar el contenedor.',
         'Con `cursos-fila` seleccionado, presiona `Ctrl + V` dos veces: tres instancias en la fila.',
         'Cambia los textos de la segunda y la tercera: `JavaScript desde cero` y `Figma para desarrolladores`, con sus descripciones.',
         'Selecciona `cursos-fila` y presiona `Ctrl + D`: una segunda fila. Cambia sus tres tarjetas a `Git y GitHub`, `Java orientado a objetos` y `Bases de datos con SQL`, con `INTERMEDIO`.',
         'Selecciona las dos filas, presiona `Shift + A` y llama al marco `cursos-grid`: Flujo vertical, W en Llenar el contenedor y Espacio `24`.'])
d.comprueba('con la guía visible, cada tarjeta ocupa exactamente 4 columnas: 410.67 de ancho. Entre tarjeta y tarjeta '
            'hay un medianil de 24.')
d.callout('Por qué coinciden:', 'tres tarjetas en Llenar el contenedor con Espacio 24 se reparten 1280 − 48 = 1232: 410.67 '
          'cada una. Cuatro columnas y tres medianiles miden lo mismo: 4 × 84.67 + 3 × 24. Es la clase `col-lg-4`.')

# ---------------- Parte 4
d.h2('Parte 4 · Los pasos y el llamado', salto=True)
d.h3('4.1 · Cuatro pasos de 3 columnas')
d.pasos(['Dentro de `pasos-section`, escribe el título `Cómo trabajamos`.',
         'Diseña un `paso` como una tarjeta: un círculo de 40 × 40 con Relleno `06B6C4` y el número `1` (Outfit ExtraBold de `16`, color `0B0F19`), el título `Diseñas` (Outfit Bold de `18`) y su texto (Geist Regular de `15`).',
         'Envuelve los tres con `Shift + A` y dale los valores de `course-card`: Flujo vertical, Espacio `12`, Espaciado `24`, Radio `12`, Relleno `FFFFFF` y Trazo `E5E7EB`. W en Llenar el contenedor.',
         'Envuelve el `paso` en un marco `pasos-fila` (Flujo horizontal, Espacio `24`, W en Llenar el contenedor) y duplícalo hasta tener cuatro: `Construyes`, `Validas` y `Publicas`.'])
d.comprueba('cada paso ocupa 3 columnas: 302 de ancho. Es `col-lg-3`.')
d.h3('4.2 · El llamado: 8 columnas centradas')
d.capa('llamado-section', 'la sección', [
    ('Disposición automática', [('Alineación', 'El punto central de la fila de arriba: centra a su hijo')]),
])
d.capa('llamado', 'dentro de llamado-section', [
    ('Disposición automática', [('Flujo', V), ('W (ancho)', '**Ancho fijo** `845`: 8 columnas y 7 medianiles'), ('H (alto)', AJUSTAR),
                                ('Alineación', 'El punto central de la fila de arriba'), ('Espacio', '`16`'),
                                ('Espaciado › campo izquierdo', '`40`'), ('Espaciado › campo derecho', '`40`')]),
    ('Apariencia', [('Radio de esquina', '`12`')]),
    ('Relleno', [('Color', '`0B0F19`'), ('Porcentaje', '`100`')]),
])
d.p('Dentro: el título `¿No sabes por cuál empezar?` (Outfit ExtraBold de `36`, Relleno `FFFFFF`), el texto '
    '`Escríbeme y te recomiendo un curso según lo que ya sabes.` (Geist Regular de `16`, Relleno `D1D5DB`) y una '
    '**instancia del componente** `btn-primary` de la sesión 11 con el texto `Escríbeme`.')
d.comprueba('a cada lado del llamado quedan 2 columnas vacías: 2 + 8 + 2 = 12. Es `col-lg-8 offset-lg-2`.')

d.h2('De la guía de columnas a Bootstrap')
d.tabla(['En Figma', 'En cursos.html'], [
    ['Guía de 12 columnas, Margen 80', '`main` como contenedor, con `padding` de 80, y una `.row` por sección'],
    ['Medianil 24 · Espacio 24 entre tarjetas', '`.row.g-4`'],
    ['`intro-text` de 7 columnas · `cifras` de 5', '`.col-lg-7` · `.col-lg-5`'],
    ['`cifra` × 3 en Llenar el contenedor', '`.row.row-cols-3` con tres `.col`'],
    ['`course-card` de 4 columnas, 3 por fila', '`.col-12.col-md-6.col-lg-4`'],
    ['`paso` de 3 columnas, 4 por fila', '`.col-12.col-sm-6.col-lg-3`'],
    ['`llamado` de 8 columnas, centrado', '`.col-lg-8.offset-lg-2`'],
    ['Guía de 4 columnas en el marco móvil', 'Sin clase de punto de quiebre: todo es `col-12` en el celular'],
], negrita_primera=False, anchos=['46%', '54%'])

asi_queda(d, [('03-cursos.png', '`mi-portafolio-cursos` · 1440: presentación de 7 y 5 columnas, catálogo, pasos y llamado de 8 columnas', '62%', None)],
          'Así se ve la página Cursos terminada. Las tarjetas son instancias de `course-card` y miden 4 columnas cada una.')

d.h2('Así deben quedar tus capas')
d.code('''mi-portafolio-cursos                 ← guía de 12 columnas · H Ajustar al contenido
├── Encabezado                       ← con Cursos en nav-links
├── cursos-intro
│   └── intro-content                ← Flujo → · Espacio 24
│       ├── intro-text               ← Ancho fijo 737 (7 columnas)
│       └── cifras                   ← Llenar (5 columnas)
│           └── cifra (× 3)
├── catalogo-section
│   ├── Catálogo
│   └── cursos-grid                  ← Flujo ↓ · Espacio 24
│       └── cursos-fila (× 2)        ← Flujo → · Espacio 24
│           └── course-card (× 3)    ← instancias del componente
├── pasos-section
│   └── pasos-fila
│       └── paso (× 4)
├── llamado-section
│   └── llamado                      ← Ancho fijo 845 (8 columnas)
└── footer-wrapper
course-card                          ← el componente principal''', corto=True)

d.h2('Lista de comprobación')
d.check(['`mi-portafolio` y `mi-portafolio-cursos` tienen una guía de 12 columnas, Margen 80 y Medianil 24.',
         '`mi-portafolio-movil` tiene una guía de 4 columnas, Margen 16.',
         'Los tres menús tienen el enlace Cursos entre Proyectos y Contacto.',
         'Cada `course-card` ocupa 4 columnas y cada `paso`, 3.',
         'El llamado ocupa 8 columnas y deja 2 vacías a cada lado.',
         'Las seis tarjetas son instancias de un mismo componente `course-card`.',
         'Todos los rellenos y trazos están al 100.'])

d.h2('Errores frecuentes en Figma')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['No veo las columnas', 'La guía está oculta: `Ctrl + Shift + 4` (en Mac, `Ctrl + G`). O el porcentaje del color está en 0'],
    ['Las columnas empiezan en el borde del marco', 'El Tipo está en Izquierda o falta el Margen 80'],
    ['Las tarjetas no coinciden con las columnas', 'El Espacio de `cursos-fila` no es 24, o una tarjeta tiene Ancho fijo'],
    ['Las tres tarjetas no miden lo mismo', 'Alguna no está en Llenar el contenedor'],
    ['Cambié el texto de una tarjeta y cambiaron todas', 'Editaste el componente principal, el que está fuera de la página. Edita las instancias, dentro de `cursos-fila`'],
    ['Al pegar no aparece una instancia sino otro componente', 'Copiaste la instancia de otra fila o pegaste fuera de la sección. Copia el componente principal y pega con la sección o la fila seleccionada'],
    ['El llamado no se centra', 'Falta la Alineación al centro en `llamado-section`'],
], anchos=['36%', '64%'])
d.callout('Tu página ya tiene grilla:', 'la guía de columnas te dice cuántas ocupa cada pieza, y ese número es la clase '
          '`col-*` que escribes en Bootstrap.')

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Figma_Sesion13_Guia_de_Columnas_y_Pagina_Cursos.html'))
print('ok')
