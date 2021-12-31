from pystark import Stark, Message


@Stark.cmd('')
async def cmd_func(bot: Stark, msg: Message):
    await msg.react('Duh2')
