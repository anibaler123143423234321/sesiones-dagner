# -*- coding: utf-8 -*-
"""Examen final · Parte B: la pauta para presentar el proyecto integrador (sesión 16).
uso: python3 pauta_parte_b.py   → guias/out/EF_Parte_B_Pauta_de_Presentacion.html (después, pdf.js)
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'guias'))
from guia import Doc  # noqa: E402

d = Doc('Examen final · Parte B: presenta tu proyecto integrador',
        'Examen final · Parte B · Pauta de presentación',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 16 · Jueves 05/11/2026',
        'Presentas tu portafolio publicado, su diseño en Figma y cómo usaste la IA para construirlo. Tienes 5 minutos '
        'para exponer y 2 para responder preguntas. Vale 10 de los 20 puntos del examen final.')

d.h3('Antes de la sesión 16')
d.tabla(['Qué', 'Cómo'], [
    ['La dirección de tu sitio', '`https://tu-nombre.netlify.app`, con las cinco páginas, la 404 y la página de gracias'],
    ['El enlace de tu Figma', 'Con permiso **puede ver**, con los marcos de escritorio y celular y tus componentes'],
    ['La carpeta del sitio', 'En `.zip`, con el nombre `apellido-nombre-portafolio.zip`'],
    ['Una captura de Lighthouse', 'De `index.html` publicado, en modo Mobile, con las cuatro notas'],
    ['Tu bitácora de prompts', 'Al menos tres prompts, con lo que te dio la IA, lo que corregiste y cómo lo comprobaste (guías Extra de IA)'],
], anchos=['28%', '72%'])
d.p('Súbelo todo a la tarea **Proyecto integrador** del Aula Virtual antes de la sesión, en la fecha que indica tu docente.')
d.callout('El día de la presentación:', 'ten abiertas en pestañas tu sitio publicado, tu Figma, tu bitácora y tu captura de '
          'Lighthouse. Si se cae internet, presentas desde la carpeta `.zip` en tu computadora.')

d.h2('Tu guion: cinco minutos')
d.tabla(['Tiempo', 'Qué muestras', 'Qué dices'], [
    ['30 s', 'La página de inicio publicada', 'Quién eres y para qué sirve tu sitio'],
    ['1 min', 'Tu Figma: escritorio, celular y un componente', 'Cómo organizaste el diseño y qué valores pasaste al código'],
    ['2 min', 'El sitio: las páginas, un hover, el celular con `F12` a 390 y el formulario', 'Qué técnica usaste en cada parte: Flexbox, Grid, media queries, Bootstrap'],
    ['1 min', 'Tu bitácora: tu mejor prompt', 'Qué le pediste a la IA, qué te dio, qué corregiste y cómo lo comprobaste'],
    ['30 s', 'Tu captura de Lighthouse', 'Qué mediste y qué mejorarías si tuvieras una semana más'],
], anchos=['12%', '44%', '44%'])
d.p('Después vienen **2 minutos de preguntas**. El docente puede pedirte que abras un archivo y expliques una regla de tu '
    'CSS o una parte de tu HTML: es la forma de comprobar que entiendes lo que entregaste.')

d.h3('Preguntas que te pueden hacer')
d.lista(['¿Por qué esta sección usa Flexbox y esta otra Grid?',
         '¿Qué hace esta media query y a qué ancho se activa?',
         '¿Qué te propuso la IA en este prompt y qué cambiaste?',
         '¿Cómo pasaste este valor de Figma a tu CSS?',
         '¿Qué hace `aria-current` en tu menú? ¿Y el enlace «Saltar al contenido»?',
         '¿Qué te marcó Lighthouse y cómo lo corregiste?'])

d.h2('Cómo se califica la Parte B')
d.tabla(['Criterio', 'Logrado (2)', 'En proceso (1)', 'No logrado (0)'], [
    ['Sitio publicado y funcional', 'En Netlify; los enlaces funcionan; se adapta a 390 px; el formulario guarda mensajes; tiene su 404', 'Publicado, con algún enlace roto o sin probar en el celular', 'No está publicado o no abre'],
    ['Diseño y fidelidad', 'Figma con escritorio, celular y componentes; el sitio respeta sus colores, letras y medidas', 'Hay Figma, pero el sitio se aparta en varias partes', 'Sin Figma o sin relación con el sitio'],
    ['Código y pruebas', 'HTML semántico y válido; explica con seguridad la parte del código que se le pide; Lighthouse de 90 o más en Accesibilidad', 'Explica con ayuda o hay errores en el validador', 'No puede explicar su código'],
    ['Uso responsable de la IA', 'Bitácora con 3 prompts o más: muestra qué pidió, qué corrigió y cómo lo comprobó', 'Bitácora incompleta o sin la comprobación', 'Sin bitácora, o código que no entiende'],
    ['Presentación', 'Sigue el guion, en 5 minutos, con orden y claridad; responde las preguntas', 'Se pasa del tiempo o salta partes del guion', 'No presenta'],
], anchos=['20%', '36%', '26%', '18%'])
d.callout('Usar IA está permitido y se valora:', 'lo que se califica es que la uses bien. Un código que no puedes '
          'explicar resta, aunque funcione.')

d.h3('Orden de las presentaciones')
d.p('El orden se sortea al inicio de la Parte B. Mientras presenta un compañero, el siguiente prepara sus pestañas. '
    'Cada presentación dura 7 minutos: 5 de exposición y 2 de preguntas.')

d.h2('Lista de comprobación')
d.check(['Mi sitio abre desde el celular, en la dirección de Netlify.',
         'Mi Figma está compartido con **puede ver**.',
         'Mi bitácora tiene al menos tres prompts con su corrección y su comprobación.',
         'Ensayé mi guion con un cronómetro: dura 5 minutos.',
         'Sé explicar cualquier regla de mi CSS y cualquier etiqueta de mi HTML.',
         'Subí todo al Aula Virtual antes de la sesión 16.'])

d.guardar(os.path.join(AQUI, '..', 'guias', 'out', 'EF_Parte_B_Pauta_de_Presentacion.html'))
print('ok')
