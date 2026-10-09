# -*- coding: utf-8 -*-
"""Guía de código · Sesión 15: proyecto integrador, pruebas y despliegue."""
import os
import sys
from guia import Doc, css_bloques, html_entre

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
P = os.path.join(REPO, 'SESION 15', 'mi-portafolio-dagner')
CSS = os.path.join(P, 'assets', 'css')
IX = os.path.join(P, 'index.html')
NF = os.path.join(P, '404.html')
CO = os.path.join(P, 'contactame.html')
CU = os.path.join(P, 'cursos.html')
HD = os.path.join(CSS, 'header.css')
CT = os.path.join(CSS, 'contenido.css')
G = css_bloques(os.path.join(CSS, 'global.css'))
C = css_bloques(CT)

d = Doc('Guía paso a paso: pruebas y despliegue del sitio completo',
        'Guía paso a paso · Sesión 15: pruebas y despliegue',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 15 · Proyecto integrador',
        'Revisas el portafolio completo como lo haría un cliente: validas, pruebas con el teclado, completas lo que '
        'falta para publicarlo bien y lo despliegas en Netlify con su formulario funcionando.')

d.callout('Vienes de la sesión 14:', 'necesitas las cinco páginas del portafolio (Inicio, Sobre mí, Proyectos, Cursos y '
          'Contacto) con su CSS. Hoy no aparece ninguna propiedad nueva de CSS: se trata de revisar, corregir y publicar.')

d.h3('Qué vas a hacer')
d.tabla(['Archivo', 'Qué cambia hoy', 'En Figma'], [
    ['Las cinco páginas', 'Un título distinto en cada una, el icono, la vista previa para compartir, el enlace «Saltar al contenido» y `aria-current`', '—'],
    ['404.html (nuevo)', 'La página que muestra Netlify cuando una dirección no existe', '—'],
    ['gracias.html (nuevo)', 'La página que aparece después de enviar un formulario', '—'],
    ['contactame.html · cursos.html', 'Los dos formularios guardan sus mensajes en Netlify', '—'],
    ['assets/img (3 imágenes nuevas)', '`favicon-32.png`, `apple-touch-icon.png` y `og-portafolio.png`', 'Los marcos `favicon` y `og-portafolio`'],
    ['global.css · header.css · contenido.css', 'El enlace para saltar, la página actual del menú y las páginas de aviso', '—'],
], anchos=['30%', '46%', '24%'])

d.h3('Cómo se reparte')
d.tabla(['Momento', 'Pasos', 'Qué practicas'], [
    ['En clase, juntos', '0 al 3', 'La lista de pruebas, los validadores, los enlaces y el `<head>` completo'],
    ['En clase, tú', '4 y 5', 'El teclado y las páginas 404 y de gracias'],
    ['Tarea', '6 al 8', 'Los formularios en Netlify, la publicación y Lighthouse'],
    ['Proyecto integrador', 'Última sección', 'Lo que entregas y cómo se califica'],
], anchos=['20%', '16%', '64%'])

d.h2('Paso 0 · La lista de pruebas')
d.p('Antes de publicar, recorre el sitio con esta lista. Cada fila es una prueba que puedes hacer en minutos:')
d.tabla(['Prueba', 'Con qué', 'Pasa si…'], [
    ['HTML válido', '**validator.w3.org**', 'Las siete páginas dicen «No errors or warnings to show»'],
    ['CSS válido', '**jigsaw.w3.org/css-validator**', 'Las seis hojas dicen «¡Enhorabuena! No error encontrado»'],
    ['Enlaces', 'Clic en cada enlace del menú, del pie y de los botones', 'Ninguno lleva a una página en blanco ni a un 404'],
    ['Imágenes', 'Revisa cada `<img>`', 'Todas tienen `alt`, `width` y `height`, y ninguna pesa más de 300 KB'],
    ['Teclado', 'Solo `Tab`, `Shift + Tab`, `Enter` y `Esc`', 'Llegas a todo, siempre ves dónde está el foco y nada queda atrapado'],
    ['Pantallas', 'Las herramientas del navegador (`F12`, icono del celular)', 'A 390, 820 y 1440 px no hay barra horizontal'],
    ['Metadatos', 'El código del `<head>`', 'Cada página tiene su título y su descripción'],
    ['Rendimiento y accesibilidad', '**Lighthouse** (Paso 8)', 'Accesibilidad y SEO de 90 o más'],
], anchos=['20%', '36%', '44%'])

