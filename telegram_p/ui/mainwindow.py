# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from resources_rc import *

class Ui_Fasttool_Telegram_UI(object):
    def setupUi(self, Fasttool_Telegram_UI):
        if not Fasttool_Telegram_UI.objectName():
            Fasttool_Telegram_UI.setObjectName(u"Fasttool_Telegram_UI")
        Fasttool_Telegram_UI.resize(1600, 840)
        Fasttool_Telegram_UI.setMinimumSize(QSize(1600, 800))
        Fasttool_Telegram_UI.setMaximumSize(QSize(16777215, 16777215))
        Fasttool_Telegram_UI.setAutoFillBackground(False)
        Fasttool_Telegram_UI.setStyleSheet(u"")
        Fasttool_Telegram_UI.setDockNestingEnabled(False)
        Fasttool_Telegram_UI.setUnifiedTitleAndToolBarOnMac(False)
        self.styleSheet = QWidget(Fasttool_Telegram_UI)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"#styleSheet{\n"
"background: transparent;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #2c313c;\n"
"    height: 15px;\n"
"    margin: 0px 21px 0 21px;\n"
"        border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #568af2;\n"
"    min-width: 25px;\n"
"        border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #272c36;\n"
"    width: 20px;\n"
"        border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #272c36;\n"
"    width: 20px;\n"
"        border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScr"
                        "ollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"        border: none;\n"
"    background: #2c313c;\n"
"    width: 15px;\n"
"    margin: 21px 0 21px 0;\n"
"        border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"        background: #568af2;\n"
"    min-height: 25px;\n"
"        border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #272c36;\n"
"     height: 20px;\n"
"        border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"        border: none;\n"
"    background: #272c36;\n"
"     height: 20px;\n"
"        border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     s"
                        "ubcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.frame_21 = QFrame(self.styleSheet)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 40))
        self.frame_21.setMaximumSize(QSize(16777215, 60))
        self.frame_21.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"\n"
"\n"
"border-top-left-radius: 20px;\n"
"\n"
"\n"
"\n"
" border-top-right-radius: 20px;\n"
"\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_10 = QFrame(self.frame_21)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 20))
        self.frame_10.setMaximumSize(QSize(16777215, 10))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_close = QPushButton(self.frame_10)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setToolTipDuration(0)
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(244, 93, 86);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(195, 0, 0);\n"
"	border-radius:8px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_close)

        self.btn_close_2 = QPushButton(self.frame_10)
        self.btn_close_2.setObjectName(u"btn_close_2")
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

        self.horizontalLayout_10.addWidget(self.btn_close_2)

        self.btn_close_3 = QPushButton(self.frame_10)
        self.btn_close_3.setObjectName(u"btn_close_3")
        self.btn_close_3.setMinimumSize(QSize(16, 16))
        self.btn_close_3.setMaximumSize(QSize(16, 16))
        self.btn_close_3.setToolTipDuration(0)
        self.btn_close_3.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 203, 0);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(195, 0, 0);\n"
"	border-radius:8px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_close_3)


        self.horizontalLayout_20.addWidget(self.frame_10, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_21)

        self.bgApp_2 = QFrame(self.styleSheet)
        self.bgApp_2.setObjectName(u"bgApp_2")
        self.bgApp_2.setMinimumSize(QSize(0, 40))
        self.bgApp_2.setStyleSheet(u"\n"
"#bgApp_2{\n"
"\n"
"	background-color: rgb(52, 59, 72);\n"
"\n"
"}")
        self.bgApp_2.setFrameShape(QFrame.StyledPanel)
        self.bgApp_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.bgApp_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QWidget(self.bgApp_2)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.bgApp)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.bgApp)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(300, 0))
        self.widget_2.setMaximumSize(QSize(300, 16777215))
        self.widget_2.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	color: rgb(138, 132, 159);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 10px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	  border-left: 4px solid blue;\n"
" \n"
"\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#topMenu .QPushButton:focus {	\n"
"	  border-left: 4px solid blue;\n"
" \n"
"\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#bottomMenu .QPushButton {	\n"
"	color: rgb(138, 132, 159);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hove"
                        "r {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 0)
        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"font: 12pt \"Alata\";")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 10, 10)
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 100))
        self.label_10.setMaximumSize(QSize(16777215, 100))
        self.label_10.setStyleSheet(u"image: url(:/Logo/Assets/Logo/Asset 34.png);")

        self.verticalLayout_3.addWidget(self.label_10)

        self.tittle = QLabel(self.frame_4)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setMinimumSize(QSize(0, 40))
        self.tittle.setMaximumSize(QSize(16777215, 40))
        self.tittle.setStyleSheet(u"font: 11pt \"Alata\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
" border-top-right-radius: 17px;\n"
" border-bottom-left-radius: 17px;\n"
"background-color: rgb(44, 49, 60);")
        self.tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.tittle)

        self.leftMenuBg = QFrame(self.frame_4)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(0, 0))
        self.leftMenuBg.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenuBg.setStyleSheet(u"")
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 20, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.topMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamilies([u"Alata"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_home)

        self.btn_group = QPushButton(self.topMenu)
        self.btn_group.setObjectName(u"btn_group")
        self.btn_group.setMinimumSize(QSize(0, 45))
        self.btn_group.setFont(font)
        self.btn_group.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_group)

        self.btn_chat_kichban = QPushButton(self.topMenu)
        self.btn_chat_kichban.setObjectName(u"btn_chat_kichban")
        self.btn_chat_kichban.setMinimumSize(QSize(0, 45))
        self.btn_chat_kichban.setFont(font)
        self.btn_chat_kichban.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_chat_kichban)

        self.btn_spam_tinnhan = QPushButton(self.topMenu)
        self.btn_spam_tinnhan.setObjectName(u"btn_spam_tinnhan")
        self.btn_spam_tinnhan.setMinimumSize(QSize(0, 45))
        self.btn_spam_tinnhan.setFont(font)
        self.btn_spam_tinnhan.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_spam_tinnhan)

        self.btn_caidat = QPushButton(self.topMenu)
        self.btn_caidat.setObjectName(u"btn_caidat")
        self.btn_caidat.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_caidat.sizePolicy().hasHeightForWidth())
        self.btn_caidat.setSizePolicy(sizePolicy)
        self.btn_caidat.setMinimumSize(QSize(0, 45))
        self.btn_caidat.setFont(font)
        self.btn_caidat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_caidat.setLayoutDirection(Qt.LeftToRight)
        self.btn_caidat.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_caidat)

        self.pushButton_8 = QPushButton(self.topMenu)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 45))

        self.verticalLayout_9.addWidget(self.pushButton_8)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.leftMenuFrame)


        self.verticalLayout_3.addWidget(self.leftMenuBg)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.maxsize = QLineEdit(self.frame_4)
        self.maxsize.setObjectName(u"maxsize")
        self.maxsize.setMinimumSize(QSize(200, 38))
        self.maxsize.setMaximumSize(QSize(16777215, 16777215))
        self.maxsize.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";")
        self.maxsize.setMaxLength(32772)

        self.verticalLayout_3.addWidget(self.maxsize)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.delaya = QLineEdit(self.frame_11)
        self.delaya.setObjectName(u"delaya")
        self.delaya.setMinimumSize(QSize(0, 38))
        self.delaya.setMaximumSize(QSize(16777215, 16777215))
        self.delaya.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";")

        self.horizontalLayout_6.addWidget(self.delaya)

        self.delayb = QLineEdit(self.frame_11)
        self.delayb.setObjectName(u"delayb")
        self.delayb.setMinimumSize(QSize(0, 38))
        self.delayb.setMaximumSize(QSize(16777215, 16777215))
        self.delayb.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";")

        self.horizontalLayout_6.addWidget(self.delayb)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"QPushButton:pressed {\n"
"   \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(255, 255, 255);\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.btn_stop = QPushButton(self.frame_3)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(0, 40))
        self.btn_stop.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background-color: rgb(244, 93, 86);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 0, 0);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_stop, 0, 1, 1, 1)

        self.btn_start = QPushButton(self.frame_3)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(0, 40))
        self.btn_start.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(100, 139, 212);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_start, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.widget = QWidget(self.bgApp)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"\n"
