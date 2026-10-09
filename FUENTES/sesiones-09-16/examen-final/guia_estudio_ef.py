# -*- coding: utf-8 -*-
"""Guía de estudio del examen final: lo esencial de las sesiones 01 a 15 y cómo es el examen.
uso: python3 guia_estudio_ef.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'guias'))
from guia import Doc  # noqa: E402

d = Doc('Guía de estudio del examen final',
        'Guía de estudio · Examen final',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 16 · Jueves 05/11/2026 · Aula Virtual USS',
        'Lo esencial del curso en pocas páginas, ordenado como el examen: HTML5, CSS3 y diseño responsivo, Bootstrap y '
        'publicación. Repásala junto con el simulacro de la sesión 16.')

d.h3('Cómo es el examen')
d.tabla(['Parte', 'Qué', 'Tiempo', 'Puntos'], [
    ['A · Cuestionario', '20 preguntas de opción múltiple de las sesiones 1 a 16, en el Aula Virtual. Un solo intento', '40 minutos', '10'],
    ['B · Caso práctico', 'La página «Semana de la Informática 2026» según su ficha técnica. Se entrega en `.zip`', '80 minutos', '10'],
], anchos=['20%', '56%', '12%', '12%'])
d.tabla(['Tu promedio final', 'Peso'], [
    ['Participación en aula [PA]', '40 %'],
    ['Taller online 1 [TA1] · sesión 6', '15 %'],
    ['Taller online 2 [TA2] · sesión 12', '15 %'],
    ['**Examen final [EF] · sesión 16**', '**30 %**'],
], anchos=['70%', '30%'])
d.callout('Para aprobar:', 'promedio final de 11 o más y una asistencia mínima del 80 %.')
d.h3('Cómo estudiar')
d.pasos(['Resuelve el **simulacro** (`cuestionario-sesion16.html`): parte 1, HTML5; parte 2, CSS3 y Bootstrap. Lee la explicación de cada respuesta.',
         'Repasa las tres tablas de esta guía. Si un concepto no te suena, abre la guía de esa sesión.',
         'Practica la Parte B: con la ficha técnica, construye la página en 80 minutos, sin mirar tu portafolio.',
         'Antes de entrar, revisa la lista de comprobación de la última página.'])

# ---------------- Bloque 1
d.h2('Bloque 1 · HTML5 y Figma (sesiones 01 a 07)', salto=True)
d.tabla(['Tema', 'Lo que tienes que recordar', 'Ses.'], [
    ['Los tres lenguajes', 'HTML: estructura y contenido. CSS: presentación. JavaScript: comportamiento', '01'],
    ['Validar', '**validator.w3.org** para el HTML y **jigsaw.w3.org/css-validator** para el CSS', '01'],
    ['El documento', '`<!doctype html>`, `<html lang="es">`, `<meta charset="UTF-8">`, `<meta name="viewport" …>` y `<title>`', '02'],
    ['Títulos', 'Un solo `h1` por página; después `h2`, `h3`… en orden, sin saltar niveles', '02'],
    ['Listas', '`ul`: con viñetas. `ol`: numerada. Cada elemento, `li`', '02'],
    ['Semántica', '`header`, `nav`, `main` (uno por página), `section` (con su título), `article`, `aside`, `footer`. `div` no tiene significado', '03'],
    ['Enlaces', 'Ruta relativa: `assets/img/foto.jpg`. Externo: `target="_blank" rel="noopener"`. `mailto:` y `tel:`', '04'],
    ['Imágenes', '`alt` describe la imagen (`alt=""` si es decorativa). `width` y `height` reservan su espacio', '04'],
    ['Tablas', '`caption` (título), `thead`, `tbody`, `th scope="col"`. `colspan` une columnas; `rowspan`, filas', '05'],
    ['Formularios', '`label for` = `id` del campo. `name` para enviar el dato. `required`, `type="email"`. `fieldset` y `legend` agrupan; `select` y `option`', '06'],
    ['Video y audio', '`controls`, `poster`, `muted` (necesario para `autoplay`), varios `source` y `track` para los subtítulos `.vtt`', '07'],
    ['Figma', '`Shift + A`: Disposición automática. Espacio es la separación entre hijos; Espaciado, el relleno interno', '07'],
], anchos=['18%', '74%', '8%'])
d.code('''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Inicio · Mi sitio</title>
    <link rel="stylesheet" href="assets/css/estilos.css" />
  </head>
  <body>
    <header> … <nav aria-label="Navegación principal"> … </nav></header>
    <main>
      <section aria-labelledby="titulo"> <h1 id="titulo">…</h1> </section>
    </main>
    <footer> … </footer>
  </body>
</html>''')

# ---------------- Bloque 2
d.h2('Bloque 2 · CSS3 y diseño responsivo (sesiones 08 a 12)', salto=True)
d.tabla(['Tema', 'Lo que tienes que recordar', 'Ses.'], [
    ['Selectores', '`p` (etiqueta), `.clase`, `#id`, `.tarjeta p` (descendiente), `a:hover` (estado), `a[href$=".pdf"]` (atributo)', '08–09'],
    ['Especificidad', 'id > clase > etiqueta. Si empatan, gana la regla escrita después', '09'],
    ['Variables', 'Se definen en `:root` (`--color-primary: #06B6C4;`) y se usan con `var(--color-primary)`', '09'],
    ['Unidades', '`px` fijo; `rem` relativo al `html` (16px); `%` relativo al padre; `vw` al ancho de la ventana', '09'],
    ['Fuentes', 'El `@import` de Google Fonts va en la primera línea de la hoja', '09'],
    ['Modelo de caja', 'contenido + `padding` + `border` + `margin`. `box-sizing: border-box` mete el relleno y el borde en el `width`', '10'],
    ['Flexbox', '`display: flex`; `flex-direction: column` es el Flujo vertical; `justify-content` en el eje principal; `align-items` en el cruzado; `gap` es el Espacio', '10'],
    ['Grid', '`display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;`', '10'],
    ['Transiciones', '`transition: propiedad duración curva`. Necesita un cambio de estado, como `:hover`', '11'],
    ['Transformaciones', '`translateY(-4px)`, `scale(1.05)`, `rotate(5deg)`: mueven sin empujar a los vecinos', '11'],
    ['Animaciones', '`@keyframes nombre { from {…} to {…} }` y `animation: nombre 1s ease infinite`', '11'],
    ['Movimiento reducido', '`@media (prefers-reduced-motion: reduce)` quita las animaciones a quien lo pidió', '11'],
    ['Responsive', '`viewport` obligatorio. `max-width`: hasta ese ancho; `min-width`: desde ese ancho. Las media queries van al final', '12'],
    ['Medidas fluidas', '`clamp(mín, ideal, máx)`, `repeat(auto-fit, minmax(300px, 1fr))`, `aspect-ratio: 16 / 9`, `img { max-width: 100%; height: auto; }`', '12'],
], anchos=['18%', '74%', '8%'])
d.tabla(['En Figma', 'En CSS'], [
    ['Flujo horizontal · vertical', '`display: flex` · `flex-direction: column`'],
    ['Espacio `24` · Espacio Auto', '`gap: 24px` · `justify-content: space-between`'],
    ['Espaciado `80` y `100`', '`padding: 100px 80px` (arriba y abajo primero)'],
    ['Llenar el contenedor · Ajustar al contenido', '`flex: 1` o `width: 100%` · ancho automático'],
    ['Radio de esquina `12` · Trazo `E5E7EB`', '`border-radius: 12px` · `border: 1px solid #E5E7EB`'],
], negrita_primera=False, anchos=['44%', '56%'])

# ---------------- Bloque 3
d.h2('Bloque 3 · Bootstrap y publicación (sesiones 13 a 15)')
d.tabla(['Tema', 'Lo que tienes que recordar', 'Ses.'], [
    ['Instalar', 'El CSS de Bootstrap en el `<head>`, **antes** de tus hojas; `bootstrap.bundle.min.js` al **final** del `<body>`', '13'],
    ['La grilla', '`.container` › `.row` › `col-*`. 12 columnas. `col-12 col-md-6 col-lg-4`: 1, 2 y 3 por fila. `g-4`: medianil de 24px', '13'],
    ['Puntos de quiebre', '`sm` 576 · `md` 768 · `lg` 992 · `xl` 1200 · `xxl` 1400. Valen desde ese ancho hacia arriba', '13'],
    ['Utilidades', '`m-*` y `p-*` de 0 a 5 (`3` = 16px, `4` = 24px), `d-flex`, `text-center`, `visually-hidden`. Usan `!important`', '14'],
    ['Componentes', '`card`, `badge`, `alert`, `btn btn-primary`, `accordion` (`collapse show`), `modal`, `navbar navbar-expand-lg`', '14'],
    ['data-bs-*', '`data-bs-toggle="modal"` y `data-bs-target="#id"` abren; `data-bs-dismiss` cierra; `data-bs-parent` deja una respuesta abierta', '14'],
    ['El tema', 'Cambia `--bs-primary` y `--bs-primary-rgb` en `tema-bootstrap.css`, justo después de Bootstrap', '14'],
    ['El `<head>` completo', 'Un `<title>` y una `description` por página, `rel="icon"`, `rel="apple-touch-icon"` y las etiquetas `og:` con la dirección completa', '15'],
    ['Teclado', 'Enlace «Saltar al contenido» y `aria-current="page"` en el menú', '15'],
    ['Netlify', 'Distingue mayúsculas. `index.html` en la raíz. `404.html` con rutas que empiezan con `/`. Formularios con `data-netlify="true"`', '15'],
    ['Lighthouse', 'Rendimiento, Accesibilidad, Buenas prácticas y SEO. El contraste del texto: 4.5 a 1', '15'],
], anchos=['18%', '74%', '8%'])

d.h2('Errores que cuestan puntos')
d.tabla(['Error', 'Cómo evitarlo'], [
    ['Confundir Espacio con Espaciado', 'Espacio = `gap` (entre hijos). Espaciado = `padding` (dentro del borde)'],
    ['Confundir `max-width` con `min-width`', '`max-width: 600px` es «hasta 600»: el celular. `min-width: 768px` es «desde 768»'],
    ['Olvidar el `#` en `data-bs-target`', 'Apunta a un `id`, como un selector: `#inscripcion`'],
    ['`label` sin `for`', 'El `for` es igual al `id` del campo, no a su `name`'],
    ['Entregar el `.zip` sin `index.html` en la raíz', 'Comprime la carpeta que tiene `index.html` directamente dentro'],
], anchos=['40%', '60%'])

d.h2('Antes del examen')
d.check(['Resolví las dos partes del simulacro y leí las explicaciones.',
         'Sé usar `F12` para probar a 390px y para abrir Lighthouse.',
         'Sé crear una carpeta con `index.html` y `assets/css/`, y comprimirla en `.zip`.',
         'Entré al Aula Virtual con mi usuario antes del día del examen.'])

d.guardar(os.path.join(AQUI, '..', 'guias', 'out', 'Guia_de_Estudio_Examen_Final.html'))
print('ok')
