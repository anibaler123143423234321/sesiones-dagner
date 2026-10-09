# -*- coding: utf-8 -*-
"""Guía de Figma · Sesión 12: la versión móvil de la página (marco de 390)."""
import os
from guia import Doc
from figma_comun import donde_estas, como_leer

V = 'Vertical: el segundo icono, con la flecha ↓'
LLENAR = 'Abre el menú y elige **Llenar el contenedor**'
AJUSTAR = '**Ajustar al contenido**'

d = Doc('Guía de Figma · Sesión 12: la versión móvil de tu página',
        'Guía de Figma · Sesión 12',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Ampliación del manual, después del Paso 14',
        'Duplicas tu página, la llevas a 390 de ancho y cambias el Flujo de cada sección: el mismo trabajo que hacen '
        'tus media queries.')

donde_estas(d, 'Sesión 12')
d.callout('El manual termina en el Paso 14:', 'esta guía es una ampliación. Los valores del marco móvil salen de tu CSS '
          'de hoy (los bloques de `@media (max-width: 600px)`), para que Figma y la página coincidan en el celular.')
como_leer(d)

d.h2('Lo que vas a construir hoy', salto=True)
d.raw('''<div class="esq nobreak" style="display:flex;gap:14px;align-items:flex-start">
<div style="flex:1"><div class="rot">mi-portafolio · 1440 (escritorio)</div>
<div class="s prev"><span><b>Encabezado</b> · nombre y menú en una fila</span><span>Altura fija 80</span></div>
<div class="s prev"><span><b>hero-section</b> · texto | tarjeta de código</span><span>Flujo →</span></div>
<div class="s prev"><span><b>about-content</b> · texto | gráfico 480</span><span>Flujo →</span></div>
<div class="s prev"><span><b>projects-grid</b> · tarjeta | tarjeta</span><span>Flujo →</span></div>
<div class="s prev"><span><b>contact-content</b> · texto | lista 520</span><span>Flujo →</span></div>
<div class="s prev"><span><b>footer-wrapper</b></span><span>Altura fija 182</span></div></div>
<div style="width:190px"><div class="rot">mi-portafolio-movil · 390</div>
<div class="s hoy"><div class="tit"><span>Encabezado</span><span>Flujo ↓</span></div><div class="pie">nombre / menú debajo</div></div>
<div class="s hoy"><div class="tit"><span>hero-section</span><span>Flujo ↓</span></div><div class="pie">título 40 · botones a todo el ancho / tarjeta</div></div>
<div class="s hoy"><div class="tit"><span>about-content</span><span>Flujo ↓</span></div><div class="pie">texto / gráfico</div></div>
<div class="s hoy"><div class="tit"><span>projects-grid</span><span>Flujo ↓</span></div><div class="pie">tarjeta / tarjeta</div></div>
<div class="s hoy"><div class="tit"><span>contact-content</span><span>Flujo ↓</span></div><div class="pie">texto / lista</div></div>
<div class="s hoy"><div class="tit"><span>footer-wrapper</span><span>Ajustar</span></div></div></div>
</div>''')
d.raw('<p class="leyenda">Las secciones no cambian de orden: lo que estaba lado a lado (→) pasa a estar una debajo de la otra (↓).</p>')
d.tabla(['Regla del celular', 'Valor', 'En tu CSS'], [
    ['Ancho del marco', '`390`: el de un iPhone 13 o 14, un ancho de celular muy común', 'La prueba a 390 px en DevTools'],
    ['Espaciado de las secciones', '`16` a los lados y `48` arriba y abajo (antes, 80 y 100)', '`main { padding: 3rem 1rem; }`'],
    ['Títulos de sección', '`28` (antes, 36)', 'El mínimo de `clamp(1.75rem, …, 2.25rem)`'],
    ['Título del Hero', '`40` (antes, 64)', 'El mínimo de `clamp(2.5rem, …, 4rem)`'],
    ['Marcos con dos columnas', 'Flujo vertical', '`flex-direction: column`'],
    ['Anchos fijos de 480, 520 o 696', 'Llenar el contenedor', '`flex-basis: auto` y `align-items: stretch`'],
], anchos=['28%', '40%', '32%'])

# ---------------- Parte 1
d.h2('Parte 1 · Duplica la página')
d.pasos(['En Capas, haz clic en `mi-portafolio`.',
         'Presiona `Ctrl + D` (en Mac, `Cmd + D`). La copia aparece a la derecha del original; si queda encima, arrástrala a un espacio libre del lienzo.',
         'En Capas, haz doble clic sobre el nombre de la copia y escribe `mi-portafolio-movil`.'])
