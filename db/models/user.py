from operator import index
from unicodedata import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship


from ..db_setup import Base
from .mixins import Timestamp


class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(20), index=True, nullable=False)
    lastname = Column(String(20), index=True, nullable=False)
    salary = Column(Integer, index=True, nullable=False)
    phone = Column(String(10), index=True, nullable=False)
    email = Column(String(40), index=True, nullable=False)
    role = Column(String(10), index=True, nullable=False)