from fpdf import FPDF
import os
import sqlite3
from datetime import datetime
import uuid

def generar_reporte_productos_pdf():
    # Crear el objeto PDF
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Times', 'B', 10) 

    # Dejar espacio en blanco en la parte superior
    pdf.ln(100)

    # Obtener la fecha y hora actual
    now = datetime.now()
    fecha_actual = now.strftime("%d-%m-%y")
    hora_actual = now.strftime("%H:%M:%S")  # Formato 99:99:99

    # Carpeta de destino para los reportes
    carpeta_destino = "Reportes de inventario"
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Nombre único del archivo de reporte
    id_unico = str(uuid.uuid4())
    nombre_reporte = f"reporte_productos_{fecha_actual}_{id_unico}.pdf"
    ruta_reporte = os.path.join(carpeta_destino, nombre_reporte)

    # Posicionamiento de la imagen en la parte superior del medio
    pdf.image("image.png", x=80, y=10, w=50)  # Ajusta las coordenadas y el tamaño de acuerdo a tu imagen

    # Título del reporte
    titulo_reporte = f"REPORTE DE PRODUCTOS - {fecha_actual}"
    pdf.set_font('times', 'B', 16)  # Cambia el tamaño de la fuente aquí
    pdf.cell(0, 10, titulo_reporte, 0, 1, "C")
    pdf.ln()  # Agrega un salto de línea después del título

    # Encabezado de la tabla
    encabezados = ["SKU", "CÓDIGO DE BARRAS", "DESCRIPCIÓN", "PRECIO", "CANTIDAD", "CONTADOS"]
    ancho_celdas = [30, 45, 31, 30, 30, 25]  # Ancho personalizado de las celdas
    for i, encabezado in enumerate(encabezados):
        pdf.cell(ancho_celdas[i], 10, encabezado, 1, 0, "C")  # Ajustar el ancho de las celdas
    pdf.ln()  # Agrega un salto de línea después del encabezado

    # Realizar la consulta a la base de datos SQLite
    conn = sqlite3.connect('Base de datos proyecto.db')
    c = conn.cursor()
    c.execute('''SELECT sku, codigo_barras, descripcion, precio, cantidad
                FROM Productos''')
    resultados = c.fetchall()

    # Agregar los resultados al PDF
    for resultado in resultados:
        for i, dato in enumerate(resultado):
            pdf.cell(ancho_celdas[i], 10, str(dato), 1, 0, "C")  # Ajustar el ancho de las celdas
        pdf.cell(ancho_celdas[-1], 10, '', 1, 0, "C")  # Celda en blanco para "CONTADOS"
        pdf.ln()

    # Mostrar la fecha en la esquina superior izquierda
    pdf.set_xy(10, 10)
    pdf.cell(0, 0, fecha_actual, 0, 1, "L")

    # Mostrar la hora en la esquina superior derecha
    pdf.set_xy(-40, 10)
    pdf.cell(0, 0, hora_actual, 0, 1, "R")

    # Marca de agua como imagen
        

    # Guardar el PDF
    pdf.output(name=ruta_reporte, dest='F')

    # Mostrar mensaje exitoso
    print(f"El reporte se ha generado exitosamente como '{nombre_reporte}'")

    # Abrir el PDF automáticamente
    os.startfile(ruta_reporte)

if __name__ == "__main__":
    generar_reporte_productos_pdf()
