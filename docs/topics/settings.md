# Project Settings

Your project can be customized using `settings.py` which is available when boilerplate is created.

All available options are:

- [PLUGINS](#plugins)
- [SET_BOT_MENU](#set_bot_menu)
- [CMD_PREFIXES](#cmd_prefixes)
- [ADDONS](#addons)
- [START](#start_option)
- [START_IN_GROUPS](#start_in_groups_option)
- [HELP](#help_option)
- [ABOUT](#about_option)
- [MUST_JOIN](#must_join_option)
- [DATABASE_TABLES](#database_tables)
- [TIMEZONE](#timezone)


## PLUGINS

Path of the directory where plugins are located; in relation to the root directory. 

For example, if name of your directory is `files` and it is in the same folder as `bot.py`, then value of `PLUGINS` should be `files` or `["files"]`.

```python
PLUGINS = "files"
```

You can also specify multiple paths as a python list like:

```python
PLUGINS = ["main_plugins", "other_plugins"]
```

Defaults to `plugins`, i.e, a folder named `plugins` in same directory as `bot.py`

```python
PLUGINS = "plugins"
```

---

## SET_BOT_MENU

Use this setting to enable or disable the bot menu. [Read more](/topics/bot-menu) about bot menu.

Defaults to `True`, i.e, pystark will set the bot menu at runtime.

```python
SET_BOT_MENU = True
```

Disable this behaviour by setting it to false

```python
SET_BOT_MENU = False
```

---

## CMD_PREFIXES

Set the prefixes using which the commands can be called.

Defaults to `/`. Bot will only reply to `/start` but not `!start` or `#start`

```python
CMD_PREFIXES = "/"
```

You can change this to anything you want

```python
CMD_PREFIXES = "!"
```

You can also add multiple prefixes by setting it to a python list

```python
CMD_PREFIXES = ["/", "!", "&"]
```

---

## ADDONS

!!! tip

    Addons are always loaded after your own plugins so you can always overwrite them. 

    For Example, If you load "start" addon and also create a `/start` command yourself, bot will use your own command.


PyStark comes with many ready-to-use plugins which can be directly added using `ADDONS` option.

These are the available options:

### start

Plugin with `/start` command which replies with text in [START](#start) option of `settings.py` in private chats and text in [START_IN_GROUPS](#start_in_groups) option in groups.


### help

Plugin with `/help` command which replies with text in [HELP](#help) option of `settings.py`. 
Only works in private chats.


### about

Plugin with `/about` command which replies with text in [ABOUT](#about) option of `settings.py`.
Only works in private chats.


### id

Plugin with `/id` command which replies with `user_id` in private chats, `chat_id` and `user_id` in groups and channels.


### sudo

Plugin with `/sudo` command which replies with all the sudo commands.


### json

Plugin with `/json` command to get Message JSON of replied message and `/jsondoc` command to get Message JSON as document. 
Only owner can use these commands.


### must_join

Force bot users to join particular chats to use the bot. Put usernames or chat ids where users must join in `MUST_JOIN` variable.

### bans

!!! note

    Needs postgresql database with table `bans`. See [DATABASE_TABLES](#database-tables) option.
    
Plugin with `/botban` command to ban people from using the bot, `/botunban` to unban, `/botbanlist` to list banned users.

### broadcast

!!! note

    Needs postgresql database with table `users`. See [DATABASE_TABLES](#database-tables) option.

Plugin with `/broadcast` command to broadcast a message to users.

### stats

!!! note

    Needs postgresql database with table `users`. See [DATABASE_TABLES](#database-tables) option.

Plugin with `/stats` to get current user stats. 

---

By default, four addons are automatically added:

```python
ADDONS = [
    "start",
    "help",
    "about",
    "id"
]
```

---

<a name="start_option"></a>

## START

To configure the START message, i.e, the message sent at `/start` command. Only needed if `start` addon is enabled. 

Default Value:

```python
START = "Thank you for starting this bot."
```

---

<a name="start_in_groups_option"></a>

## START_IN_GROUPS

To configure the START_IN_GROUPS message, i.e, the message sent at `/start` command in groups. Only needed if `start` addon is enabled. 

If you want to set it same to `START` variable, then:

```python
START = "..."
START_IN_GROUPS = START
```

If you want the bot to not reply, set it to empty string.

```python
START_IN_GROUPS = ""
```

Default Value:

```python
START_IN_GROUPS = "Thank you for starting me in your group. PM for questions!"
```

---

<a name="help_option"></a>

## HELP

To configure the HELP message, i.e, the message sent at `/help` command. Only needed if `help` addon is enabled. 

Default Value:

```python
HELP = """
Available Commands

{commands}
/start - Start the bot
/help - Show this message
/about - About the bot
/id - Get Telegram ID
"""
```

{commands} is automatically replaced with your commands if default is used

---

<a name="about_option"></a>

## ABOUT

To configure the ABOUT message, i.e, the message sent at `/about` command. Only needed if `about` addon is enabled. 

Default Value:

```python
ABOUT = "About This Bot \nDeveloped using @PyStark"
```

---

<a name="must_join_option"></a>

## MUST_JOIN

List of chat ids or usernames where user must join.

For example:

```python
MUST_JOIN = ["StarkBots", -100123456789, "Telegram"]
```

Defaults to empty list, i.e, no chat.

```python
MUST_JOIN = []
```

---

## DATABASE_TABLES

List of pre-made database tables you want to ship from PyStark.

### bans

!!! tip

    [bans](#bans) addon needs a postgres table named `bans` with `user_id` and `reason` attributes. 

    If you are not creating your own, you can use this one.

A sqlalchemy model table `bans` with attributes `user_id` and `reason`. Useful for `ban` addon.


### users

!!! tip

    [broadcast](#broadcast) and [stats](#stats) addon need a postgres table named `users` with `user_id` attribute. 

    If you are not creating your own, you can use this one.

A sqlalchemy model table `users` with attribute `user_id`. Useful for `broadcast` and `stats` addon.

To enable both:

```python
DATABASE_TABLES = ["users", "bans"]
```

Defaults to empty list, i.e, no table.

```python
DATABASE_TABLES = []
```

---

## TIMEZONE

Timezone to use while logging. See full list of available timezones in [GitHub Gist](https://gist.github.com/StarkBotsIndustries/7a6210355f40052a71ba96032d4638df)

For example:

```python
TIMEZONE = "America/New_York"
```

Defaults to India, i.e, `Asia/Kolkata`

```python
TIMEZONE = "Asia/Kolkata"
```
