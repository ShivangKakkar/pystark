Creating Plugins
================

Some Python knowledge is required to create plugins in general. Therfore, I highly recommend you to learn Python first.

.. note::

    - All plugins must be added to the **plugins** folder.
    - Plugins must end with .py extension


Here's a sample code for a new plugin

.. code-block:: python

    # Import class 'Stark' in every plugin
    from pystark import Stark, Message

    # use 'Stark.cmd' decorator to create commands
    # @Stark.cmd('name', owner_only=False, extra_filters=None, group=0) - defaults

    @Stark.cmd('sample')  # or @Stark.command('sample')
    async def sample_function(bot: Stark, msg: Message):
        # 'msg.react()' is 'msg.reply()' with del_in added argument
        await msg.react('This will be the reply when /sample is sent.')


But anyway, you can create easier plugins like text plugins with no python knowledge whatsoever.

.. code-block:: python

    from pystark import Stark


    @Stark.cmd('command_name')
    async def text_plugin(bot, msg):
        text = 'your text here'
        await msg.react(text)

For example, below plugin has a command ``/greet`` and the bot will reply with `Welcome to the Bot`

.. code-block:: python

    from pystark import Stark


    @Stark.cmd('greet')
    async def text_plugin(bot, msg):
        text = 'Welcome to the Bot'
        await msg.react(text)
