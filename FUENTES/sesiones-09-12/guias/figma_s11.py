# -*- coding: utf-8 -*-
"""Guía de Figma · Sesión 11: el botón como componente, su variante Hover y el prototipo."""
import os
from guia import Doc
from figma_comun import donde_estas, como_leer

d = Doc('Guía de Figma · Sesión 11: el botón como componente, su variante Hover y el prototipo',
        'Guía de Figma · Sesión 11',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Ampliación del manual, después del Paso 14',
        'Conviertes el botón principal en un componente con dos estados y le das movimiento con un prototipo. '
        'Es lo mismo que hoy escribes en CSS con `:hover` y `transition`.')

donde_estas(d, 'Sesión 11')
d.callout('El manual termina en el Paso 14:', 'esta guía es una ampliación. Los valores marcados con «sugerido» son una '
          'propuesta; los demás salen de tu CSS de hoy, para que Figma y la página coincidan.')
como_leer(d)

d.h2('Cuatro palabras nuevas', salto=True)
d.tabla(['Palabra', 'Qué es', 'Cómo se ve en Capas'], [
    ['Componente (Component)', 'Un elemento reutilizable. El original se llama **componente principal**: si lo cambias, cambian todas sus copias', 'Icono de cuatro rombos y nombre en morado'],
    ['Instancia (Instance)', 'Una copia conectada al componente principal. Puedes cambiar su texto, pero su forma la manda el principal', 'Icono de un rombo vacío'],
    ['Variante (Variant)', 'Otra versión del mismo componente: el botón normal y el botón con el cursor encima. Viven juntas en un **conjunto de componentes**', 'Un marco con borde morado discontinuo'],
    ['Propiedad (Property)', 'El nombre que distingue las variantes. Hoy se llama `Estado` y tiene dos valores: `Predeterminado` y `Hover`', 'En el nombre de cada variante: `Estado=Hover`'],
], anchos=['22%', '50%', '28%'])
d.p('Y una pestaña nueva: en la parte de arriba del panel derecho hay dos pestañas, **Diseño (Design)**, la que has usado '
    'hasta hoy, y **Prototipo (Prototype)**, donde se conectan las variantes con interacciones.')

d.h3('Lo que vas a construir hoy')
d.code('''(lienzo, fuera de mi-portafolio)
btn-primary                       ← conjunto de componentes, borde morado discontinuo
├── Estado=Predeterminado         ← Relleno 06B6C4
└── Estado=Hover                  ← Relleno 05A3B0 y sombra azul

          Mientras se pasa el cursor → Cambiar a Hover
          Animación inteligente · Salida suave · 200 ms

mi-portafolio › … › hero-actions
└── btn-primary                   ← instancia del componente''')

# ---------------- Parte 1
d.h2('Parte 1 · Convierte el botón en componente', salto=True)
d.p('El componente principal se guarda fuera de la página, en el lienzo gris. En la página queda una instancia.')
d.pasos(['En Capas, abre las flechas `mi-portafolio` › `hero-section` › `hero-left` › `hero-actions` y haz clic en `btn-primary`.',
         'Presiona `Ctrl + D` (en Mac, `Cmd + D`). Aparece una copia dentro de `hero-actions`, junto al original.',
         'En el lienzo, haz clic sostenido sobre la copia y arrástrala fuera de `mi-portafolio`, hasta el espacio gris de la derecha. Suéltala allí.',
         'Comprueba en Capas que la copia no tenga sangría: está al mismo nivel que `mi-portafolio`. Si quedó dentro, arrástrala otra vez.',
         'Con la copia seleccionada, presiona `Ctrl + Alt + K` (en Mac, `Cmd + Option + K`). También puedes pulsar el icono de cuatro rombos, **Crear componente (Create component)**, en la barra de herramientas.'])
d.comprueba('en Capas, el icono de la capa son cuatro rombos y su nombre se ve en morado. El nombre sigue siendo `btn-primary`; si no, haz doble clic y corrígelo.')

# ---------------- Parte 2
d.h2('Parte 2 · Añade la variante Hover')
d.h3('2.1 · Crea la segunda variante')
d.pasos(['Con el componente `btn-primary` seleccionado, mira el panel derecho, pestaña **Diseño**.',
         'Pulsa **Añadir variante (Add variant)**. Figma envuelve el botón en un marco con borde morado discontinuo y crea una copia debajo.',
         'Si no encuentras ese botón: presiona `Ctrl + D` para duplicar el componente, selecciona los dos con Shift y pulsa **Combinar como variantes (Combine as variants)** en el panel derecho.'])
d.p('El marco morado es el **conjunto de componentes**. Toma el nombre `btn-primary` y dentro tiene dos variantes con '
    'nombres como `Property 1=Default` y `Property 1=Variant2` (o `Propiedad 1=…`, según el idioma de tu Figma).')
d.h3('2.2 · Pon nombre a la propiedad y a sus valores')
d.p('El nombre de cada variante tiene la forma `Propiedad=Valor`. Cámbialo directamente en Capas:')
d.pasos(['En Capas, abre la flecha del conjunto `btn-primary`.',
         'Haz doble clic sobre el nombre de la primera variante y escribe `Estado=Predeterminado`. Pulsa Enter.',
         'Haz doble clic sobre el nombre de la segunda y escribe `Estado=Hover`. Pulsa Enter.'])
