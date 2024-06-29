# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"images/redondo_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	font-family: Agency FB;\n"
"	font-weight: bold;\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background: url(\"images/cafe.png\");\n"
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
"#stacked_widget QWidget{\n"
"	ba"
                        "ckground: transparent;\n"
"}\n"
"\n"
"#stacked_widget{\n"
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
        self.boton_v_facturar = QPushButton(self.widget_menu)
        self.boton_v_facturar.setObjectName(u"boton_v_facturar")
        self.boton_v_facturar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.boton_v_facturar.setTabletTracking(False)

        self.verticalLayout_2.addWidget(self.boton_v_facturar)

        self.boton_v_productos = QPushButton(self.widget_menu)
        self.boton_v_productos.setObjectName(u"boton_v_productos")
        self.boton_v_productos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.boton_v_productos.setTabletTracking(False)

        self.verticalLayout_2.addWidget(self.boton_v_productos)

        self.boton_v_registrar_cliente = QPushButton(self.widget_menu)
        self.boton_v_registrar_cliente.setObjectName(u"boton_v_registrar_cliente")
        self.boton_v_registrar_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.boton_v_registrar_cliente)

        self.boton_v_registrar_producto = QPushButton(self.widget_menu)
        self.boton_v_registrar_producto.setObjectName(u"boton_v_registrar_producto")
        self.boton_v_registrar_producto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.boton_v_registrar_producto)

        self.boton_v_editar_clientes = QPushButton(self.widget_menu)
        self.boton_v_editar_clientes.setObjectName(u"boton_v_editar_clientes")

        self.verticalLayout_2.addWidget(self.boton_v_editar_clientes)

        self.boton_v_editar_facturas = QPushButton(self.widget_menu)
        self.boton_v_editar_facturas.setObjectName(u"boton_v_editar_facturas")

        self.verticalLayout_2.addWidget(self.boton_v_editar_facturas)


        self.gridLayout.addWidget(self.widget_menu, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.widget_opciones = QWidget(self.contenedor_principal)
        self.widget_opciones.setObjectName(u"widget_opciones")
        self.horizontalLayout = QHBoxLayout(self.widget_opciones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boton_v_cierre = QPushButton(self.widget_opciones)
        self.boton_v_cierre.setObjectName(u"boton_v_cierre")

        self.horizontalLayout.addWidget(self.boton_v_cierre)

        self.boton_v_divisas = QPushButton(self.widget_opciones)
        self.boton_v_divisas.setObjectName(u"boton_v_divisas")

        self.horizontalLayout.addWidget(self.boton_v_divisas)

        self.boton_v_configuracion = QPushButton(self.widget_opciones)
        self.boton_v_configuracion.setObjectName(u"boton_v_configuracion")
        self.boton_v_configuracion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_configuracion)

        self.boton_cerrar_sesion = QPushButton(self.widget_opciones)
        self.boton_cerrar_sesion.setObjectName(u"boton_cerrar_sesion")
        self.boton_cerrar_sesion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_cerrar_sesion)


        self.gridLayout.addWidget(self.widget_opciones, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.contenedor_logo = QWidget(self.contenedor_principal)
        self.contenedor_logo.setObjectName(u"contenedor_logo")
        self.horizontalLayout_2 = QHBoxLayout(self.contenedor_logo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.LOGO = QLabel(self.contenedor_logo)
        self.LOGO.setObjectName(u"LOGO")
        self.LOGO.setMaximumSize(QSize(80, 80))
        self.LOGO.setPixmap(QPixmap(u"images/redondo_white.png"))
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
"border: 2px solid #48e;\n"
"border-radius: 0.5em;\n"
"\n"
"}\n"
"\n"
"QDoubleSpinBox,QSpinBox,QPushButton{\n"
"\n"
"	border: 2px solid #48e;\n"
"	border-radius: 0.5em;\n"
"}\n"
"\n"
"QDoubleSpinBox,QSpinBox{\n"
"padding-right: 2em;\n"
"}\n"
"\n"
"QLineEdit,QTextEdit{\n"
"	padding: 0em 0.2em;\n"
"\n"
"	border: 2px solid #48e;\n"
"	border-radius: 0.5em;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover,QComboBox:focus,QComboBox:hover,QTextEdit:focus,QTextEdit:hover,QPushButton:focus,QPushButton:hover{\n"
"border-color: rgb(0, 255, 238);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	border: 2px solid #48e;\n"
"border-radius: 0.5em;\n"
"}\n"
"QTableWidget QTableWidgetItem{\n"
"	border: 2px solid #48e;\n"
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
        self.text_descripcion.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.text_descripcion)

        self.combo_categoria = QComboBox(self.widget_registrar_producto)
        icon1 = QIcon()
        icon1.addFile(u"images/coffee.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_categoria.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u"images/te.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_categoria.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u"images/cerveza.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_categoria.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u"images/sandwich.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_categoria.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u"images/pastel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_categoria.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u"images/chocolate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_categoria.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u"images/batido.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_categoria.addItem(icon7, "")
        self.combo_categoria.setObjectName(u"combo_categoria")

        self.verticalLayout.addWidget(self.combo_categoria)

        self.double_precio = QDoubleSpinBox(self.widget_registrar_producto)
        self.double_precio.setObjectName(u"double_precio")
        self.double_precio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.double_precio.setStyleSheet(u"padding-right:25px;")

        self.verticalLayout.addWidget(self.double_precio)

        self.boton_registrar_producto = QPushButton(self.widget_registrar_producto)
        self.boton_registrar_producto.setObjectName(u"boton_registrar_producto")
        self.boton_registrar_producto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.line_nombre = QLineEdit(self.widget_registrar_cliente)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_nombre, 2, 0, 1, 1)

        self.line_cedula = QLineEdit(self.widget_registrar_cliente)
        self.line_cedula.setObjectName(u"line_cedula")
        self.line_cedula.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_cedula, 0, 1, 1, 1)

        self.nacionalidad = QComboBox(self.widget_registrar_cliente)
        self.nacionalidad.addItem("")
        self.nacionalidad.addItem("")
        self.nacionalidad.setObjectName(u"nacionalidad")

        self.gridLayout_2.addWidget(self.nacionalidad, 0, 0, 1, 1)

        self.boton_buscar = QPushButton(self.widget_registrar_cliente)
        self.boton_buscar.setObjectName(u"boton_buscar")

        self.gridLayout_2.addWidget(self.boton_buscar, 0, 2, 1, 1)

        self.line_apellido = QLineEdit(self.widget_registrar_cliente)
        self.line_apellido.setObjectName(u"line_apellido")
        self.line_apellido.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_apellido, 2, 2, 1, 1)

        self.line_telefono = QLineEdit(self.widget_registrar_cliente)
        self.line_telefono.setObjectName(u"line_telefono")
        self.line_telefono.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_telefono, 3, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.text_direccion = QTextEdit(self.widget_registrar_cliente)
        self.text_direccion.setObjectName(u"text_direccion")
        self.text_direccion.setTabChangesFocus(True)

        self.gridLayout_2.addWidget(self.text_direccion, 4, 0, 1, 3)

        self.boton_registrar = QPushButton(self.widget_registrar_cliente)
        self.boton_registrar.setObjectName(u"boton_registrar")

        self.gridLayout_2.addWidget(self.boton_registrar, 5, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.stacked_widget.addWidget(self.widget_registrar_cliente)
        self.widget_facturar = QWidget()
        self.widget_facturar.setObjectName(u"widget_facturar")
        self.verticalLayout_15 = QVBoxLayout(self.widget_facturar)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.boton_buscar_cliente_facturar = QPushButton(self.widget_facturar)
        self.boton_buscar_cliente_facturar.setObjectName(u"boton_buscar_cliente_facturar")
        self.boton_buscar_cliente_facturar.setStyleSheet(u"min-width: 6em;")

        self.gridLayout_5.addWidget(self.boton_buscar_cliente_facturar, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.label_total = QLabel(self.widget_facturar)
        self.label_total.setObjectName(u"label_total")

        self.gridLayout_5.addWidget(self.label_total, 4, 0, 1, 2)

        self.boton_buscar_producto_facturar = QPushButton(self.widget_facturar)
        self.boton_buscar_producto_facturar.setObjectName(u"boton_buscar_producto_facturar")
        self.boton_buscar_producto_facturar.setMinimumSize(QSize(140, 0))
        self.boton_buscar_producto_facturar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.boton_buscar_producto_facturar, 2, 1, 1, 1)

        self.line_cedula_facturar = QLineEdit(self.widget_facturar)
        self.line_cedula_facturar.setObjectName(u"line_cedula_facturar")

        self.gridLayout_5.addWidget(self.line_cedula_facturar, 0, 1, 1, 1)

        self.table_productos_facturar = QTableWidget(self.widget_facturar)
        if (self.table_productos_facturar.columnCount() < 5):
            self.table_productos_facturar.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_productos_facturar.setObjectName(u"table_productos_facturar")
        self.table_productos_facturar.setEnabled(True)
        self.table_productos_facturar.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_productos_facturar.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_productos_facturar.horizontalHeader().setCascadingSectionResizes(False)
        self.table_productos_facturar.horizontalHeader().setDefaultSectionSize(110)
        self.table_productos_facturar.horizontalHeader().setStretchLastSection(True)
        self.table_productos_facturar.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.table_productos_facturar, 3, 0, 1, 3)

        self.line_nombre_facturar = QLineEdit(self.widget_facturar)
        self.line_nombre_facturar.setObjectName(u"line_nombre_facturar")
        self.line_nombre_facturar.setEnabled(False)
        self.line_nombre_facturar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.line_nombre_facturar, 1, 0, 1, 1)

        self.boton_facturar = QPushButton(self.widget_facturar)
        self.boton_facturar.setObjectName(u"boton_facturar")
        self.boton_facturar.setMinimumSize(QSize(140, 0))
        self.boton_facturar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.boton_facturar, 8, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_cop_facturar = QLabel(self.widget_facturar)
        self.label_cop_facturar.setObjectName(u"label_cop_facturar")

        self.gridLayout_6.addWidget(self.label_cop_facturar, 1, 4, 1, 1)

        self.label_dolar = QLabel(self.widget_facturar)
        self.label_dolar.setObjectName(u"label_dolar")
        self.label_dolar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.label_dolar, 1, 1, 1, 1)

        self.label_dolar_facturar = QLabel(self.widget_facturar)
        self.label_dolar_facturar.setObjectName(u"label_dolar_facturar")

        self.gridLayout_6.addWidget(self.label_dolar_facturar, 1, 0, 1, 1)

        self.label_bs_facturar = QLabel(self.widget_facturar)
        self.label_bs_facturar.setObjectName(u"label_bs_facturar")

        self.gridLayout_6.addWidget(self.label_bs_facturar, 1, 2, 1, 1)

        self.double_dolares_facturar = QDoubleSpinBox(self.widget_facturar)
        self.double_dolares_facturar.setObjectName(u"double_dolares_facturar")
        self.double_dolares_facturar.setMaximum(999999999.990000009536743)

        self.gridLayout_6.addWidget(self.double_dolares_facturar, 0, 0, 1, 2)

        self.label_bs = QLabel(self.widget_facturar)
        self.label_bs.setObjectName(u"label_bs")
        self.label_bs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.label_bs, 1, 3, 1, 1)

        self.label_cop = QLabel(self.widget_facturar)
        self.label_cop.setObjectName(u"label_cop")
        self.label_cop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.label_cop, 1, 5, 1, 1)

        self.double_bs_facturar = QDoubleSpinBox(self.widget_facturar)
        self.double_bs_facturar.setObjectName(u"double_bs_facturar")
        self.double_bs_facturar.setMaximum(999999999.990000009536743)

        self.gridLayout_6.addWidget(self.double_bs_facturar, 0, 2, 1, 2)

        self.spin_cop_facturar = QSpinBox(self.widget_facturar)
        self.spin_cop_facturar.setObjectName(u"spin_cop_facturar")
        self.spin_cop_facturar.setMinimum(0)
        self.spin_cop_facturar.setMaximum(999999999)
        self.spin_cop_facturar.setSingleStep(1000)
        self.spin_cop_facturar.setDisplayIntegerBase(10)

        self.gridLayout_6.addWidget(self.spin_cop_facturar, 0, 4, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_6, 7, 0, 1, 3)

        self.line_apellido_facturar = QLineEdit(self.widget_facturar)
        self.line_apellido_facturar.setObjectName(u"line_apellido_facturar")
        self.line_apellido_facturar.setEnabled(False)
        self.line_apellido_facturar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.line_apellido_facturar, 1, 2, 1, 1)

        self.combo_nacionalidad_facturar = QComboBox(self.widget_facturar)
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.setObjectName(u"combo_nacionalidad_facturar")

        self.gridLayout_5.addWidget(self.combo_nacionalidad_facturar, 0, 0, 1, 1)

        self.label_total_iva = QLabel(self.widget_facturar)
        self.label_total_iva.setObjectName(u"label_total_iva")

        self.gridLayout_5.addWidget(self.label_total_iva, 5, 0, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_5)

        self.stacked_widget.addWidget(self.widget_facturar)
        self.widget_editar_clientes = QWidget()
        self.widget_editar_clientes.setObjectName(u"widget_editar_clientes")
        self.verticalLayout_8 = QVBoxLayout(self.widget_editar_clientes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.text_direccion_actualizar = QTextEdit(self.widget_editar_clientes)
        self.text_direccion_actualizar.setObjectName(u"text_direccion_actualizar")
        self.text_direccion_actualizar.setTabChangesFocus(True)

        self.gridLayout_3.addWidget(self.text_direccion_actualizar, 4, 0, 1, 3)

        self.line_cedula_actualizar = QLineEdit(self.widget_editar_clientes)
        self.line_cedula_actualizar.setObjectName(u"line_cedula_actualizar")
        self.line_cedula_actualizar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.line_cedula_actualizar, 0, 1, 1, 1)

        self.line_telefono_actualizar = QLineEdit(self.widget_editar_clientes)
        self.line_telefono_actualizar.setObjectName(u"line_telefono_actualizar")
        self.line_telefono_actualizar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.line_telefono_actualizar, 3, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.line_nombre_actualizar = QLineEdit(self.widget_editar_clientes)
        self.line_nombre_actualizar.setObjectName(u"line_nombre_actualizar")
        self.line_nombre_actualizar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.line_nombre_actualizar, 2, 0, 1, 1)

        self.nacionalidad_actualizar = QComboBox(self.widget_editar_clientes)
        self.nacionalidad_actualizar.addItem("")
        self.nacionalidad_actualizar.addItem("")
        self.nacionalidad_actualizar.setObjectName(u"nacionalidad_actualizar")

        self.gridLayout_3.addWidget(self.nacionalidad_actualizar, 0, 0, 1, 1)

        self.boton_buscar_actualizar = QPushButton(self.widget_editar_clientes)
        self.boton_buscar_actualizar.setObjectName(u"boton_buscar_actualizar")

        self.gridLayout_3.addWidget(self.boton_buscar_actualizar, 0, 2, 1, 1)

        self.line_apellido_actualizar = QLineEdit(self.widget_editar_clientes)
        self.line_apellido_actualizar.setObjectName(u"line_apellido_actualizar")
        self.line_apellido_actualizar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.line_apellido_actualizar, 2, 2, 1, 1)

        self.boton_actualizar = QPushButton(self.widget_editar_clientes)
        self.boton_actualizar.setObjectName(u"boton_actualizar")
        self.boton_actualizar.setStyleSheet(u"min-width: 6em;")

        self.gridLayout_3.addWidget(self.boton_actualizar, 5, 1, 1, 1)

        self.boton_borrar = QPushButton(self.widget_editar_clientes)
        self.boton_borrar.setObjectName(u"boton_borrar")

        self.gridLayout_3.addWidget(self.boton_borrar, 7, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_3)

        self.stacked_widget.addWidget(self.widget_editar_clientes)
        self.widget_cierre_diario = QWidget()
        self.widget_cierre_diario.setObjectName(u"widget_cierre_diario")
        self.verticalLayout_10 = QVBoxLayout(self.widget_cierre_diario)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.boton_buscar_cierre = QPushButton(self.widget_cierre_diario)
        self.boton_buscar_cierre.setObjectName(u"boton_buscar_cierre")

        self.gridLayout_8.addWidget(self.boton_buscar_cierre, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_cierre_diario)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_8.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.widget_cierre_diario)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_8.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_cierre_bs = QLabel(self.widget_cierre_diario)
        self.label_cierre_bs.setObjectName(u"label_cierre_bs")

        self.gridLayout_8.addWidget(self.label_cierre_bs, 3, 1, 1, 1)

        self.label_cierre_dolar = QLabel(self.widget_cierre_diario)
        self.label_cierre_dolar.setObjectName(u"label_cierre_dolar")

        self.gridLayout_8.addWidget(self.label_cierre_dolar, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget_cierre_diario)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-size: 28px;")

        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_cierre_cop = QLabel(self.widget_cierre_diario)
        self.label_cierre_cop.setObjectName(u"label_cierre_cop")

        self.gridLayout_8.addWidget(self.label_cierre_cop, 4, 1, 1, 1)

        self.boton_cierre = QPushButton(self.widget_cierre_diario)
        self.boton_cierre.setObjectName(u"boton_cierre")
        self.boton_cierre.setEnabled(False)
        self.boton_cierre.setStyleSheet(u"min-width: 8em;")

        self.gridLayout_8.addWidget(self.boton_cierre, 5, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_8 = QLabel(self.widget_cierre_diario)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 2, 0, 1, 1)

        self.date_cierre = QDateEdit(self.widget_cierre_diario)
        self.date_cierre.setObjectName(u"date_cierre")
        self.date_cierre.setStyleSheet(u"border: 2px solid #48e;\n"
"border-radius: 0.5em;")
        self.date_cierre.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(8, 0, 11)))
        self.date_cierre.setCalendarPopup(False)

        self.gridLayout_8.addWidget(self.date_cierre, 1, 0, 1, 1)

        self.boton_rehacer = QPushButton(self.widget_cierre_diario)
        self.boton_rehacer.setObjectName(u"boton_rehacer")
        self.boton_rehacer.setEnabled(False)
        self.boton_rehacer.setStyleSheet(u"min-width: 8em;")

        self.gridLayout_8.addWidget(self.boton_rehacer, 6, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_10.addLayout(self.gridLayout_8)

        self.stacked_widget.addWidget(self.widget_cierre_diario)
        self.widget_divisas = QWidget()
        self.widget_divisas.setObjectName(u"widget_divisas")
        self.verticalLayout_6 = QVBoxLayout(self.widget_divisas)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(14)
        self.gridLayout_7.setContentsMargins(-1, 16, -1, 16)
        self.combo_divisa_adivisa = QComboBox(self.widget_divisas)
        self.combo_divisa_adivisa.addItem("")
        self.combo_divisa_adivisa.addItem("")
        self.combo_divisa_adivisa.setObjectName(u"combo_divisa_adivisa")
        self.combo_divisa_adivisa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.combo_divisa_adivisa.setStyleSheet(u"min-width: 8em;")

        self.gridLayout_7.addWidget(self.combo_divisa_adivisa, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.widget_divisas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 22px;")

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.boton_actualizar_adivisa = QPushButton(self.widget_divisas)
        self.boton_actualizar_adivisa.setObjectName(u"boton_actualizar_adivisa")
        self.boton_actualizar_adivisa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.boton_actualizar_adivisa.setStyleSheet(u"min-width: 6em;")

        self.gridLayout_7.addWidget(self.boton_actualizar_adivisa, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.double_valor_adivisa = QDoubleSpinBox(self.widget_divisas)
        self.double_valor_adivisa.setObjectName(u"double_valor_adivisa")
        self.double_valor_adivisa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.double_valor_adivisa.setMaximum(9999999999.000000000000000)

        self.gridLayout_7.addWidget(self.double_valor_adivisa, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 4, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_7)

        self.stacked_widget.addWidget(self.widget_divisas)
        self.widget_configuracion = QWidget()
        self.widget_configuracion.setObjectName(u"widget_configuracion")
        self.widget_configuracion.setStyleSheet(u"min-width: 8em;")
        self.gridLayout_9 = QGridLayout(self.widget_configuracion)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.boton_registrar_usuarios = QPushButton(self.widget_configuracion)
        self.boton_registrar_usuarios.setObjectName(u"boton_registrar_usuarios")

        self.gridLayout_9.addWidget(self.boton_registrar_usuarios, 2, 1, 1, 1)

        self.boton_configurar_bd = QPushButton(self.widget_configuracion)
        self.boton_configurar_bd.setObjectName(u"boton_configurar_bd")

        self.gridLayout_9.addWidget(self.boton_configurar_bd, 1, 1, 1, 1)

        self.boton_actualizar_usuarios = QPushButton(self.widget_configuracion)
        self.boton_actualizar_usuarios.setObjectName(u"boton_actualizar_usuarios")

        self.gridLayout_9.addWidget(self.boton_actualizar_usuarios, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.stacked_widget.addWidget(self.widget_configuracion)
        self.widget_actualizar_usuarios = QWidget()
        self.widget_actualizar_usuarios.setObjectName(u"widget_actualizar_usuarios")
        self.verticalLayout_11 = QVBoxLayout(self.widget_actualizar_usuarios)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.line_contrasena_usuario = QLineEdit(self.widget_actualizar_usuarios)
        self.line_contrasena_usuario.setObjectName(u"line_contrasena_usuario")
        self.line_contrasena_usuario.setEnabled(False)
        self.line_contrasena_usuario.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_contrasena_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.line_contrasena_usuario, 1, 1, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.line_actualizar_usuario = QLineEdit(self.widget_actualizar_usuarios)
        self.line_actualizar_usuario.setObjectName(u"line_actualizar_usuario")
        self.line_actualizar_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.line_actualizar_usuario, 0, 1, 1, 1)

        self.boton_buscar_actualizar_usuario = QPushButton(self.widget_actualizar_usuarios)
        self.boton_buscar_actualizar_usuario.setObjectName(u"boton_buscar_actualizar_usuario")
        self.boton_buscar_actualizar_usuario.setStyleSheet(u"min-width:5em;")

        self.gridLayout_10.addWidget(self.boton_buscar_actualizar_usuario, 0, 2, 1, 1)

        self.boton_actulizar_usuario = QPushButton(self.widget_actualizar_usuarios)
        self.boton_actulizar_usuario.setObjectName(u"boton_actulizar_usuario")
        self.boton_actulizar_usuario.setEnabled(False)

        self.gridLayout_10.addWidget(self.boton_actulizar_usuario, 3, 1, 1, 2)

        self.line_confirmar_usuario = QLineEdit(self.widget_actualizar_usuarios)
        self.line_confirmar_usuario.setObjectName(u"line_confirmar_usuario")
        self.line_confirmar_usuario.setEnabled(False)
        self.line_confirmar_usuario.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_confirmar_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.line_confirmar_usuario, 2, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_10)

        self.stacked_widget.addWidget(self.widget_actualizar_usuarios)
        self.widget_editar_facturas = QWidget()
        self.widget_editar_facturas.setObjectName(u"widget_editar_facturas")
        self.verticalLayout_12 = QVBoxLayout(self.widget_editar_facturas)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.date_factura = QDateEdit(self.widget_editar_facturas)
        self.date_factura.setObjectName(u"date_factura")

        self.gridLayout_12.addWidget(self.date_factura, 0, 0, 1, 1)

        self.boton_buscar_factura = QPushButton(self.widget_editar_facturas)
        self.boton_buscar_factura.setObjectName(u"boton_buscar_factura")

        self.gridLayout_12.addWidget(self.boton_buscar_factura, 0, 1, 1, 1)

        self.table_facturas = QTableWidget(self.widget_editar_facturas)
        if (self.table_facturas.columnCount() < 6):
            self.table_facturas.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_facturas.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_facturas.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_facturas.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_facturas.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_facturas.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_facturas.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.table_facturas.setObjectName(u"table_facturas")
        self.table_facturas.setEnabled(True)
        self.table_facturas.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_facturas.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_facturas.horizontalHeader().setCascadingSectionResizes(False)
        self.table_facturas.horizontalHeader().setDefaultSectionSize(86)
        self.table_facturas.horizontalHeader().setStretchLastSection(True)
        self.table_facturas.verticalHeader().setVisible(False)

        self.gridLayout_12.addWidget(self.table_facturas, 1, 0, 1, 2)


        self.verticalLayout_12.addLayout(self.gridLayout_12)

        self.stacked_widget.addWidget(self.widget_editar_facturas)
        self.widget_actualizar_productos = QWidget()
        self.widget_actualizar_productos.setObjectName(u"widget_actualizar_productos")
        self.verticalLayout_16 = QVBoxLayout(self.widget_actualizar_productos)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.line_nombre_eproducto = QLineEdit(self.widget_actualizar_productos)
        self.line_nombre_eproducto.setObjectName(u"line_nombre_eproducto")
        self.line_nombre_eproducto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.line_nombre_eproducto)

        self.text_descripcion_eproducto = QTextEdit(self.widget_actualizar_productos)
        self.text_descripcion_eproducto.setObjectName(u"text_descripcion_eproducto")
        self.text_descripcion_eproducto.setTabletTracking(False)
        self.text_descripcion_eproducto.setTabChangesFocus(True)

        self.verticalLayout_9.addWidget(self.text_descripcion_eproducto)

        self.combo_eproducto = QComboBox(self.widget_actualizar_productos)
        self.combo_eproducto.addItem(icon1, "")
        self.combo_eproducto.addItem(icon2, "")
        self.combo_eproducto.addItem(icon3, "")
        self.combo_eproducto.addItem(icon4, "")
        self.combo_eproducto.addItem(icon5, "")
        self.combo_eproducto.addItem(icon6, "")
        self.combo_eproducto.addItem(icon7, "")
        self.combo_eproducto.setObjectName(u"combo_eproducto")

        self.verticalLayout_9.addWidget(self.combo_eproducto)

        self.double_precio_eproducto = QDoubleSpinBox(self.widget_actualizar_productos)
        self.double_precio_eproducto.setObjectName(u"double_precio_eproducto")
        self.double_precio_eproducto.setMaximum(9999999999.989999771118164)

        self.verticalLayout_9.addWidget(self.double_precio_eproducto)

        self.boton_actualizar_eproducto = QPushButton(self.widget_actualizar_productos)
        self.boton_actualizar_eproducto.setObjectName(u"boton_actualizar_eproducto")

        self.verticalLayout_9.addWidget(self.boton_actualizar_eproducto)

        self.boton_borrar_eproducto = QPushButton(self.widget_actualizar_productos)
        self.boton_borrar_eproducto.setObjectName(u"boton_borrar_eproducto")

        self.verticalLayout_9.addWidget(self.boton_borrar_eproducto)


        self.verticalLayout_16.addLayout(self.verticalLayout_9)

        self.stacked_widget.addWidget(self.widget_actualizar_productos)
        self.widget_productos = QWidget()
        self.widget_productos.setObjectName(u"widget_productos")
        self.widget_productos.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_productos)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line_nombre_bproducto = QLineEdit(self.widget_productos)
        self.line_nombre_bproducto.setObjectName(u"line_nombre_bproducto")

        self.gridLayout_4.addWidget(self.line_nombre_bproducto, 0, 1, 1, 1)

        self.combo_bproducto = QComboBox(self.widget_productos)
        icon8 = QIcon()
        icon8.addFile(u"images/alll.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_bproducto.addItem(icon8, "")
        self.combo_bproducto.addItem(icon1, "")
        self.combo_bproducto.addItem(icon2, "")
        self.combo_bproducto.addItem(icon3, "")
        self.combo_bproducto.addItem(icon4, "")
        self.combo_bproducto.addItem(icon5, "")
        self.combo_bproducto.addItem(icon6, "")
        self.combo_bproducto.addItem(icon7, "")
        self.combo_bproducto.setObjectName(u"combo_bproducto")
        self.combo_bproducto.setStyleSheet(u"min-width:4em;")

        self.gridLayout_4.addWidget(self.combo_bproducto, 0, 0, 1, 1)

        self.table_productos = QTableWidget(self.widget_productos)
        if (self.table_productos.columnCount() < 5):
            self.table_productos.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.table_productos.setObjectName(u"table_productos")
        self.table_productos.setStyleSheet(u"")
        self.table_productos.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_productos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_productos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.table_productos.setShowGrid(False)
        self.table_productos.setCornerButtonEnabled(True)
        self.table_productos.setRowCount(0)
        self.table_productos.horizontalHeader().setVisible(True)
        self.table_productos.horizontalHeader().setCascadingSectionResizes(False)
        self.table_productos.horizontalHeader().setMinimumSectionSize(61)
        self.table_productos.horizontalHeader().setDefaultSectionSize(100)
        self.table_productos.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_productos.horizontalHeader().setStretchLastSection(True)
        self.table_productos.verticalHeader().setVisible(False)
        self.table_productos.verticalHeader().setCascadingSectionResizes(False)
        self.table_productos.verticalHeader().setHighlightSections(True)

        self.gridLayout_4.addWidget(self.table_productos, 1, 0, 1, 2)


        self.verticalLayout_7.addLayout(self.gridLayout_4)

        self.stacked_widget.addWidget(self.widget_productos)

        self.gridLayout.addWidget(self.stacked_widget, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.contenedor_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.boton_v_facturar, self.boton_v_productos)
        QWidget.setTabOrder(self.boton_v_productos, self.boton_v_registrar_cliente)
        QWidget.setTabOrder(self.boton_v_registrar_cliente, self.boton_v_registrar_producto)
        QWidget.setTabOrder(self.boton_v_registrar_producto, self.boton_v_editar_clientes)
        QWidget.setTabOrder(self.boton_v_editar_clientes, self.boton_v_editar_facturas)
        QWidget.setTabOrder(self.boton_v_editar_facturas, self.boton_v_cierre)
        QWidget.setTabOrder(self.boton_v_cierre, self.boton_v_divisas)
        QWidget.setTabOrder(self.boton_v_divisas, self.boton_v_configuracion)
        QWidget.setTabOrder(self.boton_v_configuracion, self.boton_cerrar_sesion)
        QWidget.setTabOrder(self.boton_cerrar_sesion, self.line_nombre_eproducto)
        QWidget.setTabOrder(self.line_nombre_eproducto, self.text_descripcion_eproducto)
        QWidget.setTabOrder(self.text_descripcion_eproducto, self.combo_eproducto)
        QWidget.setTabOrder(self.combo_eproducto, self.double_precio_eproducto)
        QWidget.setTabOrder(self.double_precio_eproducto, self.boton_actualizar_eproducto)
        QWidget.setTabOrder(self.boton_actualizar_eproducto, self.boton_borrar_eproducto)
        QWidget.setTabOrder(self.boton_borrar_eproducto, self.line_actualizar_usuario)
        QWidget.setTabOrder(self.line_actualizar_usuario, self.boton_buscar_actualizar_usuario)
        QWidget.setTabOrder(self.boton_buscar_actualizar_usuario, self.line_contrasena_usuario)
        QWidget.setTabOrder(self.line_contrasena_usuario, self.line_confirmar_usuario)
        QWidget.setTabOrder(self.line_confirmar_usuario, self.boton_actulizar_usuario)
        QWidget.setTabOrder(self.boton_actulizar_usuario, self.date_cierre)
        QWidget.setTabOrder(self.date_cierre, self.boton_buscar_cierre)
        QWidget.setTabOrder(self.boton_buscar_cierre, self.boton_cierre)
        QWidget.setTabOrder(self.boton_cierre, self.boton_rehacer)
        QWidget.setTabOrder(self.boton_rehacer, self.boton_configurar_bd)
        QWidget.setTabOrder(self.boton_configurar_bd, self.boton_registrar_usuarios)
        QWidget.setTabOrder(self.boton_registrar_usuarios, self.boton_actualizar_usuarios)
        QWidget.setTabOrder(self.boton_actualizar_usuarios, self.combo_divisa_adivisa)
        QWidget.setTabOrder(self.combo_divisa_adivisa, self.double_valor_adivisa)
        QWidget.setTabOrder(self.double_valor_adivisa, self.boton_actualizar_adivisa)
        QWidget.setTabOrder(self.boton_actualizar_adivisa, self.nacionalidad_actualizar)
        QWidget.setTabOrder(self.nacionalidad_actualizar, self.line_cedula_actualizar)
        QWidget.setTabOrder(self.line_cedula_actualizar, self.boton_buscar_actualizar)
        QWidget.setTabOrder(self.boton_buscar_actualizar, self.line_nombre_actualizar)
        QWidget.setTabOrder(self.line_nombre_actualizar, self.line_apellido_actualizar)
        QWidget.setTabOrder(self.line_apellido_actualizar, self.line_telefono_actualizar)
        QWidget.setTabOrder(self.line_telefono_actualizar, self.text_direccion_actualizar)
        QWidget.setTabOrder(self.text_direccion_actualizar, self.boton_actualizar)
        QWidget.setTabOrder(self.boton_actualizar, self.boton_borrar)
        QWidget.setTabOrder(self.boton_borrar, self.combo_nacionalidad_facturar)
        QWidget.setTabOrder(self.combo_nacionalidad_facturar, self.line_cedula_facturar)
        QWidget.setTabOrder(self.line_cedula_facturar, self.boton_buscar_cliente_facturar)
        QWidget.setTabOrder(self.boton_buscar_cliente_facturar, self.line_nombre_facturar)
        QWidget.setTabOrder(self.line_nombre_facturar, self.line_apellido_facturar)
        QWidget.setTabOrder(self.line_apellido_facturar, self.boton_buscar_producto_facturar)
        QWidget.setTabOrder(self.boton_buscar_producto_facturar, self.table_productos_facturar)
        QWidget.setTabOrder(self.table_productos_facturar, self.double_dolares_facturar)
        QWidget.setTabOrder(self.double_dolares_facturar, self.double_bs_facturar)
        QWidget.setTabOrder(self.double_bs_facturar, self.spin_cop_facturar)
        QWidget.setTabOrder(self.spin_cop_facturar, self.boton_facturar)
        QWidget.setTabOrder(self.boton_facturar, self.combo_bproducto)
        QWidget.setTabOrder(self.combo_bproducto, self.line_nombre_bproducto)
        QWidget.setTabOrder(self.line_nombre_bproducto, self.table_productos)
        QWidget.setTabOrder(self.table_productos, self.nacionalidad)
        QWidget.setTabOrder(self.nacionalidad, self.line_cedula)
        QWidget.setTabOrder(self.line_cedula, self.boton_buscar)
        QWidget.setTabOrder(self.boton_buscar, self.line_nombre)
        QWidget.setTabOrder(self.line_nombre, self.line_apellido)
        QWidget.setTabOrder(self.line_apellido, self.line_telefono)
        QWidget.setTabOrder(self.line_telefono, self.text_direccion)
        QWidget.setTabOrder(self.text_direccion, self.boton_registrar)
        QWidget.setTabOrder(self.boton_registrar, self.line_nombre_producto)
        QWidget.setTabOrder(self.line_nombre_producto, self.text_descripcion)
        QWidget.setTabOrder(self.text_descripcion, self.combo_categoria)
        QWidget.setTabOrder(self.combo_categoria, self.double_precio)
        QWidget.setTabOrder(self.double_precio, self.boton_registrar_producto)
        QWidget.setTabOrder(self.boton_registrar_producto, self.date_factura)
        QWidget.setTabOrder(self.date_factura, self.boton_buscar_factura)
        QWidget.setTabOrder(self.boton_buscar_factura, self.table_facturas)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CAFE BLUM", None))
        self.boton_v_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
        self.boton_v_productos.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.boton_v_registrar_cliente.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"CLIENTES", None))
        self.boton_v_registrar_producto.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"PRODUCTOS", None))
        self.boton_v_editar_clientes.setText(QCoreApplication.translate("MainWindow", u"EDITAR\n"
"CLIENTES", None))
        self.boton_v_editar_facturas.setText(QCoreApplication.translate("MainWindow", u"VER\n"
"FACTURAS", None))
        self.boton_v_cierre.setText(QCoreApplication.translate("MainWindow", u"CIERRE", None))
        self.boton_v_divisas.setText(QCoreApplication.translate("MainWindow", u"DIVISAS", None))
        self.boton_v_configuracion.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.boton_cerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESI\u00d3N", None))
        self.LOGO.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"BLUM CAFE", None))
        self.line_nombre_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL PRODUCTO", None))
        self.text_descripcion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DESCRIPCION", None))
        self.combo_categoria.setItemText(0, QCoreApplication.translate("MainWindow", u"CAFE", None))
        self.combo_categoria.setItemText(1, QCoreApplication.translate("MainWindow", u"TE", None))
        self.combo_categoria.setItemText(2, QCoreApplication.translate("MainWindow", u"CERVEZA", None))
        self.combo_categoria.setItemText(3, QCoreApplication.translate("MainWindow", u"COMIDA", None))
        self.combo_categoria.setItemText(4, QCoreApplication.translate("MainWindow", u"PASTELERIA", None))
        self.combo_categoria.setItemText(5, QCoreApplication.translate("MainWindow", u"CHOCOLATE", None))
        self.combo_categoria.setItemText(6, QCoreApplication.translate("MainWindow", u"MALTEADAS", None))

        self.boton_registrar_producto.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR PRODUCTO", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRES", None))
        self.line_cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.nacionalidad.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.nacionalidad.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.boton_buscar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.line_apellido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDOS", None))
        self.line_telefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONO", None))
        self.text_direccion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECCI\u00d3N", None))
        self.boton_registrar.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.boton_buscar_cliente_facturar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"TOTAL EN DOLARES:", None))
        self.boton_buscar_producto_facturar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR PRODUCTO", None))
        self.line_cedula_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        ___qtablewidgetitem = self.table_productos_facturar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_productos_facturar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PRODUCTO", None));
        ___qtablewidgetitem2 = self.table_productos_facturar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        ___qtablewidgetitem3 = self.table_productos_facturar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD", None));
        ___qtablewidgetitem4 = self.table_productos_facturar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SUBTOTAL", None));
        self.line_nombre_facturar.setText("")
        self.line_nombre_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.boton_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
        self.label_cop_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor COP:", None))
        self.label_dolar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_dolar_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor $:", None))
        self.label_bs_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor BS:", None))
        self.label_bs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_apellido_facturar.setText("")
        self.line_apellido_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.combo_nacionalidad_facturar.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.combo_nacionalidad_facturar.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.label_total_iva.setText(QCoreApplication.translate("MainWindow", u"TOTAL + IVA:", None))
        self.text_direccion_actualizar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECCI\u00d3N", None))
        self.line_cedula_actualizar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.line_telefono_actualizar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONO", None))
        self.line_nombre_actualizar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRES", None))
        self.nacionalidad_actualizar.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.nacionalidad_actualizar.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.boton_buscar_actualizar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.line_apellido_actualizar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDOS", None))
        self.boton_actualizar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.boton_borrar.setText(QCoreApplication.translate("MainWindow", u"BORRAR", None))
        self.boton_buscar_cierre.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TOTAL BS:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TOTAL COP:", None))
        self.label_cierre_bs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cierre_dolar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cierre Diario", None))
        self.label_cierre_cop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.boton_cierre.setText(QCoreApplication.translate("MainWindow", u"REALIZAR CIERRE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TOTAL $:", None))
        self.boton_rehacer.setText(QCoreApplication.translate("MainWindow", u"REHACER CIERRE", None))
        self.combo_divisa_adivisa.setItemText(0, QCoreApplication.translate("MainWindow", u"BOLIVAR", None))
        self.combo_divisa_adivisa.setItemText(1, QCoreApplication.translate("MainWindow", u"COP", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR DIVISAS", None))
        self.boton_actualizar_adivisa.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.boton_registrar_usuarios.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR USUARIOS", None))
        self.boton_configurar_bd.setText(QCoreApplication.translate("MainWindow", u"CONFIGURAR BASE DE DATOS", None))
        self.boton_actualizar_usuarios.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR USUARIOS", None))
        self.line_contrasena_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A", None))
        self.line_actualizar_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"USUARIO", None))
        self.boton_buscar_actualizar_usuario.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.boton_actulizar_usuario.setText(QCoreApplication.translate("MainWindow", u"ACTULIZAR", None))
        self.line_confirmar_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CONFIRMAR CONTRASE\u00d1A", None))
        self.boton_buscar_factura.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem5 = self.table_facturas.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.table_facturas.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"CEDULA", None));
        ___qtablewidgetitem7 = self.table_facturas.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem8 = self.table_facturas.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"TOTAL BS", None));
        ___qtablewidgetitem9 = self.table_facturas.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TOTAL $", None));
        ___qtablewidgetitem10 = self.table_facturas.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TOTAL COP", None));
        self.line_nombre_eproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.text_descripcion_eproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DESCRIPCION PRODUCTO", None))
        self.combo_eproducto.setItemText(0, QCoreApplication.translate("MainWindow", u"CAFE", None))
        self.combo_eproducto.setItemText(1, QCoreApplication.translate("MainWindow", u"TE", None))
        self.combo_eproducto.setItemText(2, QCoreApplication.translate("MainWindow", u"CERVEZA", None))
        self.combo_eproducto.setItemText(3, QCoreApplication.translate("MainWindow", u"COMIDA", None))
        self.combo_eproducto.setItemText(4, QCoreApplication.translate("MainWindow", u"PASTELERIA", None))
        self.combo_eproducto.setItemText(5, QCoreApplication.translate("MainWindow", u"CHOCOLATE", None))
        self.combo_eproducto.setItemText(6, QCoreApplication.translate("MainWindow", u"MALTEADAS", None))

        self.boton_actualizar_eproducto.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.boton_borrar_eproducto.setText(QCoreApplication.translate("MainWindow", u"BORRAR PRODUCTO", None))
        self.line_nombre_bproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE PRODUCTO", None))
        self.combo_bproducto.setItemText(0, QCoreApplication.translate("MainWindow", u"TODO", None))
        self.combo_bproducto.setItemText(1, QCoreApplication.translate("MainWindow", u"CAFE", None))
        self.combo_bproducto.setItemText(2, QCoreApplication.translate("MainWindow", u"TE", None))
        self.combo_bproducto.setItemText(3, QCoreApplication.translate("MainWindow", u"CERVEZA", None))
        self.combo_bproducto.setItemText(4, QCoreApplication.translate("MainWindow", u"COMIDA", None))
        self.combo_bproducto.setItemText(5, QCoreApplication.translate("MainWindow", u"PASTELERIA", None))
        self.combo_bproducto.setItemText(6, QCoreApplication.translate("MainWindow", u"CHOCOLATE", None))
        self.combo_bproducto.setItemText(7, QCoreApplication.translate("MainWindow", u"MALTEADAS", None))

        ___qtablewidgetitem11 = self.table_productos.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.table_productos.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"PRODUCTO", None));
        ___qtablewidgetitem13 = self.table_productos.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"DESCRIPCION", None));
        ___qtablewidgetitem14 = self.table_productos.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        ___qtablewidgetitem15 = self.table_productos.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"CATEGORIA", None));
    # retranslateUi

