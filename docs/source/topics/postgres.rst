Querying Postgres Tables
========================

In this guide, you will learn how to query using postgres tables while using PyStark

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

--------

.. _default-functions:

Using the in-built functions
----------------------------

PyStark provides some default functions to query postgres tables. These functions allow you to query tables using table name (``__tablename__`` attribute), that is, a string instead of a class. Therefore, you do not need to import classes.

.. note::

    All the in-built functions are asynchronous.

.. list-table:: In-built Functions
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Function
   * - **all_db**
     - :ref:`Get All Rows <all_db>`
   * - **get_db**
     - :ref:`Get a Particular Row <get_db>`
   * - **count_db**
     - :ref:`Get Number of Rows <count_db>`
   * - **set_db**
     - :ref:`Set/Update value of a key in a Row <set_db>`
   * - **delete_db**
     - :ref:`Delete a Row <delete_db>`

.. _all_db:

- **Get All Rows**

.. code-block:: python

    from pystark.database.postgres import all_db


    # Get all rows from "users" table as dicts.
    async def get_users():
        all_data = await all_db("users")
        print(all_data)

.. _get_db:

- **Get a Particular Row**

.. code-block:: python

    from pystark.database.postgres import get_db


    # Get row using primary key from "users" table.
    async def get_user():
        user_id = 500123456  # primary key
        get_data = await get_db("users", user_id)
        print(get_data)

.. _count_db:

- **Get Number of Rows**

.. code-block:: python

    from pystark.database.postgres import count_db


    # Get number of rows in "users" table.
    async def user_count():
        count = await count_db("users")
        print(count)


.. _set_db:

- **Set/Update value of a key in a Row**

.. code-block:: python

    from pystark.database.postgres import set_db


    # set/update key, value pairs in "users" table.
    async def set_data():
        user_id = 500123456  # primary key
        key_to_change = "aim"
        new_value = "programmer"
        set_data = await set_db("users", user_id, key_to_change, new_value)
        print("Set")

.. _delete_db:

- **Delete a Row**

.. code-block:: python

    from pystark.database.postgres import delete_db


    # Delete a row using primary key from "users" table.
    async def delete_user():
        user_id = 500123456
        delete_data = await delete_db("users", user_id)
        print("Deleted")

--------

.. _session-object:

Using the Regular Way (Session object)
--------------------------------------

You can query tables using the ``Session`` object which is the regular way in sqlalchemy.


.. code-block:: python

    # import 'Session' object
    from pystark.database.postgres import Session
    # import Python class for respective table
    # let's say it is in 'users_sql.py' inside 'database' folder.
    from database.users_sql import Users


    # This function gives total 'rows', that is total user ids in 'users' table.
    def num_users():
        users = Session.query(Users).count()
        # close session after all queries are made.
        Session.close()
        return users


    # This function returns 'name' and 'aim' for users by using 'user_id'
    def get_name_and_aim(user_id):
        query = Session.query(Users).get(user_id)
        name = query.name  # get name
        aim = query.aim  # get aim
        Session.close()
        return (name, aim)


    # This function sets name and aim for users by using 'user_id'
    def set_name_and_aim(user_id, name, aim):
        query = Session.query(Users).get(user_id)
        query.name = name  # set name
        query.aim = aim  # set aim
        Session.commit()  # use this after setting anything.
        # Now you don't need to 'Session.close()' as you used 'Session.commit()' already.

    # Etc
