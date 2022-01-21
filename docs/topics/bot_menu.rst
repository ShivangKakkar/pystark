Bot Menu
========

Telegram has a feature to create a bot menu for your bot. It's usually created using BotFather. It looks like this:


.. raw:: html

    <div align="center">

.. image:: /images/bot_menu.jpg
  :width: 300
  :alt: Bot Menu

.. raw:: html

    </div>

|

But it's exhausting to keep updating it using BotFather. Why not let pystark generate it for you automatically at runtime?

**But How to Do That?**

It's very easy. Just add command description when you create a function. Like this:

.. code-block:: python

    from pystark import Stark


    @Stark.command('stats', description='Get the bot stats')
    def stats():
        "your code"


Or a more simple look:

.. code-block:: python

    from pystark import Stark


    @Stark.cmd('stats', 'Get the bot stats')
    def stats():
        "your code"


Don't want users to see a command in menu? Then don't pass it.

.. code-block:: python

    from pystark import Stark


    @Stark.cmd('stats')  # no description
    def stats():
        "your code"


.. note::

    1. Menu will be automatically updated when you start the bot.
    2. It will be automatically removed when you stop the bot.

-------------------

.. _customize-bot-menu:

**Prevent pystark from updating bot menu**


By default this feature is enabled. But what if you don't want it? You need to pass ``set_menu=False`` to ``activate``  function.

Open ``bot.py``

You will see something like this:

.. code-block:: python

    Stark().activate()

Change it to this:

.. code-block:: python

    Stark().activate(set_menu=False)

