# -*- coding: utf-8 -*-
"""Generador de las guías en PDF del curso Diseño Web (USS · Protech XP).

Cada guía se escribe con las funciones de la clase Doc y se guarda como HTML;
pdf.js la imprime en A4 con Chromium. El código CSS y HTML que aparece en las
guías se extrae de los archivos del portafolio resuelto, así nunca difiere.
"""
import html
import os
import re
import textwrap

AQUI = os.path.dirname(os.path.abspath(__file__))

CSS = r"""
@import url('assets/carlito-local.css');
@page { size: A4; margin: 16mm 19mm 18mm 19mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Carlito, Calibri, 'Liberation Sans', sans-serif; font-size: 10.6pt; line-height: 1.5; color: #1F2326; margin: 0; }
.cab { display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #33393D; padding: 0 0 8px; margin: 0 0 12px; }
.cab img.uss { height: 40px; } .cab img.px { height: 27px; }
.cab .centro { text-align: center; font-size: 9pt; line-height: 1.35; }
.cab .centro b { display: block; font-size: 9.6pt; }
h1 { font-size: 19pt; line-height: 1.18; margin: 4px 0 4px; }
.meta { color: #5F676C; font-size: 8.4pt; margin: 0 0 2px; }
.lead { margin: 0 0 6px; }
h2 { color: #177E89; font-size: 13.4pt; border-bottom: 1px solid #CFD5D9; padding-bottom: 3px; margin: 20px 0 9px; break-after: avoid; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 15px 0 6px; break-after: avoid; page-break-after: avoid; }
h4 { font-size: 10.6pt; margin: 12px 0 5px; break-after: avoid; }
.in { margin-left: 18px; }
p { margin: 0 0 7px; }
ul, ol { margin: 2px 0 9px; padding-left: 22px; }
li { margin: 0 0 3px; }
code, .mono { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.5pt; }
pre.code { font-family: 'DejaVu Sans Mono', monospace; font-size: 7.9pt; line-height: 1.45; border: 1px solid #CFD5D9; background: #FAFBFB; padding: 7px 12px; margin: 6px 0 10px; white-space: pre-wrap; word-break: break-word; }
pre.code.corto { break-inside: avoid; page-break-inside: avoid; }
pre.code .nota { color: #177E89; font-weight: bold; }
table.t { width: 100%; border-collapse: collapse; font-size: 9.4pt; margin: 6px 0 12px; line-height: 1.38; }
table.t th { text-align: left; border-top: 1.5px solid #1F2326; border-bottom: 1px solid #1F2326; padding: 6px 8px; font-weight: bold; }
table.t td { border-bottom: 1px solid #CFD5D9; padding: 6px 8px; vertical-align: top; }
table.t tr:last-child td { border-bottom: 1.5px solid #1F2326; }
table.t.b1 td:first-child { font-weight: bold; }
table.t tr { break-inside: avoid; page-break-inside: avoid; }
.callout { border: 1.5px solid #33393D; padding: 8px 13px; margin: 10px 0 12px; break-inside: avoid; page-break-inside: avoid; }
.callout p:last-child { margin-bottom: 0; }
.comprueba { margin: 6px 0 10px; }
ul.check { list-style: none; padding-left: 4px; }
ul.check li { padding-left: 22px; position: relative; }
ul.check li::before { content: ''; position: absolute; left: 0; top: 3px; width: 11px; height: 11px; border: 1.2px solid #5F676C; border-radius: 2px; }
.nobreak { break-inside: avoid; page-break-inside: avoid; }
.salto { break-before: page; page-break-before: always; }
/* Bloques de Figma: Selecciona en Capas */
.capa { margin: 8px 0 14px; break-inside: avoid; page-break-inside: avoid; }
.capa-tit { border-top: 1.5px solid #1F2326; border-bottom: 1px solid #1F2326; padding: 5px 8px; font-size: 9.4pt; }
.capa-tit b { font-weight: bold; } .capa-tit i { color: #33393D; }
table.panel { width: 100%; border-collapse: collapse; font-size: 9.2pt; line-height: 1.35; }
table.panel th { text-align: left; color: #5F676C; font-size: 7.4pt; font-weight: normal; letter-spacing: .04em; padding: 4px 8px; border-bottom: 1px solid #CFD5D9; }
table.panel td { padding: 4px 8px; border-bottom: 1px solid #E3E7EA; vertical-align: top; }
table.panel td.sec { font-weight: bold; border-right: 1px solid #CFD5D9; width: 27%; }
table.panel td.campo { width: 31%; }
table.panel tr.fin td { border-bottom: 1px solid #1F2326; }
/* Esquema de la página */
.esq { border: 1px solid #CFD5D9; padding: 8px 10px 10px; font-size: 7.6pt; color: #33393D; margin: 6px 0 4px; }
.esq .rot { color: #5F676C; margin-bottom: 4px; }
.esq .s { border: 1px solid #9AA2A7; background: #fff; margin: 3px 0; padding: 4px 8px; display: flex; justify-content: space-between; }
.esq .s.hoy { border: 1.5px solid #177E89; background: #F1F8F9; display: block; padding: 5px 8px 8px; }
.esq .s.hoy > .tit { display: flex; justify-content: space-between; color: #177E89; font-weight: bold; margin-bottom: 5px; }
.esq .s.hoy > .tit span:last-child { font-weight: normal; color: #5F676C; }
.esq .s.prev { background: #F3F5F6; color: #5F676C; }
.esq .fila { display: flex; gap: 8px; align-items: center; margin-left: 22px; }
.esq .caja { border: 1px solid #9AA2A7; background: #fff; border-radius: 3px; padding: 4px 7px; }
.esq .gris { background: #D9DEE2; text-align: center; color: #33393D; }
.esq .num { color: #177E89; font-weight: bold; font-size: 7.6pt; }
.esq .pie { color: #5F676C; }
.leyenda { font-style: italic; color: #5F676C; font-size: 9pt; margin: 2px 0 10px; }
"""