"\n"
"\n"
"#widget{\n"
"\n"
"\n"
" \n"
"	background-color: rgb(44, 49, 60);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"background: transparent;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 10)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget_4 = QStackedWidget(self.widget)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setStyleSheet(u"background: transparent;")
        self.bangdieukhien = QWidget()
        self.bangdieukhien.setObjectName(u"bangdieukhien")
        self.verticalLayout_5 = QVBoxLayout(self.bangdieukhien)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.bangdieukhien)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"QPushButton {\n"
"font: 12pt \"Alata\";\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"\n"
"  height: 50px;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(11, 0, 0, 30)
        self.btn_quanlyaccount = QPushButton(self.frame)
        self.btn_quanlyaccount.setObjectName(u"btn_quanlyaccount")
        self.btn_quanlyaccount.setMinimumSize(QSize(0, 0))
        self.btn_quanlyaccount.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_quanlyaccount)

        self.btn_quanytacvu = QPushButton(self.frame)
        self.btn_quanytacvu.setObjectName(u"btn_quanytacvu")
        self.btn_quanytacvu.setMinimumSize(QSize(0, 0))
        self.btn_quanytacvu.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_quanytacvu)


        self.verticalLayout_5.addWidget(self.frame, 0, Qt.AlignLeft)

        self.stackedWidget = QStackedWidget(self.bangdieukhien)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 35))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.stackedWidget.setLineWidth(0)
        self.page_account = QWidget()
        self.page_account.setObjectName(u"page_account")
        self.verticalLayout_2 = QVBoxLayout(self.page_account)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.page_account)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 50))
        self.widget_3.setMaximumSize(QSize(16777215, 50))
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
"}\n"
"QLineEdit {\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_26.setSpacing(20)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(240, 38))
        self.comboBox.setMaximumSize(QSize(300, 16777215))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
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

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(120, 40))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_26.addWidget(self.pushButton_3)

        self.pushButton_11 = QPushButton(self.widget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(120, 40))
        self.pushButton_11.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_11.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_26.addWidget(self.pushButton_11)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_26.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_26.addWidget(self.pushButton)

        self.comboBox_5 = QComboBox(self.widget_3)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(130, 38))
        self.comboBox_5.setStyleSheet(u"QComboBox{\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
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

        self.horizontalLayout_26.addWidget(self.comboBox_5)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 38))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_26.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page_account)
        self.page_tacvu = QWidget()
        self.page_tacvu.setObjectName(u"page_tacvu")
        self.page_tacvu.setStyleSheet(u"QComboBox{\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
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
"}\n"
"QPushButton:pressed {\n"
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
        self.verticalLayout_22 = QVBoxLayout(self.page_tacvu)
        self.verticalLayout_22.setSpacing(7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(11, 11, 11, 11)
        self.widget_8 = QWidget(self.page_tacvu)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"font: 10pt \"Alata\";\n"
"")
        self.verticalLayout_26 = QVBoxLayout(self.widget_8)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.widget_8)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius : 10px")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_31)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(20)
        self.gridLayout_8.setVerticalSpacing(10)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_31)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(400, 250))
        self.frame_47.setMaximumSize(QSize(16777215, 16777215))
        self.frame_47.setStyleSheet(u"\n"
"#frame_47{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_47)
        self.verticalLayout_43.setSpacing(11)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(11, 11, 11, 11)
        self.groupBox_33 = QGroupBox(self.frame_47)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setMinimumSize(QSize(0, 95))
        self.groupBox_33.setMaximumSize(QSize(16777215, 95))
        self.groupBox_33.setStyleSheet(u"\n"
"\n"
"QGroupBox::title {\n"
"\n"
"}\n"
"QGroupBox {\n"
"background-color: rgb(44, 49, 60);\n"
"}")
        self.horizontalLayout_32 = QHBoxLayout(self.groupBox_33)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pushButton_22 = QPushButton(self.groupBox_33)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(120, 40))
        self.pushButton_22.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_22.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_32.addWidget(self.pushButton_22)

        self.lineEdit_14 = QLineEdit(self.groupBox_33)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 38))
        self.lineEdit_14.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_32.addWidget(self.lineEdit_14)


        self.verticalLayout_43.addWidget(self.groupBox_33)

        self.groupBox_44 = QGroupBox(self.frame_47)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.groupBox_44.setMinimumSize(QSize(0, 95))
        self.groupBox_44.setMaximumSize(QSize(16777215, 95))
        self.groupBox_44.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.horizontalLayout_38 = QHBoxLayout(self.groupBox_44)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pushButton_37 = QPushButton(self.groupBox_44)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(120, 40))
        self.pushButton_37.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_37.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_38.addWidget(self.pushButton_37)

        self.lineEdit_18 = QLineEdit(self.groupBox_44)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(0, 38))
        self.lineEdit_18.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_38.addWidget(self.lineEdit_18)


        self.verticalLayout_43.addWidget(self.groupBox_44)

        self.groupBox_43 = QGroupBox(self.frame_47)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.groupBox_43.setMinimumSize(QSize(0, 95))
        self.groupBox_43.setMaximumSize(QSize(16777215, 95))
        self.groupBox_43.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.horizontalLayout_35 = QHBoxLayout(self.groupBox_43)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pushButton_36 = QPushButton(self.groupBox_43)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(120, 40))
        self.pushButton_36.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_36.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_35.addWidget(self.pushButton_36)

        self.lineEdit_17 = QLineEdit(self.groupBox_43)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 38))
        self.lineEdit_17.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_35.addWidget(self.lineEdit_17)


        self.verticalLayout_43.addWidget(self.groupBox_43)

        self.groupBox_35 = QGroupBox(self.frame_47)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setMinimumSize(QSize(0, 95))
        self.groupBox_35.setMaximumSize(QSize(16777215, 95))
        self.groupBox_35.setStyleSheet(u"\n"
"\n"
"QGroupBox::title {\n"
"\n"
"}\n"
"QGroupBox {\n"
"background-color: rgb(44, 49, 60);\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.groupBox_35)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pushButton_48 = QPushButton(self.groupBox_35)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(120, 40))
        self.pushButton_48.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_29.addWidget(self.pushButton_48)

        self.lineEdit_13 = QLineEdit(self.groupBox_35)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(0, 38))
        self.lineEdit_13.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_29.addWidget(self.lineEdit_13)


        self.verticalLayout_43.addWidget(self.groupBox_35)


        self.gridLayout_8.addWidget(self.frame_47, 0, 1, 2, 1)

        self.frame_37 = QFrame(self.frame_31)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(400, 250))
        self.frame_37.setMaximumSize(QSize(400, 16777215))
        self.frame_37.setStyleSheet(u"\n"
"#frame_37{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_37)
        self.verticalLayout_32.setSpacing(11)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(11, 11, 11, 11)
        self.checkBox_7 = QCheckBox(self.frame_37)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setStyleSheet(u"font: 10pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_32.addWidget(self.checkBox_7)

        self.frame_36 = QFrame(self.frame_37)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 50))
        self.frame_36.setMaximumSize(QSize(16777215, 50))
        self.frame_36.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_37.setSpacing(7)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 11, 11, 11)
        self.radioButton_6 = QRadioButton(self.frame_36)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setChecked(True)

        self.horizontalLayout_37.addWidget(self.radioButton_6)

        self.radioButton_3 = QRadioButton(self.frame_36)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_37.addWidget(self.radioButton_3)


        self.verticalLayout_32.addWidget(self.frame_36)

        self.checkBox_11 = QCheckBox(self.frame_37)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setStyleSheet(u"font: 10pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_32.addWidget(self.checkBox_11)

        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 50))
        self.frame_40.setMaximumSize(QSize(16777215, 50))
        self.frame_40.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_39.setSpacing(7)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, 11, 11, 11)
        self.radioButton_10 = QRadioButton(self.frame_40)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setChecked(True)

        self.horizontalLayout_39.addWidget(self.radioButton_10)

        self.radioButton_9 = QRadioButton(self.frame_40)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.horizontalLayout_39.addWidget(self.radioButton_9)


        self.verticalLayout_32.addWidget(self.frame_40)

        self.checkBox_15 = QCheckBox(self.frame_37)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setStyleSheet(u"font: 10pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_32.addWidget(self.checkBox_15)

        self.frame_48 = QFrame(self.frame_37)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 50))
        self.frame_48.setMaximumSize(QSize(16777215, 50))
        self.frame_48.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_36.setSpacing(7)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, 11, 11, 11)
        self.radioButton_18 = QRadioButton(self.frame_48)
        self.radioButton_18.setObjectName(u"radioButton_18")
        self.radioButton_18.setChecked(True)

        self.horizontalLayout_36.addWidget(self.radioButton_18)

        self.radioButton_17 = QRadioButton(self.frame_48)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.horizontalLayout_36.addWidget(self.radioButton_17)


        self.verticalLayout_32.addWidget(self.frame_48)

        self.checkBox_6 = QCheckBox(self.frame_37)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_32.addWidget(self.checkBox_6)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 50))
        self.frame_38.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_8 = QRadioButton(self.frame_38)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_8)

        self.radioButton_7 = QRadioButton(self.frame_38)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_3.addWidget(self.radioButton_7)

        self.lineEdit_12 = QLineEdit(self.frame_38)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 38))
        self.lineEdit_12.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit_12)


        self.verticalLayout_32.addWidget(self.frame_38, 0, Qt.AlignTop)

        self.checkBox_9 = QCheckBox(self.frame_37)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_32.addWidget(self.checkBox_9)


        self.gridLayout_8.addWidget(self.frame_37, 0, 0, 2, 1)

        self.frame_49 = QFrame(self.frame_31)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setEnabled(True)
        self.frame_49.setMinimumSize(QSize(0, 100))
        self.frame_49.setMaximumSize(QSize(16777215, 16777215))
        self.frame_49.setStyleSheet(u"\n"
"#frame_49{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_49)
        self.verticalLayout_45.setSpacing(11)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(11, 11, 11, 11)
        self.checkBox_16 = QCheckBox(self.frame_49)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setStyleSheet(u"font: 10pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_45.addWidget(self.checkBox_16)

        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 0))
        self.frame_50.setMaximumSize(QSize(16777215, 16777215))
        self.frame_50.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 11, 11, 11)
        self.pushButton_41 = QPushButton(self.frame_50)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(120, 40))
        self.pushButton_41.setMaximumSize(QSize(120, 40))
        self.pushButton_41.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_34.addWidget(self.pushButton_41)

        self.checkBox_20 = QCheckBox(self.frame_50)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.horizontalLayout_34.addWidget(self.checkBox_20)

        self.checkBox_19 = QCheckBox(self.frame_50)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.horizontalLayout_34.addWidget(self.checkBox_19)

        self.checkBox_5 = QCheckBox(self.frame_50)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_34.addWidget(self.checkBox_5)

        self.checkBox_8 = QCheckBox(self.frame_50)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.horizontalLayout_34.addWidget(self.checkBox_8)


        self.verticalLayout_45.addWidget(self.frame_50)


        self.gridLayout_8.addWidget(self.frame_49, 2, 0, 1, 2)


        self.verticalLayout_26.addWidget(self.frame_31, 0, Qt.AlignBottom)


        self.verticalLayout_22.addWidget(self.widget_8)

        self.stackedWidget.addWidget(self.page_tacvu)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_33 = QVBoxLayout(self.page_3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_7 = QWidget(self.page_3)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_35 = QVBoxLayout(self.widget_7)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")

        self.verticalLayout_33.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.stackedWidget_4.addWidget(self.bangdieukhien)
        self.nhom_kenh = QWidget()
        self.nhom_kenh.setObjectName(u"nhom_kenh")
        self.nhom_kenh.setStyleSheet(u"font: 10pt \"Alata\";")
        self.verticalLayout_13 = QVBoxLayout(self.nhom_kenh)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.nhom_kenh)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 70))
        self.frame_7.setMaximumSize(QSize(16777215, 70))
        self.frame_7.setStyleSheet(u"QPushButton {\n"
"font: 12pt \"Alata\";\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"\n"
"  height: 50px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:focus {	\n"
"  border-bottom: 4px solid rgb(255, 255, 255) ;\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 0, 0, 30)
        self.btn_themthanhvien = QPushButton(self.frame_7)
        self.btn_themthanhvien.setObjectName(u"btn_themthanhvien")
        self.btn_themthanhvien.setMinimumSize(QSize(0, 0))
        self.btn_themthanhvien.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btn_themthanhvien)

        self.btn_locthanhvien_2 = QPushButton(self.frame_7)
        self.btn_locthanhvien_2.setObjectName(u"btn_locthanhvien_2")
        self.btn_locthanhvien_2.setMinimumSize(QSize(0, 0))
        self.btn_locthanhvien_2.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btn_locthanhvien_2)

        self.btn_tienichgroup_channel = QPushButton(self.frame_7)
        self.btn_tienichgroup_channel.setObjectName(u"btn_tienichgroup_channel")

        self.horizontalLayout_11.addWidget(self.btn_tienichgroup_channel)


        self.verticalLayout_13.addWidget(self.frame_7, 0, Qt.AlignLeft|Qt.AlignTop)

        self.getmemandaddmem = QStackedWidget(self.nhom_kenh)
        self.getmemandaddmem.setObjectName(u"getmemandaddmem")
        self.getmemandaddmem.setMinimumSize(QSize(0, 35))
        self.getmemandaddmem.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QPlainTextEdit {\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QLineEdit {\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QPushButton:pressed {\n"
"font: 10pt \"Alata\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(111, 15"
                        "5, 234);\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"QSpinBox {\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"")
        self.getmemandaddmem.setFrameShape(QFrame.NoFrame)
        self.getmemandaddmem.setFrameShadow(QFrame.Raised)
        self.getmemandaddmem.setLineWidth(0)
        self.tienich_group_2 = QWidget()
        self.tienich_group_2.setObjectName(u"tienich_group_2")
        self.tienich_group_2.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QComboBox{\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
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
"}\n"
"QPushButton:pressed {\n"
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
        self.horizontalLayout_40 = QHBoxLayout(self.tienich_group_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.widget_18 = QWidget(self.tienich_group_2)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(600, 0))
        self.widget_18.setMaximumSize(QSize(16777215, 16777215))
        self.widget_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius : 10px")
        self.verticalLayout_49 = QVBoxLayout(self.widget_18)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.comboBox_8 = QComboBox(self.widget_18)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(0, 40))
        self.comboBox_8.setStyleSheet(u"\n"
"QComboBox QAbstractItemView {\n"
"color: rgb(170, 0, 255);\n"
"	background-color: rgb(239, 238, 254);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"	border:none\n"
"}")

        self.verticalLayout_49.addWidget(self.comboBox_8)

        self.stackedWidget_3 = QStackedWidget(self.widget_18)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_48 = QVBoxLayout(self.page_8)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.page_8)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"#frame_33{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_33)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_41 = QFrame(self.frame_33)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 50))
        self.frame_41.setMaximumSize(QSize(16777215, 16777215))
        self.frame_41.setStyleSheet(u"background-color: rgb(33, 37, 43)")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_6 = QWidget(self.frame_41)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 100))
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_20 = QRadioButton(self.widget_6)
        self.radioButton_20.setObjectName(u"radioButton_20")

        self.verticalLayout_14.addWidget(self.radioButton_20)

        self.radioButton_15 = QRadioButton(self.widget_6)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.verticalLayout_14.addWidget(self.radioButton_15)

        self.checkBox_12 = QCheckBox(self.widget_6)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_14.addWidget(self.checkBox_12)

        self.frame_53 = QFrame(self.widget_6)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.radioButton_13 = QRadioButton(self.frame_53)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setChecked(True)

        self.horizontalLayout_61.addWidget(self.radioButton_13)

        self.radioButton_11 = QRadioButton(self.frame_53)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setChecked(False)

        self.horizontalLayout_61.addWidget(self.radioButton_11)


        self.verticalLayout_14.addWidget(self.frame_53, 0, Qt.AlignTop)

        self.frame_35 = QFrame(self.widget_6)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_9 = QLabel(self.frame_35)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_53.addWidget(self.label_9)

        self.spinBox_5 = QSpinBox(self.frame_35)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMinimumSize(QSize(0, 38))
        self.spinBox_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.spinBox_5.setMaximum(999999999)
        self.spinBox_5.setSingleStep(10)

        self.horizontalLayout_53.addWidget(self.spinBox_5)

        self.spinBox_6 = QSpinBox(self.frame_35)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMinimumSize(QSize(0, 38))
        self.spinBox_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.spinBox_6.setMaximum(999999999)
        self.spinBox_6.setSingleStep(10)

        self.horizontalLayout_53.addWidget(self.spinBox_6)


        self.verticalLayout_14.addWidget(self.frame_35, 0, Qt.AlignTop)


        self.horizontalLayout_12.addWidget(self.widget_6, 0, Qt.AlignTop)

        self.plainTextEdit_8 = QPlainTextEdit(self.frame_41)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.horizontalLayout_12.addWidget(self.plainTextEdit_8)


        self.verticalLayout_28.addWidget(self.frame_41)


        self.verticalLayout_48.addWidget(self.frame_33)

        self.stackedWidget_3.addWidget(self.page_8)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_41 = QVBoxLayout(self.page_10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.page_10)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"#frame_39{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_39)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.plainTextEdit_9 = QPlainTextEdit(self.frame_39)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setStyleSheet(u"background-color: rgb(33, 37, 43)")

        self.verticalLayout_40.addWidget(self.plainTextEdit_9)


        self.verticalLayout_41.addWidget(self.frame_39)

        self.stackedWidget_3.addWidget(self.page_10)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_56 = QVBoxLayout(self.page_9)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.page_9)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"#frame_44{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_44)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 50))
        self.frame_45.setMaximumSize(QSize(16777215, 16777215))
        self.frame_45.setStyleSheet(u"background-color: rgb(33, 37, 43)")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_13 = QWidget(self.frame_45)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 100))
        self.verticalLayout_18 = QVBoxLayout(self.widget_13)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.radioButton_19 = QRadioButton(self.widget_13)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.verticalLayout_18.addWidget(self.radioButton_19)

        self.radioButton_22 = QRadioButton(self.widget_13)
        self.radioButton_22.setObjectName(u"radioButton_22")

        self.verticalLayout_18.addWidget(self.radioButton_22)


        self.horizontalLayout_14.addWidget(self.widget_13, 0, Qt.AlignTop)

        self.plainTextEdit_11 = QPlainTextEdit(self.frame_45)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.horizontalLayout_14.addWidget(self.plainTextEdit_11)


        self.verticalLayout_53.addWidget(self.frame_45)


        self.verticalLayout_56.addWidget(self.frame_44)

        self.stackedWidget_3.addWidget(self.page_9)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"#frame_42{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.verticalLayout_58 = QVBoxLayout(self.page_5)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.page_5)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"#frame_33{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_42)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 50))
        self.frame_43.setMaximumSize(QSize(16777215, 16777215))
        self.frame_43.setStyleSheet(u"background-color: rgb(33, 37, 43)")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_52 = QFrame(self.frame_43)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_52)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_13.addWidget(self.frame_52)

        self.widget_12 = QWidget(self.frame_43)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 100))
        self.verticalLayout_15 = QVBoxLayout(self.widget_12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.radioButton_16 = QRadioButton(self.widget_12)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setMinimumSize(QSize(0, 40))

        self.verticalLayout_15.addWidget(self.radioButton_16)

        self.radioButton_21 = QRadioButton(self.widget_12)
        self.radioButton_21.setObjectName(u"radioButton_21")
        self.radioButton_21.setMinimumSize(QSize(0, 40))

        self.verticalLayout_15.addWidget(self.radioButton_21)

        self.frame_51 = QFrame(self.widget_12)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_51)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = QLabel(self.frame_51)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.frame_51)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 40))
        self.lineEdit_16.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_4.addWidget(self.lineEdit_16, 0, 1, 1, 1)

        self.label_13 = QLabel(self.frame_51)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.frame_51)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(0, 40))
        self.lineEdit_21.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_4.addWidget(self.lineEdit_21, 1, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_51, 0, Qt.AlignTop)


        self.horizontalLayout_13.addWidget(self.widget_12)

        self.plainTextEdit_12 = QPlainTextEdit(self.frame_43)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.horizontalLayout_13.addWidget(self.plainTextEdit_12)


        self.verticalLayout_50.addWidget(self.frame_43)


        self.verticalLayout_58.addWidget(self.frame_42)

        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_20 = QVBoxLayout(self.page_6)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.page_6)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"#frame_33{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_46)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_46)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 50))
        self.frame_54.setMaximumSize(QSize(16777215, 16777215))
        self.frame_54.setStyleSheet(u"background-color: rgb(33, 37, 43)")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.widget_16 = QWidget(self.frame_54)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 100))
        self.verticalLayout_19 = QVBoxLayout(self.widget_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.checkBox_23 = QCheckBox(self.widget_16)
        self.checkBox_23.setObjectName(u"checkBox_23")
        self.checkBox_23.setEnabled(False)
        self.checkBox_23.setMinimumSize(QSize(0, 40))

        self.verticalLayout_19.addWidget(self.checkBox_23)

        self.frame_56 = QFrame(self.widget_16)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_56)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_19 = QLineEdit(self.frame_56)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(0, 40))
        self.lineEdit_19.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_6.addWidget(self.lineEdit_19, 0, 1, 1, 1)

        self.label_14 = QLabel(self.frame_56)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_56, 0, Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.widget_16)

        self.plainTextEdit_13 = QPlainTextEdit(self.frame_54)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")
        self.plainTextEdit_13.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.horizontalLayout_16.addWidget(self.plainTextEdit_13)


        self.verticalLayout_52.addWidget(self.frame_54)


        self.verticalLayout_20.addWidget(self.frame_46)

        self.stackedWidget_3.addWidget(self.page_6)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_46 = QVBoxLayout(self.page_11)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.page_11)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 50))
        self.frame_55.setMaximumSize(QSize(16777215, 16777215))
        self.frame_55.setStyleSheet(u"background-color: rgb(33, 37, 43)")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.widget_29 = QWidget(self.frame_55)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(0, 100))
        self.verticalLayout_34 = QVBoxLayout(self.widget_29)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, -1, -1)
        self.frame_57 = QFrame(self.widget_29)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_57)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.radioButton_23 = QRadioButton(self.frame_57)
        self.radioButton_23.setObjectName(u"radioButton_23")

        self.gridLayout_10.addWidget(self.radioButton_23, 1, 0, 1, 1)

        self.lineEdit_26 = QLineEdit(self.frame_57)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(0, 40))
        self.lineEdit_26.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_10.addWidget(self.lineEdit_26, 0, 1, 1, 1)

        self.btn_start_2 = QPushButton(self.frame_57)
        self.btn_start_2.setObjectName(u"btn_start_2")
        self.btn_start_2.setMinimumSize(QSize(100, 40))
        self.btn_start_2.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgb(100, 139, 212);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout_10.addWidget(self.btn_start_2, 0, 0, 1, 1)

        self.radioButton_24 = QRadioButton(self.frame_57)
        self.radioButton_24.setObjectName(u"radioButton_24")

        self.gridLayout_10.addWidget(self.radioButton_24, 1, 1, 1, 1)


        self.verticalLayout_34.addWidget(self.frame_57, 0, Qt.AlignTop)

        self.widget_30 = QWidget(self.widget_29)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_54 = QVBoxLayout(self.widget_30)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_15 = QPlainTextEdit(self.widget_30)
        self.plainTextEdit_15.setObjectName(u"plainTextEdit_15")
        self.plainTextEdit_15.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.verticalLayout_54.addWidget(self.plainTextEdit_15)


        self.verticalLayout_34.addWidget(self.widget_30)


        self.horizontalLayout_23.addWidget(self.widget_29)

        self.widget_31 = QWidget(self.frame_55)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(200, 0))
        self.verticalLayout_47 = QVBoxLayout(self.widget_31)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_14 = QPlainTextEdit(self.widget_31)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")
        self.plainTextEdit_14.setStyleSheet(u"background-color: rgb(52, 59, 72)")

        self.verticalLayout_47.addWidget(self.plainTextEdit_14)


        self.horizontalLayout_23.addWidget(self.widget_31)


        self.verticalLayout_46.addWidget(self.frame_55)

        self.stackedWidget_3.addWidget(self.page_11)

        self.verticalLayout_49.addWidget(self.stackedWidget_3)


        self.horizontalLayout_40.addWidget(self.widget_18)

        self.getmemandaddmem.addWidget(self.tienich_group_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_12 = QVBoxLayout(self.page_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_5 = QWidget(self.page_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.widget_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(500, 0))
        self.frame_15.setMaximumSize(QSize(500, 16777215))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_15)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(20)
        self.frame_12 = QFrame(self.frame_15)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.comboBox_3 = QComboBox(self.frame_12)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(150, 40))
        self.comboBox_3.setMaximumSize(QSize(150, 16777215))
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
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

        self.horizontalLayout_9.addWidget(self.comboBox_3)

        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.checkBox_3 = QCheckBox(self.frame_12)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.checkBox_3.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkBox_3)


        self.gridLayout_5.addWidget(self.frame_12, 2, 0, 1, 2)

        self.frame_30 = QFrame(self.frame_15)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 50))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.checkBox_17 = QCheckBox(self.frame_30)
        self.checkBox_17.setObjectName(u"checkBox_17")
        self.checkBox_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.checkBox_17)

        self.checkBox_2 = QCheckBox(self.frame_30)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.frame_30)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.checkBox)

        self.checkBox_4 = QCheckBox(self.frame_30)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.checkBox_4)


        self.gridLayout_5.addWidget(self.frame_30, 6, 0, 1, 2)

        self.plainTextEdit_5 = QPlainTextEdit(self.frame_15)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setMinimumSize(QSize(200, 200))
        self.plainTextEdit_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.plainTextEdit_5, 3, 0, 1, 2)

        self.radioButton_4 = QRadioButton(self.frame_15)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton_4.setChecked(True)

        self.gridLayout_5.addWidget(self.radioButton_4, 4, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_15)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(217, 40))
        self.pushButton_17.setMaximumSize(QSize(217, 40))

        self.gridLayout_5.addWidget(self.pushButton_17, 9, 1, 1, 1)

        self.searching_3 = QLineEdit(self.frame_15)
        self.searching_3.setObjectName(u"searching_3")
        self.searching_3.setMinimumSize(QSize(250, 40))
        self.searching_3.setMaximumSize(QSize(16777215, 16777215))
        self.searching_3.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_5.addWidget(self.searching_3, 10, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_15)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 40))
        self.pushButton_12.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_5.addWidget(self.pushButton_12, 9, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_15)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 40))
        self.lineEdit_11.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_5.addWidget(self.lineEdit_11, 10, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.frame_15)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.radioButton_5, 4, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_15)

        self.widget_15 = QWidget(self.widget_5)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_21 = QVBoxLayout(self.widget_15)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")

        self.horizontalLayout_17.addWidget(self.widget_15)


        self.verticalLayout_12.addWidget(self.widget_5)

        self.getmemandaddmem.addWidget(self.page_4)
        self.addmem = QWidget()
        self.addmem.setObjectName(u"addmem")
        self.addmem.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius : 10px")
        self.horizontalLayout_18 = QHBoxLayout(self.addmem)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_14 = QFrame(self.addmem)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_14)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 11, 11)
        self.widget_14 = QWidget(self.frame_14)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(320, 0))
        self.widget_14.setMaximumSize(QSize(320, 16777215))
        self.widget_14.setStyleSheet(u"#widget_14{\n"
"background-color: rgb(52, 59, 72);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.verticalLayout_23 = QVBoxLayout(self.widget_14)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_16 = QFrame(self.widget_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(300, 0))
        self.frame_16.setMaximumSize(QSize(300, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_16)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_16)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 1)

        self.label = QLabel(self.frame_16)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.frame_16)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(0, 38))
        self.spinBox_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setSingleStep(10)

        self.gridLayout_7.addWidget(self.spinBox_2, 0, 1, 1, 1)

        self.spinBox_3 = QSpinBox(self.frame_16)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(0, 38))
        self.spinBox_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.spinBox_3.setMaximum(999999999)
        self.spinBox_3.setSingleStep(10)

        self.gridLayout_7.addWidget(self.spinBox_3, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_4, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.frame_16)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 38))
        self.spinBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.spinBox.setMaximum(999999999)
        self.spinBox.setSingleStep(10)

        self.gridLayout_7.addWidget(self.spinBox, 2, 1, 1, 1)

        self.spinBox_4 = QSpinBox(self.frame_16)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimumSize(QSize(0, 38))
        self.spinBox_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.spinBox_4.setMaximum(999999999)
        self.spinBox_4.setSingleStep(10)

        self.gridLayout_7.addWidget(self.spinBox_4, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_5, 3, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.frame_17 = QFrame(self.widget_14)
        self.frame_17.setObjectName(u"frame_17")
        font1 = QFont()
        font1.setFamilies([u"Alata"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.frame_17.setFont(font1)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_17)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(10)
        self.gridLayout_9.setVerticalSpacing(12)
        self.gridLayout_9.setContentsMargins(0, 5, 0, 5)
        self.pushButton_6 = QPushButton(self.frame_17)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 40))

        self.gridLayout_9.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_17)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 40))

        self.gridLayout_9.addWidget(self.pushButton_7, 1, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_17, 0, Qt.AlignBottom)

        self.comboBox_6 = QComboBox(self.widget_14)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(240, 38))
        self.comboBox_6.setStyleSheet(u"QComboBox{\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
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

        self.verticalLayout_23.addWidget(self.comboBox_6)

        self.lineEdit_6 = QLineEdit(self.widget_14)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 40))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_23.addWidget(self.lineEdit_6)

        self.lineEdit_4 = QLineEdit(self.widget_14)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_23.addWidget(self.lineEdit_4)


        self.verticalLayout_24.addWidget(self.widget_14)


        self.horizontalLayout_18.addWidget(self.frame_14, 0, Qt.AlignLeft)

        self.frame_13 = QFrame(self.addmem)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_13)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_13)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.total_mem = QLabel(self.frame_29)
        self.total_mem.setObjectName(u"total_mem")

        self.horizontalLayout_19.addWidget(self.total_mem, 0, Qt.AlignTop)

        self.thatbaistt = QLabel(self.frame_29)
        self.thatbaistt.setObjectName(u"thatbaistt")
        self.thatbaistt.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_19.addWidget(self.thatbaistt, 0, Qt.AlignTop)

        self.stt_thanhcong = QLabel(self.frame_29)
        self.stt_thanhcong.setObjectName(u"stt_thanhcong")
        self.stt_thanhcong.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.horizontalLayout_19.addWidget(self.stt_thanhcong, 0, Qt.AlignTop)


        self.verticalLayout_31.addWidget(self.frame_29, 0, Qt.AlignTop)

        self.frame_28 = QFrame(self.frame_13)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_28)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, -1, 0, -1)

        self.verticalLayout_31.addWidget(self.frame_28)


        self.horizontalLayout_18.addWidget(self.frame_13)

        self.getmemandaddmem.addWidget(self.addmem)

        self.verticalLayout_13.addWidget(self.getmemandaddmem)

        self.stackedWidget_4.addWidget(self.nhom_kenh)
        self.spamtinnhan = QWidget()
        self.spamtinnhan.setObjectName(u"spamtinnhan")
        self.verticalLayout_17 = QVBoxLayout(self.spamtinnhan)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.spamtinnhan)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 70))
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setStyleSheet(u"QPushButton {\n"
"font: 12pt \"Alata\";\n"
"	color: rgb(138, 132, 159);\n"
"	border: none;\n"
"\n"
"  height: 50px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:focus {	\n"
"  border-bottom: 4px solid rgb(255, 255, 255) ;\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(11, 0, 0, 30)
        self.pushButton_20 = QPushButton(self.frame_9)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.pushButton_20)

        self.pushButton_31 = QPushButton(self.frame_9)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(0, 0))
        self.pushButton_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.pushButton_31, 0, Qt.AlignLeft)

        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.pushButton_5)


        self.verticalLayout_17.addWidget(self.frame_9, 0, Qt.AlignLeft)

        self.stackedWidget_6 = QStackedWidget(self.spamtinnhan)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.stackedWidget_6.setMinimumSize(QSize(0, 35))
        self.stackedWidget_6.setStyleSheet(u"background: transparent;")
        self.stackedWidget_6.setFrameShape(QFrame.NoFrame)
        self.stackedWidget_6.setFrameShadow(QFrame.Raised)
        self.stackedWidget_6.setLineWidth(0)
        self.page_90 = QWidget()
        self.page_90.setObjectName(u"page_90")
        self.page_90.setStyleSheet(u"")
        self.horizontalLayout_41 = QHBoxLayout(self.page_90)
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_19 = QStackedWidget(self.page_90)
        self.stackedWidget_19.setObjectName(u"stackedWidget_19")
        self.stackedWidget_19.setMinimumSize(QSize(500, 0))
        self.stackedWidget_19.setMaximumSize(QSize(500, 16777215))
        self.stackedWidget_19.setStyleSheet(u"font: 10pt \"Alata\";")
        self.stackedWidget_19Page1 = QWidget()
        self.stackedWidget_19Page1.setObjectName(u"stackedWidget_19Page1")
        self.stackedWidget_19Page1.setStyleSheet(u"QPlainTextEdit {\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.stackedWidget_19Page1)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 0, 0, 8)
        self.widget_54 = QWidget(self.stackedWidget_19Page1)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.pushButton_42 = QPushButton(self.widget_54)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(120, 40))
        self.pushButton_42.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_42.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_42.addWidget(self.pushButton_42)

        self.lineEdit_22 = QLineEdit(self.widget_54)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(0, 38))
        self.lineEdit_22.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_42.addWidget(self.lineEdit_22)


        self.verticalLayout_16.addWidget(self.widget_54, 0, Qt.AlignTop)

        self.widget_55 = QWidget(self.stackedWidget_19Page1)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.pushButton_43 = QPushButton(self.widget_55)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMinimumSize(QSize(120, 40))
        self.pushButton_43.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_43.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_43.addWidget(self.pushButton_43)

        self.lineEdit_23 = QLineEdit(self.widget_55)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(0, 38))
        self.lineEdit_23.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_43.addWidget(self.lineEdit_23)


        self.verticalLayout_16.addWidget(self.widget_55, 0, Qt.AlignTop)

        self.widget_19 = QWidget(self.stackedWidget_19Page1)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_10 = QPlainTextEdit(self.widget_19)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_44.addWidget(self.plainTextEdit_10)


        self.verticalLayout_16.addWidget(self.widget_19)

        self.widget_23 = QWidget(self.stackedWidget_19Page1)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_47 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.pushButton_45 = QPushButton(self.widget_23)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(237, 40))
        self.pushButton_45.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_47.addWidget(self.pushButton_45)

        self.lineEdit_25 = QLineEdit(self.widget_23)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(0, 38))
        self.lineEdit_25.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_47.addWidget(self.lineEdit_25)


        self.verticalLayout_16.addWidget(self.widget_23)

        self.widget_20 = QWidget(self.stackedWidget_19Page1)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 50))
        self.widget_20.setStyleSheet(u"QPushButton:pressed {\n"
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
        self.horizontalLayout_46 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.pushButton_32 = QPushButton(self.widget_20)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(40, 40))
        self.pushButton_32.setMaximumSize(QSize(40, 40))
        self.pushButton_32.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        icon = QIcon()
        icon.addFile(u":/16x16/Assets/icon_16x16/6737974021623860963-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_32.setIcon(icon)

        self.horizontalLayout_46.addWidget(self.pushButton_32)

        self.pushButton_29 = QPushButton(self.widget_20)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(0, 40))
        self.pushButton_29.setStyleSheet(u"")

        self.horizontalLayout_46.addWidget(self.pushButton_29)

        self.pushButton_44 = QPushButton(self.widget_20)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_46.addWidget(self.pushButton_44)


        self.verticalLayout_16.addWidget(self.widget_20)

        self.stackedWidget_19.addWidget(self.stackedWidget_19Page1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_42 = QVBoxLayout(self.page)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.page)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_51 = QVBoxLayout(self.widget_24)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_42.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.page)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_44 = QVBoxLayout(self.widget_25)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.checkBox_13 = QCheckBox(self.widget_27)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.horizontalLayout_49.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.widget_27)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.horizontalLayout_49.addWidget(self.checkBox_14)


        self.verticalLayout_44.addWidget(self.widget_27, 0, Qt.AlignBottom)

        self.widget_28 = QWidget(self.widget_25)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_50 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_28 = QLineEdit(self.widget_28)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setMinimumSize(QSize(0, 38))
        self.lineEdit_28.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_50.addWidget(self.lineEdit_28)

        self.lineEdit_27 = QLineEdit(self.widget_28)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(0, 38))
        self.lineEdit_27.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_50.addWidget(self.lineEdit_27)


        self.verticalLayout_44.addWidget(self.widget_28)

        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_48 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.pushButton_46 = QPushButton(self.widget_26)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMinimumSize(QSize(225, 40))
        self.pushButton_46.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_48.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.widget_26)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(0, 40))
        self.pushButton_47.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_48.addWidget(self.pushButton_47)

        self.pushButton_28 = QPushButton(self.widget_26)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(50, 50))
        self.pushButton_28.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/16x16/Assets/icon_16x16/exchange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_28.setIcon(icon1)
        self.pushButton_28.setIconSize(QSize(50, 50))

        self.horizontalLayout_48.addWidget(self.pushButton_28)


        self.verticalLayout_44.addWidget(self.widget_26, 0, Qt.AlignBottom)


        self.verticalLayout_42.addWidget(self.widget_25, 0, Qt.AlignBottom)

        self.stackedWidget_19.addWidget(self.page)

        self.horizontalLayout_41.addWidget(self.stackedWidget_19)

        self.widget_21 = QWidget(self.page_90)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(100, 0))
        self.widget_21.setStyleSheet(u"font: 10pt \"Alata\";")
        self.verticalLayout_36 = QVBoxLayout(self.widget_21)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_29 = QStackedWidget(self.widget_21)
        self.stackedWidget_29.setObjectName(u"stackedWidget_29")
        self.stackedWidget_29Page1 = QWidget()
        self.stackedWidget_29Page1.setObjectName(u"stackedWidget_29Page1")
        self.verticalLayout_37 = QVBoxLayout(self.stackedWidget_29Page1)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_29.addWidget(self.stackedWidget_29Page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_38 = QVBoxLayout(self.page_2)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_41 = QWidget(self.page_2)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_39 = QVBoxLayout(self.widget_41)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_38.addWidget(self.widget_41)

        self.frame_34 = QFrame(self.page_2)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, -1)
        self.pushButton_30 = QPushButton(self.frame_34)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(0, 40))
        self.pushButton_30.setStyleSheet(u"QPushButton:pressed {\n"
"font: 10pt \"Alata\";\n"
"\n"
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

        self.horizontalLayout_31.addWidget(self.pushButton_30)


        self.verticalLayout_38.addWidget(self.frame_34, 0, Qt.AlignBottom)

        self.stackedWidget_29.addWidget(self.page_2)

        self.verticalLayout_36.addWidget(self.stackedWidget_29)


        self.horizontalLayout_41.addWidget(self.widget_21)

        self.stackedWidget_6.addWidget(self.page_90)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_21 = QHBoxLayout(self.page_7)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.page_7)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.widget_17)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_8 = QFrame(self.widget_17)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_56 = QWidget(self.frame_8)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.pushButton_49 = QPushButton(self.widget_56)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMinimumSize(QSize(120, 40))
        self.pushButton_49.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_49.setStyleSheet(u"QPushButton:pressed {\n"
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

        self.horizontalLayout_45.addWidget(self.pushButton_49)

        self.lineEdit_24 = QLineEdit(self.widget_56)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMinimumSize(QSize(0, 38))
        self.lineEdit_24.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_45.addWidget(self.lineEdit_24)


        self.verticalLayout_27.addWidget(self.widget_56, 0, Qt.AlignTop)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 38))
        self.lineEdit_2.setStyleSheet(u"\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"font: 9pt \"Alata\";\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_27.addWidget(self.lineEdit_2)

        self.frame_19 = QFrame(self.frame_8)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_22.addWidget(self.label_11)

        self.spinBox_7 = QSpinBox(self.frame_19)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMinimumSize(QSize(0, 40))
        self.spinBox_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(64, 71, 88);\n"
"background-color: rgb(33, 37, 43);")
        self.spinBox_7.setMinimum(1)

        self.horizontalLayout_22.addWidget(self.spinBox_7)


        self.verticalLayout_27.addWidget(self.frame_19)

        self.checkBox_10 = QCheckBox(self.frame_8)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_27.addWidget(self.checkBox_10)


        self.verticalLayout_25.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.widget_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_18)


        self.horizontalLayout_21.addWidget(self.widget_17)

        self.stackedWidget_22 = QStackedWidget(self.page_7)
        self.stackedWidget_22.setObjectName(u"stackedWidget_22")
        self.stackedWidget_22.setMinimumSize(QSize(750, 0))
        self.stackedWidget_22Page1 = QWidget()
        self.stackedWidget_22Page1.setObjectName(u"stackedWidget_22Page1")
        self.verticalLayout_29 = QVBoxLayout(self.stackedWidget_22Page1)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_22.addWidget(self.stackedWidget_22Page1)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_55 = QVBoxLayout(self.page_12)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.stackedWidget_22.addWidget(self.page_12)

        self.horizontalLayout_21.addWidget(self.stackedWidget_22)

        self.stackedWidget_6.addWidget(self.page_7)

        self.verticalLayout_17.addWidget(self.stackedWidget_6)

        self.stackedWidget_4.addWidget(self.spamtinnhan)
        self.caidat = QWidget()
        self.caidat.setObjectName(u"caidat")
        self.caidat.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.caidat)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.caidat)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 70))
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"font: 12pt \"Alata\";\n"
"	color: rgb(138, 132, 159);\n"
"	border: none;\n"
"\n"
"  height: 50px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:focus {	\n"
"  border-bottom: 4px solid rgb(255, 255, 255) ;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 0, 30)
        self.btn_proxy = QPushButton(self.frame_5)
        self.btn_proxy.setObjectName(u"btn_proxy")
        self.btn_proxy.setMinimumSize(QSize(0, 0))
        self.btn_proxy.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.btn_proxy, 0, Qt.AlignLeft)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.stackedWidget_2 = QStackedWidget(self.caidat)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 35))
        self.stackedWidget_2.setStyleSheet(u"QComboBox{\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
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
"}\n"
"QPushButton:pressed {\n"
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
        self.stackedWidget_2.setFrameShape(QFrame.NoFrame)
        self.stackedWidget_2.setFrameShadow(QFrame.Raised)
        self.stackedWidget_2.setLineWidth(0)
        self.stack_proxy = QWidget()
        self.stack_proxy.setObjectName(u"stack_proxy")
        self.verticalLayout_10 = QVBoxLayout(self.stack_proxy)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_4 = QWidget(self.stack_proxy)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 50))
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.widget_4.setStyleSheet(u"QPushButton:pressed {\n"
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
"}\n"
"QLineEdit {\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_27.setSpacing(20)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.widget_4)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(240, 38))
        self.comboBox_2.setMaximumSize(QSize(300, 16777215))
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"font: 10pt \"Alata\";background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
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

        self.horizontalLayout_27.addWidget(self.comboBox_2)

        self.pushButton_9 = QPushButton(self.widget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(120, 40))
        self.pushButton_9.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_9.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_27.addWidget(self.pushButton_9)

        self.pushButton_14 = QPushButton(self.widget_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(140, 40))
        self.pushButton_14.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_14.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_27.addWidget(self.pushButton_14)

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(140, 40))
        self.pushButton_4.setStyleSheet(u"font: 9pt \"Alata\";")

        self.horizontalLayout_27.addWidget(self.pushButton_4)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.widget_9 = QWidget(self.stack_proxy)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"QPlainTextEdit {\n"