d.h2('Paso 1 · Valida las siete páginas y las seis hojas')
d.pasos(['Abre **validator.w3.org**, elige la pestaña **Validate by File Upload** y sube `index.html`. Repite con cada página.',
         'Abre **jigsaw.w3.org/css-validator**, pestaña **Por carga de archivo**, y sube cada hoja de `assets/css/`.',
         'Corrige cada error en el orden en que aparece: muchas veces, arreglar el primero hace desaparecer los siguientes.'])
d.tabla(['Mensaje del validador', 'Qué significa'], [
    ['`End tag for X seen, but there were open elements`', 'Falta cerrar una etiqueta antes de esa línea'],
    ['`Duplicate ID`', 'Dos elementos tienen el mismo `id`. Cada `id` es único en la página'],
    ['`An img element must have an alt attribute`', 'A una imagen le falta `alt`'],
    ['`The for attribute of the label element must refer to…`', 'El `for` de una etiqueta no coincide con el `id` de su campo'],
    ['`Parse Error` (CSS)', 'Falta una llave, un punto y coma o los dos puntos de una propiedad'],
], anchos=['52%', '48%'])
d.callout('Bootstrap no se valida:', 'en `cursos.html` el validador revisa tu HTML, no el CSS de Bootstrap. Valida solo '
          'tus hojas; `tema-bootstrap.css` también es tuya.')

d.h2('Paso 2 · Los enlaces y los nombres de archivo')
d.p('Netlify guarda tu sitio en un servidor que distingue mayúsculas de minúsculas. En tu computadora, `Foto.JPG` y '
    '`foto.jpg` pueden ser el mismo archivo; en Netlify, no. Lo mismo pasa con los espacios y las tildes.')
d.tabla(['En tu carpeta', 'En el HTML', 'En Netlify'], [
    ['`foto-carnet.jpg`', '`src="assets/img/foto-carnet.jpg"`', 'Se ve'],
    ['`Foto-Carnet.jpg`', '`src="assets/img/foto-carnet.jpg"`', 'Imagen rota: la mayúscula no coincide'],
    ['`mis proyectos.html`', '`href="mis proyectos.html"`', 'Funciona a veces: el espacio se convierte en `%20`'],
    ['`diseño.png`', '`src="diseño.png"`', 'Puede fallar: evita la ñ y las tildes en los nombres'],
], negrita_primera=False, anchos=['28%', '40%', '32%'])
d.p('La regla del curso, desde la sesión 01: nombres en minúsculas, con guiones y sin espacios ni tildes. Revisa '
    'también que cada `href="#…"` tenga su `id` en la página.')
d.comprueba('haz clic en todos los enlaces de las cinco páginas. Ninguno abre una página en blanco.')

d.h2('Paso 3 · El <head> completo', salto=True)
d.p('El `<head>` no se ve en la página, pero decide cómo aparece tu sitio en la pestaña, en Google y cuando alguien '
    'comparte el enlace. Así queda el de `index.html`:')
d.code(html_entre(IX, '<title>', '<meta property="og:locale" content="es_PE" />'), corto=False)
d.h3('3.1 · Un título distinto en cada página')
d.p('Hasta la sesión 14, cuatro páginas se llamaban igual: «Portafolio - Dagner Chuman». Con varias pestañas abiertas '
    'no se distinguen, y Google muestra ese título como enlace. Primero lo propio de la página y después el nombre:')
d.tabla(['Página', '<title>'], [
    ['index.html', '`Dagner Chuman · Docente e Ingeniero Web`'],
    ['sobre-mi.html', '`Sobre mí · Dagner Chuman`'],
    ['mis-proyectos.html', '`Proyectos · Dagner Chuman`'],
    ['cursos.html', '`Cursos · Dagner Chuman`'],
    ['contactame.html', '`Contacto · Dagner Chuman`'],
], anchos=['30%', '70%'])
d.p('La `description` también cambia en cada página: una o dos frases, unos 150 caracteres, que digan qué hay en ella.')
d.h3('3.2 · El icono de la pestaña')
d.tabla(['Etiqueta', 'Archivo', 'Dónde aparece'], [
    ['`<link rel="icon">`', '`favicon-32.png` · 32 × 32', 'La pestaña del navegador y los marcadores'],
    ['`<link rel="apple-touch-icon">`', '`apple-touch-icon.png` · 180 × 180', 'El acceso directo en la pantalla del celular'],
], anchos=['34%', '34%', '32%'])
d.p('Los dos salen del marco `favicon` de tu Figma (ver la guía de Figma). Sin icono, el navegador lo pide igual a '
    '`/favicon.ico` y, como no existe, aparece un error 404 en la consola.')
