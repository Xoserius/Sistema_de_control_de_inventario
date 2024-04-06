import sys
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
        # Obtener los valores de los campos de texto
        usuario = self.lineEdit_usuario.text()
        clave = self.lineEdit_clave.text()

        # Realizar la consulta a la base de datos
        cursor = self.conexion_db.cursor()
        consulta = "SELECT * FROM usuarios WHERE usuario = ? AND clave = ?"
        cursor.execute(consulta, (usuario, clave))
        resultado = cursor.fetchone()
        
        # Cerrar el cursor
        cursor.close()

        if resultado:
            # Si la consulta devuelve resultados, abrir la ventana del menú principal
            self.close()
            self.ventana_menu_principal.showFullScreen()
        else:
            # Si la consulta no devuelve resultados, mostrar un mensaje de error
            QMessageBox.warning(self, "Error", "Usuario o clave incorrectos.")

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
      

        # Instanciar ventanas
        self.ventana_gestionusu = Ui_QMainwindow_Gestion_de_usuarios(QMainWindow)
        self.ventana_ingresarven = Ui_QMainwindow_Ingresar_ventas(QMainWindow)
        self.ventana_report = Ui_QMainwindow_Reportes(QMainWindow)
        self.ventana_ajustes = Ui_QMainwindow_Ajustes_anadir_eliminar(QMainWindow)
       

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

    def salir(self):
        self.close()
        # Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.

class Ui_QMainwindow_Gestion_de_usuarios(QMainWindow): #clase creada para la ventana de gestion de usuarios 
    
    def __init__(self, ventana_gestiondeusuarios):
        super().__init__()
        loadUi("4.Gestion_de_usuarios.ui", self)
        # Carga la interfaz de usuario desde el archivo

        self.pushButton_regresar_gestion.clicked.connect(self.salir)
        # Crear una instancia de la ventana de gestion de usuarios
        self.ventana_gestiondeusu = ventana_gestiondeusuarios

        
        # Conexiones de los botones a sus respectivos métodos para mostrar páginas
        self.pushButton_usuarios.clicked.connect(self.mostrar_pagina_usuarios)
        self.pushButton_anadir.clicked.connect(self.mostrar_pagina_anadir)
        self.pushButton_eliminar.clicked.connect(self.mostrar_pagina_eliminar)
        self.pushButton_actualizar.clicked.connect(self.mostrar_pagina_actualizar)
      
    # Metodos para mostrar las paginas
    def mostrar_pagina_usuarios(self):
       self.stackedWidget.setCurrentIndex(0)
    def mostrar_pagina_actualizar(self):
        self.stackedWidget.setCurrentIndex(1)
    def mostrar_pagina_eliminar(self):
        self.stackedWidget.setCurrentIndex(2)    
    def mostrar_pagina_anadir(self):
        self.stackedWidget.setCurrentIndex(3)
             

    def salir(self):
        self.close()
        # Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.

class Ui_QMainwindow_Ingresar_ventas(QMainWindow): #clase creada para la ventana de ingresar ventas 
    
    def __init__(self, ventana_ingresarventas):
        super().__init__()
        loadUi("5.Ingresar_ventas.ui", self)
        # Carga la interfaz de usuario desde el archivo
        self.pushButton_regresar_iv.clicked.connect(self.salir)
        # Crear una instancia de la ventana de ingresar ventas
        self.ventana_ingresarventas = ventana_ingresarventas

    def salir(self):
        self.close()
        # Cierra la ventana actual. Este método es llamado cuando se hace clic en el botón 'regresar' en la interfaz gráfica. Cierra la ventana actual.    

class Ui_QMainwindow_Reportes(QMainWindow): #clase creada para la ventana de Reportes 
    
    def __init__(self, ventana_report):
        super().__init__()
        loadUi("6.Reportes.ui", self)
        # Carga la interfaz de usuario desde el archivo

        # Conectar botones a funciones
        self.pushButton_regresar_rep.clicked.connect(self.salir)
        # Crear una instancia de la ventana de Reportes
        self.ventana_report = ventana_report

        # Conexiones de los botones a sus respectivos métodos para mostrar páginas
        self.pushButton_stock.clicked.connect(self.mostrar_pagina_stock)
        self.pushButton_Ventas.clicked.connect(self.mostrar_pagina_ventas)
        
      
    # Metodos para mostrar las paginas
    def mostrar_pagina_stock(self):
       self.stackedWidget.setCurrentIndex(0)
    def mostrar_pagina_ventas(self):
        self.stackedWidget.setCurrentIndex(1)
    

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Punto de entrada principal de la aplicación.
    ventana = Ui_ventana_inicio()
    ventana.showFullScreen() 
    # Instanciar y mostrar la ventana de inicio en pantalla completa
    sys.exit(app.exec_())
    # Ejecutar la aplicación hasta que se cierre la ventana principal
