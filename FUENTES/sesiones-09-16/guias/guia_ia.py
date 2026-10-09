# -*- coding: utf-8 -*-
"""Extra de IA de las sesiones 11 a 15: una guía por sesión, con el contenido de ia_contenido.py.
uso: python3 guia_ia.py [11 12 13 14 15]   → out/Guia_IA_SesionNN_….html (después, pdf.js)
"""
import os
import sys
from guia import Doc
from ia_contenido import FORMULA, REGLAS, FIGMA_AVISO, SESIONES

AQUI = os.path.dirname(os.path.abspath(__file__))


def guia(n):
    s = SESIONES[n]
    d = Doc(f'Extra de IA · Sesión {n}: {s["tema"]}',
            f'Extra de IA · Sesión {n}',
            f'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión {n} · Codificar con IA y Figma con IA',
            'Usas un asistente de IA para escribir, entender y corregir el código de la sesión con buenos prompts, y las '
            'funciones de IA de Figma para avanzar más rápido en tu diseño. La IA acelera lo que ya entiendes: no '
            'reemplaza la guía ni tu criterio.')

    d.h3('Las reglas del curso')
    d.lista(REGLAS)

    d.h2('La fórmula del buen prompt')
    d.p('Un buen prompt tiene cinco partes. Funciona con cualquier asistente (ChatGPT, Gemini, Claude o Copilot): '
        'escríbelo en español y en un solo mensaje.')
    d.tabla(['Parte', 'Qué escribes', 'Ejemplo'], FORMULA, anchos=['16%', '26%', '58%'])
    d.callout('Si la respuesta no sirve, no empieces de cero:', 'responde en el mismo chat qué falló («usaste '
              '`margin-top`, quiero `transform`») y pide solo ese cambio.')

    d.h2('Mal prompt y buen prompt')
    d.h3('Así no')
    d.code(s['malo'])
    d.h3('Así sí')
    d.code(s['bueno'])
    d.p('**Por qué funciona:**')
    d.lista(s['por_que'])

    d.h2(f'Prompts para la sesión {n}')
    d.p('Cambia lo que está entre corchetes por tu código. Después de cada respuesta, haz la revisión que se indica.')
    for titulo, prompt, revisa in s['prompts']:
        d.h3(titulo)
        d.code(prompt)
        d.p(f'**Revisa:** {revisa}')

    d.h2('Antes de usar lo que te dio la IA')
    d.check(s['verifica'])

    d.h2('Figma con IA', salto=True)
    d.tabla(['Qué', 'Cómo'], s['figma'], anchos=['24%', '76%'])
    d.callout('Sobre los nombres:', FIGMA_AVISO)

    d.h2('Tu bitácora de prompts')
    d.p('Anota cada prompt que te sirvió. La bitácora va en tu proyecto integrador: la entregas con tu sitio en la '
        'sesión 15 y la muestras en tu presentación de la sesión 16.')
    d.tabla(['N.º', 'Para qué', 'Prompt (resumido)', 'Qué me dio', 'Qué corregí', 'Cómo lo comprobé'],
            [['1', '', '', '', '', ''], ['2', '', '', '', '', ''], ['3', '', '', '', '', '']],
            anchos=['6%', '14%', '26%', '18%', '18%', '18%'])
    d.callout('Ejemplo:', '«Hover del botón» · «Actúa como docente de CSS… escribe solo `.btn-primary:hover`…» · '
              'el `:hover` y la `transition` · cambié `all` por `background-color` · lo comparé con la variante Hover de Figma.')

    salida = os.path.join(AQUI, 'out', s['archivo'] + '.html')
    d.guardar(salida)
    return salida


if __name__ == '__main__':
    for n in sys.argv[1:] or sorted(SESIONES):
        print('ok', guia(n))
