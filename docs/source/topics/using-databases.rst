Using Databases
===============

You can use any database you wish with PyStark, but we have provided a simple default setup for some databases, such as PostgreSQL and Redis, to make them even easier to use.
By following this guide, you will have a basic understanding of how to use them.

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

------

TinyDB
-------

TinyDB is a simple database which does not require a Database URL and is very simple. If you are a beginner, it is for you. :doc:`Read How to Use It </topics/tinydb>`.

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
        user_id = Column(Integer, primary_key=True)  # sql primary key (pk)
        name = Column(String)
        aim = Column(String)

        def __init__(self, user_id, name, aim=None):
            self.user_id = user_id
            self.name = name
            self.aim = aim


    # Create Table
    Users.__table__.create(checkfirst=True)

- **Querying Tables** - You can query tables using ``Session`` object or the in-built pystark functions.

    - :ref:`Using Session object <session-object>`
    - :ref:`Using in-built functions <default-functions>`

--------

Using Telegram as a Database
----------------------------

You can use Telegram as a Database, thanks to `this project <https://pypi.org/project/TelegramDB/>`_.

**But How?** - :doc:`Read Documentation Here </topics/telegram-as-database>`


--------

Redis (using redis-py)
----------------------

- **Variables** - You need to set ``REDIS_URL`` (public endpoint) and ``REDIS_PASSWORD`` by creating a database at `redislabs.com <https://redislabs.com>`_

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