d.h3('3.3 · La vista previa al compartir: Open Graph')
d.p('Cuando pegas un enlace en WhatsApp, LinkedIn o Facebook, la aplicación lee las etiquetas `og:` y arma una tarjeta '
    'con imagen, título y descripción. Sin ellas, solo se ve la dirección.')
d.tabla(['Etiqueta', 'Qué pone'], [
    ['`og:title` · `og:description`', 'El título y el texto de la tarjeta. Repiten el `<title>` y la `description`'],
    ['`og:image`', 'La imagen de 1200 × 630, con la **dirección completa**: `https://…/assets/img/og-portafolio.png`'],
    ['`og:url`', 'La dirección completa de esa página'],
    ['`og:type` · `og:site_name` · `og:locale`', '`website`, tu nombre y el idioma: `es_PE`, español de Perú'],
], anchos=['36%', '64%'])
d.callout('og:image necesita la dirección completa:', 'la aplicación que arma la tarjeta no está en tu sitio, así que '
          'una ruta como `assets/img/…` no le sirve. Si tu sitio se llama distinto en Netlify, cambia '
          '`mi-portafolio-dagner` por tu nombre en `og:image` y `og:url`.')
d.comprueba('las cinco pestañas muestran el icono «DC» y un título distinto.')

d.h2('Paso 4 · El teclado: saltar al contenido y la página actual')
d.h3('4.1 · El enlace «Saltar al contenido»')
d.p('Quien navega con el teclado recorre el menú completo en cada página antes de llegar al contenido. Un enlace al '
    'inicio de `<body>` lo evita: está escondido y aparece con el primer `Tab`.')
d.code(html_entre(IX, '<!-- Sesión 15 · Con Tab', 'Saltar al contenido</a>'))
d.p('Para que funcione, `<main>` lleva el `id` al que apunta: `<main id="contenido">`. El estilo va en el bloque 11 de '
    '`global.css`:')
d.code(G['11'])
d.h3('4.2 · La página actual en el menú')
d.p('El atributo `aria-current="page"` marca el enlace de la página en la que estás. El lector de pantalla lo anuncia '
    '(«Sobre mí, página actual») y el CSS lo puede mostrar. Va en el menú de la cabecera y en el del pie:')
d.code('''<!-- en sobre-mi.html -->
<li><a href="sobre-mi.html" aria-current="page">Sobre mí</a></li>''')
d.p('En `header.css`, el enlace actual usa el mismo subrayado que el hover de la sesión 09:')
d.code(html_entre(HD, '/* Sesión 15: aria-current', '}\n'))
d.code(html_entre(HD, '/* Sesión 15: la página actual', '}\n'))
d.comprueba('abre `sobre-mi.html` y pulsa `Tab` una vez: aparece «Saltar al contenido». Pulsa `Enter` y el siguiente '
            '`Tab` ya está dentro del contenido. En el menú, «Sobre mí» se ve subrayado.')

d.h2('Paso 5 · Las páginas de aviso: 404 y gracias', salto=True)
d.h3('5.1 · 404.html')
d.p('Si alguien escribe mal una dirección, Netlify muestra el archivo `404.html` de la raíz del sitio, si existe. Copia '
    '`sobre-mi.html`, cámbiale el nombre a `404.html` y cambia su `<main>`:')
d.code(html_entre(NF, '<main id="contenido">', '</main>'), corto=False)
d.p('Dos cambios más en la copia:')
d.lista(['**Las rutas empiezan con `/`:** `/assets/css/global.css`, `/index.html`. La 404 puede aparecer en cualquier '
         'carpeta, como `/proyectos/viejo.html`; desde ahí, `assets/…` no existe. La `/` inicial empieza desde la raíz del sitio.',
         '**`<meta name="robots" content="noindex" />`** en el `<head>`: le pide a Google que no la muestre en sus resultados.',
         'Ningún enlace del menú lleva `aria-current`: la 404 no es ninguna de las cinco páginas.'])
