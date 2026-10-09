# -*- coding: utf-8 -*-
"""Guía de Figma · Sesión 15: revisión final, el icono, la vista previa al compartir y la entrega."""
import os
from guia import Doc
from figma_comun import asi_queda, donde_estas, como_leer

d = Doc('Guía de Figma · Sesión 15: revisión final, icono y entrega',
        'Guía de Figma · Sesión 15',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Cierre del proyecto integrador',
        'Revisas el archivo completo antes de entregarlo, diseñas y exportas el icono y la imagen que se ve al '
        'compartir tu sitio, y compartes el diseño con un enlace de solo lectura.')

donde_estas(d, 'Sesión 15')
d.callout('Hoy no se dibuja ninguna sección nueva:', 'el portafolio ya tiene sus tres páginas. Se diseñan dos marcos '
          'pequeños que se exportan como imágenes para el `<head>` de tu HTML.')
como_leer(d)

# ---------------- Parte 1
d.h2('Parte 1 · La revisión final del archivo', salto=True)
d.p('Quien reciba tu enlace verá el panel Capas. Un archivo ordenado se entiende sin explicaciones, igual que un HTML '
    'con buenos nombres de clase. Recorre esta lista de arriba abajo:')
d.tabla(['Qué revisar', 'Dónde', 'Está bien si…'], [
    ['Los nombres', 'Panel Capas', 'Ninguna capa se llama `Frame 12`, `Rectangle 3` o `Group 5`. Cada marco tiene el nombre de la guía'],
    ['La Disposición automática', 'Panel Capas, el icono a la izquierda del nombre', 'Los marcos muestran el icono de tres líneas, no el `#` de un marco libre'],
    ['Las capas ocultas', 'Panel Capas, el ojo de cada fila', 'No quedan capas ocultas ni vacías. Las variantes de un componente sí pueden estar ocultas'],
    ['Los colores', 'Panel derecho › Relleno', 'Muestran el nombre de una variable (`color-primary`), no un código suelto (sesión 14)'],
    ['Los textos', 'El lienzo', 'Son los mismos de tu sitio, con sus tildes. No queda ningún «Lorem ipsum»'],
    ['El orden', 'El lienzo', 'Los marcos están en fila, de izquierda a derecha, y los componentes a un lado'],
], anchos=['22%', '30%', '48%'])
d.h3('1.1 · Compara el diseño con tu sitio publicado')
d.pasos(['Abre tu sitio publicado a 1440 px de ancho y haz una captura de la página de inicio completa.',
         'En Figma, pega la captura con `Ctrl + V` fuera de los marcos y colócala encima de `mi-portafolio`, alineada arriba a la izquierda.',
         'Con la captura seleccionada, baja su **Opacidad** (en Apariencia) a `50%`. Ahora ves el diseño y la web a la vez.',
         'Donde los bordes no coinciden hay una diferencia: anótala y corrige el CSS o la capa. Si no coinciden, manda Figma.',
         'Al terminar, borra la captura con `Supr`.'])
d.callout('Así se revisa en un equipo de verdad:', 'el diseño y la web superpuestos muestran en segundos lo que a simple '
          'vista se escapa: un margen de 8px de más o un título que baja de línea.')

# ---------------- Parte 2
d.h2('Parte 2 · El icono de la pestaña: el marco favicon', salto=True)
d.p('El icono se diseña grande, en 512 × 512, y Figma lo reduce al exportarlo. Son tus iniciales en cian sobre el '
    'fondo oscuro del llamado, los dos colores de tu marca.')
d.pasos(['Fuera de los marcos, en una zona vacía del lienzo, presiona `T` y escribe tus iniciales: `DC`.',
         'Con el texto seleccionado, presiona `Shift + A`. Aparece un marco alrededor: renómbralo `favicon`.',
         'Aplica los valores de los dos bloques siguientes.'])
