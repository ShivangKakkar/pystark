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
from typing import Union
from .decorators import Mechanism
from pyrogram import Client, idle
from pyrogram.types import Message
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
from .decorators.command import command_data

data = {"plugins": 0, "plugins_list": []}


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
    def log(message, level: Union[str, int] = logging.INFO):
        """Log messages to console.

        .. list-table:: Possible values for Level
           :widths: 50 50
           :header-rows: 1

           * - String
             - Integer
           * - **debug**
             - 10
           * - **info**
             - 20
           * - **warning**
             - 30
           * - **error**
             - 40
           * - **critical**
             - 50

        Parameters:
            message: Item to print to console.
            level: Logging level as string or int.
        """
        if isinstance(level, str):
            level = level.lower()
        if level in ["critical", 50]:
            level = logging.CRITICAL
        elif level in ["error", 40]:
            level = logging.ERROR
        elif level in ["warning", "warn", 30]:
            level = logging.WARNING
        elif level in ["info", 20]:
            level = logging.INFO
        elif level in ["debug", 10]:
            level = logging.DEBUG
        logger.log(level, message)

    def activate(self, plugins: str = 'plugins', default_plugins: bool = True):
        """Activate/Run your bot.

        Parameters:
            plugins (`str`):
                Path of the 'plugins' directory in relation to the root directory.
                If name of your directory is 'files' and it is in the same folder as 'bot.py', pass plugin='files'.
                Defaults to 'plugins', i.e, a folder named 'plugins' in same directory as 'bot.py'

            default_plugins (`bool`):
                Pass False to disable default plugins. Defaults to True.
        """
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
            data["plugins"] += 1
            data["plugins_list"].append(module)
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

    @staticmethod
    def list_args(message: Union[Message, str], split: str = " "):
        """List arguments passed in a message. Removes first word (the command itself)

        Parameters:
            message:
                Pass a command message or message.text to get arguments passed in this message.

            split (`str`):
                How to split the arguments, Defaults to ' '.

        **Example**: if text is "/start reply user", reply would be ["reply", "user"]
        """
        if isinstance(message, Message):
            message = message.text
        args = message.split(split)
        args.pop(0)
        return args

    @staticmethod
    def data(key: str = None):
        """Returns a special dictionary with four keys.

        .. list-table:: Possible Keys
           :widths: 25 75
           :header-rows: 1

           * - Key
             - Returns
           * - **plugins**
             - number of plugins in bot
           * - **plugins_list**
             - list of plugins in bot
           * - **commands**
             - number of commands in bot
           * - **commands_list**
             - list of commands in bot

        Parameters:
            key (`str`) :
                Return only one of the four keys from ["plugins", "plugins_list", "commands", "commands_list"]

        Example:
            .. code-block:: python

                {"plugins": 2, "plugins_list": ["basic", "sample"], "commands": 5, "command_list": ["start", "help", "about", "id", "sample"]}
        """
        data.update(command_data)
        if not key:
            return data
        else:
            return data[key]
