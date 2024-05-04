import os
import re
import sqlite3
import sys
import uuid

from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5.uic import loadUi
from fpdf import FPDF



class Ui_Qdialog_login(QDialog):
    # Clase creada para la ventana de Login 
    def __init__(self):
        super().__init__()
        loadUi("2.Login.ui", self)
        # Carga la interfaz de usuario desde el archivo
        self.establecer_icono()

        self.conexion_db = sqlite3.connect("Base de datos proyecto.db")  # Establecer la conexión a la base de datos

        self.pushButton_aceptar.clicked.connect(self.iniciar_sesion)
        self.pushButton_salir.clicked.connect(self.salir)

    def iniciar_sesion(self):
        usuario = self.lineEdit_usuario.text()
        clave = self.lineEdit_clave.text()

        if not usuario and not clave:
            QMessageBox.warning(self, "Campos requeridos", "Por favor, ingrese su usuario y clave.")
            return
        elif not usuario:
            QMessageBox.warning(self, "Campo requerido", "Por favor, ingrese su usuario.")
            return
        elif not clave:
            QMessageBox.warning(self, "Campo requerido", "Por favor, ingrese su clave.")
            return

        try:
            cursor = self.conexion_db.cursor()
            consulta = "SELECT * FROM usuarios WHERE usuario = ? AND clave = ?"
            cursor.execute(consulta, (usuario, clave))
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                self.close()
                self.abrir_menu_principal()
            else:
                QMessageBox.critical(self, "Acceso denegado", "Usuario o clave inválida.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error al intentar iniciar sesión: {str(e)}")

    def abrir_menu_principal(self):
        # Método para abrir el menu principal
        self.conexion_db.close()
        self.close()  # Ocultar la ventana de inicio de sesión
        self.menu_principal = Ui_QMainwindow_Menu_principal()
        self.menu_principal.showFullScreen()

    def salir(self):
        self.conexion_db.close()
        self.close()
        # Cierra la ventana actual.

    def establecer_icono(self):
        icono = QIcon("user.ico")  # Ruta al archivo de ícono
        self.setWindowIcon(icono)

