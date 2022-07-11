# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from resources_rc import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1003, 709)
        Dialog.setStyleSheet(u"QLineEdit {\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(89, 140, 234);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(255, 203, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 90, 831, 541))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 25, 370, 460))
        self.label_2.setMinimumSize(QSize(370, 460))
        self.label_2.setMaximumSize(QSize(370, 460))
        self.label_2.setStyleSheet(u"background-color: rgb(52, 59, 72); border-radius:8px;")
#         self.label_3 = QLabel(self.widget)
#         self.label_3.setObjectName(u"label_3")
#         self.label_3.setGeometry(QRect(40, 30, 350, 191))
#         self.label_3.setStyleSheet(u"\n"
# "\n"
# "\n"
# "\n"
# "image:url(:/Logo/Assets/Logo/fasttool.png)")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 230, 311, 41))
   
        self.label_4.setStyleSheet(u"font: 12pt \"Alata\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
" border-top-right-radius: 17px;\n"
" border-bottom-left-radius: 17px;\n"
"background-color: rgb(44, 49, 60);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.btn_close_2 = QPushButton(self.widget)
        self.btn_close_2.setObjectName(u"btn_close_2")
        self.btn_close_2.setGeometry(QRect(60, 40, 16, 16))
        self.btn_close_2.setMinimumSize(QSize(16, 16))
        self.btn_close_2.setMaximumSize(QSize(16, 16))
        self.btn_close_2.setToolTipDuration(0)
        self.btn_close_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(111, 155, 234);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(195, 0, 0);\n"
"	border-radius:8px;\n"
"}")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 360, 120, 120))
        self.pushButton_2.setMinimumSize(QSize(120, 120))
        self.pushButton_2.setMaximumSize(QSize(120, 120))
        self.pushButton_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"border-image: url(:/16x16/Assets/icon_16x16/Fingerprint.png);\n"
"\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(40, 25, 370, 460))
        self.widget_2.setMinimumSize(QSize(370, 460))
        self.widget_2.setMaximumSize(QSize(370, 460))
        self.widget_2.setStyleSheet(u"\n"
"\n"
"#widget_2{\n"
"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 59, 72), stop:1 rgb(44, 49, 60));\n"
"border-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"\n"
"#label{\n"
"font: 12pt \"Alata\";\n"
"background-color: rgb(111, 155, 234);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, -1, -1, 40)
        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 130))
        self.frame_4.setStyleSheet(u"image: url(:/16x16/Assets/icon_16x16/user.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 40))
        self.pushButton.setStyleSheet(u"border: none;\n"
"font: 8pt \"Alata\";\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/16x16/Assets/icon_16x16/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(100, 100))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 40))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_7)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.widget_3, 0, Qt.AlignBottom)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"border: none;\n"
"font: 10pt \"Alata\";\n"
"color: rgb(111, 155, 234);")
        self.pushButton_6.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 100))
        self.widget_4.setMaximumSize(QSize(16777215, 100))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.widget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 100))
        self.pushButton_3.setMaximumSize(QSize(100, 100))
        self.pushButton_3.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/Assets/icon_16x16/phone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 100))
        self.pushButton_4.setMaximumSize(QSize(100, 100))
        self.pushButton_4.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/Assets/icon_16x16/telegram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 100))
        self.pushButton_5.setMaximumSize(QSize(100, 100))
        self.pushButton_5.setStyleSheet(u"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/Assets/icon_16x16/fb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 10pt \"Alata\";\n"
"color: rgb(111, 155, 234);")

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignRight)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 370, 321, 40))
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.raise_()
        self.widget_2.raise_()
        self.label_2.raise_()
        # self.label_3.raise_()
        self.label_4.raise_()
        self.btn_close_2.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText("")
        # self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">TELEGRAM PRO VER 3.0.2</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_close_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_close_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_close_2.setText("")
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Information", None))
        self.pushButton.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Dialog", u"Public key", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Activated", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Author : FastSoft   ", None))
    # retranslateUi

