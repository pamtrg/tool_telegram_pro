

import queue,string,shutil

from requests import session
from qt_core import *
from os_core import *
from Telegram_pro import MainWindow
from pandas import read_excel
import socket,struct,threading


from ..widgets import PyTableWidget
queryKey = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

queryKey = abc + ABC

check_tab_R = {0:'bangdieukhien',1:'nhom_kenh',2:'spamtinnhan',3:'chatkichban',4:'caidat'}
def read_file_txt(file) -> list:

    with open(file,'r',encoding='utf-8-sig') as myfile:
        datas = myfile.read().splitlines()

    return datas

def isEnglish(name):
    char_set = string.ascii_letters
    return all((True if x in char_set else False for x in name.replace(' ','')))
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)



class Core_Functions:
    def gop_file_contact(self: MainWindow):
        try:
            tableWidget__home: PyTableWidget = self.ui.tableWidget__home
            # get all path file in folder
            path = r'Database\Account\Phone'
            all_path = [
                path+'\\'+x for x in os.listdir(path) 
                if os.path.isfile(os.path.join(path, x)) if 'xlsx' == x.split('.')[-1]  
            ]
            # print(all_path)
            list_path_ss = []
            selects = tableWidget__home.getSelected()
            for index in selects:
                path = tableWidget__home.item(index,1).text()
                for i in all_path:
                    if path in i:
                        list_path_ss.append(i)
            list_data = []
            for fileName in list_path_ss:
                # print(fileName)
                df = read_excel(fileName,keep_default_na=False)
     
                if len(df.values) > 0:
                    for row in df.values:
                        list_data.append(row)
  
            if len(list_data) == 0:
                return False
            workbook = xlsxwriter.Workbook(f'All_Contact.xlsx')
            worksheet = workbook.add_worksheet()
            row = 0
            col = 0
            # print(list_data)
            for phone, id,username, in (list_data):
                worksheet.write(row, col, phone)
                worksheet.write(row, col + 1, id)
                worksheet.write(row, col + 2, username)
                row += 1

            workbook.close()
            return True
        except Exception as e:
            print(e)
            return False





    def loadData_Seeding(self : MainWindow):
        Core_Functions.set_text_open_file(self,QLine = self.ui.lineEdit_24)
        
        df = read_excel(self.ui.lineEdit_24.text(),keep_default_na=False,index_col=None, header=None)
        if self.ui.stackedWidget_22.currentIndex() == 0:
            tableWidget : PyTableWidget = self.ui.tableWidget__seeding
            tableWidget.setRowCount(0)
            try:
                for data in df.values:
                    for i in data:
                        if i != '' or i != 'None':

                            row = tableWidget.add_row()
                            
                            # print(i)
                            tableWidget.add_value_tab(row,[i])
            except Exception as e:
                print(e)
        elif self.ui.stackedWidget_22.currentIndex() == 1:
            tableWidget : PyTableWidget = self.ui.tableWidget__scripts
            tableWidget.setRowCount(0)
            for data in df.values:
                
 
                vl = [i for i in data]
                if vl[0] == '' or vl[0] == 'None':
                    continue
                elif vl[1] == '' or vl[1] == 'None':
                    continue
                elif vl[2] == '' and vl[3] == 'None':
                    continue
           
                
                # print(i)
                row = tableWidget.add_row()
                tableWidget.add_value_tab(row,vl)



    def Checklive(self:MainWindow):
        proxys = self.ui.plainTextEdit.toPlainText().split('\n')
  
        self.ui.plainTextEdit_3.clear()
        self.ui.plainTextEdit_4.clear()
        def main(proxy):
            def connect(proxyport, data):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                try:
                        s.connect(proxyport)
                        s.sendall(data)
                        return s.recv(2)
                except Exception as e:
                #        print(e)
                        return 'None'

            try:
                ip = proxy.split(":")[0]
                port = int(proxy.split(":")[1])
            except:
                self.core.signals.Notif_stt_proxy.emit(proxy,0)
                return


            pconnect = (ip, port)
            data_socks5 = struct.pack('BBB', 0x05, 0x01, 0x00)

            response = connect(pconnect, data_socks5)

            if response == b'\x05\x00' :
                self.core.signals.Notif_stt_proxy.emit(proxy,1)
                # self.signal.emit(1,proxy)
                # print(proxy)
                return
                
            if response == 'None' or response == b'\x05\xff':
                self.core.signals.Notif_stt_proxy.emit(proxy,0)
                
            data_socks4 = struct.pack('BBH', 0x04, 0x01, port)
            response = connect(pconnect, data_socks4)
            if response == b'':
                self.core.signals.Notif_stt_proxy.emit(proxy,1)
                # print(proxy)
            return
        list_task = []
        for i in range(0,len(proxys)):
            task = threading.Thread(target=main,args=(proxys[i],))
         
            
            list_task.append(task)
        for thread in list_task:
            thread.start()

        # Wait for all to complete
        for thread in list_task:
            thread.join()
        return True
      



        
    def load_data_spammes_(self:MainWindow):
        tableWidget : PyTableWidget = self.ui.tableWidget__spammes 
        tableWidget.setRowCount(0)
        tableWidget.checkboxlist = []
        list_data = []
      
        # fileName, _ = QFileDialog.getOpenFileName(self,caption="Chọn file ", filter= f"Files (*.txt)")
        
        # if fileName != None:

        #     df = read_excel(fileName,keep_default_na=False,index_col=None, header=None)
        #     for row in df.values:
        #         list_data.append(row[0])


        fileName, _ = QFileDialog.getOpenFileName(self,caption="Chọn file ", filter= f"Files (*.txt)")
        
        if fileName != None:
            list_data = read_file_txt(fileName)
     






        list_data = list(set(list_data))
        list_data_ = []
        for fl in list_data:
            if fl != 'False' and fl != '':
                list_data_.append(fl)


        
        for j in range(len(list_data_)):
            data_ = [list_data_[j],None] 
      
            row = tableWidget.add_row()
            
      
            tableWidget.add_value_tab(row,data_)









    def load_message_kickban(self:MainWindow):
        tableWidget : PyTableWidget = self.ui.tableWidget__addkickban    
        tableWidget.setRowCount(0)
 
        selects = self.ui.tableWidget_kickban.getSelected()
        # print(selects)
        
        self.core.list_data_message_kickban = []
        for i in selects:
            data = self.core._list_Data_kickban[i]
            df = read_excel(data,keep_default_na=False,index_col=None, header=None)
            # df.replace(r'^\s+$', np.nan, regex=True)
            # print(df)
         
            try:
                for row in df.values:
                   
                    self.core.list_data_message_kickban.append(row)
            except Exception as e:
                print(e)
        # print(self.core.list_data_message_kickban)
        # self.parent.ui.tableWidget_2.setRowCount(0)
        for j in self.core.list_data_message_kickban:
            row = tableWidget.add_row()
            
      
            tableWidget.add_value_tab(row,j)


        


    def load_data_list_kickban(self:MainWindow):
        tableWidget : PyTableWidget = self.ui.tableWidget_kickban    
        tableWidget.setRowCount(0)
        tableWidget.checkboxlist = []
    
        path = r'Database\Script'
        self.core._list_Data_kickban = [
            path+'\\'+x for x in os.listdir(path) 
            if os.path.isfile(os.path.join(path, x)) if 'xlsx' == x.split('.')[-1]  
        ]
      
  

        for j in self.core._list_Data_kickban:
            
            row = tableWidget.add_row()
            
      
            tableWidget.add_value_tab(row,[j])
        # print(tableWidget.checkboxlist)
        # QShortcut(QKeySequence("Ctrl+Q'"), self).activated.connect(tableWidget.selectCheckbox)



    def Coppy_data(self:MainWindow,type: str):
        dict_ = {
            'ID':2,
            'USERNAME':3,
            'PHONE':5,
            'SESSION':1,
            'PATH':10
        }
        tableWidget__home: PyTableWidget = self.ui.tableWidget__home
        index_list = tableWidget__home.getSelected()  

        list_data = []
        for index in index_list:
            
            tx = tableWidget__home.item(index,dict_.get(type))
            if type == 'SESSION':
                path = tableWidget__home.item(index,dict_.get('PATH')).text()
                session =  path +'\\'+ tx.text() 
                # print(session)
                shutil.copy(session, './Session_EX/')
            else:
                list_data.append(tx.text())

                copy_text('\n'.join(list_data))
                
        if type == 'SESSION':
            QMessageBox.information(self, 'Information', 'Đã copy vào Session_EX')
        else:
            QMessageBox.information(self, 'Information', 'Đã copy vào clipboard')





    def Opne_app_Telegram(self:MainWindow):
        tableWidget__home: PyTableWidget = self.ui.tableWidget__home
        index_list = tableWidget__home.getSelected()  
        for index in index_list:
            tx = tableWidget__home.item(index,5)
            # check exist folder
            if not os.path.exists(f'./Telegram_Desktop/{tx.text()}'):
                self.core.signals.Notif_updated.emit('STATUS',index,f'Không tìm thấy file Tdata !')
            else:
                # check exist file
                if not os.path.exists(f'./Telegram_Desktop/{tx.text()}/Telegram.exe'):
                    shutil.copy(r"Database\Exe_Telegram_Desktop\Telegram.exe", f'./Telegram_Desktop/{tx.text()}')
                else:
                    shutil.copy(r"Database\Exe_Telegram_Desktop\Telegram.exe", f'./Telegram_Desktop/{tx.text()}')
                self.core.signals.Notif_updated.emit('STATUS',index,f'Đang mở Telegram')
                os.startfile(f'Telegram_Desktop\\{tx.text()}\\Telegram.exe')
    def addpassword(self : MainWindow, PASSWORD):
        tableWidget__home: PyTableWidget = self.ui.tableWidget__home
        index_list = tableWidget__home.getSelected()  
        try:
            for index in index_list:
                tx = tableWidget__home.item(index,1)
                self.core.SQL.Update_Data(self.ui.comboBox.currentText(),tx.text(),{'PASSWORD':PASSWORD})
            # QMessageBox.information(self, 'Information', 'Thêm mật khẩu thành công !')
            return True
        except Exception as e:
            print(e)
            return False
            # QMessageBox.warning(self, 'Information', str(e))



    def removeAccount(self:MainWindow,remove = False):
        
        tableWidget__home: PyTableWidget = self.ui.tableWidget__home
        index_list = tableWidget__home.getSelected()  
        table_name = self.ui.comboBox.currentText().strip()
        try:
           
            for index in index_list:
                tx = tableWidget__home.item(index,1)
                tx2 = tableWidget__home.item(index,10)
                path = tx2.text() + '\\' + tx.text()
                self.core.SQL.Delete_Rows(table_name,tx.text())
                if remove:
                    try:
                        os.remove(path)
                    except OSError as e:
                        print(e)
            return True
        except Exception as e :
            
            print(e) 
            return False 
    def getCheckedRbName( rbParent: QWidget) -> str:
        for rb in rbParent.findChildren(QRadioButton):
            if rb.isChecked():
                return rb.text()



    def get_function_run(parent: MainWindow,Config_run:dict):
        inddex =  parent.ui.stackedWidget_4.currentIndex()
        tab_name = check_tab_R.get(inddex)
        # print(tab_name,tab_name)

        if tab_name == 'nhom_kenh':
            # print(parent.ui.getmemandaddmem.currentIndex())
            index_nhomkenh = parent.ui.getmemandaddmem.currentIndex()
            print(index_nhomkenh)
            if index_nhomkenh == 1:
                Config_run['linkgroup'] = parent.ui.searching_3.text()
                ftn = 'Get_member_group'
                parent.count_getmem = 0
                if parent.ui.checkBox_3.isChecked():
                    parent.ui.tableWidget__getmem.checkboxlist = []
                    parent.ui.tableWidget__getmem.setRowCount(0)
 
 
                queue_Key = queue.Queue()
                for key in queryKey:
                    queue_Key.put(key)
                Config_run['otp_member_get'] = {
                    'list_member':[],
                    'total_clone':parent.ui.spinBox_4.value(),
                    'otp_getmem':Core_Functions.getCheckedRbName(parent.ui.frame_15),
                    'check_mem':[],
                    
                    'queryKey':queue_Key,
                    
                }
            elif index_nhomkenh == 2:
                parent.count_addmem_success = 0
                parent.count_addmem_fail = 0
                ftn = 'Add_member_group'
                # print(parent.core.list_data_addmem)
                queue_member = queue.Queue()
                a,b = int(parent.ui.spinBox_2.value()),int(parent.ui.spinBox_3.value())
                if len(parent.core.list_data_addmem) < b:
                    b = len(parent.core.list_data_addmem)
                for key in parent.core.list_data_addmem[a:b]:
                    queue_member.put(key)
                linkgroup = parent.ui.lineEdit_6.text().split('/')[-1]
                if os.path.exists(f'Database\\history\\{linkgroup}.txt'):
                    membersUsed = open(f'Database\\history\\{linkgroup}.txt','a+').read().split('\n')
                else:
                    membersUsed = []
                Config_run['otp_member_add'] = {
                    'checkMember':[],
                    'list_member_id':parent.core.list_data_addmem_id,
                    'linkgr_add':parent.ui.lineEdit_6.text(),
                    'linkgr_clone':parent.ui.lineEdit_4.text(),
                    'ands':[parent.ui.spinBox_2.value(), parent.ui.spinBox_3.value()],
                    'total_count_add':parent.ui.spinBox.value(),
                    'membersUsed':membersUsed,
                    'otp_addmem':parent.ui.comboBox_6.currentText(),
                    'queue_member':queue_member,
                }
                if parent.ui.comboBox_6.currentText() == 'Add members by ID':
                    parent.list_data_addmem_check_index = []
                    tableWidget__addmem: PyTableWidget = parent.ui.tableWidget__addmem
                    tableWidget__addmem.checkboxlist = []
                    tableWidget__addmem.setRowCount(0)
                    
                    
                    queue_Key = queue.Queue()
                    for key in queryKey:
                        queue_Key.put(key)
                    Config_run['otp_member_get'] = {
                        'check_mem':[],
                        'list_member':[],
                        'total_clone':parent.ui.spinBox_4.value(),
                        'queryKey':queue_Key,
                        
                    }
            else:
                ftn = 'tien ich group'
                condition = {
                    
                }
                list_enti = None
                otp_tienich = parent.ui.comboBox_8.currentText()
                if otp_tienich == 'Join Group Or Channel':
                    list_enti = parent.ui.plainTextEdit_9.toPlainText().split("\n")
                elif otp_tienich == 'Leave Groups or Channel':
                    list_enti = parent.ui.plainTextEdit_8.toPlainText().split("\n")
                    condition.update({
                        'Otp':Core_Functions.getCheckedRbName(parent.ui.widget_6),
                    })

                    if parent.ui.checkBox_12.isChecked():
                        condition.update({
                            'TotalMember':[parent.ui.spinBox_5.value(), parent.ui.spinBox_6.value()],
                            'Blockchat': True if  Core_Functions.getCheckedRbName(parent.ui.frame_53) == 'Block Chat' else False,

                        })
                        
                elif otp_tienich == 'Buff view post Channel':
                    list_enti = parent.ui.plainTextEdit_11.toPlainText().split("\n")

                    condition.update({
                        'Otp':Core_Functions.getCheckedRbName(parent.ui.widget_13),

                    })
                elif otp_tienich == 'Buff reaction post Channel or Group':
                    list_enti = parent.ui.plainTextEdit_12.toPlainText().split("\n")

                    condition.update({
                        'Otp':Core_Functions.getCheckedRbName(parent.ui.widget_12),
                        'CountIcon':parent.ui.lineEdit_21.text().split("|"),
                        'ListIcon':parent.ui.lineEdit_16.text().split(",")

                    })
                elif otp_tienich == 'Comment channel':
                    list_enti = parent.ui.plainTextEdit_15.toPlainText().split("\n")
                    list_text = parent.ui.plainTextEdit_14.toPlainText().split("\n")
                    condition.update({
                        'list_text':list_text,
                        'Otp':Core_Functions.getCheckedRbName(parent.ui.frame_57),


                    })
                elif otp_tienich == 'Scrape Data Message':
                    list_enti = parent.ui.plainTextEdit_13.toPlainText().split("\n")

                    condition.update({
                        'filter':parent.ui.checkBox_23.isChecked(),
                        'CountMessages': int(parent.ui.lineEdit_19.text()) if parent.ui.lineEdit_19.text() else 10000
              
                    })
                    # parent.ui.lineEdit_19.setText(str(10000))

                
                Config_run['otp_group_tienich'] = {
                    'list_enti':list_enti,
                    # 'list_text':parent.ui.plainTextEdit_7.toPlainText().split("\n"),
                    'check_icon':{'check':0},
                    'count_check':{},
                    'otp_tienich':otp_tienich,
                    'condition':condition
                }


           
            # print(ftn)
            return ftn
        elif tab_name == 'spamtinnhan':
            index_nhomkenh = parent.ui.stackedWidget_6.currentIndex()
            # print(index_nhomkenh)
            if index_nhomkenh == 0:
                tableWidget__spammes : PyTableWidget = parent.ui.tableWidget__spammes 
                tableWidget__addkickban : PyTableWidget = parent.ui.tableWidget__addkickban 
                ftn = 'spam_tinnhan'
                Config_run['otp_chatkickban'] = {
                        'otp_spam':parent.ui.comboBox_5.currentText(),
                        'Max_Message_Group':parent.ui.lineEdit_28.text(),
                        'Max_Group_Account':parent.ui.lineEdit_27.text(),
                        'randommesage':parent.ui.checkBox_13.isChecked(),
                        'Duplicate':parent.ui.checkBox_14.isChecked(),
                    }
                

                if parent.ui.checkBox_13.isChecked():
                    queue_Key = tableWidget__addkickban.get_data_from_table()
                else:
                    queue_Key = queue.Queue()
                    for key in tableWidget__addkickban.get_data_from_table():
                        queue_Key.put(key)

                Config_run['otp_chatkickban'].update(
                    {'list_text':queue_Key}
                )


                if parent.ui.checkBox_14.isChecked():
                    queue_Key = tableWidget__spammes.get_data_from_table()
                else:
                    queue_Key = queue.Queue()
                    for key in tableWidget__spammes.get_data_from_table():
                        queue_Key.put(key)
                Config_run['otp_chatkickban'].update(
                    {'list_user':queue_Key}
                )
            elif index_nhomkenh == 1:
                if parent.ui.stackedWidget_22.currentIndex() == 0:
                    ftn = 'spam_seeding'
                    tableWidget__seeding : PyTableWidget = parent.ui.tableWidget__seeding 
                    loop_ = parent.ui.spinBox_7.value()
                    queue_Key = queue.Queue()
                    for _ in range(loop_):
                        
                        for key in tableWidget__seeding.get_data_from_table():
                            queue_Key.put(key)


                    Config_run['otp_seeding'] = {'list_text':queue_Key,
                        'reply':parent.ui.checkBox_10.isChecked(),
                        'list_id':[],
                        'entity':parent.ui.lineEdit_2.text()
                        }
                elif parent.ui.stackedWidget_22.currentIndex() == 1:
                    ftn = 'spam_scripts'
                    
                    tableWidget__scripts : PyTableWidget = parent.ui.tableWidget__scripts
                    loop_ = parent.ui.spinBox_7.value()
                    queue_Key = queue.Queue()
                    list_acctive_log = []
                    acctiveChat = {}

                    a = 0
                    for key in tableWidget__scripts.get_data_from_table():
                        print(key)
                        list_acctive_log.append(key['SESSION']['data'])
                        if a == 0:
                            acctiveChat[key['SESSION']['data']] = True
                            a = 1
                        else:
                            acctiveChat[key['SESSION']['data']] = False
                        queue_Key.put(key)


                    Config_run['otp_scripts'] = {
                        'acctiveLog':list_acctive_log,
                        'acctiveChat':acctiveChat,
                        'queue_Key':queue_Key,
                        'list_id':{},
                        'entity':parent.ui.lineEdit_2.text()
                        }
                
                

            return ftn
        elif tab_name == 'bangdieukhien':
            if parent.ui.stackedWidget.currentIndex() == 1:
                if int(parent.ui.checkBox_7.isChecked()) + int(parent.ui.checkBox_15.isChecked()) + int(parent.ui.checkBox_11.isChecked()) +int(parent.ui.checkBox_6.isChecked())+int(parent.ui.checkBox_9.isChecked())+int(parent.ui.checkBox_16.isChecked()) == 0:
                    QMessageBox.warning(parent, 'Thông báo', 'Bạn chưa chọn đủ thông tin để tiếp tục')
                    return False
                ftn = 'chane_in4_account'
                otpUsername = otp = otpBio =otp2fa=otpName=files= otpchangesession=None
                if parent.ui.checkBox_16.isChecked():
                    otpchangesession = True
                    if int(parent.ui.checkBox_8.isChecked()) + int(parent.ui.checkBox_5.isChecked()) + int(parent.ui.checkBox_19.isChecked()) + int(parent.ui.checkBox_20.isChecked()) == 0:
                        QMessageBox.warning(parent, 'Thông báo', 'Bạn chưa chọn đủ thông tin để tiếp tục')
                        return False

        


                # avatar
                if parent.ui.checkBox_7.isChecked():
                    otp = Core_Functions.getCheckedRbName(parent.ui.frame_36)
                    if otp == 'Change Avatar':
                        # check exist folder
          
                        if parent.ui.lineEdit_17.text() == '':
                            QMessageBox.warning(parent, 'Thông báo', 'Bạn chưa nhập link ảnh')
                            return False
                        elif not os.path.exists(parent.ui.lineEdit_17.text()):
                            QMessageBox.warning(parent, 'Thông báo', 'Link ảnh không tồn tại')
                            return False

                # username
                if parent.ui.checkBox_15.isChecked():
                    otpUsername = Core_Functions.getCheckedRbName(parent.ui.frame_48)
                    if otpUsername == 'Change Username':
                        if parent.ui.lineEdit_14.text() == '':
                            QMessageBox.warning(parent, 'Thông báo', 'Bạn chưa nhập Link File')
                            return False
                        elif not os.path.exists(parent.ui.lineEdit_14.text()):
                            QMessageBox.warning(parent, 'Thông báo', 'Link File username không tồn tại')
                            return False
                # Bio

                if parent.ui.checkBox_11.isChecked():
                    otpBio = Core_Functions.getCheckedRbName(parent.ui.frame_40)
                    if otpBio == 'Change Bio':
                        if parent.ui.lineEdit_18.text() == '':
                            QMessageBox.warning(parent, 'Thông báo', 'Bạn chưa nhập Link File')
                            return False
                        elif not os.path.exists(parent.ui.lineEdit_18.text()):
                            QMessageBox.warning(parent, 'Thông báo', 'Link File Bio không tồn tại')
                            return False
                if parent.ui.checkBox_9.isChecked():
                    otpName = 'Change Full Name'
                    if otpName == 'Change Full Name':
                        if parent.ui.lineEdit_13.text() == '':
                            QMessageBox.warning(parent, 'Thông báo', 'Bạn chưa nhập Link File')
                            return False
                        files = [parent.ui.lineEdit_13.text() + '/first_name.txt', parent.ui.lineEdit_13.text() + '/last_name.txt']
                        for file in files:
                            if not os.path.exists(file):
                                QMessageBox.warning(parent, 'Thông báo', 'Link File Fullname không tồn tại')
                                return False
                if parent.ui.checkBox_6.isChecked():
                    otp2fa = Core_Functions.getCheckedRbName(parent.ui.frame_38)
                    if otp2fa == 'Change':
                        if parent.ui.lineEdit_12.text() == '':
                            QMessageBox.warning(parent, 'Thông báo', 'Bạn chưa nhập 2fa')
                            return False
                  
                 
                Config_run['otp_change_in4'] = {
                    'avatar':{
                        'stt':parent.ui.checkBox_7.isChecked(),
                        'otp':otp ,
                        'link':parent.ui.lineEdit_17.text(),
                    },
                    'username':{
                        'stt':parent.ui.checkBox_15.isChecked(),
                        'otp':otpUsername,
                        'link':parent.ui.lineEdit_14.text()},
                    'bio':{
                        'stt':parent.ui.checkBox_11.isChecked(),
                        'otp':otpBio,
                        'link':parent.ui.lineEdit_18.text()
                    },
                    'fullname':{
                        'stt':parent.ui.checkBox_9.isChecked(),
                        'otp':otpName,
                        'link':files
                    },
                    '2fa':{
                        'stt':parent.ui.checkBox_6.isChecked(),
                        'otp':otp2fa,
                        'pasw':parent.ui.lineEdit_12.text()
                    },
                    'changesession':{
                        'stt':parent.ui.checkBox_16.isChecked(),
                        'otp':otpchangesession,
                        'closeall_session':parent.ui.checkBox_20.isChecked(),
                        'createnew_session':parent.ui.checkBox_19.isChecked(),
                        'deleteall_message':parent.ui.checkBox_5.isChecked(),
                        'outall_group_or_channel':parent.ui.checkBox_8.isChecked(),


                    }
              
                }
                return ftn
                        




         




    def save_data_kickban(self:MainWindow):
        tableWidget : PyTableWidget = self.ui.tableWidget_kickban    
        tableWidget__addkickban: PyTableWidget = self.ui.tableWidget__addkickban
 
        try:
            workbook = xlsxwriter.Workbook(f'Database\\Script\\{self.ui.lineEdit_25.text()}.xlsx')
            worksheet = workbook.add_worksheet("Member")

            row = 0
            col = 0

            # Iterate over the data and write it out row by row.
            for IMAGE, FILE,MESSENGER, in (self.core._Data_kickban):
                # print(MESSENGER)
                worksheet.write(row, col, IMAGE)
                worksheet.write(row, col + 1, FILE)
                worksheet.write(row, col + 2, MESSENGER)
    
                row += 1

            workbook.close()


            self.core._Data_kickban = []
            tableWidget.setRowCount(0)
            tableWidget__addkickban.setRowCount(0)
            QMessageBox.information(self, "Thông báo", "Đã lưu file thành công")
            # self.Stt_mes('Lưu thành công !')
        except Exception as e:
            # print(e)
            QMessageBox.information(self, "Thông báo", "Lưu thất bại")
            # Message.showInfo(self.parent,f'Lỗi ! {e}')

    def clean_data_kickban(self:MainWindow):
        data = [
           self.ui.lineEdit_22,self.ui.lineEdit_23,self.ui.plainTextEdit_10,
        ]

        for i in data:
            i.clear()

    def paste_data_spammes(self:MainWindow):
        tableWidget : PyTableWidget = self.ui.tableWidget__addkickban

        # get data coppy clipboard
        datas = QApplication.clipboard().text().splitlines()
        print(datas)

        for data in datas:
            print(data)
            row = tableWidget.add_row()
            vl = [
            'None','None',data,
            ]
            self.core._Data_kickban.append(vl)

            tableWidget.add_value_tab(row,vl)
    def add_data_kickban(self:MainWindow):
        tableWidget: PyTableWidget = self.ui.tableWidget__addkickban
        row = tableWidget.add_row()
        data = [
           self.ui.lineEdit_22.text(),self.ui.lineEdit_23.text(),self.ui.plainTextEdit_10.toPlainText(),
        ]
        self.core._Data_kickban.append(data)

        tableWidget.add_value_tab(row,data)


    def get_index_stackedWidge(stackedWidget : QStackedWidget):
        return stackedWidget.currentIndex()
    def load_data_meskichban_image(self:MainWindow):

        supportedFormats = QImageReader.supportedImageFormats()
        text_filter = "Images ({})".format(" ".join(["*.{}".format(fo.data().decode()) for fo in supportedFormats]))

        fname, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Load a profile picture", 
            filter=text_filter
        )
        if fname :
            self.ui.lineEdit_22.setText(fname)
    def load_data_meskichban_file(self:MainWindow):
  
        fname, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Load a File", 
    
        )
        if fname :
            self.ui.lineEdit_23.setText(fname)
    def setup_Input(self,list_QLineEdit):
        QLine : QLineEdit
        for QLine in list_QLineEdit:

            onlyInt = QIntValidator()
            QLine.setValidator(onlyInt)
    def set_text_open_file(self:MainWindow, QLine:QLineEdit = False, QPlainTextEdit:QPlainTextEdit = False,filter:str = '*.xlsx'):
        if filter == 'Folder':
            fname = QFileDialog.getExistingDirectory(
                parent=self,
                caption="Open a folder", 
                options=QFileDialog.ShowDirsOnly
            )
            if fname:
                if QLine:
                    QLine.setText(fname)
                else:
                    QPlainTextEdit.appendPlainText(fname)
        else:
            if QLine:
                fileName, _ = QFileDialog.getOpenFileName(self,caption="Chọn file ", filter= f"Files ({filter})")
                if fileName != None:
                    QLine.setText(fileName)
                if QPlainTextEdit:
                    list_data = read_file_txt(fileName)
                    QPlainTextEdit.setPlainText('\n'.join(list_data))
            else:
                fileName, _ = QFileDialog.getOpenFileName(self,caption="Chọn file ", filter= f"Files (*.txt)")
                
                if fileName != None:
                    list_data = read_file_txt(fileName)
                    QPlainTextEdit.setPlainText('\n'.join(list_data))
        


           
    def loc_trung(self:MainWindow):
        # QMessageBox.warning(self, 'Warning', 'Tiến Hành lọc trùng')
        try:
            list_data_1 = []
            path_1 = self.ui.lineEdit_8.text()
            list_data_2 = []
            path_2 = self.ui.lineEdit_7.text()
            list_data_3 = []
            df = read_excel(path_1,keep_default_na=False,index_col=None, header=None)


            for j in df.values:
                # print(j)
                list_data_1.append(str(j[1]))
            df = read_excel(path_2,keep_default_na=False,index_col=None, header=None)
            for j in df.values:
                list_data_2.append(j)
            row = 0
            col = 0
            workbook = xlsxwriter.Workbook(f'loctrung\\loctrung_{self.ui.lineEdit_9.text()}.xlsx')
            worksheet = workbook.add_worksheet()
            for i in list_data_2:
                if str(i[1]) not in list_data_1:
                    worksheet.write(row, col, str(i[0]))
                    
                    worksheet.write(row, col + 1, str(i[1]))
                    worksheet.write(row, col + 2, str(i[2]))
                    worksheet.write(row, col + 3, str(i[3]))
                    worksheet.write(row, col + 4, str(i[4]))
                    worksheet.write(row, col + 5, str(i[5]))
                    row += 1

            workbook.close()
            return 1
        
        except Exception as e:
            print(e)
            return 0





        # QMessageBox.information(self, 'Information', 'Đã lọc trùng xong')



    def export_data_addmem(self,TableWidget:PyTableWidget):
        list_member = []
        index_list = TableWidget.getSelected()

        indexss = TableWidget.config['MEMBER']['loc']
        for row in index_list:
            tx = TableWidget.item(row,indexss)
            list_member.append(tx.text())
        copy_text(
            '\n'.join(list_member)
        )
        QMessageBox.information(self, 'Information', 'Đã copy vào clipboard')


    def select_data_addmem(self:MainWindow,TableWidget : PyTableWidget,otp='False'):
        index_list = TableWidget.getSelected()
        indexss = TableWidget.config['STATUS']['loc']
        for row in index_list:
            tx = TableWidget.item(row,indexss)
            if otp == 'True':
                if tx.text() == 'Thành Công':
                    TableWidget.checkboxlist[row].setCheckState(Qt.Checked)
                else:
                    TableWidget.checkboxlist[row].setCheckState(Qt.Unchecked)
            elif otp == 'False':
                if tx.text() != 'Thành Công':
                    TableWidget.checkboxlist[row].setCheckState(Qt.Checked)
                else:
                    TableWidget.checkboxlist[row].setCheckState(Qt.Unchecked)
        Core_Functions.export_data_addmem(self,TableWidget)



    def select_account(TableWidget : PyTableWidget,otp='False'):
        index_list = TableWidget.getSelected()
        indexss = TableWidget.config['LIVE']['loc']
        for row in index_list:
            tx = TableWidget.item(row,indexss)
            if otp == 'True':
                if tx.text() == 'True':
                    TableWidget.checkboxlist[row].setCheckState(Qt.Checked)
                else:
                    TableWidget.checkboxlist[row].setCheckState(Qt.Unchecked)
            elif otp == 'False':
                if tx.text() == 'False':
                    TableWidget.checkboxlist[row].setCheckState(Qt.Checked)
                else:
                    TableWidget.checkboxlist[row].setCheckState(Qt.Unchecked)
    def handle_item_clicked(self : MainWindow):
        # print(tableItem.row(), tableItem.column())
        tableWidget__home: PyTableWidget = self.ui.tableWidget__home
        check = 0

        for index in range(tableWidget__home.rowCount()):
            if tableWidget__home.checkboxlist[index].checkState() == Qt.Checked:
                check = check + 1

        self.ui.dangchonstt.setText(f'Đang chọn : {check}')
        check_live_ok = 0
        check_live_fail = 0
        for i in tableWidget__home.get_data_from_table():
            if i['LIVE']['data'] == 'False':
                check_live_fail = check_live_fail + 1
            elif i['LIVE']['data'] == 'True':
                check_live_ok = check_live_ok + 1
        self.ui.livestt.setText(f'Live : {check_live_ok}')
        self.ui.diestt.setText(f'Die : {check_live_fail}')




    def findUid(self: MainWindow):
        tableWidget__home: PyTableWidget = self.ui.tableWidget__home
        text = self.ui.lineEdit.text().strip()
        # print(tableWidget__home.config.get(self.ui.comboBox_5.currentText())['loc'])
        for row in range(tableWidget__home.rowCount()):
            item = tableWidget__home.item(row, tableWidget__home.config.get(self.ui.comboBox_5.currentText())['loc'])
            tableWidget__home.setRowHidden(row, text not in item.text())

    def dichuyenacount(self:MainWindow,__tablename__):
        # print(__tablename__)
        try:
            tableWidget__home: PyTableWidget = self.ui.tableWidget__home
            lok = []
            data_Database_2 = self.core.SQL.Get_data(__tablename__)
            for kil in data_Database_2:
                lok.append(kil['SESSION'])

            list_data = []
            select = tableWidget__home.getSelected()
            # print(len(self.core.data_Database))
            for k in range(len(self.core.data_Database)):
                if k in select and self.core.data_Database[k]['SESSION'] not in lok:
                
                    list_data.append(self.core.data_Database[k])
            # print(list_data)
            if len(list_data) == 0:
                return 0
            elif self.core.SQL.Add_row(__tablename__,list_data) == 1:
                Core_Functions.removeAccount(self)
                return 1
                
            else:
                return 0
        except Exception as e:
            print(e)
            # return 0



    def load_data_addmem(self:MainWindow):
        tableWidget__addmem: PyTableWidget = self.ui.tableWidget__addmem
        list_data = []
        if self.ui.comboBox_6.currentText() != 'Add members by PHONE':
            fileName, _ = QFileDialog.getOpenFileName(self,caption="Chọn file ", filter= f"Files (*.xlsx)",dir='./Member')
            # print(fileName)
            if fileName != '':

                df = read_excel(fileName,keep_default_na=False,index_col=None, header=None)
                for row in df.values:
                    if self.ui.comboBox_6.currentText() == 'Add members by USERNAME':
                        list_data.append(row[0])
                    elif self.ui.comboBox_6.currentText() == 'Add members by ID':
                        # print(row)
                        list_data.append(row[1])
        else:
            fileName, _ = QFileDialog.getOpenFileName(self,caption="Chọn file ", filter= f"Files (*.txt)")
            
            if fileName != '':
                list_data = read_file_txt(fileName)

        # list_data = list(set(list_data))
        # list_data.remove('') if '' in list_data else None
        # fl.remove('FALSE') for fl in list_data if 'FALSE' == fl 
        list_data_ = []
        for fl in list_data:
            if fl != 'False' and fl != '':
                list_data_.append(fl)
        self.ui.total_mem.setText(f'Total : {len(list_data_)}')
        self.ui.spinBox_2.setMaximum(len(list_data_))
        self.ui.spinBox_3.setMaximum(len(list_data_))#
        tableWidget__addmem.checkboxlist = []
        tableWidget__addmem.setRowCount(0)
        self.core.list_data_addmem = []
        self.core.list_data_addmem_id = []
        for j in list_data_:
            
            row = tableWidget__addmem.add_row()
            self.core.list_data_addmem_id.append(str(j))
            j = [j,row]
            self.core.list_data_addmem.append(j)
            
            tableWidget__addmem.add_value_tab(row,j)
        # SetupMainWindow.reload_data_mem(self.parent,list_data_)





    def _Export_Data_Getmem(self: MainWindow):
        datas =  self.ui.tableWidget__getmem.get_data_from_table()
        # print(datas)
        lis_mem =[]
        data_isEnglish = []
        data_not_isEnglish = []
        noavt =[]
        coavt = []
        name_fil = open(r'Database\hoten.txt',encoding='utf-8-sig').read().splitlines()
        for user in datas:
            # print(user)
            
            accept=True
            try:
                if self.ui.comboBox_3.currentText() != 'Get All Member':
                    if user['ONLINE']['data']  == 'False':
                        accept = False
                    else:
                        # year,month,day=user['ONLINE']['data'].split('-')
                        date_start = datetime.strptime(user['ONLINE']['data'], "%Y-%m-%d").date()
                
                        f = date_start-datetime.now().date()
                    
                        if abs(f.days) <= int(''.join(filter(str.isdigit, self.ui.comboBox_3.currentText()))):
                            accept=True
                        else:
                            accept=False
          
              
            except Exception as e:
                print(e)
                accept=False
                continue
            if accept:
                username = user['USERNAME']['data']
                ID = user['ID']['data']
         
                if self.ui.checkBox_17.isChecked():
                    if str(ID) in self.admins:
                        continue
                first_name = user['FIRTNAME']['data']
                last_name = user['LASTNAME']['data']
                PHOTO = user['PHOTO']['data']
                ONLINE = user['ONLINE']['data']


                # name = first_name + ' ' + last_name if first_name and last_name else False

            
                dt_ = [username,ID ,first_name,last_name,PHOTO,ONLINE]
             
                lis_mem.append(dt_)


                
                if self.ui.checkBox_2.isChecked():
                    fulname = first_name + ' ' + last_name
                    if isEnglish(fulname):
                        if fulname.split(' ')[0].lower() in name_fil or fulname.split(' ')[1].lower() in name_fil:
                            data_not_isEnglish.append(dt_)
                        else:
                            data_isEnglish.append(dt_)
                    else:
                        data_not_isEnglish.append(dt_)
                if  self.ui.checkBox.isChecked():
                    if PHOTO == 'True':
                        coavt.append(dt_)
                    else:
                        noavt.append(dt_)


                #check avt
        
        # ADD_ui.showDiaglogUInamile(self_)
        namesave = self.ui.lineEdit_11.text()
        createFolder(f'Member\\{namesave}')
 

  









        data_not_isEnglish_s =[]

        # workbook = xlsxwriter.Workbook(f'Member\\{namesave}\\__membersnotisEnglish.xlsx')
        # worksheet = workbook.add_worksheet()

        row = 0
        col = 0

        for i in data_not_isEnglish:
            data_not_isEnglish_s.append(i[1])


        # # Iterate over the data and write it out row by row.
        # for username, id_,first_name,last_name,photo,was_online in (data_not_isEnglish):
        #     data_not_isEnglish_s.append(id_)
        #     worksheet.write(row, col, username)
        #     worksheet.write(row, col + 1, id_)
        #     worksheet.write(row, col + 2, first_name)
        #     worksheet.write(row, col + 3, last_name)
        #     worksheet.write(row, col + 4, photo)
        #     worksheet.write(row, col + 5, was_online)
        #     row += 1

        # workbook.close()












        # workbook = xlsxwriter.Workbook(f'Member\\{namesave}\\__membersisEnglish.xlsx')
        # worksheet = workbook.add_worksheet()

        # row = 0
        # col = 0

        # # Iterate over the data and write it out row by row.
        # for username, id_,first_name,last_name,photo,was_online in (data_isEnglish):
        #     worksheet.write(row, col, username)
        #     worksheet.write(row, col + 1, id_)
        #     worksheet.write(row, col + 2, first_name)
        #     worksheet.write(row, col + 3, last_name)
        #     worksheet.write(row, col + 4, photo)
        #     worksheet.write(row, col + 5, was_online)
        #     row += 1

        # workbook.close()




        # workbook = xlsxwriter.Workbook(f'Member\\{namesave}\\__memberisAvartar.xlsx')
        # worksheet = workbook.add_worksheet()

        # row = 0
        # col = 0
        coavt_ = []
        # Iterate over the data and write it out row by row.
        for i in coavt:
            coavt_.append(i[1])
        # for username, id_,first_name,last_name,photo,was_online in (coavt):
        #     coavt_.append(id_)
        #     worksheet.write(row, col, username)
        #     worksheet.write(row, col + 1, id_)
        #     worksheet.write(row, col + 2, first_name)
        #     worksheet.write(row, col + 3, last_name)
        #     worksheet.write(row, col + 4, photo)
        #     worksheet.write(row, col + 5, was_online)
        #     row += 1

        # workbook.close()


        # workbook = xlsxwriter.Workbook(f'Member\\{namesave}\\__membernoAvartar.xlsx')
        # worksheet = workbook.add_worksheet()

        # row = 0
        # col = 0

        # for username, id_,first_name,last_name,photo,was_online in (noavt):
        #     worksheet.write(row, col, username)
        #     worksheet.write(row, col + 1, id_)
        #     worksheet.write(row, col + 2, first_name)
        #     worksheet.write(row, col + 3, last_name)
        #     worksheet.write(row, col + 4, photo)
        #     worksheet.write(row, col + 5, was_online)
        #     row += 1

        # workbook.close()





        workbook = xlsxwriter.Workbook(f'Member\\{namesave}\\__membersall.xlsx')
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0

        for username, id_,first_name,last_name,photo,was_online in (lis_mem):

            if self.ui.checkBox_2.isChecked() == True and  self.ui.checkBox.isChecked()== True:
                # print(1)
                if id_ in coavt_ and id_ in data_not_isEnglish_s:
                    worksheet.write(row, col, username)
                    worksheet.write(row, col + 1, id_)
                    worksheet.write(row, col + 2, first_name)
                    worksheet.write(row, col + 3, last_name)
                    worksheet.write(row, col + 4, photo)
                    worksheet.write(row, col + 5, was_online)
                    row += 1
            elif self.ui.checkBox_2.isChecked():
                # print(2)
                if id_ in data_not_isEnglish_s:
                    worksheet.write(row, col, username)
                    worksheet.write(row, col + 1, id_)
                    worksheet.write(row, col + 2, first_name)
                    worksheet.write(row, col + 3, last_name)
                    worksheet.write(row, col + 4, photo)
                    worksheet.write(row, col + 5, was_online)
                    row += 1
            elif self.ui.checkBox.isChecked():
                # print(3)
                if id_  in coavt_:
                    worksheet.write(row, col, username)
                    worksheet.write(row, col + 1, id_)
                    worksheet.write(row, col + 2, first_name)
                    worksheet.write(row, col + 3, last_name)
                    worksheet.write(row, col + 4, photo)
                    worksheet.write(row, col + 5, was_online)
                    row += 1
            else:
  
                worksheet.write(row, col, username)
                worksheet.write(row, col + 1, id_)
                worksheet.write(row, col + 2, first_name)
                worksheet.write(row, col + 3, last_name)
                worksheet.write(row, col + 4, photo)
                worksheet.write(row, col + 5, was_online)
                row += 1
            # id
        workbook.close()

        workbook = xlsxwriter.Workbook(f'Member\\{namesave}\\__memberID.xlsx')
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0

        for username, id_,first_name,last_name,photo,was_online in (lis_mem):
            if self.ui.checkBox_4.isChecked():
                if username == "False":
                    worksheet.write(row, col, username)
                    worksheet.write(row, col + 1, id_)
                    worksheet.write(row, col + 2, first_name)
                    worksheet.write(row, col + 3, last_name)
                    worksheet.write(row, col + 4, photo)
                    worksheet.write(row, col + 5, was_online)
                    row += 1
      
        workbook.close()




        self.core.signals.Notif_stt.emit('Export Success')  