d.comprueba('al seleccionar el conjunto, el panel derecho muestra una propiedad llamada `Estado` con dos valores: '
            '`Predeterminado` y `Hover`.')
d.h3('2.3 · Los valores de la variante Hover')
d.p('Solo cambian el Relleno y un efecto nuevo. El Espaciado, el Radio de esquina y el texto quedan igual que en la variante '
    'Predeterminado: si cambias el tamaño, el botón saltaría al pasar el cursor.')
d.capa('Estado=Hover', 'la segunda variante, dentro del conjunto btn-primary', [
    ('Relleno', [('Color', '`05A3B0` (sugerido): el mismo azul, un poco más oscuro'), ('Porcentaje', '`100`')]),
    ('Efectos', [('Tipo', '**Sombra paralela (Drop shadow)**'), ('X', '`0`'), ('Y', '`4`'),
                 ('Desenfoque (Blur)', '`14`'), ('Propagación (Spread)', '`0`'),
                 ('Color', '`06B6C4`'), ('Porcentaje', '`35`: aquí sí, el porcentaje no es 100')]),
])
d.pasos(['Para añadir la sombra: en la sección **Efectos**, pulsa **+**. Figma añade una Sombra paralela.',
         'Haz clic en el icono que está a la izquierda de su nombre: se abre la ventana con X, Y, Desenfoque, Propagación y Color.',
         'Escribe los valores del bloque y cierra la ventana.'])
d.callout('Lo que Figma no dibuja:', 'en tu CSS, el botón además sube 2 px al pasar el cursor y se encoge un poco al '
          'presionarlo (`transform`). En Figma eso se nota solo en el prototipo; en el diseño quieto, las dos variantes '
          'están en el mismo sitio.')
d.capa('Estado=Predeterminado', 'la primera variante: revisa que conserve los valores de la sesión 07', [
    ('Disposición automática', [('Espaciado › campo izquierdo', '`24` (horizontal)'), ('Espaciado › campo derecho', '`14` (vertical)')]),
    ('Apariencia', [('Radio de esquina', '`8`')]),
    ('Relleno', [('Color', '`06B6C4`'), ('Porcentaje', '`100`')]),
    ('Efectos', [('Efectos', 'Ninguno')]),
])

# ---------------- Parte 3
d.h2('Parte 3 · El prototipo: Mientras se pasa el cursor', salto=True)
d.pasos(['En Capas, haz clic en la variante `Estado=Predeterminado`.',
         'Arriba del panel derecho, cambia a la pestaña **Prototipo (Prototype)**.',
         'En la sección **Interacciones (Interactions)**, pulsa **+**. Aparece una interacción nueva con su ventana de opciones.',
         'Elige los valores del bloque siguiente. Cierra la ventana cuando termines.'])
d.capa('Estado=Predeterminado', 'pestaña Prototipo › Interacciones', [
    ('Interacción', [('Desencadenante (Trigger)', '**Mientras se pasa el cursor (While hovering)**'),
                     ('Acción (Action)', '**Cambiar a (Change to)**'),
                     ('Destino', 'En el menú de `Estado`, elige `Hover`')]),
    ('Animación', [('Tipo', '**Animación inteligente (Smart animate)**'),
                   ('Curva', '**Salida suave (Ease out)**'),
                   ('Duración', '`200` ms')]),
])
d.p('En el lienzo aparece una flecha azul de la variante Predeterminado a la variante Hover. No hace falta una segunda '
    'flecha de vuelta: **Mientras se pasa el cursor** regresa sola a Predeterminado cuando el cursor se va, igual que `:hover` en CSS.')
d.callout('La Animación inteligente empareja capas por su nombre:', 'para animar el color, busca en las dos variantes '
          'capas con el mismo nombre. Si renombraste el texto `Ver Proyectos` en una sola de ellas, el cambio será de golpe.')
d.tabla(['En Figma', 'En tu CSS de hoy'], [
    ['Mientras se pasa el cursor', '`.btn-primary:hover`'],
    ['Cambiar a `Estado=Hover`', 'Las propiedades dentro de `:hover`: `background-color`, `box-shadow`'],
    ['Animación inteligente', '`transition`'],
    ['Salida suave · 200 ms', '`var(--duration-fast) var(--ease-out)`, es decir, `0.2s` y una curva de salida suave'],
    ['Relleno `05A3B0`', '`--color-primary-hover: #05A3B0;`'],
    ['Sombra paralela Y 4, Desenfoque 14, `06B6C4` al 35 %', '`box-shadow: 0 4px 14px rgba(6, 182, 196, 0.35);`'],
], anchos=['42%', '58%'])

