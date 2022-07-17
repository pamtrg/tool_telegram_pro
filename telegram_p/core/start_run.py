

import threading

from qt_core import *
import asyncio ,queue

from Telegram_pro import MainWindow
from random import randint
from threading import Thread
import time,os,socks

from .scripts import Telegram_Home
from telethon import TelegramClient,functions
from .scripts import convertP
from .var_all import Messages_Noti












            


       



class Tele_Home:
    def __init__(self,Config_run,loop,parent:MainWindow) -> None:
        self.parent = parent
        self.loop = loop
        self.list_account = Config_run['list_account']
        self.list_proxy = Config_run['list_proxy']
        self.maxsize = Config_run['cauhinh']['maxsize']
        self.List_check = Config_run['List_check']
        # print(Config_run)
        self.cauhinh = Config_run['cauhinh']
        

    async def tcp_echo_client(self):
        while True:
            try:
                await asyncio.sleep(1)
                data_account = await self.queue.get()

        


                session = data_account['PATH']['data'] +'\\'+ data_account['SESSION']['data']
                phone = data_account['PHONE']['data']
                # check exist file
                if not os.path.exists(session):
                    self.parent.core.signals.Notif_updated.emit('STATUS',data_account['row'],f'Không tìm thấy file session !')
                    self.parent.core.SQL.Update_Data(self.cauhinh['name_table'],data_account['SESSION']['data'],{
                        'MESSENGER':Messages_Noti.NofindFileSession
                    })
                else:
                    # if self.cauhinh['function_run'] in ['Get Mem No Link','Get Mem With Link']:
                    #     queue_keys : queue.Queue = self.cauhinh['otp_member']['queryKey']
                    #     if queue_keys.qsize() == 0:
                    #         self.parent.core.signals.Notif_updated.emit('STATUS',data_account['row'],f'Hết key !')
                    #         self.queue.task_done()
                    #         continue
                    if self.cauhinh['function_run'] == 'Convert Tdata':
                        if await convertP(session,f'Telegram_Desktop\\{phone}\\tdata'):
                            self.parent.core.signals.Notif_updated.emit('STATUS',data_account['row'],Messages_Noti.ConvertSuccess)
                        else:
                            self.parent.core.signals.Notif_updated.emit('STATUS',data_account['row'],Messages_Noti.ConvertFailed)

                    else:
                        if self.cauhinh['function_run'] == 'spam_scripts':
                            if data_account['SESSION']['data'] not in self.cauhinh['otp_scripts']['acctiveLog']:
                                self.parent.core.signals.Notif_updated.emit('STATUS',data_account['row'],f'Tài khoản không nằm trong danh sách kịch bản !')
                              
                                continue
                    




                        try:
                            count_proxy = self.List_check['count_proxy']
                            keyproxy = self.list_proxy[count_proxy]

                            proxy = keyproxy.split(':')
                            otp_proxy = self.parent.ui.comboBox_2.currentText()
                            if otp_proxy == 'SOCKS4':
                                proxy = (socks.SOCKS4, proxy[0], int(proxy[1]), True)
                            elif otp_proxy == 'SOCKS5':
                                proxy = (socks.SOCKS5, proxy[0], int(proxy[1]), True)
                            elif otp_proxy == 'HTTPS':
                                proxy = (socks.HTTP, proxy[0], int(proxy[1]), True)
                            elif otp_proxy == 'NONE':
                                proxy = None
                            elif len(proxy) > 2:
                                self.parent.core.signals.Notif_updated.emit('Proxy sai dịnh dạng !')
                                return
        
              
                            
             
                            self.List_check['count_proxy'] += 1
                        except Exception as e:
                            # print(e)
                            self.parent.core.signals.Notif_updated.emit('STATUS',data_account['row'],Messages_Noti.NofindProxy)
                            proxy = None
                        self.parent.core.signals.Notif_updated.emit('PROXY',data_account['row'],str(proxy))
                        Telegram_Cl = Telegram_Home(
                            self.parent,
                            self.cauhinh,data_account,session,7134163,'2f44d3200456c46ffea61ada8c8bfaec',proxy=proxy)
                        
 
             
                        await Telegram_Cl.Start_P()
                        await Telegram_Cl.cilent.disconnect()
    
                self.queue.task_done()
            except Exception as e:
                print(e,'Tele_Home')
                self.parent.core.signals.Notif_updated.emit('STATUS',data_account['row'],str(e))
                self.queue.task_done()

    async def coroutine(self):

        session : TelegramClient = None
        for session in self.parent.list_session:
            try:
                await session.disconnect()
            except:
                pass
        self.parent.list_session.clear()
        self.queue = asyncio.Queue()
        

        for account in self.list_account:
            self.queue.put_nowait(account)
       




        tasks = []
        maxsize = self.maxsize
        if maxsize > len(self.list_account):
            maxsize = len(self.list_account)
        for i in range(maxsize):
            task =  self.loop.create_task(self.tcp_echo_client())
            tasks.append(task)
        # await asyncio.wait(tasks)
        await self.queue.join()
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks,return_exceptions=True)



        for session in self.parent.list_session:
            try:
                await session.disconnect()
            except:
                pass
        self.parent.list_session.clear()



class AsyncLoopThread(Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.loop = asyncio.new_event_loop()
    def run(self):
        print("Starting event loop in a separate thread")
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()







        # print(f'Coro {self.num} has finished')
class  Start_fun:
    def __init__(self,parent : MainWindow) -> None:
        
        self.parent = parent
        self.loop_handler = AsyncLoopThread()
        self.loop_handler.start()
        self.tasks = []
        self.list_tasks_ = {'Getmem':[],'Addmem':[],'Home':[]}
      
        


    def Add_Thead(self,Config_run:dict):
        self.parent.ui.btn_start.setText('Đang Chạy...')
        # print(Config_run)


        Var_All = self.parent.core.Var_All
        # print(Config_run['cauhinh']['function_run'])
        # if Config_run['cauhinh']['function_run'] in Var_All.get_var('home_table'):
        task =  asyncio.run_coroutine_threadsafe(Tele_Home.coroutine(Tele_Home(Config_run,self.loop_handler.loop,self.parent)), self.loop_handler.loop)
            
        #     self.list_tasks_['Home'].append(task)
        # elif Config_run['cauhinh']['function_run'] in Var_All.get_var('group_channel'):
        #     task =  asyncio.run_coroutine_threadsafe(Tele_Home.coroutine(Tele_Home(Config_run,self.loop_handler.loop,self.parent)), self.loop_handler.loop)
            
        self.tasks.append(task)
  





        # time.sleep(10)
        while self.loop_handler.loop.is_running():
            time.sleep(1)
       
            if len(self.tasks) == 0:
                break
            for task in self.tasks:
                if task._state == 'FINISHED':
                    self.tasks.remove(task)

        
        async def close_session(session):
            # print(session)
            await session.disconnect()
        for session in self.parent.list_session:
            try:
                asyncio.run(close_session(session))
            except:
                pass
        self.parent.list_session.clear()
            
        self.parent.core.function_run = None
        self.parent.ui.btn_start.setText('Start')
        self.parent.core.signals.Notif_stt.emit('Hoàn Thành !')
                  
        # print(f'finished')

            