d.capa('DC', 'el texto, dentro de favicon', [
    ('Tipografía', [('Fuente', '`Outfit`'), ('Grosor de letra', '`ExtraBold`'), ('Tamaño', '`248`'),
                    ('Espaciado entre letras', '`-5%`, con el signo (sugerido)')]),
    ('Relleno', [('Color', 'Variable `color-primary`'), ('Porcentaje', '`100`')]),
])
d.capa('favicon', 'el marco, fuera de los demás', [
    ('Disposición automática', [('W (ancho)', '**Ancho fijo** `512`'), ('H (alto)', '**Altura fija** `512`'),
                                ('Alineación', 'El punto del centro')]),
    ('Apariencia', [('Radio de esquina', '`112` (sugerido)')]),
    ('Relleno', [('Color', 'Variable `color-text-primary`'), ('Porcentaje', '`100`')]),
    ('Recortar contenido', [('Casilla', 'Marcada')]),
])
d.h3('2.1 · La versión para el celular')
d.p('El celular redondea las esquinas del icono por su cuenta. Si ya vienen redondeadas, quedan esquinas blancas.')
d.pasos(['Selecciona `favicon` y presiona `Ctrl + D`. Renombra la copia `apple-touch-icon`.',
         'En la copia, escribe `0` en **Radio de esquina**.'])
d.h3('2.2 · Exporta los dos iconos')
d.pasos(['Selecciona `favicon`. Al final del panel derecho está la sección **Exportar (Export)**: pulsa **+**.',
         'En la fila que aparece, el primer campo es el tamaño: escribe `32w` (32 de ancho). El segundo campo es el sufijo: escribe `-32`. El formato es `PNG`.',
         'Pulsa **Exportar favicon**. Se descarga `favicon-32.png`.',
         'Selecciona `apple-touch-icon`, pulsa **+** en Exportar, escribe `180w`, deja el sufijo vacío y exporta. Se descarga `apple-touch-icon.png`.',
         'Copia los dos archivos en `assets/img/` de tu portafolio, con esos nombres exactos.'])
d.tabla(['Marco en Figma', 'Exportar', 'Archivo', 'En el <head>'], [
    ['`favicon`', '`32w` · sufijo `-32` · PNG', '`favicon-32.png`', '`<link rel="icon" …>`'],
    ['`apple-touch-icon`', '`180w` · PNG', '`apple-touch-icon.png`', '`<link rel="apple-touch-icon" …>`'],
    ['`og-portafolio`', '`1x` · PNG', '`og-portafolio.png`', '`<meta property="og:image" …>`'],
], negrita_primera=False, anchos=['22%', '26%', '24%', '28%'])
d.comprueba('abre `favicon-32.png`: es muy pequeño, pero se leen las dos letras. Si no se leen, sube el tamaño del texto.')

# ---------------- Parte 3
d.h2('Parte 3 · La vista previa al compartir: el marco og-portafolio', salto=True)
d.p('Es la imagen que aparece cuando alguien pega tu enlace en WhatsApp o LinkedIn. Mide 1200 × 630, la proporción '
    'que usan todas esas aplicaciones. Repite el Hero en pequeño: tu nombre, el título y la tarjeta de código.')
d.pasos(['Presiona `F` y dibuja un marco cualquiera fuera de los demás. Renómbralo `og-portafolio`.',
         'Escribe `1200` en W y `630` en H, y presiona `Shift + A`.',
         'Dentro, crea la columna `og-texto` con los textos de la tabla y, a su derecha, pega una copia de `hero-right` (`Ctrl + C` en el Hero, `Ctrl + V` con `og-portafolio` seleccionado).'])
