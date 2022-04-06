# Bot Menu

Telegram has a feature to create a bot menu for your bot. It's usually created using BotFather. It looks like this:

<div align="center">
<img src="/images/bot_menu.jpg" width="300" alt="Bot Menu"/>
</div>


But it's exhausting to keep updating it using BotFather. Why not let pystark generate it for you automatically at runtime?

**But How to Do That?**

It's very easy. Just add command description when you create a function. Like this:

```python
from pystark import Stark


@Stark.command('stats', description='Get the bot stats')
def stats():
    # your code
```


Or a more simple look:

```python
from pystark import Stark


@Stark.cmd('stats', 'Get the bot stats')
def stats():
    # your code
```


Don't want users to see a command in menu? Then don't pass it.

```python
from pystark import Stark


@Stark.cmd('stats')  # no description
def stats():
    # your code
```


!!! note

    1. Menu will be automatically updated when you start the bot.
    2. It will be automatically removed when you stop the bot.

---

<a name="customize-bot-menu"></a>

**Prevent pystark from updating bot menu**


By default, this feature is enabled. But what if you don't want it? You need to configure `SET_BOT_MENU` option of `settings.py`

You will see something like this:

```python
SET_BOT_MENU = True
```

Change it to this:

```python
SET_BOT_MENU = False
```
