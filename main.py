from schemas import VehicleUpdate
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal, engine, Base
from models import Vehicle

app = FastAPI() # Initialize FastAPI app

# Create tables
Base.metadata.create_all(bind=engine)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put("/vehicles/{vehicle_id}", response_model=schemas.VehicleOut)
def update_vehicle(vehicle_id: str, updates: VehicleUpdate, db: Session = Depends(get_db)):
    update_data = updates.dict(exclude_unset=True)
    updated = crud.update_vehicle(db, vehicle_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return updated

@app.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_vehicle(db, vehicle_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"message": f"Vehicle {vehicle_id} deleted successfully"}
    
