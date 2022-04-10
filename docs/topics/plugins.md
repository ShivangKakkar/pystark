# Creating Plugins

Some Python knowledge is required to create plugins in general. Therefore, I highly recommend you to learn Python first. [Please see this FAQ](/meta/faqs#learn-python)

!!! note

    - All plugins must be added to the **plugins** folder.
    - Plugins must end with .py extension


Here's a sample code for a new plugin

```python
# Import class 'Stark' in every plugin
from pystark import Stark, Message

# use 'Stark.cmd' decorator to create commands
# @Stark.cmd('name', description="...", owner_only=False, extra_filters=None, group=0, private=False) - defaults

@Stark.cmd('sample', "Sample command for bot")  # or @Stark.command('sample', description="Sample command for bot")
async def sample_function(bot: Stark, msg: Message):
    # 'msg.react()' is 'msg.reply()' with del_in added argument
    await msg.react('This will be the reply when /sample is sent.')
```

But anyway, you can create easier plugins like text plugins with no python knowledge whatsoever.

```python
from pystark import Stark


@Stark.cmd('command_name', description='command description')
async def text_plugin(bot, msg):
    text = 'your text here'
    await msg.react(text)
```

For example, below plugin has a command ``/greet`` and the bot will reply with `Welcome to the Bot`

```python
from pystark import Stark


@Stark.cmd('greet', "Greet the user")
async def text_plugin(bot, msg):
    text = 'Welcome to the Bot'
    await msg.react(text)
```
