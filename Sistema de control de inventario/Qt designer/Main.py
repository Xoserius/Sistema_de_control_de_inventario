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

    def salir(self):
        # Cerrar la conexión a la base de datos antes de salir
        self.conexion_db.close()
        self.close()

    def abrir_ventana_login(self):
        # Mostrar la ventana de inicio de sesión
        self.ventana_login = Ui_Qdialog_login(self.conexion_db)
        self.ventana_login.show()

class Ui_Qdialog_login(QDialog):
    
    def __init__(self, conexion_db):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("2.Login.ui", self)

        self.conexion_db = conexion_db

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
            ventana_menu_principal = Ui_QMainwindow_Menu_principal()
            ventana_menu_principal.show()
        else:
            # Si la consulta no devuelve resultados, mostrar un mensaje de error
            QMessageBox.warning(self, "Error", "Usuario o clave incorrectos.")

class Ui_QMainwindow_Menu_principal(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui
        loadUi("3.Menu_principal.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ui_ventana_inicio()
    ventana.showFullScreen() # Muestra la ventana de inicio en pantalla completa
    sys.exit(app.exec_())

