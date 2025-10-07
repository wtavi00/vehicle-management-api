from pydantic import BaseModel, Field
from typing import Optional

class VehicleBase(BaseModel):
    registration_number: str = Field(..., example="ABC-1234")
    brand: str = Field(..., example="Toyota")
    model: str = Field(..., example="Corolla")
    year: int = Field(..., ge=1950, le=2100, example=2020)
    is_active: Optional[bool] = True

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(BaseModel):
    brand: Optional[str]
    model: Optional[str]
    year: Optional[int]
    is_active: Optional[bool]

class VehicleResponse(VehicleBase):
    id: int
    class Config:
        orm_mode = True
