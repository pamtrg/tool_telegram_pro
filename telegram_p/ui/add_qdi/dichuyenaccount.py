# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dichuyenaccount.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(415, 179)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"#widget{\n"
"\n"
"	background-color: rgb(52, 59, 72);\n"
"border-radius: 20px;\n"
"	\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 46))
        self.frame.setMaximumSize(QSize(16777215, 46))
        self.frame.setStyleSheet(u"background-color: rgb(111, 155, 234);\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_close_2 = QPushButton(self.frame)
        self.pushButton_close_2.setObjectName(u"pushButton_close_2")
        self.pushButton_close_2.setMinimumSize(QSize(16, 16))
        self.pushButton_close_2.setMaximumSize(QSize(16, 16))
        self.pushButton_close_2.setToolTipDuration(0)
        self.pushButton_close_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(244, 93, 86);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(195, 0, 0);\n"
"	border-radius:8px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_close_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"font: 9pt \"Alata\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 100))
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"	background-color: rgb(44, 49, 60);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #3cbaa2; border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(10, 0, 10, 0)
        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 38))
        self.comboBox.setMaximumSize(QSize(240, 16777215))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"color: rgb(170, 0, 255);\n"
"	background-color: rgb(239, 238, 254);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"	border:none\n"
"}")

        self.horizontalLayout_26.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 40))
        self.pushButton.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_26.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)
        self.pushButton_close_2.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.pushButton_close_2.setToolTip(QCoreApplication.translate("Dialog", u"C l o se", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_close_2.setStatusTip(QCoreApplication.translate("Dialog", u"C l o se", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_close_2.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Di Chuy\u1ec3n Account", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK fen", None))
    # retranslateUi