d.capa('og-portafolio', 'el marco, fuera de los demás', [
    ('Disposición automática', [('Flujo', 'Horizontal: el tercer icono, con la flecha →'),
                                ('W (ancho)', '**Ancho fijo** `1200`'), ('H (alto)', '**Altura fija** `630`'),
                                ('Alineación', 'El punto del centro de la columna izquierda'),
                                ('Espacio', '**Auto**'),
                                ('Espaciado › campo izquierdo', '`72`'), ('Espaciado › campo derecho', '`64`')]),
    ('Relleno', [('Color', 'Variable `color-bg`'), ('Porcentaje', '`100`')]),
    ('Recortar contenido', [('Casilla', 'Marcada')]),
])
d.capa('og-texto', 'la columna, dentro de og-portafolio', [
    ('Disposición automática', [('Flujo', 'Vertical: el segundo icono, con la flecha ↓'),
                                ('W (ancho)', '**Ancho fijo** `600`'), ('H (alto)', '**Ajustar al contenido**'),
                                ('Espacio', '`32`')]),
])
d.tabla(['Capa dentro de og-texto', 'Texto', 'Tipografía', 'Relleno'], [
    ['`og-marca`', 'Una copia de `favicon` reducida a 44 × 44 y el texto `Dagner Chuman`', 'Outfit Bold `26`', '`color-text-primary`'],
    ['El título', '`Formando a la próxima generación de desarrolladores web.`', 'Outfit ExtraBold `62` · Altura de la línea `108%`', '`color-text-primary`'],
    ['El subtítulo', '`Docente e Ingeniero · Centro de Informática USS`', 'Geist Regular `24`', '`color-text-secondary`'],
    ['`og-url`', 'Una barra de 120 × 8 (Radio `4`, `color-primary`) y el texto `mi-portafolio-dagner.netlify.app`', 'Geist Medium `22`', '`6B7280`'],
], negrita_primera=False, anchos=['18%', '38%', '26%', '18%'])
d.p('Para reducir la copia de `favicon` sin que el texto quede grande, usa la herramienta **Escala** (`K`) y arrastra '
    'una esquina hasta 44 × 44: escala el marco y su texto a la vez. Ponle `og-marca` al marco horizontal que la '
    'envuelve con el nombre (Espacio `16`, Alineación al centro).')
d.capa('hero-right (copia)', 'la tarjeta de código, dentro de og-portafolio', [
    ('Disposición automática', [('W (ancho)', '**Ancho fijo** `440`'), ('H (alto)', '**Ajustar al contenido**')]),
])
d.h3('3.1 · Exporta la imagen')
d.pasos(['Selecciona `og-portafolio`. En **Exportar**, pulsa **+**, deja `1x` y `PNG`.',
         'Pulsa **Exportar og-portafolio**. Copia `og-portafolio.png` en `assets/img/`.',
         'Revisa su peso: debe quedar por debajo de 600 KB. Si pasa, expórtala en `JPG` y cambia la extensión en `og:image`.'])
d.callout('Los textos de la imagen no se leen en un buscador:', 'por eso el título también va en `og:title` y en el '
          '`<title>` de la página. La imagen es solo para llamar la atención.')

# ---------------- Parte 4
d.h2('Parte 4 · Comparte el diseño y preséntalo', salto=True)
d.h3('4.1 · El enlace de solo lectura')
d.pasos(['Pulsa el botón **Compartir (Share)**, arriba a la derecha.',
         'En el menú de acceso, cambia **Solo personas invitadas (Only people invited)** por **Cualquier persona con el enlace (Anyone with the link)**.',
         'A su derecha, elige **puede ver (can view)**. Nunca **puede editar (can edit)**: cualquiera podría cambiar tu diseño.',
         'Pulsa **Copiar enlace (Copy link)**. Ese es el enlace que entregas.'])
d.comprueba('abre el enlace en una ventana de incógnito. Ves el diseño, pero al hacer clic en una capa no puedes moverla.')
d.h3('4.2 · Presenta el prototipo')
d.p('En la sesión 11 conectaste el botón con su variante Hover y creaste un prototipo. Para mostrarlo en la exposición:')
d.pasos(['Selecciona el marco `mi-portafolio`.',
         'Pulsa el botón **Presentar (Present)**, el triángulo ▷ de la esquina superior derecha. El prototipo se abre en una pestaña nueva.',
         'Pasa el cursor sobre «Ver Proyectos»: cambia al color Hover. Con las flechas `→` y `←` pasas de un marco a otro.',
         'Presiona `Esc` para salir.'])

