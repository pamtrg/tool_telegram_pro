


from os_core import *
from telegram_p.widgets.friend_message_button.friend_message_button import FriendMessageButton
from .json_themes import Themes
from .json_settings import Settings
from ..ui.create_ui import Create_Ui
from .operazione_sql import SQL_Database_P
from ..ui.add_qdi.add import Dialog_UI_taothumuc, Dialog_UI_nhaptaikhoan
from .core_functions import Core_Functions
import threading
from ..ui.slots import Slots
from ..ui.signals import Connect_all_Signals
from .start_run import Start_fun
from ..widgets.py_table_widget import PyTableWidget
from .var_all import VarAll
from qt_core import *
from Telegram_pro import MainWindow
from Worker_thread import Worker,WorkerSignals
# from getcookie import getCookie
def get_or_create_eventloop():
    try:
        return get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = new_event_loop()
            set_event_loop(loop)
            return get_event_loop()
class Task(threading.Thread):

    def __init__(self,name,namefunc):
        threading.Thread.__init__(self,target=namefunc,name=name,daemon=True)

        threads=list(filter(lambda x: type(x) is Task,threading.enumerate()))
        if len(threads) == 0:
            self.start()
        else:
            self.stt = 1




class Core:
  

    def __init__(self, parent : MainWindow = None):
        self.parent = parent
        self.themes = Themes()
        self.settings = Settings()
        self.loop = get_or_create_eventloop()
        self.slot = Slots(parent)
        
        self.signals = Connect_all_Signals()
        self.SQL = SQL_Database_P()
        self.start_ = Start_fun(self.parent)
        self.Create_Ui_ = Create_Ui(self.themes.items, self.settings.items, self.parent)
        self.function_run = None
        self.Var_All = VarAll()
        self.threadpool = QThreadPool()
        self.threads = []

        self.signals.Notif_updated.connect(self.slot.status_all)
        self.signals.Notif_stt.connect(self.slot.Info_stt)
        self.signals.get_mem_updated.connect(self.slot.status_get_mem)
        self.signals.get_mem__nolink.connect(self.slot.status_getmem_nolink)
        self.signals.add_mem_updated_from_user.connect(self.slot.status_add_mem_from_user)
        self.signals.add_data_from_user.connect(self.slot.add_data_addmem_id)
        self.signals.stt_fail.connect(self.slot.stt_addmem_fail)
        self.signals.Notif_stt_proxy.connect(self.slot.stt_proxy)
        self.signals.stt_success.connect(self.slot.stt_addmem_success)
        # self.startThreads(
        #     getCookie
        # )
    def startThreads(self,fn,*args, **kwargs):
        worker = Worker(fn,*args, **kwargs)
        worker.signals.finished.connect(self.slot.stt_start_stop)
        worker.signals.error.connect(self.slot.stt_error)
        self.threadpool.start(worker)
  
    def save_config_data(self):
        # save file json
        try:
            with open('Database\\proxy.txt','w') as f:
                # f.write(self.parent.ui.comboBox_2.currentText()+'\n')
                proxys = self.parent.ui.plainTextEdit.toPlainText().split('\n')
                for proxy in proxys:
                    f.write(proxy+'\n')
            QMessageBox.warning(self.parent, 'Lỗi', 'Lưu file thành công !')

        except Exception as ex:
            print(ex)
            QMessageBox.warning(self.parent, 'Lỗi', 'Không thể lưu file')
    # a setter function
    def set_config_data(self):
        try:
            with open('Database\\proxy.txt') as f:
                fs = f.read().splitlines()
     
                # self.parent.ui.comboBox_2.setCurrentIndex(self.parent.ui.comboBox_2.findText(fs[0]))
                self.parent.ui.plainTextEdit.appendPlainText("\n".join(fs))
        except Exception as ex:
            print(ex)
            # QMessageBox.warning(self.parent, 'Lỗi', 'Không thể lấy dữ liệu')
    def change_stt_label(self, a):

        self.parent.ui.dangchonstt.setText(f'Đang chọn : {a}')

    def setup_core(self):
        
        self.parent.ui.comboBox_3.addItems([
            '1 Day',
            '2 Day',
            '3 Day',
            '4 Day',
            '5 Day',
            '6 Day',
            '7 Day',
            '8 Day',
            '9 Day',
            '10 Day',
            '11 Day',
            '12 Day',
            '13 Day',
            '14 Day',
            '15 Day',


        ])
        self._list_Data_kickban = []
        self._Data_kickban = []
        self.list_data_message_kickban = []
        self.parent.ui.comboBox_6.addItems(
                ["Add members by USERNAME", "Add members by PHONE", "Add members by ID"]
            )
        def handle_item_clicked(s):
            tx = self.parent.ui.tableWidget__home.item(s.row(),s.column())
         
            copy_text(
                tx.text(),
            )

        self.parent.ui.tableWidget__home = self.Create_Ui_.Create_TableWidget(
            "tableWidget__home", self.parent.ui.verticalLayout_2)
        self.parent.ui.tableWidget__home.itemClicked.connect(
            lambda : Core_Functions.handle_item_clicked(self.parent))
        self.parent.ui.tableWidget__home.doubleClicked.connect(
           handle_item_clicked)
         


        # convert dict keys to list

    

        
        self.parent.ui.comboBox_5.addItems([k  for  k in  self.parent.ui.tableWidget__home.config.keys() if k != ""])


        self.parent.ui.tableWidget__seeding = self.Create_Ui_.Create_TableWidget(
            "tableWidget__seeding", self.parent.ui.verticalLayout_29)
        # self.parent.ui.tableWidget__seeding.add_row()

        self.parent.ui.tableWidget__getmem = self.Create_Ui_.Create_TableWidget(
            "tableWidget__getmem", self.parent.ui.verticalLayout_21)
 
        self.parent.ui.tableWidget__addmem = self.Create_Ui_.Create_TableWidget(
            "tableWidget__addmem",self.parent.ui.verticalLayout_30)
        
        self.parent.ui.tableWidget_kickban = self.Create_Ui_.Create_TableWidget(
            "tableWidget_kickban",self.parent.ui.verticalLayout_51)
        self.parent.ui.tableWidget__addkickban = self.Create_Ui_.Create_TableWidget(
            "tableWidget__addkickban",self.parent.ui.verticalLayout_37)


        self.parent.ui.tableWidget__spammes = self.Create_Ui_.Create_TableWidget(
            "tableWidget__spammes",self.parent.ui.verticalLayout_39)

        self.parent.ui.pushButton_6.clicked.connect(
            lambda:Core_Functions.load_data_addmem(self.parent))

        self.parent.ui.lineEdit.textChanged.connect(
            lambda: Core_Functions.findUid(self.parent))
        self.parent.ui.pushButton_17.clicked.connect(
            lambda: Core_Functions._Export_Data_Getmem(self.parent))
        self.parent.ui.pushButton.clicked.connect(
            lambda: [Dialog_UI_nhaptaikhoan(self.parent).exec_()])
        self.parent.ui.pushButton_3.clicked.connect(
            lambda: Dialog_UI_taothumuc(self.parent).exec_())
        self.parent.ui.pushButton_46.clicked.connect(
            lambda: Core_Functions.load_data_list_kickban(self.parent)
        )
        self.parent.ui.pushButton_30.clicked.connect(
            lambda:Core_Functions.load_data_spammes_(self.parent)
        )
        
        self.parent.ui.comboBox.currentTextChanged.connect(self.setDatabase)
        self.parent.ui.lineEdit.textChanged.connect(self.setDatabase)
        self.parent.ui.pushButton_11.clicked.connect(self.remove_table)
        self.parent.ui.pushButton_2.clicked.connect(self.setDatabase)
        self.parent.ui.pushButton_41.clicked.connect(self.save_config_change_account)
        
        self.parent.ui.btn_start.clicked.connect(self.Run_Proces)
        self.parent.ui.btn_stop.clicked.connect(lambda:self.start_.loop_handler.loop.stop())
        # self.parent.ui.pushButton_33.clicked.connect(self.save_config_data)
        self.parent.ui.pushButton_7.clicked.connect(self.save_config_addmem)
        self.parent.ui.pushButton_12.clicked.connect(self.GetListNameGroup)
        self.parent.ui.pushButton_45.clicked.connect(lambda:Core_Functions.save_data_kickban(self.parent))
        self.parent.ui.pushButton_29.clicked.connect(lambda:Core_Functions.add_data_kickban(self.parent))
        self.parent.ui.pushButton_44.clicked.connect(lambda:Core_Functions.clean_data_kickban(self.parent))
        self.parent.ui.pushButton_43.clicked.connect(lambda:Core_Functions.load_data_meskichban_file(self.parent))
        self.parent.ui.pushButton_42.clicked.connect(lambda:Core_Functions.load_data_meskichban_image(self.parent))
        self.parent.ui.pushButton_9.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QPlainTextEdit= self.parent.ui.plainTextEdit))
        self.parent.ui.plainTextEdit.textChanged.connect(lambda : self.parent.ui.label_6.setText("Tổng proxy : " +  str(len(self.parent.ui.plainTextEdit.toPlainText().split('\n')))))
        self.parent.ui.pushButton_4.clicked.connect(lambda: self.save_config_data())
        self.parent.ui.pushButton_49.clicked.connect(lambda : Core_Functions.loadData_Seeding(self.parent))
       
       
        self.parent.ui.label_7.setText('')
        self.parent.ui.label_8.setText('')
        self.parent.ui.plainTextEdit_2.hide()
        self.parent.ui.pushButton_14.clicked.connect(lambda: self.startThreads(
            Core_Functions.Checklive,
            self.parent
        ))
        # self.parent.ui.pushButton_21.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QPlainTextEdit= self.parent.ui.plainTextEdit_7))
        # self.parent.ui.pushButton_15.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QPlainTextEdit= self.parent.ui.plainTextEdit_6))
        # self.parent.ui.pushButton_18.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QLine = self.parent.ui.lineEdit_7))
        # self.parent.ui.pushButton_19.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QLine = self.parent.ui.lineEdit_8))

        # self.parent.ui.pushButton_22.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QLine = self.parent.ui.lineEdit_14,filter = "*.txt"))
        # self.parent.ui.pushButton_37.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QLine = self.parent.ui.lineEdit_18,filter = "*.txt"))
        # self.parent.ui.pushButton_48.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QLine = self.parent.ui.lineEdit_13,filter = "Folder"))
        # self.parent.ui.pushButton_36.clicked.connect(lambda:Core_Functions.set_text_open_file(self.parent,QLine = self.parent.ui.lineEdit_17,filter = "Folder"))
        self.parent.ui.pushButton_8.clicked.connect(
            lambda: 
            self.startThreads(
                os.system,
                f"update.exe --pid {self.parent.pid} --pad {self.parent.pathtoool}" 
            )
            
        )
      
        self.parent.ui.comboBox_2.addItems(
            self.settings.items['proxy']
   
        )

        # self.startThreads(
        #     os.system,
        #     f"update.exe --pid {self.parent.pid} --pad {self.parent.pathtoool}" 
        # )
      
        # self.parent.ui.pushButton_13.clicked.connect(lambda:self.startThreads(Core_Functions.loc_trung,self.parent))
        # self.parent.ui.plainTextEdit_6.textChanged.connect(lambda:
        #     self.parent.ui.label_10.setText('Total : {}'.format(len(list(self.parent.ui.plainTextEdit_6.toPlainText().split("\n")))) )
        # )
        self.parent.ui.comboBox_6.currentTextChanged.connect(self.set_state_addmem)
        # get value plainTextEdit_6 text
        

        self.set_config_data()
    
        # show list table name
        self.Show_combobox()
        # set data
        self.setDatabase()


        # setup input
        Core_Functions.setup_Input(self.parent,
        [
            self.parent.ui.maxsize,
            self.parent.ui.delayb,
            self.parent.ui.delaya,


        ])
        self.Var_All.set_var(
            'home_table',[
                'Check Live With Session',
                'Check Live With Bot',
                'Check account information'

            ]
        )
        self.Var_All.set_var(
            'group_channel',[
                'Get Mem No Link',
                'Get Mem With Link'
            ]
        )
        self.load_config_addmem()
        self.set_state_addmem()
        self.set_config_change_account()
        
        self.parent.ui.stackedWidget_19.setCurrentWidget(self.parent.ui.page)
        self.parent.ui.stackedWidget_29.setCurrentWidget(self.parent.ui.stackedWidget_29Page1)

  

        # rs = FriendMessageButton(
        #     1,r"D:\tool_telegram_pro\Assets\48x48\1564506_close_exit_logout_power_icon.png",'Phạm Trường','0902212504',None,0,0
        # )
        # self.parent.ui.messages_layout.addWidget(rs)
    def addusser(self):
        for i in range(10):
            rs = FriendMessageButton(
                i,r"D:\tool_telegram_pro\Assets\48x48\1564506_close_exit_logout_power_icon.png",'Phạm Trường','0902212504',None,0,0
            )
            self.parent.ui.messages_layout.addWidget(rs)
    def GetListNameGroup(self):
        self.function_run = 'Get List Name Group'
        self.parent.ui.plainTextEdit_5.clear()
        self.Run_Proces()
    def set_state_addmem(self):
        index_t = self.parent.ui.comboBox_6.currentText()
        if index_t == 'Add members by USERNAME':
            self.parent.ui.spinBox_4.hide()
            self.parent.ui.label_5.hide()
            self.parent.ui.lineEdit_4.hide()
            self.parent.ui.label.show()
            self.parent.ui.label_3.show()
            self.parent.ui.spinBox_2.show()
            self.parent.ui.spinBox_3.show()
        elif index_t == 'Add members by PHONE':
            self.parent.ui.spinBox_4.hide()
            self.parent.ui.label_5.hide()
            self.parent.ui.lineEdit_4.hide()
            self.parent.ui.label.show()
            self.parent.ui.label_3.show()
            self.parent.ui.spinBox_2.show()
            self.parent.ui.spinBox_3.show()
        elif index_t == 'Add members by ID':
            self.parent.ui.spinBox_4.show()
            self.parent.ui.label_5.show()
            self.parent.ui.lineEdit_4.show()
            self.parent.ui.label.show()
            self.parent.ui.label_3.show()
            self.parent.ui.spinBox_2.show()
            self.parent.ui.spinBox_3.show()
        




    def set_config_change_account(self):
        try:
         
            with open(r'config\cauhinh.json','r') as f:
                dict_ = json.load(f)
                self.parent.ui.lineEdit_14.setText(dict_['PathUsername'])
                self.parent.ui.lineEdit_18.setText(dict_['PathBio'])
                self.parent.ui.lineEdit_17.setText(dict_['PathFolderImage'])
                self.parent.ui.lineEdit_13.setText(dict_['PathFullname'])
        except Exception as e:
            print(e)
            # QMessageBox.warning(self.parent, 'Lỗi', 'Không thể lấy dữ liệu')
    def save_config_change_account(self):
        try:
            dict_ = {
                'PathUsername':self.parent.ui.lineEdit_14.text(),
                'PathBio':self.parent.ui.lineEdit_18.text(),
                'PathFolderImage':self.parent.ui.lineEdit_17.text(),
                'PathFullname':self.parent.ui.lineEdit_13.text(),
            }
            with open(r'config\cauhinh.json','w') as f:
                json.dump(dict_,f)
            QMessageBox.information(self.parent, 'Thông báo', 'Lưu thành công')
        except Exception as e:
            print(e)
            QMessageBox.warning(self.parent, 'Lỗi', 'Không thể lưu dữ liệu')

        
        
    def save_config_addmem(self):
        #write file json
        try:
            dict_ = {}
            with open(r'config\addmem.json', 'w') as f:
                dict_['linkgr_add'] = self.parent.ui.lineEdit_6.text()
                dict_['link_clone'] = self.parent.ui.lineEdit_4.text()
                dict_['ands'] = [self.parent.ui.spinBox_2.value(), self.parent.ui.spinBox_3.value()]
                dict_['total_count_add'] = self.parent.ui.spinBox.value()
                dict_['total_clone'] = self.parent.ui.spinBox_4.value()
                json.dump(dict_, f, indent=4)
                QMessageBox.information(self.parent, 'Thông báo', 'Lưu thành công')
        except Exception as ex:
            print(ex)
            QMessageBox.warning(self.parent, 'Lỗi', 'Không thể lưu file')
    def load_config_addmem(self):
        # read file json
        try:
            with open(r'config\addmem.json', 'r') as f:
                cauhinhs_addmem = json.load(f)
                self.parent.ui.spinBox_2.setValue(cauhinhs_addmem['ands'][0])
                self.parent.ui.spinBox_3.setValue(cauhinhs_addmem['ands'][1])
                self.parent.ui.spinBox.setValue(cauhinhs_addmem['total_count_add'])
                self.parent.ui.spinBox_4.setValue(cauhinhs_addmem['total_clone'])
                self.parent.ui.lineEdit_6.setText(cauhinhs_addmem['linkgr_add'])
                self.parent.ui.lineEdit_4.setText(cauhinhs_addmem['link_clone'])
                
        except Exception as ex:
            print(ex)
            QMessageBox.warning(self.parent, 'Lỗi', 'Không thể lấy dữ liệu')



    def Chech_Input(self):
        tableWidget__home: PyTableWidget = self.parent.ui.tableWidget__home
        if self.parent.ui.maxsize.text() == '':
            QMessageBox().warning(self.parent, 'Lỗi', 'Vui lòng nhập Số Luồng')
            return False
        elif self.parent.ui.delayb.text() == '' or self.parent.ui.delaya.text() == '':
            QMessageBox().warning(self.parent, 'Lỗi', 'Vui lòng nhập Delay')
            return False
        elif len(tableWidget__home.get_data_from_table()) == 0:
            QMessageBox().warning(self.parent, 'Lỗi', 'Vui lòng chọn Tài Khoản')
            return False

        return True
        


    def Get_config_run(self):
        
        if self.Chech_Input():
            tableWidget__home: PyTableWidget = self.parent.ui.tableWidget__home
            list_account = tableWidget__home.get_data_from_table()
            if self.function_run == 'Get List Name Group':
                list_account = [list_account[0]]
            proxys = self.parent.ui.plainTextEdit.toPlainText().split("\n")
            list_proxy = []
            for proxy in proxys:
                if ':' in proxy:
                    list_proxy.append(proxy)
            if len(list_proxy) == 0:
                self.signals.Notif_stt.emit('Vui lòng import Proxy')
                return False
        
            Config_run = {
                'list_account': list_account,
                'list_proxy':list_proxy,
                'List_check':{
                    'count_proxy':0
                },
                'cauhinh':{            
                    'maxsize':int(self.parent.ui.maxsize.text()) if int(self.parent.ui.maxsize.text()) >= 1 else 1,
                    'name_table': self.parent.ui.comboBox.currentText(),
                    'dalay_before': [int(self.parent.ui.delaya.text()),int(self.parent.ui.delayb.text())],
                    'function_run': self.function_run
                }

            }
            if self.function_run == None or self.parent.ui.stackedWidget_4.currentIndex() != 0 and self.function_run != 'Get List Name Group':
                # print(self.parent.ui.stackedWidget.currentIndex())
            

                if self.parent.ui.stackedWidget_4.currentIndex() or self.parent.ui.stackedWidget.currentIndex() == 1:
                    ftn = Core_Functions.get_function_run(self.parent,Config_run['cauhinh'])
                    if ftn:
                        Config_run['cauhinh']['function_run'] = ftn
                   
                 
                else:
                    QMessageBox().warning(self.parent, 'Lỗi', 'Vui lòng chọn chức năng')
                    return False
            return Config_run
        return False



    def Stop_Proces(self):
        self.start_.loop_handler.loop.stop()
        self.start_.tasks = []
     
   

    def Run_Proces(self):
   
        Config_run = self.Get_config_run()
        if Config_run:
            if self.start_.loop_handler.loop.is_running() != True:
                self.start_ = Start_fun(self.parent)
            self._thread = threading.Thread(
                target=self.start_.Add_Thead,args=(Config_run,), daemon=True, name="nemo"
            )
            self._thread.start()
    def Show_combobox(self):
        self.parent.ui.comboBox.addItems(self.SQL.list_Table_names)

    def setDatabase(self):
        self.data_Database = self.SQL.Get_data(
            self.parent.ui.comboBox.currentText())
        # print(self.data_Database)
        self.parent.ui.tongacc.setText(f'Tổng acc : {len(self.data_Database)}')
        if len(self.data_Database) >= 1:
            self.parent.ui.tableWidget__home.setDatabaseOnTable(
                self.data_Database)

        else:
            self.parent.ui.tableWidget__home.setRowCount(0)

    def Create_Table(self, __tablename__):

        if self.SQL.Create_Table(__tablename__) == 1:

            self.parent.ui.comboBox.insertItem(0, __tablename__)
            self.parent.ui.comboBox.setCurrentText(__tablename__)

            QMessageBox.information(
                self.parent, "Thông báo", "Tạo bảng thành công")
            return 1

        else:
            QMessageBox.warning(self.parent, "Warning", "Tạo thất bại")
            return 0

    def Insert_Data(self, __tablename__, __data__,__password__):
        # print(__data__)
        # if __data__[0][0] == '+':

        res =  self.SQL.Insert_Data(__tablename__, __data__,__password__)
        if res:
         
            self.setDatabase()
        return res


    def remove_table(self):

        response = QMessageBox.warning(
            self.parent, "Exit?", "Are you sure you want to delete the table ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if response == QMessageBox.Yes:
            tablename = self.parent.ui.comboBox.currentText()
            self.parent.ui.comboBox.removeItem(
                self.parent.ui.comboBox.findText(tablename))
            if self.SQL.remove_table(tablename):
                QMessageBox.information(
                    self.parent, "Thông báo", "Xóa bảng thành công")
            else:
                QMessageBox.warning(self.parent, "Warning", "Xóa thất bại")
            self.SQL.list_Table_names = self.SQL.Get_list_Table()
    