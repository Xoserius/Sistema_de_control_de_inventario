import sys
from PyQt5.uic import loadUi
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5.QtGui import QPixmap


class Ui_Qmainwindow_Ajustes(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # Cargar el archivo .ui
        loadUi("7.Ajustes_anadir_eliminar.ui", self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ui_Qmainwindow_Ajustes()
    ventana.showFullScreen() # Muestra la ventana de inicio en pantalla completa
    sys.exit(app.exec_())