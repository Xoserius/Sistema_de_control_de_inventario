# Form implementation generated from reading ui file 'c:\Users\User\OneDrive\Tesis TSU Informatica\Sistema de control de inventario\Qt designer\3.Menu_principal.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_menuprincipa(object):
    def setupUi(self, MainWindow_menuprincipa):
        MainWindow_menuprincipa.setObjectName("MainWindow_menuprincipa")
        MainWindow_menuprincipa.resize(1080, 1047)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_menuprincipa)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_fondo = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_fondo.setStyleSheet("background-color: rgb(22, 22, 26);")
        self.frame_fondo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fondo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fondo.setObjectName("frame_fondo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_fondo)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(parent=self.frame_fondo)
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_superior.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:1, y2:0.5, stop:0 rgba(11, 38, 67, 184), stop: 1 rgba(150, 88, 240, 255));\n"
"border-radius: 10px;\n"
"font: 12pt \"Sans Serif\";\n"
"color: rgb(255, 255, 254); }\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, stop: 0 rgba(11, 38, 67, 184), stop:1 rgba(88, 240, 171, 255));\n"
"border-radius:10px;\n"
"font: 12pt \"Sans Serif\";\n"
"color: rgb(255, 255, 254);\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_productos = QtWidgets.QPushButton(parent=self.frame_superior)
        self.pushButton_productos.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_productos.setObjectName("pushButton_productos")
        self.horizontalLayout.addWidget(self.pushButton_productos)
        self.pushButton_Inventario = QtWidgets.QPushButton(parent=self.frame_superior)
        self.pushButton_Inventario.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_Inventario.setObjectName("pushButton_Inventario")
        self.horizontalLayout.addWidget(self.pushButton_Inventario)
        self.pushButton_reportes = QtWidgets.QPushButton(parent=self.frame_superior)
        self.pushButton_reportes.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_reportes.setObjectName("pushButton_reportes")
        self.horizontalLayout.addWidget(self.pushButton_reportes)
        self.pushButton_gestiondeusuario = QtWidgets.QPushButton(parent=self.frame_superior)
        self.pushButton_gestiondeusuario.setMinimumSize(QtCore.QSize(160, 30))
        self.pushButton_gestiondeusuario.setObjectName("pushButton_gestiondeusuario")
        self.horizontalLayout.addWidget(self.pushButton_gestiondeusuario)
        self.pushButton_soporte = QtWidgets.QPushButton(parent=self.frame_superior)
        self.pushButton_soporte.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_soporte.setObjectName("pushButton_soporte")
        self.horizontalLayout.addWidget(self.pushButton_soporte)
        spacerItem = QtWidgets.QSpacerItem(207, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_salir_menu = QtWidgets.QPushButton(parent=self.frame_superior)
        self.pushButton_salir_menu.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_salir_menu.setStyleSheet("QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.727273 rgba(142, 19, 16, 255));\n"
"border-radius:10px;\n"
"font: 12pt \"Sans Serif\";\n"
"color: rgb(255, 255, 254);\n"
"}")
        self.pushButton_salir_menu.setObjectName("pushButton_salir_menu")
        self.horizontalLayout.addWidget(self.pushButton_salir_menu)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_inferior = QtWidgets.QFrame(parent=self.frame_fondo)
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.label = QtWidgets.QLabel(parent=self.frame_inferior)
        self.label.setGeometry(QtCore.QRect(80, 0, 1201, 661))
        self.label.setWhatsThis("")
        self.label.setStyleSheet("image: url(:/Producto/LOGO_POTRO.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_inferior)
        self.label_2.setGeometry(QtCore.QRect(480, 640, 421, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial Rounded MT Bold\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.frame_inferior)
        self.verticalLayout.addWidget(self.frame_fondo)
        MainWindow_menuprincipa.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_menuprincipa)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_menuprincipa)

    def retranslateUi(self, MainWindow_menuprincipa):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_menuprincipa.setWindowTitle(_translate("MainWindow_menuprincipa", "Menu Principal"))
        self.pushButton_productos.setText(_translate("MainWindow_menuprincipa", "Productos"))
        self.pushButton_Inventario.setText(_translate("MainWindow_menuprincipa", "Inventario"))
        self.pushButton_reportes.setText(_translate("MainWindow_menuprincipa", "Reportes"))
        self.pushButton_gestiondeusuario.setText(_translate("MainWindow_menuprincipa", "Gestion de Usuario"))
        self.pushButton_soporte.setText(_translate("MainWindow_menuprincipa", "Soporte"))
        self.pushButton_salir_menu.setText(_translate("MainWindow_menuprincipa", "Salir"))
        self.label_2.setText(_translate("MainWindow_menuprincipa", "2024 José Vásquez. Todos los derechos reservados"))
