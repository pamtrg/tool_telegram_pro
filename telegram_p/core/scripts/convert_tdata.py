
from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession 
import asyncio

async def convertP(pathfilesession,pathfiletdata):

    try:

        oldclient = TelegramClient(pathfilesession)
        await oldclient.connect()
        # await oldclient.PrintSessions()
        in4 = await oldclient.get_me()
        # print(in4)
        if  in4 == None:
            return False

        tdesk = await oldclient.ToTDesktop(flag=UseCurrentSession)
        # tdesk.__isLoaded = True
        a =  tdesk.SaveTData(pathfiletdata)
        # print(a)
        await oldclient.disconnect()
        return a
    except Exception as e:
        print(e)
        return False 

# asyncio.run(
#     convertP(
#         r'C:\Users\MKSTORE\Downloads\Telegram Desktop\New folder (3)\+84797479251.session',
#         r'D:\tool_telegram_pro\Telegram_Desktop\+84562674384\tdata'

#     )
# )