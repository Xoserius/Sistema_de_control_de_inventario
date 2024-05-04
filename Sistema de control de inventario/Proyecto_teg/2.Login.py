import sys
from PyQt5.uic import loadUi

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5.QtGui import QPixmap


class Ui_Qdialog_login(QDialog):
    
    def __init__(self):
        super().__init__()

        # Cargar el archivo .ui
        loadUi("2.Login.ui", self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ui_Qdialog_login()
    ventana.show() # Muestra la ventana de inicio en pantalla completa
    sys.exit(app.exec_())