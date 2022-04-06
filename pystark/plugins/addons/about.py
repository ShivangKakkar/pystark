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
from pyrogram.types import InlineKeyboardMarkup
from pystark.plugins.helpers import replace, send_buttons, module
from pystark.plugins.stark import HOME_BUTTON


@Stark.cmd('about', description="About the bot", private_only=True)
async def about_func(bot, msg):
    try:
        text = await replace(module.ABOUT, msg, bot)
        if await send_buttons():
            await msg.react(text, reply_markup=InlineKeyboardMarkup(HOME_BUTTON))
        else:
            await msg.react(text)
    except AttributeError:
        pass
