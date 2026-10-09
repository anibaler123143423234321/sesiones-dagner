# -*- coding: utf-8 -*-
"""Piezas comunes de las guías de Figma (formato de la versión 5)."""
from guia import fmt


def donde_estas(d, hoy):
    filas = [
        ['Sesiones 05 y 06', '1 al 6', 'Marco principal, cabecera, menú y el marco `hero-section`'],
        ['Sesión 07', '7 al 9', 'El Hero completo: columna de texto, botones y tarjeta de código'],
        ['Sesión 08', '—', 'Feriado del 8 de octubre: no hubo clase'],
        ['Sesión 09', '10 y 11', 'Sobre mí y Proyectos'],
        ['Sesión 10', '12 al 14', 'Contacto, pie de página e imágenes'],
    ]
    # Las sesiones 11 y 12 van más allá del manual: solo aparecen en sus propias guías
    if hoy in ('Sesión 11', 'Sesión 12', 'Sesión 13', 'Sesión 14', 'Sesión 15'):
        filas += [
            ['Sesión 11', 'Ampliación', 'El botón como componente, su variante Hover y el prototipo'],
            ['Sesión 12', 'Ampliación', 'La versión móvil de la página, en un marco de 390'],
        ]
    if hoy in ('Sesión 13', 'Sesión 14', 'Sesión 15'):
        filas += [
            ['Sesión 13', 'Ampliación', 'La cuadrícula de 12 columnas y la página Cursos'],
            ['Sesión 14', 'Ampliación', 'Las variables de color y medida, y el componente de curso'],
        ]
    if hoy == 'Sesión 15':
        filas.append(['Sesión 15', 'Cierre', 'La revisión final, el icono, la vista previa al compartir y la entrega'])
    for f in filas:
        if f[0] == hoy:
            f[0] = f'**{hoy} (hoy)**'
            f[1] = f'**{f[1]}**'
            f[2] = f'**{f[2]}**'
    d.h3('Dónde estás')
    d.tabla(['Cuándo', 'Pasos del manual', 'Qué construyes'], filas, negrita_primera=False, anchos=['24%', '20%', '56%'])
    d.callout('Si ya tienes una capa creada:', 'no la crees otra vez. Selecciónala, compara sus valores con el bloque de '
              'esa capa y corrige lo que no coincida.')
    d.callout('Sobre los nombres:', 'esta guía usa `mi-portafolio` para el marco principal y `Encabezado` para la cabecera. '
              'En el manual se llaman `portafolio-dagner-chuman` y `Header`: son las mismas capas.')


