# -*- coding: utf-8 -*-
"""Examen final · Parte A: el banco de 40 preguntas en dos formatos.
- banco-ef-moodle.gift.txt: para importar en un Aula Virtual con Moodle (Banco de preguntas › Importar › GIFT)
- guias/out/Banco_EF_Parte_A_con_Clave.html: la clave para el docente (se imprime a PDF con guias/pdf.js)
uso: python3 build_banco.py <repo>
"""
import html
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'guias'))
from guia import Doc, fmt  # noqa: E402
from banco_ef import BLOQUES  # noqa: E402

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
DOCENTE = os.path.join(REPO, 'SESION 16', 'docente')
os.makedirs(DOCENTE, exist_ok=True)


# ---------- GIFT
def gift_html(texto):
    """`código` → <code>, el resto escapado para HTML y después para GIFT."""
    partes = re.split(r'(`[^`]+`)', texto)
    out = ''.join(f'<code>{html.escape(p[1:-1], quote=False)}</code>' if p.startswith('`') else html.escape(p, quote=False)
                  for p in partes)
    return re.sub(r'([~=#{}:\\])', r'\\\1', out)


lineas = ['// Examen final · Diseño Web · Centro de Informática USS · Parte A',
          '// 40 preguntas en tres categorías. Sortear 8 del bloque 1, 7 del bloque 2 y 5 del bloque 3.', '']
n = 0
for titulo, _, preguntas in BLOQUES:
    lineas += [f'$CATEGORY: $course$/top/Examen final EF/{titulo.split(" · ")[0]}', '']
    for x in preguntas:
        n += 1
        ops = ' '.join(('=' if k == x['c'] else '~') + gift_html(o) for k, o in enumerate(x['o']))
        lineas.append(f'::EF-{n:02d} · S{x["sesion"]} · {gift_html(x["tema"])}::[html]{gift_html(x["p"])} {{ {ops} #### {gift_html(x["e"])} }}')
        lineas.append('')
gift = os.path.join(DOCENTE, 'banco-ef-moodle.gift.txt')
open(gift, 'w', encoding='utf-8').write('\n'.join(lineas))
print('ok', gift, n, 'preguntas')

# ---------- Clave para el docente
d = Doc('Examen final · Parte A: banco de preguntas con clave',
        'Examen final · Parte A · Banco con clave (solo docente)',
        'Curso Diseño Web · Centro de Informática USS · Protech XP · Sesión 16 · Jueves 05/11/2026 · Aula Virtual USS',
        'Cuarenta preguntas de opción múltiple sobre las sesiones 01 a 15, en tres bloques. El Aula Virtual sortea veinte: '
        'ocho del bloque 1, siete del bloque 2 y cinco del bloque 3. Cada una vale 0.5 puntos.')
d.callout('Documento para el docente:', 'no lo compartas con los estudiantes. El simulacro de la sesión 16 '
          '(`cuestionario-sesion16.html`) usa otras preguntas sobre los mismos temas.')
d.h3('Cómo configurarlo en el Aula Virtual')
d.tabla(['Ajuste', 'Valor propuesto'], [
    ['Preguntas', '20 al azar: 8 del bloque 1, 7 del bloque 2 y 5 del bloque 3'],
    ['Puntaje', '0.5 por pregunta: 10 puntos en total, la mitad de la nota del examen'],
    ['Tiempo', '40 minutos, un solo intento'],
    ['Orden', 'Preguntas y opciones en orden aleatorio'],
    ['Revisión', 'Mostrar la respuesta correcta y la explicación al cerrar el examen'],
    ['Importar', 'Si el Aula Virtual usa Moodle: Banco de preguntas › Importar › formato GIFT › `banco-ef-moodle.gift.txt`. Crea las tres categorías solo'],
], anchos=['22%', '78%'])
n = 0
for titulo, sortear, preguntas in BLOQUES:
    d.h2(f'{titulo} · se sortean {sortear} de {len(preguntas)}', salto=n > 0)
    filas = []
    for x in preguntas:
        n += 1
        ops = '<br>'.join(('<b>' if k == x['c'] else '') + f'{"ABCD"[k]}) {fmt(o)}' + ('</b>' if k == x['c'] else '')
                          for k, o in enumerate(x['o']))
        filas.append(f'<tr><td>{n:02d}</td><td>S{x["sesion"]}</td><td>{fmt(x["p"])}<br><span style="color:#4B5563">{ops}</span></td>'
                     f'<td><b>{"ABCD"[x["c"]]}</b></td><td>{fmt(x["e"])}</td></tr>')
    d.raw('<table class="t"><colgroup><col style="width:6%"><col style="width:7%"><col style="width:52%"><col style="width:7%"><col style="width:28%"></colgroup>'
          '<thead><tr><th>N.º</th><th>Ses.</th><th>Pregunta y opciones</th><th>Clave</th><th>Por qué</th></tr></thead>'
          f'<tbody>{"".join(filas)}</tbody></table>')
d.h2('Clave rápida')
claves = []
n = 0
for _, _, preguntas in BLOQUES:
    for x in preguntas:
        n += 1
        claves.append(f'{n:02d}-{"ABCD"[x["c"]]}')
filas = [claves[i:i + 8] for i in range(0, 40, 8)]
d.tabla(['', '', '', '', '', '', '', ''], filas, negrita_primera=False)
d.guardar(os.path.join(AQUI, '..', 'guias', 'out', 'Banco_EF_Parte_A_con_Clave.html'))
print('ok clave')
