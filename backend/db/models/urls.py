from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base
import hashlib
import base64

class URL(Base):
    __tablename__ = "URLs"
    id = Column(Integer, primary_key=True, index=True)
    unshortened_url = Column(String, unique=True, index=True)
    shortened_url = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def generate_shortened_url(self):
        if not self.shortened_url:
            raise ValueError("no unshortened URL exists for this object")
        
        hash = hashlib.md5(self.unshortened_url.encode())
        
        short_hash = base64.urlsafe_b64encode(hash.digest())[:8].decode()
        
        self.shortened_url = short_hash
        return self.shortened_url