# -*- coding: utf-8 -*-
"""Guía de Figma · Sesión 14: variables locales y el componente de curso con variantes."""
import os
from guia import Doc
from figma_comun import asi_queda, donde_estas, como_leer

d = Doc('Guía de Figma · Sesión 14: variables y el componente de curso',
        'Guía de Figma · Sesión 14',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Ampliación del manual, después del Paso 14',
        'Guardas los colores y las medidas de tu diseño como variables, las aplicas a tus capas y le das a la tarjeta '
        'de curso dos variantes: Básico e Intermedio.')

donde_estas(d, 'Sesión 14')
d.callout('El manual termina en el Paso 14:', 'esta guía es una ampliación. Las variables de Figma son las mismas '
          'variables de `global.css` y las que hoy le cambias a Bootstrap en `tema-bootstrap.css`.')
como_leer(d)

d.h2('Una variable, tres lugares', salto=True)
d.p('Desde la sesión 09 escribes los colores de Figma como variables de CSS. Hoy haces el camino de vuelta: los '
    'guardas en Figma como **variables locales**. Si cambias una variable, cambian todas las capas que la usan, '
    'igual que en CSS.')
d.tabla(['Variable en Figma', 'En global.css', 'En tema-bootstrap.css'], [
    ['`color-primary` · `06B6C4`', '`--color-primary`', '`--bs-primary`'],
    ['`color-primary-hover` · `05A3B0`', '`--color-primary-hover`', '`--bs-btn-hover-bg`'],
    ['`color-text-primary` · `0B0F19`', '`--color-text-primary`', '`--bs-dark-rgb`'],
    ['`color-text-secondary` · `374151`', '`--color-text-secondary`', '`--bs-body-color`'],
    ['`color-border` · `E5E7EB`', '`--color-border`', '`--bs-border-color`'],
    ['`radius-sm` · `8`', '`--radius-sm`', '`--bs-border-radius`'],
    ['`radius-md` · `12`', '`--radius-md`', '`--bs-border-radius-lg` y `--bs-card-border-radius`'],
], negrita_primera=False, anchos=['36%', '28%', '36%'])

# ---------------- Parte 1
d.h2('Parte 1 · Crea la colección de variables')
d.pasos(['Haz clic en una zona vacía del lienzo gris: no debe quedar ninguna capa seleccionada.',
         'En el panel derecho, busca la sección **Variables locales (Local variables)** y pulsa **Abrir variables (Open variables)**. Se abre una ventana grande.',
         'Arriba a la izquierda está el nombre de la colección: `Collection 1` o `Colección 1`. Haz doble clic y escribe `tokens`.',
         'Pulsa **+ Crear variable (Create variable)** y elige **Color**. Escribe el nombre y, en la columna del valor, el código del color.',
         'Repite con cada color de la tabla. Para las medidas, elige **Número (Number)**.'])
d.tabla(['Nombre', 'Tipo', 'Valor', 'Para qué'], [
    ['`color-primary`', 'Color', '`06B6C4`', 'Botones, iconos y acentos'],
    ['`color-primary-hover`', 'Color', '`05A3B0`', 'La variante Hover del botón (sesión 11)'],
    ['`color-primary-subtle`', 'Color', '`E6F8FA`', 'El fondo de la insignia Básico'],
    ['`color-bg`', 'Color', '`F9FAFB`', 'El fondo de la página'],
    ['`color-surface`', 'Color', '`FFFFFF`', 'Tarjetas y cabecera'],
    ['`color-text-primary`', 'Color', '`0B0F19`', 'Títulos; el fondo del llamado'],
    ['`color-text-secondary`', 'Color', '`374151`', 'Párrafos'],
    ['`color-border`', 'Color', '`E5E7EB`', 'Trazos'],
    ['`radius-sm`', 'Número', '`8`', 'Botones y campos'],
    ['`radius-md`', 'Número', '`12`', 'Tarjetas'],
    ['`gutter`', 'Número', '`24`', 'El Espacio entre tarjetas: el medianil de `g-4`'],
], anchos=['30%', '14%', '16%', '40%'])
d.callout('Los nombres, como en CSS:', 'en minúsculas, con guiones y sin espacios. Así se leen igual en Figma y en tu código. '
          'Si escribes una barra, como `color/primary`, Figma crea un grupo llamado `color`.')
d.comprueba('la ventana muestra 8 variables de color con su muestra y 3 de número. Ciérrala con la X.')

