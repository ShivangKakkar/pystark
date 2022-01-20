# PyStark

> A star ⭐ from you means a lot

An incomplete add-on extension to [Pyrogram](https://pypi.org/project/Pyrogram), to create telegram bots a bit more easily.


## Documentation

Read the Documentation : https://pystark.codes

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


## Credits

- [Dan](https://github.com/delivrance) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library on top of which **pystark** works.

## Community and Support

Telegram Channel - **[StarkBots](https://t.me/StarkBots)**

Telegram Chat - **[StarkBotsChat](https://t.me/StarkBotsChat)**

## Copyright and License

- Copyright (C) 2021-2022 **Stark Bots** <<https://github.com/StarkBotsIndustries>>

- Licensed under the terms of [GNU General Public License v3 or later (GPLv3+)](https://github.com/StarkBotsIndustries/PyStark/blob/master/LICENSE)
