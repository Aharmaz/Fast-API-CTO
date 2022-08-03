from typing import List

from unittest import skip
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.user import User
from api.utils.users import get_users



router = fastapi.APIRouter()

@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users