# ---------------- Parte 2
d.h2('Parte 2 · Aplica las variables a tus capas')
d.h3('2.1 · Un color')
d.pasos(['En Capas, abre el componente `btn-primary` del lienzo y haz clic en la variante `Estado=Predeterminado`.',
         'En **Relleno**, pasa el cursor sobre la fila del color. A la derecha aparece el icono de cuatro puntos, **Aplicar estilos y variables (Apply styles and variables)**: púlsalo.',
         'En la lista, elige `color-primary`. El código `06B6C4` se cambia por el nombre de la variable.'])
d.capa('btn-primary › Estado=Predeterminado · Estado=Hover', 'las dos variantes del botón (sesión 11)', [
    ('Relleno', [('Estado=Predeterminado', 'Variable `color-primary`'), ('Estado=Hover', 'Variable `color-primary-hover`')]),
    ('Apariencia', [('Radio de esquina', 'Variable `radius-sm`: ver 2.2')]),
])
d.h3('2.2 · Una medida')
d.pasos(['Con la variante seleccionada, pasa el cursor sobre el campo **Radio de esquina**.',
         'Pulsa el icono que aparece dentro del campo, **Aplicar variable (Apply variable)**, y elige `radius-sm`. El campo muestra el nombre en un recuadro.'])
d.capa('course-card', 'el componente principal, en el lienzo (sesión 13)', [
    ('Disposición automática', [('Espaciado', 'Sigue en `24`')]),
    ('Apariencia', [('Radio de esquina', 'Variable `radius-md`')]),
    ('Relleno', [('Color', 'Variable `color-surface`')]),
    ('Trazo', [('Color', 'Variable `color-border`')]),
])
d.capa('cursos-fila (× 2) · pasos-fila', 'en mi-portafolio-cursos', [
    ('Disposición automática', [('Espacio', 'Variable `gutter`')]),
])
d.capa('llamado', 'en mi-portafolio-cursos', [
    ('Relleno', [('Color', 'Variable `color-text-primary`')]),
    ('Apariencia', [('Radio de esquina', 'Variable `radius-md`')]),
])
d.comprueba('abre otra vez la ventana de variables y cambia `color-primary` a cualquier otro color. Todos los botones de '
            'las tres páginas cambian a la vez. Deshaz con `Ctrl + Z`.')
d.callout('Es lo mismo que hiciste en tema-bootstrap.css:', 'cambiaste `--bs-primary` y cambiaron todos los botones, '
          'las insignias y los bordes de Bootstrap sin tocar el HTML.')

# ---------------- Parte 3
d.h2('Parte 3 · La tarjeta de curso con dos variantes', salto=True)
d.p('En la página web, la insignia **Básico** es cian claro con texto oscuro y la **Intermedio** es oscura con texto '
    'blanco. En Figma, eso es un componente con dos variantes, como el botón de la sesión 11.')
d.pasos(['En el lienzo, haz clic en el componente principal `course-card`.',
         'En el panel derecho, pulsa **Añadir variante (Add variant)**. Figma lo envuelve en un conjunto con borde morado discontinuo y crea una copia debajo.',
         'En Capas, renombra la primera variante `Nivel=Básico` y la segunda `Nivel=Intermedio`.',
         'En la variante Intermedio, cambia el texto `BÁSICO` por `INTERMEDIO` y aplica los valores del bloque siguiente.'])
d.capa('curso-nivel', 'la insignia, dentro de Nivel=Intermedio', [
    ('Relleno', [('Color', 'Variable `color-text-primary`')]),
])
d.capa('INTERMEDIO', 'el texto de la insignia, dentro de Nivel=Intermedio', [
    ('Relleno', [('Color', 'Variable `color-surface`: blanco')]),
])
d.capa('curso-nivel', 'la insignia, dentro de Nivel=Básico', [
    ('Relleno', [('Color', 'Variable `color-primary-subtle`')]),
])
d.h3('3.1 · Cambia las instancias de la segunda fila')
d.pasos(['En `mi-portafolio-cursos`, selecciona con Shift las tres tarjetas de la segunda `cursos-fila`.',
         'En el panel derecho aparece la propiedad **Nivel** con un menú. Elige `Intermedio`.',
         'Las tres tarjetas cambian de insignia y conservan sus textos.'])
d.comprueba('la primera fila muestra insignias claras y la segunda, oscuras. Al seleccionar una tarjeta, el panel '
            'derecho dice `Nivel: Básico` o `Nivel: Intermedio`.')
