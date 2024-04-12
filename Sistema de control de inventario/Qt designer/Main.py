import sys
import re
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
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
        

class Ui_QMainwindow_Menu_principal(QMainWindow): #clase creada para la ventana de menu principal 
    
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

        # Conexiones de los botones a sus respectivos métodos para mostrar páginas
        self.pushButton_regresar_gestion.clicked.connect(self.salir)
        self.pushButton_usuarios.clicked.connect(self.mostrar_pagina_usuarios)
        self.pushButton_anadir.clicked.connect(self.mostrar_pagina_anadir)
        self.pushButton_eliminar.clicked.connect(self.mostrar_pagina_eliminar)
        self.pushButton_actualizar.clicked.connect(self.mostrar_pagina_actualizar)
        self.pushButton_limpiar_registrodeusuario.clicked.connect(self.limpiar)
        self.pushButton_guardar_registrodeusuario.clicked.connect(self.guardar)

    # Métodos para mostrar las páginas
    def mostrar_pagina_usuarios(self):
        self.stackedWidget.setCurrentIndex(0)

    def mostrar_pagina_actualizar(self):
        self.stackedWidget.setCurrentIndex(1)

    def mostrar_pagina_eliminar(self):
        self.stackedWidget.setCurrentIndex(2)

    def mostrar_pagina_anadir(self):
        self.stackedWidget.setCurrentIndex(3)

    def limpiar(self):
        self.lineEdit_nombre_registrodeusuario.clear()
        self.lineEdit_cedula_registrodeusuario.clear()
        self.lineEdit_telefono_registrodeusuario.clear()
        self.lineEdit_apellido_registrodeusuario.clear()
        self.lineEdit_usuario_registrodeusuario.clear()
        self.lineEdit_clave_registrodeusuario.clear() 
        #Limpia todos los campos del formulario de registro de usuario. 

    def guardar(self):
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
        
         # Capturar cualquier otro tipo de excepción genérica
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Se produjo un error al guardar los datos: {str(e)}")
        
         # Asegurarse de cerrar la conexión a la base de datos, independientemente del resultado de las operaciones anteriores.
        finally:
            if conexion:
                conexion.close()

    def salir(self):
        self.close()
        # Cierra la ventana actual.

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

        # Guardar los datos en la base de datos
        conexion = sqlite3.connect("Base de datos proyecto.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO ventas (fecha, sku_prod, codigo_barra_prod, cant, descripcion_prod) VALUES (?, ?, ?, ?, ?)",
                           (datos['fecha'], datos['sku_prod'], datos['codigo_barra_prod'], datos['cant'], datos['descripcion_prod']))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Venta ingresada satisfactoriamente.")
        except Exception as e:
            # Capturar cualquier otro tipo de excepción genérica
            QMessageBox.critical(self, "Error al guardar", f"Se produjo un error al enviar los datos: {str(e)}")
        finally:
            cursor.close()  # Cierra el cursor
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
        # Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.    

class Ui_QMainwindow_Reportes(QMainWindow): #clase creada para la ventana de Reportes 
    
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

class Ui_QMainwindow_Ajustes_anadir_eliminar(QMainWindow): #clase creada para la ventana de Añadir/eliminar 
    
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
        self.close()
# Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.






















if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Punto de entrada principal de la aplicación.
    ventana = Ui_ventana_inicio()
    ventana.showFullScreen() 
    # Instanciar y mostrar la ventana de inicio en pantalla completa
    sys.exit(app.exec_())
    # Ejecutar la aplicación hasta que se cierre la ventana principal
