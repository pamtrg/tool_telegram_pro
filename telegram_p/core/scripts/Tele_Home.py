

import asyncio
import re
from multiprocessing import Queue
from time import sleep
import random
import os
import string,json
from Telegram_pro import MainWindow
import datetime
import names
import xlsxwriter
from telethon.sessions import StringSession
from telethon import TelegramClient
from .convert_str_telethon import tele_to_pyro
from telethon import types, functions, errors, events
from telethon.tl.functions.account import UpdateUsernameRequest,GetAuthorizationsRequest,ResetAuthorizationRequest
from pyrogram import Client, idle
from pyrogram import filters
from pyrogram import types as pyrogram_types
from pyrogram.handlers import MessageHandler
import queue
import logging
from .function.grORcn import Group_Channel
from ..var_all import Messages_Noti
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.errors import SessionPasswordNeededError
# import pytgcalls
# logging.basicConfig(level=logging.DEBUG)


async def add_Pyro(session_string):

    app = Client(":memory:", session_string=session_string, api_id=7134163,
                 api_hash="2f44d3200456c46ffea61ada8c8bfaec", no_updates=True)
    await app.connect()
    return app


def filter_image_endswith(path):
    try:
        # path = r"E:\Bot_chat\Image"
        list_image = [x for x in os.listdir(path)
                      if os.path.isfile(os.path.join(path, x))
                      ]
        list_image = [x for x in list_image if x.endswith(
            '.jpg') or x.endswith('.png') or x.endswith('.jpeg')]
        image = random.choice(list_image)
        pathimg = path+'\\'+image
        return pathimg
    except:
        return False


