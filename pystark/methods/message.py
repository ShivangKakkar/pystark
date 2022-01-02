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


import asyncio
from pyromod.utils import patch, patchable
from pyrogram.types import Message


@patch(Message)
class Message:
    @patchable
    async def react(self, text: str, del_in: int = 0, **kwargs):
        reply = await self.reply(text, quote=True, disable_web_page_preview=True, **kwargs)
        if del_in:
            await asyncio.sleep(del_in)
            await reply.delete()
