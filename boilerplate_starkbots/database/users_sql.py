from pystark.database.postgres import Base, Session
from sqlalchemy import Column, BigInteger, String


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)
    data = Column(String)

    def __init__(self, user_id, data=None):
        self.user_id = user_id
        self.data = data


Users.__table__.create(checkfirst=True)


def num_users():
    try:
        return Session.query(Users).count()
    finally:
        Session.close()
