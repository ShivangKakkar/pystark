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

import sqlalchemy
from ..config import ENV
from sqlalchemy import inspect
from pystark.logger import logger
from typing import Optional, Union
from pystark.config import settings
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


# Needs to be outside the class so that models can exist without database
Base = declarative_base()
__checked__ = False


class Database:
    """Class Database with in-built functions to make sqlalchemy easier.

    Attributes:
        url - DATABASE_URL
        base - SQLAlchemy Base
        session - SQLAlchemy Session
        engine - SQLAlchemy engine
    """

    def __init__(self):
        self.url = ENV.DATABASE_URL
        if not self.url:
            logger.critical('No DATABASE_URL defined. Exiting...')
            raise SystemExit
        module = settings()
        self.base = Base
        engine = create_engine(ENV.DATABASE_URL)
        Base.metadata.bind = engine
        global __checked__
        if not __checked__:
            specified_tables = module.DATABASE_TABLES
            actual_tables = Base.metadata.tables
            all_tables = ["bans", "users"]
            for t in all_tables:
                if t not in specified_tables and t in actual_tables:
                    Base.metadata.remove(actual_tables[t])
            __checked__ = True
        Base.metadata.create_all(bind=engine, checkfirst=True)
        Session = scoped_session(sessionmaker(bind=engine, autoflush=False))
        # Type-Hinting is wrong here, but a temporary way to get Hints for Session object as their methods are similar
        self.session: sqlalchemy.orm.Session = Session
        self.engine = Session.get_bind()

    async def get(self, table_name: str, primary_key, key: Union[str] = "") -> Union[dict, None]:
        """Get data from postgres database using table name as string.

        Parameters:
            table_name (``str``):
                The table name to query on.

            primary_key:
                The value of a primary_key to query the table.

            key:
                If you only need one key.

        Returns:
            Key-value pairs if no key is passed. Value of the key if key is passed. None if no such row.

        Raises:
            TableNotFound- If table is not found
        """
        tables_dict = await self.tables_dict()
        if table_name not in tables_dict:
            raise TableNotFound(f'No such table exists : {table_name}')
        table = tables_dict[table_name]
        query = self.session.query(table).get(primary_key)
        if not query:
            return
        all_val = await self._class_vars(query)
        if key:
            return all_val.get(key)
        return all_val

    async def set(self, table_name: str, primary_key, data: dict = None):
        """Set data in postgres database using table name as string. ``insert`` is an alias of ``set``

        If `data` is not passed, `primary key` is added in a new row to table.

        Parameters:
            table_name (``str``):
                The table name to query on.

            primary_key:
                The value of a primary_key to query the table.

            data (``dict``):
                Key-value pairs of column name and row value as dictionary

        Returns:
            ``bool``: True on success
        """
        if data is None:
            data = {}
        tables_dict = await self.tables_dict()
        if table_name not in tables_dict:
            raise TableNotFound(f'No such table exists : {table_name}')
        table = tables_dict[table_name]
        try:
            query = self.session.query(table).get(primary_key)
            if query:
                for i in data:
                    setattr(query, i, data[i])
            else:
                row = table(primary_key)
                for i in data:
                    setattr(query, i, data[i])
                self.session.add(row)
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise

    async def count(self, table_name: str) -> Optional[int]:
        """Get number of rows in postgres table.

        Parameters:
            table_name:
                The table name to query on.
        """
        tables_dict = await self.tables_dict()
        if table_name not in tables_dict:
            raise TableNotFound(f'No such table exists : {table_name}')
        table = tables_dict[table_name]
        count = self.session.query(table).count()
        return count

    insert = set

    async def all(self, table_name: str) -> Optional[list[dict]]:
        """Get all rows in postgres table. Better use ``get_all_data``

        Parameters:
            table_name (``str``):
                The table name to query on.
        """
        tables_dict = await self.tables_dict()
        if table_name not in tables_dict:
            raise TableNotFound(f'No such table exists : {table_name}')
        table = tables_dict[table_name]
        try:
            try:
                all_ = self.session.query(table).all()
                self.session.close()
                return [await self._class_vars(d) for d in all_]
            except ProgrammingError:
                self.session.rollback()
                data = []
                raw = self.session.execute(f'SELECT * FROM {table_name}')
                for r in raw:
                    row = {}
                    for key, value in r.items():
                        row.update({key: value})
                    data.append(row)
                return data
        except Exception:
            self.session.rollback()
            raise

    async def delete(self, table_name: str, primary_key) -> None:
        """Delete row in postgres database using table name as string.

        Parameters:
            table_name (``str``):
                The table name to query on.

            primary_key:
                The value of a primary_key to query the table.
        """
        tables_dict = await self.tables_dict()
        if table_name not in tables_dict:
            raise TableNotFound(f'No such table exists : {table_name}')
        table = tables_dict[table_name]
        try:
            query = self.session.query(table).get(primary_key)
            self.session.delete(query)
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise

    async def get_all_primary_keys(self, table_name) -> list:
        """Get all primary keys of the table

        Parameters:
            table_name (``str``):
                Name of the table whose primary keys you need.
        """
        return [i[0] for i in self.engine.execute('SELECT * FROM %s' % table_name)]

    async def get_all_data(self, table_name: str) -> list[dict]:
        """Get all data of the table as a list of rows as dictionaries

        Parameters:
            table_name (``str``):
                Name of the table whose data you need.
        """
        return [getattr(x, "_asdict")() for x in self.engine.execute('SELECT * FROM %s' % table_name)]

    async def change_column_type(self, table_name: str, column_name: str, column_type: str):
        """Change Column Type of Table using raw sql queries. Supposed to be run only one time for any particular values.

        Parameters:
            table_name (``str``):
                Name of the table where the column exists.

            column_name:
                Name of the column you want to change.

            column_type:
                New Column Type.
        """
        self.engine.execute('ALTER TABLE %s ALTER COLUMN %s TYPE %s' % (table_name, column_name, column_type))

    async def add_column(self, table_name: str, column_name: str, column_type: str):
        """Add Column of Table using raw sql queries. Supposed to be run only one time for any particular values.

        Parameters:
            table_name (``str``):
                Name of the table where you want the table.

            column_name:
                Name of the column you want to add.

            column_type:
                New Column Type.
        """
        self.engine.execute('ALTER TABLE %s ADD %s %s' % (table_name, column_name, column_type))

    async def remove_column(self, table_name: str, column_name: str):
        """Remove Column of Table using raw sql queries. Supposed to be run only one time for any particular values.

        Parameters:
            table_name (``str``):
                Name of the table where the table exists.

            column_name:
                Name of the column you want to delete.
        """
        self.engine.execute('ALTER TABLE %s DROP COLUMN %s' % (table_name, column_name))

    async def columns(self, table_name: str) -> list[tuple[str]]:
        """List of all public column names in the database

        Parameters:
            table_name (``str``):
                Name of the table whose columns you need.
        """
        return [x[0] for x in self.engine.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '%s'" % table_name)]

    async def list_tables(self) -> list:
        """Returns list all tables in your database"""
        return inspect(self.engine).get_table_names()

    async def has_table(self, table_name: str) -> bool:
        """Returns True if table exists else False. To also check if it's sqlalchemy model exists, use function ``table_exists`` instead"""
        inspect(self.engine)
        return inspect(self.engine).has_table(table_name)

    async def table_exists(self, table_name: str) -> bool:
        """Returns True if table exists with sqlalchemy model else False. To check only for table, use function ``has_table`` instead"""
        tables_dict = await self.tables_dict()
        if table_name in tables_dict:
            return True
        else:
            return False

    async def tables_dict(self) -> dict:
        """Returns all {tablename: table} where tablename is a string and table is a model (python class)"""
        return {table.__tablename__: table for table in self.base.__subclasses__()}

    @staticmethod
    async def _class_vars(class_obj) -> dict:
        v = vars(class_obj)
        return {key: v[key] for key in v if key != "_sa_instance_state"}


class TableNotFound(Exception):
    pass
