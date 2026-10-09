# -*- coding: utf-8 -*-
"""Examen final [EF]: rellena la plantilla del TA1 con el contenido del examen final.

Conserva el formato, la cabecera, el pie y los estilos del documento de la sesión 06,
igual que build_ta2.py; solo cambian los textos y la tabla de criterios.
uso: python3 build_ef.py <repo>
     → <repo>/SESION 16/Examen Final [EF].docx
Para el PDF: soffice --headless --convert-to pdf "Examen Final [EF].docx"
"""
import os
import re
import shutil
import sys
import tempfile
import zipfile
from xml.sax.saxutils import escape

REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/user/sesiones-dagner'
PLANTILLA = os.path.join(REPO, 'SESION 06', 'Taller online [TA1].docx')
SALIDA = os.path.join(REPO, 'SESION 16', 'Examen Final [EF].docx')

TMP = tempfile.mkdtemp()
with zipfile.ZipFile(PLANTILLA) as z:
    z.extractall(TMP)
DOC = os.path.join(TMP, 'word', 'document.xml')
s = open(DOC, encoding='utf8').read()
SPANS = [m.span() for m in re.finditer(r'<w:p[ >].*?</w:p>', s, flags=re.S)]
ps = [s[a:b] for a, b in SPANS]
NUEVOS = {}

RPR = {'n': '', 'b': '<w:rPr><w:b/><w:bCs/></w:rPr>', 'i': '<w:rPr><w:i/><w:iCs/></w:rPr>',
       'c': '<w:rPr><w:rStyle w:val="CdigoHTML"/></w:rPr>',
       'ct': '<w:rPr><w:rStyle w:val="CdigoHTML"/><w:rFonts w:eastAsia="Calibri"/></w:rPr>'}


def runs(markup, tabla=False):
    """**negrita**, _cursiva_ y `código` → runs de Word."""
    out = []
    for tok in re.split(r'(\*\*.+?\*\*|_.+?_|`.+?`)', markup):
        if not tok:
            continue
        if tok.startswith('**'): k, t = 'b', tok[2:-2]
        elif tok.startswith('`'): k, t = ('ct' if tabla else 'c'), tok[1:-1]
        elif tok.startswith('_') and tok.endswith('_') and len(tok) > 2: k, t = 'i', tok[1:-1]
        else: k, t = 'n', tok
        out.append(f'<w:r>{RPR[k]}<w:t xml:space="preserve">{escape(t)}</w:t></w:r>')
    return ''.join(out)


def poner(i, markup, tabla=False):
    p = NUEVOS.get(i, ps[i])
    ppr = re.match(r'(<w:p[ >][^>]*>|<w:p>)(<w:pPr>.*?</w:pPr>)?', p, flags=re.S)
    NUEVOS[i] = ppr.group(1) + (ppr.group(2) or '') + runs(markup, tabla) + '</w:p>'


def cambiar(i, viejo, nuevo):
    p = NUEVOS.get(i, ps[i])
    assert p.count(viejo) == 1, (i, viejo)
    NUEVOS[i] = p.replace(viejo, nuevo)


# cabecera: TALLER ONLINE [TA1-1] → EXAMEN FINAL [EF]
cambiar(0, '>TALLER<', '>EXAMEN<')
cambiar(0, '>ONLINE<', '>FINAL<')
cambiar(0, '[TA1-1]', '[EF]')
cambiar(4, '>(Zoom)<', '>(Aula Virtual USS)<')
cambiar(4, '>15%<', '>30%<')
cambiar(5, '01/10/2026', '05/11/2026')
cambiar(6, 'DISEÑAR EN FIGMA Y HTML', 'EVALUACIÓN INTEGRADORA')
cambiar(7, '4 horas', '2 horas')

poner(12, 'El **examen final** evalúa las **sesiones 1 a 16**. Es **individual** y se rinde en el **Aula Virtual USS** '
          'el **jueves 05/11/2026**, en el horario de clase.')
