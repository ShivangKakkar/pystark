from pystark.database.sql import Base
from sqlalchemy import Column, BigInteger, String


class Bans(Base):
    __tablename__ = "bans"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)
    reason = Column(String, nullable=True)

    def __init__(self, user_id, reason=None):
        self.user_id = user_id
        self.reason = reason
