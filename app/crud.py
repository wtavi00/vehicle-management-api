from sqlalchemy.orm import Session
from app import models, schemas

def get_vehicles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Vehicle).offset(skip).limit(limit).all()

def get_vehicle_by_id(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()

def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def update_vehicle(db: Session, vehicle_id: int, update_data: schemas.VehicleUpdate):
    db_vehicle = get_vehicle_by_id(db, vehicle_id)
    if not db_vehicle:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_vehicle, key, value)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = get_vehicle_by_id(db, vehicle_id)
    if not db_vehicle:
        return None
    db.delete(db_vehicle)
    db.commit()
    return True