class Ui_QMainwindow_Menu_principal(QMainWindow): 
    #clase creada para la ventana de menu principal

    def __init__(self):
        super().__init__() 
        loadUi("3.Menu_principal.ui", self)
        # Carga la interfaz de usuario desde el archivo

        self.label.setPixmap(QPixmap("LOGO_POTRO.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setScaledContents(True)

        # Conectar botones a funciones
        self.pushButton_salir_menu.clicked.connect(self.salir)
        self.pushButton_gestiondeusuario.clicked.connect(self.abrir_ventana_gestion)
        self.pushButton_Inventario.clicked.connect(self.abrir_ventana_inventario)
        self.pushButton_reportes.clicked.connect(self.abrir_reportes)
        
        self.pushButton_productos.clicked.connect(self.abrir_Productos)
      

        # Instanciar ventanas
        self.ventana_gestionusu = Ui_QMainwindow_Gestion_de_usuarios(QMainWindow)
        self.ventana_report = Ui_QMainwindow_Reportes(QMainWindow)
        self.ventana_producto = ui_QMainWindow_productos(QMainWindow)
        self.ventana_inventario = ui_QMainWindow_inventario(QMainWindow)
       

    def abrir_ventana_gestion(self):
        # metodo para mostrar la ventana de gestion de usuarios
        self.ventana_gestionusu = Ui_QMainwindow_Gestion_de_usuarios(self.ventana_gestionusu)
        # Instanciar ventana
        self.ventana_gestionusu.showFullScreen()
        # Mostrar ventana en pantalla completa

    def abrir_reportes (self):
        # Mostrar la ventana de Reportes
        self.ventana_report = Ui_QMainwindow_Reportes(self.ventana_report)
        # Instanciar ventana
        self.ventana_report.showFullScreen()
        # Mostrar ventana en pantalla completa

    def abrir_Productos (self):# Mostrar la ventana de añadir/eliminar
        self.ventana_producto = ui_QMainWindow_productos(self.ventana_producto)
        # Instanciar ventana
        self.ventana_producto.showFullScreen()
        # Mostrar ventana en pantalla completa    

    def abrir_ventana_inventario (self):

        self.ventana_inventario = ui_QMainWindow_inventario(self.ventana_inventario)
        # Instanciar ventana
        self.ventana_inventario.showFullScreen()
        # Mostrar ventana en pantalla completa 

    def salir(self):
        self.close()
        # Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.      

class Ui_QMainwindow_Gestion_de_usuarios(QMainWindow): 
    def __init__(self, ventana_gestiondeusu):
        super().__init__()
        loadUi("4.Gestion_de_usuarios.ui", self)
        # Carga la interfaz de usuario desde el archivo

        # Crear una instancia de la ventana de gestion de usuarios
        self.ventana_gestiondeusu = ventana_gestiondeusu

        # Configurar la tabla como de solo lectura
        self.tableWidget_usuarios.setEditTriggers(QTableWidget.NoEditTriggers)

        # Conexiones de los botones a sus respectivos métodos.
        self.pushButton_regresar_gestion.clicked.connect(self.salir)

        self.pushButton_usuarios.clicked.connect(self.mostrar_pagina_usuarios)
        self.pushButton_anadir.clicked.connect(self.mostrar_pagina_anadir)
        self.pushButton_eliminar.clicked.connect(self.mostrar_pagina_eliminar)
        self.pushButton_actualizar.clicked.connect(self.mostrar_pagina_actualizar)

        self.pushButton_limpiar_registrodeusuario.clicked.connect(self.limpiar_registro)
        self.pushButton_guardar_registrodeusuario.clicked.connect(self.guardar_registro)

        self.pushButton_buscar_usu.clicked.connect(self.buscar_actualizar)
        self.pushButton_actualizarusuarios.clicked.connect(self.actualizar)

        self.pushButton_eliminar_eliminar.clicked.connect(self.eliminar_eliminar)
        self.pushButton_buscar_eliminar.clicked.connect(self.buscar_eliminar)

        self.pushButton_buscar_anadir_usu.clicked.connect(self.buscar_anadir)

        self.pushButton_refrescar.clicked.connect(self.refrescar)


    # Métodos para mostrar las páginas
    def mostrar_pagina_usuarios(self):
        self.stackedWidget.setCurrentIndex(0)

    def mostrar_pagina_actualizar(self):
        self.stackedWidget.setCurrentIndex(1)

    def mostrar_pagina_eliminar(self):
        self.stackedWidget.setCurrentIndex(2)

    def mostrar_pagina_anadir(self):
        self.stackedWidget.setCurrentIndex(3)

    def limpiar_registro(self):
        self.lineEdit_nombre_registrodeusuario.clear()
        self.lineEdit_cedula_registrodeusuario.clear()
        self.lineEdit_telefono_registrodeusuario.clear()
        self.lineEdit_apellido_registrodeusuario.clear()
        self.lineEdit_usuario_registrodeusuario.clear()
        self.lineEdit_clave_registrodeusuario.clear() 
        #Limpia todos los campos del formulario de registro de usuario. 

    def buscar_anadir(self):
        cedula = self.lineEdit_cedula_registrodeusuario.text().strip()  

        if not cedula:
            # Verifica si el campo de cédula está vacío y muestra un mensaje de error
            QMessageBox.warning(self, "Campo requerido", "Por favor ingrese la cédula que desea buscar")
            return

        # Conexion con la base datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        try:
            # Realiza la consulta en la base de datos buscando por cédula
            cursor.execute("SELECT nombre, apellido, telefono, usuario, clave, permiso FROM usuarios WHERE cedula = ?", (cedula,))
            usuario = cursor.fetchone()

            if usuario:
                QMessageBox.warning(self, "Usuario existente", "Este Usuario ya se encuentra registrado.")
                # Si encuentra el usuario, carga los datos en los Campos correspondientes
                self.lineEdit_nombre_registrodeusuario.setText(usuario[0])
                self.lineEdit_apellido_registrodeusuario.setText(usuario[1])
                self.lineEdit_telefono_registrodeusuario.setText(usuario[2])
                self.lineEdit_usuario_registrodeusuario.setText(usuario[3])
                self.lineEdit_clave_registrodeusuario.setText(usuario[4])
                self.comboBox_permiso.setCurrentText(usuario[5])
            else:
                # Si no encuentra el usuario, muestra un mensaje de error
                QMessageBox.warning(self, "No encontrado", "Esta cédula no se encuentra registrada")

        except Exception as e:
            # Capturar cualquier otro tipo de excepción genérica.
            QMessageBox.critical(self, "Error", f"Error al buscar en la base de datos: {str(e)}")
        finally:
            # Cierra el cursor y la conexión a la base de datos
            cursor.close()
            conexion.close()

    def guardar_registro(self):
        cedula = self.lineEdit_cedula_registrodeusuario.text()
        nombre = self.lineEdit_nombre_registrodeusuario.text()
        apellido = self.lineEdit_apellido_registrodeusuario.text()
        telefono = self.lineEdit_telefono_registrodeusuario.text()
        usuario = self.lineEdit_usuario_registrodeusuario.text()
        clave = self.lineEdit_clave_registrodeusuario.text()
        permiso = self.comboBox_permiso.currentText()
        #Recopila los datos ingresados en los campos del formulario de registro de usuario. 

        campos_vacios = []
        if not cedula: campos_vacios.append("cédula")
        if not nombre: campos_vacios.append("nombre")
        if not apellido: campos_vacios.append("apellido")
        if not telefono: campos_vacios.append("teléfono")
        if not usuario: campos_vacios.append("usuario")
        if not clave: campos_vacios.append("clave")
        if not permiso: campos_vacios.append("permiso")
        # Comprobación de cada campo para verificar si está vacío. Si lo está, se añade a la lista `campos_vacios`.

        if campos_vacios:
            QMessageBox.critical(self, "Campos vacíos", "Por favor, ingrese " + ", ".join(campos_vacios) + ".")
            return
        # Se muestra un mensaje crítico con los nombres de los campos que están vacíos.

        try:
            # Conectar a la base de datos SQLite.
            conexion = sqlite3.connect("Base de datos proyecto.db")
            # Crear un cursor para ejecutar comandos SQL.
            cursor = conexion.cursor()
            
            # Consultar si el número de teléfono ya está asociado a otro usuario.
            cursor.execute("SELECT * FROM usuarios WHERE telefono = ?", (telefono,))
            if cursor.fetchone():
                QMessageBox.critical(self, "Error de duplicidad", "El número de teléfono ingresado ya está asociado a otro usuario.")
                return
            
            # Ejecutar un comando SQL para insertar datos en la tabla 'usuarios'.
            cursor.execute("INSERT INTO usuarios (cedula, nombre, apellido, telefono, usuario, clave, permiso) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (cedula, nombre, apellido, telefono, usuario, clave, permiso))
            # Confirmar la transacción para asegurar que los datos se guarden de forma permanente.
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Datos guardados correctamente.")
            # Mensaje al usuario que los datos han sido Guardados correctamente.
            self.lineEdit_cedula_registrodeusuario.clear()
            self.lineEdit_nombre_registrodeusuario.clear()
            self.lineEdit_apellido_registrodeusuario.clear()
            self.lineEdit_telefono_registrodeusuario.clear()
            self.lineEdit_usuario_registrodeusuario.clear()
            self.lineEdit_clave_registrodeusuario.clear()

        # Manejar errores específicos de operaciones con la base de datos, como una base de datos bloqueada.
        except sqlite3.OperationalError as e:
            if str(e) == "database is locked":
                QMessageBox.critical(self, "Error de base de datos", "La base de datos está bloqueada. Por favor, inténtelo de nuevo más tarde.")
            else:
                QMessageBox.critical(self, "Error de base de datos", f"Error desconocido: {str(e)}")

        # Manejar errores de integridad.
        except sqlite3.IntegrityError as e:
            if "usuarios.cedula" in str(e):
                QMessageBox.critical(self, "Error de duplicidad", "La cédula ingresada ya existe. Por favor ingrese una cédula diferente.")
            elif "usuarios.usuario" in str(e):
                QMessageBox.critical(self, "Error de duplicidad", "El nombre de usuario ingresado ya existe. Por favor elija otro nombre de usuario.")
        
        # Capturar cualquier otro tipo de excepción genérica. 
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error al guardar los datos: {str(e)}")
        
        # Asegurarse de cerrar la conexión a la base de datos y el cursor, independientemente del resultado de las operaciones anteriores.
        finally:
            if conexion:
                cursor.close()
                conexion.close()                

    def buscar_actualizar(self):
        cedula = self.lineEdit_cedulabuscar_actualizarusuarios.text().strip()  

        if not cedula:
            # Verifica si el campo de cédula está vacío y muestra un mensaje de error
            QMessageBox.warning(self, "Campo requerido", "Por favor ingrese la cédula que desea buscar")
            return

        # Conexion con la base datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        try:
            # Realiza la consulta en la base de datos buscando por cédula
            cursor.execute("SELECT nombre, apellido, telefono, usuario, clave, permiso FROM usuarios WHERE cedula = ?", (cedula,))
            usuario = cursor.fetchone()

            if usuario:
                # Si encuentra el usuario, carga los datos en los Campos correspondientes
                self.lineEdit_nombre_actualizarusuarios.setText(usuario[0])
                self.lineEdit_apellido_actualizarusuarios.setText(usuario[1])
                self.lineEdit_telefono_actualizarusuarios.setText(usuario[2])
                self.lineEdit_usuario_actualizarusuarios.setText(usuario[3])
                self.lineEdit_clave_actualizarusuarios.setText(usuario[4])
                self.comboBox_permiso_actualizarusuarios.setCurrentText(usuario[5])
            else:
                # Si no encuentra el usuario, muestra un mensaje de error
                QMessageBox.warning(self, "No encontrado", "Esta cédula no se encuentra registrada")

        except Exception as e:
            # Capturar cualquier otro tipo de excepción genérica.
            QMessageBox.critical(self, "Error", f"Error al buscar en la base de datos: {str(e)}")
        finally:
            # Cierra el cursor y la conexión a la base de datos
            cursor.close()
            conexion.close()

    def actualizar (self):
        
        # Crea un diccionario llamado 'campos' que almacena los valores ingresados en los campos de la interfaz.
        campos = {
            
            # Obtiene los datos ingresados.
            "cedula": self.lineEdit_cedulabuscar_actualizarusuarios.text().strip(),
            "nombre": self.lineEdit_nombre_actualizarusuarios.text().strip(),
            "apellido": self.lineEdit_apellido_actualizarusuarios.text().strip(),
            "telefono": self.lineEdit_telefono_actualizarusuarios.text().strip(),
            "usuario": self.lineEdit_usuario_actualizarusuarios.text().strip(),
            "clave": self.lineEdit_clave_actualizarusuarios.text().strip(),
            "permiso": self.comboBox_permiso_actualizarusuarios.currentText()
        }

        if "" in campos.values():
            # Verifica si algún campo está vacío y muestra un mensaje de error indicando cuál campo esta vacio.
            campo_vacio = [k for k, v in campos.items() if not v][0]
            QMessageBox.warning(self, "Campo requerido", f"Por favor, complete el campo {campo_vacio}.")
            return

        # Conexion con la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        try:
            # Verifica si el usuario existe en la base de datos.
            cursor.execute("SELECT * FROM usuarios WHERE cedula = ?", (campos["cedula"],))
            usuario_actual = cursor.fetchone()

            if usuario_actual:
                # Compara los datos actuales con los de la base de datos para detectar cambios.
                datos_sin_cambios = all([
                    campos["nombre"] == usuario_actual[1],
                    campos["apellido"] == usuario_actual[2],
                    campos["telefono"] == usuario_actual[3],
                    campos["usuario"] == usuario_actual[4],
                    campos["clave"] == usuario_actual[5],
                    campos["permiso"] == usuario_actual[6]
                ])

                if datos_sin_cambios:
                    # Si no hay cambios, muestra un mensaje de advertencia
                    QMessageBox.warning(self, "Datos sin cambios", "Los datos son los mismos ya guardados, por favor revisar.")
                else:
                    # Si hay cambios, actualiza la información en la base de datos
                    cursor.execute("""
                        UPDATE usuarios SET nombre = ?, apellido = ?, telefono = ?, usuario = ?, clave = ?, permiso = ?
                        WHERE cedula = ?
                    """, (campos["nombre"], campos["apellido"], campos["telefono"], campos["usuario"], campos["clave"], campos["permiso"], campos["cedula"]))
                    conexion.commit()
                    QMessageBox.information(self, "Actualización exitosa", "Datos actualizados satisfactoriamente")

            else:
                QMessageBox.warning(self, "Usuario no encontrado", "No se encontró un usuario con esa cédula para actualizar.")

        except Exception as e:
            # Capturar cualquier otro tipo de excepción genérica.
            QMessageBox.critical(self, "Error de actualización", f"Error al actualizar los datos: {str(e)}")
        finally:
            # Cierra el cursor y la conexión a la base de datos
            cursor.close()  
            conexion.close()
            
            # Limpia los campos despues de Actualizar la base de datos.
            self.lineEdit_cedulabuscar_actualizarusuarios.clear()
            self.lineEdit_nombre_actualizarusuarios.clear()
            self.lineEdit_apellido_actualizarusuarios.clear()
            self.lineEdit_telefono_actualizarusuarios.clear()
            self.lineEdit_usuario_actualizarusuarios.clear()
            self.lineEdit_clave_actualizarusuarios.clear() 

    def buscar_eliminar(self):
        
        # Captura la cedula ingresada
        cedula = self.lineEdit_cedulabuscar_eliminar.text().strip()

        # Verifica si el campo de cédula está vacío y muestra un mensaje de error si es así.
        if not cedula:
            QMessageBox.warning(self, "Campo requerido", "Por favor ingrese la cédula")
            return # Termina la ejecución de la función si no hay cédula
        
        # Establece una conexión con la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        # Ejecuta una consulta SQL para buscar un usuario por su cédula
        cursor.execute("SELECT cedula, nombre, apellido, telefono, usuario, clave, permiso FROM usuarios WHERE cedula = ?", (cedula,))
        resultado = cursor.fetchall()

        # Mensaje de error si no se encontro ningun usuario.
        if not resultado:
            QMessageBox.warning(self, "No encontrado", "Esta cédula no se encuentra registrada")

        else: # Si se encontraron resultados de la consulta, procede a llenar el tableWidget
            self.tableWidget_eliminar.setRowCount(0)
            # Limpia todas las filas existentes antes de agregar nuevas
            for row_number, row_data in enumerate(resultado):
                # Añadir una nueva fila en el tableWidget
                self.tableWidget_eliminar.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    # Convertir los datos a cadena y asignarlos a la celda correspondiente
                    self.tableWidget_eliminar.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()
        
    def eliminar_eliminar(self):
        
        # Captura la cedula ingresada
        cedula = self.lineEdit_cedulabuscar_eliminar.text().strip()

        # Verifica si el campo de cédula está vacío antes de intentar eliminar
        if not cedula:
            QMessageBox.warning(self, "Campo requerido", "Por favor ingrese la cédula")
            return # Termina la ejecución si no hay cédula ingresada

        # Conexión a la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        # Ejecuta la consulta SQL para buscar al usuario con la cédula especificada
        cursor.execute("SELECT * FROM usuarios WHERE cedula = ?", (cedula,))

        
        # Verificar si se encontró un usuario con la cédula especificada
        if not cursor.fetchone():
        # Mensaje de error si no se encontró ningún usuario.
            QMessageBox.warning(self, "No encontrado", "Esta cédula no se encuentra registrada")
        else:
            # Confirmar la eliminación con un cuadro de diálogo
            respuesta = QMessageBox.question(self, "Confirmar eliminación", "¿Está seguro de que desea eliminar este usuario?",
                                    QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                # Ejecutar la consulta SQL para eliminar al usuario con la cédula especificada
                cursor.execute("DELETE FROM usuarios WHERE cedula = ?", (cedula,))
                conexion.commit()
                # Mensaje para mostrar que el usuario ha sido eliminado.
                QMessageBox.information(self, "Eliminado", "El usuario ha sido eliminado satisfactoriamente")
                self.tableWidget_eliminar.setRowCount(0)  # Limpiar la tabla después de eliminar
                # Cierra el cursor y la conexión
                cursor.close()
                conexion.close()

                self.lineEdit_cedulabuscar_eliminar.clear()

    def refrescar(self):
        
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        # Establecer conexión con la base de datos

        cursor.execute("SELECT cedula, nombre, apellido, telefono, usuario, clave, permiso FROM usuarios")
        usuarios = cursor.fetchall()
        # Ejecutar consulta para obtener todos los usuarios

        # Limpiar las filas existentes en el widget de tabla
        self.tableWidget_usuarios.setRowCount(0)
        # Recorre sobre cada usuario obtenido de la consulta
        for row_number, usuario in enumerate(usuarios):
            # Insertar una nueva fila por cada usuario
            self.tableWidget_usuarios.insertRow(row_number)
            # Recorre sobre cada dato del usuario
            for column_number, data in enumerate(usuario):
                # Asigna cada dato a la celda correspondiente en el tableWidget
                self.tableWidget_usuarios.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        # Cerrar cursor y conexión
        cursor.close()
        conexion.close()

    def salir(self):
        self.close()
        # Cierra la ventana actual.

class Ui_QMainwindow_Reportes(QMainWindow): 
    #clase creada para la ventana de Reportes. 
    
    def __init__(self, ventana_report):
        super().__init__()
        loadUi("6.Reportes.ui", self)
        # Carga la interfaz de usuario desde el archivo
        
        
        # Crear una instancia de la ventana de Reportes
        self.ventana_report = ventana_report

        # Configurar las tablas como de solo lectura
        self.tableWidget_stock.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_stock_danados.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_stock_vencidos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_ventas.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_compras.setEditTriggers(QTableWidget.NoEditTriggers)

        # Conexiones de los botones a sus respectivos métodos para mostrar páginas
        self.pushButton_regresar_rep.clicked.connect(self.salir)

        self.pushButton_stock.clicked.connect(self.mostrar_pagina_stock)
        self.pushButton_stock_danados.clicked.connect(self.mostrar_pagina_danados)
        self.pushButton_stock_vencidos.clicked.connect(self.mostrar_pagina_vencidos)
        self.pushButton_Ventas.clicked.connect(self.mostrar_pagina_ventas)
        self.pushButton_compras.clicked.connect(self.mostrar_pagina_compra)  

        self.pushButton_refrescar_ventas.clicked.connect(self.refrescar_ventas)
        self.pushButton_refrescar_stock.clicked.connect(self.refrescar_productos)    
        self.pushButton_refrescar_stock_danados.clicked.connect(self.refrescar_stock_danados)
        self.pushButton_refrescar_stock_vencidos.clicked.connect(self.refrescar_stock_vencidos)
        self.pushButton_refrescar_compras.clicked.connect(self.refrescar_stock_compra)

        self.pushButton_imprimir_stock.clicked.connect(self.generar_reporte_productos_pdf)
        self.pushButton_imprimir_danados.clicked.connect(self.generar_reporte_productos_danados_pdf)
        self.pushButton_imprimir_vencidos.clicked.connect(self.generar_reporte_productos_vencidos_pdf)
        self.pushButton_imprimir_ventas.clicked.connect(self.generar_reporte_productos_ventas_pdf)
        self.pushButton_imprimir_compras.clicked.connect(self.generar_reporte_productos_compras_pdf)

        self.pushButton_refrescar_stock.clicked.connect(self.color_stock)
        self.columnas_stock()   
        self.columnas_stock_danados()
        self.columnas_stock_vencidos()
        self.columnas_stock_ventas()
        self.columnas_stock_compras()
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_ventas.setDate(QDate.currentDate())

        ayer = QDate.currentDate().addDays(-1)
        self.dateEdit_desde_compras.setDate(ayer)
        self.dateEdit_desde_ventas.setDate(ayer)

        self.dateEdit.dateChanged.connect(self.verificar_fecha)
        self.dateEdit_desde_compras.dateChanged.connect(self.verificar_fecha)
        self.dateEdit_ventas.dateChanged.connect(self.verificar_fecha)
        self.dateEdit_desde_ventas.dateChanged.connect(self.verificar_fecha)

    def verificar_fecha(self):
        fecha_seleccionada = self.sender().date()  # Utiliza sender() para obtener el QDateEdit que emitió la señal
        fecha_actual = QDate.currentDate()
        if fecha_seleccionada > fecha_actual:
            QMessageBox.warning(self, "Error", "No se puede seleccionar una fecha futura.")
            self.sender().setDate(fecha_actual)  # Utiliza sender() para establecer la fecha en el QDateEdit que emitió la señal

    def columnas_stock(self):
        # Establecer tamaño de las columnas
        self.tableWidget_stock.setColumnWidth(0, 150)
        self.tableWidget_stock.setColumnWidth(1, 200)
        self.tableWidget_stock.setColumnWidth(2, 150)
        self.tableWidget_stock.setColumnWidth(3, 150)
        self.tableWidget_stock.setColumnWidth(4, 140)

    def columnas_stock_danados(self):
        # Establecer tamaño de las columnas
        self.tableWidget_stock_danados.setColumnWidth(0, 100)
        self.tableWidget_stock_danados.setColumnWidth(1, 200)
        self.tableWidget_stock_danados.setColumnWidth(2, 100)
        self.tableWidget_stock_danados.setColumnWidth(3, 100)
        self.tableWidget_stock_danados.setColumnWidth(4, 100)

    def columnas_stock_vencidos(self):
        # Establecer tamaño de las columnas
        self.tableWidget_stock_vencidos.setColumnWidth(0, 100)
        self.tableWidget_stock_vencidos.setColumnWidth(1, 200)
        self.tableWidget_stock_vencidos.setColumnWidth(2, 100)
        self.tableWidget_stock_vencidos.setColumnWidth(3, 100)
        self.tableWidget_stock_vencidos.setColumnWidth(4, 100)

    def columnas_stock_ventas(self):
        # Establecer tamaño de las columnas
        self.tableWidget_ventas.setColumnWidth(0, 100)
        self.tableWidget_ventas.setColumnWidth(1, 100)
        self.tableWidget_ventas.setColumnWidth(2, 200)
        self.tableWidget_ventas.setColumnWidth(3, 250)
        self.tableWidget_ventas.setColumnWidth(4, 100)
        self.tableWidget_ventas.setColumnWidth(5, 200)

    def columnas_stock_compras(self):
        # Establecer tamaño de las columnas
        self.tableWidget_compras.setColumnWidth(0, 100)
        self.tableWidget_compras.setColumnWidth(1, 100)
        self.tableWidget_compras.setColumnWidth(2, 200)
        self.tableWidget_compras.setColumnWidth(3, 250)
        self.tableWidget_compras.setColumnWidth(4, 100)
        self.tableWidget_compras.setColumnWidth(5, 200)


    def color_stock(self):
     # Iterar sobre todas las filas de la tabla
        for row in range(self.tableWidget_stock.rowCount()):
            cantidad_item = self.tableWidget_stock.item(row, self.tableWidget_stock.columnCount() - 1)  # Obtener el item de la última columna
            if cantidad_item is not None:
                cantidad = int(cantidad_item.text())  # Obtener la cantidad como entero
                if cantidad <= 5:
                    self.colocar_color_stock(row, QColor(255,105,97))  # Rojo
                elif cantidad <= 15:
                    self.colocar_color_stock(row, QColor(253,253,150))  # Amarillo
                else:
                    self.colocar_color_stock(row, QColor(119,221,119))  # Azul

    def colocar_color_stock(self, row, color):
        # Establecer el color de toda la fila
        for col in range(self.tableWidget_stock.columnCount()):
            item = self.tableWidget_stock.item(row, col)
            if item is not None:
                item.setBackground(color)
        

    def generar_reporte_productos_pdf(self):

        # Crear el objeto PDF
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Times', 'B', 10)  # Reducir el tamaño de la fuente

        pdf.ln(50)

        # Obtener la fecha y hora actual
        now = datetime.now()
        fecha_actual = now.strftime("%Y-%m-%d")
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
        pdf.image("logo_potro_pdf.png", x=80, y=10, w=50)

        # Título del reporte
        titulo_reporte = f"REPORTE DE PRODUCTOS - {fecha_actual}"
        pdf.set_font('times', 'B', 16)  # Cambia el tamaño de la fuente aquí
        pdf.cell(190, 10, titulo_reporte, 0, 1, "C")
        pdf.set_font('Times', 'B', 10)

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

        pdf.image("logo_potro_pdf_fondo.png", x=55, y=100, w=100)


        # Guardar el PDF
        pdf.output(name=ruta_reporte, dest='F')

        # Mostrar mensaje exitoso
        QMessageBox.information(self, "Éxito", f"El reporte se ha generado exitosamente como '{nombre_reporte}'")

        # Abrir el PDF automáticamente
        os.startfile(ruta_reporte)

    def generar_reporte_productos_danados_pdf(self):
        # Crear el objeto PDF
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Times', 'B', 10)  # Reducir el tamaño de la fuente

        # Obtener la fecha y hora actual
        now = datetime.now()
        fecha_actual = now.strftime("%Y-%m-%d")
        hora_actual = now.strftime("%H:%M:%S")  # Formato 99:99:99

        # Carpeta de destino para los reportes
        carpeta_destino = "Reportes de Productos dañados"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Nombre único del archivo de reporte
        id_unico = str(uuid.uuid4())
        nombre_reporte = f"reporte_productos_dañados_{fecha_actual}_{id_unico}.pdf"
        ruta_reporte = os.path.join(carpeta_destino, nombre_reporte)

        # Título del reporte
        titulo_reporte = "Reporte Productos dañados - " + fecha_actual
        pdf.cell(190, 10, titulo_reporte, 0, 1, "C")  # Utilizar multicell para el título

        # Encabezado de la tabla
        encabezados = ["SKU", "CÓDIGO DE BARRAS", "DESCRIPCIÓN", "PRECIO", "CANTIDAD"]
        for encabezado in encabezados:
            pdf.cell(38, 10, encabezado, 1, 0, "C")  # Aumentar el ancho de las celdas
        pdf.ln()

        # Realizar la consulta a la base de datos SQLite
        conn = sqlite3.connect('Base de datos proyecto.db')
        c = conn.cursor()
        c.execute('''SELECT sku, codigo_barras, descripcion, precio, cantidad
                    FROM Productos_danados''')
        resultados = c.fetchall()

        # Agregar los resultados al PDF
        for resultado in resultados:
            for dato in resultado:
                pdf.cell(38, 10, str(dato), 1, 0, "C")  # Ajustar el ancho de las celdas
            pdf.ln()

        # Mostrar la fecha en la esquina superior izquierda
        pdf.set_xy(10, 10)
        pdf.cell(0, 0, fecha_actual, 0, 1, "L")

        # Mostrar la hora en la esquina superior derecha
        pdf.set_xy(-40, 10)
        pdf.cell(0, 0, hora_actual, 0, 1, "R")

        # Guardar el PDF
        pdf.output(name=ruta_reporte, dest='F')

        # Mostrar mensaje exitoso
        QMessageBox.information(self, "Éxito", f"El reporte se ha generado exitosamente como '{nombre_reporte}'")

        # Abrir el PDF automáticamente
        os.startfile(ruta_reporte)

    def generar_reporte_productos_vencidos_pdf(self):

        # Crear el objeto PDF
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Times', 'B', 10)  # Reducir el tamaño de la fuente

        # Obtener la fecha y hora actual
        now = datetime.now()
        fecha_actual = now.strftime("%Y-%m-%d")
        hora_actual = now.strftime("%H:%M:%S")  # Formato 99:99:99

        # Carpeta de destino para los reportes
        carpeta_destino = "Reportes de Productos vencidos"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Nombre único del archivo de reporte
        id_unico = str(uuid.uuid4())
        nombre_reporte = f"reporte_productos_vencidos_{fecha_actual}_{id_unico}.pdf"
        ruta_reporte = os.path.join(carpeta_destino, nombre_reporte)

        # Título del reporte
        titulo_reporte = "Reporte Productos vencidos - " + fecha_actual
        pdf.cell(190, 10, titulo_reporte, 0, 1, "C")  # Utilizar multicell para el título

        # Encabezado de la tabla
        encabezados = ["SKU", "CÓDIGO DE BARRAS", "DESCRIPCIÓN", "PRECIO", "CANTIDAD"]
        for encabezado in encabezados:
            pdf.cell(38, 10, encabezado, 1, 0, "C")  # Aumentar el ancho de las celdas
        pdf.ln()

        # Realizar la consulta a la base de datos SQLite
        conn = sqlite3.connect('Base de datos proyecto.db')
        c = conn.cursor()
        c.execute('''SELECT sku, codigo_barras, descripcion, precio, cantidad
                    FROM Productos_vencidos''')
        resultados = c.fetchall()

        # Agregar los resultados al PDF
        for resultado in resultados:
            for dato in resultado:
                pdf.cell(38, 10, str(dato), 1, 0, "C")  # Ajustar el ancho de las celdas
            pdf.ln()

        # Mostrar la fecha en la esquina superior izquierda
        pdf.set_xy(10, 10)
        pdf.cell(0, 0, fecha_actual, 0, 1, "L")

        # Mostrar la hora en la esquina superior derecha
        pdf.set_xy(-40, 10)
        pdf.cell(0, 0, hora_actual, 0, 1, "R")

        # Guardar el PDF
        pdf.output(name=ruta_reporte, dest='F')

        # Mostrar mensaje exitoso
        QMessageBox.information(self, "Éxito", f"El reporte se ha generado exitosamente como '{nombre_reporte}'")

        # Abrir el PDF automáticamente
        os.startfile(ruta_reporte)

    def generar_reporte_productos_ventas_pdf(self):
            
            # Crear el objeto PDF
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Times', 'B', 10)  # Mantener el tamaño de la fuente en 10

        # Obtener la fecha y hora actual
        now = datetime.now()
        fecha_actual = now.strftime("%Y-%m-%d")
        hora_actual = now.strftime("%H:%M:%S")  # Formato 99:99:99

        # Carpeta de destino para los reportes
        carpeta_destino = "Reportes de ventas"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Nombre único del archivo de reporte
        id_unico = str(uuid.uuid4())
        nombre_reporte = f"reporte_ventas_{fecha_actual}_{id_unico}.pdf"
        ruta_reporte = os.path.join(carpeta_destino, nombre_reporte)

        # Título del reporte
        titulo_reporte = "Reporte de ventas - " + fecha_actual
        pdf.cell(190, 10, titulo_reporte, 0, 1, "C")  # Utilizar multicell para el título

        # Encabezado de la tabla
        encabezados = ["ID", "Fecha", "SKU", "Código de Barras", "Cantidad", "Descripción"]
        anchos_columnas = [15, 25, 25, 35, 20, 70]  # Definir anchos de las columnas
        for encabezado, ancho in zip(encabezados, anchos_columnas):
            pdf.cell(ancho, 10, encabezado, 1, 0, "C")  # Ajustar el ancho de las celdas
        pdf.ln()

        # Realizar la consulta a la base de datos SQLite
        conn = sqlite3.connect('Base de datos proyecto.db')
        c = conn.cursor()
        c.execute('''SELECT id, fecha, sku_prod, codigo_barra_prod, cant, Descripcion_prod
                    FROM ventas''')
        resultados = c.fetchall()

        # Agregar los resultados al PDF
        for resultado in resultados:
            for dato, ancho in zip(resultado, anchos_columnas):
                pdf.cell(ancho, 10, str(dato), 1, 0, "C")  # Ajustar el ancho de las celdas
            pdf.ln()

        # Mostrar la fecha en la esquina superior izquierda
        pdf.set_xy(10, 10)
        pdf.cell(0, 0, fecha_actual, 0, 1, "L")

        # Mostrar la hora en la esquina superior derecha
        pdf.set_xy(-40, 10)
        pdf.cell(0, 0, hora_actual, 0, 1, "R")

        # Guardar el PDF
        pdf.output(name=ruta_reporte, dest='F')

        # Mostrar mensaje exitoso
        QMessageBox.information(self, "Éxito", f"El reporte se ha generado exitosamente como '{nombre_reporte}'")

        # Abrir el PDF automáticamente
        os.startfile(ruta_reporte)

    def generar_reporte_productos_compras_pdf(self):
        
          # Crear el objeto PDF
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Times', 'B', 10)  # Mantener el tamaño de la fuente en 10

        # Obtener la fecha y hora actual
        now = datetime.now()
        fecha_actual = now.strftime("%Y-%m-%d")
        hora_actual = now.strftime("%H:%M:%S")  # Formato 99:99:99

        # Carpeta de destino para los reportes
        carpeta_destino = "Reportes de compras"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Nombre único del archivo de reporte
        id_unico = str(uuid.uuid4())
        nombre_reporte = f"reporte_compras_{fecha_actual}_{id_unico}.pdf"
        ruta_reporte = os.path.join(carpeta_destino, nombre_reporte)

        # Título del reporte
        titulo_reporte = "Reporte de compras - " + fecha_actual
        pdf.cell(190, 10, titulo_reporte, 0, 1, "C")  # Utilizar multicell para el título

        # Encabezado de la tabla
        encabezados = ["ID", "Fecha", "SKU", "Código de Barras", "Cantidad", "Descripción"]
        anchos_columnas = [20, 20, 30, 40, 20, 60]  # Definir anchos de las columnas
        for encabezado, ancho in zip(encabezados, anchos_columnas):
            pdf.cell(ancho, 10, encabezado, 1, 0, "C")  # Ajustar el tamaño de las celdas
        pdf.ln()

        # Realizar la consulta a la base de datos SQLite
        conn = sqlite3.connect('Base de datos proyecto.db')
        c = conn.cursor()
        c.execute('''SELECT id, fecha, sku_prod, codigo_barra_prod, cant, Descripcion_prod
                    FROM compras''')
        resultados = c.fetchall()

        # Agregar los resultados al PDF
        for resultado in resultados:
            for dato, ancho in zip(resultado, anchos_columnas):
                pdf.cell(ancho, 10, str(dato), 1, 0, "C")  # Ajustar el tamaño de los campos
            pdf.ln()

        # Mostrar la fecha en la esquina superior izquierda
        pdf.set_xy(10, 10)
        pdf.cell(0, 0, fecha_actual, 0, 1, "L")

        # Mostrar la hora en la esquina superior derecha
        pdf.set_xy(-40, 10)
        pdf.cell(0, 0, hora_actual, 0, 1, "R")

        # Guardar el PDF
        pdf.output(name=ruta_reporte, dest='F')

        # Mostrar mensaje exitoso
        QMessageBox.information(self, "Éxito", f"El reporte se ha generado exitosamente como '{nombre_reporte}'")

        # Abrir el PDF automáticamente
        os.startfile(ruta_reporte)

        fecha_desde = self.dateEdit_desde_compras.date().toString("dd-MM-yyyy")
        fecha_hasta = self.dateEdit.date().toString("dd-MM-yyyy")

        # Crear el objeto PDF
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Times', 'B', 10)  # Mantener el tamaño de la fuente en 10

        # Obtener la fecha y hora actual
        now = datetime.now()
        fecha_actual = now.strftime("%Y-%m-%d")
        hora_actual = now.strftime("%H:%M:%S")  # Formato 99:99:99

        # Carpeta de destino para los reportes
        carpeta_destino = "Reportes de compras"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Nombre único del archivo de reporte
        id_unico = str(uuid.uuid4())
        nombre_reporte = f"reporte_compras_{fecha_actual}_{id_unico}.pdf"
        ruta_reporte = os.path.join(carpeta_destino, nombre_reporte)

        # Título del reporte
        titulo_reporte = "Reporte de compras - " + fecha_actual
        pdf.cell(190, 10, titulo_reporte, 0, 1, "C")  # Utilizar multicell para el título

        # Encabezado de la tabla
        encabezados = ["ID", "Fecha", "SKU", "Código de Barras", "Cantidad", "Descripción"]
        anchos_columnas = [20, 20, 30, 40, 20, 60]  # Definir anchos de las columnas
        for encabezado, ancho in zip(encabezados, anchos_columnas):
            pdf.cell(ancho, 10, encabezado, 1, 0, "C")  # Ajustar el tamaño de las celdas
        pdf.ln()

        # Realizar la consulta a la base de datos SQLite
        conn = sqlite3.connect('Base de datos proyecto.db')
        c = conn.cursor()
        fecha_seleccionada = self.dateEdit.date().toString("dd-MM-yyyy")
        c.execute("SELECT * FROM compras WHERE fecha BETWEEN ? AND ?", (fecha_desde, fecha_hasta))
        resultados = c.fetchall()

        # Verificar si se encontraron resultados
        if len(resultados) == 0:
            QMessageBox.warning(self, "Error", f"No se encuentran compras desde {fecha_desde} hasta {fecha_hasta}")
        else:
            # Agregar los resultados al PDF
            for resultado in resultados:
                for dato, ancho in zip(resultado, anchos_columnas):
                    pdf.cell(ancho, 10, str(dato), 1, 0, "C")  # Ajustar el tamaño de los campos
                pdf.ln()

            # Mostrar la fecha en la esquina superior izquierda
            pdf.set_xy(10, 10)
            pdf.cell(0, 0, fecha_actual, 0, 1, "L")

            # Mostrar la hora en la esquina superior derecha
            pdf.set_xy(-40, 10)
            pdf.cell(0, 0, hora_actual, 0, 1, "R")

            # Marca de agua como imagen
            pdf.image("logo_potro_pdf_fondo.png", x=55, y=100, w=100)

            # Guardar el PDF
            pdf.output(name=ruta_reporte, dest='F')

            # Mostrar mensaje exitoso
            QMessageBox.information(self, "Éxito", f"El reporte se ha generado exitosamente como '{nombre_reporte}'")

            # Abrir el PDF automáticamente
            os.startfile(ruta_reporte)

    # Metodos para mostrar las paginas
    def mostrar_pagina_stock(self):
       self.stackedWidget.setCurrentIndex(0)
    def mostrar_pagina_danados(self):
        self.stackedWidget.setCurrentIndex(1)
    def mostrar_pagina_vencidos(self):
       self.stackedWidget.setCurrentIndex(2)
    def mostrar_pagina_ventas(self):
        self.stackedWidget.setCurrentIndex(3)
    def mostrar_pagina_compra(self):
        self.stackedWidget.setCurrentIndex(4)    

    def refrescar_productos (self):
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM Productos")
            productos = cursor.fetchall()

            self.tableWidget_stock.setRowCount(0)  # Limpiar la tabla antes de añadir nuevas filas
        
            for row_number, row_data in enumerate(productos):
                self.tableWidget_stock.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_stock.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
            QMessageBox.information(self, "Actualizado", "Stock actualizado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error al actualizar", f"Se produjo un error al actualizar el stock: {str(e)}")
        finally:
            cursor.close()
            conexion.close()
    
    def refrescar_ventas (self): 
           
        try:
            conexion = sqlite3.connect("Base de datos proyecto.db")
            cursor = conexion.cursor()
            fecha_desde = self.dateEdit_desde_ventas.date().toString("dd-MM-yyyy")
            fecha_hasta = self.dateEdit_ventas.date().toString("dd-MM-yyyy")
            
            cursor.execute("SELECT * FROM ventas WHERE fecha BETWEEN ? AND ?", (fecha_desde, fecha_hasta))
            ventas = cursor.fetchall()
            
            if ventas:  # Si hay ventas para el intervalo de fechas seleccionado
                self.tableWidget_ventas.setRowCount(0)  # Limpiar la tabla antes de añadir nuevas filas
                for row_number, row_data in enumerate(ventas):
                    self.tableWidget_ventas.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_ventas.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                QMessageBox.information(self, "Actualizado", "Stock actualizado correctamente.")
            else:  # Si no hay ventas para el intervalo de fechas seleccionado
                QMessageBox.warning(self, "Error", f"No se encuentran ventas desde {fecha_desde} hasta {fecha_hasta}")
        except Exception as e:
            QMessageBox.critical(self, "Error al actualizar", f"Se produjo un error al actualizar el stock: {str(e)}")
        finally:
            conexion.close()

    def refrescar_stock_danados (self):
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM Productos_danados")
            danados = cursor.fetchall()

            self.tableWidget_stock_danados.setRowCount(0)  # Limpiar la tabla antes de añadir nuevas filas
        
            for row_number, row_data in enumerate(danados):
                self.tableWidget_stock_danados.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_stock_danados.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
            QMessageBox.information(self, "Actualizado", "Stock actualizado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error al actualizar", f"Se produjo un error al actualizar el stock: {str(e)}")
        finally:
            cursor.close()
            conexion.close()

    def refrescar_stock_vencidos (self):
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM Productos_vencidos")
            vencidos = cursor.fetchall()

            self.tableWidget_stock_vencidos.setRowCount(0)  # Limpiar la tabla antes de añadir nuevas filas
        
            for row_number, row_data in enumerate(vencidos):
                self.tableWidget_stock_vencidos.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_stock_vencidos.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
            QMessageBox.information(self, "Actualizado", "Stock actualizado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error al actualizar", f"Se produjo un error al actualizar el stock: {str(e)}")
        finally:
            cursor.close()
            conexion.close()

    def refrescar_stock_compra (self):
        try:
            conexion = sqlite3.connect("Base de datos proyecto.db")
            cursor = conexion.cursor()
            fecha_desde = self.dateEdit_desde_compras.date().toString("dd-MM-yyyy")
            fecha_hasta = self.dateEdit.date().toString("dd-MM-yyyy")
            
            cursor.execute("SELECT * FROM compras WHERE fecha BETWEEN ? AND ?", (fecha_desde, fecha_hasta))
            compras = cursor.fetchall()
            
            if compras:  # Si hay compras para el intervalo de fechas seleccionado
                self.tableWidget_compras.setRowCount(0)  # Limpiar la tabla antes de añadir nuevas filas
                for row_number, row_data in enumerate(compras):
                    self.tableWidget_compras.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_compras.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                QMessageBox.information(self, "Actualizado", "Stock actualizado correctamente.")
            else:  # Si no hay compras para el intervalo de fechas seleccionado
                QMessageBox.warning(self, "Error", f"No se encuentran compras desde {fecha_desde} hasta {fecha_hasta}")
        except Exception as e:
            QMessageBox.critical(self, "Error al actualizar", f"Se produjo un error al actualizar el stock: {str(e)}")
        finally:
            conexion.close()


    def salir(self):
        self.close()
        # Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.

class ui_QMainWindow_productos(QMainWindow):
    def __init__(self, ventana_producto):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("8.Productos.ui", self)
        

        # Configurar la tabla como de solo lectura
        self.tableWidget_eliminar.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # Conexiones de los botones a sus respectivos métodos para mostrar páginas
        self.pushButton_regresar.clicked.connect(self.salir)
        self.pushButton_anadir_in.clicked.connect(self.mostrar_anadir)
        self.pushButton_eliminar_su.clicked.connect(self.mostrar_eliminar)
        self.pushButton_actualizar.clicked.connect(self.mostra_actualizar)

        self.pushButton_limpiar_registrodeproducto.clicked.connect(self.limpiar_registro)
        self.pushButton_eliminar_limpiar.clicked.connect(self.limpiar_eliminar)

        self.pushButton_buscar_anadir.clicked.connect(self.buscar_anadir)
        self.pushButton_guardar_anadir.clicked.connect(self.guardar_anadir)

        self.pushButton_buscar_eliminar.clicked.connect(self.buscar_eliminar)
        self.pushButton_eliminar_eliminar.clicked.connect(self.elimar_prod)

        self.pushButton_buscar_sku.clicked.connect(self.buscar_actualizar)
        self.pushButton_actualizar_prod.clicked.connect(self.guardar_actualizar)
        self.pushButton_limpiar_actualizar.clicked.connect(self.limpiar_actualizar)
        

        # Conectar la señal cellDoubleClicked de la QTableWidget con la función mostrar_error_modificacion
        self.tableWidget_eliminar.cellDoubleClicked.connect(self.mostrar_error_modificacion)


        # Instanciar ventanas
        self.ventana_producto = ventana_producto

    def mostrar_error_modificacion(self):
        QMessageBox.warning(self, "Error", "No se permite la modificación de datos en esta tabla.")
        # Deseleccionar la celda que se intentó modificar
        self.tableWidget_eliminar.clearSelection()    

    # Metodos para mostrar las paginas
    def mostrar_eliminar(self):
       self.stackedWidget.setCurrentIndex(0)
    def mostrar_anadir(self):
        self.stackedWidget.setCurrentIndex(1)
    def mostra_actualizar(self):
        self.stackedWidget.setCurrentIndex(2)

    def limpiar_registro (self):
        self.lineEdit_Sku_anadir.clear()
        self.lineEdit_codigodebarra_anadir.clear()
        self.lineEdit_descripcion_anadir.clear()
        self.lineEdit_precio_anadir.clear()
        self.lineEdit_cant_anadir.clear()

    def limpiar_eliminar (self):
        self.lineEdit_sku_buscar_eliminar.clear()

    def buscar_anadir(self):
        # Recolecta el SKU ingresado en el QLineEdit
        sku_ingresado = self.lineEdit_Sku_anadir.text().strip()

        # Verificar si el campo está vacío
        if not sku_ingresado:
            QMessageBox.warning(self, "Campo vacío", "Por favor, ingrese el código a buscar.")
            return

        # Realizar la consulta en la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM Productos WHERE sku=?", (sku_ingresado,))
            producto = cursor.fetchone()

            if producto:
                QMessageBox.warning(self, "Código existente", "Este código ya se encuentra registrado.")
                # Mostrar los datos del producto en los lineEdits correspondientes
                self.lineEdit_codigodebarra_anadir.setText(producto[1])
                self.lineEdit_descripcion_anadir.setText(producto[2])
                self.lineEdit_precio_anadir.setText(str(producto[3]))
                self.lineEdit_cant_anadir.setText(str(producto[4]))
            else:
                QMessageBox.information(self, "Código nuevo", "Este código no se encuentra registrado. Es posible registrarlo.")
                # Limpiar los lineEdits
                self.lineEdit_codigodebarra_anadir.clear()
                self.lineEdit_descripcion_anadir.clear()
                self.lineEdit_precio_anadir.clear()
                self.lineEdit_cant_anadir.clear()
        except Exception as e:
            QMessageBox.critical(self, "Error al buscar", f"Se produjo un error al buscar el código: {str(e)}")
        finally:
            cursor.close()
            conexion.close() 

    def guardar_anadir(self):
        # Recolecta los datos ingresados en los QLineEdit
        sku = self.lineEdit_Sku_anadir.text().strip()
        codigo_barras = self.lineEdit_codigodebarra_anadir.text().strip()
        descripcion = self.lineEdit_descripcion_anadir.text().strip()
        precio = self.lineEdit_precio_anadir.text().strip()
        cantidad = self.lineEdit_cant_anadir.text().strip()

        # Validación de campos
        if not sku or not codigo_barras or not descripcion or not precio or not cantidad:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")
            return

        try:
            # Verificar si el SKU contiene solo caracteres numéricos
            int(sku)
        except ValueError:
            QMessageBox.warning(self, "Error en SKU", "El SKU debe contener solo caracteres numéricos.")
            return

        try:
            # Verificar si el precio es un número válido
            float(precio)
        except ValueError:
            QMessageBox.warning(self, "Error en precio", "El precio debe contener solo caracteres numéricos.")
            return

        try:
            # Verificar si la cantidad es un número válido
            int(cantidad)
        except ValueError:
            QMessageBox.warning(self, "Error en cantidad", "La cantidad debe contener solo caracteres numéricos.")
            return

        # Realizar consultas a la base de datos para verificar duplicados
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        try:
            # Verificar duplicados en SKU
            cursor.execute("SELECT sku FROM Productos WHERE sku=?", (sku,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Duplicado en SKU", "Ya existe un producto con este SKU.")
                return

            # Verificar duplicados en código de barras
            cursor.execute("SELECT codigo_barras FROM Productos WHERE codigo_barras=?", (codigo_barras,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Duplicado en Código de Barras", "Ya existe un producto con este código de barras.")
                return

            # Si no hay duplicados, insertar los datos en la base de datos
            cursor.execute("INSERT INTO Productos (sku, codigo_barras, descripcion, precio, cantidad) VALUES (?, ?, ?, ?, ?)",
                           (sku, codigo_barras, descripcion, precio, cantidad))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Registro guardado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error al guardar", f"Se produjo un error al guardar el registro: {str(e)}")
        finally:
            cursor.close()
            conexion.close()
        
    def buscar_eliminar(self):
        # Recolectar el SKU ingresado en el QLineEdit
        sku = self.lineEdit_sku_buscar_eliminar.text().strip()

        # Verificar si el campo está vacío
        if not sku:
            QMessageBox.warning(self, "Campo vacío", "Por favor, ingrese el SKU a buscar.")
            return

        # Realizar la consulta en la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM Productos WHERE sku=?", (sku,))
            productos_encontrados = cursor.fetchall()

            # Verificar si se encontraron productos
            if not productos_encontrados:
                QMessageBox.warning(self, "Producto no encontrado", "No se encontraron productos con el SKU especificado.")
                return

            # Limpiar la tabla antes de añadir nuevos resultados
            self.tableWidget_eliminar.setRowCount(0)

            # Mostrar los resultados en la tabla
            for producto in productos_encontrados:
                row_position = self.tableWidget_eliminar.rowCount()
                self.tableWidget_eliminar.insertRow(row_position)
                for column, data in enumerate(producto):
                    self.tableWidget_eliminar.setItem(row_position, column, QTableWidgetItem(str(data)))

            QMessageBox.information(self, "Búsqueda completada", "Se encontraron los productos con el SKU especificado.")
        except Exception as e:
            QMessageBox.critical(self, "Error al buscar", f"Se produjo un error al buscar los productos: {str(e)}")
        finally:
            cursor.close()
            conexion.close()

    def elimar_prod(self):
        try:
            # Recolectar el SKU ingresado en el QLineEdit
            sku = self.lineEdit_sku_buscar_eliminar.text().strip()

            # Verificar si el campo está vacío
            if not sku:
                QMessageBox.warning(self, "Campo vacío", "Por favor, ingrese el SKU a eliminar.")
                return

            # Realizar la consulta en la base de datos
            conexion = sqlite3.connect("Base de datos proyecto.db")
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT * FROM Productos WHERE sku=?", (sku,))
                producto = cursor.fetchone()

                # Verificar si se encontró un producto con el SKU especificado
                if not producto:
                    QMessageBox.warning(self, "Producto no encontrado", "No se encontró un producto con el SKU especificado.")
                    return

                # Si se encontró el producto, confirmar la eliminación
                respuesta = QMessageBox.question(self, "Confirmar eliminación", "¿Está seguro de que desea eliminar este producto?",
                                                  QMessageBox.Yes | QMessageBox.No)
                if respuesta == QMessageBox.Yes:
                    # Ejecutar la consulta de eliminación
                    cursor.execute("DELETE FROM Productos WHERE sku=?", (sku,))
                    conexion.commit()
                    QMessageBox.information(self, "Éxito", "Producto eliminado correctamente.")
                    self.tableWidget_eliminar.setRowCount(0)
            finally:
                cursor.close()
                conexion.close()
        except Exception as e:
            QMessageBox.critical(self, "Error al eliminar", f"Se produjo un error al eliminar el producto: {str(e)}")

    def buscar_actualizar (self):
       # Recolectar el SKU ingresado en el QLineEdit
        sku = self.lineEdit_skubuscar_actualizar.text().strip()

        # Verificar si el campo está vacío
        if not sku:
            QMessageBox.warning(self, "Campo vacío", "Por favor, ingrese el SKU a buscar.")
            return

        # Realizar la consulta en la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT codigo_barras, descripcion, precio FROM Productos WHERE sku=?", (sku,))
            producto = cursor.fetchone()

            # Verificar si se encontró un producto con el SKU especificado
            if not producto:
                QMessageBox.warning(self, "Producto no encontrado", "No se encontró un producto con el SKU especificado.")
                self.lineEdit_skubuscar_actualizar.clear()
                self.lineEdit_cb_actualizar.clear()
                self.lineEdit_descrp_actualizar.clear()
                self.lineEdit_precio_actualizar.clear()
                return

            # Si se encontró el producto, actualizar los campos correspondientes
            codigo_barras, descripcion, precio = producto
            self.lineEdit_cb_actualizar.setText(codigo_barras)
            self.lineEdit_descrp_actualizar.setText(descripcion)
            self.lineEdit_precio_actualizar.setText(str(precio))
        except Exception as e:
            QMessageBox.critical(self, "Error al buscar", f"Se produjo un error al buscar el producto: {str(e)}")
        finally:
            cursor.close()
            conexion.close()   

    def guardar_actualizar (self):
        # Recolectar los datos ingresados en los QLineEdit
        sku = self.lineEdit_skubuscar_actualizar.text().strip()
        codigo_barras = self.lineEdit_cb_actualizar.text().strip()
        descripcion = self.lineEdit_descrp_actualizar.text().strip()
        precio = self.lineEdit_precio_actualizar.text().strip()

        # Verificar que los campos no estén vacíos
        if not sku or not codigo_barras or not descripcion or not precio:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")
            return

        # Verificar que el campo de código de barras sea numérico
        if not codigo_barras.isdigit():
            QMessageBox.warning(self, "Error", "El código de barras debe ser numérico.")
            return

        # Verificar que el campo de precio sea numérico
        try:
            float(precio)
        except ValueError:
            QMessageBox.warning(self, "Error", "El precio debe ser un valor numérico.")
            return

        # Confirmar la actualización con un cuadro de diálogo
        respuesta = QMessageBox.question(self, "Confirmar actualización", "¿Está seguro de que desea actualizar los datos del producto?",
                                          QMessageBox.Yes | QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
            # Actualizar los datos en la base de datos
            conexion = sqlite3.connect("Base de datos proyecto.db")
            cursor = conexion.cursor()
            try:
                cursor.execute("UPDATE Productos SET codigo_barras=?, descripcion=?, precio=? WHERE sku=?",
                               (codigo_barras, descripcion, precio, sku))
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Producto actualizado correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error al actualizar", f"Se produjo un error al actualizar el producto: {str(e)}")
            finally:
                cursor.close()
                conexion.close()
                self.lineEdit_skubuscar_actualizar.clear()
                self.lineEdit_cb_actualizar.clear()
                self.lineEdit_descrp_actualizar.clear()
                self.lineEdit_precio_actualizar.clear()
        
    def limpiar_actualizar (self):
        self.lineEdit_skubuscar_actualizar.clear()
        self.lineEdit_cb_actualizar.clear()
        self.lineEdit_descrp_actualizar.clear()
        self.lineEdit_precio_actualizar.clear()  

    def salir(self):
        self.close() # Cierra la ventana actual.

class ui_QMainWindow_inventario(QMainWindow):

    def __init__(self, ventana_inventario):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("10.Inventario.ui", self)

        self.ventana_inventario = ventana_inventario

        self.pushButton_salir_menu.clicked.connect(self.salir)
        self.pushButton_ajustesmanuales.clicked.connect(self.mostrar_pagina_ajustes_manuales)
        self.pushButton_ingresarcompras.clicked.connect(self.mostrar_pagina_compras)
        self.pushButton_ingresarventa.clicked.connect(self.mostrar_pagina_ventas)

        self.pushButton_buscar_ingresarventa.clicked.connect(self.buscar_sku_venta)
        self.pushButton_enviar.clicked.connect(self.guardar_venta)
        self.pushButton_limpiar.clicked.connect(self.limpiar_campos_venta)

        self.pushButton_buscar_sku.clicked.connect(self.buscar_sku_ajuste)
        self.pushButton_actualizar_cant.clicked.connect(self.actualizar_cant_ajuste)
        self.pushButton_buscar_ingresarcompra.clicked.connect(self.buscar_sku_compras)
        self.pushButton_enviar_compra.clicked.connect(self.guardar_compra)
        self.pushButton_limpiar_campos_compras.clicked.connect(self.limpiar_campos_compra)


        # Metodos para mostrar las paginas
    def mostrar_pagina_ajustes_manuales(self):
       self.stackedWidget.setCurrentIndex(0)
    def mostrar_pagina_compras(self):
        self.stackedWidget.setCurrentIndex(1)
    def mostrar_pagina_ventas(self):
       self.stackedWidget.setCurrentIndex(2)

    def buscar_sku_venta(self):

        sku = self.lineEdit_sku_ingresarventa.text().strip()

        # Verificar si el campo está vacío
        if not sku:
            QMessageBox.warning(self, "Error", "Por favor ingrese el SKU del producto.")
            return

        # Conectar a la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        # Preparar la consulta para buscar el código de barras y la descripción correspondiente al SKU
        try:
            cursor.execute("SELECT codigo_barras, descripcion FROM Productos WHERE sku = ?", (sku,))
            resultado = cursor.fetchone()

            if resultado:
                # Si encontramos un resultado, actualizar los QLineEdit del código de barras y descripción
                self.lineEdit_cod_ingresarventa.setText(resultado[0])
                self.lineEdit_descripicion_ingresarventa.setText(resultado[1])
            else:
                # Si no hay resultados, limpiar los QLineEdit y mostrar un mensaje
                self.lineEdit_cod_ingresarventa.clear()
                self.lineEdit_descripicion_ingresarventa.clear()
                QMessageBox.warning(self, "Sin resultados", "No se encontraron productos con el SKU proporcionado.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error al buscar el producto: {str(e)}")
        finally:
            cursor.close()
            conexion.close()

    def guardar_venta(self):

        # Recolecta datos de los QLineEdit
        datos = {
            "fecha": self.lineEdit_fecha_ingresarventa.text().strip(),
            "sku_prod": self.lineEdit_sku_ingresarventa.text().strip(),
            "codigo_barra_prod": self.lineEdit_cod_ingresarventa.text().strip(),
            "cant": self.lineEdit_cant_ingresarventa.text().strip(),
            "descripcion_prod": self.lineEdit_descripicion_ingresarventa.text().strip()
        }

        # Validación del formato de la fecha
        if not re.match(r'\d{2}-\d{2}-\d{4}', datos['fecha']):
            QMessageBox.warning(self, "Error en la fecha", "Por favor revise la fecha. El formato debe ser 99/99/9999.")
            return

        # Verifica si algún campo obligatorio está vacío.
        campos_vacios = []
        for campo, valor in datos.items():
            if not valor:
                if campo == 'cant':
                    QMessageBox.warning(self, "Campo requerido", "Por favor, ingrese la cantidad.")
                elif campo == 'descripcion_prod':
                    QMessageBox.warning(self, "Campo requerido", "Por favor, ingrese descripción del producto.")
                else:
                    campos_vacios.append(campo)

        if campos_vacios:
            QMessageBox.warning(self, "Campos requeridos", f"Por favor, complete los siguientes campos: {', '.join(campos_vacios)}")
            return

        # Conversión de la cantidad a entero y manejo de la posible excepción
        try:
            datos['cant'] = int(datos['cant'])
        except ValueError:
            QMessageBox.warning(self, "Error de tipo", "La cantidad debe ser un número entero.")
            return
        
        # Verificar que la cantidad no sea cero
        if datos['cant'] <= 0:
            QMessageBox.warning(self, "Error en la cantidad", "La cantidad debe ser mayor que cero.")
            return

        # Conexion con la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT cantidad FROM Productos WHERE sku = ?", (datos['sku_prod'],))
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is None:
                QMessageBox.warning(self, "Error de stock", "Producto no encontrado en el inventario.")
                return

            if datos['cant'] > cantidad_actual[0]:
                QMessageBox.warning(self, "Error de stock", "No hay suficiente stock para realizar la venta.")
                return

            # Si hay suficiente stock, procedemos a registrar la venta y actualizar el stock
            cursor.execute("INSERT INTO ventas (fecha, sku_prod, codigo_barra_prod, cant, descripcion_prod) VALUES (?, ?, ?, ?, ?)",
                           (datos['fecha'], datos['sku_prod'], datos['codigo_barra_prod'], datos['cant'], datos['descripcion_prod']))
            conexion.commit()

            cursor.execute("UPDATE Productos SET cantidad = cantidad - ? WHERE sku = ?",
                           (datos['cant'], datos['sku_prod']))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Venta ingresada y stock actualizado satisfactoriamente.")

        except Exception as e:
            QMessageBox.critical(self, "Error al guardar", f"Se produjo un error al procesar la venta: {str(e)}")
        finally:
            cursor.close()
            conexion.close()
            self.lineEdit_fecha_ingresarventa.clear()
            self.lineEdit_sku_ingresarventa.clear()
            self.lineEdit_cod_ingresarventa.clear()
            self.lineEdit_cant_ingresarventa.clear()
            self.lineEdit_descripicion_ingresarventa.clear()  # Cierra la conexión a la base de datos

    def limpiar_campos_venta(self):

        self.lineEdit_fecha_ingresarventa.clear()
        self.lineEdit_sku_ingresarventa.clear()
        self.lineEdit_cod_ingresarventa.clear()
        self.lineEdit_cant_ingresarventa.clear()
        self.lineEdit_descripicion_ingresarventa.clear()
        #Limpia todos los campos del formulario de ingresar ventas.

    def buscar_sku_ajuste (self):

        sku = self.lineEdit_sku_buscar.text().strip()

        # Verificar si el campo está vacío
        if not sku:
            QMessageBox.warning(self, "Error", "Por favor ingrese el SKU del producto.")
            return

        # Conectar a la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        # Preparar la consulta para buscar el código de barras y la descripción correspondiente al SKU
        try:
            cursor.execute("SELECT descripcion, cantidad FROM Productos WHERE sku = ?", (sku,))
            resultado = cursor.fetchone()

            if resultado:
                # Si encontramos un resultado, actualizar los QLineEdit del código de barras y descripción
                self.lineEdit_descrip_prod.setText(resultado[0])
                self.lineEdit_cant_prod.setText(str(resultado[1]))
            else:
                # Si no hay resultados, limpiar los QLineEdit y mostrar un mensaje
                self.lineEdit_sku_buscar.clear()
                QMessageBox.warning(self, "Sin resultados", "No se encontraron productos con el SKU proporcionado.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error al buscar el producto: {str(e)}")
        finally:
            cursor.close()
            conexion.close()

    def actualizar_cant_ajuste (self):
        # Obtiene el SKU ingresado
        sku = self.lineEdit_sku_buscar.text().strip()

        # Verifica si el campo SKU está vacío
        if not sku:
            QMessageBox.warning(self, "Campo requerido", "Por favor, ingrese el SKU del producto.")
            return

        # Obtiene la nueva cantidad ingresada
        nueva_cantidad = self.lineEdit_cant_prod.text().strip()

        # Verifica si la nueva cantidad es un número entero
        try:
            nueva_cantidad = int(nueva_cantidad)
        except ValueError:
            QMessageBox.warning(self, "Error", "La cantidad debe ser un número entero.")
            return

        # Conectar a la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        try:
            # Verifica si el producto existe en la base de datos
            cursor.execute("SELECT * FROM Productos WHERE sku = ?", (sku,))
            producto_actual = cursor.fetchone()

            if producto_actual:
                # Si el producto existe, actualiza la cantidad en la base de datos
                cursor.execute("UPDATE Productos SET cantidad = ? WHERE sku = ?", (nueva_cantidad, sku))
                conexion.commit()
                QMessageBox.information(self, "Actualización exitosa", "Cantidad actualizada satisfactoriamente")
            else:
                QMessageBox.warning(self, "Producto no encontrado", "No se encontró un producto con ese SKU.")

        except Exception as e:
            # Capturar cualquier otro tipo de excepción genérica
            QMessageBox.critical(self, "Error de actualización", f"Error al actualizar la cantidad: {str(e)}")

        finally:
            # Cierra el cursor y la conexión a la base de datos
            cursor.close()
            conexion.close()
    
    def buscar_sku_compras(self):

        sku = self.lineEdit_sku_ingresarcompra.text().strip()

        # Verificar si el campo está vacío
        if not sku:
            QMessageBox.warning(self, "Error", "Por favor ingrese el SKU del producto.")
            return

        # Conectar a la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        # Preparar la consulta para buscar el código de barras y la descripción correspondiente al SKU
        try:
            cursor.execute("SELECT codigo_barras, descripcion FROM Productos WHERE sku = ?", (sku,))
            resultado = cursor.fetchone()

            if resultado:
                # Si encontramos un resultado, actualizar los QLineEdit del código de barras y descripción
                self.lineEdit_cod_ingresarcompra.setText(resultado[0])
                self.lineEdit_descripicion_ingresarcompra.setText(resultado[1])
            else:
                # Si no hay resultados, limpiar los QLineEdit y mostrar un mensaje
                self.lineEdit_cod_ingresarcompra.clear()
                self.lineEdit_descripicion_ingresarcompra.clear()
                QMessageBox.warning(self, "Sin resultados", "No se encontraron productos con el SKU proporcionado.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error al buscar el producto: {str(e)}")
        finally:
            cursor.close()
            conexion.close()

    def guardar_compra(self):

        # Obtiene los datos ingresados
        datos = {
            "fecha": self.lineEdit_fecha_ingresarcompra.text().strip(),
            "sku_prod": self.lineEdit_sku_ingresarcompra.text().strip(),
            "codigo_barra_prod": self.lineEdit_cod_ingresarcompra.text().strip(),
            "cant": self.lineEdit_cant_ingresarcompra.text().strip(),
            "descripcion_prod": self.lineEdit_descripicion_ingresarcompra.text().strip()
        }

        # Verifica si algún campo está vacío
        campos_vacios = [campo for campo, valor in datos.items() if not valor]

        if campos_vacios:
            QMessageBox.warning(self, "Campos requeridos", f"Por favor, complete los siguientes campos: {', '.join(campos_vacios)}")
            return

        # Validación del formato de la fecha
        if not re.match(r'\d{2}-\d{2}-\d{4}', datos['fecha']):
            QMessageBox.warning(self, "Error en la fecha", "Por favor revise la fecha. El formato debe ser 99/99/9999.")
            return

        # Conversión de la cantidad a entero y manejo de la posible excepción
        try:
            datos['cant'] = int(datos['cant'])
        except ValueError:
            QMessageBox.warning(self, "Error de tipo", "La cantidad debe ser un número entero.")
            return

        # Verificar que la cantidad no sea cero
        if datos['cant'] <= 0:
            QMessageBox.warning(self, "Error en la cantidad", "La cantidad debe ser mayor que cero.")
            return

        # Conexion con la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()

        try:
            # Inserta la nueva venta en la base de datos
            cursor.execute("INSERT INTO ventas (fecha, sku_prod, codigo_barra_prod, cant, descripcion_prod) VALUES (?, ?, ?, ?, ?)",
                        (datos['fecha'], datos['sku_prod'], datos['codigo_barra_prod'], datos['cant'], datos['descripcion_prod']))
            conexion.commit()

            # Actualiza la cantidad de productos sumándola con la cantidad ingresada
            cursor.execute("UPDATE Productos SET cantidad = cantidad + ? WHERE sku = ?", (datos['cant'], datos['sku_prod']))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Venta ingresada y stock actualizado satisfactoriamente.")

        except Exception as e:
            QMessageBox.critical(self, "Error al guardar", f"Se produjo un error al procesar la venta: {str(e)}")

        finally:
            cursor.close()
            conexion.close()
            self.lineEdit_fecha_ingresarcompra.clear()
            self.lineEdit_sku_ingresarcompra.clear()
            self.lineEdit_cod_ingresarcompra.clear()
            self.lineEdit_cant_ingresarcompra.clear()
            self.lineEdit_descripicion_ingresarcompra.clear()

    def limpiar_campos_compra(self):
        self.lineEdit_fecha_ingresarcompra.clear()
        self.lineEdit_sku_ingresarcompra.clear()
        self.lineEdit_cod_ingresarcompra.clear()
        self.lineEdit_cant_ingresarcompra.clear()
        self.lineEdit_descripicion_ingresarcompra.clear()


    def salir (self):
        self.close()
        # Cierra la ventana actual.      

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Ui_Qdialog_login()
    login.show()
    sys.exit(app.exec_())