


import struct, base64
from telethon.sessions.string import StringSession
from telethon.sync import TelegramClient
from pyrogram.storage.storage import Storage
from pyrogram import utils








def telethon_to_unpack(string):
  ST = StringSession(string)
  return ST


async def start_session(string):
  async with TelegramClient(StringSession(string), 6 ,"eb06d4abfb49dc3eeb1aeb98ae0f581e") as ses:
    ml = ses.get_me()
  return ml


def pack_to_pyro(data : StringSession, ses ):
  Dt = Storage.SESSION_STRING_FORMAT if ses.id < utils.MAX_USER_ID else Storage.SESSION_STRING_FORMAT
  

  return base64.urlsafe_b64encode(
            struct.pack(
                Dt,
                data.dc_id,
                6,
                None,
                data.auth_key.key,
                ses.id,
                ses.bot
        )).decode().rstrip("=")


def tele_to_pyro(string,MK):
    DL = telethon_to_unpack(string)
   
    return pack_to_pyro(DL, MK)