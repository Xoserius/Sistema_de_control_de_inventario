# Form implementation generated from reading ui file 'c:\Users\User\OneDrive\Tesis TSU Informatica\Sistema de control de inventario\Qt designer\5.Ingresar_ventas.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_ingresarventa(object):
    def setupUi(self, MainWindow_ingresarventa):
        MainWindow_ingresarventa.setObjectName("MainWindow_ingresarventa")
        MainWindow_ingresarventa.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_ingresarventa)
        self.centralwidget.setMinimumSize(QtCore.QSize(1080, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_fondo = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_fondo.setStyleSheet("background-color: rgb(22, 22, 20);")
        self.frame_fondo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fondo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fondo.setObjectName("frame_fondo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_fondo)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(parent=self.frame_fondo)
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 50))
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
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(245, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButton_regresar_iv = QtWidgets.QPushButton(parent=self.frame_superior)
        self.pushButton_regresar_iv.setMinimumSize(QtCore.QSize(126, 30))
        self.pushButton_regresar_iv.setStyleSheet("QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.727273 rgba(142, 19, 16, 255));\n"
"border-radius:10px;\n"
"font: 12pt \"Sans Serif\";\n"
"color: rgb(255, 255, 254);\n"
"}")
        self.pushButton_regresar_iv.setObjectName("pushButton_regresar_iv")
        self.horizontalLayout_6.addWidget(self.pushButton_regresar_iv)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_inferior = QtWidgets.QFrame(parent=self.frame_fondo)
        self.frame_inferior.setStyleSheet("\n"
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
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(351, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.frame_busquedadeusuarios_4 = QtWidgets.QFrame(parent=self.frame_inferior)
        self.frame_busquedadeusuarios_4.setMinimumSize(QtCore.QSize(369, 606))
        self.frame_busquedadeusuarios_4.setMaximumSize(QtCore.QSize(369, 670))
        self.frame_busquedadeusuarios_4.setStyleSheet("QLineEdit{\n"
"background-color: rgb(22, 22, 26);\n"
"border-radius: 10px;\n"
"font: 12pt \"SansSerif\";\n"
"color: rgb(255, 255, 254);\n"
"border: 2px solid rgb(114, 117, 126);}\n"
"\n"
"QLineEdit:hover{\n"
"background-color: rgb(22, 22, 26);\n"
"border-radius: 10px;\n"
"font: 12pt \"Sans Serif\";\n"
"border: 2px solid rgb(44, 182, 125); }\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(1, 1, 1);\n"
"border-radius:10px;\n"
"font: 12pt \"Sans Serif\";\n"
"border: 2px solid rgb(127, 90, 240);\n"
"}\n"
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
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(22, 22, 26);\n"
"border-radius: 10px;\n"
"font: 12pt \"SansSerif\";\n"
"color: rgb(255, 255, 254);\n"
"border: 2px solid rgb(114, 117, 126);}\n"
"\n"
"QComboBox:hover{\n"
"background-color: rgb(22, 22, 26);\n"
"border-radius: 10px;\n"
"font: 12pt \"Sans Serif\";\n"
"border: 2px solid rgb(44, 182, 125); }\n"
"\n"
"QFrame{\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(84, 135, 255)\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_busquedadeusuarios_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_busquedadeusuarios_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_busquedadeusuarios_4.setObjectName("frame_busquedadeusuarios_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_busquedadeusuarios_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ingresarventa = QtWidgets.QLabel(parent=self.frame_busquedadeusuarios_4)
        self.label_ingresarventa.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        self.label_ingresarventa.setFont(font)
        self.label_ingresarventa.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 0px;\n"
"\n"
"border:0px;")
        self.label_ingresarventa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ingresarventa.setObjectName("label_ingresarventa")
        self.verticalLayout_3.addWidget(self.label_ingresarventa)
        self.lineEdit_sku_ingresarventa = QtWidgets.QLineEdit(parent=self.frame_busquedadeusuarios_4)
        self.lineEdit_sku_ingresarventa.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_sku_ingresarventa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_sku_ingresarventa.setObjectName("lineEdit_sku_ingresarventa")
        self.verticalLayout_3.addWidget(self.lineEdit_sku_ingresarventa)
        self.pushButton_buscar_ingresarventa = QtWidgets.QPushButton(parent=self.frame_busquedadeusuarios_4)
        self.pushButton_buscar_ingresarventa.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_buscar_ingresarventa.setObjectName("pushButton_buscar_ingresarventa")
        self.verticalLayout_3.addWidget(self.pushButton_buscar_ingresarventa)
        self.lineEdit_descripicion_ingresarventa = QtWidgets.QLineEdit(parent=self.frame_busquedadeusuarios_4)
        self.lineEdit_descripicion_ingresarventa.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_descripicion_ingresarventa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_descripicion_ingresarventa.setObjectName("lineEdit_descripicion_ingresarventa")
        self.verticalLayout_3.addWidget(self.lineEdit_descripicion_ingresarventa)
        self.lineEdit_fecha_ingresarventa = QtWidgets.QLineEdit(parent=self.frame_busquedadeusuarios_4)
        self.lineEdit_fecha_ingresarventa.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_fecha_ingresarventa.setMaxLength(8)
        self.lineEdit_fecha_ingresarventa.setFrame(True)
        self.lineEdit_fecha_ingresarventa.setCursorPosition(8)
        self.lineEdit_fecha_ingresarventa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_fecha_ingresarventa.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_fecha_ingresarventa.setObjectName("lineEdit_fecha_ingresarventa")
        self.verticalLayout_3.addWidget(self.lineEdit_fecha_ingresarventa)
        self.lineEdit_cod_ingresarventa = QtWidgets.QLineEdit(parent=self.frame_busquedadeusuarios_4)
        self.lineEdit_cod_ingresarventa.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_cod_ingresarventa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_cod_ingresarventa.setObjectName("lineEdit_cod_ingresarventa")
        self.verticalLayout_3.addWidget(self.lineEdit_cod_ingresarventa)
        self.lineEdit_cant_ingresarventa = QtWidgets.QLineEdit(parent=self.frame_busquedadeusuarios_4)
        self.lineEdit_cant_ingresarventa.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_cant_ingresarventa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_cant_ingresarventa.setObjectName("lineEdit_cant_ingresarventa")
        self.verticalLayout_3.addWidget(self.lineEdit_cant_ingresarventa)
        self.pushButton_enviar = QtWidgets.QPushButton(parent=self.frame_busquedadeusuarios_4)
        self.pushButton_enviar.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_enviar.setObjectName("pushButton_enviar")
        self.verticalLayout_3.addWidget(self.pushButton_enviar)
        self.pushButton_limpiar = QtWidgets.QPushButton(parent=self.frame_busquedadeusuarios_4)
        self.pushButton_limpiar.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_limpiar.setStyleSheet("QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.727273 rgba(142, 19, 16, 255));\n"
"border-radius:10px;\n"
"font: 12pt \"Sans Serif\";\n"
"color: rgb(255, 255, 254);\n"
"}")
        self.pushButton_limpiar.setObjectName("pushButton_limpiar")
        self.verticalLayout_3.addWidget(self.pushButton_limpiar)
        self.horizontalLayout_11.addWidget(self.frame_busquedadeusuarios_4)
        spacerItem2 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_inferior)
        self.verticalLayout.addWidget(self.frame_fondo)
        MainWindow_ingresarventa.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_ingresarventa)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_ingresarventa)

    def retranslateUi(self, MainWindow_ingresarventa):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_ingresarventa.setWindowTitle(_translate("MainWindow_ingresarventa", "MainWindow"))
        self.pushButton_regresar_iv.setText(_translate("MainWindow_ingresarventa", "Regresar"))
        self.label_ingresarventa.setText(_translate("MainWindow_ingresarventa", "INGRESAR VENTA"))
        self.lineEdit_sku_ingresarventa.setPlaceholderText(_translate("MainWindow_ingresarventa", "SKU"))
        self.pushButton_buscar_ingresarventa.setText(_translate("MainWindow_ingresarventa", "Buscar"))
        self.lineEdit_descripicion_ingresarventa.setPlaceholderText(_translate("MainWindow_ingresarventa", "Descripción"))
        self.lineEdit_fecha_ingresarventa.setInputMask(_translate("MainWindow_ingresarventa", "99/99/99;_"))
        self.lineEdit_fecha_ingresarventa.setText(_translate("MainWindow_ingresarventa", "//", "DD/MM/AA"))
        self.lineEdit_fecha_ingresarventa.setPlaceholderText(_translate("MainWindow_ingresarventa", "DD/MM/AA", "DD/MM/AA"))
        self.lineEdit_cod_ingresarventa.setPlaceholderText(_translate("MainWindow_ingresarventa", "Codigo de Producto"))
        self.lineEdit_cant_ingresarventa.setPlaceholderText(_translate("MainWindow_ingresarventa", "Cantidad"))
        self.pushButton_enviar.setText(_translate("MainWindow_ingresarventa", "Enviar"))
        self.pushButton_limpiar.setText(_translate("MainWindow_ingresarventa", "Limpiar"))