d.tabla(['En Figma', 'En cursos.html'], [
    ['`Nivel=Básico` · Relleno `color-primary-subtle`', '`badge rounded-pill bg-primary-subtle text-primary-emphasis`'],
    ['`Nivel=Intermedio` · Relleno `color-text-primary`', '`badge rounded-pill text-bg-dark`'],
    ['`course-card` · Radio `radius-md`, Trazo `color-border`', '`card` (con el radio del tema) y `shadow-sm`'],
    ['`curso-meta` con Trazo superior', '`card-footer`'],
], negrita_primera=False, anchos=['46%', '54%'])

d.h2('Ampliación: la ventana de inscripción')
d.p('Si terminas antes, diseña la ventana modal sobre una copia de `mi-portafolio-cursos`:')
d.lista(['**Fondo oscuro:** un rectángulo de 1440 × 900 con Relleno `000000` al `50`, encima de toda la página. Aquí el porcentaje no es 100: deja ver la página detrás.',
         '**La ventana:** un marco de 500 de ancho, centrado, con Flujo vertical, Radio `radius-md`, Relleno `color-surface` y una Sombra paralela (Y `8`, Desenfoque `24`, `000000` al `15`).',
         '**Dentro:** el título `Inscríbete` (Outfit Bold de `20`), tres campos como los del formulario de contacto y dos botones a la derecha: `Cancelar` (Trazo `374151`) y una instancia de `btn-primary` con `Enviar inscripción`.'])

asi_queda(d, [('05-course-card.png', 'El conjunto `course-card`: `Nivel=Básico` y `Nivel=Intermedio`, con las variables de `tokens`', '80%', None)],
          'Así se ve el componente de curso con sus dos variantes. Sus colores y radios vienen de las variables de la colección `tokens`.')

d.h2('Así deben quedar tus capas')
d.code('''(variables locales)
tokens                               ← 8 colores y 3 números

btn-primary                          ← conjunto: Estado=Predeterminado · Estado=Hover
course-card                          ← conjunto: Nivel=Básico · Nivel=Intermedio

mi-portafolio-cursos
├── Encabezado
├── cursos-intro
├── catalogo-section
│   └── cursos-grid
│       ├── cursos-fila              ← Espacio: gutter · 3 tarjetas Nivel=Básico
│       └── cursos-fila              ← Espacio: gutter · 3 tarjetas Nivel=Intermedio
├── pasos-section
├── llamado-section                  ← llamado: Relleno color-text-primary
└── footer-wrapper''', corto=True)

d.h2('Lista de comprobación')
d.check(['La colección `tokens` tiene 8 variables de color y 3 de número, con los nombres de la tabla.',
         'Las dos variantes del botón usan `color-primary` y `color-primary-hover`.',
         '`course-card` usa `radius-md`, `color-surface` y `color-border`.',
         'El Espacio de las filas de tarjetas y de pasos es la variable `gutter`.',
         '`course-card` tiene las variantes `Nivel=Básico` y `Nivel=Intermedio`.',
         'Las tres tarjetas de la segunda fila son `Nivel=Intermedio`.',
         'Al cambiar `color-primary`, cambian todos los botones; después lo devolviste a `06B6C4`.'])

d.h2('Errores frecuentes en Figma')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['No aparece la sección Variables locales', 'Hay una capa seleccionada. Haz clic en el lienzo gris, fuera de todo marco'],
    ['El icono de cuatro puntos no aparece', 'Pasa el cursor sobre la fila del color, a la derecha del porcentaje: solo se ve al pasar encima'],
    ['La variable de número no aparece en el Radio', 'La creaste como Color o como Cadena. Bórrala y créala como Número'],
    ['Cambié la variable y una capa no cambió', 'Esa capa tiene el código escrito a mano. Selecciónala y aplica la variable'],
    ['No veo la propiedad Nivel en las tarjetas', 'Seleccionaste el marco `cursos-fila` y no las tarjetas. Selecciónalas en Capas'],
    ['La variante Intermedio cambió de tamaño', 'Cambiaste el Espaciado de la insignia. Solo cambian el Relleno y el texto'],
], anchos=['36%', '64%'])
d.callout('Tu diseño y tu código hablan igual:', 'los mismos nombres en Figma, en `global.css` y en el tema de '
          'Bootstrap. Si mañana cambia el color de la marca, se cambia en un solo lugar de cada uno.')

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Figma_Sesion14_Variables_y_Componente_de_Curso.html'))
print('ok')
