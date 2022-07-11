from .nhaptaikhoan import Ui_Dialog as UI_nhaptaikhoan
from .taothumuc import Ui_Dialog as UI_taothumuc
from .dichuyenaccount import Ui_Dialog as Ui_dichuyenaccount
from Telegram_pro import MainWindow
from ...core.core_functions import Core_Functions
from qt_core import *
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import PhoneCodeEmptyError,PhoneNumberInvalidError,SessionPasswordNeededError,PasswordHashInvalidError
from telethon.tl.types import *
import asyncio
class Dialog_Ui_dichuyenaccount(QDialog, Ui_dichuyenaccount):
    def __init__(self, parent:MainWindow = None):
        QDialog.__init__(self, parent)
        self.dragPos = None
        
        self.setupUi(self)
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)



        self.comboBox.addItems(parent.core.SQL.Get_list_Table())
        self.pushButton.clicked.connect(lambda:parent.core.startThreads(
                Core_Functions.dichuyenacount,
                parent,self.comboBox.currentText()))
       



        def moveWindow(event):
            try:
                if event.buttons() == Qt.LeftButton:
                    p = event.globalPosition()
                    globalPos = p.toPoint()

                    self.move(self.pos() + globalPos - self.dragPos)
                    self.dragPos = globalPos
                    event.accept()
            except:
                pass
        self.widget.mouseMoveEvent = moveWindow
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos




class Dialog_UI_taothumuc(QDialog,UI_taothumuc):
    def __init__(self, parent:MainWindow = None):
        QDialog.__init__(self, parent)
        self.dragPos = None
        self.parent_ = parent
        
        self.setupUi(self)
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)



        self.pushButton.clicked.connect(lambda:self.create_table(self.lineEdit.text()))
       



        def moveWindow(event):
            try:
                if event.buttons() == Qt.LeftButton:
                    p = event.globalPosition()
                    globalPos = p.toPoint()

                    self.move(self.pos() + globalPos - self.dragPos)
                    self.dragPos = globalPos
                    event.accept()
            except:
                pass
        self.widget.mouseMoveEvent = moveWindow
    def create_table(self,name):
        if self.parent_.core.Create_Table(name):
            self.close()
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos



class Dialog_UI_nhaptaikhoan(QDialog,UI_nhaptaikhoan):
    def __init__(self, parent:MainWindow = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.dragPos = None
        self.SQL = parent.core.SQL
     
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
  

        self.comboBox.addItems(parent.core.SQL.Get_list_Table())
        self.pushButton_2.clicked.connect(lambda:Core_Functions.set_text_open_file(self,QPlainTextEdit = self.plainTextEdit,filter = "Folder"))
        self.pushButton.clicked.connect(
            lambda:parent.core.startThreads(
                parent.core.Insert_Data,
                self.comboBox.currentText(),
                self.plainTextEdit.toPlainText().strip().split('\n'),
                self.lineEdit.text().strip()
            ))
        self.pushButton_3.clicked.connect(lambda:QMessageBox.warning(self, 'Warning', 'Vui lòng đợi bản update !'))
    
        def moveWindow(event):
            try:
                if event.buttons() == Qt.LeftButton:
                    p = event.globalPosition()
                    globalPos = p.toPoint()

                    self.move(self.pos() + globalPos - self.dragPos)
                    self.dragPos = globalPos
                    event.accept()
            except:
                pass
        self.widget.mouseMoveEvent = moveWindow
    
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

    async def add_account(self):
    
       
        
        otp = self.pushButton_3.text()

        

    
        try:
            phone_number = self.lineEdit_2.text()
            
            
            if otp == 'Login':
                
                if phone_number == '':
                    QMessageBox.warning(self, 'Warning', 'Please enter a phone number')
                else:
                    try:
                        await self.client.log_out()

                    except:
                        pass
                    try:
                        await self.client.disconnect()
                    except:
                            pass
                     
                    self.client = TelegramClient(f'Database\\Account\\AddNew\\{phone_number}', 7134163, '2f44d3200456c46ffea61ada8c8bfaec')
                    
                    await self.client.connect()
               
                    if not await self.client.is_user_authorized():
                      
                        try:
                        
                            result = await self.client.send_code_request(phone_number,force_sms=False)
                            print(result)
                            # if isinstance(result.type, auth.SentCodeTypeApp):
                            self.pushButton_3.setText('Điền code !')
                                # QMessageBox.warning(self, 'Warning', 'Đã gửi code !')



                             
                        except Exception as e:
                            print(e,e)
            elif otp == 'Điền code !':
                try:
                    await self.client.sign_in(phone_number, self.lineEdit_3.text())
                    QMessageBox.warning(self, 'Warning', 'Thêm account Thành Công')
                    self.SQL.Add_row(self.comboBox.currentText(),[{'SESSION':str(phone_number)+'.session','PATH':'Database\\Account\\AddNew\\'}])
                    self.pushButton_3.setText('Login')
                    await self.client.disconnect()
                except PhoneCodeEmptyError:
                    QMessageBox.warning(self, 'Warning', 'The phone code is empty')
                    # print( 'The phone code entered was invalid')
                except PhoneNumberInvalidError:
                    QMessageBox.warning(self, 'Warning', 'The phone number is invalid')
                    # print('The phone number is invalid') 
                except SessionPasswordNeededError:
                    self.pushButton_3.setText('2FA')
        
            elif otp == '2FA':
                try:
                    await self.client.sign_in(password= self.lineEdit.text())
                    QMessageBox.warning(self, 'Warning', 'Đăng Nhập Thành Công')
                    self.SQL.Add_row(self.comboBox.currentText(),[{'SESSION':str(phone_number)+'.session','PATH':'Database\\Account\\AddNew\\'}])
                    self.pushButton_3.setText('Login')
                    await self.client.disconnect()
                    # print('Đăng Nhập Thành Công')
                except PasswordHashInvalidError:
                    
                    QMessageBox.warning(self, 'Warning', 'The password is invalid')
                    # print('The password (and thus its hash value) you entered is invalid')
                    # return 'The password (and thus its hash value) you entered is invalid'
            # else:
            #     # print('Đã tồn tại account!')
            #     QMessageBox.warning(self, 'Warning', 'Đã tồn tại account!')
            # if otp == 'Login':
            #     await client.disconnect()
            
        except Exception as e:
            print(e)
            await self.client.log_out()
            QMessageBox.warning(self, 'Warning', str(e))