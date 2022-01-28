from pystark import Stark, Message


@Stark.cmd('')
async def cmd_func(_, msg: Message):
    await msg.react('Duh2')
