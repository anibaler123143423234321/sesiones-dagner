# -*- coding: utf-8 -*-
"""Examen final · Parte B: la ficha técnica del caso práctico, para los estudiantes.
uso: python3 ficha_parte_b.py <carpeta-de-capturas>
     (las capturas salen de shot_ef.js sobre SESION 16/docente/solucion-parte-b)
"""
import base64
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'guias'))
from guia import Doc  # noqa: E402

CAPTURAS = sys.argv[1] if len(sys.argv) > 1 else AQUI


def imagen(archivo, ancho, alt):
    datos = base64.b64encode(open(os.path.join(CAPTURAS, archivo), 'rb').read()).decode()
    return (f'<img src="data:image/png;base64,{datos}" alt="{alt}" '
            f'style="width:{ancho};border:1px solid #CFD5D9;border-radius:6px;display:block">')


d = Doc('Examen final · Parte B: caso práctico',
        'Examen final · Parte B · Ficha técnica',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 16 · Jueves 05/11/2026 · Aula Virtual USS',
        'Construyes una página de una sola vista para un evento del Centro de Informática, con HTML semántico, CSS '
        'externo y diseño adaptable. Tienes 80 minutos y vale 10 de los 20 puntos del examen.')

d.h3('Lo que entregas')
d.tabla(['Qué', 'Cómo'], [
    ['Una carpeta comprimida', '`apellido-nombre-ef.zip`, subida a la tarea **Examen final · Parte B** del Aula Virtual'],
    ['Dentro de la carpeta', '`index.html` y `assets/css/estilos.css`. Si usas Bootstrap, enlázalo desde el CDN, como en la página Cursos'],
    ['Opcional', 'Si la publicas en Netlify, escribe la dirección en el comentario de la entrega'],
], anchos=['26%', '74%'])
d.callout('Puedes consultar:', 'tu portafolio, las guías del curso y la documentación oficial (MDN y getbootstrap.com). '
          'El trabajo es individual: no se permite comunicarse con otras personas durante el examen.')

d.h2('Así debe verse', salto=True)
d.raw('<div style="display:flex;gap:14px;align-items:flex-start;break-inside:avoid">'
      f'<div style="flex:0 0 70%">{imagen("ef-parte-b-1440.png", "100%", "La página a 1440 px")}'
      '<p style="font-size:8.5pt;color:#6B7378;margin-top:4px">Escritorio · 1440 px</p></div>'
      f'<div style="flex:1">{imagen("ef-parte-b-390.png", "100%", "La página a 390 px")}'
      '<p style="font-size:8.5pt;color:#6B7378;margin-top:4px">Celular · 390 px</p></div></div>')

d.h2('El contenido, sección por sección', salto=True)
d.p('Copia los textos tal como están. Las etiquetas indicadas son obligatorias.')
d.tabla(['Sección', 'Etiquetas', 'Contenido'], [
    ['Cabecera', '`header`, `nav` con `ul`', 'El nombre `SemInfo USS` («USS» en cian) a la izquierda y dos enlaces a la derecha: `Charlas` (a `#charlas`) e `Inscripción` (a `#inscripcion`)'],
    ['Presentación', '`main` › `section`, un solo `h1`', '`Del 16 al 18 de noviembre · Auditorio del Centro de Informática` · título `Semana de la Informática 2026` · `Tres charlas gratuitas para dar el siguiente paso en el desarrollo web.` · botón `Inscríbete` (enlace a `#inscripcion`)'],
    ['Charlas', '`section id="charlas"`, `h2`, tres `article` con `h3`', '**Lunes 16 · 6:00 p. m.** Del diseño en Figma al código: Cómo leer la Disposición automática y llevarla a Flexbox. **Martes 17 · 6:00 p. m.** Bootstrap en diez minutos: La grilla, las utilidades y un tema con tus colores. **Miércoles 18 · 6:00 p. m.** Publica tu sitio hoy: Pruebas, Lighthouse y despliegue en Netlify.'],
    ['Inscripción', '`section id="inscripcion"`, `form`', 'Nombre completo (texto) · Correo electrónico (`email`) · Charla (`select` con las tres charlas). Los tres con `label` y `required`. Botón `Enviar inscripción`'],
    ['Pie', '`footer`', '`© 2026 Centro de Informática USS · Protech XP`'],
], anchos=['16%', '28%', '56%'])

