# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"*{\n"
"	font-family: Agency FB;\n"
"	font-weight: bold;\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background: url(\"images/cafeteria.png\");\n"
"	\n"
"}\n"
"\n"
"#contenedor_principal{\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.846154 rgba(0, 0, 0, 190));\n"
"	border-radius: 1em;\n"
"}\n"
"\n"
"#LOGO{\n"
"	color: black;\n"
"}\n"
"\n"
"#widget_menu QPushButton, #widget_opciones QPushButton,#boton_registrar{\n"
"	color: #fff;\n"
"	border:none;\n"
"	border-left: 2px solid white;\n"
"	border-right: 2px solid white;\n"
"	padding: 0.1em 0.8em;\n"
"}\n"
"\n"
"#widget_menu QPushButton:hover, #widget_opciones QPushButton:hover,#boton_registrar:hover,#widget_menu QPushButton:focus, #widget_opciones QPushButton:focus,#boton_registrar:focus{\n"
"	color: #48e;\n"
"	border-color: #48e;\n"
"}\n"
"\n"
"#widget_menu QPushButton:pressed, #widget_opciones QPushButton:pressed,#boton_registrar:pressed{\n"
"	color: black;\n"
"	border-color: black;\n"
"}\n"
"\n"
"#stacked_widget QWidge"
                        "t{\n"
