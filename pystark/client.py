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
import ntpath
import struct
import logging
import importlib
import importlib.util
from typing import Union
from pystark.logger import logger
from pyrogram.types import Message
from pyrogram.types import BotCommand
from pyrogram import Client, idle, raw
from pystark.decorators import Mechanism
from pystark.config import ENV, settings
from pystark.constants import __version__
from inspect import getmembers, isfunction
from pystark.decorators.command import command_data, sudo_cmds
from pystark.plugins.models.users import Users
from pystark.plugins.models.bans import Bans
from pyrogram.errors import (
    ApiIdInvalid,
    AccessTokenInvalid,
    AuthKeyDuplicated,
    AuthKeyUnregistered,
    UserDeactivated,
)

__data__ = {"plugins": 0, "plugins_list": []}
__printed__ = False


class Stark(Client, Mechanism):
    __support__ = "StarkBotsChat"
    __updates__ = "pystark"
    __channel__ = "StarkBots"

    # ToDo:
    #  Make some methods private [OOP 101].
    #  Documentation for using things separately instead of activate().
    #  Make activate() a staticmethod.

    def __init__(self, **kwargs):
        global __printed__
        if not __printed__:
            print(f'Welcome to PyStark [v{__version__}]')
            print('Copyright (C) 2021-2022 Stark Bots <https://github.com/StarkBotsIndustries> \n')
            __printed__ = True
        env = ENV()
        super().__init__(
            ":memory:",
            api_id=env.API_ID,
            api_hash=env.API_HASH,
            bot_token=env.BOT_TOKEN,
            **kwargs
        )

    def activate(self):
        """Main method of `Stark` class which loads plugins and activates/runs your bot."""
        module = settings()
        try:
            self.log("Starting the Bot")
            self.start()
            self.log("Loading Modules")
            plugins = getattr(module, "PLUGINS")
            if isinstance(plugins, list):
                for folder in plugins:
                    Stark.log(f"Searching for plugins in '{folder}'...")
                    self.load_modules(folder)
            else:
                self.load_modules(plugins)
            from pystark.plugins import addons as plugins
            addons = module.ADDONS
            if module.STARKBOTS:
                addons.append("buttons")
            for i in addons:
                path = plugins.__path__[0]+f"/{i}"
                if not path.endswith(".py"):
                    path += ".py"
                self.load_modules(path)
            for i in module.DATABASE_TABLES:
                self._load_sql_model(i)
            if getattr(module, "SET_BOT_MENU"):
                self.log("Updating Bot Menu")
                self.update_bot_menu()
            else:
                self.log("Skipping Bot Menu Update")
            logger.info("{} is now running...".format('@' + self.get_me().username))
            idle()
        finally:
            if getattr(module, "SET_BOT_MENU"):
                try:
                    self.remove_bot_menu()
                except ConnectionError:
                    pass
            self.stop()
            logger.info("Bot has stopped working. For issues, visit <https://t.me/StarkBotsChat>")

    def run(self):
        """Alias of `Stark.activate()`"""
        self.activate()

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
        logger.info("For support visit @{}".format(self.__support__))
        raise SystemExit

    @staticmethod
    def list_modules(directory):
        """List all modules in a directory"""
        if not os.path.exists(directory):
            Stark.log(f"No directory named '{directory}' found")
            return
        if "/." not in directory:
            directory = directory.replace('.', '/')
        return [file[:-3] for file in os.listdir(directory) if file.endswith(".py")]

    def load_modules(self, plugins: str):
        """Load all modules from a directory or a single module as pyrogram handlers"""
        if plugins.endswith(".py"):
            plugins = os.path.abspath(plugins)
            x, y = ntpath.split(plugins)
            file = y or ntpath.basename(x)
            plugins = x if y else ntpath.dirname(x)
            plugins = ntpath.relpath(plugins)
            modules = [file[:-3]]
        else:
            modules = self.list_modules(plugins)
        if not modules:
            return
        for module in modules:
            plugins = os.path.abspath(plugins)
            spec = importlib.util.spec_from_file_location(module, plugins+"/"+module+".py")
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            funcs = [func for func, _ in getmembers(mod, isfunction)]
            for func in funcs:
                try:
                    for handler, group in getattr(mod, func).handlers:
                        self.add_handler(handler, group)
                except AttributeError:  # Other Functions shouldn't be included
                    pass
            __data__["plugins"] += 1
            __data__["plugins_list"].append(module)
            if "addons" in plugins:
                logger.info("Loaded addon - {}.py".format(module))
            else:
                logger.info("Loaded plugin - {}.py".format(module))
        # logger.info("Loaded In-Built [Default] Plugins")

    @staticmethod
    def list_args(message: Union[Message, str], split: str = " ") -> list[str]:
        """List arguments passed in a message. Removes first word (the command itself)

        Parameters:

            message (pystark.Message): Pass a command message or message.text to get arguments passed in this message.

            split (str, optional): Define how to split the arguments, defaults to whitespace.

        Example:

            If text is `/start reply user`, return value would be `["reply", "user"]`
        """
        if isinstance(message, Message):
            message = message.text
        args = message.split(split)
        args.pop(0)
        return args

    @staticmethod
    def log(message, level: Union[str, int] = logging.INFO):
        """Log messages to console.

        | String       | Integer  |
        |:------------:|:--------:|
        | **debug**    | 10       |
        | **info**     | 20       |
        | **warning**  | 30       |
        | **error**    | 40       |
        | **critical** | 50       |

        Parameters:

            message (Any): Item to print to console.
            level (optional): Logging level as string or int.
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

    @staticmethod
    def data(key: str = None):
        """Returns a special dictionary with five keys.

        | Key                      | Returns                   |
        |:------------------------:|:-------------------------:|
        | **plugins**              | number of plugins in bot  |
        | **plugins_list**         | list of plugins in bot    |
        | **commands**             | number of commands in bot |
        | **commands_list**        | list of commands in bot   |
        | **command_descriptions** | dictionary of command and their descriptions if passed in ``Stark.cmd`` decorator |

        Parameters:

            key (str, optional) : If you want to get only one of the five keys from `["plugins", "plugins_list", "commands", "commands_list", "command_descriptions"]`

        Example:

            ```python
            {"plugins": 2, "plugins_list": ["basic", "sample"], "commands": 5, "command_list": ["start", "help", "about", "id", "sample"]}, command_descriptions: {"start": "Start the bot"}
            ```
        """
        __data__.update(command_data)
        if not key:
            return __data__
        else:
            return __data__[key]

    @staticmethod
    def sudo_commands() -> list[str]:
        """Returns a list of all sudo commands available."""
        return sudo_cmds

    def update_bot_menu(self):
        dictionary = Stark.data("command_descriptions")
        commands = []
        for key in dictionary:
            commands.append(BotCommand(key, str(dictionary[key])).write())
        self.send(
            raw.functions.bots.SetBotCommands(
                scope=raw.types.BotCommandScopeDefault(),
                lang_code='en',
                commands=commands
            )
        )

    def remove_bot_menu(self):
        self.send(
            raw.functions.bots.ResetBotCommands(
                scope=raw.types.BotCommandScopeDefault(),
                lang_code='en',
            )
        )

    @staticmethod
    def _load_sql_model(name: str):
        tables = [Users, Bans]
        for t in tables:
            if t.__tablename__ == name:
                t.__table__.create(checkfirst=True)
