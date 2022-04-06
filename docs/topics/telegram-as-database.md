# Using Telegram as a Database

You can use Telegram as a Database, thanks to [TelegramDB](https://pypi.org/project/TelegramDB/).

!!! note

    This feature is still in beta and this is just a pre-release.

---

## Needed Variables

- ``DB_SESSION`` - String Session for a Telegram account.

- ``DB_CHAT_ID`` - Create a new telegram channel for database. Set Telegram ID for that channel as this.

---

## What is a DataPack?

Like there are Tables in SQL, TelegramDB has DataPacks. It is just a fancy term to scare you.

---

## Create a DataPack

```python
from pystark import Stark
from pystark.database.telegram_db import DataPack, Member, Session


# Create a DataPack like you create a Table in Postgres (SQLAlchemy).
class TestData(DataPack):
    __datapack_name__ = "test"

    id = Member(int, is_primary=True)
    name = Member(str)
    aim = Member(str)

    def __init__(self, id, name=None, aim=None):
        self.id = id
        self.name = name
        self.aim = aim


Session.prepare_datapack(TestData)
```

---

## Query a DataPack

```python
# Import Session object from pystark
from pystark.database.telegram_db import Session
# "test_data.py" is a file in "database" folder, where class TestData is located.

from database.test_data import TestData


# Commit to DataPack.
test = TestData(1, name="Stark", aim="Create Time Machine")
Session.commit(test)


# Get info from DataPack.
user = TestData(1)  # pass primary key.
if Session.get(user):
    print("User exists!")
    print("ID: ", user.id)
    print("Name: ", user.name)
    print("Aim: ", user.aim)
else:
    print("No user with ID: 1")
```

---

## Load DataPacks and Enable Telegram DB

After adding variables specified above, you need to [create datapack(s) using Python Classes](#create-a-datapack). For a datapack to be loaded, you need to import it in some plugin. Also, you obviously you need to import it to use it anyway.

Example:

```python
# Let's say I've a file named `a.py` with class `DataPack1`.
# This file is located in a folder named `dbs` in same directory as 'bot.py'.
from dbs.a import DataPack1
```

This will enable the database and load ``DataPack1`` named datapack.
