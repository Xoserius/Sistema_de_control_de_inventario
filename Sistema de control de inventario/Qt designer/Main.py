import sys
import re
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QImage


class Ui_ventana_inicio(QMainWindow): #clase creada para la ventana de Inicio 
    
    def __init__(self):
        # Inicializa una nueva instancia de la clase.
        super().__init__() 
        # Llama al constructor de la clase base
        loadUi("1.Inicio.ui", self) 
        # Carga la interfaz de usuario desde el archivo

        # Conectar el botón "Iniciar sesión" a la función para abrir la ventana de inicio de sesión
        self.pushButton_iniciarsesion.clicked.connect(self.abrir_ventana_login)
        self.pushButton_Salir.clicked.connect(self.salir)
        # Conectar a la base de datos
        self.conexion_db = sqlite3.connect("Base de datos proyecto.db")
        # Crear una instancia de la ventana de menú principal
        self.ventana_menu_principal = Ui_QMainwindow_Menu_principal()

    def salir(self):
        # Cerrar la conexión a la base de datos antes de salir
        self.conexion_db.close()
        self.close()

    def abrir_ventana_login(self):
        # Mostrar la ventana de inicio de sesión
        self.ventana_login = Ui_Qdialog_login(self.conexion_db, self.ventana_menu_principal)
        self.ventana_login.show()
 
class Ui_Qdialog_login(QDialog): #clase creada para la ventana de Login 

    
    def __init__(self, conexion_db, ventana_menu_principal):
        super().__init__()
        loadUi("2.Login.ui", self)
        # Carga la interfaz de usuario desde el archivo

        self.conexion_db = conexion_db
        self.ventana_menu_principal = ventana_menu_principal

        # Conectar el botón "Aceptar" a la función para iniciar sesión
        self.pushButton_aceptar.clicked.connect(self.iniciar_sesion)

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
                self.ventana_menu_principal.showFullScreen()
            else:
                QMessageBox.warning(self, "Acceso denegado", "Usuario o clave inválida.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error al intentar iniciar sesión: {str(e)}")    

