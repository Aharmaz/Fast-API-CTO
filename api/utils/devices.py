from sqlalchemy.orm import Session
 
from db.models.device import Device


def get_devices(db: Session, skip: int =0, limit: int = 100):
    return db.query(Device).offset(skip).limit(limit).all()