def como_leer(d):
    d.h2('Cómo leer esta guía')
    d.p('Cada bloque de valores tiene la misma forma. En la primera línea está la capa que debes seleccionar en el panel '
        'Capas. Debajo van las secciones del panel derecho, en el mismo orden en que aparecen en Figma, y en cada una el '
        'campo y el valor exacto que debes poner.')
    d.tabla(['Regla', 'Qué significa'], [
        ['Espacio no es Espaciado', '**Espacio** es la separación entre los elementos que están dentro del marco. **Espaciado** es el relleno interno: la distancia entre el borde del marco y su contenido'],
        ['Los dos campos de Espaciado', 'El campo izquierdo es el horizontal (izquierda y derecha). El campo derecho es el vertical (arriba y abajo)'],
        ['Color y porcentaje', 'En Relleno y en Trazo van dos datos: el color y, a su derecha, el porcentaje. El porcentaje es siempre `100`. Si el ojo de esa fila está tachado, el color existe pero está oculto'],
        ['Opacidad', 'En Apariencia, la Opacidad de toda capa es `100%`'],
        ['El signo %', 'En Altura de la línea escribe el valor con el signo: `160%`. Sin el signo, Figma lo toma como 160 píxeles por línea'],
        ['W y H', 'Son los campos del ancho y del alto. Al abrir el menú de cada campo: **Ajustar al contenido**, la capa mide lo que su contenido; **Llenar el contenedor**, se estira hasta ocupar su marco padre; un número, medida fija'],
        ['Los campos de Tipografía', 'La fuente es el primer menú; debajo, a la izquierda, el grosor de letra (Regular, Medium, SemiBold, Bold, ExtraBold); a su derecha, el tamaño'],
        ['Peso', 'En Trazo, el grosor de la línea es el campo Peso'],
        ['Flujo', 'La fila tiene cuatro iconos. Vertical es el segundo, con la flecha ↓. Horizontal es el tercero, con la flecha →. Al pasar el cursor aparece el nombre'],
        ['Textos copiados', 'Un texto copiado desde este PDF llega partido en varias líneas. Después de pegarlo, borra los saltos de línea'],
        ['La marca «sugerido»', 'El manual no fija ese valor. Es una propuesta: puedes cambiarla'],
    ], anchos=['26%', '74%'])
    d.h3('Primero el contenido, después el marco')
    d.p('En esta guía, casi todos los marcos se crean alrededor de algo que ya existe: escribes el texto o dibujas la '
        'figura y después presionas `Shift + A`. Así el marco nace del tamaño de su contenido y dentro del lugar correcto. '
        '`Shift + A` hace una de estas tres cosas, según lo que tengas seleccionado:')
    d.tabla(['Si tienes seleccionado', 'Shift + A hace esto'], [
        ['Un texto, una figura o varias capas', 'Crea un marco nuevo que las envuelve. En Capas aparece con un nombre como `Frame 1` o `Marco 1`: haz doble clic sobre el nombre y escribe el que indica la guía'],
        ['Un marco que ya tiene Disposición automática', 'Crea otro marco nuevo que lo envuelve. Sirve para meter una tarjeta dentro de su lista'],
        ['Un marco recién dibujado con F', 'No crea nada nuevo: le activa la Disposición automática a ese mismo marco. Se usa solo en marcos de medida fija o con Espaciado'],
    ], anchos=['36%', '64%'])
    d.callout('Si Shift + A no crea un marco nuevo:', 'mira el panel de capas. Si después de presionarlo no aparece un marco '
              'nuevo alrededor de lo que tenías seleccionado, deshaz con `Ctrl + Z`, presiona `Ctrl + Alt + G` para '
              'enmarcar la selección (en Mac, `Cmd + Option + G`) y, con ese marco seleccionado, presiona `Shift + A`.')
    d.p('Para seleccionar varias capas: en Capas, haz clic en la primera y, con Shift pulsado, en la última. Atajos: `F` crea '
        'un marco, `T` un texto, `O` un círculo, `R` un rectángulo, `Shift + A` activa la Disposición automática y '
        '`Ctrl + D` duplica (en Mac, `Cmd + D`).')


# Bloques de valores reutilizados
def seccion_base(d, nombre, donde):
    d.capa(nombre, donde, [
        ('Disposición automática', [('Flujo', 'Vertical: el segundo icono, con la flecha ↓'),
                                    ('W (ancho)', 'Abre el menú y elige **Llenar el contenedor**'),
                                    ('H (alto)', '**Ajustar al contenido**'),
                                    ('Alineación', 'El punto de arriba a la izquierda'),
                                    ('Espacio', '`48`'),
                                    ('Espaciado › campo izquierdo', '`80` (horizontal)'),
                                    ('Espaciado › campo derecho', '`100` (vertical)'),
                                    ('Recortar contenido', 'Casilla desmarcada')]),
        ('Apariencia', [('Opacidad', '`100%`')]),
        ('Relleno', [('Color', '`FFFFFF`'), ('Porcentaje', '`100`')]),
    ])


