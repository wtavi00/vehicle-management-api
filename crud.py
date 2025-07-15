from models import Vehicle
from sqlalchemy.orm import Session
from schemas import VehicleCreate

PREMIUM_RATES = {
    "Two Wheeler": 0.02,
    "Four Wheeler": 0.06
}

