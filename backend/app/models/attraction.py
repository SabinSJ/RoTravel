import uuid
from sqlalchemy import UUID, Column, Integer, String, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Attraction(Base):
    __tablename__ = "attractions"

    id               = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    city_id          = Column(UUID(as_uuid=True), ForeignKey("cities.id"))
    name             = Column(String, nullable=False)
    category         = Column(String, nullable=False)
    rating           = Column(Numeric)
    duration_minutes = Column(Integer)
    description      = Column(Text)
    lat              = Column(Numeric)
    lng              = Column(Numeric)
    created_at       = Column(DateTime, server_default=func.now())

    city = relationship("City", back_populates="attractions")