def titulo_seccion(d, texto, donde):
    d.capa(texto, donde, [
        ('Disposición', [('Redimensionar (tres iconos)', 'El primero: **Ajuste automático de ancho**')]),
        ('Tipografía', [('Fuente', '`Outfit`'), ('Grosor de letra', '`ExtraBold`'), ('Tamaño', '`36`'),
                        ('Alineación', 'Izquierda: el primer icono')]),
        ('Relleno', [('Color', '`0B0F19`'), ('Porcentaje', '`100`')]),
        ('Apariencia', [('Opacidad', '`100%`')]),
    ])


def marco_envoltorio(d, nombre, donde, flujo, w, alineacion, espacio, extra_w=None):
    flujo_txt = 'Vertical: el segundo icono, con la flecha ↓' if flujo == 'v' else 'Horizontal: el tercer icono, con la flecha →'
    d.capa(nombre, donde, [
        ('Disposición automática', [('Flujo', flujo_txt), ('W (ancho)', w), ('H (alto)', '**Ajustar al contenido**'),
                                    ('Alineación', alineacion), ('Espacio', espacio),
                                    ('Espaciado › campo izquierdo', '`0`'), ('Espaciado › campo derecho', '`0`')]),
        ('Apariencia', [('Opacidad', '`100%`')]),
        ('Relleno', [('Color', 'Ninguno: si hay uno, quítalo con −')]),
    ])


def texto_bloque(d, nombre, donde, w, fuente, grosor, tam, color, alto_linea=None, alineacion='Izquierda: el primer icono'):
    tip = [('Fuente', fuente), ('Grosor de letra', grosor), ('Tamaño', tam)]
    if alto_linea:
        tip.append(('Altura de la línea', alto_linea))
    tip.append(('Alineación', alineacion))
    disp = [('W (ancho)', 'Abre el menú del campo y elige **Llenar el contenedor**')] if w == 'llenar' else \
        [('Redimensionar (tres iconos)', 'El primero: **Ajuste automático de ancho**')]
    d.capa(nombre, donde, [
        ('Disposición', disp),
        ('Tipografía', tip),
        ('Relleno', [('Color', color), ('Porcentaje', '`100`')]),
        ('Apariencia', [('Opacidad', '`100%`')]),
    ])


