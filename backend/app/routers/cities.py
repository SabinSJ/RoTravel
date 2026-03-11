from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database import get_db
from app.models.city import City
from app.models.attraction import Attraction
from app.schemas.city import CityOut
from app.schemas.attraction import AttractionOut

router = APIRouter(prefix="/cities", tags=["cities"])

@router.get("/", response_model=List[CityOut])
def get_cities(db: Session = Depends(get_db)):
    return db.query(City).order_by(City.name).all()

@router.get("/{city_id}", response_model=CityOut)
def get_city(city_id: UUID, db: Session = Depends(get_db)):
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/{city_id}/attractions", response_model=List[AttractionOut])
def get_city_attractions(city_id: UUID, db: Session = Depends(get_db)):
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return db.query(Attraction).filter(Attraction.city_id == city_id).all()