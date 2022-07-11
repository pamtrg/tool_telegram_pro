
import psutil

from qt_core import *
import urllib.request
import json,requests,time,os
from update_ui import Ui_MainUpdate
from Worker_thread import Worker
import glob
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pid', type=str)
parser.add_argument('-pt', '--pad', type=str)
args = parser.parse_args()
pid = args.pid
pad = args.pad





class UI_Update(QMainWindow):
    change_value = Signal(int)
    set_state_stt = Signal(int)
    set_text_stt = Signal(str)
    def __init__(self,urlconfig,urltool,name_tool):
        QMainWindow.__init__(self)
        self.urlconfig = urlconfig
        self.urltool = urltool
        self.name_tool = name_tool
        self.ui = Ui_MainUpdate()
        self.threadpool = QThreadPool()

        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.widget.mouseMoveEvent = self.moveWindow
        self.ui.progressBar.hide()
        self.ui.label.setText('Đang kiểm tra phiên bản !')
        self.ui.pushButton_11.hide()
        self.ui.pushButton_2.clicked.connect(lambda:self.exit_pool())
        self.startThreads(
            self.Check_ver
        )
        self.ui.pushButton_11.clicked.connect(lambda:self.startThreads(self.start_dowload))
        self.change_value.connect(self.updateProgressBar)
        self.set_state_stt.connect(self.state_stt)
        self.set_text_stt.connect(self.text_stt)
        self.pathFile()
    @Slot(str)
    def text_stt(self,text):
        self.ui.label.setText(text)
    def pathFile(self):
        mylist = [f for f in glob.glob("*.exe")]
        return mylist


        
    def start_dowload(self):

        p = psutil.Process(int(pid))
        p.terminate()





        urllib.request.urlretrieve(self.urltool, self.name_tool+f' {self.version_new}.exe', self.progressing)
        mylist = self.pathFile()
        mylist.remove(self.name_tool+f' {self.version_new}.exe')
        mylist.remove('update.exe')
        self.set_text_stt.emit("Tải xuống hoàn tất")
        self.set_state_stt.emit(0)
        self.ui.pushButton_2.setText('Đóng')
        with open("config\\update.json",'r',encoding='utf-8-sig') as myfile:
            config_addmem_ = json.load(myfile)
        # wirte json
  
        config_addmem_['version'] = self.version_new
        with open("config\\update.json",'w',encoding='utf-8-sig') as myfile:
            json.dump(config_addmem_,myfile,indent=4)
            myfile.close()
        for path in mylist:
            os.remove(path)
        


    @Slot(int)
    def state_stt(self, val):
        if val:
            self.ui.pushButton_11.show()
            # self.ui.label.setText("Phiên bản hiện tại là phiên bản cũ, click OK để update !")
        else:
            self.ui.pushButton_11.hide()


    @Slot(int)
    def updateProgressBar(self, val):
        if val == 26062003:
            self.ui.progressBar.show()
        else:
            self.ui.progressBar.setValue(val)
    def progressing(self,block_num, block_size, total_size):
        self.change_value.emit(26062003)
        downloaded = block_num * block_size/1048576
        ok = round((block_num * block_size/total_size*100))
        if downloaded < total_size/1048576:
            self.change_value.emit(ok)
            self.set_text_stt.emit('Đang tải: '+str(round(downloaded,1))+" mb")
     
            # self.ui.label.setText('Kích thước: '+str(round(downloaded,1))+" mb")
    
        
    def exit_pool(self):
        self.threadpool.globalInstance().waitForDone()
        self.threadpool.deleteLater()

        sys.exit(0)


    def startThreads(self,fn,*args, **kwargs):
        worker = Worker(fn,*args, **kwargs)
        self.threadpool.start(worker)

    def moveWindow(self,event):
        if event.buttons() == Qt.LeftButton:
            p = event.globalPosition()
            globalPos = p.toPoint()

            self.move(self.pos() + globalPos - self.dragPos)
            self.dragPos = globalPos
            event.accept()
    def Check_ver(self):
    
        with open("config\\update.json",'r',encoding='utf-8-sig') as myfile:
            config_addmem_ = json.load(myfile)
            self.version_ex = config_addmem_['version']
        response = requests.get(self.urlconfig).json()
        self.version_new = response['version']
 
        if response['version'] != self.version_ex:
            time.sleep(2)
            self.set_state_stt.emit(1)
            self.set_text_stt.emit("Phiên bản hiện tại là phiên bản cũ, click OK để update !")
        else:
            self.set_text_stt.emit("Phiên bản hiện tại là phiên bản bản mới nhất !")
            self.ui.pushButton_2.setText('Đóng')

            

        

    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos





if __name__ == "__main__":
 
    name_ver = 'FastSoft Telegram Pro '


    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.ico"))

    urlconfig = 'https://raw.githubusercontent.com/pamtrg/Telegram_Pro/main/update.json'
    urltool = 'https://github.com/pamtrg/Telegram_Pro/raw/main/Telegram_pro.exe'
    Dialog = UI_Update(urlconfig,urltool,name_ver)





    Dialog.show()


    sys.exit(app.exec())

