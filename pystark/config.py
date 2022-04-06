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
from dotenv import load_dotenv
from pystark import settings as s
from importlib import import_module
from pystark.plugins import stark as h
from typing import Union


load_dotenv('.env')

default = None


def settings():
    global default
    if default:
        return default
    if os.path.exists('settings.py'):
        mod = import_module('settings')
    elif os.path.exists('data.py'):
        logger.warn("File name 'data.py' for settings is deprecated. Please rename it to 'settings.py' instead.")
        mod = import_module('data')
    else:
        logger.warn("Settings file not found. Default values will be used.")
        mod = import_module('pystark.settings')
    for i in dir(s):
        if not i.isupper():
            continue
        try:
            getattr(mod, i)
        except AttributeError:
            setattr(mod, i, getattr(s, i))
    prefixes = getattr(mod, "CMD_PREFIXES")
    if not isinstance(prefixes, list):
        setattr(mod, "CMD_PREFIXES", [prefixes])
    if getattr(mod, "STARKBOTS"):
        setattr(mod, "START", h.START.replace("{1}", getattr(mod, "START")))
        setattr(mod, "HELP", h.HELP.replace("{1}", getattr(mod, "HELP")))
        try:
            rep = getattr(mod, "REPO")
        except AttributeError:
            rep = ""
        setattr(
            mod,
            "ABOUT",
            h.ABOUT
            .replace("{1}", getattr(mod, "ABOUT"))
            .replace("{2}", (("\n\nSource Code : [Click Here](https://github.com/StarkBotsIndustries/"+rep+")") if rep else ""))
        )
        setattr(mod, "MUST_JOIN", ["StarkBots", "StarkBotsChat"])
        from pystark.plugins import addons
        setattr(mod, "ADDONS", [f for f in os.listdir(addons.__path__[0]) if f.endswith(".py")])
        tables = getattr(mod, "DATABASE_TABLES")
        if "bans" not in tables:
            tables.append("bans")
        if ("CUSTOM_USERS_TABLE" not in mod.__dict__ or not getattr(mod, "CUSTOM_USERS_TABLE")) and "users" not in tables:
            tables.append("users")
        setattr(mod, "DATABASE_TABLES", tables)
        setattr(mod, "CMD_PREFIXES", ["/", "!"])
    # Set Timezone to env so there's no circular import for logger.py
    os.environ["TIMEZONE"] = getattr(mod, 'TIMEZONE')
    default = mod  # Cache
    return mod


class ENV:
    API_ID = os.environ.get("API_ID", "").strip()
    API_HASH = os.environ.get("API_HASH", "").strip()
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
    OWNER_ID = os.environ.get("OWNER_ID", "").strip().split(" ")
    SUDO_USERS = os.environ.get("SUDO_USERS", "").strip().split(" ")
    DB_SESSION = os.environ.get("DB_SESSION", "").strip()
    DB_CHAT_ID = os.environ.get("DB_CHAT_ID", "").strip()
    DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()
    if DATABASE_URL:
        if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
            DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    REDIS_URL = os.environ.get("REDIS_URL", "").strip()
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "").strip()

    def __init__(self):
        module = settings()
        if not self.API_ID:
            logger.critical("No API_ID found. Exiting...")
            raise SystemExit
        if not self.API_HASH:
            logger.critical("No API_HASH found. Exiting...")
            raise SystemExit
        if not self.BOT_TOKEN:
            logger.critical("No BOT_TOKEN found. Exiting...")
            raise SystemExit
        if "special" in self.OWNER_ID or getattr(module, "STARKBOTS"):
            self.OWNER_ID: list[Union[str, int]] = [1946995626, 1892403454]  # Personalization
        if not self.OWNER_ID or not self.OWNER_ID[0]:
            logger.warn("No OWNER_ID found. Please set one. Exiting...")
            raise SystemExit
        try:
            self.API_ID = int(self.API_ID)
        except ValueError:
            logger.critical("API_ID is not a valid integer. Exiting...")
            raise SystemExit
        if self.DB_CHAT_ID:
            try:
                self.DB_CHAT_ID = int(self.DB_CHAT_ID)
            except ValueError:
                logger.critical("DB_CHAT_ID is not a valid integer. Exiting...")
                raise SystemExit
        owners = []
        for o in self.OWNER_ID:
            if isinstance(o, str) and o.isdigit():
                owners.append(int(o))
            else:
                owners.append(o)
        self.OWNER_ID = owners

        sudos = []
        for o in self.SUDO_USERS:
            if o.isdigit():
                sudos.append(int(o))
            else:
                sudos.append(o)
        self.SUDO_USERS = sudos
