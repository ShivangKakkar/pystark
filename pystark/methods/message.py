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

import os
import asyncio
from typing import Optional, Union
from pystark.helpers.patch import patch
from pyrogram.types import Message, User
from pyrogram.errors import MessageTooLong
from pystark.helpers.localization import l10n


@patch(Message)
class Message:
    """Message class instances represents messages. This class adds some additional methods to existing pyrogram methods of Message"""

    async def react(self, text: str, del_in: int = 0, **kwargs) -> "Message":
        """React/Reply to a message. Similar to pyrogram's `msg.reply` but takes care of:

        - Long messages - Sends long messages which raise `MESSAGE_TOO_LONG` as documents automatically.
        - Localization - For example, if your `en.yml` file has a HAS_BEEN` key then `message.react("HAS_BEEN")` will be replaced by it.
        - `del_in` argument - Extra argument to delete a message after n seconds asynchronously. If n is 0, message is not deleted at all.
        """
        text = str(text)
        lang = await l10n()
        if lang and text in lang:
            text = lang[text]
        try:
            reply = await self.reply(text, quote=True, disable_web_page_preview=True, **kwargs)
        except MessageTooLong:
            reply = await self.reply("Sending as document...", quote=True)
            file = f'{reply.message_id}.txt'
            with open(file, 'w+', encoding="utf-8") as f:
                f.write(text)
            await reply.delete()
            reply = await self.reply_document(file, caption="Output")
            os.remove(file)
        if del_in:
            await asyncio.sleep(del_in)
            await reply.delete()
        return reply

    @property
    def args(self, split: str = " ") -> list[str]:
        """List arguments passed in a message. Removes first word (the command itself)

        Parameters:

            split (str, optional): Define how to split the arguments, defaults to whitespace.

        Example:

            If text is `/start reply user`, return value would be `["reply", "user"]`
        """
        args = self.text.split(split)
        args.pop(0)
        return args

    @property
    def input(self) -> str:
        """Input passed in a message. Removes first word (the command itself)

        Example:

            If text is `/start reply user`, return value would be `reply user`
        """
        return self.text.split(" ", 1)[1]

    @property
    def ref(self) -> Union[int, str, None]:
        """Returns the referred user's id or username. To get the full user, use method `get_ref_user`

        Useful to get the referent user's id or username for a command.
        If command was replied to a message, the replied message's user id is returned.
        Otherwise, the first argument of command is returned (which isn't guaranteed to be an actual user or an id).

        **Example**:

            If command `/ban` was replied to a user's message, user id (`message.reply_to_message.from_user.id`) is returned.

            If command `/ban 12345678` was sent, user id (integer) `12345678` is returned.

            If command `/ban StarkProgrammer` was sent, username (string) `StarkProgrammer` is returned.

            If command `/ban 87654321 12345678` was sent, user id (integer) `87654321` is returned but `12345678` is ignored because it's not the first argument.

            If command `/ban` was sent with no arguments and was also not a reply to any message, None is returned.

            If command `/ban ok` was sent, "ok" is returned which isn't an actual user but will not raise exception.
        """
        if self.reply_to_message:
            return self.reply_to_message.from_user.id
        args = self.args
        if not args:
            return
        return args[0] if not args[0].isdigit() else int(args[0])

    async def get_ref_user(self) -> Optional[User]:
        """Returns the full referred user. To get only user id or username, use property `ref` as it's faster.

        Useful to get the referent of a command.
        If command was replied to a message, the replied message's user is returned.
        Otherwise, the first argument of command is used to get the user.

        !!! note

            If command is not replied then first argument of command is considered user id or username. It's on you to handle PeerIdInvalid and UsernameInvalid

        **Example**:

            If command `/ban` was replied to a user's message, user (`message.reply_to_message.from_user`) is returned.

            If command `/ban 12345678` was sent, the user instance of user with id `12345678` is returned.

            If command `/ban StarkProgrammer` was sent, the user instance of user with username `StarkProgrammer` is returned.

            If command `/ban 87654321 12345678` was sent, the user instance of user with id `87654321` is returned but `12345678` is ignored because it's not the first argument.

            If command `/ban` was sent with no arguments and was also not a reply to any message, None is returned.
        """
        if self.reply_to_message:
            return self.reply_to_message.from_user
        args = self.args
        if not args:
            return
        user = args[0] if not args[0].isdigit() else int(args[0])
        user = await self._client.get_users(user)
        return user
