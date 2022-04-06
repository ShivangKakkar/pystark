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
from pystark.config import ENV
from pystark.plugins.helpers import db
from pyrogram.errors import PeerIdInvalid


@Stark.cmd("ban", owner_only=True)
async def ban_users(bot: Stark, msg):
    if len(msg.command) == 1:
        user_id = None
        if msg.reply_to_message:
            for word in msg.reply_to_message.text.split():
                if word.isdigit() and len(word) == 10:
                    user_id = int(word)
        else:
            await msg.reply("Pass an ID", quote=True)
            return
        if user_id:
            reason = await bot.get_messages(msg.chat.id, msg.reply_to_message.message_id)
            try:
                reason = reason.reply_to_message.link
            except AttributeError:
                reason = None
            await db.set("bans", user_id, {"user_id": user_id, "reason": reason})
            await msg.reply(f"Banned `{user_id}`")
    else:
        user_id = msg.command[1]
        if user_id.isdigit() and len(user_id) == 10:
            user_id = int(user_id)
        else:
            await msg.reply("Wrong ID", quote=True)
            return
        if user_id:
            if user_id in ENV().OWNER_ID:
                await msg.reply(f"Banned `{user_id}`", quote=True)
                await msg.reply(f"Seriously banned.", quote=True)
                await msg.reply(f"I'm not kidding.", quote=True)
                return
            await db.set("bans", user_id, {"user_id": user_id, "reason": None})
            await msg.reply(f"Banned `{user_id}`", quote=True)


@Stark.cmd("unban", owner_only=True)
async def unban_users(_, msg):
    if len(msg.command) == 1:
        await msg.reply("Please pass a user id or username", quote=True)
    else:
        user_id = msg.command[1]
        if user_id.isdigit() and len(user_id) == 10:
            user_id = int(user_id)
        else:
            await msg.reply("Wrong ID", quote=True)
            return
        if user_id:
            if user_id in await db.get_all_data("bans"):
                await db.delete("bans", user_id)
                await msg.reply(f"Unbanned `{user_id}`", quote=True)
            else:
                await msg.reply("Wasn't banned...", quote=True)


@Stark.cmd("banlist", owner_only=True)
async def ban_list(bot: Stark, msg):
    number = 0
    banned = await db.get_all_data("bans")
    if len(banned) == 0:
        text = "No one is banned currently"
    else:
        text = f'**Banned Users [{len(banned)}]**'
        try:
            users = await bot.get_users([i["user_id"] for i in banned])
            for user in users:
                number = number+1
                user_text = f"\n\n{number}) {user.mention} [`{user.id}`]"
                reason = [i["reason"] for i in banned if i["user_id"] == user.id]
                if reason[0]:
                    user_text += f" - Reason - {reason[0]}"
                text += user_text
        except PeerIdInvalid:
            for i in banned:
                number = number+1
                try:
                    user = await bot.get_users(i["user_id"])
                    user_text = f"\n\n{number}) {user.mention} [`{user.id}`]"
                except PeerIdInvalid:
                    user_text = f"\n\n{number}) {i['user_id']}"
                if i["reason"]:
                    user_text += f" - Reason - {i['reason']}"
                text += user_text
    await msg.reply(text, quote=True)
