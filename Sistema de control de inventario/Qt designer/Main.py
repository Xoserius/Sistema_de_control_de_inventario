import sys
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox


class Ui_ventana_inicio(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # Cargar el archivo .ui
        loadUi("1.Inicio.ui", self)
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

class Ui_Qdialog_login(QDialog):
    
    def __init__(self, conexion_db, ventana_menu_principal):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("2.Login.ui", self)

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

class Ui_QMainwindow_Menu_principal(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("3.Menu_principal.ui", self)

        self.pushButton_salir_menu.clicked.connect(self.salir)
        self.pushButton_gestiondeusuario.clicked.connect(self.abrir_ventana_gestion)
        self.pushButton_ingresarventa.clicked.connect(self.abrir_ingresar_ventas)
        self.pushButton_reportes.clicked.connect(self.abrir_reportes)
        self.pushButton_anadir_eliminar.clicked.connect(self.abrir_ajustes)
      


        self.ventana_gestionusu = Ui_QMainwindow_Gestion_de_usuarios(QMainWindow)
        self.ventana_ingresarven = Ui_QMainwindow_Ingresar_ventas(QMainWindow)
        self.ventana_report = Ui_QMainwindow_Reportes(QMainWindow)
        self.ventana_ajustes = Ui_QMainwindow_Ajustes_anadir_eliminar(QMainWindow)
       

    def abrir_ventana_gestion(self):
        # Mostrar la ventana de inicio de sesión
        self.ventana_gestionusu = Ui_QMainwindow_Gestion_de_usuarios(self.ventana_gestionusu)
        self.ventana_gestionusu.show()

    def abrir_ingresar_ventas(self):
        # Mostrar la ventana de inicio de sesión
        self.ventana_ingresarven = Ui_QMainwindow_Ingresar_ventas(self.ventana_ingresarven)
        self.ventana_ingresarven.show()

    def abrir_reportes (self):
        # Mostrar la ventana de inicio de sesión
        self.ventana_report = Ui_QMainwindow_Reportes(self.ventana_report)
        self.ventana_report.show()
    
    def abrir_ajustes (self):# Mostrar la ventana de inicio de sesión
        self.ventana_ajustes = Ui_QMainwindow_Ajustes_anadir_eliminar(self.ventana_ajustes)
        self.ventana_ajustes.show()

    def salir(self):
        self.close()

class Ui_QMainwindow_Gestion_de_usuarios(QMainWindow):
    
    def __init__(self, ventana_gestiondeusuarios):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("4.Gestion_de_usuarios.ui", self)

        self.ventana_gestiondeusu = ventana_gestiondeusuarios


class Ui_QMainwindow_Ingresar_ventas(QMainWindow):
    
    def __init__(self, ventana_ingresarventas):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("5.Ingresar_ventas.ui", self)
        self.ventana_ingresarventas = ventana_ingresarventas

class Ui_QMainwindow_Reportes(QMainWindow):
    
    def __init__(self, ventana_report):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("6.Reportes.ui", self)
        self.ventana_report = ventana_report

class Ui_QMainwindow_Ajustes_anadir_eliminar(QMainWindow):
    
    def __init__(self, ventana_ajustes):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("7.Ajustes_anadir_eliminar.ui", self)
        self.ventana_ajustes = ventana_ajustes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ui_ventana_inicio()
    ventana.showFullScreen() # Muestra la ventana de inicio en pantalla completa
    sys.exit(app.exec_())
