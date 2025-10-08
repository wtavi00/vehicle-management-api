from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.VehicleResponse])
def list_vehicles(skip: int = 0, limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    return crud.get_vehicles(db, skip=skip, limit=limit)

@router.get("/{vehicle_id}", response_model=schemas.VehicleResponse)
def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = crud.get_vehicle_by_id(db, vehicle_id)
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle

@router.post("/", response_model=schemas.VehicleResponse)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    return crud.create_vehicle(db, vehicle)

@router.put("/{vehicle_id}", response_model=schemas.VehicleResponse)
def update_vehicle(vehicle_id: int, update_data: schemas.VehicleUpdate, db: Session = Depends(get_db)):
    updated = crud.update_vehicle(db, vehicle_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return updated

@router.delete("/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_vehicle(db, vehicle_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"message": "Vehicle deleted successfully"}
