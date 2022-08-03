from datetime import datetime
from sqlite3 import IntegrityError
from tokenize import String

from pydantic import BaseModel


class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    salary: int
    phone: str
    email: str
    role: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True