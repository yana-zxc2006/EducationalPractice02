from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    hashed_password = Column(Text, nullable=False)
    birth_date = Column(DateTime, nullable=True)
    birth_place = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DiaryEntry(Base):
    __tablename__ = "diary_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    mood = Column(String(50), nullable=False)
    planets_positions = Column(Text, nullable=True) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())