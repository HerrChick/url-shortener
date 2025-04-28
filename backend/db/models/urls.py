from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class URLS(Base):
    __tablename__ = "URLs"
    id = Column(Integer, primary_key=True, index=True)
    unshortened_url = Column(String, unique=True, index=True)
    shortened_url = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
