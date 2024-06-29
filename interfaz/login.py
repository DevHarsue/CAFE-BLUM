# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(800, 600)
        Login.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"images/redondo_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(u"*{\n"
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
"QComboBox{\n"
"min-width: 1em;\n"
""
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
"	background: transparent;\n"
"	border: 2px solid #48e;\n"
"	border-radius: 0.5em;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover,QComboBox:focus,QComboBox:hover,QTextEdit:focus,QTextEdit:hover,QPushButton:focus,QPushButton:hover{\n"
"border-color: rgb(0, 255, 238);\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contenedor_principal = QWidget(self.centralwidget)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.gridLayout_2 = QGridLayout(self.contenedor_principal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(30)
        self.lineEdit_2 = QLineEdit(self.contenedor_principal)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)

        self.label = QLabel(self.contenedor_principal)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:28px;")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.contenedor_principal)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.contenedor_principal)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.contenedor_principal)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"min-width: 8em;")

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.contenedor_principal)

        Login.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"LOGIN", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"CONTRASE\u00d1A", None))
        self.label.setText(QCoreApplication.translate("Login", u"INICIO DE SESI\u00d3N", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"USUARIO", None))
        self.pushButton.setText(QCoreApplication.translate("Login", u"INICIAR SESI\u00d3N", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"SALIR", None))
    # retranslateUi

