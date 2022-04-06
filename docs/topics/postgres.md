# Querying Postgres Tables

In this guide, you will learn how to query using postgres tables while using PyStark

!!! tip 
    No need to add `sqlalchemy` or `psycopg2` to `requirement.txt` as they are dependencies of pystark

---

<a name="default-functions"></a>

## Using the in-built functions

PyStark provides some default functions to query postgres tables. These functions allow you to query tables using table name (``__tablename__`` attribute), that is, a string instead of a class. Therefore, you do not need to import classes.

!!! note

    All the in-built functions are asynchronous and use raw sql.

First thing you need to do is creating an instance of `Database` class

!!! tip

    It's a good idea to create this instance in a separate module so that it's easily importable.

```python
from pystark.database.sql import Database

db = Database()
```

Now you can call other functions.

|    Name    |                  Function                  |
|:----------:|:------------------------------------------:|
|  **all**   |            [Get All Rows](#all)            |
|  **get**   |        [Get a Particular Row](#get)        |
| **count**  |        [Get Number of Rows](#count)        |
|  **set**   | [Set/Update value of a key in a Row](#set) |
| **delete** |          [Delete a Row](#delete)           |

<a name="all"></a>

- **Get All Rows**

```python
# Get all rows from "users" table as dicts.
async def get_users():
    all_data = await db.get_all_data("users")  # or await db.all("users")
    print(all_data)
```

<a name="get"></a>

- **Get a Particular Row**

```python
# Get row using primary key from "users" table.
async def get_user():
    user_id = 500123456  # primary key
    get_data = await db.get("users", user_id)
    print(get_data)
```

<a name="count"></a>

- **Get Number of Rows**

```python
# Get number of rows in "users" table.
async def user_count():
    count = await db.count("users")
    print(count)
```

<a name="set"></a>

- **Set/Update value of a key in a Row**

```python
# set/update key, value pairs in "users" table.
async def set_data():
    user_id = 500123456  # primary key
    key_to_change = "aim"
    new_value = "programmer"
    await db.set("users", user_id, key_to_change, new_value)
    print("Set")
```

<a name="delete"></a>

- **Delete a Row**

```python
# Delete a row using primary key from "users" table.
async def delete_user():
    user_id = 500123456
    delete_data = await db.delete("users", user_id)
    print("Deleted")
```

---

<a name="session-object"></a>

## Using the Regular Way (Session object)

You can query tables using the ``session`` object which is the regular way in sqlalchemy.
Session objects is available as an attribute to `Database` class of `pystark.database.sql`

```python
# import 'Session' object
from pystark.database.sql import Database
# import Python class for respective table
# let's say it is in 'users_sql.py' inside 'database' folder.
from database.users_sql import Users


db = Database()


# This function gives total 'rows', that is total user ids in 'users' table.
def num_users():
    users = db.session.query(Users).count()
    # close session after all queries are made.
    db.session.close()
    return users


# This function returns 'name' and 'aim' for users by using 'user_id'
def get_name_and_aim(user_id):
    query = db.session.query(Users).get(user_id)
    name = query.name  # get name
    aim = query.aim  # get aim
    db.session.close()
    return (name, aim)


# This function sets name and aim for users by using 'user_id'
def set_name_and_aim(user_id, name, aim):
    query = db.session.query(Users).get(user_id)
    query.name = name  # set name
    query.aim = aim  # set aim
    db.session.commit()  # use this after setting anything.
    # Now you don't need to 'db.session.close()' as you used 'db.session.commit()' already.

# Etc
```