"font: 10pt \"Alata\";\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"\n"
"	padding-left: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 11, 0, 0)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(400, 0))
        self.gridLayout_2 = QGridLayout(self.widget_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.widget_10)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 2)

        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"Alata\";")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_3 = QGridLayout(self.widget_11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setStyleSheet(u"color: rgb(0, 255, 127);\n"
"font: 9pt \"Alata\";")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.widget_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 0))
        self.label_8.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 9pt \"Alata\";")

        self.gridLayout_3.addWidget(self.label_8, 2, 1, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.widget_11)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.plainTextEdit_3, 1, 0, 1, 1)

        self.plainTextEdit_4 = QPlainTextEdit(self.widget_11)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);color: rgb(255, 0, 0);")

        self.gridLayout_3.addWidget(self.plainTextEdit_4, 1, 1, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget_11)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setMinimumSize(QSize(0, 150))
        self.plainTextEdit_2.setMaximumSize(QSize(16777215, 150))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.plainTextEdit_2, 0, 0, 1, 2)


        self.horizontalLayout_7.addWidget(self.widget_11)


        self.verticalLayout_10.addWidget(self.widget_9)

        self.stackedWidget_2.addWidget(self.stack_proxy)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)

        self.stackedWidget_4.addWidget(self.caidat)

        self.verticalLayout_4.addWidget(self.stackedWidget_4)


        self.horizontalLayout_4.addWidget(self.widget)


        self.verticalLayout_8.addWidget(self.bgApp)

        self.frame_6 = QFrame(self.bgApp_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 40))
        self.frame_6.setMaximumSize(QSize(16777215, 40))
        self.frame_6.setStyleSheet(u"\n"
"\n"
"#frame_6{\n"
" border-bottom-left-radius: 20px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 0, 0, 0)
        self.tongacc = QLabel(self.frame_6)
        self.tongacc.setObjectName(u"tongacc")
        self.tongacc.setStyleSheet(u"color: rgb(255, 203, 0);")

        self.horizontalLayout.addWidget(self.tongacc)

        self.dangchonstt = QLabel(self.frame_6)
        self.dangchonstt.setObjectName(u"dangchonstt")
        self.dangchonstt.setStyleSheet(u"color: rgb(0, 170, 255);")

        self.horizontalLayout.addWidget(self.dangchonstt)

        self.livestt = QLabel(self.frame_6)
        self.livestt.setObjectName(u"livestt")
        self.livestt.setStyleSheet(u"color: rgb(0, 255, 127);")

        self.horizontalLayout.addWidget(self.livestt)

        self.diestt = QLabel(self.frame_6)
        self.diestt.setObjectName(u"diestt")
        self.diestt.setMinimumSize(QSize(10000, 0))
        self.diestt.setMaximumSize(QSize(16777215, 16777215))
        self.diestt.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.diestt, 0, Qt.AlignLeft)

        self.frame_27 = QFrame(self.frame_6)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(40, 0))
        self.frame_27.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.frame_27.setStyleSheet(u"image: url(:/16x16/Assets/icon_16x16/size_maximize_icon_142968.png);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_27)


        self.verticalLayout_8.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.bgApp_2)

        Fasttool_Telegram_UI.setCentralWidget(self.styleSheet)

        self.retranslateUi(Fasttool_Telegram_UI)

        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.getmemandaddmem.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_6.setCurrentIndex(1)
        self.stackedWidget_19.setCurrentIndex(0)
        self.stackedWidget_29.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Fasttool_Telegram_UI)
    # setupUi

    def retranslateUi(self, Fasttool_Telegram_UI):
        Fasttool_Telegram_UI.setWindowTitle(QCoreApplication.translate("Fasttool_Telegram_UI", u" TELEGRAM PRO", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_close.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_close_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_close_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_close_3.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_close_3.setText("")
        self.label_10.setText("")
        self.tittle.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u" TELEGRAM PRO", None))
        self.btn_home.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Dashboard", None))
        self.btn_group.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Groups / Channels", None))
        self.btn_chat_kichban.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Chat Scrips", None))
        self.btn_spam_tinnhan.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Spam Messages", None))
        self.btn_caidat.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Settings", None))
        self.pushButton_8.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"C\u1eadp nh\u1eadt", None))
        self.maxsize.setInputMask("")
        self.maxsize.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"S\u1ed1 Lu\u1ed3ng", None))
