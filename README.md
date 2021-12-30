# PyStark

> A star ⭐ from you means a lot

An incomplete add-on extension to [Pyrogram](https://pypi.org/project/Pyrogram), to create telegram bots a bit more easily.

**Intended for personal use**

I do **NOT** 'especially' recommend you to use it.

## Installation (using pip)

**[Available on PyPI](https://pypi.org/project/PyStark/)**

```bash
pip3 install pystark
```

## What's the main purpose?

There are some things that are common in every bot. This makes it a bit simple to generate a boilerplate and ease overall creation.

1. **Default Plugins** - Any bot created using `pystark` will automatically have some commands like */start*, */help*, */about* and */id*. 

   Of course that can be turned off using *default_plugins=False* in the main function.


2. **Databases** - Both `postgres` and `redis` are ready to use once the environment variables are present. 
 
    To know more about **postgres** and **redis** usage in pystark - [Click Here](https://github.com/StarkBotsIndustries/PyStark/tree/master/pystark/database#databases)


3. **Boilerplate** - You can generate a boilerplate with all the files you will need using our command line utility. Optionally, you can generate it with Heroku Support (app.json, Procfile, etc). Please scroll down below to `Usage` section to know how.


4. **Easier** - There are multiple things that make it easier. 
   
- Start the bot using 2-lines of code.

```python
from pystark import Stark

Stark().activate()
```
- Easier to use methods and decorators

## Usage

- ### Creating Boilerplate Code

You can generate a boilerplate to set up the common files you need. You can also choose to have added heroku support which will create `app.json`, `Procfile`, etc.
This can be done using the **command-line utility**.

Run below command

```bash
pystark
```


`cd` into the directory where you want to create the **boilerplate** folder. Then run below command.

```bash
pystark --boilerplate
```

To create boilerplate with **Heroku Support**

```bash
pystark --boilerplate-heroku
```

Boilerplate folder will be created with a **plugins** directory and some other necessary files

- ### Making Basic Changes to the folder

1. **Filling variables** - Fill the mandatory values in `.env` file. (Step only if non-heroku boilerplate is created)
2. **Changing Text for Messages** - Go to 'data.py' and change string values as it suits you.

- ### Create your own plugins

You can create plugins and add it in **plugins** folder, and it'll be automatically loaded while starting the bot. Of course, you need Python knowledge to create awesome plugins.

```python
# Import class 'Stark' in top of every plugin
from pystark import Stark, Message


# use 'Stark.cmd' decorator to create commands
# @Stark.cmd('name', owner_only=False, extra_filters=None, group=0) - defaults

@Stark.cmd('sample')  # or @Stark.command('sample')
async def sample_function(bot: Stark, msg: Message):
    # 'msg.react()' is 'msg.reply()' with del_in added argument
    await msg.react('This will be the reply when /sample is sent to the bot.')
```

- ### Run the bot

**Heroku** - Create a repository and tap on Deploy Heroku Button. Fill the values, click deploy and wait for 2 minutes and done.

**Local Deploy** - Make sure you filled variables in `.env` as told above. Run the `bot.py` file using command `python3 bot.py` and there you go.

## Credits and Library

- [Dan](https://github.com/delivrance) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library on top of which **pystark** works.

## Community and Support

Telegram Channel - **[StarkBots](https://t.me/StarkBots)**

Telegram Chat - **[StarkBotsChat](https://t.me/StarkBotsChat)**


## Copyright and License

- Copyright (C) 2021-2022 **Stark Bots** <<https://github.com/StarkBotsIndustries>>

- Licensed under the terms of [GNU General Public License v3 or later (GPLv3+)](https://github.com/StarkBotsIndustries/PyStark/blob/master/LICENSE)