class Ui_QMainwindow_Menu_principal(QMainWindow): 
    #clase creada para la ventana de menu principal

    def __init__(self):
        super().__init__() 
        loadUi("3.Menu_principal.ui", self)
        # Carga la interfaz de usuario desde el archivo

        # Conectar botones a funciones
        self.pushButton_salir_menu.clicked.connect(self.salir)
        self.pushButton_gestiondeusuario.clicked.connect(self.abrir_ventana_gestion)
        self.pushButton_ingresarventa.clicked.connect(self.abrir_ingresar_ventas)
        self.pushButton_reportes.clicked.connect(self.abrir_reportes)
        self.pushButton_anadir_eliminar.clicked.connect(self.abrir_ajustes)
        self.pushButton_productos.clicked.connect(self.abrir_Productos)
      

        # Instanciar ventanas
        self.ventana_gestionusu = Ui_QMainwindow_Gestion_de_usuarios(QMainWindow)
        self.ventana_ingresarven = Ui_QMainwindow_Ingresar_ventas(QMainWindow)
        self.ventana_report = Ui_QMainwindow_Reportes(QMainWindow)
        self.ventana_ajustes = Ui_QMainwindow_Ajustes_anadir_eliminar(QMainWindow)
        self.ventana_producto = ui_QMainWindow_productos(QMainWindow)
       

    def abrir_ventana_gestion(self):
        # metodo para mostrar la ventana de gestion de usuarios
        self.ventana_gestionusu = Ui_QMainwindow_Gestion_de_usuarios(self.ventana_gestionusu)
        # Instanciar ventana
        self.ventana_gestionusu.showFullScreen()
        # Mostrar ventana en pantalla completa

    def abrir_ingresar_ventas(self):
        # metodo para mostrar la ventana de ingresar ventas
        self.ventana_ingresarven = Ui_QMainwindow_Ingresar_ventas(self.ventana_ingresarven)
        # Instanciar ventana
        self.ventana_ingresarven.showFullScreen()
        # Mostrar ventana en pantalla completa

    def abrir_reportes (self):
        # Mostrar la ventana de Reportes
        self.ventana_report = Ui_QMainwindow_Reportes(self.ventana_report)
        # Instanciar ventana
        self.ventana_report.showFullScreen()
        # Mostrar ventana en pantalla completa
    
    def abrir_ajustes (self):# Mostrar la ventana de añadir/eliminar
        self.ventana_ajustes = Ui_QMainwindow_Ajustes_anadir_eliminar(self.ventana_ajustes)
        # Instanciar ventana
        self.ventana_ajustes.showFullScreen()
        # Mostrar ventana en pantalla completa

    def abrir_Productos (self):# Mostrar la ventana de añadir/eliminar
        self.ventana_producto = ui_QMainWindow_productos(self.ventana_producto)
        # Instanciar ventana
        self.ventana_producto.showFullScreen()
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
            # Ejecutar un comando SQL para insertar datos en la tabla 'usuarios'.
            cursor.execute("INSERT INTO usuarios (cedula, nombre, apellido, telefono, usuario, clave, permiso) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (cedula, nombre, apellido, telefono, usuario, clave, permiso))
            # Confirmar la transacción para asegurar que los datos se guarden de forma permanente.
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Datos guardados correctamente.")
            # Mensaje al usuario que los datos han sido Guardados correctamente.

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

            self.lineEdit_cedula_registrodeusuario.clear()
            self.lineEdit_nombre_registrodeusuario.clear()
            self.lineEdit_apellido_registrodeusuario.clear()
            self.lineEdit_telefono_registrodeusuario.clear()
            self.lineEdit_usuario_registrodeusuario.clear()
            self.lineEdit_clave_registrodeusuario.clear()        

    def salir(self):
        self.close()
        # Cierra la ventana actual.

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

        
        if not cursor.fetchone():
            # Mensaje de error si no se encontro ningun usuario.
            QMessageBox.warning(self, "No encontrado", "Esta cédula no se encuentra registrada")
        else:
            # Ejecuta la consulta SQL para eliminar al usuario con la cédula especificada
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

class Ui_QMainwindow_Ingresar_ventas(QMainWindow): #clase creada para la ventana de ingresar ventas 
    
    def __init__(self, ventana_ingresarventas):
        super().__init__()
        loadUi("5.Ingresar_ventas.ui", self)
        # Carga la interfaz de usuario desde el archivo
        self.pushButton_regresar_iv.clicked.connect(self.salir)
        self.pushButton_buscar_ingresarventa.clicked.connect(self.buscar)
        self.pushButton_enviar.clicked.connect(self.guardar)
        self.pushButton_limpiar.clicked.connect(self.limpiar)
        # Crear una instancia de la ventana de ingresar ventas
        self.ventana_ingresarventas = ventana_ingresarventas

    
    def buscar(self):

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


    def guardar(self):

        # Recolecta datos de los QLineEdit
        datos = {
            "fecha": self.lineEdit_fecha_ingresarventa.text().strip(),
            "sku_prod": self.lineEdit_sku_ingresarventa.text().strip(),
            "codigo_barra_prod": self.lineEdit_cod_ingresarventa.text().strip(),
            "cant": self.lineEdit_cant_ingresarventa.text().strip(),
            "descripcion_prod": self.lineEdit_descripicion_ingresarventa.text().strip()
        }

        # Validación del formato de la fecha
        if not re.match(r'\d{2}/\d{2}/\d{2}', datos['fecha']):
            QMessageBox.warning(self, "Error en la fecha", "Por favor revise la fecha. El formato debe ser 99/99/99.")
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
            conexion.close()  # Cierra la conexión a la base de datos

    def limpiar(self):

        self.lineEdit_fecha_ingresarventa.clear()
        self.lineEdit_sku_ingresarventa.clear()
        self.lineEdit_cod_ingresarventa.clear()
        self.lineEdit_cant_ingresarventa.clear()
        self.lineEdit_descripicion_ingresarventa.clear()
        #Limpia todos los campos del formulario de ingresar ventas.

    def salir(self):
        self.close()

class Ui_QMainwindow_Reportes(QMainWindow): 
    #clase creada para la ventana de Reportes. 
    
    def __init__(self, ventana_report):
        super().__init__()
        loadUi("6.Reportes.ui", self)
        # Carga la interfaz de usuario desde el archivo
        
        # Crear una instancia de la ventana de Reportes
        self.ventana_report = ventana_report

        # Conexiones de los botones a sus respectivos métodos para mostrar páginas
        self.pushButton_regresar_rep.clicked.connect(self.salir)
        self.pushButton_stock.clicked.connect(self.mostrar_pagina_stock)
        self.pushButton_stock_danados.clicked.connect(self.mostrar_pagina_danados)
        self.pushButton_stock_vencidos.clicked.connect(self.mostrar_pagina_vencidos)
        self.pushButton_Ventas.clicked.connect(self.mostrar_pagina_ventas)
        
      
    # Metodos para mostrar las paginas
    def mostrar_pagina_stock(self):
       self.stackedWidget.setCurrentIndex(0)
    def mostrar_pagina_danados(self):
        self.stackedWidget.setCurrentIndex(1)
    def mostrar_pagina_vencidos(self):
       self.stackedWidget.setCurrentIndex(2)
    def mostrar_pagina_ventas(self):
        self.stackedWidget.setCurrentIndex(3)
    

    def salir(self):
        self.close()
        # Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.

class Ui_QMainwindow_Ajustes_anadir_eliminar(QMainWindow):
    #clase creada para la ventana de Añadir/eliminar  
    
    def __init__(self, ventana_ajustes):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("7.Ajustes_anadir_eliminar.ui", self)
         # Conectar botones a funciones
        self.pushButton_regresar_ajus.clicked.connect(self.salir)
        # Instanciar ventanas
        self.ventana_ajustes = ventana_ajustes

    def salir(self):
        self.close()
        # Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.

class ui_QMainWindow_productos(QMainWindow):
    def __init__(self, ventana_producto):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("8.Productos.ui", self)
        
        # Conexiones de los botones a sus respectivos métodos para mostrar páginas
        self.pushButton_regresar.clicked.connect(self.salir)
        self.pushButton_anadir_in.clicked.connect(self.mostrar_anadir)
        self.pushButton_eliminar_su.clicked.connect(self.mostrar_eliminar)
        # Instanciar ventanas
        self.ventana_producto = ventana_producto

    # Metodos para mostrar las paginas
    def mostrar_eliminar(self):
       self.stackedWidget.setCurrentIndex(0)
    def mostrar_anadir(self):
        self.stackedWidget.setCurrentIndex(1)

    def salir(self):
        self.close() # Cierra la ventana actual.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Punto de entrada principal de la aplicación.
    ventana = Ui_ventana_inicio()
    ventana.showFullScreen() 
    # Instanciar y mostrar la ventana de inicio en pantalla completa
    sys.exit(app.exec_())
    # Ejecutar la aplicación hasta que se cierre la ventana principal