d.callout('Si la abres con doble clic, se ve sin estilos:', 'en tu computadora, `/` es la raíz del disco, no la de tu '
          'sitio. Pruébala con Live Server o ya publicada en Netlify, escribiendo una dirección que no exista.')
d.h3('5.2 · gracias.html')
d.p('Es otra copia, con rutas normales (`assets/…`), `noindex` y un mensaje: «¡Gracias por escribirme!». Aparece '
    'después de enviar un formulario (Paso 6).')
d.h3('5.3 · El estilo de las dos páginas')
d.p('Las dos usan las clases `aviso`, `aviso-codigo` y `aviso-acciones`, y su `<body>` lleva `class="pagina-aviso"`. '
    'Como la página es corta, el `body` pasa a Flujo vertical y el `main` crece hasta llenar el alto: el pie queda abajo.')
d.code(C['14'], corto=False)
d.p('El botón «Contacto» de la cabecera se buscaba con `a[href="contactame.html"]`. En la 404 su enlace es '
    '`/contactame.html` y el botón perdía su estilo. El selector `$=` significa «termina en» y encuentra los dos:')
d.code('header > a[href$="contactame.html"] { … }')
d.comprueba('en la 404, el número es gris claro, el pie queda al fondo de la pantalla y el botón «Contacto» tiene su borde.')

d.h2('Paso 6 · Los formularios con Netlify Forms')
d.p('Hasta hoy, el formulario de contacto no enviaba nada. Netlify puede guardar los mensajes sin que escribas un '
    'servidor: basta con tres atributos en `<form>` y un `name` en cada campo.')
d.code(html_entre(CO, '<!-- Rejilla de dos columnas', '<form class="form-grid"') .rsplit('\n', 1)[0] + '\n' +
       html_entre(CO, '<form class="form-grid"', 'data-netlify="true">'))
d.tabla(['Atributo', 'Qué hace'], [
    ['`name="contacto"`', 'El nombre del formulario en el panel de Netlify. El de `cursos.html` se llama `inscripcion`'],
    ['`data-netlify="true"`', 'Netlify encuentra el formulario al publicar y prepara dónde guardar sus mensajes'],
    ['`method="post"`', 'Envía los datos ocultos, no en la dirección'],
    ['`action="/gracias.html"`', 'La página que aparece después de enviar. Netlify pide que empiece con `/`'],
    ['`name` en cada campo', 'Solo se guardan los campos que tienen `name`: `nombre`, `correo`, `mensaje`…'],
], anchos=['32%', '68%'])
d.pasos(['Publica el sitio (Paso 7).',
         'En el panel de Netlify, abre tu sitio y entra a **Forms**. Si ves el botón **Enable form detection**, púlsalo.',
         'Vuelve a publicar: Netlify solo busca formularios cuando publicas.',
         'Envía un mensaje de prueba desde tu sitio publicado. Debe aparecer `gracias.html`.',
         'En **Forms** aparece `contacto` con tu mensaje. Ahí también puedes pedir que te avise por correo.'])
d.callout('En tu computadora no funciona:', 'al enviar desde Live Server verás un error: el formulario solo guarda '
          'mensajes en el sitio publicado.')

d.h2('Paso 7 · Publica en Netlify', salto=True)
d.h3('Opción A · Arrastrar la carpeta')
d.pasos(['Entra a **app.netlify.com** con tu cuenta y abre el sitio que publicaste antes.',
         'Ve a la pestaña **Deploys**. Abajo está el recuadro para arrastrar una carpeta.',
         'Arrastra la carpeta `mi-portafolio-dagner`: la que tiene `index.html` directamente dentro, no una carpeta que la contenga.',
         'Espera a que diga **Published** y abre la dirección.'])
d.h3('Opción B · Desde GitHub')
d.pasos(['Sube la carpeta a un repositorio de GitHub (sesión de Git del curso).',
         'En Netlify: **Add new project** (o **Add new site**) › **Import an existing project** › **GitHub** y elige el repositorio.',
         'En **Publish directory** escribe la carpeta donde está `index.html`; si está en la raíz del repositorio, déjalo vacío.',
         'Pulsa **Deploy**. Desde ahora, cada `git push` publica el sitio solo.'])
