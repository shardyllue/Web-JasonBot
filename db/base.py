from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, BigInteger, String


Base = declarative_base()


class UserTable(Base):

    __tablename__ = "user"

    user_id  = Column(BigInteger, primary_key=True)
    hash_token = Column(String(256), unique=True)

    def __init__(self, user_id : int, hashed_token : str):

        self.user_id = user_id
        self.hash_token = hashed_token


class ChannelTable(Base):

    __tablename__ = "channel"

    id = Column(BigInteger, primary_key=True)
    user_id  = Column(BigInteger)
    channel_id : int = Column(BigInteger)

    def __init__(self, user_id : int, channel_id : str):

        self.user_id = user_id
        self.channel_id = channel_id