# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Question(object):
    def setupUi(self, Question):
        if not Question.objectName():
            Question.setObjectName(u"Question")
        Question.resize(370, 80)
        Question.setMaximumSize(QSize(370, 80))
        icon = QIcon()
        icon.addFile(u"images/redondo_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Question.setWindowIcon(icon)
        Question.setStyleSheet(u"*{\n"
"	font-family: Agency FB;\n"
"	font-weight: bold;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#Question{background: url(\"images/fondo_messagebox.png\")}\n"
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
"")
        self.verticalLayout = QVBoxLayout(Question)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralwidget = QWidget(Question)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.centralwidget)

        QWidget.setTabOrder(self.pushButton_2, self.pushButton)

        self.retranslateUi(Question)

        QMetaObject.connectSlotsByName(Question)
    # setupUi

    def retranslateUi(self, Question):
        Question.setWindowTitle(QCoreApplication.translate("Question", u"title", None))
        self.pushButton.setText(QCoreApplication.translate("Question", u"SI", None))
        self.pushButton_2.setText(QCoreApplication.translate("Question", u"NO", None))
        self.label.setText(QCoreApplication.translate("Question", u"xds", None))
    # retranslateUi