asi_queda(d, [('06-favicon.png', 'El marco `favicon`: 512 × 512, Radio 112', '28%', None), ('07-og-portafolio.png', 'El marco `og-portafolio`: 1200 × 630', '66%', None)],
          'Así se ven los dos marcos que exportas hoy. `apple-touch-icon` es igual a `favicon`, sin Radio de esquina.')

d.h2('Así deben quedar tus capas')
d.code('''(variables locales)
tokens                               ← 8 colores y 3 números (sesión 14)

mi-portafolio                        ← 1440 · Inicio, Sobre mí, Proyectos y Contacto
mi-portafolio-movil                  ← 390 (sesión 12)
mi-portafolio-cursos                 ← 1440 · la página Cursos (sesiones 13 y 14)

btn-primary                          ← componente: Estado=Predeterminado · Estado=Hover
course-card                          ← componente: Nivel=Básico · Nivel=Intermedio

favicon                              ← 512 × 512 · Radio 112 · exporta 32w con sufijo -32
apple-touch-icon                     ← 512 × 512 · Radio 0   · exporta 180w
og-portafolio                        ← 1200 × 630 · exporta 1x
├── og-texto                         ← Flujo ↓ · Ancho fijo 600 · Espacio 32
│   ├── og-marca
│   ├── Formando a la próxima…
│   ├── Docente e Ingeniero…
│   └── og-url
└── hero-right                       ← copia · Ancho fijo 440''', corto=True)

d.h2('Lista de comprobación')
d.check(['Ninguna capa se llama `Frame`, `Rectangle` o `Group` con un número.',
         'No quedan capas ocultas ni vacías, salvo las variantes de los componentes.',
         'Comparaste `mi-portafolio` con una captura de tu sitio al 50% y corregiste las diferencias.',
         '`favicon` y `apple-touch-icon` miden 512 × 512 y solo el primero tiene Radio de esquina.',
         '`og-portafolio` mide 1200 × 630 y tiene Recortar contenido marcada.',
         'Exportaste `favicon-32.png`, `apple-touch-icon.png` y `og-portafolio.png` con esos nombres.',
         'El enlace de Figma está en **Cualquier persona con el enlace** y **puede ver**.',
         'Presentar abre el prototipo y el botón cambia al pasar el cursor.'])

d.h2('Errores frecuentes en Figma')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['No veo la sección Exportar', 'No hay ninguna capa seleccionada. Selecciona el marco en Capas: la sección está al final del panel derecho'],
    ['El archivo se llama `favicon.png`', 'Falta el sufijo `-32` en la fila de exportación. Renómbralo o vuelve a exportar'],
    ['El icono exportado tiene un borde blanco', 'El marco no tiene Relleno, o el texto es más grande que el marco y Recortar contenido está desmarcada'],
    ['La imagen og-portafolio sale cortada', 'Algún hijo es más grande que el marco. Revisa el Ancho fijo de `og-texto` (600) y de la tarjeta (440)'],
    ['Quien abre el enlace ve «Solicitar acceso»', 'El acceso sigue en **Solo personas invitadas**. Cámbialo a **Cualquier persona con el enlace**'],
    ['Presentar no muestra el cambio de color', 'El prototipo no está conectado. Revisa la Parte 3 de la guía de Figma de la sesión 11'],
], anchos=['36%', '64%'])
d.callout('Cierre del diseño:', 'tu archivo ya tiene el sitio de escritorio, la versión móvil, la página Cursos, los '
          'componentes, las variables y las imágenes para publicar. Es el mismo recorrido que hace un equipo antes de '
          'entregar un proyecto.')

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Figma_Sesion15_Revision_Final_Icono_y_Entrega.html'))
print('ok')
