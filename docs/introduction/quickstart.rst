Quick Start
============

Following these steps will allow you to see **PyStark** in action as quickly as possible.

.. note::
    Installation of Python with version 3.6 or above is required.

--------

Steps
-----

1. :ref:`Open up your terminal <open-terminal>`.

.. |a| raw:: html

    <a />

2. Install PyStark with pip:

.. code-block:: console

    $ pip3 install pystark

3. Generate a boilerplate using PyStark's command-line tool.

.. code-block:: console

    $ pystark --boilerplate

4. :ref:`Open the file manager in current directory. <open-file-manager>`

.. |b| raw:: html

    <b />

5. Edit the ``.env`` file and fill your :guilabel:`API_ID`, :guilabel:`API_HASH` and :guilabel:`BOT_TOKEN`. Get the API keys from `<my.telegram.org>`_ and bot token from `BotFather <https://telegram.me/BotFather>`_

.. |c| raw:: html

    <c />

6. Change the default values of messages in ``data.py``.

.. |d| raw:: html

    <d />

7. Run the bot using python:

.. code-block:: console

    $ python3 bot.py


--------

What does this do?
------------------

The above steps will help you set up your bot and run it. You can use the command **/start** to check if your bot is actually running.

Your bot now has four default commands:

.. hlist::
    :columns: 1

    - ``/start`` - Start the bot.
    - ``/help`` - See a help message for the bot.
    - ``/about`` - About the bot.
    - ``/id`` - Get Telegram ID (also works in groups)


You can change the messages for all commands in ``data.py`` file.

