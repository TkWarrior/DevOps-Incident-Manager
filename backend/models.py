from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.sql import func
from backend.db import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    error = Column(Text)
    root_cause = Column(Text)
    patch = Column(Text)
    pr = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