#if QT_CONFIG(tooltip)
        self.delaya.setToolTip(QCoreApplication.translate("Fasttool_Telegram_UI", u"<html><head/><body><p>Th\u1eddi gian ch\u1edd thao t\u00e1c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delaya.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Min Delay", None))
#if QT_CONFIG(tooltip)
        self.delayb.setToolTip(QCoreApplication.translate("Fasttool_Telegram_UI", u"<html><head/><body><p>Th\u1eddi gian ch\u1edd thao t\u00e1c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delayb.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Max Delay", None))
        self.btn_stop.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Stop", None))
        self.btn_start.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Start", None))
        self.btn_quanlyaccount.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Account Management", None))
        self.btn_quanytacvu.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Change Account", None))
        self.pushButton_3.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Add folder", None))
        self.pushButton_11.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Remove folder", None))
        self.pushButton_2.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Reload", None))
        self.pushButton.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Import Account", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Search......", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("Fasttool_Telegram_UI", u"Set Path Username", None))
        self.pushButton_22.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Open", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110\u01b0\u1eddng D\u1eabn ....", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("Fasttool_Telegram_UI", u"Set Path Bio", None))
        self.pushButton_37.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Open", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110\u01b0\u1eddng D\u1eabn ....", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("Fasttool_Telegram_UI", u"Set Path Image", None))
        self.pushButton_36.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Open", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110\u01b0\u1eddng D\u1eabn ....", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("Fasttool_Telegram_UI", u"Set Path Full Name", None))
        self.pushButton_48.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Open", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110\u01b0\u1eddng D\u1eabn ....", None))
        self.checkBox_7.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Avartar", None))
        self.radioButton_6.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Change Avatar", None))
        self.radioButton_3.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"X\u00f3a Avatar", None))
        self.checkBox_11.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Bio", None))
        self.radioButton_10.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Change Bio", None))
        self.radioButton_9.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"X\u00f3a Bio", None))
        self.checkBox_15.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Username", None))
        self.radioButton_18.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Change Username", None))
        self.radioButton_17.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"X\u00f3a Username", None))
        self.checkBox_6.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"2FA Auth", None))
        self.radioButton_8.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Change", None))
        self.radioButton_7.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"X\u00f3a", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"2FA New", None))
        self.checkBox_9.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Change Full Name", None))
        self.checkBox_16.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Session", None))
        self.pushButton_41.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Save", None))
        self.checkBox_20.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Close All Session", None))
        self.checkBox_19.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Create New Session", None))
        self.checkBox_5.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Delete All Message", None))
        self.checkBox_8.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Out All Groups and Channels", None))
        self.btn_themthanhvien.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Add Member", None))
        self.btn_locthanhvien_2.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Filter Members", None))
        self.btn_tienichgroup_channel.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Utilities", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("Fasttool_Telegram_UI", u"Join Group Or Channel", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("Fasttool_Telegram_UI", u"Leave Groups or Channel", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("Fasttool_Telegram_UI", u"Comment channel", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff view post Channel", None))
        self.comboBox_8.setItemText(4, QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff reaction post Channel or Group", None))
        self.comboBox_8.setItemText(5, QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff Online", None))
        self.comboBox_8.setItemText(6, QCoreApplication.translate("Fasttool_Telegram_UI", u"Scrape Data Message", None))
        self.comboBox_8.setItemText(7, QCoreApplication.translate("Fasttool_Telegram_UI", u"Join Video Call", None))

        self.radioButton_20.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"leave the Groups or Channel by link", None))
        self.radioButton_15.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"leave group all groups and channels", None))
        self.checkBox_12.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"leave the groups on conditions", None))
        self.radioButton_13.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Block Chat", None))
        self.radioButton_11.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"No Block Chat", None))
        self.label_9.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Total Member", None))
        self.plainTextEdit_8.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link Group Or Channel", None))
        self.plainTextEdit_9.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link group or channel", None))
        self.radioButton_19.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff view post by link Channel", None))
        self.radioButton_22.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff view post by Link Post", None))
        self.plainTextEdit_11.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link Post Or Channel", None))
        self.radioButton_16.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff reaction post by Link Post", None))
        self.radioButton_21.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff reaction post by Link Channel or Group", None))
        self.label_12.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Icons", None))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"List Icon", None))
        self.label_13.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Count Icon", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"number|number", None))
        self.plainTextEdit_12.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link Post, Group Or Channel", None))
        self.checkBox_23.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Filter bot", None))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Count Messages", None))
        self.label_14.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Count Messages", None))
        self.plainTextEdit_13.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link Group Or Channel", None))
        self.radioButton_23.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff comment by link Channel", None))
        self.lineEdit_26.setText("")
        self.lineEdit_26.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110\u01b0\u1eddng d\u1eabn file message", None))
        self.btn_start_2.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Open", None))
        self.radioButton_24.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Buff comment by Link Post", None))
        self.plainTextEdit_15.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link channel or link post", None))
        self.plainTextEdit_14.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"N\u1ed9i dung", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Fasttool_Telegram_UI", u"Get All Member", None))

        self.label_2.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Total : ", None))
        self.checkBox_3.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Clean table", None))
        self.checkBox_17.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Delete Admin", None))
        self.checkBox_2.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Vi\u1ec7t Nam", None))
        self.checkBox.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Avatar", None))
        self.checkBox_4.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"ID", None))
        self.radioButton_4.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Get Mem No Link", None))
        self.pushButton_17.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Export Data", None))
        self.searching_3.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"LINK group or ID group", None))
        self.pushButton_12.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Get List Name Group", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110i\u1ec1n t\u00ean file", None))
        self.radioButton_5.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Get Mem With Link", None))
        self.label_3.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Add To", None))
        self.label.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Add From", None))
        self.label_4.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Total add / account", None))
        self.label_5.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Total id / account", None))
        self.pushButton_6.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Import Data", None))
        self.pushButton_7.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Save", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link group or ID group c\u1ea7n add member", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link group or ID group c\u1ea7n clone", None))
        self.total_mem.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Total :", None))
        self.thatbaistt.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Fail:", None))
        self.stt_thanhcong.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Success :", None))
        self.pushButton_20.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Spam", None))
        self.pushButton_31.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Seeding", None))
        self.pushButton_5.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"K\u1ecbch b\u1ea3n", None))
        self.pushButton_42.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Open", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110\u01b0\u1eddng D\u1eabn File....", None))
        self.pushButton_43.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Open", None))
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110\u01b0\u1eddng D\u1eabn File....", None))
        self.plainTextEdit_10.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Message .....", None))
        self.pushButton_45.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Save Scripts", None))
        self.lineEdit_25.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Name Scripts", None))
        self.pushButton_32.setText("")
        self.pushButton_29.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Add", None))
        self.pushButton_44.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Clean", None))
        self.checkBox_13.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Random Massage", None))
        self.checkBox_14.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Duplicate", None))
        self.lineEdit_28.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Max Message / Group", None))
        self.lineEdit_27.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Max Group / Account", None))
        self.pushButton_46.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"ReLoad Scripts", None))
        self.pushButton_47.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Add Scripts", None))
        self.pushButton_28.setText("")
        self.pushButton_30.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Import Data", None))
        self.pushButton_49.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Open", None))
        self.lineEdit_24.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110\u01b0\u1eddng D\u1eabn File....", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Link group", None))
        self.label_11.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Loop", None))
        self.checkBox_10.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Random repLy", None))
        self.btn_proxy.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"PROXY", None))
        self.pushButton_9.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Import Proxy", None))
        self.pushButton_14.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Check Live Proxy", None))
        self.pushButton_4.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Save ", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"\u0110i\u1ec1n proxy v\u00e0o \u0111\u00e2y ...!", None))
        self.label_6.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"S\u1ed1 l\u01b0\u1ee3ng proxy : 0", None))
        self.label_7.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"LIVE : 0", None))
        self.label_8.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"DIE : 0", None))
        self.plainTextEdit_3.setPlainText("")
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Live ...", None))
        self.plainTextEdit_4.setPlainText("")
        self.plainTextEdit_4.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Die ...", None))
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Tr\u1ea1ng Th\u00e1i.....", None))
        self.tongacc.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"T\u1ed5ng acc : ", None))
        self.dangchonstt.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Selected :", None))
        self.livestt.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Live : ", None))
        self.diestt.setText(QCoreApplication.translate("Fasttool_Telegram_UI", u"Die :", None))
    # retranslateUi

