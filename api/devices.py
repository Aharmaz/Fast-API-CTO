from typing import List


from db.models.device import Device
import fastapi 
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.device import Device
from api.utils.devices import get_devices

router = fastapi.APIRouter()

@router.get("/devices", response_model=List[Device])
def read_devices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        devices = get_devices(db, skip=skip, limit=limit)
        return devices