d.capa('mi-portafolio-movil', 'la copia, en el lienzo', [
    ('Disposición automática', [('Flujo', V), ('W (ancho)', '**Ancho fijo** `390`'),
                                ('H (alto)', 'Por ahora, déjalo como está: lo ajustas en la Parte 6')]),
])
d.p('El marco se angosta, pero varias piezas siguen midiendo lo mismo que en el escritorio y se salen por la derecha: '
    'son las que tienen **Ancho fijo**. Las vas a corregir de arriba abajo. No te preocupes por cómo se ve mientras tanto.')
d.callout('Trabaja solo en la copia:', 'antes de cambiar un valor, mira en Capas que la capa seleccionada esté dentro de '
          '`mi-portafolio-movil`. Si tu `btn-primary` es una instancia (sesión 11), la copia también lo es y sigue '
          'conectada al componente.')

# ---------------- Parte 2
d.h2('Parte 2 · El Encabezado')
d.capa('Encabezado', 'dentro de mi-portafolio-movil', [
    ('Disposición automática', [('Flujo', V), ('W (ancho)', LLENAR), ('H (alto)', AJUSTAR + ': deja de medir 80'),
                                ('Alineación', 'El punto del centro'), ('Espacio', '`12`'),
                                ('Espaciado › campo izquierdo', '`16` (horizontal)'),
                                ('Espaciado › campo derecho', '`16` (vertical)')]),
])
d.capa('nav-links', 'dentro del Encabezado de mi-portafolio-movil', [
    ('Disposición automática', [('Flujo', 'Horizontal: el tercer icono, con la flecha → (no cambia)'), ('Espacio', '`20` (antes, 32)')]),
])
d.comprueba('el nombre queda centrado arriba y los tres enlaces del menú, en una fila debajo.')

# ---------------- Parte 3
d.h2('Parte 3 · El Hero', salto=True)
d.capa('hero-section', 'dentro de mi-portafolio-movil', [
    ('Disposición automática', [('Flujo', V), ('W (ancho)', LLENAR), ('Alineación', 'El punto del centro'),
                                ('Espacio', '`64` (no cambia)'),
                                ('Espaciado › campo izquierdo', '`16` (horizontal)'),
                                ('Espaciado › campo derecho', '`48` (vertical)')]),
])
d.capa('hero-left', 'dentro de hero-section', [
    ('Disposición automática', [('W (ancho)', LLENAR + ': deja de medir 696'), ('Alineación', 'El punto del centro de la fila de arriba'),
                                ('Espacio', '`32` (no cambia)')]),
])
d.capa('Formando a la próxima…', 'el título del Hero, dentro de hero-left', [
    ('Disposición', [('W (ancho)', LLENAR + ': el texto baja de línea dentro del marco')]),
    ('Tipografía', [('Tamaño', '`40` (antes, 64)'), ('Alineación', 'Centrado: el segundo icono')]),
])
d.capa('Docente e Ingeniero…', 'el párrafo del Hero, dentro de hero-left', [
    ('Disposición', [('W (ancho)', LLENAR)]),
    ('Tipografía', [('Alineación', 'Centrado: el segundo icono')]),
])
d.capa('hero-actions', 'dentro de hero-left', [
    ('Disposición automática', [('Flujo', V), ('W (ancho)', LLENAR), ('Espacio', '`16` (no cambia)')]),
])
d.capa('btn-primary · btn-secundary', 'los dos botones, dentro de hero-actions: selecciónalos juntos con Shift', [
    ('Disposición automática', [('W (ancho)', LLENAR + ': los botones ocupan todo el ancho'), ('Alineación', 'El punto del centro: el texto queda al medio')]),
])
d.capa('hero-right', 'la tarjeta de código, dentro de hero-section', [
    ('Disposición automática', [('W (ancho)', LLENAR + ': deja de medir 520'), ('H (alto)', AJUSTAR + ': deja de medir 404')]),
])
d.capa('code-body', 'dentro de hero-right', [
    ('Disposición automática', [('Espaciado › campo izquierdo', '`16` (antes, 24)'), ('Espaciado › campo derecho', '`16` (antes, 24)')]),
])
d.p('Selecciona el texto del código, dentro de `code-body`, y cambia su **Tamaño** a `12`.')
d.comprueba('el título ocupa cuatro líneas centradas; los dos botones, uno debajo del otro, miden 358 de ancho; la '
            'tarjeta de código queda debajo y ninguna línea de código se sale.')

