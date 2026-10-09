# Fuentes de las sesiones 09 a 16

Scripts que generan los materiales de `SESION 09/` a `SESION 16/`. Sirven para
corregir un texto y volver a producir el PDF o la presentación sin rehacerlos a mano.

Los portafolios resueltos (`SESION 09/mi-portafolio-dagner/` a
`SESION 15/mi-portafolio-dagner/`) no se generan: son el código fuente del curso.
Las guías leen de ellos el CSS y el HTML que muestran, así que nunca difieren.

## Qué genera cada carpeta

| Carpeta | Genera | Comando |
|---|---|---|
| `guias/` | Las catorce guías en PDF (código y Figma, de la 09 a la 15) | ver «Guías» |
| `diapositivas/` | Las ocho presentaciones `.pptx` | ver «Diapositivas» |
| `cuestionarios/` | `cuestionario-sesion09.html` a `cuestionario-sesion16.html` | `python3 cuestionarios/quiz.py <repo>` (09 y 10), `quiz_1112.py` (11 y 12), `quiz_1314.py` (13 y 14) y `quiz_1516.py` (15 y el simulacro de la 16) |
| `taller-ta2/` | `SESION 12/Taller online [TA2].docx`, sobre la plantilla del TA1 | `python3 taller-ta2/build_ta2.py <repo>` |
| `imagenes-proyectos/` | Las dos imágenes de ejemplo de las tarjetas de proyecto | `node imagenes-proyectos/render.js` |
| `imagenes-sitio/` | El favicon, el icono del celular y la imagen Open Graph de la sesión 15 | ver «Imágenes del sitio» |
| `examen-final/` | Todo el examen final de la sesión 16 | ver «Examen final» |
| `herramientas/` | Capturas con Playwright; descarga las fuentes de Google y los archivos de jsDelivr | lo usan los demás |

`<repo>` es la carpeta raíz del repositorio (la que contiene `SESION 08/`).

## Requisitos

- Node 18 o superior, con `npm install pptxgenjs playwright` en esta carpeta.
- Python 3.
- Para pasar las presentaciones y el taller a PDF: LibreOffice con Impress y Writer.
- ImageMagick (`convert` y `montage`): arma las imágenes de la sesión 11.
- Para que los PDF salgan con la letra de las sesiones anteriores: la fuente Carlito
  instalada (equivale a Calibri). Las guías ya la traen en `guias/assets/fonts/`.

## Guías

```bash
python3 guias/guia_s11.py <repo>      # también guia_s09 … s15 y figma_s09 … s15 (las de Figma 10 a 15 leen las
                                      # capturas de SESION 15/figma-portafolio-completo)
node guias/pdf.js guias/out/Guia_Sesion11_Transiciones_Transformaciones_y_Animaciones.html \
                  guias/out/Guia_Sesion11_Transiciones_Transformaciones_y_Animaciones.pdf
```

El texto de cada guía está en su script, escrito con las funciones de `guia.py`
(`d.h2`, `d.p`, `d.tabla`, `d.callout`, `d.capa`…). En el texto, `código` va entre
comillas invertidas y **negrita** entre dobles asteriscos.

Las guías de Figma de las sesiones 11 a 15 son una ampliación del manual, que termina
en el Paso 14: el botón como componente con su variante Hover y el prototipo (11), el
marco móvil de 390 (12), la guía de 12 columnas y la página Cursos (13), las
variables locales con el componente de curso (14) y la revisión final con los marcos
`favicon` y `og-portafolio` y el enlace de solo lectura (15).

## Diapositivas

```bash
bash diapositivas/extraer_media.sh <repo>        # bandas CINFO y diapositivas fijas, desde la sesión 08
node diapositivas/render_img.js <repo>           # imágenes de las sesiones 09 y 10
node diapositivas/render_img_1112.js <repo>      # imágenes de las sesiones 11 y 12
node diapositivas/render_img_1314.js <repo>      # demostraciones de Bootstrap y capturas de la 13 y la 14
node diapositivas/render_img_15.js <repo> <informe-lighthouse.html>   # capturas de la 15
node diapositivas/deck_s09.js                    # → diapositivas/out/Sesion09-….pptx
node diapositivas/deck_s10.js                    # y así hasta deck_s16.js
soffice --headless --convert-to pdf --outdir diapositivas/out diapositivas/out/*.pptx
```

`uss.js` reproduce la plantilla de las sesiones 07 y 08: las bandas Conceptual,
Instrumental, Nivelador, Funcional y Orientador, los títulos, las tarjetas y los
bloques de código. Cada diapositiva se escribe en `deck_s09.js` a `deck_s16.js`.
En los bloques de código, `«texto»` se pinta en cian. `fit.js` coloca una imagen en
una caja sin deformarla.

`render_img_1112.js` también arma `s11-hero.gif`, la entrada del Hero en bucle. En
PowerPoint se reproduce; en el PDF se ve su primer cuadro, que es el Hero ya terminado.

