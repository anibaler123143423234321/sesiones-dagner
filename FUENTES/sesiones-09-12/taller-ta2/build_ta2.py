# -*- coding: utf-8 -*-
"""Taller online TA2: rellena la plantilla del TA1 con el contenido del TA2.

Conserva el formato, la cabecera, el pie y los estilos del documento de la sesión 06;
solo cambia los textos y la rúbrica.
uso: python3 build_ta2.py <repo>
     → <repo>/SESION 12/Taller online [TA2].docx
Para el PDF: soffice --headless --convert-to pdf "Taller online [TA2].docx"
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
SALIDA = os.path.join(REPO, 'SESION 12', 'Taller online [TA2].docx')

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
    p = ps[i]
    ppr = re.match(r'(<w:p[ >][^>]*>|<w:p>)(<w:pPr>.*?</w:pPr>)?', p, flags=re.S)
    NUEVOS[i] = ppr.group(1) + (ppr.group(2) or '') + runs(markup, tabla) + '</w:p>'

def cambiar(i, viejo, nuevo):
    p = ps[i]
    assert p.count(viejo) == 1, (i, viejo)
    NUEVOS[i] = p.replace(viejo, nuevo)

cambiar(0, '[TA1-1]', '[TA2-1]')
cambiar(5, '01/10/2026', '22/10/2026')
cambiar(6, 'DISEÑAR EN FIGMA Y HTML', 'CSS3 Y DISEÑO RESPONSIVO')

poner(12, 'Aplicar **CSS3** al **sitio web de su TA1** (o a su portafolio del curso) para que reproduzca su '
          'diseño de Figma **en escritorio y en celular**.')
poner(13, 'El proyecto debe ser publicado en **Netlify** y cumplir estrictamente con los siguientes requerimientos '
          'técnicos desarrollados entre las sesiones 7 y 12:')
poner(14, '**Diseño en Figma de escritorio y celular:** Presentar el marco de escritorio y un marco móvil de 390 de '
          'ancho, con al menos un componente con variante Hover y su prototipo. Enlace compartido en modo de '
          '_solo lectura_.')
poner(15, '**Hojas de estilo externas:** CSS en `assets/css/`, con los colores y tipografías de Figma como '
          'variables en `:root` y sin estilos en línea.')
poner(16, '**Flexbox y Grid:** Al menos un contenedor `flex` y uno `grid` que reproduzcan la Disposición '
          'automática de su diseño.')
poner(17, '**Diseño responsivo:** Etiqueta `viewport`, media queries para tablet y celular y al menos una medida '
          'fluida (`clamp()`, `auto-fit` o `aspect-ratio`), sin desplazamiento horizontal a 390 px.')
poner(18, '**Transiciones y animaciones:** Estados `:hover` con `transition` en enlaces y botones, al menos un '
          '`transform` y una animación con `@keyframes`, respetando `prefers-reduced-motion`.')

poner(20, '**Entrega por Aula Virtual:** Debe enviar la **URL del sitio publicado en Netlify** y el **enlace de '
          'Figma** con los dos marcos (escritorio y celular).')
poner(22, '**Originalidad:** No se aceptan trabajos elaborados total o parcialmente por terceros ni la carpeta '
          'resuelta del curso.')

filas = [
    (32, 33, 34, 'Diseño en Figma', 'Marco de escritorio y marco móvil de 390 coherentes con el sitio; al menos un componente con variante Hover y su prototipo; enlace en modo solo lectura.', '15%'),
    (35, 36, 37, 'Arquitectura CSS', 'Hojas externas en `assets/css/`, variables en `:root` con los colores y tipografías de Figma, selectores de clase legibles y sin estilos en línea.', '15%'),
    (38, 39, 40, 'Maquetación (Flexbox y Grid)', 'Contenedores `flex` y `grid` que reproducen el Flujo, el Espacio, el Espaciado y la alineación del diseño.', '20%'),
    (41, 42, 43, 'Diseño Responsivo', 'Etiqueta `viewport`, media queries para tablet y celular, medidas fluidas (`clamp`, `auto-fit`, `aspect-ratio`) y sin desplazamiento horizontal a 390 px.', '25%'),
    (44, 45, 46, 'Transiciones y Animaciones', 'Estados `:hover` con `transition`, al menos un `transform` y una animación `@keyframes`; respeta `prefers-reduced-motion`.', '10%'),
    (47, 48, 49, 'Validación y Despliegue', 'HTML y CSS validados sin errores en el W3C y sitio web correctamente desplegado y funcional en Netlify.', '15%'),
]
for a, b, c, crit, desc, pts in filas:
    poner(a, f'**{crit}**', tabla=True)
    poner(b, desc, tabla=True)
    poner(c, pts, tabla=True)

for i in sorted(NUEVOS, reverse=True):
    a, b = SPANS[i]
    s = s[:a] + NUEVOS[i] + s[b:]
with open(DOC, 'w', encoding='utf8') as f:
    f.write(s)
# el título del documento en sus propiedades
for prop in ('core.xml', 'app.xml'):
    ruta = os.path.join(TMP, 'docProps', prop)
    if os.path.exists(ruta):
        t = open(ruta, encoding='utf8').read().replace('TA1', 'TA2')
        open(ruta, 'w', encoding='utf8').write(t)

# se vuelve a comprimir con [Content_Types].xml primero, como lo guarda Word
with zipfile.ZipFile(PLANTILLA) as z:
    orden = [i.filename for i in z.infolist()]
with zipfile.ZipFile(SALIDA, 'w', zipfile.ZIP_DEFLATED) as z:
    for nombre in orden:
        z.write(os.path.join(TMP, nombre), nombre)
shutil.rmtree(TMP)
print('ok', SALIDA)
