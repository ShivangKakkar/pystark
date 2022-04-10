# Customization

There are a lot of customization options in PyStark to customize the behavior of your bot. All customization options can be configured using `settings.py` which is generated along with boilerplate. This is the same thing we read in the last page but with some highlights.

!!! tip 

    Don't skip [this section](#change-the-default-messages) as it's special.

---

## Change the default messages

PyStark comes with in-built plugins like `start` and `help`. But what if you want to have different messages than the in-built ones? They are easily customizable.

You can change their values in `settings.py`. Change `START` value for `/start` command in private chats, `START_IN_GROUPS` value for `/start` command in groups, `HELP` for `/help` and `ABOUT` for `/about`.

### **Special Keywords**

You may want to mention user or bot in `start` or `help` messages. You can use special keywords to do that. They will be replaced at runtime.

- `{user}` - User's first name
- `{bot}` - Bot's name
- `{user_mention}` - User mention as a hyperlink
- `{bot_mention}` - Bot mention as a hyperlink
- `{owner}` - Owner mention (only works if `OWNER_ID` is set, otherwise `@pystark` is used)
- `{commands}` - Only for [HELP](/topics/settings#help-option) message. It is replaced with all the commands and their descriptions for an easy help message.

So let's say your `start` message is set to `Hi {user}` and your first name on telegram is `Stark` then bot will send `Hi Stark`.

---

## Remove the default plugins

PyStark comes with many in-built plugins, also called addons. By default, four of them are enabled which are `start`, `help`, `about` and `id`
To remove them you need to configure `ADDONS` options of `settings.py`.

To remove all addons, do this:

```python
ADDONS = []
```

You can also choose specific addons to configure. For example, you can enable only `start` and `help` like this:

```python
ADDONS = [
    "start",
    "help",
]
```

---

## Rename the plugins directory

You may notice that if you rename the `plugins` directory, the plugins won't load. To fix this you need to put the name of your `plugins` directory to `PLUGINS` option of `settings.py`

```python
PLUGINS = "name of plugins folder"
```

Let's say you renamed the ``plugins`` folder to ``files``. Then you should do this:

```python
PLUGINS = "files"
```

---

## Disable Bot Menu Updating

- [Please refer here](/topics/bot-menu#customize-bot-menu)
