# Import class 'Stark' in every plugin
from pystark import Stark, Message


# use 'Stark.cmd' decorator to create commands
# @Stark.cmd('name', owner_only=False, extra_filters=None, group=0) - defaults

@Stark.cmd('sample')  # or @Stark.command('sample')
async def sample_function(bot: Stark, msg: Message):
    # 'msg.react()' is 'msg.reply()' with del_in added argument
    await msg.react('This will be the reply when /sample is sent.')
