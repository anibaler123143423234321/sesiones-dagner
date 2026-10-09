# Fuentes de las sesiones 09 a 12

Scripts que generan los materiales de `SESION 09/` a `SESION 12/`. Sirven para
corregir un texto y volver a producir el PDF o la presentación sin rehacerlos a mano.

Los portafolios resueltos (`SESION 09/mi-portafolio-dagner/` a
`SESION 12/mi-portafolio-dagner/`) no se generan: son el código fuente del curso.
Las guías leen de ellos el CSS y el HTML que muestran, así que nunca difieren.

## Qué genera cada carpeta

| Carpeta | Genera | Comando |
|---|---|---|
| `guias/` | Las ocho guías en PDF (código y Figma, de la 09 a la 12) | ver «Guías» |
| `diapositivas/` | Las cuatro presentaciones `.pptx` | ver «Diapositivas» |
| `cuestionarios/` | `cuestionario-sesion09.html` a `cuestionario-sesion12.html` | `python3 cuestionarios/quiz.py <repo>` (09 y 10) y `python3 cuestionarios/quiz_1112.py <repo>` (11 y 12) |
| `taller-ta2/` | `SESION 12/Taller online [TA2].docx`, sobre la plantilla del TA1 | `python3 taller-ta2/build_ta2.py <repo>` |
| `imagenes-proyectos/` | Las dos imágenes de ejemplo de las tarjetas de proyecto | `node imagenes-proyectos/render.js` |
| `herramientas/` | Capturas con Playwright y descarga de las fuentes de Google | lo usan los demás |

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
python3 guias/guia_s11.py <repo>      # también guia_s09/10/12.py y figma_s09/10/11/12.py
node guias/pdf.js guias/out/Guia_Sesion11_Transiciones_Transformaciones_y_Animaciones.html \
                  guias/out/Guia_Sesion11_Transiciones_Transformaciones_y_Animaciones.pdf
```

El texto de cada guía está en su script, escrito con las funciones de `guia.py`
(`d.h2`, `d.p`, `d.tabla`, `d.callout`, `d.capa`…). En el texto, `código` va entre
comillas invertidas y **negrita** entre dobles asteriscos.

Las guías de Figma de las sesiones 11 y 12 son una ampliación del manual, que termina
en el Paso 14: el botón como componente con su variante Hover y el prototipo (11) y el
marco móvil de 390 (12).

## Diapositivas

```bash
bash diapositivas/extraer_media.sh <repo>        # bandas CINFO y diapositivas fijas, desde la sesión 08
node diapositivas/render_img.js <repo>           # imágenes de las sesiones 09 y 10
node diapositivas/render_img_1112.js <repo>      # imágenes de las sesiones 11 y 12
node diapositivas/deck_s09.js                    # → diapositivas/out/Sesion09-….pptx
node diapositivas/deck_s10.js
node diapositivas/deck_s11.js
node diapositivas/deck_s12.js
soffice --headless --convert-to pdf --outdir diapositivas/out diapositivas/out/*.pptx
```

`uss.js` reproduce la plantilla de las sesiones 07 y 08: las bandas Conceptual,
Instrumental, Nivelador, Funcional y Orientador, los títulos, las tarjetas y los
bloques de código. Cada diapositiva se escribe en `deck_s09.js` a `deck_s12.js`.
En los bloques de código, `«texto»` se pinta en cian. `fit.js` coloca una imagen en
una caja sin deformarla.

`render_img_1112.js` también arma `s11-hero.gif`, la entrada del Hero en bucle. En
PowerPoint se reproduce; en el PDF se ve su primer cuadro, que es el Hero ya terminado.

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

## Lo que no se guarda

`.gitignore` excluye lo que se genera: `out/`, `diapositivas/img/`,
`diapositivas/media/`, la caché de fuentes, `__pycache__/` y `node_modules/`.
