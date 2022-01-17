Using Databases
===============

You can use any database you wish with PyStark, but we have provided a simple default setup for some databases, such as PostgreSQL and Redis, to make them even easier to use.
By following this guide, you will have a basic understanding of how to use them.

.. note::

    This feature is still in beta. There are a lot of things to do like adding global functions, default classes, alembic support for sqlalchemy, etc and this is just a pre-release.

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

--------

PostgreSQL (using sqlalchemy)
-----------------------------

- **Database URL** - You need to add ``DATABASE_URL`` to ``.env``. If you are using Heroku boilerplate, leave it to **Heroku** and **pystark**. Otherwise, you can get a Database URL from `ElephantSQL <http://www.elephantsql.com>`_

.. |a| raw:: html

    <a />

- **Creating Tables** - You need to create all the tables with all columns you need. In Python, using Classes.

Below is a code example for a table named ``users`` with 3 columns named ``user_id``, ``name``, and ``aim``:

.. code-block:: python

    # Import 'Base' and 'Session' already made by pystark
    from pystark.database.postgres import Base, Session
    # Import basic sqlalchemy classes
    from sqlalchemy import Column, Integer, String


    # Every class should inherit from 'Base'
    class Users(Base):
        __tablename__ = "users"
        __table_args__ = {'extend_existing': True}
        user_id = Column(Integer, primary_key=True)  # sql pk
        name = Column(String)
        aim = Column(String)

        def __init__(self, user_id, name, aim=None):
            self.user_id = user_id
            self.name = name
            self.aim = aim


    # Create Table
    Users.__table__.create(checkfirst=True)

- **Querying Tables** - You can query tables using ``Session`` object.

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

--------

Redis (using redis-py)
----------------------

- **Variables** - You need to set ```REDIS_URL`` (public endpoint) and ``REDIS_PASSWORD`` by creating a database at `redislabs.com <https://redislabs.com>`_

.. |b| raw:: html

    <b />

- **Setting and Getting key-value pairs**

.. code-block:: python

    from pystark.database.redis_db import redis

    redis.set('Agra', 'Taj Mahal')


.. code-block:: python

    redis.get('Agra')


.. code-block:: python

    b'Taj Mahal'


--------

MongoDB
-------

Coming soon.
