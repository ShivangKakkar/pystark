## Databases

In-built core for using **postgres** and **redis** in your bot. Though they are few lines and almost nothing so may say you're better without it, you are right. This is incomplete.

There are a lot of things to do like adding global functions, default classes, alembic support for sqlalchemy, etc and this is just beginning.

### Postgres (using SqlAlchemy)

1. **Database URL** - You need to add `DATABASE_URL` to your environment variables. If you are using Heroku boilerplate, leave it to **Heroku** and **pystark**

2. **Creating and Querying Tables** - You need to create all the tables with all the rows and columns you need. In python, using Classes.
Below is a code example

```python
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


# Define basic functions and query tables using 'Session'
def num_users():
    try:
        return Session.query(Users).count()
    finally:
        Session.close()
```


### Redis (using redis-py)

1. **Variables** - You need to set `REDIS_URL` (public endpoint) and `REDIS_PASSWORD` by creating a database at [redislabs.com](https://redislabs.com)
2. **Setting and Getting key-value pairs**

```python
from pystark.database.redis_db import redis

redis.set('Agra', 'Taj Mahal')
redis.get('Agra')
```
```shell
b'Taj Mahal'
```

**Suggestions** are welcome at **[StarkBotsChat](https://t.me/StarkBotsChat)**
