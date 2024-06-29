# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seleccionar_numero.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Cantidad(object):
    def setupUi(self, Cantidad):
        if not Cantidad.objectName():
            Cantidad.setObjectName(u"Cantidad")
        Cantidad.resize(370, 80)
        Cantidad.setMaximumSize(QSize(370, 80))
        icon = QIcon()
        icon.addFile(u"images/redondo_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Cantidad.setWindowIcon(icon)
        Cantidad.setStyleSheet(u"*{\n"
"	font-family: Agency FB;\n"
"	font-weight: bold;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#Cantidad{background: url(\"images/fondo_messagebox.png\")}\n"
"#centralwidget{\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.846154 rgba(0, 0, 0, 190));\n"
"	border-radius: 0.5em;\n"
"}\n"
"QComboBox{\n"
"min-width: 1em;\n"
"border: 2px solid #48e;\n"
"border-radius: 0.5em;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	min-width: 6em;\n"
"	border: 2px solid #48e;\n"
"	border-radius: 1em;\n"
"}\n"
"QDoubleSpinBox,QSpinBox{\n"
"padding-right: 2em;\n"
"}\n"
"\n"
"QDoubleSpinBox,QSpinBox{\n"
"\n"
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
"")
        self.verticalLayout = QVBoxLayout(Cantidad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralwidget = QWidget(Cantidad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 1, 2, 1)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(Cantidad)

        QMetaObject.connectSlotsByName(Cantidad)
    # setupUi

    def retranslateUi(self, Cantidad):
        Cantidad.setWindowTitle(QCoreApplication.translate("Cantidad", u"SELECCIONE CANTIDAD", None))
        self.label.setText(QCoreApplication.translate("Cantidad", u"Cantidad:", None))
    # retranslateUi