def esc(s):
    return html.escape(s, quote=False)


def fmt(s):
    """Texto en línea: `código` y **negrita**."""
    out = esc(s)
    out = re.sub(r'`([^`]+)`', r'<code>\1</code>', out)
    out = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', out)
    return out


def leer(ruta):
    with open(ruta, encoding='utf8') as f:
        return f.read()


def css_bloques(ruta):
    """Divide una hoja de estilos en bloques numerados por sus comentarios
    '/* 1. …', '/* 13.2 …' escritos al inicio de la línea."""
    lineas = leer(ruta).split('\n')
    bloques, actual, clave = {}, [], None
    for ln in lineas:
        m = re.match(r'^/\* (\d+(?:\.\d+)?)[.\s]', ln)
        if m or ln.startswith('/* ====='):
            if clave is not None:
                bloques[clave] = '\n'.join(actual).rstrip()
            clave = m.group(1) if m else None
            actual = [ln] if m else []
            continue
        if clave is not None:
            actual.append(ln)
    if clave is not None:
        bloques[clave] = '\n'.join(actual).rstrip()
    return bloques


def html_entre(ruta, desde, hasta, incluir_hasta=True, ocurrencia_hasta=1):
    """Fragmento de un HTML entre dos textos, sin la sangría común."""
    s = leer(ruta)
    i = s.index(desde)
    i = s.rindex('\n', 0, i) + 1
    j = i
    for _ in range(ocurrencia_hasta):
        j = s.index(hasta, j + 1)
    j = j + len(hasta) if incluir_hasta else j
    return textwrap.dedent(s[i:j]).strip('\n')


