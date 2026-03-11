import uuid
from sqlalchemy import UUID, Column, String, Text, Numeric, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class City(Base):
    __tablename__ = "cities"

    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name        = Column(String, nullable=False)
    region      = Column(String, nullable=False)
    description = Column(Text)
    lat         = Column(Numeric)
    lng         = Column(Numeric)
    created_at  = Column(DateTime, server_default=func.now())

    attractions = relationship("Attraction", back_populates="city")