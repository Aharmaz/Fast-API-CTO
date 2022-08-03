from operator import index
from unicodedata import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from db.models.mixins import Timestamp

from ..db_setup import Base


class Device(Timestamp, Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    internet_speed = Column(Integer, index=True, nullable=False)
    speed = Column(Integer, index=True, nullable=False)
    temperature = Column(Integer, index=True, nullable=False)
    batry = Column(Integer, index=True, nullable=False)
    distance = Column(Integer, index=True, nullable=False)
    image = Column(String(500), index=True, nullable=False)
