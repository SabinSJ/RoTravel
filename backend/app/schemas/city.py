from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class CityBase(BaseModel):
    name: str
    region: str
    description: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None

class CityOut(CityBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True