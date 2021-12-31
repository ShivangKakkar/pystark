from pystark import Stark, Message, filters


@Stark.cmd(extra_filters=filters.text)
async def main_func(bot: Stark, msg: Message):
    await msg.react('Duh')
