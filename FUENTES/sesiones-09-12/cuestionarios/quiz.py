# -*- coding: utf-8 -*-
"""Genera los cuestionarios de las sesiones 09 y 10 a partir del de la sesión 07.

Se conserva todo el diseño y la lógica del original; solo cambian los textos de
portada y los dos bancos de preguntas (10 de pretest y 10 de postest).
uso: python3 quiz.py <repo>
"""
import json
import os
import re
import sys

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
BASE = open(os.path.join(REPO, 'SESION 07', 'cuestionario-sesion07.html'), encoding='utf8').read()


def q(sesion, tema, p, o, c, e):
    assert len(o) == 4 and 0 <= c < 4
    return {'sesion': sesion, 'tema': tema, 'p': p, 'o': o, 'c': c, 'e': e}


def banco_js(nombre, preguntas):
    cuerpo = ',\n'.join('      ' + json.dumps(x, ensure_ascii=False) for x in preguntas)
    return f'const {nombre} = [\n{cuerpo}\n    ];'


def lista(items):
    return '\n'.join(f'              <li>{i}</li>' for i in items)


def generar(cfg, salida):
    s = BASE
    rep = [
        ('<title>Cuestionario de la sesión 07 · Diseño Web USS</title>', f'<title>Cuestionario de la sesión {cfg["n"]} · Diseño Web USS</title>'),
        ('Diseño Web <span>Sesión 07</span>', f'Diseño Web <span>Sesión {cfg["n"]}</span>'),
        ('📅 Sesión 07 · Multimedia avanzada en HTML5 y diseño en Figma', f'📅 Sesión {cfg["n"]} · {cfg["tema"]}'),
        ('<h1 id="titulo-principal">Cuestionario de la sesión 07</h1>', f'<h1 id="titulo-principal">Cuestionario de la sesión {cfg["n"]}</h1>'),
        ('<p>Mide lo que recuerdan de las sesiones 01 a 06 antes de comenzar la clase de hoy.</p>', f'<p>{cfg["pre_p"]}</p>'),
        ('<p>Mide lo que aprendieron en la Sesión 07 al finalizar la clase de hoy.</p>', f'<p>{cfg["post_p"]}</p>'),
        ('<span class="test-descripcion-corta" id="desc-tipo-test">Saberes previos (Sesiones 01 a 06)</span>', f'<span class="test-descripcion-corta" id="desc-tipo-test">{cfg["pre_desc"]}</span>'),
        ('? "Saberes previos (Sesiones 01 a 06)"', f'? "{cfg["pre_desc"]}"'),
        (': "Evaluación de salida (Sesión 07 y Figma)";', f': "{cfg["post_desc"]}";'),
        ('"RESULTADOS PRETEST (SESIONES 01 A 06)" : "RESULTADOS POSTEST (SESIÓN 07 Y FIGMA)"', f'"{cfg["pre_badge"]}" : "{cfg["post_badge"]}"'),
        ('"➡️ Ir al Postest (Sesión 07)"', f'"➡️ Ir al Postest (Sesión {cfg["n"]})"'),
        ('"⬅️ Ir al Pretest (Sesiones 01-06)"', f'"⬅️ Ir al Pretest ({cfg["pre_corto"]})"'),
    ]
    for a, b in rep:
        assert a in s, a
        s = s.replace(a, b)
    # listas de las tarjetas de portada
    pre_ini = s.index('<ul class="card-lista">')
    pre_fin = s.index('</ul>', pre_ini)
    s = s[:pre_ini] + '<ul class="card-lista">\n' + lista(cfg['pre_lista']) + '\n            ' + s[pre_fin:]
    post_ini = s.index('<ul class="card-lista">', pre_ini + 30)
    post_fin = s.index('</ul>', post_ini)
    s = s[:post_ini] + '<ul class="card-lista">\n' + lista(cfg['post_lista']) + '\n            ' + s[post_fin:]
    # bancos de preguntas
    for nombre, banco in (('BANCO_PRETEST', cfg['pre']), ('BANCO_POSTEST', cfg['post'])):
        m = re.search(r'const ' + nombre + r' = \[.*?\n    \];', s, re.S)
        assert m, nombre
        s = s[:m.start()] + banco_js(nombre, banco) + s[m.end():]
    s = s.replace('PRETEST (SESIONES 01 A 06) - 10 PREGUNTAS', f'PRETEST ({cfg["pre_corto"].upper()}) - 10 PREGUNTAS')
    s = s.replace('POSTEST (SESIÓN 07 Y FIGMA) - 10 PREGUNTAS', f'POSTEST (SESIÓN {cfg["n"]} Y FIGMA) - 10 PREGUNTAS')
    fuera_de_bancos = re.sub(r'const BANCO_\w+ = \[.*?\n    \];', '', s, flags=re.S)
    assert not re.search(r'[Ss]esi[oó]n 07(?!:</strong>)|SESIÓN 07|01 a 06|01-06', fuera_de_bancos), 'quedan textos de la sesión 07'
    with open(salida, 'w', encoding='utf8') as f:
        f.write(s)
    print('ok', salida)