d.h3('El nombre del sitio')
d.p('Netlify inventa un nombre como `funny-panda-12ab34.netlify.app`. Cámbialo en la configuración del sitio, con la '
    'opción **Change site name** (en el panel nuevo, **Change project name**). Usa el mismo nombre en `og:image` y `og:url`.')
d.comprueba('abre tu dirección en el celular, escribe una página que no existe (`/hola`) y aparece tu 404 con estilos.')

d.h2('Paso 8 · Lighthouse: mide el sitio publicado')
d.pasos(['Abre tu sitio publicado en una **ventana de incógnito**: así las extensiones del navegador no cambian el resultado.',
         'Pulsa `F12` y elige la pestaña **Lighthouse** (puede estar dentro de `»`).',
         'Modo **Navigation**, dispositivo **Mobile** y las cuatro categorías. Pulsa **Analyze page load**.',
         'Lee las cuatro notas y, debajo de cada una, la lista de lo que falla.'])
d.tabla(['Categoría', 'Qué mide', 'index.html, sesión 14 → 15'], [
    ['Performance (rendimiento)', 'Cuánto tarda en verse y en responder', '98 → 98'],
    ['Accessibility (accesibilidad)', 'Contraste, `alt`, etiquetas, orden de los títulos', '94 → 94: falta el contraste del botón cian'],
    ['Best Practices (buenas prácticas)', 'HTTPS, errores en la consola, imágenes con su proporción', 'Desaparece el error 404 de `/favicon.ico`'],
    ['SEO (buscadores)', '`<title>`, `description`, `lang`, enlaces con texto', '100 → 100'],
], anchos=['30%', '40%', '30%'])
d.p('Las notas cambian unos puntos entre una medición y otra, y entre una computadora y otra. Mira sobre todo la lista '
    'de fallas.')
d.h3('8.1 · El contraste: una decisión de diseño')
d.p('Lighthouse marca el texto blanco sobre el cian `06B6C4`: su contraste es **2.47 a 1**. La norma WCAG pide 4.5 a 1 '
    'para el texto normal y 3 a 1 para el texto grande (desde 24px, o 18.66px en negrita). El gris del menú en reposo, '
    '`9CA3AF` sobre blanco, tiene 2.54 a 1.')
d.p('En el portafolio del curso, los colores los fija el manual de Figma, así que se quedan. En un proyecto tuyo, '
    'cualquiera de estas opciones pasa la prueba:')
d.tabla(['Opción', 'Contraste'], [
    ['Texto `0B0F19` sobre el cian `06B6C4`', '7.75 a 1'],
    ['Texto blanco sobre un cian más oscuro, `0E7490`', '5.36 a 1'],
    ['Menú en reposo `6B7280` en lugar de `9CA3AF`', '4.83 a 1'],
], negrita_primera=False, anchos=['64%', '36%'])
d.callout('Si cambias un color, cámbialo en los dos lados:', 'en la variable de `global.css` (y en `tema-bootstrap.css`) '
          'y en la variable de Figma. Así el diseño y el código siguen hablando igual.')

d.h2('El proyecto integrador', salto=True)
d.p('Tu portafolio es el proyecto integrador del curso: reúne todo lo que hiciste desde la sesión 01. Lo entregas '
    'publicado, con su diseño en Figma y tu bitácora de prompts, y lo presentas en la sesión 16: es la Parte B del '
    'examen final.')
d.h3('Qué entregas')
d.tabla(['Entregable', 'Cómo'], [
    ['La dirección del sitio publicado', '`https://tu-nombre.netlify.app`, con las cinco páginas, la 404 y la página de gracias'],
    ['El enlace de tu Figma', 'Con permiso **puede ver** (ver la guía de Figma)'],
    ['La carpeta del sitio', 'Comprimida en `.zip`, con el nombre `apellido-nombre-portafolio.zip`'],
    ['Una captura de Lighthouse', 'De `index.html` publicado, en modo Mobile, con las cuatro notas a la vista'],
    ['Tu bitácora de prompts', 'Al menos tres prompts, con lo que te dio la IA, lo que corregiste y cómo lo comprobaste (guías Extra de IA)'],
], anchos=['32%', '68%'])
d.p('Súbelo a la tarea **Proyecto integrador** del Aula Virtual antes de la sesión 16, en la fecha que indica tu docente.')
d.h3('Lo que se revisa')
d.p('Se califica al presentarlo en la sesión 16, con la pauta de presentación (Parte B del examen final, 10 puntos). '
    'Esto es lo que se revisa:')
