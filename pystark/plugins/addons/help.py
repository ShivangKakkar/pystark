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
from pystark.plugins.stark import HOME_BUTTON
from pyrogram.types import InlineKeyboardMarkup
from pystark.plugins.helpers import replace, send_buttons, module, LOADED_BUT_EMPTY, replace_commands


@Stark.cmd('help', description="How to use the bot?", private_only=True)
async def help_func(bot: Stark, msg):
    try:
        if not module.HELP:
            Stark.log(LOADED_BUT_EMPTY.format("help", "help"), "warn")
            return
        text = str(module.HELP)
        if "{commands}" in text:
            text = await replace_commands(bot, text)
        text = await replace(text, msg, bot)
        if await send_buttons():
            await msg.react(text, reply_markup=InlineKeyboardMarkup(HOME_BUTTON))
        else:
            await msg.react(text)
    except AttributeError:
        pass