S09 = dict(
    n='09', tema='CSS3: selectores, cascada y propiedades básicas',
    pre_p='Mide lo que recuerdan de las sesiones 02 a 07 y de Figma antes de empezar con CSS.',
    post_p='Mide lo que aprendieron hoy: CSS3 y el paso de Figma a CSS.',
    pre_desc='Saberes previos (Sesiones 02 a 07 y Figma)', post_desc='Evaluación de salida (Sesión 09 y Figma)',
    pre_badge='RESULTADOS PRETEST (SESIONES 02 A 07)', post_badge='RESULTADOS POSTEST (SESIÓN 09 Y FIGMA)',
    pre_corto='Sesiones 02-07',
    pre_lista=['📌 <strong>Sesiones 02 y 03:</strong> &lt;head&gt;, &lt;link&gt; y &lt;nav&gt;',
               '📌 <strong>Sesión 04:</strong> Rutas relativas',
               '📌 <strong>Sesión 05:</strong> Tablas (&lt;caption&gt;, scope)',
               '📌 <strong>Sesión 06:</strong> Formularios (&lt;label&gt; y for)',
               '📌 <strong>Sesión 07:</strong> Video y JavaScript',
               '🎨 <strong>Figma:</strong> Relleno y Trazo'],
    post_lista=['🎨 <strong>CSS3 (7 preguntas):</strong> sintaxis y selectores',
                '⚖️ <strong>Cascada:</strong> especificidad y herencia',
                '📏 <strong>Unidades y color:</strong> rem y variables',
                '🔲 <strong>Bordes:</strong> tablas con border-collapse',
                '🧩 <strong>Figma a CSS (3 preguntas):</strong> Trazo, Radio y medidas'],
    pre=[
        q('Sesión 02', 'El documento HTML5', '¿Dónde va la etiqueta `<link>` que conecta una hoja de estilos?',
          ['Al final de `<body>`', 'Dentro de `<head>`', 'Dentro de `<header>`', 'Dentro de `<main>`'], 1,
          '`<link>` es un metadato: va en el `<head>`, junto a `<title>` y `<meta>`. No se confunde con `<header>`, que es la cabecera visible de la página.'),
        q('Sesión 03', 'Estructura semántica', 'Tu portafolio tiene dos `<nav>`. ¿Qué atributo los distingue para un lector de pantalla?',
          ['`class`', '`title`', '`aria-label`', '`id`'], 2,
          '`aria-label="Navegacion principal"` y `aria-label="Enlaces rapidos"` dan nombre a cada menú. Hoy usarás ese atributo como selector en CSS.'),
        q('Sesión 04', 'Rutas relativas', 'Desde `index.html`, en la raíz, ¿cuál es la ruta correcta a `global.css` dentro de `assets/css/`?',
          ['`assets/css/global.css`', '`../assets/css/global.css`', '`C:\\Users\\Alumno\\assets\\css\\global.css`', '`global.css`'], 0,
          'La ruta relativa parte de la carpeta del archivo HTML: entra a `assets/`, luego a `css/`. Es la misma lógica que usaste con las imágenes.'),
        q('Sesión 05', 'Tablas accesibles', '¿Qué etiqueta describe una tabla y es lo primero que anuncia un lector de pantalla?',
          ['`<thead>`', '`<th>`', '`<title>`', '`<caption>`'], 3,
          '`<caption>` va justo después de `<table>` y resume su contenido. `<thead>` agrupa las filas de encabezado y `<th>` marca una celda de encabezado.'),
        q('Sesión 05', 'Tablas accesibles', '¿Qué atributo indica que un `<th>` encabeza toda una columna?',
          ['`colspan="1"`', '`scope="col"`', '`rowspan="col"`', '`headers="col"`'], 1,
          '`scope="col"` dice que el encabezado se aplica a la columna; `scope="row"`, a la fila. `colspan` y `rowspan` sirven para combinar celdas.'),
        q('Sesión 06', 'Formularios', '¿Cómo se asocia un `<label>` con su campo para que al pulsar el texto se active el campo?',
          ['`for` en el label e `id` en el campo, con el mismo valor', '`name` en los dos', '`class` en los dos', 'Escribiendo el label justo antes del campo'], 0,
          'El valor de `for` del `<label>` debe coincidir con el `id` del campo. Así funciona también para los lectores de pantalla.'),
        q('Sesión 07', 'Multimedia', '¿Qué atributo de `<video>` muestra una imagen de portada mientras el video no se reproduce?',
          ['`preload`', '`controls`', '`poster`', '`cover`'], 2,
          '`poster` muestra una imagen fija hasta que el video empieza. Sin él, el navegador suele mostrar el primer fotograma.'),
        q('Sesión 07', 'JavaScript', '¿Para qué tiene el video el atributo `id="video-presentacion"`?',
          ['Para darle estilo desde CSS', 'Para que JavaScript lo encuentre con `getElementById`', 'Para que se reproduzca solo', 'Para que el validador lo acepte'], 1,
          '`reproductor.js` busca el video con `document.getElementById("video-presentacion")`. Para dar estilo usaremos clases; los `id` quedan para el script.'),
        q('Figma', 'Panel derecho', 'En Figma, ¿qué sección del panel derecho define el color de fondo de un marco?',
          ['Trazo', 'Efectos', 'Apariencia', 'Relleno'], 3,
          '**Relleno** pinta el fondo del marco (o el color de un texto). En CSS será `background-color` o `color`.'),
        q('Figma', 'Panel derecho', 'En Figma, ¿qué es el **Trazo** de un marco?',
          ['La línea que rodea al marco', 'La sombra del marco', 'El espacio entre sus hijos', 'El relleno interno'], 0,
          'El Trazo es la línea del contorno, con su color y su Peso (grosor). En CSS se escribe con `border`.'),
    ],
    post=[
        q('Sesión 09', 'Anatomía de una regla', 'En la regla `h2 { color: #0B0F19; }`, ¿qué es `color`?',
          ['El selector', 'La propiedad', 'El valor', 'La declaración'], 1,
          '`h2` es el selector, `color` la propiedad, `#0B0F19` el valor, y `color: #0B0F19;` completo es una declaración.'),
        q('Sesión 09', 'Selectores combinados', 'La cabecera tiene un enlace a Contacto en el menú y otro como botón. ¿Qué selector apunta solo al botón?',
          ['`header a`', '`a[href="contactame.html"]`', '`header > a[href="contactame.html"]`', '`nav a`'], 2,
          'El signo `>` exige que el enlace sea hijo directo de `header`. El del menú está dentro de `nav` y `ul`, así que queda fuera.'),
        q('Sesión 09', 'Especificidad', 'Sobre un enlace dentro de `<main>` chocan `a { color: inherit; }` y `main a { color: … }`. ¿Cuál gana?',
          ['`a`, porque está en global.css', 'La que esté escrita primero', 'Ninguna: se mezclan', '`main a`, porque tiene más especificidad'], 3,
          '`main a` tiene dos etiquetas (0-0-2) y `a` solo una (0-0-1). La especificidad se compara antes que el orden.'),
        q('Sesión 09', 'Herencia', '¿Cuál de estas propiedades escrita en `body` baja sola a todos los párrafos?',
          ['`color`', '`padding`', '`border`', '`background-color`'], 0,
          'Las propiedades de texto (`color`, `font-family`, `line-height`…) se heredan. Las de caja (`padding`, `border`, `background`) no.'),
        q('Sesión 09', 'Unidades', 'El título de sección mide 36 px en Figma. ¿Cuánto es en `rem`, con la raíz de 16 px?',
          ['`3.6rem`', '`2.25rem`', '`36rem`', '`1.5rem`'], 1,
          'Para pasar de píxeles a `rem` se divide entre 16: 36 ÷ 16 = 2.25. Por eso `main h2 { font-size: 2.25rem; }`.'),
        q('Sesión 09', 'Variables CSS', '¿Cómo se usa la variable `--color-primary` declarada en `:root`?',
          ['`color: --color-primary;`', '`color: $color-primary;`', '`color: var(--color-primary);`', '`color: root(color-primary);`'], 2,
          'Las variables se declaran con dos guiones y se leen con `var()`. Si cambia el color de la marca, editas una sola línea.'),
        q('Sesión 09', 'Tablas con bordes', '¿Qué hace `border-collapse: collapse` en una tabla?',
          ['Oculta los bordes de la tabla', 'Une los bordes de celdas vecinas en una sola línea', 'Redondea las esquinas', 'Pinta las filas alternas'], 1,
          'Sin `border-collapse`, cada celda dibuja su propio borde y aparecen líneas dobles. Las filas alternas se pintan con `:nth-child(even)`.'),
        q('Figma a CSS', 'Trazo', 'Una tarjeta tiene en Figma Trazo `E5E7EB`, Peso 1. ¿Cómo se escribe en CSS?',
          ['`outline: E5E7EB;`', '`border-color: 1px;`', '`stroke: 1px #E5E7EB;`', '`border: 1px solid #E5E7EB;`'], 3,
          '`border` lleva grosor, estilo y color. En el portafolio se escribe con la variable: `border: 1px solid var(--color-border);`.'),
        q('Figma a CSS', 'Radio de esquina', 'El Radio de esquina 12 de las tarjetas de Figma, ¿qué propiedad es en CSS?',
          ['`border-radius: 12px;`', '`corner: 12px;`', '`radius: 12;`', '`border: 12px round;`'], 0,
          '`border-radius` redondea las esquinas. Con `50%` una caja cuadrada se vuelve círculo, como la foto de perfil.'),
        q('Figma', 'Medidas', '`mi-portafolio` mide 1440. Proyectos tiene Espaciado 80 a cada lado y Espacio 24 entre dos tarjetas iguales. ¿Cuánto mide cada tarjeta?',
          ['640', '720', '628', '600'], 2,
          '1440 − 80 − 80 = 1280 de ancho útil. Menos los 24 de Espacio quedan 1256, y entre dos tarjetas, 628 cada una.'),
    ],
)

