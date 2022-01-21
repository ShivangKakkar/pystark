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

command_data = {"commands": 0, "commands_list": [], "command_descriptions": {}}


class Command(OnMessage):
    @staticmethod
    def command(
        cmd: str = None,
        description: str = None,
        group: int = 0,
        owner_only: bool = False,
        private: bool = False,
        extra_filters=None
    ):
        if not cmd and not extra_filters:
            filters_ = None
        elif cmd and extra_filters:
            command_data["commands"] += 1
            command_data["commands_list"].append(cmd)
            filters_ = f.command(cmd, prefixes=CMD_PREFIXES) & extra_filters
        elif extra_filters:
            filters_ = extra_filters
        else:
            command_data["commands"] += 1
            command_data["commands_list"].append(cmd)
            filters_ = f.command(cmd, prefixes=CMD_PREFIXES)
        if cmd and description:
            command_data["command_descriptions"][cmd] = description
        if owner_only:
            filters_ = filters_ & f.user(OWNER_ID)
        if extra_filters:
            filters_ = filters_ & extra_filters
        if private:
            filters_ = filters_ & f.private
        decorator = OnMessage.on_message(filters_, group)
        return decorator

    cmd = command
