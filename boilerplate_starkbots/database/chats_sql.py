from sqlalchemy import Column, BigInteger
from pystark.database.postgres import Base, Session


class Chats(Base):
    __tablename__ = "chats"
    __table_args__ = {'extend_existing': True}
    chat_id = Column(BigInteger, primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Chats.__table__.create(checkfirst=True)


async def num_chats():
    try:
        return Session.query(Chats).count()
    finally:
        Session.close()
