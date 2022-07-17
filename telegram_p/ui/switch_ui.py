


from qt_core import *
from .ui_functions import UIFunctions
from Telegram_pro import MainWindow




def Remove_style(widgets,btn):
    for widget in widgets:
        widget.setStyleSheet("")
    btn.setStyleSheet('  border-bottom: 4px solid rgb(255, 255, 255) ;')

class switch_Tab:
    def __init__(self, parent: MainWindow):
       
        self.parent = parent
        self.Connect_btn()
    def Connect_btn(self ):
        self.parent.ui.btn_home.clicked.connect(lambda:self.switch_Btn(self.parent.ui.btn_home))
        self.parent.ui.btn_group.clicked.connect(lambda:self.switch_Btn(self.parent.ui.btn_group))
        self.parent.ui.btn_caidat.clicked.connect(lambda:self.switch_Btn(self.parent.ui.btn_caidat))
        self.parent.ui.btn_chat_kichban.clicked.connect(lambda:self.switch_Btn(self.parent.ui.btn_chat_kichban))
        self.parent.ui.btn_spam_tinnhan.clicked.connect(lambda:self.switch_Btn(self.parent.ui.btn_spam_tinnhan))
        

        #page manager
        self.parent.ui.btn_quanlyaccount.clicked.connect(lambda:self.switch_Dashboard(self.parent.ui.btn_quanlyaccount))
        self.parent.ui.btn_quanytacvu.clicked.connect(lambda:self.switch_Dashboard(self.parent.ui.btn_quanytacvu))
        # self.parent.ui.pushButton_34.clicked.connect(lambda:self.switch_Dashboard(self.parent.ui.pushButton_34))
     
        # btn group and channel
        self.parent.ui.btn_themthanhvien.clicked.connect(lambda:self.switch_Group_Channel(self.parent.ui.btn_themthanhvien))
        self.parent.ui.btn_locthanhvien_2.clicked.connect(lambda:self.switch_Group_Channel(self.parent.ui.page_4))
        self.parent.ui.btn_tienichgroup_channel.clicked.connect(lambda:self.switch_Group_Channel(self.parent.ui.btn_tienichgroup_channel))

        # page setting
      
        self.parent.ui.btn_proxy.clicked.connect(lambda:self.switch_Setting(self.parent.ui.btn_proxy))

    
        
        # spam setting
        self.parent.ui.pushButton_47.clicked.connect(lambda:self.switch_spam(self.parent.ui.pushButton_47))
        self.parent.ui.pushButton_32.clicked.connect(lambda:self.switch_spam(self.parent.ui.pushButton_32))
        self.parent.ui.pushButton_28.clicked.connect(lambda:self.switch_spam(self.parent.ui.pushButton_28))

        self.parent.ui.pushButton_20.clicked.connect(lambda:self.parent.ui.stackedWidget_6.setCurrentWidget(self.parent.ui.page_90))
        self.parent.ui.pushButton_31.clicked.connect(lambda:self.parent.ui.stackedWidget_6.setCurrentWidget(self.parent.ui.page_7))
        self.parent.ui.comboBox_8.currentTextChanged.connect(self.on_combobox_changed)
    def on_combobox_changed(self,value):
        # print(value)
      
        if value == 'Leave Groups or Channel':
            self.parent.ui.stackedWidget_3.setCurrentWidget(self.parent.ui.page_8)
        elif value == 'Join Group Or Channel':
            self.parent.ui.stackedWidget_3.setCurrentWidget(self.parent.ui.page_10)
        elif value == 'Buff view post Channel':
            self.parent.ui.stackedWidget_3.setCurrentWidget(self.parent.ui.page_9)
        elif value == 'Buff reaction post Channel or Group':
            self.parent.ui.stackedWidget_3.setCurrentWidget(self.parent.ui.page_5)

        elif value == 'Join Video Call':
            self.parent.ui.stackedWidget_3.setCurrentWidget(self.parent.ui.page_10)
        elif value == 'Buff Online':
            self.parent.ui.stackedWidget_3.setCurrentWidget(self.parent.ui.page_10)
        elif value == 'Scrape Data Message':
            self.parent.ui.stackedWidget_3.setCurrentWidget(self.parent.ui.page_6)
        elif value == 'Comment channel':
            self.parent.ui.stackedWidget_3.setCurrentWidget(self.parent.ui.page_11)

    def switch_spam(self,btn : QPushButton):
        Remove_style(self.parent.ui.frame_9.findChildren(QPushButton),btn)
        btnName = btn.objectName()
        # print(btnName)
        if btnName == "pushButton_47":
            self.parent.ui.stackedWidget_19.setCurrentWidget(self.parent.ui.stackedWidget_19Page1)
    
    
        elif btnName == "pushButton_32":
            self.parent.ui.stackedWidget_19.setCurrentWidget(self.parent.ui.page)
      
        elif btnName == "pushButton_28":
            i = self.parent.ui.stackedWidget_29.currentIndex()
            
            if i == 1:
                self.parent.ui.stackedWidget_29.setCurrentWidget(self.parent.ui.stackedWidget_29Page1)
            else:
                self.parent.ui.stackedWidget_29.setCurrentWidget(self.parent.ui.page_2)
    
    def switch_Btn(self,btn : QPushButton):
        # Remove_style(self.parent.ui.frame_7.findChildren(QPushButton),btn)
        btnName = btn.objectName()
        print(btnName)
        if btnName == "btn_home":
            self.parent.ui.stackedWidget_4.setCurrentWidget(self.parent.ui.bangdieukhien)
            self.parent.ui.stackedWidget.setCurrentWidget(self.parent.ui.page_account)
            UIFunctions.resetStyle(self.parent.ui, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            
        elif btnName == "btn_group":
            self.parent.ui.stackedWidget_4.setCurrentWidget(self.parent.ui.nhom_kenh)
            # self.parent.ui.getmemandaddmem.setCurrentWidget(self.parent.ui.addmem)
            UIFunctions.resetStyle(self.parent.ui, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        elif btnName == "btn_caidat":
            self.parent.ui.stackedWidget_4.setCurrentWidget(self.parent.ui.caidat)
            UIFunctions.resetStyle(self.parent.ui, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            # self.parent.ui.stackedWidget_4.setCurrentWidget(self.parent.ui.bangdieukhien_3)
        elif btnName == "btn_chat_kichban":
            self.parent.ui.stackedWidget_4.setCurrentWidget(self.parent.ui.chatkichban)
            UIFunctions.resetStyle(self.parent.ui, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        elif btnName == "btn_spam_tinnhan":
            self.parent.ui.stackedWidget_4.setCurrentWidget(self.parent.ui.spamtinnhan)
            UIFunctions.resetStyle(self.parent.ui, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    def switch_Dashboard(self,btn : QPushButton):
        Remove_style(self.parent.ui.frame.findChildren(QPushButton),btn)
        btnName = btn.objectName()
        # print(btnName)
        if btnName == "btn_quanytacvu":
            self.parent.ui.stackedWidget.setCurrentWidget(self.parent.ui.page_tacvu)
    

        
    
        elif btnName == "btn_quanlyaccount":
            self.parent.ui.stackedWidget.setCurrentWidget(self.parent.ui.page_account)


        elif btnName == "pushButton_34":
            self.parent.ui.stackedWidget.setCurrentWidget(self.parent.ui.page_3)
   
    def switch_Group_Channel(self,btn : QPushButton):
        # Remove_style(self.parent.ui.frame_7.findChildren(QPushButton),btn)
        btnName = btn.objectName()
     
     

    
        if btnName == "btn_themthanhvien":
            self.parent.ui.getmemandaddmem.setCurrentWidget(self.parent.ui.addmem)

        elif btnName == "btn_tienichgroup_channel":
            self.parent.ui.getmemandaddmem.setCurrentWidget(self.parent.ui.tienich_group_2)
        elif btnName == "page_4":
            self.parent.ui.getmemandaddmem.setCurrentWidget(self.parent.ui.page_4)

    def switch_Setting(self,btn : QPushButton):
        btnName = btn.objectName()
    
        if btnName == "btn_proxy":
            self.parent.ui.stackedWidget_2.setCurrentWidget(self.parent.ui.stack_proxy)

            # UIFunctions.resetStyle(self.ui, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
