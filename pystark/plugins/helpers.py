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

from pystark import Stark
from pystark.logger import logger
from pystark.config import settings, ENV
from pyrogram.errors import PeerIdInvalid
from pystark.database.sql import Database


module = settings()
OWNER_ID = ENV().OWNER_ID
db = Database()


async def replace(m, msg, bot):
    # I do know str.format() but that'll be unnecessary execution of multiple things and anyway these are optional.
    # For same reason, IF statements are used below. Replies should be fast no matter what.
    # Also, prevents
    if '{user}' in m:
        m = m.replace("{user}", msg.from_user.first_name)
    if '{bot}' in m:
        m = m.replace("{bot}", (await bot.get_me()).first_name)
    if '{user_mention}' in m:
        m = m.replace("{user_mention}", msg.from_user.mention)
    if '{bot_mention}' in m:
        m = m.replace("{bot_mention}", (await bot.get_me()).mention)
    if '{owner}' in m:
        owner = '@pystark'
        if OWNER_ID:
            try:
                owner = (await bot.get_users(OWNER_ID[0])).mention
            except PeerIdInvalid:
                logger.warn(f"Can't interact with bot owner [user={OWNER_ID[0]}]. Please send a message to bot.")
        m = m.replace("{owner}", owner)
    return m

# ToDO
#   1. Don't repeat replace() function everywhere.


async def send_buttons():
    if module.NO_BUTTONS:
        return False
    if 'buttons' not in module.ADDONS and 'buttons.py' not in module.ADDONS:
        return False
    if module.STARKBOTS:
        return True
    return False


LOADED_BUT_EMPTY = "You loaded '{}' addon but {} message is empty"

cache_commands = ""


async def replace_commands(bot: Stark, text: str):
    global cache_commands
    if cache_commands:
        return cache_commands
    basics = {"1": "", "2": "", "3": "", "4": ""}
    others = []
    cmds = bot.all_commands
    for c in cmds:
        if cmds[c]:
            x = f"/{c} - {cmds[c]} \n"
            if c == "start":
                basics["1"] = x
            elif c == "help":
                basics["2"] = x
            elif c == "about":
                basics["3"] = x
            elif c == "id":
                basics["4"] = x
            else:
                others.append(x)
    basics_str = basics["1"] + basics["2"] + basics["3"] + basics["4"]
    others_str = "".join(others)
    text = text.replace("{commands}", others_str+basics_str)
    cache_commands = text
    return text
