from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from app.database import get_db
from app.models.attraction import Attraction
from app.schemas.attraction import AttractionOut

router = APIRouter(prefix="/attractions", tags=["attractions"])

@router.get("/", response_model=List[AttractionOut])
def get_attractions(
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    q = db.query(Attraction)
    if category:
        q = q.filter(Attraction.category == category)
    return q.order_by(Attraction.rating.desc()).all()

@router.get("/{attraction_id}", response_model=AttractionOut)
def get_attraction(attraction_id: UUID, db: Session = Depends(get_db)):
    attraction = db.query(Attraction).filter(Attraction.id == attraction_id).first()
    if not attraction:
        raise HTTPException(status_code=404, detail="Attraction not found")
    return attraction