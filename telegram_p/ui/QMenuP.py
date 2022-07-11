# from telegram.client.Task import  Task
from qt_core import *
from ..core.core_functions import Core_Functions
from ..widgets import PyTableWidget
from ..ui.add_qdi import Dialog_Ui_dichuyenaccount
from Telegram_pro import MainWindow
import os
class Create_QMenuP:
    def connect_QMenu(self: MainWindow,name,eventPosition : QPoint, child : PyTableWidget):
      
        if name == 'tableWidget__home':
            Create_QMenuP.QMenu_home(self,eventPosition, child)
        elif name == 'tableWidget__addmem':
            Create_QMenuP.QMenu_addmem(self,eventPosition, child)
        elif name == 'tableWidget_kickban':
            Create_QMenuP.QMenu_kickban(self,eventPosition, child)
        elif name == 'tableWidget__addkickban':
            Create_QMenuP.QMenu_addkickban(self,eventPosition, child)
        elif name == 'tableWidget__spammes':
            Create_QMenuP.QMenu_spammes(self,eventPosition, child)


        print(name)

    def QMenu_spammes(self :MainWindow,eventPosition : QPoint, child : PyTableWidget):
        contextMenu = QMenu()


        Select = contextMenu.addAction("Select")
        Select_All = contextMenu.addAction("Select All")
        Remove_Select = contextMenu.addAction("Remove Select")

        action = contextMenu.exec_(child.mapToGlobal(eventPosition))

        if Select_All == action:
            [i.setCheckState(Qt.Checked) for i in child.checkboxlist]
        elif Remove_Select == action:
            [i.setCheckState(Qt.Unchecked) for i in child.checkboxlist]
        if Select == action:
      
            indexes = list(set(index.row() for index in child.selectedIndexes()))
            for i in indexes:
                child.checkboxlist[i].setCheckState(Qt.Checked)


    def QMenu_addkickban(self :MainWindow,eventPosition : QPoint, child : PyTableWidget):
        contextMenu = QMenu()


        Select = contextMenu.addAction("Select")
        Select_All = contextMenu.addAction("Select All")
        Remove_Select = contextMenu.addAction("Remove Select")
        Clean_data = contextMenu.addAction("Clean Data")
        Paste_data = contextMenu.addAction("Paste Data")
        action = contextMenu.exec_(child.mapToGlobal(eventPosition))

        if Select_All == action:
            [i.setCheckState(Qt.Checked) for i in child.checkboxlist]
        elif Remove_Select == action:
            [i.setCheckState(Qt.Unchecked) for i in child.checkboxlist]
        elif Clean_data == action:
            child.setRowCount(0)
            child.checkboxlist.clear()


        if Select == action:
      
            indexes = list(set(index.row() for index in child.selectedIndexes()))
            for i in indexes:
                child.checkboxlist[i].setCheckState(Qt.Checked)
        elif Paste_data == action:
           Core_Functions.paste_data_spammes(self)
    def QMenu_kickban(self :MainWindow,eventPosition : QPoint, child : PyTableWidget):
        contextMenu = QMenu()



        export_Succes = contextMenu.addAction("Load Data Kịch bản")
        Select = contextMenu.addAction("Select")
        Select_All = contextMenu.addAction("Select All")
        Remove_Select = contextMenu.addAction("Remove Select")
        action = contextMenu.exec_(child.mapToGlobal(eventPosition))
        if export_Succes == action:
            Core_Functions.load_message_kickban(self)
        if Select_All == action:
            [i.setCheckState(Qt.Checked) for i in child.checkboxlist]
        elif Remove_Select == action:
            [i.setCheckState(Qt.Unchecked) for i in child.checkboxlist]
        if Select == action:
            indexes = list(set(index.row() for index in child.selectedIndexes()))
            for i in indexes:
                child.checkboxlist[i].setCheckState(Qt.Checked)


    def QMenu_addmem(self :MainWindow,eventPosition : QPoint, child : PyTableWidget):
        contextMenu = QMenu()



        export_Succes = contextMenu.addAction("Xuất Data Succes")
        remove_Fail = contextMenu.addAction("Xuất Data Fail")
        action = contextMenu.exec_(child.mapToGlobal(eventPosition))
        if export_Succes == action:
            Core_Functions.select_data_addmem(self,child,otp='True')
        elif remove_Fail == action:
            Core_Functions.select_data_addmem(self,child,otp='False')


    def QMenu_home(self :MainWindow,eventPosition : QPoint, child : PyTableWidget):
        
        


        contextMenu = QMenu()

        select = contextMenu.addMenu("Select")

        Select = select.addAction("Select")
        Select_All = select.addAction("Select All")
        # Select_spam = select.addAction("Select Account Spam")
        Remove_Select = select.addAction("Remove Select")
        Select_Acc_Die = select.addAction("Select Acc Die")
        Select_Acc_Live = select.addAction("Select Acc Live")
        contextMenu.addSeparator()


        CheckLive = contextMenu.addMenu("Check Live")
        CheckLive_Session =  CheckLive.addAction("With Session")
        CheckLive_Bot = CheckLive.addAction("With Bot")
        contextMenu.addSeparator()
        Check_account_information = contextMenu.addAction("Check account information")
        Check_spam = contextMenu.addAction("Check spam")
        Get_Code = contextMenu.addAction("Get Code")
        contextMenu.addSeparator()
        Add_Password = contextMenu.addAction("Add Password")
        contextMenu.addSeparator()
        Tien_ich = contextMenu.addMenu("Tiện ích")
        Remove_ALL_Contact_in_Account = Tien_ich.addAction("Remove ALL Contact in Account")
        tienich_gopfile_Contact = Tien_ich.addAction("Gộp File Contact")
        contextMenu.addSeparator()
        Export_Data = contextMenu.addMenu("Export Data")
        Export_All_Contact_in_Account = Export_Data.addAction("Export All Contact in Account")
        Export_session = Export_Data.addAction("Export Session")
        Export_USERNAME = Export_Data.addAction("Export USERNAME")
        Export_Phone = Export_Data.addAction("Export PHONE")
        Export_ID = Export_Data.addAction("Export ID")
        contextMenu.addSeparator()
        APPTelegram = contextMenu.addMenu("APP Telegram")
        Convert_tdata = APPTelegram.addAction("Convert Tdata")
        Opne_app_Telegram = APPTelegram.addAction("Open APP Telegram")
        Kill_app_Telegram = APPTelegram.addAction("Kill All APP Telegram")

        contextMenu.addSeparator()
        dichuyen_account = contextMenu.addAction("Di chuyển Account")
        contextMenu.addSeparator()
        removeaccount = contextMenu.addMenu("Remove Account")
        removeaccounttamthoi = removeaccount.addAction("Remove Account Tạm Thời")
        removevinhvien = removeaccount.addAction("Remove Account Vĩnh Viễn")



  
        action = contextMenu.exec_(child.mapToGlobal(eventPosition))
        if Select_All == action:
            [i.setCheckState(Qt.Checked) for i in child.checkboxlist]
        elif Remove_Select == action:
            [i.setCheckState(Qt.Unchecked) for i in child.checkboxlist]
        elif Select == action:
            indexes = list(set(index.row() for index in child.selectedIndexes()))
            for i in indexes:
                child.checkboxlist[i].setCheckState(Qt.Checked)

        elif dichuyen_account == action:
            Dialog_Ui_dichuyenaccount(self).exec_()
        elif Export_USERNAME == action:
            Core_Functions.Coppy_data(self,type='USERNAME')
        elif Export_Phone == action:
            Core_Functions.Coppy_data(self,type='PHONE')
        elif Export_ID == action:
            Core_Functions.Coppy_data(self,type='ID')
        elif Export_session == action:
            Core_Functions.Coppy_data(self,type='SESSION')
        elif Export_All_Contact_in_Account == action:
            self.core.function_run = 'Export All Contact in Account'
            self.core.Run_Proces()
        elif Remove_ALL_Contact_in_Account == action:
            self.core.function_run = 'Remove ALL Contact in Account'
            self.core.Run_Proces()

        elif tienich_gopfile_Contact == action:
            self.core.startThreads(
                Core_Functions.gop_file_contact,
                self)    
        elif removeaccounttamthoi == action:
            self.core.startThreads(
                Core_Functions.removeAccount,
                self,
                False)    
        elif removevinhvien == action:
            self.core.startThreads(
                Core_Functions.removeAccount,
                self,
                True)    


        elif Opne_app_Telegram == action:
            self.core.startThreads(
                Core_Functions.Opne_app_Telegram,
                self)    
        elif Convert_tdata == action:
            self.core.function_run = 'Convert Tdata'
            self.core.Run_Proces()
        elif Add_Password == action:
            text, ok = QInputDialog.getText(self.core.parent, 'Thêm mật khẩu', 'Is this ok?')
            if ok:
                self.core.startThreads(
                    Core_Functions.addpassword,
                    self,
                    text
                    )    
        
        elif Kill_app_Telegram == action:
            os.system('Taskkill /IM Telegram.exe /F')
        elif Select_Acc_Die == action:
            Core_Functions.select_account(child,otp='False')
         
        elif Select_Acc_Live == action:
            Core_Functions.select_account(child,otp='True')
        elif  Check_spam == action:
            self.core.function_run = 'Check spam'
            self.core.Run_Proces()
        elif  Get_Code == action:
            self.core.function_run = 'Get Code'
            self.core.Run_Proces()
        elif  Check_account_information == action:
            self.core.function_run = 'Check account information'
            self.core.Run_Proces()
        elif  CheckLive_Bot == action:
            QMessageBox.information(self.core.parent, 'Thông báo', 'Vui lòng chuyển sang Check Live With Session')
            # self.core.function_run = 'Check Live With Bot'
            # self.core.Run_Proces()
        elif  CheckLive_Session == action:
            self.core.function_run = 'Check Live With Session'
            self.core.Run_Proces()
         


 
  



