from pydantic import BaseModel, validator
from typing import Optional

class VehicleBase(BaseModel):
    vehicle_type: str
    cost: float
