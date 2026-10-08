# Fuentes de las sesiones 09 y 10

Scripts que generan los materiales de `SESION 09/` y `SESION 10/`. Sirven para
corregir un texto y volver a producir el PDF o la presentación sin rehacerlos a mano.

Los portafolios resueltos (`SESION 09/mi-portafolio-dagner/` y
`SESION 10/mi-portafolio-dagner/`) no se generan: son el código fuente del curso.
Las guías leen de ellos el CSS y el HTML que muestran, así que nunca difieren.

## Qué genera cada carpeta

| Carpeta | Genera | Comando |
|---|---|---|
| `guias/` | Las cuatro guías en PDF (código y Figma, 09 y 10) | ver «Guías» |
| `diapositivas/` | Las dos presentaciones `.pptx` | ver «Diapositivas» |
| `cuestionarios/` | `cuestionario-sesion09.html` y `cuestionario-sesion10.html` | `python3 cuestionarios/quiz.py <repo>` |
| `imagenes-proyectos/` | Las dos imágenes de ejemplo de las tarjetas de proyecto | `node imagenes-proyectos/render.js` |
| `herramientas/` | Capturas con Playwright y descarga de las fuentes de Google | lo usan los demás |

`<repo>` es la carpeta raíz del repositorio (la que contiene `SESION 08/`).

## Requisitos

- Node 18 o superior, con `npm install pptxgenjs playwright` en esta carpeta.
- Python 3.
- Para pasar las presentaciones a PDF: LibreOffice con Impress.
- Para que los PDF salgan con la letra de las sesiones anteriores: la fuente Carlito
  instalada (equivale a Calibri). Las guías ya la traen en `guias/assets/fonts/`.

## Guías

```bash
python3 guias/guia_s09.py <repo>      # también guia_s10.py, figma_s09.py, figma_s10.py
node guias/pdf.js guias/out/Guia_Sesion09_CSS3_Selectores_Cascada_y_Propiedades.html \
                  guias/out/Guia_Sesion09_CSS3_Selectores_Cascada_y_Propiedades.pdf
```

El texto de cada guía está en su script, escrito con las funciones de `guia.py`
(`d.h2`, `d.p`, `d.tabla`, `d.callout`, `d.capa`…). En el texto, `código` va entre
comillas invertidas y **negrita** entre dobles asteriscos.

## Diapositivas

```bash
bash diapositivas/extraer_media.sh <repo>     # bandas CINFO y diapositivas fijas, desde la sesión 08
node diapositivas/render_img.js <repo>        # capturas del portafolio y demostraciones de CSS
node diapositivas/deck_s09.js                 # → diapositivas/out/Sesion09-….pptx
node diapositivas/deck_s10.js
soffice --headless --convert-to pdf --outdir diapositivas/out diapositivas/out/*.pptx
```

`uss.js` reproduce la plantilla de las sesiones 07 y 08: las bandas Conceptual,
Instrumental, Nivelador, Funcional y Orientador, los títulos, las tarjetas y los
bloques de código. Cada diapositiva se escribe en `deck_s09.js` o `deck_s10.js`.
En los bloques de código, `«texto»` se pinta en cian.

## Imágenes de los proyectos

`imagenes-proyectos/render.js` produce `proyecto-cinf.jpg` y `proyecto-certificados.jpg`
(1256 × 440, el doble de 628 × 220). Son vistas de ejemplo: cópialas a
`SESION 10/mi-portafolio-dagner/assets/img/` o reemplázalas por capturas reales.

## Lo que no se guarda

`.gitignore` excluye lo que se genera: `out/`, `diapositivas/img/`,
`diapositivas/media/`, la caché de fuentes y `node_modules/`.
