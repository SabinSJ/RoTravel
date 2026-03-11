from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class AttractionBase(BaseModel):
    name: str
    category: str
    rating: Optional[float] = None
    duration_minutes: Optional[int] = None
    description: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None

class AttractionOut(AttractionBase):
    id: UUID
    city_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True