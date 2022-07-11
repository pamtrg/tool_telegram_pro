


import asyncio


import io
from telethon.tl.types import InputPeerUser,GlobalPrivacySettings,InputPrivacyValueAllowContacts,InputPrivacyValueAllowAll,InputPrivacyKeyStatusTimestamp,InputPrivacyValueDisallowAll,InputPrivacyValueDisallowUsers,InputPrivacyKeyChatInvite
from telethon.tl.functions.messages import  GetMessagesViewsRequest
import requests,shutil,time
from telethon import TelegramClient,events,errors
from telethon.network import ConnectionTcpAbridged
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import PeerUser,PeerChannel
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateUsernameRequest,GetAuthorizationsRequest,ResetAuthorizationRequest,SetGlobalPrivacySettingsRequest,SetPrivacyRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty,InputPeerChannel,InputUser,InputChannel
from telethon.tl.functions import channels
from telethon.tl.functions.messages import ImportChatInviteRequest
import logging as log
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import UserChannelsTooMuchError
log.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=log.INFO)
logger = log.getLogger(__name__)
def bytes_to_string(byte_count):
    suffix_index = 0
    while byte_count >= 1024:
        byte_count /= 1024
        suffix_index += 1

    return '{:.2f}{}'.format(
        byte_count, [' bytes', 'KB', 'MB', 'GB', 'TB'][suffix_index]
    )