class Doc:
    def __init__(self, titulo, titulo_corto, meta, lead):
        self.titulo, self.titulo_corto = titulo, titulo_corto
        self.partes = [
            '<div class="cab"><img class="uss" src="assets/logo-uss.png" alt="USS">'
            '<div class="centro"><b>Curso de Diseño Web</b>Docente: Ing. Dagner Anibal Chuman Lluen</div>'
            '<img class="px" src="assets/logo-protech.png" alt="Protech XP"></div>',
            f'<h1>{fmt(titulo)}</h1>',
            f'<p class="meta">{fmt(meta)}</p>',
            f'<p class="lead">{fmt(lead)}</p>',
        ]
        self._in = False

    # --- estructura
    def h2(self, t, salto=False):
        self._cerrar()
        attr = ' class="salto"' if salto else ''
        self.partes.append(f'<h2{attr}>{fmt(t)}</h2>')
        self.partes.append('<div class="in">')
        self._in = True

    def h3(self, t):
        self._cerrar()
        self.partes.append(f'<h3>{fmt(t)}</h3>')
        self.partes.append('<div class="in">')
        self._in = True

    def h4(self, t):
        self.partes.append(f'<h4>{fmt(t)}</h4>')

    def _cerrar(self):
        if self._in:
            self.partes.append('</div>')
            self._in = False

    def salto(self):
        self.partes.append('<div class="salto"></div>')

    # --- contenido
    def p(self, t):
        self.partes.append(f'<p>{fmt(t)}</p>')

    def comprueba(self, t):
        self.partes.append(f'<p class="comprueba"><b>Comprueba:</b> {fmt(t)}</p>')

    def lista(self, items, ordenada=False):
        tag = 'ol' if ordenada else 'ul'
        self.partes.append(f'<{tag}>' + ''.join(f'<li>{fmt(i)}</li>' for i in items) + f'</{tag}>')

    def pasos(self, items):
        self.lista(items, ordenada=True)

    def check(self, items):
        self.partes.append('<ul class="check">' + ''.join(f'<li>{fmt(i)}</li>' for i in items) + '</ul>')

    def callout(self, lead, texto):
        self.partes.append(f'<div class="callout"><p><b>{fmt(lead)}</b> {fmt(texto)}</p></div>')

    def code(self, texto, corto=None):
        texto = texto.strip('\n')
        if corto is None:
            corto = texto.count('\n') < 22
        cls = 'code corto' if corto else 'code'
        self.partes.append(f'<pre class="{cls}">{esc(texto)}</pre>')

    def tabla(self, cabecera, filas, negrita_primera=True, anchos=None):
        cols = ''
        if anchos:
            cols = '<colgroup>' + ''.join(f'<col style="width:{a}">' for a in anchos) + '</colgroup>'
        h = ''.join(f'<th>{fmt(c)}</th>' for c in cabecera)
        cuerpo = ''.join('<tr>' + ''.join(f'<td>{fmt(c)}</td>' for c in f) + '</tr>' for f in filas)
        cls = 't b1' if negrita_primera else 't'
        self.partes.append(f'<table class="{cls}">{cols}<thead><tr>{h}</tr></thead><tbody>{cuerpo}</tbody></table>')

    def raw(self, h):
        self.partes.append(h)

    def capa(self, nombre, donde, secciones):
        """Bloque de Figma. secciones = [(sección, [(campo, valor), ...]), ...]"""
        filas = []
        for k, (sec, campos) in enumerate(secciones):
            for i, (campo, valor) in enumerate(campos):
                fin = ' class="fin"' if (k == len(secciones) - 1 and i == len(campos) - 1) else ''
                celda_sec = f'<td class="sec" rowspan="{len(campos)}">{fmt(sec)}</td>' if i == 0 else ''
                filas.append(f'<tr{fin}>{celda_sec}<td class="campo">{fmt(campo)}</td><td>{fmt(valor)}</td></tr>')
        self.partes.append(
            f'<div class="capa"><div class="capa-tit">Selecciona en Capas: <b><code>{esc(nombre)}</code></b> <i>{fmt(donde)}</i></div>'
            '<table class="panel"><thead><tr><th>SECCIÓN DEL PANEL</th><th>CAMPO</th><th>VALOR</th></tr></thead>'
            f'<tbody>{"".join(filas)}</tbody></table></div>')

    # --- salida
    def guardar(self, ruta_html):
        self._cerrar()
        import shutil
        destino = os.path.dirname(os.path.abspath(ruta_html))
        os.makedirs(destino, exist_ok=True)
        shutil.copytree(os.path.join(AQUI, 'assets'), os.path.join(destino, 'assets'), dirs_exist_ok=True)
        doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
               f'<title>{esc(self.titulo)}</title><style>{CSS}</style></head><body>'
               + '\n'.join(self.partes) + '</body></html>')
        with open(ruta_html, 'w', encoding='utf8') as f:
            f.write(doc)
        with open(ruta_html + '.pie', 'w', encoding='utf8') as f:
            f.write(self.titulo_corto)
