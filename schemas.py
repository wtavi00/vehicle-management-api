from pydantic import BaseModel, validator
from typing import Optional

class VehicleBase(BaseModel):
    vehicle_type: str
    cost: float

    @validator("vehicle_type") 
    def validate_type(cls, v):
        if v not in ["Two Wheeler", "Four Wheeler"]:
            raise ValueError("Vehicle type must be 'Two Wheeler' or 'Four Wheeler'")
        return v

class VehicleCreate(VehicleBase):
    vehicle_id: str

class VehicleOut(VehicleCreate):
    premium_amount: float

class VehicleUpdate(BaseModel):
    vehicle_type: Optional[str] = None
    cost: Optional[float] = None

