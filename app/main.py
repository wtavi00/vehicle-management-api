from fastapi import FastAPI
from app.routes import vehicles
from app.database import Base, engine

# Create all DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vehicle Management API",
    description="A simple REST API to manage vehicles using FastAPI + SQLAlchemy.",
    version="1.0.0"
)

app.include_router(vehicles.router, prefix="/api/v1/vehicles", tags=["Vehicles"])

@app.get("/", tags=["Root"])
def root():
    return {"message": "Vehicle Management API is running 🚗"}

