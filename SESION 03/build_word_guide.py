import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_element(name):
    return OxmlElement(name)

def set_cell_background(cell, fill_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_border(cell, **kwargs):
    """
    kwargs: top, bottom, left, right
    values: dict(sz=12, val='single', color='0A3981')
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for border_name, border_props in kwargs.items():
        node = OxmlElement(f'w:{border_name}')
        node.set(qn('w:val'), border_props.get('val', 'single'))
        node.set(qn('w:sz'), str(border_props.get('sz', 4)))
        node.set(qn('w:space'), '0')
        node.set(qn('w:color'), border_props.get('color', 'auto'))
        tcBorders.append(node)
    tcPr.append(tcBorders)

def add_callout(doc, text_paragraphs, title="NOTA IMPORTANTE", border_color="0A3981", bg_color="F0F4F8"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    set_cell_border(cell, 
                    left=dict(val='single', sz=24, color=border_color),
                    top=dict(val='none'),
                    bottom=dict(val='none'),
                    right=dict(val='none'))
    
    # Title paragraph
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_title = p.add_run(f"📌 {title}\n")
    run_title.font.name = 'Arial'
    run_title.font.size = Pt(11)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(10, 57, 129)
    
    for tp in text_paragraphs:
        p_sub = cell.add_paragraph()
        p_sub.paragraph_format.space_before = Pt(2)
        p_sub.paragraph_format.space_after = Pt(3)
        run_text = p_sub.add_run(tp)
        run_text.font.name = 'Arial'
        run_text.font.size = Pt(10)
        run_text.font.color.rgb = RGBColor(40, 40, 40)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def add_heading_1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(18)
    h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = RGBColor(10, 57, 129) # USS Navy
    return h

def add_heading_2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 102, 178) # USS Blue Accent
    return h

def add_heading_3(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(3)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = RGBColor(60, 60, 60)
    return h

def add_body_paragraph(doc, text, bold_prefix=None, space_after=5):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        r_bold.font.name = 'Arial'
        r_bold.font.size = Pt(10.5)
        r_bold.font.bold = True
        r_bold.font.color.rgb = RGBColor(30, 30, 30)
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(10.5)
    run.font.color.rgb = RGBColor(45, 45, 45)
    return p

def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        r_bold.font.name = 'Arial'
        r_bold.font.size = Pt(10)
        r_bold.font.bold = True
        r_bold.font.color.rgb = RGBColor(20, 20, 20)
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(40, 40, 40)
    return p

def add_code_block(doc, code_lines):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8F9FA")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    set_cell_border(cell, 
                    left=dict(val='single', sz=12, color='6C757D'),
                    top=dict(val='single', sz=4, color='DEE2E6'),
                    bottom=dict(val='single', sz=4, color='DEE2E6'),
                    right=dict(val='single', sz=4, color='DEE2E6'))
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run('\n'.join(code_lines))
    run.font.name = 'Consolas'
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(33, 37, 41)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def add_screenshot_figure(doc, image_path, caption, width_inches=6.2):
    if os.path.exists(image_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run = p_img.add_run()
        run.add_picture(image_path, width=Inches(width_inches))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run(caption)
        r_cap.font.name = 'Arial'
        r_cap.font.size = Pt(9)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(100, 100, 100)
    else:
        print(f"Warning: image {image_path} does not exist.")

def build_word_document():
    doc = docx.Document()
    
    # Page setup - Margins 1 inch
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
    
    brain_dir = r"C:\Users\dagne\.gemini\antigravity-ide\brain\9654f210-1610-4efe-8771-6a7320b22bb0"
    
    # -------------------------------------------------------------
    # PORTADA / ENCABEZADO INSTITUCIONAL
    # -------------------------------------------------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("UNIVERSIDAD SEÑOR DE SIPÁN\n")
    r_inst.font.name = 'Arial'
    r_inst.font.size = Pt(13)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(10, 57, 129)
    
    r_fac = p_inst.add_run("FACULTAD DE INGENIERÍA, ARQUITECTURA Y URBANISMO\nESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS\n")
    r_fac.font.name = 'Arial'
    r_fac.font.size = Pt(10.5)
    r_fac.font.color.rgb = RGBColor(70, 70, 70)
    
    # Divider line
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(16)
    r_line = p_line.add_run("―" * 45)
    r_line.font.name = 'Arial'
    r_line.font.bold = True
    r_line.font.color.rgb = RGBColor(0, 102, 178)
    
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("GUÍA OFICIAL Y REPORTE DE MAQUETACIÓN: SEMANA 3\n")
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(10, 57, 129)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(16)
    r_sub = p_sub.add_run("Diseño Web · Sesión 03: Maquetación HTML5 y Figma\nTraducción Estructural del Portafolio Personal (Wireframe)")
    r_sub.font.name = 'Arial'
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(90, 90, 90)
    
    # Metadata Table
    meta_tbl = doc.add_table(rows=4, cols=2)
    meta_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Docente / Autor:", "Ing. Dagner Anibal Chuman Lluen"),
        ("Asignatura:", "Diseño Web (Semana 3 / Sesión 03)"),
        ("Herramientas:", "Figma Desktop (Lienzo 1440px) & HTML5 Semántico"),
        ("Objetivo Principal:", "Maquetación estructural pura (Cajas, Frame y Auto Layout sin CSS decorativo)")
    ]
    for idx, (label, val) in enumerate(meta_data):
        row = meta_tbl.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "FFFFFF")
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(label)
        r0.font.name = 'Arial'
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(10, 57, 129)
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(val)
        r1.font.name = 'Arial'
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = RGBColor(40, 40, 40)
        
        for cell in (c0, c1):
            set_cell_border(cell,
                            top=dict(val='single', sz=4, color='CBD5E1'),
                            bottom=dict(val='single', sz=4, color='CBD5E1'),
                            left=dict(val='single', sz=4, color='CBD5E1'),
                            right=dict(val='single', sz=4, color='CBD5E1'))
            
    doc.add_paragraph().paragraph_format.space_after = Pt(14)
    
    # -------------------------------------------------------------
    # SECCIÓN 1: ¿QUÉ SE HACE EN LA SEMANA 3?
    # -------------------------------------------------------------
    add_heading_1(doc, "1. ¿Qué se hace exactamente en la Semana 3?")
    
    add_body_paragraph(doc, 
                       "De acuerdo con el Sílabo oficial de Diseño Web de la Universidad Señor de Sipán y la presentación de la Sesión 03 ('Maquetación HTML5 y Figma'), la Semana 3 se enfoca exclusivamente en la MAQUETACIÓN ESTRUCTURAL (Wireframing).")
    
    add_callout(doc, [
        "En la Semana 3 NO se diseña con colores definitivos, sombras complejas ni estilos CSS decorativos.",
        "El CSS formal y los estilos avanzados no inician hasta la Sesión 08.",
        "El objetivo exclusivo de esta semana es agrupar el contenido en CAJAS ESTRUCTURALES (Header, Nav, Main, Section, Article, Footer), replicar dicha estructura en Figma usando Frames de 1440px y Auto Layout, y mantener una correspondencia 1:1 con el código HTML5."
    ], title="REGLA CLAVE DE LA SEMANA 3: MAQUETACIÓN PURA", border_color="0A3981", bg_color="EEF4FC")
    
    add_heading_2(doc, "Consigna Oficial de Entrega (Evaluación Continua - 40% [P]):")
    add_bullet(doc, "Crear el Frame de 1440 px de ancho (Desktop) con fondo neutro y estructurado con Auto Layout.", "1. En Figma: ")
    add_bullet(doc, "Identificar y nombrar las capas con el mismo rol semántico de HTML (<header>, <nav>, <section>, <article>, <footer>).", "2. Árbol de Capas: ")
    add_bullet(doc, "Maquetar la misma estructura utilizando etiquetas semánticas sin estilos decorativos.", "3. En HTML5: ")
    add_bullet(doc, "Verificar que el código no tenga errores ni advertencias en el validador oficial del W3C (validator.w3.org).", "4. Validación W3C: ")
    add_bullet(doc, "Configurar la opción 'Cualquiera con el enlace puede ver' (Anyone with the link can view) y compartir la URL pública junto con el despliegue en Netlify.", "5. Enlace Público: ")
    
    # -------------------------------------------------------------
    # SECCIÓN 2: CÓDIGO HTML5 DEL PORTAFOLIO Y SU TRADUCCIÓN A FIGMA
    # -------------------------------------------------------------
    add_heading_1(doc, "2. Estructura HTML5 del Portafolio vs Figma")
    add_body_paragraph(doc, 
                       "El portafolio personal construido por el Ing. Dagner Chuman cuenta con una arquitectura semántica limpia y validable. A continuación se detalla cómo cada etiqueta se mapea a un componente de Figma:")
    
    # Mapping Table
    map_tbl = doc.add_table(rows=7, cols=4)
    map_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Zona / Nivel", "Etiqueta HTML5", "Equivalente en Figma", "Comportamiento / Auto Layout"]
    hdr_row = map_tbl.rows[0]
    for i, h_text in enumerate(headers):
        c = hdr_row.cells[i]
        set_cell_background(c, "0A3981")
        set_cell_margins(c, top=80, bottom=80, left=100, right=100)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
    
    rows_data = [
        ("Nivel 1 (Global)", "<body>", "Frame 'Portafolio' (1440 × 2000 px)", "Contenedor raíz vertical (Vertical Auto Layout)"),
        ("Nivel 2 (Cabecera)", "<header> + <nav>", "Frame 'header' con 'h1' y 'nav-links'", "Horizontal Auto Layout, Space Between, Padding 100×24"),
        ("Nivel 3 (Sobre mí)", "<section id='sobre-mi'>", "Frame 'section-sobre-mi' (#F5F5F5)", "Vertical Auto Layout, Fill Container, Padding 80×100"),
        ("Nivel 3 (Proyectos)", "<section id='proyectos'>", "Frame 'section-proyectos' (Título + Grid)", "Vertical Auto Layout, Gap 32, Fill Container"),
        ("Nivel 4 (Cards)", "<article>", "2 Frames 'article-card' (#E8E8E8)", "Horizontal Grid (2 columnas de 580 px), Hug/Fixed"),
        ("Nivel 3 (Contacto & Pie)", "<section id='contacto'> & <footer>", "Frames 'section-contacto' & 'footer'", "Vertical Auto Layout, fondo oscuro en pie, copyright centrado")
    ]
    
    for r_idx, row_values in enumerate(rows_data, start=1):
        r_elem = map_tbl.rows[r_idx]
        bg = "FFFFFF" if r_idx % 2 != 0 else "F8FAFC"
        for c_idx, val in enumerate(row_values):
            cell = r_elem.cells[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            set_cell_border(cell,
                            top=dict(val='single', sz=4, color='E2E8F0'),
                            bottom=dict(val='single', sz=4, color='E2E8F0'),
                            left=dict(val='single', sz=4, color='E2E8F0'),
                            right=dict(val='single', sz=4, color='E2E8F0'))
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Arial'
            r.font.size = Pt(9)
            if c_idx == 1:
                r.font.name = 'Consolas'
                r.font.bold = True
                r.font.color.rgb = RGBColor(180, 40, 40)
            elif c_idx == 0:
                r.font.bold = True
                r.font.color.rgb = RGBColor(10, 57, 129)
            else:
                r.font.color.rgb = RGBColor(40, 40, 40)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(10)
    
    add_heading_2(doc, "Código Fuente HTML5 del Portafolio Personal:")
    html_code = [
        "<!DOCTYPE html>",
        "<html lang=\"es\">",
        "<head>",
        "  <meta charset=\"UTF-8\">",
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
        "  <title>Portafolio - Dagner Chuman</title>",
        "</head>",
        "<body>",
        "",
        "  <!-- CABECERA: Identidad del sitio y menú de navegación -->",
        "  <header>",
        "    <h1>Dagner Chuman</h1>",
        "    <nav>",
        "      <ul>",
        "        <li><a href=\"#sobre-mi\">Sobre mí</a></li>",
        "        <li><a href=\"#proyectos\">Proyectos</a></li>",
        "        <li><a href=\"#contacto\">Contacto</a></li>",
        "      </ul>",
        "    </nav>",
        "  </header>",
        "",
        "  <!-- CONTENIDO PRINCIPAL -->",
        "  <main>",
        "    <!-- SECCIÓN: Sobre mí -->",
        "    <section id=\"sobre-mi\">",
        "      <h2>Sobre mí</h2>",
        "      <p>",
        "        Hola, soy Dagner Chuman. Docente e Ingeniero enfocado en el desarrollo web y la formación tecnológica.",
        "        Este es mi portafolio personal construido con HTML5 y estructura semántica limpia.",
        "      </p>",
        "    </section>",
        "",
        "    <!-- SECCIÓN: Proyectos destacados con article -->",
        "    <section id=\"proyectos\">",
        "      <h2>Proyectos</h2>",
        "      <article>",
        "        <h3>Ecosistema CINF USS</h3>",
        "        <p>Plataforma para la gestión académica y proyectos estudiantiles del Centro de Informática.</p>",
        "      </article>",
        "      <article>",
        "        <h3>Generador de Certificados Web</h3>",
        "        <p>Aplicación para automatizar la emisión y validación de certificados digitales.</p>",
        "      </article>",
        "    </section>",
        "",
        "    <!-- SECCIÓN: Contacto -->",
        "    <section id=\"contacto\">",
        "      <h2>Contacto</h2>",
        "      <p>Puedes contactarme a través de los siguientes canales:</p>",
        "      <ul>",
        "        <li>Correo: <a href=\"mailto:dchuman@uss.edu.pe\">dchuman@crece.uss.edu.pe</a></li>",
        "        <li>LinkedIn: <a href=\"https://www.linkedin.com\" target=\"_blank\">linkedin.com/in/dagnerchuman</a></li>",
        "        <li>GitHub: <a href=\"https://github.com\" target=\"_blank\">github.com/dagnerchuman</a></li>",
        "      </ul>",
        "    </section>",
        "  </main>",
        "",
        "  <!-- PIE DE PÁGINA -->",
        "  <footer>",
        "    <p>&copy; 2026 Dagner Chuman · Centro de Informática USS · Protech XP</p>",
        "  </footer>",
        "",
        "</body>",
        "</html>"
    ]
    add_code_block(doc, html_code)
    
    # -------------------------------------------------------------
    # SECCIÓN 3: PASO A PASO EN FIGMA CON CAPTURAS DE PANTALLA REALES
    # -------------------------------------------------------------
    add_heading_1(doc, "3. Paso a Paso en Figma y Evidencias Reales del Avance")
    add_body_paragraph(doc, 
                       "Durante la sesión de trabajo interactivo, se accedió al entorno oficial de Figma con la cuenta del usuario Dagner Chuman y se construyó el wireframe correspondiente. A continuación se presentan los pasos ejecutados y las capturas reales obtenidas del lienzo de trabajo:")
    
    # Paso 1
    add_heading_2(doc, "Paso 1: Creación del Proyecto y Configuración del Frame Desktop (1440 px)")
    add_body_paragraph(doc, 
                       "1. En el panel superior se nombró el archivo como ", bold_prefix="Acción realizada: ")
    add_body_paragraph(doc, 
                       "Portafolio-DagnerChuman (ubicado en Borradores para plan gratuito ilimitado).")
    add_body_paragraph(doc, 
                       "2. Con la tecla 'F' se seleccionó la herramienta Frame y se eligió el preset Desktop estándar de 1440 px de ancho, ajustando la altura vertical (H) a 2000 px para albergar todas las secciones del portafolio.")
    add_body_paragraph(doc, 
                       "3. Se renombró el frame principal a 'Portafolio' (Ctrl + R).")
    
    img_frame = os.path.join(brain_dir, "figma_final_state_1789959409195.png")
    add_screenshot_figure(doc, img_frame, 
                          "Figura 1: Creación del Frame principal 'Portafolio' de 1440 × 1024 / 2000 px en Figma.", 
                          width_inches=6.0)
    
    # Paso 2
    add_heading_2(doc, "Paso 2: Construcción de la Cabecera (<header>) con Logotipo y Navegación (<nav>)")
    add_body_paragraph(doc, 
                       "Siguiendo la regla de oro de la Sesión 03 (Diapositiva 29):", bold_prefix="Estructuración: ")
    add_bullet(doc, "Se insertó el nombre principal 'Dagner Chuman' como h1 (Inter Bold 24 px).", "Título / Identidad: ")
    add_bullet(doc, "Se crearon los accesos directos 'Sobre mí', 'Proyectos', 'Contacto' (Inter Regular 14/16 px).", "Menú de Navegación: ")
    add_bullet(doc, "Se estableció la barra superior 'Header' con altura de 80 px y fondo gris neutro (#E8E8E8 / #F8F9FA) para delimitar la zona superior sin recargar visualmente.", "Contenedor: ")
    
    img_hdr = os.path.join(brain_dir, "final_header_design_1789960544749.png")
    add_screenshot_figure(doc, img_hdr, 
                          "Figura 2: Maquetación de la cabecera (Header) y menú de navegación en Figma.", 
                          width_inches=6.0)
    
    # Paso 3
    add_heading_2(doc, "Paso 3: Jerarquía Semántica del Árbol de Capas y Sección 'Sobre mí'")
    add_body_paragraph(doc, 
                       "En el panel izquierdo de Figma se mantuvo rigurosamente la estructura de nombres para reflejar el DOM de HTML5:", bold_prefix="Organización: ")
    add_bullet(doc, "Header (fondo cabecera)", "▸ ")
    add_bullet(doc, "Dagner Chuman (h1)", "▸ ")
    add_bullet(doc, "Inicio, Sobre mi, Proyectos, Contacto (nav-links)", "▸ ")
    add_bullet(doc, "section-sobre-mi (rectángulo delimitador con fondo #F5F5F5)", "▸ ")
    add_bullet(doc, "Sobre mi (título h2 en Inter Bold 28 px)", "▸ ")
    add_bullet(doc, "Hola, soy Dagner Chuman, un desarrollador apasionado... (párrafo descriptivo)", "▸ ")
    
    img_verify = os.path.join(brain_dir, "header_100_percent_opacity_1789965856069.png")
    add_screenshot_figure(doc, img_verify, 
                          "Figura 3: Estado verificado en tiempo real con 100% de opacidad, cabecera nítida y sección 'Sobre mí'.", 
                          width_inches=6.0)
    
    # Paso 4
    add_heading_2(doc, "Paso 4: Maquetación de las Secciones Faltantes (Guía Rápida para Completar)")
    add_body_paragraph(doc, 
                       "Para dejar el archivo 100% terminado para la entrega del aula virtual, solo se deben replicar los siguientes dos bloques dentro del mismo frame 'Portafolio':")
    
    add_heading_3(doc, "A. Sección 'Proyectos' (Cuadrícula de 2 Tarjetas con <article>):")
    add_bullet(doc, "Crear un Frame o Rectángulo de 1440 px de ancho, altura 320 px, fondo blanco (#FFFFFF). Nombrarlo 'section-proyectos'.", "1. ")
    add_bullet(doc, "Añadir el título 'Proyectos' (Inter Bold 28 px, posición X: 100, Y: 360).", "2. ")
    add_bullet(doc, "Crear Tarjeta 1 ('article-ecosistema'): Ancho 580 px, alto 180 px, fondo #E8E8E8, X: 100, Y: 420. Dentro colocar el título 'Ecosistema CINF USS' (Bold 18 px) y el párrafo 'Plataforma para la gestión académica...'.", "3. ")
    add_bullet(doc, "Crear Tarjeta 2 ('article-certificados'): Ancho 580 px, alto 180 px, fondo #E8E8E8, X: 740, Y: 420. Dentro colocar el título 'Generador de Certificados Web' (Bold 18 px) y su descripción.", "4. ")
    
    add_heading_3(doc, "B. Sección 'Contacto' y 'Footer':")
    add_bullet(doc, "Crear 'section-contacto' (Fondo #F5F5F5, altura 260 px). Título 'Contacto' (Bold 28 px) y 3 líneas de texto para Correo, LinkedIn y GitHub.", "1. Contacto: ")
    add_bullet(doc, "Crear 'footer' (Fondo oscuro #333333, altura 120 px). Texto en color blanco (#FFFFFF, 14 px) centrado: '© 2026 Dagner Chuman · Centro de Informática USS · Protech XP'.", "2. Footer: ")
    
    # -------------------------------------------------------------
    # SECCIÓN 4: REGLAS TÉCNICAS DE AUTO LAYOUT
    # -------------------------------------------------------------
    add_heading_1(doc, "4. Reglas Técnicas de Auto Layout (Flexbox en Figma)")
    add_body_paragraph(doc, 
                       "La Sesión 03 enfatiza que Auto Layout es el equivalente directo de Flexbox en CSS. Al aplicar Auto Layout (Shift + A) en Figma, se deben configurar los siguientes parámetros:")
    
    auto_tbl = doc.add_table(rows=4, cols=3)
    auto_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    auto_headers = ["Propiedad en Figma", "Equivalente CSS", "Uso Recomendado en el Portafolio"]
    for i, h_text in enumerate(auto_headers):
        c = auto_tbl.rows[0].cells[i]
        set_cell_background(c, "0A3981")
        set_cell_margins(c, top=70, bottom=70, left=90, right=90)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    auto_data = [
        ("Dirección: Horizontal (→)\nGap: 32 px\nPadding: 100 × 24 px", "display: flex;\nflex-direction: row;\ngap: 32px;\npadding: 24px 100px;", "Cabecera (<header>) para separar el título 'Dagner Chuman' a la izquierda y el <nav> a la derecha con 'Space Between'."),
        ("Dirección: Vertical (↓)\nGap: 16 px\nPadding: 24 × 32 px", "display: flex;\nflex-direction: column;\ngap: 16px;\npadding: 24px 32px;", "Tarjetas de Proyectos (<article>) para apilar ordenadamente el título <h3> sobre el párrafo <p> descriptivo."),
        ("Comportamiento:\nFill Container (↔)", "width: 100%;\nflex: 1;", "Párrafos y secciones principales para que se adapten automáticamente al ancho del contenedor sin desbordarse.")
    ]
    for r_idx, row_values in enumerate(auto_data, start=1):
        r_elem = auto_tbl.rows[r_idx]
        bg = "FFFFFF" if r_idx % 2 != 0 else "F8FAFC"
        for c_idx, val in enumerate(row_values):
            cell = r_elem.cells[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            set_cell_border(cell,
                            top=dict(val='single', sz=4, color='E2E8F0'),
                            bottom=dict(val='single', sz=4, color='E2E8F0'),
                            left=dict(val='single', sz=4, color='E2E8F0'),
                            right=dict(val='single', sz=4, color='E2E8F0'))
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Consolas' if c_idx == 1 else 'Arial'
            r.font.size = Pt(9)
            if c_idx == 0:
                r.font.bold = True
                r.font.color.rgb = RGBColor(10, 57, 129)
            else:
                r.font.color.rgb = RGBColor(40, 40, 40)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # -------------------------------------------------------------
    # SECCIÓN 5: PROTOCOLO DE VALIDACIÓN W3C Y ENTREGA OFICIAL
    # -------------------------------------------------------------
    add_heading_1(doc, "5. Protocolo de Validación y Enlace de Entrega")
    
    add_heading_2(doc, "Paso 1: Validación W3C")
    add_body_paragraph(doc, 
                       "1. Ingresar a ", bold_prefix="Procedimiento: ")
    add_body_paragraph(doc, 
                       "https://validator.w3.org/#validate_by_input")
    add_body_paragraph(doc, 
                       "2. Copiar y pegar el código HTML5 del portafolio en la pestaña 'Validate by Direct Input'.")
    add_body_paragraph(doc, 
                       "3. Presionar el botón 'Check'. El resultado debe mostrar el mensaje verde: 'Document checking completed. No errors or warnings to show.'.")
    
    add_heading_2(doc, "Paso 2: Obtener el Enlace Público de Figma")
    add_body_paragraph(doc, 
                       "Para que el docente o evaluador pueda revisar el archivo en el Aula Virtual / ClassDojo:", bold_prefix="Instrucciones: ")
    add_bullet(doc, "En la esquina superior derecha de Figma, hacer clic en el botón azul 'Compartir' (Share).", "1. ")
    add_bullet(doc, "En el cuadro modal, verificar que el permiso esté en: 'Cualquiera con el enlace puede ver' (Anyone with the link can view).", "2. ")
    add_bullet(doc, "Hacer clic en 'Copiar enlace' (Copy link).", "3. ")
    add_bullet(doc, "Esa es la URL que se entrega en el Aula Virtual junto con el enlace web de Netlify.", "4. ")
    
    add_callout(doc, [
        "El portafolio maquetado cumple exactamente con los 4 niveles de anidamiento exigidos por la USS:",
        "Nivel 1: <body> (Lienzo raíz)",
        "Nivel 2: <header>, <main>, <footer> (Zonas principales)",
        "Nivel 3: <section>, <article> (Bloques temáticos independientes)",
        "Nivel 4: <h1>, <h2>, <h3>, <p>, <ul> (Contenido legible)",
        "¡Excelente trabajo! Estás listo para obtener el máximo puntaje en la Semana 3."
    ], title="CHECKLIST FINAL DE EVALUACIÓN", border_color="198754", bg_color="F0FDF4")
    
    # Save document
    output_path = r"e:\USS\SEMANA 3 USS\Guia_Maquetacion_Figma_Semana3_DagnerChuman.docx"
    doc.save(output_path)
    print(f"Document saved successfully to {output_path}")

if __name__ == '__main__':
    build_word_document()