class TELEGRAM_CLIENT:


    def __init__(self, id: int, hash: str, session_name: str, proxy: object = None) -> object:
        self.api_id = id

        self.api_hash = hash
        self.session_name = session_name
        self.client= TelegramClient(session_name,self.api_id, self.api_hash,proxy=proxy,connection_retries=100000000,retry_delay=0.1,)

        self.listmas = []
      
 
    async def get_entity_(self,entity):
        try:
            return  await  self.client.get_entity(entity)
        except Exception as e:
            return {"er":e}
    async def Add_mem(self,channel,USER):
        try:
            await self.client(InviteToChannelRequest(channel,[USER]))
            return True
        except Exception as e:
            return e

    async def Kill_list_Session(self):

        GetSessions = await self.client(GetAuthorizationsRequest()) 
        if len(GetSessions.authorizations)>1:
            print("Another Session    :\tYes")
            for ss in GetSessions.authorizations:
                SessionHash = ss.hash
                SessionIp   = ss.ip
                if SessionHash>0:
                    result = await self.client(ResetAuthorizationRequest(hash=SessionHash))
                    print("Session Killed     :\t" + str(SessionIp)) 
        else:
            print("Another Session    :\tNo")


    async def send_message_all(self,entity,message=None,image=False,file=None):
        try:
            # if type(entity) == int:
            #     entity = PeerUser(entity) if object_ == 'User' else PeerChannel(entity)
            if file:
                await self.client.send_file(entity,file)
            if image:
                await self.client.send_file(entity,image)
            if message:
                await self.client.send_message(entity,message)

           
            # await self.client.send_file(
            #     entity=entity,file=image,caption=message,
            #     progress_callback=self.upload_progress_callback)


            
            return True
        except Exception as e:
            print(e)
            return False


    async def Get_member_groups(self,group='', getfull=False):
        groups = []
        if getfull:
            dialogs = await  self.client.get_dialogs()
            for dialog in dialogs:
                
                if dialog.is_group and dialog.is_channel:
                    groups.append(dialog)
        else:
            group = await  self.client.get_entity(group)
            groups.append(group)

        return groups


    async def  join_channel(self,channel,otp='Private') -> bool:
        try:
            if otp == 'Private':
                try:
                    rs = await self.client(ImportChatInviteRequest(channel))
                except Exception as e:
                    if 'The authenticated user is ' in str(e):
                        return True
                    return False

            else:
                rs = await self.client(channels.JoinChannelRequest(channel))
        except Exception as e:
            print(e)
            return False

        # print(b)
        # chat = (await self.client(channels.GetChannelsRequest([b]))).chats[0]
        # chat = (await self.client(channels.GetChannelsRequest(
        #     [channel]
        #     ))).chats[0]

        return True
        # return {'response':True,'data':rs}
    
    async def get_in4(self):
        try:
            me = await self.client.get_me()

         
            
            first_name = me.first_name if me.first_name else ""
            last_name = me.last_name if me.last_name else ""
            return {'response': True,'data':{
                'ID': me.id,'FULLNAME':first_name + ' ' +last_name,
                'USERNAME':me.username,
                'PHONE':me.phone,'AVATAR': 'True' if me.photo else 'False'
                }
                    
                    }
        except Exception as e:
            print(e)
            return {'response':False,'data':str(e)}




    async def connect(self):
        try:
            await self.client.connect()
            return True
        except:
            return False

    async def PrivacySettings(self):
    # large_long = 2**62
    # request = functions.account.SetPrivacyRequest(
    #     key=types.InputPrivacyKeyChatInvite(),
    #     rules=[types.InputPrivacyValueDisallowUsers(users=[large_long])]
    # )
    # with pytest.raises(TypeError):
    #     bytes(request)
        large_long = 2**62
        result =await self.client(SetPrivacyRequest(
            key=InputPrivacyKeyChatInvite(),
            rules=[InputPrivacyValueAllowContacts()]
        ))
        # print(result.stringify())
    async def Settings_online(self,hide):
        hideOrShow = InputPrivacyValueDisallowAll() if hide else InputPrivacyValueAllowAll()
        result =await self.client(SetPrivacyRequest(
            key=	InputPrivacyKeyStatusTimestamp(),
            rules=[hideOrShow]
        ))
        # prin
    async def log_out(self):
        await  self.client.log_out()
        time.sleep(2)
        try:
            shutil.rmtree(self.session_name)
        except:
            pass
    async def close_connection(self):
        try:
            await self.client.disconnect()
            return True
        except:
            return False
    async def buff_view(self,channel,search):
        # channel = await self.client.get_entity(channel)
        try:
            list_id = []
            async for message in self.client.iter_messages(channel, search=search):
                list_id.append(message.id)
            result =await self.client(GetMessagesViewsRequest(
                peer=channel,
                id=list_id,
                increment=True
            ))
            print(result,list_id)
            return True
        except Exception as e:
            print(e) 
            return False
        # print(result)

    async def get_chat(self,InputUser_):
        codes = []
        if InputUser_ == 1:
            Input  = InputUser(777000,4976228689240769012)
        elif InputUser_ == 2:
            Input = PeerUser(178220800)
        else: 
            Input = InputUser_
        messages = await self.client.get_messages(Input, limit=10)
       
        # Iterate over all (in reverse order so the latest appear
        # the last in the console) and print them with format:
        # "[hh:mm] Sender: Message"
        for msg in reversed(messages):
            # Note how we access .sender here. Since we made an
            # API call using the self client, it will always have
            # information about the sender. This is different to
            # events, where Telegram may not always send the user.

            # Format the message content
            if getattr(msg, 'media', None):
                self.found_media[msg.id] = msg
                content = '<{}> {}'.format(
                    type(msg.media).__name__, msg.message)

            elif hasattr(msg, 'message'):
                content = msg.message
            elif hasattr(msg, 'action'):
                content = str(msg.action)
            else:
                # Unknown message, simply print its class name
                content = type(msg).__name__
      
            # And print it to the user
            if InputUser_:
                codes.append(content)
                # if 'Login code' in content:
                #     code= '{} ==> {}; {}'.format(msg.date ,'Telegram', content[12:17])
                #     codes.append(code)
            else:
                codes.append(content)
            # open('datachat.user', 'w').write(str(msg)+'\n')



        return codes
    async  def is_auth(self):
        # print(self.session_name)
        if not await self.client.is_user_authorized():
            return False
        return True





    @staticmethod
    def upload_progress_callback(uploaded_bytes, total_bytes):
        TELEGRAM_CLIENT.print_progress(
            'Uploaded', uploaded_bytes, total_bytes
        )
    @staticmethod
    def print_progress(progress_type, downloaded_bytes, total_bytes):
        print('{} {} out of {} ({:.2%})'.format(
            progress_type, bytes_to_string(downloaded_bytes),
            bytes_to_string(total_bytes), downloaded_bytes / total_bytes)
        )