# ---------------- Parte 4
d.h2('Parte 4 · Sobre mí y Proyectos')
d.p('Las tres secciones interiores cambian igual. Selecciona `about-section`, `projects-section` y `contact-section` '
    'juntas con Shift y escribe los valores una sola vez:')
d.capa('about-section · projects-section · contact-section', 'las tres secciones de mi-portafolio-movil', [
    ('Disposición automática', [('Espaciado › campo izquierdo', '`16` (horizontal)'), ('Espaciado › campo derecho', '`48` (vertical)'),
                                ('Espacio', '`48` (no cambia)')]),
])
d.p('Selecciona los tres títulos, `Sobre mí`, `Proyectos` y `Contacto`, juntos con Shift, y cambia su **Tamaño** a `28`.')
d.capa('about-content', 'dentro de about-section', [
    ('Disposición automática', [('Flujo', V), ('Alineación', 'El punto de arriba a la izquierda'), ('Espacio', '`64` (no cambia)')]),
])
d.capa('about-graphic', 'dentro de about-content', [
    ('Disposición automática', [('W (ancho)', LLENAR + ': deja de medir 480'), ('H (alto)', '**Altura fija** `264` (no cambia)')]),
])
d.capa('projects-grid', 'dentro de projects-section', [
    ('Disposición automática', [('Flujo', V), ('Espacio', '`24` (no cambia)')]),
])
d.capa('project-card (× 2)', 'las dos tarjetas: selecciónalas juntas con Shift', [
    ('Disposición automática', [('W (ancho)', LLENAR + ' (no cambia)'), ('H (alto)', AJUSTAR + ': deja de medir 475')]),
])
d.capa('project-image (× 2)', 'las dos imágenes, dentro de cada tarjeta', [
    ('Disposición', [('W (ancho)', LLENAR + ' (no cambia)'), ('H (alto)', '`125`: 358 × 220 ÷ 628, la misma proporción del escritorio')]),
])
d.callout('La proporción también existe en CSS:', 'en tu código no escribes 125. Escribes `aspect-ratio: 628 / 220` y el '
          'navegador calcula el alto para cualquier ancho.')

# ---------------- Parte 5
d.h2('Parte 5 · Contacto y pie de página')
d.capa('contact-content', 'dentro de contact-section', [
    ('Disposición automática', [('Flujo', V), ('Espacio', '`64` (no cambia)')]),
])
d.capa('contact-list', 'dentro de contact-content', [
    ('Disposición automática', [('W (ancho)', LLENAR + ': deja de medir 520')]),
])
d.capa('contact-card (× 3)', 'las tres filas: selecciónalas juntas con Shift', [
    ('Disposición automática', [('W (ancho)', LLENAR + ': deja de medir 520'), ('H (alto)', '**Altura fija** `84` (no cambia)')]),
])
d.capa('footer-wrapper', 'dentro de mi-portafolio-movil, al final', [
    ('Disposición automática', [('H (alto)', AJUSTAR + ': deja de medir 182'),
                                ('Espaciado › campo izquierdo', '`16` (horizontal)'),
                                ('Espaciado › campo derecho', '`48` (vertical)')]),
])
d.p('Selecciona el texto del pie y, en Disposición, cambia su W a **Llenar el contenedor**: así baja de línea en lugar de salirse.')

# ---------------- Parte 6
d.h2('Parte 6 · La altura del marco y la prueba')
d.pasos(['En Capas, haz clic en `mi-portafolio-movil`.',
         'En Disposición automática, abre el menú del campo H y elige **Ajustar al contenido**. El marco toma la altura de todo lo que tiene dentro.',
         'Revisa el marco de arriba abajo: ninguna capa debe salirse por la derecha.',
         'Con `mi-portafolio-movil` seleccionado, pulsa **Presentar (Present)**, el triángulo ▷ de la esquina superior derecha, y recorre la página con la rueda del mouse.',
         'Abre tu `index.html` en DevTools con el modo dispositivo a 390 (guía de código, Paso 0) y compara las dos versiones.'])
