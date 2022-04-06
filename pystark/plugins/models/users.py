from pystark.database.sql import Base
from sqlalchemy import Column, BigInteger


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id
