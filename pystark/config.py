# PyStark - Python add-on extension to Pyrogram
# Copyright (C) 2021-2022 Stark Bots <https://github.com/StarkBotsIndustries>
#
# This file is part of PyStark.
#
# PyStark is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyStark is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyStark. If not, see <https://www.gnu.org/licenses/>.


import os
from .logger import logger
from importlib import import_module
from dotenv import load_dotenv

load_dotenv('.env')

API_ID = os.environ.get("API_ID", 0)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
CMD_PREFIXES = list(os.environ.get("CMD_PREFIX", "/").strip())
OWNER_ID = os.environ.get("OWNER_ID", 1946995626)
TIMEZONE = os.environ.get("TIMEZONE", "Asia/Kolkata")

DB_SESSION = os.environ.get("DB_SESSION", None)
DB_CHAT_ID = os.environ.get("DB_CHAT_ID", 0)
DATABASE_URL = os.environ.get("DATABASE_URL", None)
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
REDIS_URL = os.environ.get("REDIS_URL", None)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)


def check_environment():
    if not API_ID:
        logger.critical("No API_ID found. Exiting...")
        raise SystemExit
    if not API_HASH:
        logger.critical("No API_HASH found. Exiting...")
        raise SystemExit
    if not BOT_TOKEN:
        logger.critical("No BOT_TOKEN found. Exiting...")
        raise SystemExit
    try:
        int(API_ID)
    except ValueError:
        logger.critical("API_ID is not a valid integer. Exiting...")
        raise SystemExit
    try:
        int(OWNER_ID)
    except ValueError:
        logger.warn("OWNER_ID is not a valid integer. Exiting...")
        raise SystemExit
    if os.path.exists('data.py'):
        module = import_module('data')
    else:
        logger.warn("No 'data.py' found. Default values will be used.")
        module = import_module('pystark.data')
    return module
