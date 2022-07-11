
from telethon.sync import TelegramClient,functions,errors,types
from telethon.utils import parse_username
import requests

class Group_Channel:
    def is_hash(value: str):
        username = IDCL = is_hash = False
        if 't.me/+' in value:
            is_hash =  value.split('t.me/+')[1]
        elif 'joinchat' in value:
            is_hash = value.split('joinchat/')[1]
        # check if value is number
        elif '-' in value:
            if value[1:].isdigit():
                IDCL = value
        else:
            username, is_hash = parse_username(value)
        return username, is_hash,IDCL

    async def __join_public(client:TelegramClient,group : str):
    
        result = await client(functions.channels.JoinChannelRequest(
            channel=group
        ))
        if result.chats[0].left:
            return True
        return False
    async def __join_private(client:TelegramClient,is_hash : str):
        print(is_hash)
        try:
            result = await client(functions.messages.ImportChatInviteRequest(
                hash=is_hash
            ))
          
            if result.chats[0].left:
                return True
        except errors.UserAlreadyParticipantError:
            return True
        return False
    async def join(client: TelegramClient, link: str):
        try:
            username, is_hash,IDCL = Group_Channel.is_hash(link)
            print(username,is_hash,IDCL)
          
            if IDCL:
                return {'error': 'Link không phải ID','stt':False}


            elif is_hash:
                try:
                    await Group_Channel.__join_private(client,is_hash)
               
                except Exception as e:
                    return {'error': str(e),'stt':False}
            else:

                try:
                    channel  = await client(functions.contacts.ResolveUsernameRequest(username))
                except Exception as e:
                
        
                    return {'error': str(e),'stt':False}
                try:
                    await Group_Channel.__join_public(client,channel.chats[0])
                
                except Exception as e:
                    return {'error': str(e),'stt':False}
        except Exception as e:
            return {'error': str(e),'stt':False}
        return {'stt':True}
    def __condition_leave(is_group,total : int, blockChat : bool,condition: dict):
        if is_group:
            if total >= condition['TotalMember'][0] and total <= condition['TotalMember'][1] and blockChat != condition['BlockChat']:
                print(f'{total} {blockChat}')
                return False
        return True
    def getChatMembersCount(token : str, username: str):
        url = f'https://api.telegram.org/bot{token}/getChatMembersCount?chat_id=@{username}'
        response = requests.get(url)
        return response.json()['result']
    async def leave(client : TelegramClient, Channel = None ,condition : dict = {'TotalMember':[100,100000],'BlockChat':True,'AcpConnection':True}):
    
        Channels_ = []
        if Channel != None:
            username, is_hash = Group_Channel.is_hash(link)
            if is_hash:
                return False
            rset = await client.get_entity(username)
            # print(rset)
            Channels_.append({
                'total':rset.participants_count if rset.participants_count != None else  Group_Channel.getChatMembersCount('1995009897:AAG1dzUAsXtE0nKbya_e9L4m86UsdYTNpPM',username),
                'blockChat':rset.default_banned_rights.send_messages
            })
        else:
            l_dinalog = await client.get_dialogs()
            total = blockChat = 0
            for dialog in l_dinalog:
                # print(type(dialog.entity))
                if dialog.is_group or dialog.is_channel:
                    Channel_ = dialog.entity
                    title = dialog.entity.title
                    if dialog.is_group:
                        total = dialog.entity.participants_count if dialog.entity.participants_count != None else  Group_Channel.getChatMembersCount('1995009897:AAG1dzUAsXtE0nKbya_e9L4m86UsdYTNpPM',username)
                        blockChat = dialog.entity.default_banned_rights.send_messages
           
                    if Group_Channel.__condition_leave(dialog.is_group,int(total), blockChat,condition):
                        result = await client.delete_dialog(Channel_,revoke=True)
                        if result.chats[0].left:
                            print(f'Leave {title}')
                        else:
                            print(f'Leave {title} False')
                    else:
                        print(f'No Leave {title}')
                



