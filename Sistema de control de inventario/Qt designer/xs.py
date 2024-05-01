from fpdf import FPDF
import sqlite3

def generar_reporte_productos():
    # Crear el objeto PDF
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Times', 'B', 12)

    # Título del reporte
    pdf.cell(190, 10, "REPORTE DE PRODUCTOS", 10, 1, "C")

    # Encabezado de la tabla
    encabezados = ["SKU", "CÓDIGO DE BARRAS", "DESCRIPCIÓN", "PRECIO", "CANTIDAD"]
    for encabezado in encabezados:
        pdf.cell(40, 10, encabezado, 1, 0, "C")
    pdf.ln()

    # Realizar la consulta a la base de datos SQLite
    conn = sqlite3.connect('Base de datos proyecto.db')
    c = conn.cursor()
    c.execute('''SELECT sku, codigo_barras, descripcion, precio, cantidad
                 FROM Productos''')
    resultados = c.fetchall()

    # Agregar los resultados al PDF
    for resultado in resultados:
        for dato in resultado:
            pdf.cell(40, 10, str(dato), 1, 0, "C")
        pdf.ln()

    # Guardar el PDF
    pdf.output(name="reporte_productos.pdf", dest='F')

# Llamar a la función para generar el reporte
generar_reporte_productos()