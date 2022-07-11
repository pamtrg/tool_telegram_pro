# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainUpdate(object):
    def setupUi(self, MainUpdate):
        if not MainUpdate.objectName():
            MainUpdate.setObjectName(u"MainUpdate")
        MainUpdate.resize(400, 250)
        MainUpdate.setMinimumSize(QSize(400, 250))
        MainUpdate.setMaximumSize(QSize(400, 250))
        self.centralwidget = QWidget(MainUpdate)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"#widget{\n"
"background-color: rgb(52, 59, 72);\n"
"border-radius:20px\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressBar = QProgressBar(self.widget_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(111, 155, 234);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QPushButton:pressed {\n"
"font: 10pt \"Alata\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(111, 155, 234);\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_11 = QPushButton(self.widget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(120, 40))
        self.pushButton_11.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_11.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_2.addWidget(self.pushButton_11)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.widget)

        MainUpdate.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainUpdate)
        self.pushButton_2.clicked.connect(MainUpdate.close)

        QMetaObject.connectSlotsByName(MainUpdate)
    # setupUi

    def retranslateUi(self, MainUpdate):
        MainUpdate.setWindowTitle(QCoreApplication.translate("MainUpdate", u"Update", None))
        self.label.setText(QCoreApplication.translate("MainUpdate", u"\u0110ang ki\u1ec3m tra phi\u00ean b\u1ea3n !", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainUpdate", u"OK", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainUpdate", u"NO", None))
    # retranslateUi