d.h2('Los valores de diseño')
d.p('Escríbelos como variables en `:root` y úsalos con `var()`.')
d.tabla(['Variable', 'Valor', 'Dónde'], [
    ['`--color-primary`', '`#06B6C4`', 'El botón, «USS», las fechas y el hover del menú'],
    ['`--color-primary-hover`', '`#05A3B0`', 'El botón al pasar el cursor'],
    ['`--color-text`', '`#0B0F19`', 'Títulos y el texto del botón'],
    ['`--color-text-secondary`', '`#374151`', 'Párrafos'],
    ['`--color-bg`', '`#F9FAFB`', 'El fondo de la página'],
    ['`--color-surface`', '`#FFFFFF`', 'Cabecera, tarjetas, formulario y pie'],
    ['`--color-border`', '`#E5E7EB`', 'Bordes de 1px'],
    ['`--font-heading` · `--font-body`', '`Outfit` (700 y 800) · `Geist` (400 y 500)', 'Títulos · textos. Desde Google Fonts'],
    ['`--radius`', '`12px`', 'Tarjetas y formulario. El botón y los campos llevan `8px`'],
], anchos=['30%', '30%', '40%'])
d.tabla(['Elemento', 'Medidas'], [
    ['Cabecera', 'Relleno `20px 80px`, borde inferior, nombre y menú en extremos opuestos, centrados en vertical. Espacio de `32px` entre los enlaces'],
    ['Presentación', 'Centrada, relleno `96px 80px`. Título de 36 a 56px con `clamp()`, peso 800'],
    ['Botón', 'Relleno `14px 24px`, fondo cian, texto oscuro. En el hover: cian oscuro y sube `2px`, con `transition` de `0.2s`'],
    ['Charlas', 'Tres columnas iguales con Espacio de `24px`. Cada tarjeta: relleno `24px`, borde y radio de `12px`'],
    ['Formulario', 'Una columna, ancho máximo `480px`, relleno `24px`. Campos con relleno `12px`'],
    ['Celular (hasta 600px)', 'Relleno lateral de `16px`; la cabecera en columna; las charlas en una sola columna; sin barra horizontal a 390px'],
], anchos=['24%', '76%'])

d.h2('Cómo se califica la Parte B')
d.tabla(['Criterio', 'Logrado (2)', 'En proceso (1)', 'No logrado (0)'], [
    ['Estructura semántica', '`header`, `nav`, `main`, `section`, `article` y `footer`; un solo `h1`; títulos en orden; HTML sin errores en el validador', 'Usa etiquetas semánticas, pero falta una o hay errores en el validador', 'Todo con `div` o sin estructura'],
    ['Estilos y variables', 'CSS externo en `assets/css/`, los valores de la ficha como variables en `:root`, las dos fuentes enlazadas', 'CSS externo con algunos valores escritos a mano', 'Estilos en línea o sin CSS'],
    ['Maquetación', 'Cabecera con Flexbox; las charlas en `grid` o en la grilla de Bootstrap; medidas de la ficha', 'La maquetación funciona, pero no respeta las medidas', 'Los elementos quedan uno debajo del otro sin orden'],
    ['Diseño adaptable', '`viewport`, una media query (o clases de Bootstrap) que pasa las charlas a una columna; sin barra horizontal a 390px', 'Se adapta en parte o aparece barra horizontal', 'No se adapta al celular'],
    ['Interacción y formulario', 'Hover con `transition` en el botón y en el menú; los tres campos con `label`, `name` y `required`; `type="email"` en el correo', 'Falta el hover o un `label`', 'Formulario sin etiquetas o sin hover'],
], anchos=['20%', '34%', '26%', '20%'])

d.h3('Cómo repartir los 80 minutos')
d.tabla(['Minutos', 'Qué haces'], [
    ['0 a 10', 'La carpeta, `index.html` con toda la estructura y los textos'],
    ['10 a 40', 'Variables, reset, cabecera, presentación, botón y charlas'],
    ['40 a 55', 'El formulario y el pie'],
    ['55 a 65', 'La media query del celular. Prueba a 390px con `F12`'],
    ['65 a 75', 'Valida el HTML y el CSS en el W3C y corrige'],
    ['75 a 80', 'Comprime la carpeta y súbela. **No dejes la entrega para el último minuto**'],
], anchos=['18%', '82%'])
d.check(['La carpeta se llama `apellido-nombre-ef` y tiene `index.html` en su raíz.',
         'El HTML y el CSS pasan los validadores sin errores.',
         'Los colores y las fuentes salen de variables en `:root`.',
         'A 390px no hay barra horizontal y las charlas están en una columna.',
         'El botón cambia de color con una transición al pasar el cursor.',
         'Los tres campos tienen `label` y `required`.'])

d.guardar(os.path.join(AQUI, '..', 'guias', 'out', 'EF_Parte_B_Ficha_Tecnica.html'))
print('ok')
