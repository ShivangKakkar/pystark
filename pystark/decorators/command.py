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
from ..config import ENV
from pyrogram.methods.decorators.on_message import OnMessage


command_data = {"commands": 0, "commands_list": [], "command_descriptions": {}}


class Command(OnMessage):
    @staticmethod
    def command(
        cmd: str = None,
        description: str = None,
        group: int = 0,
        owner_only: bool = False,
        private_only: bool = False,
        group_only: bool = False,
        channel_only: bool = False,
        extra_filters=None
    ):
        """This decorator is used to handle messages. Mainly used to create commands. All arguments are  optional.
        You can also use the alias ``Stark.cmd`` instead of ``Stark.command``.

        `Parameters`:
            cmd (`str`, optional) -
                Command that triggers your function. Defaults to None, if you only want to use extra_filters argument.

            description (`str`,  optional) -
                Command description to create Bot Menu. Defaults to None. :doc:`Read More </topics/bot-menu>`

            group (`int`, optional) -
                Define a group for this handler. Defaults to 0. `Read More <https://docs.pyrogram.org/topics/more-on-updates#handler-groups>`_

            owner_only (`bool`, optional) -
                Allow only owner to use this command. Defaults to False.

            private_only (`bool`, optional) -
                Only handle messages for private chats. Bot will ignore messages in groups and channels. Defaults to False.

            group_only (`bool`, optional) -
                Only handle messages for groups. Bot will ignore messages in private chats and channels. Defaults to False.

            channel_only (`bool`, optional) -
                Only handle messages for channels. Bot will ignore messages in private chats and groups. Defaults to False.

            extra_filters (optional) -
                Extra filters to apply in your function. Import ``filters`` from pyrogram or pystark to use this. See example below.

        **Examples**

        .. code-block:: python

            from pystark import Stark

            # The normal way. Bot will reply to command ``/greet`` sent anywhere and by anyone.
            @Stark.command('greet', description='Greet the user')

            # or
            @Stark.cmd('greet', 'Greet the user')

            # Bot will reply only to owner, that is, the user whose id is set as OWNER_ID in environment variables.
            # Others will be ignored.
            @Stark.command('greet', owner_only=True)

            # Bot will reply only if message is sent in private chat (aka pm).
            # Messages in groups and channels will be ignored.
            @Stark.command('greet', private_only=True)

            # Bot will reply only if message is sent in groups.
            # Messages in groups and private chats will be ignored.
            @Stark.command('greet', group_only=True)

            # Bot will reply only if message is sent in channels.
            # Messages in private chats and groups will be ignored.
            @Stark.command('greet', channel_only=True)


            # Filter all messages.

            # Use positive integer to execute after executing another function in default group that also filtered this message.
            @Stark.command(group=1)

            # or Use negative integer to execute before executing another function in default group that also filtered this message.
            @Stark.command(group=-1)

            # Don't use this as other functions won't work.
            @Stark.command()


            # Filter other type of messages using extra_filters.

            # Import filters from pyrogram or pystark.
            from pystark import filters

            # Filter only media messages.
            @Stark.command(extra_filters=filters.media)

            # Filter only text messages.
            @Stark.command(extra_filters=filters.text)

            # Filter only messages sent by 'StarkProgrammer'.
            @Stark.command(extra_filters=filters.user('StarkProgrammer'))

            # Filter only messages sent in 'StarkBotsChat'
            @Stark.command(extra_filters=filters.chat('StarkBotsChat'))

            # Filter only messages with the word 'baby'.
            @Stark.command(extra_filters=filters.regex('baby'))

            # Filter all media messages sent by bots.
            @Stark.command(extra_filters=filters.bot & filters.media)

            # Filter all messages sent by bots except media messages.
            @Stark.command(extra_filters=filters.bot & ~filters.media)

            # Filter either media messages or text messages.
            @Stark.command(extra_filters=filters.text | filters.media)
        """
        if not cmd and not extra_filters:
            filters_ = None
        elif cmd and extra_filters:
            command_data["commands"] += 1
            command_data["commands_list"].append(cmd)
            filters_ = f.command(cmd, prefixes=ENV.CMD_PREFIXES) & extra_filters
        elif extra_filters:
            filters_ = extra_filters
        else:
            command_data["commands"] += 1
            command_data["commands_list"].append(cmd)
            filters_ = f.command(cmd, prefixes=ENV.CMD_PREFIXES)
        if cmd and description:
            command_data["command_descriptions"][cmd] = description
        if owner_only:
            filters_ = filters_ & f.user(ENV().OWNER_ID)
        if private_only:
            filters_ = filters_ & f.private
        if group_only:
            filters_ = filters_ & f.group
        if channel_only:
            filters_ = filters_ & f.channel
        decorator = OnMessage.on_message(filters_, group)
        return decorator

    cmd = command
