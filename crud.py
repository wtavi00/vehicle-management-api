from models import Vehicle
from sqlalchemy.orm import Session
from schemas import VehicleCreate

PREMIUM_RATES = {
    "Two Wheeler": 0.02,
    "Four Wheeler": 0.06
}

def calculate_premium(vehicle_type: str, cost: float) -> float:
    return PREMIUM_RATES[vehicle_type] * cost

def get_vehicle(db: Session, vehicle_id: str):
    return db.query(Vehicle).filter(Vehicle.vehicle_id == vehicle_id).first()

def create_vehicle(db: Session, vehicle: VehicleCreate):
    premium = calculate_premium(vehicle.vehicle_type, vehicle.cost)
    db_vehicle = Vehicle(
        vehicle_id=vehicle.vehicle_id,
        vehicle_type=vehicle.vehicle_type,
        cost=vehicle.cost,
        premium_amount=premium
    )
    
