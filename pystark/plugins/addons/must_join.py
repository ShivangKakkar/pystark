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

from pystark import Stark, filters
from pystark.config import settings, ENV
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Stark.cmd(private_only=True, extra_filters=~filters.edited & filters.incoming, group=-1)
async def must_join_channel(bot: Stark, msg: Message):
    if ENV.DATABASE_URL:
        from pystark.plugins.helpers import db
        if (await db.has_table("bans")) and msg.from_user.id in (await db.get_all_primary_keys("bans")):
            await msg.reply("You have been banned from using this bot !", quote=True)
            await msg.stop_propagation()
            return
    module = settings()
    try:
        chats = module.MUST_JOIN
    except AttributeError:
        chats = []
    if not chats:
        Stark.log("Addon must_join is loaded but no chat is listed in MUST_JOIN var of settings", "warn")
        return
    nope = []
    for chat in chats:
        try:
            await bot.get_chat_member(chat, msg.from_user.id)
        except UserNotParticipant:
            nope.append(chat)
        except ChatAdminRequired:
            Stark.log(f"I'm not admin in the {chat} Chat !", "warning")
    if not nope:
        return
    buttons = []
    for i in nope:
        c = await bot.get_chat(i)
        if isinstance(i, int):
            i = c.title
        buttons.append([InlineKeyboardButton(f"✨ Join {i} ✨", url=c.invite_link)])
    try:
        await msg.reply(
            f"You must join my {'chats' if len(nope)>1 else 'chat'} to use me. Click on below buttons to join {'them' if len(nope)>1 else 'it'} \n\nAfter joining try again !",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        await msg.stop_propagation()
    except ChatWriteForbidden:
        pass