poner(13, 'Tiene **dos partes**, que se rinden una después de la otra en la misma sesión:')
poner(14, '**Parte A · Cuestionario (10 puntos, 40 minutos):** 20 preguntas de opción múltiple de las sesiones 1 a 16, '
          'a 0.5 puntos cada una. Un solo intento, en orden aleatorio.')
poner(15, '**Parte B · Caso práctico (10 puntos, 80 minutos):** construir la página _Semana de la Informática 2026_ '
          'según la **ficha técnica** publicada en el Aula Virtual, con HTML semántico, CSS externo y diseño adaptable.')
poner(16, '**Requisitos de la Parte B:** etiquetas semánticas, variables en `:root`, `grid` o la grilla de Bootstrap, '
          'una media query para el celular, un `:hover` con `transition` y un formulario con `label` y `required`.')
poner(17, '**Entrega de la Parte B:** la carpeta comprimida `apellido-nombre-ef.zip`, con `index.html` y '
          '`assets/css/estilos.css`, en la tarea del Aula Virtual.')
poner(18, '**Materiales permitidos:** su portafolio, las guías del curso, MDN y getbootstrap.com. Para repasar: el '
          '**simulacro** de la sesión 16.')

poner(20, '**Conexión:** Ingrese al Aula Virtual 10 minutos antes. Cada parte se cierra a la hora indicada, aunque no '
          'haya terminado.')
poner(21, '**Problemas técnicos:** Si se corta la conexión, vuelva a ingresar: el cuestionario conserva las respuestas '
          'guardadas. Avise al docente de inmediato.')
poner(22, '**Originalidad:** El examen es individual. Los trabajos iguales entre sí o elaborados por terceros se '
          'califican con cero.')

filas = [
    (32, 33, 34, 'Parte A · Cuestionario', '20 preguntas de opción múltiple de las sesiones 1 a 16, en el Aula Virtual. 0.5 puntos por respuesta correcta.', '50%'),
    (35, 36, 37, 'Estructura semántica', '`header`, `nav`, `main`, `section`, `article` y `footer`; un solo `h1`; HTML sin errores en el validador del W3C.', '10%'),
    (38, 39, 40, 'Estilos y variables', 'CSS externo en `assets/css/`, con los valores de la ficha técnica como variables en `:root` y las fuentes enlazadas.', '10%'),
    (41, 42, 43, 'Maquetación', 'Cabecera con Flexbox y charlas en `grid` o en la grilla de Bootstrap, con las medidas de la ficha técnica.', '10%'),
    (44, 45, 46, 'Diseño adaptable', 'Etiqueta `viewport` y una media query que pasa las charlas a una columna, sin barra horizontal a 390 px.', '10%'),
    (47, 48, 49, 'Interacción y formulario', 'Hover con `transition` en el botón y en el menú; campos con `label`, `name` y `required`; `type="email"` en el correo.', '10%'),
]
for a, b, c, crit, desc, pts in filas:
    poner(a, f'**{crit}**', tabla=True)
    poner(b, desc, tabla=True)
    poner(c, pts, tabla=True)
cambiar(52, '15% del Promedio Final', '30% del Promedio Final')

for i in sorted(NUEVOS, reverse=True):
    a, b = SPANS[i]
    s = s[:a] + NUEVOS[i] + s[b:]
with open(DOC, 'w', encoding='utf8') as f:
    f.write(s)
# el título del documento en sus propiedades
for prop in ('core.xml', 'app.xml'):
    ruta = os.path.join(TMP, 'docProps', prop)
    if os.path.exists(ruta):
        t = open(ruta, encoding='utf8').read().replace('Taller online', 'Examen final').replace('TA1', 'EF')
        open(ruta, 'w', encoding='utf8').write(t)

# se vuelve a comprimir con [Content_Types].xml primero, como lo guarda Word
os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
with zipfile.ZipFile(PLANTILLA) as z:
    orden = [i.filename for i in z.infolist()]
with zipfile.ZipFile(SALIDA, 'w', zipfile.ZIP_DEFLATED) as z:
    for nombre in orden:
        z.write(os.path.join(TMP, nombre), nombre)
shutil.rmtree(TMP)
print('ok', SALIDA)