S10 = dict(
    n='10', tema='Modelo de caja, Flexbox y Grid',
    pre_p='Mide lo que recuerdan de la sesión 09 (CSS3) antes de empezar a maquetar.',
    post_p='Mide lo que aprendieron hoy: modelo de caja, Flexbox, Grid y su relación con Figma.',
    pre_desc='Saberes previos (Sesión 09: CSS3)', post_desc='Evaluación de salida (Sesión 10 y Figma)',
    pre_badge='RESULTADOS PRETEST (SESIÓN 09)', post_badge='RESULTADOS POSTEST (SESIÓN 10 Y FIGMA)',
    pre_corto='Sesión 09',
    pre_lista=['🔗 <strong>Enlazar:</strong> el orden de las hojas de estilo',
               '⚖️ <strong>Cascada:</strong> especificidad y herencia',
               '📏 <strong>Unidades:</strong> rem y em',
               '🎨 <strong>Color:</strong> hexadecimal y rgba',
               '🔲 <strong>Bordes:</strong> border, border-radius y outline',
               '🧩 <strong>Figma:</strong> Relleno de un texto'],
    post_lista=['📦 <strong>Modelo de caja (3 preguntas):</strong> padding, box-sizing y display',
                '↔️ <strong>Flexbox (3 preguntas):</strong> contenedor, ejes y flex: 1',
                '▦ <strong>Grid (1 pregunta):</strong> columnas con fr',
                '🧩 <strong>Figma a CSS (3 preguntas):</strong> Espacio Auto, Recortar contenido y modo Llenar'],
    pre=[
        q('Sesión 09', 'Enlazar hojas de estilo', '¿En qué orden se enlazan las hojas de estilo en las páginas interiores?',
          ['`contenido.css`, `header.css`, `global.css`', '`global.css`, `header.css`, `contenido.css`', '`header.css`, `global.css`, `contenido.css`', 'El orden no importa'], 1,
          'De lo general a lo particular: `global.css` define las variables que usan las demás, y lo particular va al final para poder ajustar lo anterior.'),
        q('Sesión 09', 'Especificidad', '¿Cuál de estos selectores tiene más especificidad?',
          ['`img`', '`main img`', '`main section img`', '`.foto-perfil`'], 3,
          'Una clase (0-1-0) gana a cualquier cantidad de etiquetas: `main section img` es 0-0-3.'),
        q('Sesión 09', 'Herencia', '¿Por qué escribimos `font: inherit` en los botones y en los campos del formulario?',
          ['Porque no heredan la letra de la página: el navegador les pone la suya', 'Para que el texto sea más grande', 'Para que pasen el validador', 'Porque `font-family` no existe en CSS'], 0,
          'Botones y campos traen estilos propios del navegador y una regla directa gana a lo heredado. `font: inherit` les pide la letra del resto del sitio.'),
        q('Sesión 09', 'Unidades', 'Con la raíz de 16 px, ¿cuántos píxeles son `1.5rem`?',
          ['15 px', '1.5 px', '24 px', '32 px'], 2,
          '1.5 × 16 = 24. Es el Espaciado 24 de las tarjetas de Figma, escrito como `padding: 1.5rem;`.'),
        q('Sesión 09', 'Color', '¿Qué significa `rgba(6, 182, 196, 0.35)`?',
          ['El azul de la marca con 35 % de opacidad', 'Un color al azar', 'El azul con 35 % más de brillo', 'Un degradado de tres colores'], 0,
          'Son los mismos números del `#06B6C4` en rojo, verde y azul, más la opacidad: 0.35. Lo usa la sombra del botón azul.'),
        q('Sesión 09', 'Bordes', '¿Qué valor de `border-radius` convierte una imagen cuadrada en un círculo?',
          ['`100px`', '`50%`', '`circle`', '`1rem`'], 1,
          '`50%` redondea cada esquina la mitad del lado. Si la imagen no es cuadrada, el resultado es un óvalo.'),
        q('Sesión 09', 'Bordes', 'La cabecera solo tiene línea abajo, como el Trazo inferior de Figma. ¿Qué propiedad usas?',
          ['`border: bottom;`', '`outline-bottom`', '`underline`', '`border-bottom`'], 3,
          '`border-bottom: 1px solid var(--color-border);` dibuja solo el borde inferior. El pie usa `border-top`.'),
        q('Sesión 09', 'Pseudo-clases', '¿A qué filas se aplica `tbody tr:nth-child(even)`?',
          ['A la primera fila', 'A las filas pares', 'A las filas impares', 'A la última fila'], 1,
          '`even` son las pares y `odd`, las impares. Así se pintan filas alternas en la tabla de herramientas.'),
        q('Sesión 09', 'Contorno', '¿En qué se diferencia `outline` de `border`?',
          ['No hay diferencia', '`outline` solo funciona en enlaces', '`outline` se dibuja por fuera y no cambia el tamaño de la caja', '`outline` siempre es azul'], 2,
          'El contorno no ocupa espacio en el modelo de caja. Por eso lo usamos en `:focus-visible` para mostrar el foco del teclado.'),
        q('Figma', 'Relleno de un texto', 'En Figma, un texto tiene Relleno `374151`. ¿Qué propiedad de CSS es?',
          ['`color`', '`background-color`', '`fill`', '`font-color`'], 0,
          'En un texto, el Relleno es el color de las letras: `color`. En un marco, el Relleno es su fondo: `background-color`.'),
    ],
    post=[
        q('Sesión 10', 'Modelo de caja', '¿Qué capa del modelo de caja está entre el contenido y el borde?',
          ['margin', 'padding', 'outline', 'gap'], 1,
          'De adentro hacia afuera: contenido, padding, borde y margen. El padding es el Espaciado de Figma y toma el fondo de la caja.'),
        q('Sesión 10', 'box-sizing', 'Con `box-sizing: border-box`, una caja con `width: 300px`, `padding: 24px` y `border: 1px` mide en total…',
          ['350 px', '324 px', '348 px', '300 px'], 3,
          'Con `border-box` el ancho incluye el padding y el borde. Con `content-box`, el valor por defecto, mediría 300 + 48 + 2 = 350.'),
        q('Sesión 10', 'display', 'Un `<span class="dot">` no toma su `width: 10px` ni su `height: 10px`. ¿Por qué?',
          ['Porque un elemento inline ignora width y height', 'Porque falta `border`', 'Porque los span no aceptan clases', 'Porque falta `position`'], 0,
          'Un `span` es `inline`. Con `display: inline-block` sigue en la línea pero acepta ancho y alto.'),
        q('Sesión 10', 'Flexbox', 'Quieres el logotipo, el menú y el botón de la cabecera en una fila. ¿Dónde escribes `display: flex`?',
          ['En cada uno de los tres hijos', 'En el `body`', 'En el `header`, el padre de los tres', 'En el `nav`'], 2,
          'Flexbox se escribe en el contenedor. Sus hijos directos son los que se ordenan.'),
        q('Sesión 10', 'Los dos ejes', 'Un contenedor tiene `flex-direction: column`. ¿Qué propiedad centra a sus hijos en horizontal?',
          ['`justify-content: center`', '`text-align: center`', '`align-items: center`', '`margin: auto`'], 2,
          'Con `column`, el eje principal es vertical. `justify-content` trabaja en el principal y `align-items` en el cruzado, que ahora es el horizontal.'),
        q('Sesión 10', 'flex: 1', '¿Qué hace `flex: 1` en `.hero-left`?',
          ['La columna toma el espacio que sobra en la fila', 'La columna mide 1 px', 'La columna se oculta', 'La columna pasa a la primera posición'], 0,
          '`flex: 1` es el **Llenar el contenedor** de Figma: el ítem crece para ocupar el espacio libre.'),
        q('Sesión 10', 'Grid', '¿Qué resultado da `grid-template-columns: repeat(2, 1fr);`?',
          ['Dos filas iguales', 'Dos columnas iguales', 'Una columna de 2 px', 'Dos columnas de 1 px'], 1,
          '`fr` es una fracción del espacio libre: dos de `1fr` miden lo mismo. Así se reparten las tarjetas de proyectos.'),
        q('Figma a CSS', 'Espacio Auto', 'En Figma, la cabecera tiene **Espacio: Auto**. ¿Qué propiedad de CSS es?',
          ['`gap: auto;`', '`margin: auto;`', '`align-items: stretch;`', '`justify-content: space-between;`'], 3,
          'Espacio Auto separa a los hijos hacia los extremos: eso hace `justify-content: space-between` en el eje principal.'),
        q('Figma a CSS', 'Recortar contenido', 'La casilla **Recortar contenido** de una tarjeta de Figma, ¿qué propiedad es en CSS?',
          ['`overflow: hidden;`', '`display: none;`', '`clip: auto;`', '`visibility: hidden;`'], 0,
          '`overflow: hidden` recorta lo que se sale de la caja. Así la imagen de proyecto respeta las esquinas redondeadas.'),
        q('Figma a CSS', 'Imágenes', 'En Figma, la imagen del proyecto está en modo **Llenar**. ¿Qué propiedad hace lo mismo con una `<img>`?',
          ['`background-size: 100%;`', '`object-fit: cover;`', '`width: auto;`', '`image-fill: cover;`'], 1,
          '`object-fit: cover` llena la caja sin deformar la imagen y recorta lo que sobra.'),
    ],
)

if __name__ == '__main__':
    generar(S09, os.path.join(REPO, 'SESION 09', 'cuestionario-sesion09.html'))
    generar(S10, os.path.join(REPO, 'SESION 10', 'cuestionario-sesion10.html'))