d.tabla(['En Figma móvil', 'En tu CSS de hoy'], [
    ['Encabezado: Flujo vertical y Ajustar al contenido', '`header { height: auto; flex-wrap: wrap; justify-content: center; }`'],
    ['`hero-section`: Flujo vertical', '`.hero-section { flex-direction: column; }`'],
    ['Título del Hero: 40', '`font-size: clamp(2.5rem, 1.5rem + 4vw, 4rem);`'],
    ['`hero-actions`: Flujo vertical; botones en Llenar el contenedor', '`.hero-actions { flex-direction: column; align-items: stretch; }`'],
    ['`about-content`, `contact-content`: Flujo vertical', '`flex-direction: column;`'],
    ['`about-graphic`, `contact-list`: Llenar el contenedor', '`flex-basis: auto;` con `align-items: stretch;`'],
    ['`projects-grid`: Flujo vertical', '`repeat(auto-fit, minmax(min(100%, 360px), 1fr))`: una columna sin media query'],
    ['Secciones: Espaciado 16 y 48', '`main { padding: 3rem 1rem; }`'],
], anchos=['46%', '54%'])

d.h2('Así deben quedar tus capas')
d.code('''mi-portafolio                    ← escritorio, 1440: no cambia
mi-portafolio-movil              ← Ancho fijo 390 · Ajustar al contenido
├── Encabezado                   ← Flujo ↓ · Espacio 12
│   ├── Dagner Chuman
│   └── nav-links                ← Espacio 20
├── hero-section                 ← Flujo ↓ · Espaciado 16 y 48
│   ├── hero-left                ← Llenar el contenedor
│   │   ├── Formando a la próxima…     ← 40, centrado
│   │   ├── Docente e Ingeniero…
│   │   └── hero-actions         ← Flujo ↓
│   │       ├── btn-primary      ← Llenar el contenedor
│   │       └── btn-secundary    ← Llenar el contenedor
│   └── hero-right               ← Llenar el contenedor
├── about-section                ← Espaciado 16 y 48
│   └── about-content            ← Flujo ↓
├── projects-section
│   └── projects-grid            ← Flujo ↓
├── contact-section
│   └── contact-content          ← Flujo ↓
│       └── contact-list         ← Llenar el contenedor
└── footer-wrapper               ← Ajustar al contenido
btn-primary                      ← el componente de la sesión 11''', corto=True)

d.h2('Lista de comprobación')
d.check(['`mi-portafolio` sigue intacto, con 1440 de ancho.',
         '`mi-portafolio-movil` mide 390 de ancho y su alto se ajusta al contenido.',
         'Ninguna capa se sale del marco por la derecha.',
         'Todos los marcos que tenían Flujo horizontal con dos columnas tienen Flujo vertical; `nav-links` sigue en horizontal.',
         'Ninguna capa del marco móvil conserva Ancho fijo de 480, 520 o 696.',
         'Las secciones tienen Espaciado 16 y 48; los títulos de sección, 28; el título del Hero, 40.',
         'Los botones del Hero ocupan todo el ancho, uno debajo del otro.'])

d.h2('Errores frecuentes en Figma')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['Un texto se sale por la derecha en una sola línea', 'Está en Ajuste automático de ancho. Cambia su W a Llenar el contenedor: baja de línea'],
    ['Una tarjeta o una fila sigue midiendo 520 o 480', 'Tiene Ancho fijo. Cámbialo a Llenar el contenedor'],
    ['Cambié un valor y también cambió el escritorio', 'Seleccionaste la capa de `mi-portafolio`. En Capas, comprueba que esté dentro de `mi-portafolio-movil`. Si cambiaste el componente principal, cambian los dos: es lo esperado'],
    ['Los botones no se estiran', 'Al cambiar `hero-actions` a vertical, los botones siguen en Ajustar al contenido. Selecciónalos y elige Llenar el contenedor'],
    ['Queda un hueco blanco al final', 'El marco móvil conserva la Altura fija de 2816. Ponle Ajustar al contenido (Parte 6)'],
    ['La imagen de proyecto se ve recortada', 'Su H sigue en 220. Escribe `125`'],
], anchos=['36%', '64%'])
d.callout('Tu diseño ya tiene dos tamaños:', 'el escritorio y el celular. Tus media queries son la lista de diferencias '
          'entre los dos marcos: cada cambio de Flujo, de ancho o de Espaciado que hiciste hoy es una regla del bloque `@media`.')

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Figma_Sesion12_Version_Movil.html'))
print('ok')
