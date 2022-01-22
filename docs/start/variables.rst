Mandatory Variables
===================

.. note::

    Never disclose these keys to anyone!

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

--------

API Keys
--------

API Keys are one of the most important needed keys to work with any MTProto Framework. They include a ``API_ID`` and ``API_HASH``.

You can get these from `my.telegram.org <https://my.telegram.org>`_


--------

Bot Token
---------

Bot Token is a specific token for every telegram bot. You will get it when you create a new bot using `BotFather <https://t.me/BotFather>`_

It should be filled as ``BOT_TOKEN``

--------

Filling the Variables
---------------------

- **For Local Deploy** - fill them in ``.env`` file.

- **For Heroku Deploy** - fill them after you tap on ``Deploy to Heroku`` button on your repository.

--------

Non-mandatory Variables
-----------------------

- ``CMD_PREFIXES`` - prefixes for commands (defaults to "/"). For multiple prefixes, specify multiple together like "/.*"
- ``OWNER_ID`` - Your Telegram ID
- ``TIMEZONE`` - "Asia/Kolkata"
- ``DATABASE_URL`` - for PostgreSQL database
- ``REDIS_URL`` - for Redis database (public endpoint)
- ``REDIS_PASSWORD`` - for Redis database
- ``DB_SESSION`` - for using Telegram as a database.
- ``DB_CHAT_ID``- for using Telegram as a database (ID of a new channel).
