import os
import sys
import traceback
from pyrogram import Client
from pystark import Stark
from pystark.config import API_ID, API_HASH, DB_SESSION, DB_CHAT_ID
from pystark.logger import logger
from telegram import TelegramDB, DataPack, Member

if not DB_SESSION:
    Stark.log('No DB_SESSION defined. Exiting...', "critical")
    raise SystemExit
userbot = Client(DB_SESSION, api_id=API_ID, api_hash=API_HASH)
userbot.start()

if not DB_CHAT_ID:
    Stark.log("No DB_CHAT_ID found. Creating a chat for database", "warning")
    channel = userbot.create_channel("PyStark Telegram DB")
    Stark.log(f"Telegram DB Channel ID is {channel.id}")
    DB_CHAT_ID = channel.id

if isinstance(DB_CHAT_ID, str) and DB_CHAT_ID[1:].isdigit():
    DB_CHAT_ID = int(DB_CHAT_ID)


sys.stdout = open(os.devnull, 'w')
try:
    Session = TelegramDB(userbot, DB_CHAT_ID, debug=True, LOGGER=logger)
    sys.stdout = sys.__stdout__
except Exception as e:
    sys.stdout = sys.__stdout__
    Stark.log(str(e), "critical")
    Stark.log("Your DB_CHAT_ID is incorrect.", "critical")
    Stark.log(traceback.format_exc(), "critical")
    raise SystemExit
Stark.log("Initializing TelegramDB [Copyright (C) 2022 anonyindian]")
