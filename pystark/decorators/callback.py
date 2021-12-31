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
from pyrogram.methods.decorators.on_callback_query import OnCallbackQuery


class Callback(OnCallbackQuery):
    @staticmethod
    def callback(
        query_string: str = None,
        in_list: list = None,
        startswith: bool = False,
        group: int = 0,
        filters=None
    ):
        if in_list:
            cmd_filter = f.create(lambda _, __, query: query.data in in_list)
        else:
            if not startswith:
                cmd_filter = f.create(lambda _, __, query: query.data == query_string)
            else:
                cmd_filter = f.create(lambda _, __, query: query.data.startswith(query_string))
        if not filters:
            filters = cmd_filter
        else:
            filters = cmd_filter & filters
        decorator = OnCallbackQuery.on_callback_query(filters, group)
        return decorator
