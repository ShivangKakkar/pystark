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


from pyrogram import filters as f
from ..config import CMD_PREFIXES, OWNER_ID
from pyrogram.methods.decorators.on_message import OnMessage


class Command(OnMessage):
    @staticmethod
    def command(
        cmd: str,
        # help_string: str = "",
        group: int = 0,
        owner_only: bool = False,
        extra_filters=None
    ):
        filters_ = f.command(cmd, prefixes=CMD_PREFIXES)
        if owner_only:
            filters_ = filters_ & f.user(OWNER_ID)
        if extra_filters:
            filters_ = filters_ & extra_filters
        decorator = OnMessage.on_message(filters_, group)
        return decorator

    cmd = command
