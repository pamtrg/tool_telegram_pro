
import threading
from time import sleep
from telegram_p import *
from login import Ui_Dialog
from qt_core import *
from os_core import *
import platform
from os import getpid
# from googletrans import Translator

# print(Translator().detect('Xin chào'))
os.environ["QT_FONT_DPI"] = "96" 
 






class Update:
    def __init__(self) -> None:
        pass




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.dragPos = None
        self.otp_running = 'Home'
        self.funt_run = None
        self.list_session = []

        self.ui = Ui_Fasttool_Telegram_UI()
        self.ui.setupUi(self)
        self.switch_Tab_ = switch_Tab(self)
        
        self.core = Core(self)
        self.core.setup_core()
     
        UIFunctions.uiDefinitions(self)
     
        # self.ui.pushButton_20.setText(str(get_mac()))


        self.show()
        self.pid = getpid()
        self.pathtoool = __file__
        
        # self.ui.pushButton_8.clicked.connect(
        #     lambda:os.system(r"update.exe --pid %s" % self.pid)
        # )
        

        #disble close button
        # self.ui.pushButton_6.hide()
        # self.ui.btn_spam_tinnhan.hide()
        # self.ui.radioButton.hide()
        # self.ui.radioButton_2.hide()
        self.ui.btn_chat_kichban.hide()
        # self.ui.btn_quanytacvu.hide()
        # btn coppy

        self.ui.frame_2.hide()
        
        # self.ui.pushButton_20.clicked.connect(lambda:copy_text(self.ui.pushButton_20.text()))


        # self.ui.commandLinkButton.clicked.connect(lambda:open_web('https://www.facebook.com/100007040733216/'))


        self.ui.btn_home.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_home.styleSheet()))
       
        # _app = QApplication.instance()
        # trans = QTranslator(self)
        # trans.load('eng-chs')
        # _app.installTranslator(trans)
     
        # print(self.Get_all_widgets())
    def Get_all_widgets(self):
        widgets = {}
        # tran = Translator()
        
        translator = Translator(
            user_agent=r"Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",service_urls=[
            'translate.google.com',
            'translate.google.co.kr',
            ]
        )
        try:
            with open(f'config\\lang.json', 'r') as f:
                lang = json.load(f)
        except:
            lang = {}

        # print(lang)
        for widget in self.findChildren(QWidget):
            try:
                # if lang.get(widget.objectName()):
                widget.setText(lang.get(widget.objectName()))
                # else:
                #     text = translator.translate(widget.text()).text
                #     # widgets[widget.objectName()] =text
                #     lang[widget.objectName()] = text
                #     widget.setText(text)
                # print(Translator().translate(widget.text(), dest='vn').text)
# <T)
            except:
                pass
        with open(f'config\\lang.json', 'w') as f:
            json.dump(lang, f)
            # widgets.append(widget)
        return widgets




    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        # self.dragPos = event.globalPosition()
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
    def closeEvent(self, event):
        UIFunctions.Check_ask_button(self,event,"Exit?", "Are you sure quit?")
        # QMessageBox:beep
        
 
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)



def get_in4_tab():
    
    html = requests.get('https://docs.google.com/spreadsheets/d/1vCp9LjzBsSyl8LqHyS2sqM3liyGMWElsnfaa5GHhVLc/edit?usp=sharing').text
    soup = BeautifulSoup(html, "lxml")
    tables = soup.find_all("table")
    indexs = []
    for table in tables:
        ass = [[td.text for td in row.find_all("td")] for row in table.find_all("tr")]
        indexs.append(ass)
    return indexs
def Check_key(Key_devices):
    return True
    indexs = get_in4_tab()
    acp = False
    for j in indexs[0][2::]:

        if str(Key_devices) == j[0] and j[3] == indexs[0][11][6]:
            date_start = datetime.strptime(j[2], "%Y/%m/%d").date()
            for l in indexs[0][3:8]:
                if j[1] == l[6]:
                    day_add = int(l[7])
                    if day_add >= 9999:
                        acp = True
                        return acp
                    else:
                        end_date = date_start + timedelta(days=day_add)
                        if end_date > date.today():
                            acp = True
                            return acp
    return acp


class Dialog_UI_Login(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.lineEdit_7.setText(str(get_mac()))
        self.lineEdit_7.setDisabled(True)
        self.btn_close_2.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.resizeD)
        self.pushButton_5.clicked.connect(lambda:open_web(r'https://www.facebook.com/pamtrg/'))
        self.pushButton_4.clicked.connect(lambda:open_web(r'https://t.me/pamtrg'))
        self.pushButton_3.clicked.connect(lambda:[copy_text('+84918189170'), QMessageBox.information(self, 'Thông báo', 'Số điện thoại đã được copy vào clipboard')])
        self.pushButton.clicked.connect(lambda:[copy_text(str(get_mac())), QMessageBox.information(self, 'Thông báo', 'Public Key đã được copy vào clipboard')])
        self.pushButton_6.clicked.connect(self.Accept_Login)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                p = event.globalPosition()
                globalPos = p.toPoint()

                self.move(self.pos() + globalPos - self.dragPos)
                self.dragPos = globalPos
                event.accept()
        self.widget.mouseMoveEvent = moveWindow
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
    def Accept_Login(self):
        if self.pushButton_6.text() == 'Activated':
            self.main = MainWindow()
            self.main.ui.tittle.setText(name_ver)
            self.main.show()
            self.close()
        else:
            QMessageBox.information(self, 'Thông báo', 'Deactivated, vui lòng liên hệ Admin')
    def resizeD(self):
        
        while True:
            try:
                if self.widget_2.x() == 40:
                    x1,y1,x2,y2 = 40,25,380,60
                elif self.widget_2.x() == 380:
                    x1,y1,x2,y2 = 380,60,40,25
                self.anim = QPropertyAnimation(self.widget_2,b'geometry') # 
                self.anim.setDuration(1000) # 
                self.anim.setStartValue(QRect(x1,y1,370,460)) #
                self.anim.setEndValue(QRect(x2,y2,370,460)) #
                self.anim.start() # 


                break
            except:
                x1,y1,x2,y2 = 40,25,380,60
        # sleep(4)
        # if self.pushButton_6.text() == 'Activated':
        #     self.main = MainWindow()
        #     self.main.ui.tittle.setText(name_ver)
        #     self.main.show()
        #     self.close()
        # else:
        #     QMessageBox.information(self, 'Thông báo', 'Deactivated, vui lòng liên hệ Admin')


if __name__ == "__main__":
    '''Phiên bản giành riêng cho Đình Hương Nguyễn'''
    # name_ver = ' TELEGRAM PRO VER 3.2.8'
    name_ver = 'Fastsoft Telegram Pro'

    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.ico"))
    Dialog = Dialog_UI_Login()
  
    Dialog.label_4.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">{name_ver}</span></p></body></html>", None))
   


    if Check_key(str(get_mac())):
        Dialog.pushButton_6.setText('Activated')
        
    else:
        Dialog.pushButton_6.setText('Deactivated')



    Dialog.show()

    # translator = QTranslator()

    # a = QCoreApplication.installTranslator(translator)
    # print(a)
    # QFontDatabase.addApplicationFont("config/Alata-Regular.ttf")

    sys.exit(app.exec())





 
