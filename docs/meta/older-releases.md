# Older Releases

!!! note

    These are the changelog for older versions. Latest Version is 1.0.0

    Please see the [changelog for latest versions](/meta/changelog)

---

### v0.2.11 <small>- January 22, 2022</small>

- Use TinyDB for your project. [Read More About It](/topics/tinydb).


### v0.2.10 <small>- January 22, 2022</small>

- Use Telegram as a Database. [Read More About It](/topics/telegram-as-database).


### v0.2.9 <small>- January 21, 2022</small>

- Fix Bugs of v0.2.8

### v0.2.8 <small>- January 21, 2022</small>

- Renamed argument ``private`` to ``private_only`` in command decorator.
- Added two new arguments ``group_only`` and ``channel_only`` in command decorator.
- Added docs for command decorator. [See Here](/decorators/command)

### v0.2.7 <small>- January 21, 2022</small>

- Auto Update Bot Menu at runtime. [Read More](/topics/bot-menu)
- Added description argument in ``command`` decorator(for bot menu).
- ``Stark.data()`` now also returns a dictionary of command descriptions (key=command, value=description). See [Stark.data][pystark.client.Stark.data]
- ``Stark.activate`` now takes an optional argument ``set_menu`` to disable (or enable) auto-update of bot menu. [Read More](/topics/bot-menu#customize-bot-menu)
- Added docs for Bot Menu. [Read Here](/topics/bot-menu)

### v0.2.6 <small>- January 20, 2022</small>

- Added two new static methods to ``Stark`` class - [Stark.list_args][pystark.client.Stark.list_args] and [Stark.data()][pystark.client.Stark.data]
- Improved ``Stark.log()`` function. Now pass int values for levels. See [Stark.log][pystark.client.Stark.log]
- Added docs for class ``Stark`` - [Read Here](/topics/class-stark)


### v0.2.5 <small>- January 20, 2022</small>

- Added in-built functions to query postgres tables - [Read More](/topics/postgres#default-functions)
- Added ChangeLog to docs (this webpage)
- Improve documentation using sphinx-toolbox


### v0.2.4 <small>- January 17, 2022</small>

- This Documentation was created