d.tabla(['Criterio', 'Logrado', 'Sesiones'], [
    ['Estructura', 'HTML semántico (`header`, `nav`, `main`, `section`, `footer`), un solo `h1`, títulos en orden y las siete páginas sin errores en el validador', '02 a 07'],
    ['Fidelidad al diseño', 'Colores, letra, medidas y espacios iguales a los de Figma; nombres de clase que siguen los de las capas', '09 y 10'],
    ['Diseño adaptable', 'Se ve bien a 390, 820 y 1440 px, sin barra horizontal; las imágenes no se deforman', '12'],
    ['Interacción', 'Hover y transiciones, el menú, el acordeón y la ventana de inscripción funcionan con mouse y con teclado', '11 y 14'],
    ['Accesibilidad y pruebas', '`alt` en las imágenes, foco visible, «Saltar al contenido», `aria-current`; Lighthouse de 90 o más en Accesibilidad y SEO', '15'],
    ['Publicación', 'Sitio en Netlify, todos los enlaces funcionan, 404 propia, formulario que guarda mensajes, icono y vista previa al compartir', '15'],
    ['Uso de la IA', 'Bitácora con al menos tres prompts: qué pediste, qué corregiste y cómo lo comprobaste; sabes explicar todo tu código', 'Extra de IA'],
], anchos=['22%', '62%', '16%'])

d.h2('Lista de comprobación')
d.check(['Las siete páginas y las seis hojas pasan los validadores del W3C sin errores.',
         'Todos los archivos tienen nombres en minúsculas, sin espacios ni tildes, y los enlaces los escriben igual.',
         'Cada página tiene su propio `<title>` y su `description`.',
         'Las cinco páginas enlazan `favicon-32.png` y `apple-touch-icon.png`, y tienen las etiquetas `og:` con la dirección completa.',
         'El primer `Tab` muestra «Saltar al contenido» y `<main>` tiene `id="contenido"`.',
         'El enlace de la página actual lleva `aria-current="page"` en la cabecera y en el pie.',
         '`404.html` usa rutas que empiezan con `/` y lleva `noindex`.',
         'Los dos formularios tienen `name`, `method="post"`, `action="/gracias.html"` y `data-netlify="true"`.',
         'El sitio está publicado y un mensaje de prueba aparece en **Forms**.',
         'Lighthouse da 90 o más en Accesibilidad y SEO.'])

d.h2('Errores frecuentes en esta sesión')
d.tabla(['Síntoma', 'Causa y solución'], [
    ['En Netlify, «Page not found» en la página de inicio', 'Arrastraste una carpeta que contiene a `mi-portafolio-dagner`. `index.html` debe estar en la raíz de lo que arrastras'],
    ['Una imagen se ve en tu computadora y no en Netlify', 'Una mayúscula o una tilde no coincide entre el nombre del archivo y el HTML'],
    ['La 404 se ve sin estilos', 'Sus rutas no empiezan con `/`; o la abriste con doble clic: pruébala publicada'],
    ['Envío el formulario y no aparece en Forms', 'La detección de formularios está apagada, falta `data-netlify="true"` o publicaste antes de añadirlo. Actívala y publica otra vez'],
    ['El mensaje llega sin algunos datos', 'A esos campos les falta el atributo `name`'],
    ['El icono no cambia en la pestaña', 'El navegador lo guardó en caché. Recarga con `Ctrl + F5` o abre una ventana de incógnito'],
    ['WhatsApp no muestra la vista previa', '`og:image` no tiene la dirección completa con `https://`, o la imagen pesa más de 600 KB. WhatsApp guarda la vista previa un tiempo: prueba con `?v=2` al final del enlace'],
    ['«Saltar al contenido» se ve siempre', 'Falta `position: absolute` o el `top` negativo en `.saltar`'],
], anchos=['36%', '64%'])

d.guardar(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'Guia_Sesion15_Pruebas_y_Despliegue_del_Sitio.html'))
print('ok')
