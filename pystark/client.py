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
import struct
import logging
from .logger import logger
from .decorators import Mechanism
from pyrogram import Client, idle
from importlib import import_module
from inspect import getmembers, isfunction
from .config import API_ID, API_HASH, BOT_TOKEN, check_environment
from pyrogram.errors import (
    ApiIdInvalid,
    AccessTokenInvalid,
    AuthKeyDuplicated,
    AuthKeyUnregistered,
    UserDeactivated,
)


class Stark(Client, Mechanism):
    support = "@StarkBotsChat"

    def __init__(self):
        check_environment()
        super().__init__(
            ":memory:",
            api_id=int(API_ID),
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
        )

    def start(self):
        try:
            super().start()
            return
        except ApiIdInvalid:
            logger.critical("API_ID and API_HASH combination is incorrect.")
        except AccessTokenInvalid:
            logger.critical("BOT_TOKEN is invalid.")
        except (AuthKeyUnregistered, AuthKeyDuplicated, struct.error):
            logger.critical("Your STRING_SESSION is invalid. Please terminate it and generate a new one.")
        except UserDeactivated:
            logger.critical(f"Account deleted. Time for me to rest.")
        except KeyboardInterrupt:
            logger.critical("Keyboard Interrupt. Exiting..")
        logger.info("For support visit {}".format(Stark.support))
        raise SystemExit

    @staticmethod
    def log(message, level=logging.INFO):
        logger.log(level, message)

    def activate(self, plugins: str = None, default_plugins: bool = True):
        if not plugins:
            plugins = 'plugins'
        self.start()
        self.load_modules(plugins)
        if default_plugins:
            from pystark import plugins
            self.load_modules(plugins.__path__[0])
        logger.info("{} is now running...".format('@' + self.get_me().username))
        idle()
        self.stop()
        logger.info("Bot has stopped working")

    def load_modules(self, plugins):
        modules = self.list_modules(plugins)
        if not modules:
            return
        for module in modules:
            if module.startswith("__"):
                return
            if 'pystark' in plugins:
                plugins = 'pystark.plugins'
            mod = import_module(plugins+'.'+module)
            funcs = [func for func, _ in getmembers(mod, isfunction)]
            for func in funcs:
                try:
                    for handler, group in getattr(mod, func).handlers:
                        self.add_handler(handler, group)
                except AttributeError:  # Other Functions shouldn't be included
                    pass
            if module == "basic":
                logger.info("Loaded - Default Plugins")
            else:
                logger.info("Loaded - {}.py".format(module))

    @staticmethod
    def list_modules(directory):
        try:
            if "/." not in directory:
                directory = directory.replace('.', '/')
            return [file[:-3] for file in os.listdir(directory) if file.endswith(".py")]
        except FileNotFoundError:
            logger.warn("No Custom Plugins Found!")
            return