## Bootstrap sin acceso a jsDelivr

Las páginas Cursos (sesiones 13 y 14) enlazan Bootstrap 5.3.8 y Bootstrap Icons 1.13.1 desde
cdn.jsdelivr.net, con su `integrity`. Si la red no deja llegar a jsDelivr, `herramientas/shot.js`
responde esas peticiones con el mismo archivo sacado del registro de npm (`npm pack`): jsDelivr
sirve los paquetes de npm tal cual, así que la huella coincide.

## Taller TA2

`build_ta2.py` abre `SESION 06/Taller online [TA1].docx`, cambia los textos, las
indicaciones y la rúbrica, y guarda el resultado en `SESION 12/`. La cabecera, el pie
y los estilos son los del TA1. Para el PDF:

```bash
cd "<repo>/SESION 12" && soffice --headless --convert-to pdf "Taller online [TA2].docx"
```

## Imágenes de los proyectos

`imagenes-proyectos/render.js` produce `proyecto-cinf.jpg` y `proyecto-certificados.jpg`
(1256 × 440, el doble de 628 × 220). Son vistas de ejemplo: cópialas a
`SESION 10/mi-portafolio-dagner/assets/img/` o reemplázalas por capturas reales.

`render_img_15.js` toma `s15-lighthouse.png` de un informe HTML de Lighthouse sobre
`index.html` de la sesión 15. Para hacerlo, sirve la carpeta del portafolio en local y corre
`lighthouse http://127.0.0.1:<puerto>/index.html --output=html --output-path=<informe>`.

## Imágenes del sitio

`imagenes-sitio/render.js` dibuja el monograma «DC» de `icono.html` y la vista previa de
`og.html`, y guarda `favicon-32.png` (32 × 32), `apple-touch-icon.png` (180 × 180) y
`og-portafolio.png` (1200 × 630) en la carpeta que le indiques. Necesita ImageMagick para
reducir el icono.

```bash
node imagenes-sitio/render.js "<repo>/SESION 15/mi-portafolio-dagner/assets/img"
```

## Examen final

La sesión 16 es el examen final (30 %). El formato es una propuesta: una Parte A con 20
preguntas sorteadas de un banco de 40, en el Aula Virtual, y una Parte B con la presentación
del proyecto integrador (5 minutos y 2 de preguntas por estudiante).

| Script | Genera |
|---|---|
| `banco_ef.py` | Las 40 preguntas, en tres bloques. Ninguna se repite en el simulacro |
| `build_banco.py <repo>` | `SESION 16/docente/banco-ef-moodle.gift.txt` y la clave en `guias/out/` |
| `build_ef.py <repo>` | `SESION 16/Examen Final [EF].docx`, sobre la plantilla del TA1, como el TA2 |
| `pauta_parte_b.py` | La pauta de presentación de la Parte B en `guias/out/` |
| `guia_estudio_ef.py` | La guía de estudio en `guias/out/` |
| `planilla_ef.py <repo>` | `SESION 16/docente/Calificacion_EF.xlsx`, con los estudiantes de `ASISTENCIAS/` |

```bash
python3 examen-final/build_ef.py <repo>
python3 examen-final/build_banco.py <repo>
python3 examen-final/pauta_parte_b.py
python3 examen-final/guia_estudio_ef.py
python3 examen-final/planilla_ef.py <repo>      # necesita openpyxl
node guias/pdf.js guias/out/EF_Parte_B_Pauta_de_Presentacion.html guias/out/EF_Parte_B_Pauta_de_Presentacion.pdf
cd "<repo>/SESION 16" && soffice --headless --convert-to pdf "Examen Final [EF].docx"
```

`SESION 16/docente/` es solo para el docente: la clave, el archivo GIFT y la planilla de
calificación. Si el Aula Virtual usa Moodle, el GIFT se importa en Banco de preguntas ›
Importar y crea las tres categorías; el cuestionario sortea 8, 7 y 5 preguntas de cada una.

## Extra de IA (sesiones 11 a 15)

`guias/ia_contenido.py` tiene todo el contenido: las reglas, la fórmula del buen prompt y, por
sesión, el mal y el buen prompt, cuatro prompts con su revisión y las funciones de IA de Figma.

```bash
python3 guias/guia_ia.py                                   # las cinco guías Extra de IA
python3 guias/ia_contenido.py > diapositivas/ia_contenido.json
node diapositivas/deck_s11.js                              # cada deck llama a ia.js antes del Nivelador
```

## El portafolio completo en Figma

`SESION 15/figma-portafolio-completo/` tiene las capturas y el enlace del archivo «Mi portafolio
(Copia) · Completo», armado con el servidor MCP de Figma a partir de los valores de las guías.

## Lo que no se guarda

`.gitignore` excluye lo que se genera: `out/`, `diapositivas/img/`,
`diapositivas/media/`, la caché de fuentes, `__pycache__/` y `node_modules/`.
