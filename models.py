from sqlalchemy import Column, String, Float
from database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(String, primary_key=True, index=True)
    vehicle_type = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    premium_amount = Column(Float, nullable=True)
    