"	background: transparent;\n"
"	border: 2px solid #48e;\n"
"	border-radius: 0.5em;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contenedor_principal = QWidget(self.centralwidget)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.gridLayout = QGridLayout(self.contenedor_principal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_menu = QWidget(self.contenedor_principal)
        self.widget_menu.setObjectName(u"widget_menu")
        self.verticalLayout_2 = QVBoxLayout(self.widget_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.widget_menu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_6 = QPushButton(self.widget_menu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.widget_menu, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.widget_opciones = QWidget(self.contenedor_principal)
        self.widget_opciones.setObjectName(u"widget_opciones")
        self.horizontalLayout = QHBoxLayout(self.widget_opciones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.widget_opciones)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget_opciones)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.widget_opciones, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.contenedor_logo = QWidget(self.contenedor_principal)
        self.contenedor_logo.setObjectName(u"contenedor_logo")
        self.horizontalLayout_2 = QHBoxLayout(self.contenedor_logo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.LOGO = QLabel(self.contenedor_logo)
        self.LOGO.setObjectName(u"LOGO")
        self.LOGO.setMaximumSize(QSize(80, 80))
        self.LOGO.setPixmap(QPixmap(u"images/taza.png"))
        self.LOGO.setScaledContents(True)
        self.LOGO.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.LOGO)

        self.label = QLabel(self.contenedor_logo)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout.addWidget(self.contenedor_logo, 0, 0, 1, 1)

        self.stacked_widget = QStackedWidget(self.contenedor_principal)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setStyleSheet(u"QComboBox{\n"
"min-width: 1em;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding: 0em 0.2em;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover,QComboBox:focus,QComboBox:hover,QTextEdit:focus,QTextEdit:hover,QPushButton:focus,QPushButton:hover{\n"
"border-color: rgb(0, 255, 238);\n"
"}")
        self.widget_registrar_producto = QWidget()
        self.widget_registrar_producto.setObjectName(u"widget_registrar_producto")
        self.verticalLayout_5 = QVBoxLayout(self.widget_registrar_producto)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_nombre_producto = QLineEdit(self.widget_registrar_producto)
        self.line_nombre_producto.setObjectName(u"line_nombre_producto")
        self.line_nombre_producto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.line_nombre_producto)

        self.text_descripcion = QTextEdit(self.widget_registrar_producto)
        self.text_descripcion.setObjectName(u"text_descripcion")

        self.verticalLayout.addWidget(self.text_descripcion)

        self.double_precio = QDoubleSpinBox(self.widget_registrar_producto)
        self.double_precio.setObjectName(u"double_precio")
        self.double_precio.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_precio.setStyleSheet(u"padding-right:25px;")

        self.verticalLayout.addWidget(self.double_precio)

        self.boton_registrar_producto = QPushButton(self.widget_registrar_producto)
        self.boton_registrar_producto.setObjectName(u"boton_registrar_producto")
        self.boton_registrar_producto.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_registrar_producto.setStyleSheet(u"min-width:8em;")

        self.verticalLayout.addWidget(self.boton_registrar_producto, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.stacked_widget.addWidget(self.widget_registrar_producto)
        self.widget_registrar_cliente = QWidget()
        self.widget_registrar_cliente.setObjectName(u"widget_registrar_cliente")
        self.widget_registrar_cliente.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_registrar_cliente)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.boton_registrar = QPushButton(self.widget_registrar_cliente)
        self.boton_registrar.setObjectName(u"boton_registrar")

        self.gridLayout_2.addWidget(self.boton_registrar, 4, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_nombre = QLineEdit(self.widget_registrar_cliente)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_nombre, 1, 1, 1, 1)

        self.nacionalidad = QComboBox(self.widget_registrar_cliente)
        self.nacionalidad.addItem("")
        self.nacionalidad.addItem("")
        self.nacionalidad.setObjectName(u"nacionalidad")

        self.gridLayout_2.addWidget(self.nacionalidad, 0, 0, 1, 1)

        self.line_telefono = QLineEdit(self.widget_registrar_cliente)
        self.line_telefono.setObjectName(u"line_telefono")
        self.line_telefono.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_telefono, 2, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_apellido = QLineEdit(self.widget_registrar_cliente)
        self.line_apellido.setObjectName(u"line_apellido")
        self.line_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_apellido, 1, 2, 1, 1)

        self.line_cedula = QLineEdit(self.widget_registrar_cliente)
        self.line_cedula.setObjectName(u"line_cedula")
        self.line_cedula.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_cedula, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.text_direccion = QTextEdit(self.widget_registrar_cliente)
        self.text_direccion.setObjectName(u"text_direccion")
        self.text_direccion.setTabChangesFocus(True)

        self.gridLayout_2.addWidget(self.text_direccion, 3, 1, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.stacked_widget.addWidget(self.widget_registrar_cliente)
        self.widget_facturar = QWidget()
        self.widget_facturar.setObjectName(u"widget_facturar")
        self.verticalLayout_15 = QVBoxLayout(self.widget_facturar)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.boton_buscar_producto = QPushButton(self.widget_facturar)
        self.boton_buscar_producto.setObjectName(u"boton_buscar_producto")
        self.boton_buscar_producto.setStyleSheet(u"min-width: 8em;")

        self.gridLayout_3.addWidget(self.boton_buscar_producto, 2, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_cedula_facturar = QLineEdit(self.widget_facturar)
        self.line_cedula_facturar.setObjectName(u"line_cedula_facturar")

        self.gridLayout_3.addWidget(self.line_cedula_facturar, 0, 0, 1, 1)

        self.line_apellido_facturar = QLineEdit(self.widget_facturar)
        self.line_apellido_facturar.setObjectName(u"line_apellido_facturar")
        self.line_apellido_facturar.setEnabled(False)
        self.line_apellido_facturar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.line_apellido_facturar, 1, 1, 1, 1)

        self.boton_buscar_cliente = QPushButton(self.widget_facturar)
        self.boton_buscar_cliente.setObjectName(u"boton_buscar_cliente")

        self.gridLayout_3.addWidget(self.boton_buscar_cliente, 0, 1, 1, 1)

        self.line_nombre_facturar = QLineEdit(self.widget_facturar)
        self.line_nombre_facturar.setObjectName(u"line_nombre_facturar")
        self.line_nombre_facturar.setEnabled(False)
        self.line_nombre_facturar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.line_nombre_facturar, 1, 0, 1, 1)

        self.list_productos = QListWidget(self.widget_facturar)
        self.list_productos.setObjectName(u"list_productos")

        self.gridLayout_3.addWidget(self.list_productos, 3, 0, 1, 2)

        self.boton_facturar = QPushButton(self.widget_facturar)
        self.boton_facturar.setObjectName(u"boton_facturar")
        self.boton_facturar.setStyleSheet(u"min-width: 8em;")

        self.gridLayout_3.addWidget(self.boton_facturar, 4, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_15.addLayout(self.gridLayout_3)

        self.stacked_widget.addWidget(self.widget_facturar)
        self.widget_productos = QWidget()
        self.widget_productos.setObjectName(u"widget_productos")
        self.widget_productos.setStyleSheet(u"#scroll_principal,#scroll_widget{\n"
"	border:none;\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_productos)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scroll_principal = QScrollArea(self.widget_productos)
        self.scroll_principal.setObjectName(u"scroll_principal")
        self.scroll_principal.setStyleSheet(u"")
        self.scroll_principal.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_widget.setGeometry(QRect(0, 0, 565, 1524))
        self.scroll_widget.setStyleSheet(u"#scroll_cafe,#scroll_te,#scroll_cerveza,#scroll_chocolate,#scroll_comida,#scroll_malteada,#scroll_pasteleria{\n"
"	border:none;\n"
"	min-height: 210px;\n"
"}\n"
"QFrame{\n"
"	border: none;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.scroll_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scroll_cafe = QScrollArea(self.scroll_widget)
        self.scroll_cafe.setObjectName(u"scroll_cafe")
        self.scroll_cafe.setMaximumSize(QSize(16777215, 16777215))
        self.scroll_cafe.setBaseSize(QSize(0, 0))
        self.scroll_cafe.setStyleSheet(u"")
        self.scroll_cafe.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 547, 210))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, -1, -1, -1)
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(80, 80))
        self.label_3.setPixmap(QPixmap(u"images/cafe.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_3)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_10.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(80, 80))
        self.label_11.setPixmap(QPixmap(u"images/cafe.png"))
        self.label_11.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(80, 80))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_13)


        self.horizontalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_10 = QVBoxLayout(self.widget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(80, 80))
        self.label_8.setPixmap(QPixmap(u"images/cafe.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(80, 80))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_10)


        self.horizontalLayout_10.addWidget(self.widget_4)


        self.horizontalLayout_7.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.scroll_cafe.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scroll_cafe)

        self.scroll_te = QScrollArea(self.scroll_widget)
        self.scroll_te.setObjectName(u"scroll_te")
        self.scroll_te.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 547, 210))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_5 = QWidget(self.frame_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(80, 80))
        self.label_14.setPixmap(QPixmap(u"images/te.png"))
        self.label_14.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_14)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(80, 80))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.horizontalLayout_11.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.frame_2)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_13 = QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_17 = QLabel(self.widget_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(80, 80))
        self.label_17.setPixmap(QPixmap(u"images/te.png"))
        self.label_17.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(80, 80))
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_19)


        self.horizontalLayout_11.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.frame_2)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_14 = QVBoxLayout(self.widget_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_20 = QLabel(self.widget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(80, 80))
        self.label_20.setPixmap(QPixmap(u"images/te.png"))
        self.label_20.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.label_20)

        self.label_21 = QLabel(self.widget_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(80, 80))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_21)

        self.label_22 = QLabel(self.widget_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_22)


        self.horizontalLayout_11.addWidget(self.widget_7)


        self.horizontalLayout_6.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.scroll_te.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scroll_te)

        self.scroll_malteada = QScrollArea(self.scroll_widget)
        self.scroll_malteada.setObjectName(u"scroll_malteada")
        self.scroll_malteada.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 547, 210))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scroll_malteada.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_6.addWidget(self.scroll_malteada)

        self.scroll_cerveza = QScrollArea(self.scroll_widget)
        self.scroll_cerveza.setObjectName(u"scroll_cerveza")
        self.scroll_cerveza.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 547, 210))
        self.scrollAreaWidgetContents_7.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scroll_cerveza.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_6.addWidget(self.scroll_cerveza)

        self.scroll_pasteleria = QScrollArea(self.scroll_widget)
        self.scroll_pasteleria.setObjectName(u"scroll_pasteleria")
        self.scroll_pasteleria.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 547, 210))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scroll_pasteleria.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_6.addWidget(self.scroll_pasteleria)

        self.scroll_chocolate = QScrollArea(self.scroll_widget)
        self.scroll_chocolate.setObjectName(u"scroll_chocolate")
        self.scroll_chocolate.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 547, 210))
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scroll_chocolate.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_6.addWidget(self.scroll_chocolate)

        self.scroll_comida = QScrollArea(self.scroll_widget)
        self.scroll_comida.setObjectName(u"scroll_comida")
        self.scroll_comida.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 547, 210))
        self.horizontalLayout_9 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.scroll_comida.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_6.addWidget(self.scroll_comida)

        self.scroll_principal.setWidget(self.scroll_widget)

        self.verticalLayout_7.addWidget(self.scroll_principal)

        self.stacked_widget.addWidget(self.widget_productos)

        self.gridLayout.addWidget(self.stacked_widget, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.contenedor_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.nacionalidad)
        QWidget.setTabOrder(self.nacionalidad, self.line_cedula)
        QWidget.setTabOrder(self.line_cedula, self.line_nombre)
        QWidget.setTabOrder(self.line_nombre, self.line_apellido)
        QWidget.setTabOrder(self.line_apellido, self.line_telefono)
        QWidget.setTabOrder(self.line_telefono, self.text_direccion)
        QWidget.setTabOrder(self.text_direccion, self.boton_registrar)
        QWidget.setTabOrder(self.boton_registrar, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"FACTURA", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"PRODUCTOS", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"CLIENTES", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESI\u00d3N", None))
        self.LOGO.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"BLUM CAFE", None))
        self.line_nombre_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL PRODUCTO", None))
        self.text_descripcion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DESCRIPCION", None))
        self.boton_registrar_producto.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR PRODUCTO", None))
        self.boton_registrar.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRES", None))
        self.nacionalidad.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.nacionalidad.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.line_telefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONO", None))
        self.line_apellido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDOS", None))
        self.line_cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.text_direccion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECCI\u00d3N", None))
        self.boton_buscar_producto.setText(QCoreApplication.translate("MainWindow", u"BUSCAR PRODUCTO", None))
        self.line_cedula_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.line_apellido_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.boton_buscar_cliente.setText(QCoreApplication.translate("MainWindow", u"BUSCAR CLIENTE", None))
        self.line_nombre_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.boton_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
    # retranslateUi

