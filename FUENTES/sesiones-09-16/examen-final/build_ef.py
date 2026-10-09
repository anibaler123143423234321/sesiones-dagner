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
cambiar(4, '>Virtual<', '>Clase sincrónica<')
cambiar(4, '>(Zoom)<', '>y Aula Virtual USS<')
cambiar(4, '>15%<', '>30%<')
cambiar(5, '01/10/2026', '05/11/2026')
cambiar(6, 'DISEÑAR EN FIGMA Y HTML', 'EVALUACIÓN INTEGRADORA')
cambiar(7, '4 horas', '4 horas (toda la sesión)')

poner(12, 'El **examen final** evalúa las **sesiones 1 a 16**. Es **individual** y se rinde el **jueves 05/11/2026**, '
          'en el horario de clase: el cuestionario en el **Aula Virtual USS** y la presentación en la clase.')
poner(13, 'Tiene **dos partes**, que se rinden una después de la otra en la misma sesión:')
poner(14, '**Parte A · Cuestionario (10 puntos, 40 minutos):** 20 preguntas de opción múltiple de las sesiones 1 a 16, '
          'a 0.5 puntos cada una. Un solo intento, en orden aleatorio.')
poner(15, '**Parte B · Presentación del proyecto integrador (10 puntos, 7 minutos por estudiante):** 5 minutos para '
          'presentar el portafolio publicado, su diseño en Figma y el uso de la IA, y 2 minutos de preguntas.')
poner(16, '**Guion de la Parte B:** presentación del sitio, diseño en Figma, recorrido por el sitio publicado (incluido '
          'el celular), el mejor prompt de la bitácora y la captura de Lighthouse. Ver la **pauta de presentación**.')
poner(17, '**Entrega previa:** antes de la sesión, subir a la tarea **Proyecto integrador** la dirección de Netlify, el '
          'enlace de Figma, la carpeta `apellido-nombre-portafolio.zip`, la captura de Lighthouse y la bitácora de prompts.')
poner(18, '**Materiales permitidos en la Parte A:** ninguno; el cuestionario es individual y sin consulta. Para repasar: '
          'la guía de estudio y el **simulacro** de la sesión 16.')

poner(20, '**Conexión:** Ingrese al Aula Virtual 10 minutos antes. El cuestionario se cierra a la hora indicada, aunque no '
          'haya terminado.')
poner(21, '**Problemas técnicos:** Si se corta la conexión, vuelva a ingresar: el cuestionario conserva las respuestas '
          'guardadas. Si su sitio no abre al presentar, presente desde la carpeta `.zip`.')
poner(22, '**Originalidad:** Puede usar IA en su proyecto si la registra en la bitácora y explica su código. Los trabajos '
          'iguales entre sí o elaborados por terceros se califican con cero.')

filas = [
    (32, 33, 34, 'Parte A · Cuestionario', '20 preguntas de opción múltiple de las sesiones 1 a 16, en el Aula Virtual. 0.5 puntos por respuesta correcta.', '50%'),
    (35, 36, 37, 'Sitio publicado y funcional', 'En Netlify, con los enlaces, el celular a 390 px, el formulario y la página 404 funcionando.', '10%'),
    (38, 39, 40, 'Diseño y fidelidad', 'Figma con escritorio, celular y componentes; el sitio respeta sus colores, letras y medidas.', '10%'),
    (41, 42, 43, 'Código y pruebas', 'HTML semántico y válido; explica la parte del código que se le pide; Lighthouse de 90 o más en Accesibilidad.', '10%'),
    (44, 45, 46, 'Uso responsable de la IA', 'Bitácora con al menos 3 prompts: qué pidió, qué corrigió y cómo lo comprobó.', '10%'),
    (47, 48, 49, 'Presentación', 'Sigue el guion en 5 minutos, con orden y claridad, y responde las preguntas.', '10%'),
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