class Telegram_Home:
    def __init__(self, parent: MainWindow, cauhinh: dict, data: dict, session, api_id: int, api_hash: str, proxy=None):
        # super().__init__(session, api_id, api_hash,proxy=proxy)

        self.cilent = TelegramClient(session, api_id, api_hash, proxy=proxy)
        self.api_id = api_id
        self.api_hash = api_hash
        self.proxy = proxy
        self.proxy = proxy
        self.parent = parent
        self.cauhinh = cauhinh
        self.data_account = data
        # print(cauhinh)

    async def check_live(self):
        if await self.check_connect():
            self._Set_stt('True', 'LIVE')
            self._Update_Data({'LIVE': 'True'})
            return True
        self._Set_stt('False', 'LIVE')
        self._Update_Data({'LIVE': 'False'})
        return False

    async def _Delay(self):
        await asyncio.sleep(random.randint(

            self.cauhinh['dalay_before'][0],
            self.cauhinh['dalay_before'][1]
        ))

    async def _connect(self):
        self.parent.list_session.append(self.cilent)
        await self.cilent.connect()

    def get_string_session(self):
        return StringSession.save(self.cilent.session)

    async def convert_string_session(self):
        session_telethon = self.get_string_session()
        return tele_to_pyro(session_telethon, await self.cilent.get_me())

    async def check_connect(self):
        return await self.cilent.is_user_authorized()

    async def _Join_group(self, link):
        await asyncio.sleep(0.5)
        try:
            rs = await Group_Channel.join(self.cilent, link)
            if rs['stt']:
                self._Set_stt(Messages_Noti.JoinGrSuccess.format(link))
            else:
                self._Set_stt(str(rs['error']))

        except Exception as e:
            self._Set_stt(str(e))

    def _Set_stt_user(self, text, row, otp='STATUS'):
        self.parent.core.signals.add_mem_updated_from_user.emit(otp, row, text)
        # self.parent.core.signals.add_mem_updated_from_user.emit("SESSION",row,self.data_account['SESSION']['data'])

    def _Set_stt(self, text, otp='STATUS'):
        self.parent.core.signals.Notif_updated.emit(
            otp, self.data_account['row'], text)
        if otp == 'STATUS':
            self._Update_Data({'STATUS': text})

    def _Update_Data(self, data):
        self.parent.core.SQL.Update_Data(
            self.cauhinh['name_table'], self.data_account['SESSION']['data'], data)

    async def get_infomation(self):
        try:
            me = await self.cilent.get_me()
            first_name = me.first_name if me.first_name else ""
            last_name = me.last_name if me.last_name else ""
            return {
                'response': True, 'data': {
                    'ID': me.id, 'FULLNAME': first_name + ' ' + last_name,
                    'USERNAME': me.username, 'PHONE': me.phone,
                    'AVATAR': 'True' if me.photo else 'False'}}
        except Exception as e:
            return {'response': False, 'data': str(e)}
    
    async def close_allSession(self,client :TelegramClient):
        GetSessions = await client(GetAuthorizationsRequest()) 
        if len(GetSessions.authorizations)>1:
            print("Another Session    :\tYes")
            for ss in GetSessions.authorizations:
                SessionHash = ss.hash
                SessionIp   = ss.ip
                if SessionHash>0:
                    result = await client(ResetAuthorizationRequest(hash=SessionHash))
                    print("Session Killed     :\t" + str(SessionIp)) 
        else:
            print("Another Session    :\tNo")


    async def create_sessions(self):

        otp_change_in4: dict = self.cauhinh['otp_change_in4']
        if otp_change_in4['changesession']['closeall_session']:
            await self.close_allSession(self.cilent)

        async def get_phone():
            me = await self.cilent.get_me()
            phone = me.phone if me.phone else None
            return phone
        path_session = self.data_account['SESSION']['data']
        client_2 = TelegramClient(
            f'Database\Account\AddNew\{path_session}', self.api_id, self.api_hash, proxy=self.proxy)

        await client_2.connect()
        if not await client_2.is_user_authorized():
            phone = await get_phone()
            if phone:
                self._Set_stt('Get số điện thoại thành công !')
                print('+'+str(phone))
                result = await client_2(functions.auth.SendCodeRequest(
                    phone_number='+'+str(phone),
                    api_id=8895483,
                    api_hash='a4b98dd3d10e33217a6091115fa58dc4',
                    settings=types.CodeSettings(
                        allow_flashcall=True,
                        current_number=True,
                        allow_app_hash=True
                    )
                ))
                print(result)
                phone_code_hash = result.phone_code_hash
                print(phone_code_hash)

                # await client_2.send_code_request('+'+str(phone))
                try:
                    # code =Login code: 66998. Do not give this code to anyone, even if they say they are from Telegram!
                    a = 0
                    c = 0
                    while True:
                        if a == 5:
                            self._Set_stt('Change session thất bại !')
                            return
                        codes = await self.get_chat(1)
                        # print(codes)
                        if len(codes) == 0:
                            self._Set_stt('Chưa có code gửi về !', 'MESSENGER')
                            await self._Delay()
                            a = a+1
                        try:
                            list_code = []
                            # print(codes)
                            for i in codes:

                                try:
                                    inp_code = re.findall(
                                        r'Login code: (.*?). Do not ', i)[0]
                                    list_code.append(inp_code)
                                except:
                                    pass

                            # print(list_code)
                            if len(list_code) != 0:
                                break
                            await self._Delay()
                            c = c+1
                            if c == 3:
                                self._Set_stt('Gửi lại code !')
                                result = await self(functions.auth.ResendCodeRequest('+'+str(phone), phone_code_hash))
                                phone_code_hash = result.phone_code_hash
                            elif c == 5:
                                self._Set_stt('Không về code !')
                                return
                        except Exception as e:
                            self._Set_stt(str(e), 'MESSENGER')
                            await self._Delay()
                            a = a+1

                    me = await client_2.sign_in(phone, list_code[-1], phone_code_hash=phone_code_hash)
                    self._Set_stt('Tạo session new thành công !')
                    if otp_change_in4['changesession']['closeall_session']:
                        await self.cilent.log_out()
                except SessionPasswordNeededError:
                    me = await client_2.sign_in(password=self.data_account['PASSWORD']['data'])
                    self._Set_stt('Tạo session new thành công !')
                    if otp_change_in4['changesession']['closeall_session']:
                        await self.cilent.log_out()
        await client_2.disconnect()


    async def Start_P(self):
        await self._connect()
        if await self.check_connect():
            self._Set_stt(Messages_Noti.VeryLogin)
        else:
            self._Set_stt(Messages_Noti.ErrorLogin)
            self._Update_Data({'LIVE': 'False'})
            return
        if await self.check_live():
            function_run = self.cauhinh['function_run']
            print(function_run, function_run)
            if function_run in ['Check Live With Session', 'Check Live With Bot']:
                if function_run == 'Check Live With Session':
                    self._Set_stt('Check live with session', 'MESSENGER')
                    await self.check_live()
                else:
                    self._Set_stt('Check live with bot', 'MESSENGER')
                self._Set_stt(Messages_Noti.Checklive_Success)
            elif function_run in ['Check account information']:
                self._Set_stt('Check account information', 'MESSENGER')
                information = await self.get_infomation()
                if information['response'] == False:
                    self._Set_stt('False', 'LIVE')
                    self._Set_stt('Check account information thất bại !')
                    information.update(
                        {'LIVE': 'False', 'MESSENGER': 'Quét Thông Tin Account'})
                else:
                    try:
                        information: dict = information['data']
                        information.update(
                            {'LIVE': 'True', 'MESSENGER': 'Quét Thông Tin Account'})
                        self._Update_Data(information)
                        self._Set_stt('Check account information thành công !')
                    except Exception as e:
                        self._Set_stt(e)
            elif function_run == 'Get_member_group':
                await self.Get_Mem()
            elif function_run == 'Get List Name Group':
                await self.Get_List_Name_Group()
            elif function_run == 'Add_member_group':
                await self.Add_member_group()
            elif function_run == 'Check spam':
                await self.Check_spam()
            elif function_run == 'Get Code':
                await self.Get_Code()
            elif function_run == 'tien ich group':
                await self.Tien_ich_group()
            elif function_run == 'spam_tinnhan':
                await self.Spam_Tinnhan()
            elif function_run == 'spam_seeding':
                await self.spam_seeding()
            elif function_run == 'spam_scripts':
                await self.spam_scripts()
            elif function_run == 'Export All Contact in Account':
                await self.Export_all_contact()
            elif function_run == 'Remove ALL Contact in Account':
                await self.Remove_all_contacts()

            elif function_run == 'chane_in4_account':
                await self.Change_in4_account()

    async def spam_scripts(self):
        otp_seeding = self.cauhinh['otp_scripts']
        linkgr = otp_seeding['entity']
        queue_Key:  queue.Queue = otp_seeding['queue_Key']
        list_id: dict = otp_seeding['list_id']
        acctiveChats : dict = otp_seeding['acctiveChat']
        while True:
            acctiveChat  = otp_seeding['acctiveChat'].get(self.data_account['SESSION']['data'])
            if acctiveChat == False:
                print(acctiveChats)
                self._Set_stt('Đang đợi đến lượt !')
                await asyncio.sleep(1)
            else:
                # if queue_Key.empty():
                #     self._Set_stt('Hết tin nhắn !', 'MESSENGER')
                #     self._Set_stt('Hoàn thành !')

                #     await asyncio.sleep(1)
                #     return
                    
                self._Set_stt('Đã lấy được tin nhắn !')
                data = queue_Key.get()
                print(data)
                session = data['SESSION']['data']
                if session == self.data_account['SESSION']['data']:
                    Id = data['ID']['data']
                    text = data['MESSENGER']['data']
                    File = data['FILE']['data']
                    if File != 'None':
                        # check exist file
                        if not os.path.exists(File):
                            self._Set_stt('File không tồn tại gửi kèm !')
                            File = None
                    else:
                        File = None   
                            
                    reply = data['REPLY']['data']
                    if reply != 'None':
                        reply_to = list_id.get(reply)
                        if reply_to:
                            self._Set_stt('Đang gửi tin nhắn !')
                            rs = await self.cilent.send_message(entity=linkgr,message=text,file=File,reply_to=reply_to)
                            self._Set_stt('Đã gửi tin nhắn !')
                        else:
                            self._Set_stt('Không tìm thấy ID của tin nhắn !')
                    else:
                        self._Set_stt('Đang gửi tin nhắn !')
                        rs = await self.cilent.send_message(entity=linkgr,message=text,file=File)
                        self._Set_stt('Đã gửi tin nhắn !')

                    list_id[Id] = rs.id
                    cd = 0
                    for i,j in acctiveChats.items():
                        print(acctiveChats)
                        if i == session:
                            self.cauhinh['otp_scripts']['acctiveChat'][i] = False
                           
                            cd = 1
                        elif cd == 1:
                            try:
                                self.cauhinh['otp_scripts']['acctiveChat'][i] = True
                                cd = 0
                            except Exception as e:
                                print(e, 'end')

                    
                    await self._Delay()
                    
                    queue_Key.task_done()

                    

                



    async def spam_seeding(self):
        otp_seeding = self.cauhinh['otp_seeding']
        linkgr = otp_seeding['entity']
        que_text:  queue.Queue = otp_seeding['list_text']
        list_id: list = otp_seeding['list_id']

        TypeInputChannel_ADD = None
        if '/' in linkgr:
            TypeInputChannel_ADD = await self.cilent.get_entity(linkgr.split('/')[-1])

        else:
            dialogs = await self.cilent.get_dialogs()
            for dialog in dialogs:
                if dialog.is_group and dialog.is_channel:
                    if str(linkgr) == str(dialog.id):
                        TypeInputChannel_ADD = dialog
                        break
        if TypeInputChannel_ADD == None:
            self._Set_stt('Không tìm thấy group !')
        else:
            while True:
                if que_text.qsize() == 0:
                    self._Set_stt('Đã hết tin nhắn  !')
                    break
                text = que_text.get()
                text = text['MESSENGER']['data']
                try:
                    if self.parent.ui.checkBox_10.isChecked():
                        a = random.randint(1, 10)
                        if a == 3:
                            print('Đang spam !')
                            if len(list_id):
                                reply_to = random.choice(list_id)
                              
                                rs = await self.cilent.send_message(
                                    entity=TypeInputChannel_ADD, message=text, reply_to=reply_to)
                            else:
                                rs = await self.cilent.send_message(
                                    entity=TypeInputChannel_ADD, message=text)
                        else:
                            rs = await self.cilent.send_message(TypeInputChannel_ADD, text)
                    else:
                        rs = await self.cilent.send_message(TypeInputChannel_ADD, text)
                    self._Set_stt(f'Gửi {text} thành công !')
                    list_id.append(rs.id)
                except Exception as e:
                    # print(e)
                    if 'banned from sending messages' in str(e):
                        self._Set_stt(str(e))
                        return
                    else:
                        self._Set_stt(str(e))
                        await self._Delay()
                        continue

                await self._Delay()

    async def Change_in4_account(self):
        self._Set_stt('Change In4 account !')
        # print(self.cauhinh)
        otp_change_in4: dict = self.cauhinh['otp_change_in4']
        acp_key = []
        for key, value in otp_change_in4.items():
            # print(key,value)
            if value['stt'] == True:
                acp_key.append(key)
        print(acp_key)
        for key in acp_key:
            if key == 'changesession':
                if otp_change_in4['changesession']['createnew_session']:
                    await self.create_sessions()
            if key == 'avatar':
                if otp_change_in4['avatar']['otp'] == 'Change Avatar':
                    try:
                        # get random file in folder
                        file_image = filter_image_endswith(
                            otp_change_in4['avatar']['link'])
                        if file_image:
                            self._Set_stt('Đang thay đổi avatar !')

                            file = await self.cilent.upload_file(file_image)
                            await self.cilent(functions.photos.UploadProfilePhotoRequest(file))
                            self._Set_stt('Change Avatar thành công !')
                        else:
                            self._Set_stt('Không tìm thấy file ảnh !')
                    except Exception as e:
                        self._Set_stt('Change Avatar thất bại !')
                        print(e)
                else:
                    try:
                        self._Set_stt('Tiến hành xóa Avatar !')
                        ps = await self.cilent.get_profile_photos('me')
                        list_id_photo = [types.InputPhoto(
                            id=p.id,
                            access_hash=p.access_hash,
                            file_reference=p.file_reference
                        ) for p in ps]
                        if list_id_photo:
                            await self.cilent(functions.photos.DeletePhotosRequest(list_id_photo))
                            self._Set_stt('Xóa Avatar thành công !')
                        else:
                            self._Set_stt('Không tìm thấy Avatar !')
                    except Exception as e:
                        self._Set_stt('Xóa Avatar thất bại !')
                        print(e)

            if key == 'username':
                if otp_change_in4['username']['otp'] == 'Change Username':
                    # get one line in file txt
                    file_name = otp_change_in4['username']['link']
                    with open(file_name, 'r') as f:
                        lines = f.read().splitlines()
                    letters = string.ascii_lowercase

                    username = random.choice(
                        lines) + ''.join(random.choice(letters) for i in range(4))
                else:
                    username = ''
                try:
                    await self.cilent(functions.account.UpdateUsernameRequest(username))
                    self._Set_stt(f'Change Username {username}  thành công !')
                except Exception as e:
                    self._Set_stt(f'Change Username {username} thất bại !')
            if key == 'bio':
                if otp_change_in4['bio']['otp'] == 'Change Bio':
                    # get one line in file txt
                    file_name = otp_change_in4['bio']['link']
                    with open(file_name, 'r') as f:
                        lines = f.read().splitlines()
                    bio = random.choice(lines)
                else:
                    bio = ''
                try:
                    await self.cilent(functions.account.UpdateProfileRequest(
                        about=bio)
                    )   # update bio
                    self._Set_stt(f'Change Bio {bio} thành công !')
                except Exception as e:
                    self._Set_stt(f'Change Bio {bio} thất bại !')
                    print(e)
            if key == 'fullname':
                # print(otp_change_in4['fullname'])
                file_name = otp_change_in4['fullname']['link'][0]
                # print(file_name)
                with open(file_name, 'r', encoding='utf-8-sig') as f:
                    lines = f.read().splitlines()
                file_name1 = otp_change_in4['fullname']['link'][1]
                with open(file_name1, 'r', encoding='utf-8-sig') as f:
                    lines1 = f.read().splitlines()
                fullname = random.choice(lines) + ' ' + random.choice(lines1)
                # print(fullname)
                try:
                    await self.cilent(functions.account.UpdateProfileRequest(
                        last_name=fullname.split(' ')[0], first_name=fullname.split(' ')[1])
                    )   # update bio
                    self._Set_stt(f'Change Name {fullname} thành công !')
                except Exception as e:
                    self._Set_stt(f'Change Name {fullname} thất bại !')
                    print(e)
            if key == '2fa':
                if otp_change_in4['2fa']['otp'] == 'Change':
                    try:
                        current_password = self.data_account['PASSWORD']['data']
                        # print(current_password)
                        if current_password == '':
                            current_password = None
                        # print(current_password)
                        await self.cilent.edit_2fa(current_password=current_password, new_password=otp_change_in4['2fa']['pasw'])
                        self._Update_Data(
                            {'PASSWORD': otp_change_in4['2fa']['pasw']})
                        self._Set_stt('Change 2FA thành công !')
                        self._Set_stt(
                            otp_change_in4['2fa']['pasw'], 'PASSWORD')
                    except Exception as e:
                        if 'The password (and thus its hash value)' in str(e):
                            self._Set_stt('Mật khẩu cũ không đúng !')
                        else:
                            self._Set_stt(str(e),'MESSENGER')
                            self._Set_stt('Change 2FA thất bại !')
                            print(e)
                     


    async def Remove_all_contacts(self):
        try:

            result_ = await self.cilent(functions.contacts.GetContactsRequest(hash=0))
            if len(result_.users) == 0:
                self._Set_stt('Không có contact nào !')
                return
            result = await self.cilent(functions.contacts.DeleteContactsRequest(
                id=result_.users
            ))
        except Exception as e:
            print(e)
    async def Export_all_contact(self):
        try:
            row = 0
            col = 0
            self._Set_stt('Đang lấy danh sách contact !')
            result = await self.cilent(functions.contacts.GetContactsRequest(hash=0))
            if len(result.users) == 0:
                self._Set_stt('Không có contact nào !')
                return
            self._Set_stt('Đang xử lý !')
            url_path = r'Database\Account\Phone\{}.xlsx'.format(
                self.data_account['SESSION']['data'])
            workbook = xlsxwriter.Workbook(url_path)
            worksheet = workbook.add_worksheet()
            for u in result.users:
                phone = u.phone if u.phone else 'None'
                id_ = u.id if u.id else 'None'
                username = u.username if u.username else 'None'
                worksheet.write(row, col, phone)
                worksheet.write(row, col + 1, id_)
                worksheet.write(row, col + 2, username)
                row += 1
            workbook.close()
            self._Set_stt('Lưu file thành công !')
        except Exception as e:
            print(e, 'Export_all_contact')
            self._Set_stt(e)

    async def Spam_Tinnhan(self):
        try:
            self._Set_stt('Spam tin nhắn', 'MESSENGER')
            otp_chatkickban = self.cauhinh['otp_chatkickban']
            list_text = otp_chatkickban['list_text']
            list_user = otp_chatkickban['list_user']
            otp_spam = otp_chatkickban['otp_spam']

            a = 0

            for _ in range(int(otp_chatkickban['Max_Group_Account'])):
                if otp_chatkickban['Duplicate']:
                    if a >= len(list_user):
                        self._Set_stt(
                            'Đã duyệt hết danh sách user !', 'MESSENGER')
                        break
                    user_ = list_user[a]
                    a = a + 1
                else:
                    list_user: queue.Queue
                    if list_user.empty():
                        self._Set_stt(
                            'Đã duyệt hết danh sách user !', 'MESSENGER')
                        break
                    user_ = list_user.get()
                self._Set_stt('Đang spam tin nhắn cho user {}'.format(
                    user_['MEMBER']['data']), 'MESSENGER')
                for _ in range(int(otp_chatkickban['Max_Message_Group'])):
                    if otp_chatkickban['randommesage']:
                        text = random.choice(list_text)
                    else:
                        list_text: queue.Queue
                        if list_text.empty():
                            self._Set_stt(
                                'Đã duyệt hết danh sách user !', 'MESSENGER')
                            break
                        text = list_text.get()

                enti: str = user_['MEMBER']['data']
                message, image, file = text['MESSENGER']['data'], text['IMAGE']['data'], text['FILE']['data']
                tos = enti
                if enti.isdigit():
                    print(enti)
                    result = await self.cilent(functions.contacts.ImportContactsRequest(
                        contacts=[types.InputPhoneContact(
                            client_id=random.randrange(-2**63, 2**63),
                            phone=enti,
                            first_name=names.get_first_name(),
                            last_name=names.get_full_name()
                        )]
                    ))

                    if len(result.users) > 0:
                        enti = result.users[0]
                        self._Set_stt('Đã tìm thấy user {}'.format(
                            enti.id), 'MESSENGER')
                        tos = enti.id

                    else:
                        self._Set_stt(f'Add phone thất bại !', 'MESSENGER')
                        enti = False

                if enti:
                    if await self.send_message_all(entity=enti, message=message, image=image, file=file):
                        self._Set_stt(
                            f'Spam to {tos} thành công !', 'MESSENGER')
                    else:
                        self._Set_stt(f'Spam to {tos} thất bại !', 'MESSENGER')
                    await self._Delay()
            self._Set_stt('Hoàn thành tiến trình!')
        except Exception as e:
            print(e, 'Spam_Tinnhan')
            self._Set_stt(str(e))

    async def send_message_all(self, entity, message=None, image=False, file=None):
        try:
            if file:
                await self.cilent.send_file(entity, file)
            if image:
                await self.cilent.send_file(entity, image)
            if message:
                await self.cilent.send_message(entity, message)

            return True
        except Exception as e:
            self._Set_stt(e)
            # print(e)
            if 'banned from sending messages' in str(e):
                self._Set_stt('Banned from sending messages', 'MESSENGER')
            elif "You can't write in this" in str(e):
                if self.cauhinh['otp_chatkickban']['Duplicate']:
                    self.cauhinh['otp_chatkickban']['list_user'].remove(entity)

            return False

    async def handler_buff_view(self, event):
        # print(event)
        # print(type(event))
        rs = await self.cilent(functions.messages.GetMessagesViewsRequest(
            peer=event.message.chat,
            id=[event.message.id],
            increment=True
        ))
        # print(rs)

    async def message_handler_react_channel(self, client_pyrogram: Client, message: pyrogram_types.Message):

        count_check: dict = self.cauhinh['otp_group_tienich']['count_check']

        if count_check.get(message.id) == None:
            count_check[message.id] = 0
        else:
            c = random.randint(int(self.a), int(self.b))
            gg = 0
            if gg == 0:
                if count_check[message.id] < c:
                    self.cauhinh['otp_group_tienich']['count_check'][message.id] += 1

                    icon_ = random.choice(self.ListIcon)
                    if self.check_icon.get(message.id):
                        icon_ = self.check_icon.get(message.id)
                    else:
                        self.check_icon[message.id] = icon_

                    try:
                        await client_pyrogram.send_reaction(message.chat.id, message.id, icon_)
                        self._Set_stt(
                            f'Đã tiến hành {icon_} trên group {message.chat.title}')
                    except Exception as e:
                        self._Set_stt(str(e))
                else:
                    self.cauhinh['otp_group_tienich']['count_check'][message.id] += 1

    async def Buff_reaction_post_Channel_or_Group(self, list_enti, condition):

        self.ListIcon = condition['ListIcon']
        if condition['Otp'] == 'Buff reaction post by Link Channel or Group':
            self.a, self.b = condition['CountIcon']
            list_check = []

            for group in list_enti:
                if 't.me/c/' in group:
                    self._Set_stt(
                        f'Group {group} phải là công khai !', 'MESSENGER')
                    continue

                channel = group.replace('https://t.me/', '').split('/')[0]
                # check exist in dict
                if channel.split('|')[0] not in list_check:
                    list_check.append(channel.split('|')[0])
            if len(list_check) == 0:
                self._Set_stt('Không có group nào để tiện ích !', 'MESSENGER')
                return False
            self.session_string = await self.convert_string_session()
            # print('Connected')

            self.check_icon: dict = self.cauhinh['otp_group_tienich']['check_icon']
            await self.cilent.disconnect()
            self.client_py_ro = Client(
                name=self.data_account['SESSION']['data'], session_string=self.session_string, api_id=7134163, api_hash="2f44d3200456c46ffea61ada8c8bfaec",)

            await self.client_py_ro.start()
            self.client_py_ro.add_handler(MessageHandler(
                self.message_handler_react_channel, filters=filters.incoming & filters.chat(list_check)))

            # print('Connected to 2')

            ass = 0
            while True:
                await asyncio.sleep(2)
                self._Set_stt(f'Checking..{ass}', 'MESSENGER')
                ass = ass+1

        else:
            self.session_string = await self.convert_string_session()
            # print('Connected')

            self.check_icon: dict = self.cauhinh['otp_group_tienich']['check_icon']
            await self.cilent.disconnect()
            self.client_py_ro = Client(
                name=self.data_account['SESSION']['data'], session_string=self.session_string, api_id=7134163, api_hash="2f44d3200456c46ffea61ada8c8bfaec",)

            await self.client_py_ro.start()
            dict_check = {}
            for group in list_enti:
                if 't.me/c/' in group:
                    self._Set_stt(
                        f'Group {group} phải là công khai !', 'MESSENGER')
                    continue
                sr = group.split('/')[-1]

                channel = group.replace('https://t.me/', '').split('/')[0]
                # check exist in dict
                if dict_check.get(channel.split('|')[0]) == None:
                    dict_check[channel.split('|')[0]] = []
                dict_check[channel.split('|')[0]].append(sr)

            for channel, j in dict_check.items():
                list_id = [int(i) for i in j]
                for id_ in list_id:
                    icon_ = random.choice(self.ListIcon)
                    await self.client_py_ro.send_reaction(channel, id_, icon_)
            await self.client_py_ro.disconnect()

    async def Scrape_Data_Message(self, list_enti, condition):
        list_check = []

        for group in list_enti:
            if 't.me/c/' in group:
                self._Set_stt(
                    f'Group {group} phải là công khai !', 'MESSENGER')
                continue

            channel = group.replace('https://t.me/', '').split('/')[0]
            # check exist in dict
            if channel.split('|')[0] not in list_check:
                list_check.append(channel.split('|')[0])

        for group in list_check:
            list_message = []
            messages = await self.cilent.get_messages(group, limit=condition['CountMessages'])
            messages.reverse()
            scrMes = {}
            a = 0

            for message in messages:
              
                list_message.append(message.message)
            #     scrMes[a] = {
            #         "message": message.message,
            #         "id_msg": message.id,
            #         "reply_to": message.reply_to_msg_id,
            #         "user_id": message.from_id.user_id,
            #     }
            #     a += 1
            # with open('message.json', 'w',encoding='utf-8-sig') as f:
            #     json.dump(scrMes, f, indent=4)
            # for message in messages:
            #     # print(message)
            #     list_message.append(message.message)
                # print(message.message)
            if os.path.exists('Member/Scrape') == False:
                os.makedirs('Member/Scrape')
            workbook = xlsxwriter.Workbook(f'Member/Scrape/{group}.xlsx')
            worksheet = workbook.add_worksheet()

            row = 0
            col = 2

            for message in (list_message):
                worksheet.write(row, col, message)
                worksheet.write(row, col+1, 'None')
                worksheet.write(row, col+2, 'None')

                row += 1

            workbook.close()















    async def Buff_view_post_(self, list_enti, condition):
        if condition['Otp'] == 'Buff view post by link Channel':
            list_check = []

            for group in list_enti:
                if 't.me/c/' in group:
                    self._Set_stt(
                        f'Group {group} phải là công khai !', 'MESSENGER')
                    continue

                channel = group.replace('https://t.me/', '').split('/')[0]
                # check exist in dict
                if channel.split('|')[0] not in list_check:
                    list_check.append(channel.split('|')[0])
            if len(list_check) == 0:
                self._Set_stt('Không có group nào để tiện ích !', 'MESSENGER')
                return False

            self.cilent.add_event_handler(
                self.handler_buff_view, events.NewMessage(chats=list_check, incoming=True))
            await self.allways_run()
        else:
            dict_check = {}
            for group in list_enti:
                if 't.me/c/' in group:
                    self._Set_stt(
                        f'Group {group} phải là công khai !', 'MESSENGER')
                    continue
                sr = group.split('/')[-1]

                channel = group.replace('https://t.me/', '').split('/')[0]
                # check exist in dict
                if dict_check.get(channel.split('|')[0]) == None:
                    dict_check[channel.split('|')[0]] = []
                dict_check[channel.split('|')[0]].append(sr)

            for channel, j in dict_check.items():
                list_id = [int(i) for i in j]
                if await self.buff_view(channel, list_id):
                    self._Set_stt(
                        f'Buff view post {channel} thành công !', 'MESSENGER')
                else:
                    self._Set_stt(
                        f'Buff view post {channel} thất bại !', 'MESSENGER')

    async def Tien_ich_group(self):
        otp_tienich = self.cauhinh['otp_group_tienich']['otp_tienich']
        list_enti = self.cauhinh['otp_group_tienich']['list_enti']
        condition = self.cauhinh['otp_group_tienich']['condition']
        print(list_enti, condition)
        # print(otp_tienich)
        if otp_tienich == 'Join Group Or Channel':
            for enti in list_enti:

                await self._Join_group(enti)
                await self._Delay()
        elif otp_tienich == 'Leave Groups or Channel':
            await self.delete_dialog_(list_enti, condition)
            self._Set_stt(f'Leave hoàn tất  !')
        elif otp_tienich == 'Buff view post Channel':
            await self.Buff_view_post_(list_enti, condition)

            self._Set_stt(f'Buff view post hoàn tất !')

        elif otp_tienich == 'Scrape Data Message':
            await self.Scrape_Data_Message(list_enti, condition)

            self._Set_stt(f'Quét tin nhắn thành công !')

        elif otp_tienich == 'Comment channel':
            # list_check = []

            # for group in list_enti:
            #     if 't.me/c/' in group:
            #         self._Set_stt(f'Group {group} phải là công khai !','MESSENGER')
            #         continue
            #     sr = group.split('/')[-1]

            #     channel = group.replace('https://t.me/','').split('/')[0]
            #     # check exist in dict
            #     if channel.split('|')[0] not in list_check:
            #         list_check.append(channel.split('|')[0])
            # if len(list_check) == 0:
            #     self._Set_stt('Không có group nào để tiện ích !','MESSENGER')
            #     return

            self.list_text = condition['list_text']
            if condition['Otp'] == 'Buff comment by link Channel':
                self.cilent.add_event_handler(self.message_handler_comment_channel, events.NewMessage(chats=list_check,incoming=True))

                await self.allways_run()
            else:

                dict_check = {}
                for group in list_enti:
                    if 't.me/c/' in group:
                        # self._Set_stt(f'Group {group} phải là công khai !','MESSENGER')
                        continue
                    sr = group.split('/')[-1]

                    channel = group.replace('https://t.me/', '').split('/')[0]
                    # check exist in dict
                    if dict_check.get(channel.split('|')[0]) == None:
                        dict_check[channel.split('|')[0]] = []
                    dict_check[channel.split('|')[0]].append(sr)

                for channel, j in dict_check.items():
                    list_id = [int(i) for i in j]
                    # for id_ in list_id:
                    #     self._Set_stt(f'Buff view post {channel}','MESSENGER')
                    for postid in list_id:
                        text = random.choice(self.list_text)
                        await self.cilent.send_message(channel, text, comment_to=postid)
                        await self._Delay()

        elif otp_tienich == 'Buff reaction post Channel or Group':
            await self.Buff_reaction_post_Channel_or_Group(list_enti, condition)
            try:
                list_check = []

                for group in list_enti:
                    if 't.me/c/' in group:
                        self._Set_stt(
                            f'Group {group} phải là công khai !', 'MESSENGER')
                        continue
                    sr = group.split('/')[-1]

                    channel = group.replace('https://t.me/', '').split('/')[0]
                    # check exist in dict
                    if channel.split('|')[0] not in list_check:
                        list_check.append(channel.split('|')[0])
                if len(list_check) == 0:
                    self._Set_stt(
                        'Không có group nào để tiện ích !', 'MESSENGER')
                    return
                self.session_string = await self.convert_string_session()
                # print('Connected')
                self.list_text = self.cauhinh['otp_group_tienich']['list_text']
                self.check_icon: dict = self.cauhinh['otp_group_tienich']['check_icon']
                await self.cilent.disconnect()
                self.client_py_ro = Client(
                    name=self.data_account['SESSION']['data'], session_string=self.session_string, api_id=7134163, api_hash="2f44d3200456c46ffea61ada8c8bfaec",)

                await self.client_py_ro.start()

                a, b = self.parent.ui.lineEdit_10.text().split('|')

                async def message_handler_react_channel(client_pyrogram: Client, message: pyrogram_types.Message):

                    count_check: dict = self.cauhinh['otp_group_tienich']['count_check']

                    if count_check.get(message.id) == None:
                        count_check[message.id] = 0
                    else:
                        c = random.randint(int(a), int(b))
                        gg = 0
                        if gg == 0:
                            if count_check[message.id] < c:
                                self.cauhinh['otp_group_tienich']['count_check'][message.id] += 1

                                icon_ = random.choice(self.list_text)
                                if self.check_icon.get(message.id):
                                    icon_ = self.check_icon.get(message.id)
                                else:
                                    self.check_icon[message.id] = icon_

                                try:
                                    await client_pyrogram.send_reaction(message.chat.id, message.id, icon_)
                                    self._Set_stt(
                                        f'Đã tiến hành {icon_} trên group {message.chat.title}')
                                except Exception as e:
                                    self._Set_stt(str(e))
                            else:
                                self.cauhinh['otp_group_tienich']['count_check'][message.id] += 1

                    # print('Start')
                self.client_py_ro.add_handler(MessageHandler(
                    message_handler_react_channel, filters=filters.incoming & filters.chat(list_check)))

                # print('Connected to 2')
                ass = 0
                while True:
                    await asyncio.sleep(2)
                    self._Set_stt(f'Checking..{ass}', 'MESSENGER')
                    ass = ass+1
            except Exception as e:
                self._Set_stt(str(e))
                print(e, 'Buff react post channel')
        elif otp_tienich == 'Buff Online':
            await self.allways_run()
        elif otp_tienich == 'Join voice':
            print('Join voice')
            self._Set_stt('Đang voice !')

            CHAT_ID = list_enti[0]
            group_call = pytgcalls.GroupCallFactory(
                self.cilent, pytgcalls.GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON
            ).get_group_call()
            await group_call.join(CHAT_ID)
            self._Set_stt('Đã kết nối voice !')
            await self.allways_run()
            # await group_call.set_is_mute(True)
            # await group_call.stop_media()

            # await self.cilent.run_until_disconnected()
            print('Disconnected')

    async def cmtchane(self, listchan):
        text = random.choice(self.list_text)
        await self.cilent.send_message(event.message.chat, text, comment_to=event.message.id)

    async def message_handler_comment_channel(self, event):
        # print(event.message.message,event.message.id)
        count_check: dict = self.cauhinh['otp_group_tienich']['count_check']

        if count_check.get(event.message.id) == None:
            count_check[event.message.id] = 0
        else:
            a, b = self.parent.ui.lineEdit_10.text().split('|')
            c = random.randint(int(a), int(b))
            gg = random.randint(0, 1)
            if gg == 0:
                if count_check[event.message.id] < c:
                    self.cauhinh['otp_group_tienich']['count_check'][event.message.id] += 1
                    await self._Delay()
                    text = random.choice(self.list_text)
                    await self.cilent.send_message(event.message.chat, text, comment_to=event.message.id)
                    self._Set_stt('Gửi tin nhắn thành công !', 'MESSENGER')
            else:
                self.cauhinh['otp_group_tienich']['count_check'][event.message.id] += 1

    async def allways_run(self):
        while True:
            # print('f')
            try:

                self._Set_stt("Đang check connect ! !")
                await asyncio.sleep(1)
                self._Set_stt("Check connect ok !")

                try:
                    await self.cilent(functions.account.UpdateStatusRequest(offline=False))
                except Exception as e:
                    print(e)
                    await self.cilent.connect()

                if not await self.cilent.is_user_authorized():
                    await asyncio.sleep(2)
                    try:
                        await self.cilent.connect()
                        await self.cilent(functions.account.UpdateStatusRequest(offline=False))
                    except:
                        pass
            except Exception as e:
                print(e, 2)

    async def buff_view(self, channel, list_id):
        # channel = await self.client.get_entity(channel)
        try:
            rs = await self.cilent(functions.messages.GetMessagesViewsRequest(
                peer=channel,
                id=list_id,
                increment=True
            ))
            # print(rs)
            return True
        except Exception as e:
            return False

    async def Buff_react(self):
        # send reaction messages channel telethon
        pass

    async def delete_dialog_(self, list_groups, condition: dict):
        # print(condition)

        async def leave_channel_(channel):

            if isinstance(channel, types.Channel):
                name = channel.title
            else:
                name = channel.name
            if await self.cilent.delete_dialog(channel, revoke=True):

                self._Set_stt(f'Leave thành công {name} !')
            else:
                self._Set_stt(f'Leave thất bại {name} !')
            await self._Delay()
        if condition['Otp'] == 'leave group all groups and channels':
            dialogs = await self.cilent.get_dialogs()
            for dialog in dialogs:
                if dialog.is_group and dialog.is_channel:
                    await leave_channel_(dialog)
        else:
            for group in list_groups:
                try:
                    enty = await self.cilent.get_entity(group.split('/')[-1])
                    await leave_channel_(enty)
                except Exception as e:
                    self._Set_stt(str(e))
                    self._Set_stt(f'Leave thất bại {group} !', 'MESSENGER')

    async def Get_Code(self):
        self._Set_stt('Get Code', 'MESSENGER')
        code = await self.get_chat(1)
        if len(code) == 0:
            self._Set_stt('Chưa có code')
        else:
            self._Set_stt('Get Code thành công !', 'MESSENGER')
            self._Set_stt(code[-1])

    async def Check_spam(self):
        self._Set_stt('Check spam', 'MESSENGER')
        rs = await self.cilent.send_message('SpamBot', message='/start')
        await asyncio.sleep(3)
        code_ = await self.get_chat(2)
        # print(code_)
        try:
            self._Set_stt(str(code_[-1]))
            self._Set_stt('Check spam thành công !', 'MESSENGER')
        except:
            self._Set_stt('Check False')

    async def get_chat(self, InputUser_):
        codes = []
        if InputUser_ == 1:
            Input = types.InputUser(777000, 4976228689240769012)
        elif InputUser_ == 2:
            Input = types.PeerUser(178220800)
        else:
            Input = InputUser_
        messages = await self.cilent.get_messages(Input, limit=10)
        for msg in reversed(messages):
            if getattr(msg, 'media', None):
                self.found_media[msg.id] = msg
                content = '<{}> {}'.format(
                    type(msg.media).__name__, msg.message)
            elif hasattr(msg, 'message'):
                content = msg.message
            elif hasattr(msg, 'action'):
                content = str(msg.action)
            else:
                content = type(msg).__name__

            if InputUser_:
                codes.append(content)
            else:
                codes.append(content)
        return codes

    async def Add_member_group(self):
        try:
            await asyncio.sleep(0.5)
            otp_addmem = self.cauhinh['otp_member_add']['otp_addmem']
            linkgr_add = self.cauhinh['otp_member_add']['linkgr_add']
            self.membersUsed = self.cauhinh['otp_member_add']['membersUsed']
            await self._Join_group(linkgr_add)

            if '/' in linkgr_add:
                TypeInputChannel_ADD = await self.cilent.get_entity(linkgr_add.split('/')[-1])

            else:
                dialogs = await self.cilent.get_dialogs()
                for dialog in dialogs:
                    if dialog.is_group and dialog.is_channel:
                        if str(linkgr_add) == str(dialog.id):
                            # print(link_,dialog.id)
                            total = dialog.entity.participants_count
                            TypeInputChannel_ADD = dialog
                            break

            if otp_addmem == 'Add members by ID':
                linkgr_clone = self.cauhinh['otp_member_add']['linkgr_clone']

                if '/' in linkgr_clone:
                    await self._Join_group(linkgr_clone)
                    # channel = opt_run['id_group'].split('/')[-1]
                    TypeInputChannel_get = await self.cilent.get_entity(linkgr_clone.split('/')[-1])
                    fullgr = await self.cilent.get_participants(TypeInputChannel_get, limit=0)
                    total = fullgr.total
                else:
                    dialogs = await self.cilent.get_dialogs()
                    for dialog in dialogs:
                        if dialog.is_group and dialog.is_channel:
                            if str(linkgr_clone) == str(dialog.id):
                                # print(link_,dialog.id)
                                total = dialog.entity.participants_count
                                TypeInputChannel_get = dialog
                                break
            if otp_addmem == 'Add members by USERNAME':
                queue_member: queue.Queue = self.cauhinh['otp_member_add']['queue_member']
                self._Set_stt('Thêm thành viên bằng USERNAME', 'MESSENGER')
            elif otp_addmem == 'Add members by PHONE':
                queue_member: queue.Queue = self.cauhinh['otp_member_add']['queue_member']
                self._Set_stt('Thêm thành viên bằng PHONE', 'MESSENGER')
            elif otp_addmem == 'Add members by ID':

                self.checkMember = self.cauhinh['otp_member_add']['checkMember']
                self._Set_stt('Thêm thành viên bằng ID', 'MESSENGER')
                self._Set_stt('Đang tiến hành setup')

                await self.Get_Mem(not_get_data=True, TypeInputChannel=TypeInputChannel_get, total=total)
                # print(self.cauhinh['otp_member_add']['list_member_id'])
                queue_member = queue.Queue()
                list_data_addmem_check_index: list = self.parent.list_data_addmem_check_index

                list_id = []
                for id_ in self.list_member_add:
                    # print(id_)
                    if str(id_) not in self.checkMember:
                        if str(id_) in self.cauhinh['otp_member_add']['list_member_id']:
                            # queue_member.put_nowait(id_)
                            list_id.append(str(id_))
                            self.parent.core.signals.add_data_from_user.emit(
                                str(id_))
                            self.checkMember.append(str(id_))
                            self._Set_stt('Thêm ID : ' + str(id_) +
                                          ' Thành công', 'MESSENGER')

                            await asyncio.sleep(0.1)
                self._Set_stt('Filter thành công !', 'MESSENGER')
                # print(id_,'đã được thêm')
                # print(list_data_addmem_check_index)
                for id_ in list_id:
                    try:
                        await asyncio.sleep(0.1)
                        index = list_data_addmem_check_index.index(str(id_))
                        queue_member.put_nowait([id_, index])
                        self._Set_stt('Check Index ID : ' +
                                      str(id_) + ' Thành công', 'MESSENGER')
                    except Exception as e:

                        print(e)
                self._Set_stt('Tiến hành thêm thành viên', 'MESSENGER')
            check_PeerFloodError = 0
            check_count_add = 1
            # print(self.cauhinh)
            while True:
                if check_count_add == self.cauhinh['otp_member_add']['total_count_add']:
                    self._Set_stt('Thêm đủ số lượng !', 'MESSENGER')
                    self._Set_stt('Hoàn tất Add Member')
                    return
                elif queue_member.qsize() == 0:
                    self._Set_stt('Hết data !', 'MESSENGER')
                    self._Set_stt('Hoàn tất Add Member')
                    return
                user_ = queue_member.get()
                user__id = user_[0]
                if user_[1] in self.membersUsed:
                    self._Set_stt_user(f'User {user_[1]} đã được thêm vào nhóm từ trước !', user_[1])
                    self._Set_stt(f'User {user_[1]} đã được thêm vào nhóm từ trước !', 'MESSENGER')
                    continue

                # print(user_)

                self._Set_stt(f'Đang thêm user {user_[0]}', 'MESSENGER')
                try:
                    if otp_addmem == 'Add members by ID':
                        user_[0] = await self.cilent.get_input_entity(types.PeerUser(int(user_[0])))
                    elif otp_addmem == 'Add members by PHONE':
                        result = await self.cilent(functions.contacts.ImportContactsRequest(
                            contacts=[types.InputPhoneContact(
                                client_id=random.randrange(-2**63, 2**63),
                                phone=user_[0],
                                first_name=names.get_first_name(),
                                last_name=names.get_full_name()
                            )]
                        ))

                        if len(result.users) <= 0:
                            self._Set_stt_user('Không tìm thấy user', user_[1])
                            self.parent.core.signals.stt_fail.emit()
                            self._Set_stt('Waiting .....')
                            await self._Delay()
                            continue
                        user_[0] = result.users[0]
                        # open('data_user.txt','a+').write(user_[0]+'|'+result.users[0].id+'|'+result.users[0].username+'|'+result.users[0].phone+'\n')

                    await self.cilent(functions.channels.InviteToChannelRequest(TypeInputChannel_ADD, [user_[0]]))
                    self._Set_stt_user('Thành Công', user_[1])
                    self._Set_stt('Thêm user {}/{} thành công !'.format(check_count_add,
                                  self.cauhinh['otp_member_add']['total_count_add']), 'MESSENGER')
                    self.parent.core.signals.stt_success.emit()
                    check_count_add += 1
                    if otp_addmem == 'Add members by PHONE':
                        try:
                            await self.cilent(functions.contacts.DeleteContactsRequest([user_[0]]))
                            self._Set_stt(f'Xóa SDT thành công', 'MESSENGER')
                        except Exception as e:
                            self._Set_stt(str(e), 'MESSENGER')

                except (
                        errors.BotGroupsBlockedError,
                        errors.ChannelInvalidError,
                        errors.ChannelPrivateError,
                        errors.ChatAdminRequiredError,
                        errors.ChatInvalidError,
                        errors.UserBannedInChannelError,
                        errors.InputUserDeactivatedError,
                        errors.BotsTooMuchError) as e:
                    self._Set_stt_user(str(e), user_[1])
                    self._Set_stt(str(e))
                    self.parent.core.signals.stt_fail.emit()
                    return
                except (errors.UserPrivacyRestrictedError, errors.UserChannelsTooMuchError) as e:
                    self.parent.core.signals.stt_fail.emit()
                    self._Set_stt_user(str(e), user_[1])
                except errors.FloodWaitError as e:
                    self.parent.core.signals.stt_fail.emit()
                    self._Set_stt('Đang đợi ' + str(e.seconds) +
                                  ' giây để thực hiện lại !')
                    await asyncio.sleep(e.seconds)
                except errors.PeerFloodError as e:
                    self.parent.core.signals.stt_fail.emit()
                    if check_PeerFloodError <= 5:
                        queue_member.put(user_)
                        check_PeerFloodError = check_PeerFloodError + 1
                        self._Set_stt_user(
                            'Fail, tiến hành add lại !', user_[1])
                        self._Set_stt(
                            'Quá nhiều yêu cầu, đang đợi 60s để thực hiện lại !')
                        await asyncio.sleep(60)
                    else:
                        self._Set_stt(
                            'Quá nhiều yêu cầu, vui lòng để account tạm nghỉ ngơi nhá !')
                        break

                except Exception as e:
                    print(e)
                    self.parent.core.signals.stt_fail.emit()
                    self._Set_stt_user(str(e), user_[1])
                    return
                self._Set_stt('Waiting .....')
                self.membersUsed.append(user__id)
                l_ = linkgr_add.split('/')[-1]
                open(f'Database\\history\\{l_}.txt',
                     'a+').write(str(user__id)+'\n')
                await self._Delay()
        except Exception as e:
            print(e, 'Add_member_group')
            self._Set_stt(str(e))

    async def Get_Mem(self, not_get_data=False, TypeInputChannel=None, total=None):
        if not_get_data == False:
            TypeInputChannel = self.cauhinh['linkgroup']
            if self.cauhinh['otp_member_get']['otp_getmem'] == 'Get Mem No Link':
                dialogs = await self.cilent.get_dialogs()
                for dialog in dialogs:
                    if dialog.is_group and dialog.is_channel:
                        if str(dialog.id) == TypeInputChannel:
                            TypeInputChannel = dialog.entity
                            total = dialog.entity.participants_count
                            break
                if TypeInputChannel == self.cauhinh['linkgroup']:
                    self._Set_stt('Không tìm thấy group !')
                    return
                else:
                    self._Set_stt('Tìm thấy group !')
            else:
                fullgr = await self.cilent.get_participants(TypeInputChannel, limit=0)
                total = fullgr.total

        # print(TypeInputChannel)
        await asyncio.sleep(0.5)

        self.list_member_add = []
        list_admin = []
        async for user in self.cilent.iter_participants(TypeInputChannel, filter=ChannelParticipantsAdmins):

            list_admin.append(str(user.id))
        self.parent.core.signals.get_admin.emit(list_admin)
        
        try:
            total_list_member = len(
                self.cauhinh['otp_member_get']['list_member'])
            while True:

                if total_list_member >= total or len(self.list_member_add) >= self.cauhinh['otp_member_get']['total_clone']:
                    self._Set_stt(f'Quét đủ số lượng !')
                    break

                queue_keys: queue.Queue = self.cauhinh['otp_member_get']['queryKey']
                if queue_keys.qsize() == 0:
                    self._Set_stt('Đã hết key !')
                    break
                offset = 0
                limit = 200
                key = queue_keys.get()
                while True:
                    if total_list_member >= total or len(self.list_member_add) >= self.cauhinh['otp_member_get']['total_clone']:
                        self._Set_stt(f'Quét đủ số lượng !')
                        break

                    self._Set_stt(f'Đang tiến hành scan key {key}!')
                    participants = await self.cilent(functions.channels.GetParticipantsRequest(
                        TypeInputChannel, types.ChannelParticipantsSearch(
                            key), offset, limit,
                        hash=0
                    ))
                    if not participants.users:
                        break
                    if total_list_member >= total or len(self.list_member_add) >= self.cauhinh['otp_member_get']['total_clone']:
                        self._Set_stt(f'Quét đủ số lượng !')
                        break
                    for user in participants.users:
                        if user.id not in self.cauhinh['otp_member_get']['check_mem']:
                            username = user.username if user.username else False
                            if not_get_data and username == False:
                                if str(user.id) not in self.membersUsed:
                                    self.list_member_add.append(user.id)
                            # self._Set_stt(str(user.id) + ' đã được thêm vào danh sách !')

                            first_name = user.first_name if user.first_name else ""
                            last_name = user.last_name if user.last_name else ""
                            photo = True if user.photo else False
                            try:
                                was_online = user.status.was_online.date()
                            except:
                                was_online = False
                            dt_ = [user.id, username, first_name,
                                   last_name, photo, was_online]
                            if not_get_data == False:
                                self.parent.core.signals.get_mem_updated.emit(
                                    dt_)
                                self.cauhinh['otp_member_get']['list_member'].append(
                                    user)
                            self.cauhinh['otp_member_get']['check_mem'].append(
                                user.id)

                    offset += len(participants.users)
                    # print(offset)
                    if total_list_member >= total or len(self.list_member_add) >= self.cauhinh['otp_member_get']['total_clone']:
                        break
            self._Set_stt(f'Quét member thành công!')
        except Exception as e:
            print(e, 'Get_Mem_With_Link')
            self._Set_stt(str(e))

    async def Get_List_Name_Group(self):
        dialogs = await self.cilent.get_dialogs()
        a = 0
        for dialog in dialogs:
            if dialog.is_group and dialog.is_channel:
                self.parent.core.signals.get_mem__nolink.emit(
                    "{} : {} : {}".format(a, dialog.name, dialog.id))
                a = a+1
