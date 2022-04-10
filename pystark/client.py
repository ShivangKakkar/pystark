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
import asyncio
import logging
import importlib
import importlib.util
from typing import Union
from pystark.logger import logger
from pyrogram.types import BotCommand
from pyrogram import Client, idle, raw
from pystark.decorators import Mechanism
from pystark.config import ENV, settings
from pystark.constants import __version__
from inspect import getmembers, isfunction
from pystark.plugins.models.bans import Bans
from pystark.plugins.models.users import Users
from pystark.helpers.localization import l10n_setup, get_all_langs
from pystark.decorators.command import command_data
from pyrogram.errors import ApiIdInvalid, AccessTokenInvalid, AuthKeyDuplicated, AuthKeyUnregistered, UserDeactivated


__data__ = {"total_plugins": 0, "all_plugins": {}}
__printed__ = False


class Stark(Client, Mechanism):
    __support__ = "StarkBotsChat"
    __updates__ = "pystark"
    __channel__ = "StarkBots"

    # __id__ = None
    # __username__ = None

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
            if plugins:
                if isinstance(plugins, list):
                    for folder in plugins:
                        Stark.log(f"Searching for plugins in '{folder}'...")
                        self.load_modules(folder)
                else:
                    self.load_modules(plugins)
            addons = module.ADDONS
            if addons:
                self.log("Loading Addons")
                for i in addons:
                    path = f"pystark/plugins/addons/{i}"
                    if not path.endswith(".py"):
                        path += ".py"
                    self.load_modules(path)
            if module.DATABASE_TABLES:
                self.log("Initializing Database")
                from pystark.database.sql import Database
                Database()  # tables need to be bound to engine
                for i in module.DATABASE_TABLES:
                    self._load_sql_model(i)
            if l10n_setup():
                self.log("Localization setup completed!")
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
        plugs = []
        for path, _, files in os.walk(directory):
            for name in files:
                if name.endswith(".py"):
                    sep = "\\" if "\\" in path else "/"
                    data: list = path.split(sep, 1)
                    data.pop(0)
                    if not data:
                        file = name
                    else:
                        file = os.path.join(data[0], name)
                    plugs.append(file[:-3].replace("\\", "/"))
        return plugs

    def load_modules(self, plugins: str):
        """Load all modules from a directory or a single module as pyrogram handlers"""
        sep = "\\" if "\\" in plugins else "/"
        if plugins.endswith(".py"):  # Absolute Path
            # C Drive can't have relative path to D: Drive in Windows so needs absolute path
            plugins, file = plugins.rsplit(sep, 1)
            modules: list[str] = [file[:-3]]
        else:
            modules: list[str] = self.list_modules(plugins)
        plugins = plugins.replace(sep, ".")
        if not modules:
            return
        for module in modules:
            sep = "\\" if "\\" in module else "/"
            module = module.replace(sep, ".")
            if module.endswith(".py"):
                module = module[:-3]
            mod = importlib.import_module(plugins+"."+module)
            funcs = [func for func, _ in getmembers(mod, isfunction)]
            for func in funcs:
                try:
                    for handler, group in getattr(mod, func).handlers:
                        self.add_handler(handler, group)
                except AttributeError:  # Other Functions shouldn't be included
                    pass
            module = module.replace(".", "/")
            __data__["total_plugins"] += 1
            __data__["all_plugins"][module] = mod.__file__
            if "addons" in plugins:
                logger.info("Loaded addon - {}".format(module))
            else:
                logger.info("Loaded plugin - {}".format(module))

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

    @property
    def data(self) -> dict:
        """A special dictionary with five keys.

        | Key                | Returns                   |
        |:------------------:|:-------------------------:|
        | **total_plugins**  | number of plugins in bot  |
        | **all_plugins**    | dictionary of all plugins and their absolute paths|
        | **total_commands** | number of commands in bot |
        | **all_commands**   | dictionary of command and their descriptions if passed in ``Stark.cmd`` decorator else None |
        | **sudo_commands**  | list of all sudo commands available and includes `owner_only` commands |

        Example:

            ```python
            {
                "total_plugins": 2,
                "all_plugins": {
                    "basic":"C:\\....\\plugins\\basic.py",
                    "sample":"D:\\...\\sample.py"
                },
                "total_commands": 3,
                "all_commands": {
                    "start": "Start the bot"
                    "help": "Get help"
                    "about": "About this bot"
                },
                "sudo_commands": ["stats", "json", "sudo", "botban"]
            }
            ```
        """
        __data__.update(command_data)
        return __data__

    @property
    def total_plugins(self) -> int:
        """Number of total plugins loaded."""
        return self.data["total_plugins"]

    @property
    def all_plugins(self) -> dict:  # not "plugins" to prevent clash with pyrogram's "plugins" attribute
        """Dictionary of all plugins and their respective absolute paths.

        Example:

        ```python
        {
            "basic":"C:\\Users\\....\\plugins\\basic.py",
            "sample":"D:\\Bots\\...\\sample.py",
            "must_join":"C:\\Users\\...\\pystark\\addons\\must_join.py"
        },
        ```
        """
        return self.data["all_plugins"]

    @property
    def total_commands(self) -> int:
        """Number of total commands loaded."""
        return self.data["total_commands"]

    @property
    def all_commands(self) -> dict:
        """Dictionary of all commands and their descriptions if present else None.

        Example:

        ```python
        {
            "start": "Start the bot"
            "help": "Get help"
            "about": "About this bot"
        },
        ```
        """
        return self.data["all_commands"]

    @property
    def sudo_commands(self) -> list[str]:
        """List of all sudo commands available. Includes `owner_only` commands too."""
        return self.data["sudo_commands"]

    def update_bot_menu(self):
        dictionary = self.data["all_commands"]
        commands = []
        for key in dictionary:
            if dictionary[key]:
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

    def _load_sql_model(self, name: str):
        tables = [Users, Bans]
        for t in tables:
            if t.__tablename__ == name:
                t.__table__.create(checkfirst=True)
                if name == "users":
                    from pystark.database.sql import Database
                    db = Database()
                    if "lang" not in asyncio.get_event_loop().run_until_complete(db.columns("users")):
                        # Temporary Way
                        asyncio.get_event_loop().run_until_complete(db.add_column("users", "lang", "text"))
                self.log(f"Loaded Database Table: {name}")
                break

    @property
    async def langs(self) -> Union[dict, None]:
        """Returns all languages and corresponding file names if localization is set up otherwise None"""
        return await get_all_langs()

    async def log_tg(self, text):
        """Log a text message to your log chat as defined in environment variable [LOG_CHAT](/start/variables#log_chat)

        Parameters:
            text: Text that needs to be logged.
        """
        await self.send_message(ENV().LOG_CHAT, text)
        # No exceptions are handled for now.

    # def _set_info(self):
    #     bot = self.get_me()
    #     self.__id__ = bot.id
    #     self.__username__ = bot.username