# ---------------- Parte 4
d.h2('Parte 4 · Pon una instancia en el Hero')
d.p('El botón que quedó en `hero-actions` todavía es el marco de la sesión 07, sin estados. Reemplázalo por una instancia del componente:')
d.pasos(['En Capas, haz clic en la variante `Estado=Predeterminado` y presiona `Ctrl + C` (en Mac, `Cmd + C`).',
         'Abre las flechas `mi-portafolio` › `hero-section` › `hero-left` › `hero-actions` y haz clic en el `btn-primary` de la sesión 07.',
         'Presiona `Ctrl + Shift + R` (en Mac, `Cmd + Shift + R`): **Pegar para reemplazar (Paste to replace)**. La instancia ocupa el lugar del botón viejo.',
         'Si ese atajo no hace nada: borra el botón viejo con Supr, selecciona `hero-actions`, presiona `Ctrl + V` y arrastra la instancia en Capas hasta que quede antes de `btn-secundary`.'])
d.comprueba('en Capas, el `btn-primary` de `hero-actions` tiene el icono de un rombo vacío, y al seleccionarlo, el panel '
            'derecho muestra `Estado: Predeterminado`. El texto sigue siendo «Ver Proyectos».')

# ---------------- Parte 5
d.h2('Parte 5 · Pruébalo')
d.pasos(['Haz clic en `mi-portafolio` en Capas.',
         'Pulsa el botón **Presentar (Present)**, el triángulo ▷ de la esquina superior derecha. El prototipo se abre en una pestaña nueva.',
         'Pasa el cursor sobre «Ver Proyectos»: se oscurece y aparece la sombra en 200 ms. Retíralo: vuelve a su estado normal.',
         'Abre tu `index.html` en el navegador y compara: el color, la sombra y la velocidad deben ser los mismos.'])

d.h2('Ampliación: más estados en tu diseño')
d.p('Si terminas antes, repite el método con otras piezas que hoy reciben `:hover` en tu CSS:')
d.tabla(['Componente', 'Variante Hover (sugerido)', 'En tu CSS'], [
    ['`btn-secundary`', 'Relleno `0B0F19` al `5`: un gris casi transparente', '`.btn-secondary:hover`'],
    ['`project-card`', 'Sombra paralela: X `0`, Y `16`, Desenfoque `32`, `0B0F19` al `8`', '`.project-card:hover`'],
    ['`contact-card`', 'Trazo `06B6C4` al `100`', '`.contact-card:hover`'],
], negrita_primera=False, anchos=['24%', '46%', '30%'])

d.h2('Así deben quedar tus capas')
d.code('''mi-portafolio
├── Encabezado
├── hero-section
│   ├── hero-left
│   │   ├── Formando a la próxima…
│   │   ├── Docente e Ingeniero…
│   │   └── hero-actions
│   │       ├── btn-primary                  ← instancia (rombo vacío)
│   │       └── btn-secundary
│   └── hero-right
├── about-section
├── projects-section
├── contact-section
└── footer-wrapper

btn-primary                                  ← conjunto de componentes, fuera de la página
├── Estado=Predeterminado                    ← interacción hacia Hover
└── Estado=Hover''')

d.h2('Lista de comprobación')
d.check(['El conjunto `btn-primary` está en el lienzo, fuera de `mi-portafolio`.',
         'Sus dos variantes se llaman `Estado=Predeterminado` y `Estado=Hover`.',
         'Las dos variantes miden lo mismo: Espaciado 24 y 14, Radio de esquina 8.',
         'La variante Hover tiene Relleno `05A3B0` al 100 y una Sombra paralela `06B6C4` al 35.',
         'La variante Predeterminado tiene la interacción Mientras se pasa el cursor › Cambiar a › Hover, con Animación inteligente, Salida suave y 200 ms.',
         'El botón del Hero es una instancia del componente.',
         'Al presentar, el botón cambia con suavidad y vuelve solo al retirar el cursor.'])

d.h2('Errores frecuentes en Figma')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['Al presentar, el botón del Hero no cambia', 'Sigue siendo el marco de la sesión 07, no una instancia. Repite la Parte 4'],
    ['El cambio es de golpe', 'En la interacción, la Animación está en Instantáneo. Elige Animación inteligente'],
    ['El botón salta o cambia de tamaño al pasar el cursor', 'La variante Hover tiene otro Espaciado u otro texto. Copia los valores de Predeterminado'],
    ['No aparece la opción Cambiar a', 'La interacción está en el conjunto o en la instancia. Ponla en la variante `Estado=Predeterminado`'],
    ['No aparece Mientras se pasa el cursor en el menú', 'Abre el primer menú de la interacción (el desencadenante): por defecto dice Al hacer clic (On click)'],
    ['El conjunto quedó dentro de `hero-actions`', 'Creaste el componente sin sacar la copia de la página. En Capas, arrastra el conjunto hasta que no tenga sangría'],
    ['Las variantes se llaman `Property 1=Default`', 'Falta el paso 2.2: renómbralas en Capas con la forma `Estado=Valor`'],
], anchos=['36%', '64%'])
d.callout('Tu diseño ya tiene estados:', 'el mismo botón existe quieto y con el cursor encima, y sabes cuánto tarda en '
          'cambiar. La guía de código de esta sesión lo escribe con `:hover`, `transition` y `transform`.')

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Figma_Sesion11_Componente_Variantes_y_Prototipo.html'))
print('ok')
