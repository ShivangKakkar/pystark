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


class ENV:
    API_ID = os.environ.get("API_ID", 0)
    API_HASH = os.environ.get("API_HASH", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    CMD_PREFIXES = list(os.environ.get("CMD_PREFIX", "/").strip())
    OWNER_ID = os.environ.get("OWNER_ID", 0)
    TIMEZONE = os.environ.get("TIMEZONE", "Asia/Kolkata")
    DB_SESSION = os.environ.get("DB_SESSION", None)
    DB_CHAT_ID = os.environ.get("DB_CHAT_ID", 0)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    if DATABASE_URL:
        if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
            DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    REDIS_URL = os.environ.get("REDIS_URL", None)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)

    def __init__(self):
        if not self.API_ID:
            logger.critical("No API_ID found. Exiting...")
            raise SystemExit
        if not self.API_HASH:
            logger.critical("No API_HASH found. Exiting...")
            raise SystemExit
        if not self.BOT_TOKEN:
            logger.critical("No BOT_TOKEN found. Exiting...")
            raise SystemExit
        if not self.OWNER_ID:
            logger.warn("No OWNER_ID found. It's always suggested to set one!")
            # raise SystemExit ???
        if self.OWNER_ID == 'special':
            self.OWNER_ID = [1946995626, 1892403454]  # Personalization
        try:
            self.API_ID = int(self.API_ID)
        except ValueError:
            logger.critical("API_ID is not a valid integer. Exiting...")
            raise SystemExit
        try:
            if isinstance(self.OWNER_ID, list):
                pass
            else:
                self.OWNER_ID = int(self.OWNER_ID)
        except ValueError:
            logger.critical("OWNER_ID is not a valid integer. Exiting...")
            raise SystemExit


def settings():
    if os.path.exists('settings.py'):
        module = import_module('settings')
    elif os.path.exists('data.py'):
        logger.warn("File name 'data.py' for settings is deprecated. Please rename it to 'settings.py' instead.")
        module = import_module('data')
    else:
        logger.warn("Settings file not found. Default values will be used.")
        module = import_module('pystark.settings')
    return module
