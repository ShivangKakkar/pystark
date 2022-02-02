# PyStark - Python add-on extension to Pyrogram
# Copyright (C) 2021-2022 Stark Bots <https://github.com/StarkBotsIndustries>
#
# This file is part of PyStark.
#
# PyStark is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyStark is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyStark. If not, see <https://www.gnu.org/licenses/>.

from pystark import Stark

# Not a very good way but personalized automation and no extra dependencies.
try:
    import sqlalchemy
except ImportError:
    import os
    Stark.log('Installing SQLAlchemy... [needed for postgres]')
    os.system('pip3 install sqlalchemy~=1.4.31')
    Stark.log('Installing psycopg2... [needed for postgres]')
    os.system('pip3 install psycopg2')
    import sqlalchemy
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from ..config import ENV
from sqlalchemy.exc import ProgrammingError

DATABASE_URL = ENV.DATABASE_URL

if not DATABASE_URL:
    Stark.log('No DATABASE_URL defined. Exiting...', "critical")
    raise SystemExit


def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


Base = declarative_base()
# Type-Hinting is wrong here, but a temporary way to get Hints for Session object
Session: sqlalchemy.orm.Session = start()


class Database:
    """Class Database with in-built functions to make sqlalchemy easier.

    Attributes:
        url - DATABASE_URL
        base - SQLAlchemy Base
        session - SQLAlchemy Session
        engine - SQLAlchemy engine
    """

    def __init__(self):
        self.url = DATABASE_URL
        self.base = Base
        self.session = Session
        self.engine = Session.get_bind()

    async def get(self, table_name: str, primary_key, key: str = None):
        """Get data from postgres database using table name as string.
        Returns dict if key_name is not passed.

        Parameters:
            table_name (``str``):
                The table name to query on.

            primary_key:
                The value of a primary_key to query the table.

            key (``str``, *optional*):
                If passed, only value for the specified key is returned.
        """
        tables_dict = await self._tables_dict()
        table_exists = await self._table_exists(table_name)
        if not table_exists:
            return
        table = tables_dict[table_name]
        query = Session.query(table).get(primary_key)
        if key:
            return query[key]
        return await self._class_vars(query)

    async def set(self, table_name: str, primary_key, key: str, value) -> bool:
        """Set data in postgres database using table name as string.

        Parameters:
            table_name (``str``):
                The table name to query on.

            primary_key:
                The value of a primary_key to query the table.

            key (``str``):
                The key name to set value in.

            value:
                The value for the key.

        Returns:
            ``bool``: True on success
        """
        tables_dict = await self._tables_dict()
        table_exists = await self._table_exists(table_name)
        if not table_exists:
            return False
        table = tables_dict[table_name]
        try:
            query = Session.query(table).get(primary_key)
            if query:
                setattr(query, key, value)
            else:
                row = table(primary_key)
                setattr(row, key, value)
                Session.add(row)
            Session.commit()
            return True
        except Exception:
            Session.rollback()
            raise

    async def count(self, table_name: str) -> Optional[int]:
        """Get number of rows in postgres table.

        Parameters:
            table_name:
                The table name to query on.
        """
        tables_dict = await self._tables_dict()
        table_exists = await self._table_exists(table_name)
        if not table_exists:
            return
        table = tables_dict[table_name]
        count = Session.query(table).count()
        return count

    async def all(self, table_name: str) -> Optional[list]:
        """Get all rows in postgres table.

        Parameters:
            table_name (``str``):
                The table name to query on.
        """
        tables_dict = await self._tables_dict()
        table_exists = await self._table_exists(table_name)
        if not table_exists:
            raise TableNotFound(f'No such table exists : {table_name}')
        table = tables_dict[table_name]
        try:
            try:
                all_ = Session.query(table).all()
                Session.close()
                return [await self._class_vars(d) for d in all_]
            except ProgrammingError:
                Session.rollback()
                data = []
                raw = Session.execute(f'SELECT * FROM {table_name}')
                for r in raw:
                    row = {}
                    for key, value in r.items():
                        row.update({key: value})
                    data.append(row)
                return data
        except Exception:
            Session.rollback()
            raise

    async def delete(self, table_name: str, primary_key) -> None:
        """Delete row in postgres database using table name as string.

        Parameters:
            table_name (``str``):
                The table name to query on.

            primary_key:
                The value of a primary_key to query the table.
        """
        tables_dict = await self._tables_dict()
        table_exists = await self._table_exists(table_name)
        if not table_exists:
            return
        table = tables_dict[table_name]
        try:
            query = Session.query(table).get(primary_key)
            Session.delete(query)
            Session.commit()
        except Exception:
            Session.rollback()
            raise

    # Private Functions
    @staticmethod
    async def _tables_dict() -> dict:
        """Returns all {tablename: table}"""
        return {table.__tablename__: table for table in Base.__subclasses__()}

    async def _table_exists(self, table_name: str) -> bool:
        """Returns True if table exists else False"""
        tables_dict = await self._tables_dict()
        if table_name in tables_dict:
            return True
        else:
            return False

    @staticmethod
    async def _class_vars(class_obj) -> dict:
        v = vars(class_obj)
        return {key: v[key] for key in v if key != "_sa_instance_state"}


class TableNotFound(Exception):
    pass
