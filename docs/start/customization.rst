Customization
=========================

There are a lot of customization options in PyStark to customize the behavior of your bot.

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

--------

Change the default messages
---------------------------

PyStark comes with in-built plugins like ``start`` and ``help``. But what if you want to have different messages than the in-built ones? They are easily customizable.

After you have finished generating a boilerplate, you will see a file named ``data.py``. You can change it's values to change the default messages.

**Special Keywords** - You may want to mention user or bot in ``start`` or ``help`` messages. You can use special keywords to do that. They will be replaced at runtime and will be different for all users.

- ``{user}`` - User's first name
- ``{bot}`` - Bot's name
- ``{user_mentions}`` - User mention as a hyperlink
- ``{bot_mentions}`` - Bot mention as a hyperlink
- ``{owner}`` - Owner mention (only works if ``OWNER_ID`` is set else ``@StarkBots``)

So let's say your ``start`` message is set to `Hi {user}` and your first name on telegram is `Stark` then bot will send `Hi Stark`.

--------

Remove the default plugins
--------------------------

PyStark comes with four in-built plugins. To remove this you need to edit ``bot.py``. Use ``default_plugins=False`` while calling the ``activate`` function.

You will see this:

.. code-block:: python

    Stark().activate()

Change that to this:

.. code-block:: python

    Stark().activate(default_plugins=False)

--------

Rename the plugins directory
----------------------------

You may notice that if you rename the plugins directory, the plugins won't load. To fix this you need to pass the name of your plugins directory to the ``activate`` function. Open ``bot.py``.

You will see this:

.. code-block:: python

    Stark().activate()

Change that to this:

.. code-block::

    Stark().activate(plugins="name of plugins folder")

Let's say I renamed the ``plugins`` folder to ``files``. Then I should do this:

.. code-block:: python

    Stark().activate(plugins="files")


------------------

Disable Bot Menu Updating
-------------------------

- :ref:`Please refer here <customize-bot-menu>`
