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
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from ..config import DATABASE_URL

if not DATABASE_URL:
    pass


def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


Base = declarative_base()
# Type-Hinting is wrong here, but a temporary way to get Hints for Session object
Session: sqlalchemy.orm.Session = start()
