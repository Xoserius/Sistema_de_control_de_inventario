import os
import sqlite3
import uuid
from datetime import datetime
from fpdf import FPDF

class ReportGenerator:
    def __init__(self):
        self.pdf = FPDF('P', 'mm', 'A4')
        self.pdf.add_page()
        self.pdf.set_font('Times', 'B', 10)

    def generate_report(self):
        # Obtener la fecha y hora actual
        # Crear el objeto PDF
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Times', 'B', 10) 

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

        # Título del reporte
        
        titulo_reporte = f"REPORTE DE PRODUCTOS - {fecha_actual}"
        pdf.set_font('times', 'B', 16)  # Cambia el tamaño de la fuente aquí
        pdf.cell(190, 10, titulo_reporte, 0, 1, "C")
        pdf.set_font('Times', 'B', 10)

        # Posicionamiento de la imagen en la parte superior del medio
        pdf.image("image.png", x=80, y=1, w=50)  # Ajusta las coordenadas y el tamaño de acuerdo a tu imagen

        # Encabezado de la tabla
        encabezados = ["SKU", "CÓDIGO DE BARRAS", "DESCRIPCIÓN", "PRECIO", "CANTIDAD", "CONTADOS"]
        ancho_celdas = [30, 45, 31, 30, 30, 25]  # Ancho personalizado de las celdas
        for i, encabezado in enumerate(encabezados):
            pdf.cell(ancho_celdas[i], 10, encabezado, 1, 0, "C")  # Ajustar el ancho de las celdas
        pdf.ln()

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
        pdf.image("image2.png", x=55, y=100, w=100)

        # Guardar el PDF
        pdf.output(name=ruta_reporte, dest='F')


if __name__ == "__main__":
    report_generator = ReportGenerator()
    ruta_reporte = report_generator.generate_report()

    # Mostrar mensaje exitoso
    print(f"El reporte se ha generado exitosamente como '{ruta_reporte}'")
