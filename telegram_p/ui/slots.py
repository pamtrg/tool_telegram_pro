
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
# from twitter.application.ui.ui_main import Ui_MainWindow
from Telegram_pro import MainWindow
from ..widgets.py_table_widget import PyTableWidget
class Slots(MainWindow):
    
    def __init__(self,parent_:MainWindow):
       
        self.parent_ = parent_
    @Slot(list)
    def add_admin(self,admins):
        self.parent_.admins = admins
    @Slot(int)
    def stt_start_stop(self,c_):
        if c_ == 0:
   
            QMessageBox.information(self.parent_, 'Thông báo', 'Hoàn tất')
    @Slot(str)
    def stt_error(self,text):
   
   
        QMessageBox.information(self.parent_, 'Thông báo', text)

    @Slot(str)
    def Info_stt(self,text):
        try:
            QMessageBox.information(self.parent_, 'Thông báo', text)
        except Exception as ex:
            print(ex,'Info_stt')

    @Slot(dict,str)
    def status_table(self,dict_,text):
        # print(text)

        try:
            item = QTableWidgetItem(text)
            # self.self_.tableWidget__reg.setItem(dict_['row'], self.self_.config['tableWidget__reg']['STATUS']['loc'], item)
            if dict_['otp_run'] in ['Home','group','spam','get','mes']:
                self.parent_.ui.tableWidget__home.setItem(dict_['row'], self.parent_.core.config_tableWidget__home['STATUS']['loc'], item)
            else:
                # print(self.self_.tableWidget__reg.rowCount())
                self.parent_.ui.tableWidget__home.setItem(dict_['row'], self.config_table['tableWidget__reg']['STATUS']['loc'], item)
        except Exception as e:
            print(e,9)


    @Slot(str, int, str)
    def status_all(self,otp,row,text):
        tableWidget: PyTableWidget = self.parent_.ui.tableWidget__home
        item = QTableWidgetItem(str(text))
        tableWidget.setItem(row, tableWidget.config[otp]['loc'], item)
    @Slot(str,int)
    def stt_proxy(self,text,otp):
        if otp == 1:
            self.parent_.ui.plainTextEdit_3.appendPlainText(text)
   
        else:
            self.parent_.ui.plainTextEdit_4.appendPlainText(text)
         
            


    @Slot(list)
    def status_get_mem(self,list_):
        tableWidget: PyTableWidget = self.parent_.ui.tableWidget__getmem
        self.parent_.count_getmem = self.parent_.count_getmem +1
        self.parent_.ui.label_2.setText('Total {}'.format(str(self.parent_.count_getmem)))
        # print(list_)

        row = tableWidget.add_row()
 
        tableWidget.add_value_tab(row,list_)


    @Slot(str, int, str)
    def status_add_mem_from_user(self,otp,row,text):
        tableWidget: PyTableWidget = self.parent_.ui.tableWidget__addmem

 
        item = QTableWidgetItem(str(text))

        tableWidget.setItem(int(row), tableWidget.config[otp]['loc'], item)

    @Slot(str)
    def status_getmem_nolink(self,text):
        PlainTextEdit: QPlainTextEdit = self.parent_.ui.plainTextEdit_5

        PlainTextEdit.appendPlainText(text)

 
    @Slot(str)
    def add_data_addmem_id(self,id_):
        self.parent_.list_data_addmem_check_index.append(id_)
        tableWidget: PyTableWidget = self.parent_.ui.tableWidget__addmem
        row = tableWidget.add_row()
        j = [id_,row]
        
        tableWidget.add_value_tab(row,j)
    @Slot()
    def stt_addmem_success(self):
        self.parent_.count_addmem_success = self.parent_.count_addmem_success +1
        self.parent_.ui.stt_thanhcong.setText(f'Thành công : {self.parent_.count_addmem_success}')
    @Slot()
    def stt_addmem_fail(self):
        self.parent_.count_addmem_fail = self.parent_.count_addmem_fail +1
        self.parent_.ui.thatbaistt.setText(f'Thất bại : {self.parent_.count_addmem_fail}')