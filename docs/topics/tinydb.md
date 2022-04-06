# Using TinyDB

TinyDB is a simple json-based database which does not need anything externally. You don't need to have a Database URL for it, and you can add unlimited data.

---

## When to use TinyDB?

It's recommended to use TinyDB during these situations. If you:

- are a beginner and need a simple database.
- are deploying your bot locally.
- have a small project.
- don't care that much about speed and performance. Though you won't see much difference in small projects.


---

## How to Initialize TinyDB?

!!! note 
    Don't forget to add `tinydb` to `requirement.txt`

Here's how to initialize TinyDB

```python
# import db object from pystark
from pystark.database.tiny_db import db, Query

# or create a db object yourself
from tinydb import TinyDB, Query
db = TinyDB('db.json')
```

---

## How to Query TinyDB?

- Insert Data

```python
from pystark.database.tiny_db import db

# just pass a python dictionary to insert() function.
db.insert({'type': 'apple', 'count': 7})
db.insert({'name': 'Stark', 'aim': 'Meet God'})
```

- Search/Query Data

```python
from pystark.database.tiny_db import db
# Along with db object, you need Query object too.
# import Query object from pystark or tinydb
from pystark.database.tiny_db import Query
# or
from tinydb import Query

Fruit = Query()
data = db.search(Fruit.type == 'apple')

User = Query()
data = db.search(User.name == 'Stark')
```

- Remove/Delete Data

```python
from pystark.database.tiny_db import db, Query

Fruit = Query()
data = db.remove(Fruit.type == 'apple')

User = Query()
data = db.remove(User.name == 'Stark')
```

- Update Data

```python
from pystark.database.tiny_db import db, Query

Fruit = Query()
data = db.update({'count': 10}, Fruit.type == 'apple')

User = Query()
data = db.update({'aim': 'Create Time Machine'}, User.name == 'Stark')
```

- Get all Data

```python
db.all()
```

- Get all Tables

```python
db.tables()
```

- Number of Tables

```python
db.tables_count()
```

- Delete all Data / Empty the Database

```python
db.truncate()
```
