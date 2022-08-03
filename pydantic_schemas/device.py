from datetime import datetime
from sqlite3 import IntegrityError
from tokenize import String

from pydantic import BaseModel


class Device(BaseModel):
    id: int
    name: str
    internet_speed: int
    speed: int
    temperature: int
    batry: int
    distance: int
    image: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True