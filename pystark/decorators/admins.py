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


aliases = {
    'edit': 'can_be_edited',
    'manage': 'can_manage_chat',
    'delete': 'can_delete_messages',
    'restrict': 'can_restrict_members',
    'promote': 'can_promote_members',
    'change': 'can_change_info',
    'invite': 'can_invite_users',
    'pin': 'can_pin_messages',
    'vc': 'can_manage_voice_chats',
}


class Admins:
    @staticmethod
    def admins(alias: str = ""):
        """This decorator is used to allow only admins to use a particular command.

        Parameters:

            alias (str, optional): Permission to check for the user. Can be `edit`/`can_be_edited` or `manage`/`can_manage_chat` or
                `delete`/`can_delete_messages` or `restrict`/`can_restrict_members` or `promote`/`can_promote_members` or `change`/`can_change_info`
                `invite`/`can_invite_users` or `pin`/`can_pin_messages` or `vc`/`can_manage_voice_chats`

        Examples:

            ```python
            from pystark import Stark


            # Bot will only execute function, if user who sent `/del` command has admin right `can_delete_messages`.
            @Stark.admins('delete')  # or @Stark.admins('can_delete_messages')
            @Stark.cmd("del")
            async def delete_message(bot, msg):
                await msg.reply_to_message.delete()


            # Bot will only execute function, if user who sent `/kick` command has admin right `can_restrict_members`.
            @Stark.admins('restrict')  # or @Stark.admins('can_restrict_members')
            @Stark.cmd("kick")
            async def kick_user(bot, msg):
                ...


            # Bot will only execute function, if user who sent `/play` command has admin right `can_manage_voice_chats`.
            @Stark.admins('vc')  # or @Stark.admins('can_manage_voice_chats')
            @Stark.cmd("play")
            async def play_song(bot, msg):
                ...
            ```
        """

        def first_decorator(func):
            if alias and alias in aliases:
                perm = aliases[alias]
            elif alias in list(aliases.values()):
                perm = alias
            else:
                perm = None

                # if not am_admin:
                #     await msg.react("I am not an admin here. That's so sad. Why am I even here?")
                # elif not info2[perm]:
                #     await msg.react(f"I am missing permission: {perm}")
                # elif not is_admin:
                #     await msg.react('You are not an admin here')
                # elif not info[perm]:
                #     await msg.react(f"You are missing permission: '{perm}'")

            async def wrapper(*args, **kwargs):
                bot = args[0]
                msg = args[1]
                bot_id = (await bot.get_me()).id
                bot_status = (await msg.chat.get_member(bot_id))
                if bot_status.status != 'administrator':
                    await msg.react("I_AM_NOT_ADMIN")
                    return
                if perm and not bot_status[perm]:
                    await msg.react("I_DONT_HAVE_RIGHT".format(perm))
                    return
                user_status = await msg.chat.get_member(msg.from_user.id)
                if user_status.status not in ['creator', 'administrator']:
                    await msg.react("USER_NOT_ADMIN")
                    return
                if perm and not user_status[perm]:
                    await msg.react("USER_DOESNT_HAVE_RIGHT".format(perm))
                    return
                if msg.reply_to_message:
                    user_id = msg.reply_to_message.from_user.id
                else:
                    args = msg.args
                    if not args:
                        await msg.react("NO_ID_PASSED")
                        return
                    user_id = args[0]
                    try:
                        user_id = (await bot.get_users(user_id)).id
                    except IndexError:
                        await msg.react("USER_NOT_FOUND")
                        return
                a_list = await bot.get_chat_members(msg.chat.id, filter="administrators")
                admin_user_ids = [a.user.id for a in a_list]
                if user_id in admin_user_ids:
                    if user_id == bot_id:
                        await msg.react("BAN_MYSELF")
                    else:
                        await msg.react("ACT_ON_ADMINS")
                    return
                await func(*args, **kwargs)

            return wrapper

        return first_decorator
