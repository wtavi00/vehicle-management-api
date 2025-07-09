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
