from models import Vehicle
from sqlalchemy.orm import Session
from schemas import VehicleCreate

PREMIUM_RATES = {
    "Two Wheeler": 0.02,
    "Four Wheeler": 0.06
}

def calculate_premium(vehicle_type: str, cost: float) -> float:
    return PREMIUM_RATES[vehicle_type] * cost