def esquema(d, hoy):
    """Esquema de la página con las secciones de hoy resaltadas. hoy: 's09' o 's10'."""
    def sec(clase, tit, der, cuerpo=''):
        if clase == 'hoy':
            return f'<div class="s hoy"><div class="tit"><span>{tit}</span><span>{der}</span></div>{cuerpo}</div>'
        return f'<div class="s {clase}"><span><b>{tit}</b></span><span>{der}</span></div>'

    about = ('<div class="fila"><div class="caja">Sobre mí · Outfit ExtraBold 36</div></div>'
             '<div class="fila" style="margin-top:5px"><div class="caja" style="flex:1;height:46px"><b>Título secundario 22</b><br>'
             '<span class="pie">Párrafos · Geist Regular 16 · #374151</span></div><span class="num">64</span>'
             '<div class="caja" style="width:200px"><b>Gráfico HTML · 480 × 264</b><br><span class="pie">&lt;header&gt; &lt;main&gt; &lt;section&gt; &lt;footer&gt;</span></div></div>')
    proyectos = ('<div class="fila"><div class="caja">Proyectos · Outfit ExtraBold 36</div></div>'
                 '<div class="fila" style="margin-top:5px"><div class="caja" style="flex:1;padding:0"><div class="gris" style="padding:9px">Imagen · 628 × 220</div>'
                 '<div style="padding:4px 7px"><b>Ecosistema CINF USS</b><br><span class="pie">Tarjeta 628 × 475 · Radio 12 · Espaciado 24</span></div></div>'
                 '<span class="num">24</span><div class="caja" style="flex:1;padding:0"><div class="gris" style="padding:9px">Imagen · 628 × 220</div>'
                 '<div style="padding:4px 7px"><b>Generador de Certificados Web</b><br><span class="pie">Tarjeta 628 × 475 · Radio 12 · Espaciado 24</span></div></div></div>')
    contacto = ('<div class="fila"><div class="caja" style="flex:1;height:62px"><b>Título y texto de contacto</b><br><span class="pie">Lado izquierdo</span></div>'
                '<span class="num">64</span><div style="width:210px;display:flex;flex-direction:column;gap:3px">'
                '<div class="caja">● Correo · fila de 520 × 84</div><div class="caja">● LinkedIn · fila de 520 × 84</div>'
                '<div class="caja">● GitHub · fila de 520 × 84</div><span class="pie">Lado derecho · Ancho fijo 520 · Espacio 16</span></div></div>')
    pie = '<div class="fila"><div class="caja" style="flex:1;text-align:center">© 2026 Dagner Chuman | Centro de Informática USS Protech XP. · Geist Regular 13</div></div>'
    partes = [sec('prev', 'Encabezado', 'Altura fija 80 · Pasos 2 al 5'),
              sec('prev', 'hero-section', 'Pasos 6 al 9 · sesión 07')]
    if hoy == 's09':
        partes += [sec('hoy', 'about-section · Paso 10', 'Espaciado 80 y 100 · Espacio 48 · Relleno FFFFFF', about),
                   sec('hoy', 'projects-section · Paso 11', 'Espaciado 80 y 100 · Espacio 48 · Relleno FFFFFF', proyectos),
                   sec('', 'contact-section · Paso 12', 'sesión 10'),
                   sec('', 'footer-wrapper · Paso 13', 'sesión 10')]
    else:
        partes += [sec('prev', 'about-section', 'Paso 10 · sesión 09'),
                   sec('prev', 'projects-section', 'Paso 11 · sesión 09 · imágenes en el Paso 14'),
                   sec('hoy', 'contact-section · Paso 12', 'Espaciado 80 y 100 · Espacio 48 · Relleno FFFFFF', contacto),
                   sec('hoy', 'footer-wrapper · Paso 13', 'Altura fija 182 · Espaciado 80 y 48 · Trazo superior', pie)]
    d.raw('<div class="esq nobreak"><div class="rot">mi-portafolio · 1440 × 2816 (no está a escala)</div>' + ''.join(partes) + '</div>')
    d.raw(f'<p class="leyenda">{fmt("Las capas resaltadas son las de hoy. Los números en color son valores de **Espacio**.")}</p>')


# Capturas del archivo de muestra «Mi portafolio (Copia) · Completo» (SESION 15/figma-portafolio-completo)
def asi_queda(d, capturas, texto):
    """capturas: [(archivo, pie, ancho, alto_max)]. Lee las imágenes de <repo>/SESION 15/figma-portafolio-completo,
    con <repo> como primer argumento del script (por defecto, /home/user/sesiones-dagner)."""
    import base64
    import os
    import sys
    repo = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
    carpeta = os.path.join(repo, 'SESION 15', 'figma-portafolio-completo')
    d.h2('Así queda en el archivo de muestra', salto=True)
    d.p(texto)
    figuras = []
    for archivo, pie, ancho, alto_max in capturas:
        datos = base64.b64encode(open(os.path.join(carpeta, archivo), 'rb').read()).decode()
        estilo = f'width:100%;border:1px solid #CFD5D9;border-radius:6px;display:block'
        if alto_max:
            estilo += f';max-height:{alto_max};object-fit:cover;object-position:top'
        figuras.append(f'<figure style="margin:0;flex:0 0 {ancho}"><img src="data:image/png;base64,{datos}" alt="" '
                       f'style="{estilo}"><figcaption style="font-size:8.5pt;color:#6B7378;margin-top:3px">{fmt(pie)}'
                       '</figcaption></figure>')
    d.raw('<div style="display:flex;gap:12px;align-items:flex-start;flex-wrap:wrap;margin:8px 0 12px">' + ''.join(figuras) + '</div>')
    d.callout('Es el diseño terminado:', 'el docente puede mostrarte el archivo completo en clase. Compáralo con el '
              'tuyo capa por capa: si un valor no coincide, manda el manual.')
