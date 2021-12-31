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


from ..client import Stark
from ..config import check_environment, OWNER_ID
from pyrogram.errors import PeerIdInvalid

module = check_environment()


@Stark.cmd('start')
async def start_func(bot: Stark, msg):
    try:
        await msg.react(await replace(module.START, msg, bot))
    except AttributeError:
        pass


@Stark.cmd('help')
async def help_func(bot, msg):
    try:
        await msg.react(await replace(module.HELP, msg, bot))
    except AttributeError:
        pass


@Stark.cmd('about')
async def about_func(bot, msg):
    try:
        await msg.react(await replace(module.ABOUT, msg, bot))
    except AttributeError:
        pass


@Stark.cmd('id')
async def id_func(_, msg):
    if msg.chat.type == 'private':
        await msg.react("Your ID is `{}`".format(msg.from_user.id))
    else:
        if msg.reply_to_message:
            await msg.react("{}'s ID is `{}`".format(msg.reply_to_message.from_user.first_name, msg.reply_to_message.from_user.id))
        else:
            await msg.react("Chat ID is `{}` \n\nYour ID is `{}`".format(msg.chat.id, msg.from_user.id))


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
        try:
            owner = (await bot.get_users(int(OWNER_ID))).mention
        except PeerIdInvalid:
            owner = '@StarkBots'
        m = m.replace("{owner}", owner)
    return m
