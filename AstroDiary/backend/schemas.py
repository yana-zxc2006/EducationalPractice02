from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    birth_date: Optional[datetime] = None
    birth_place: Optional[str] = None
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    birth_date: Optional[datetime] = None
    birth_place: Optional[str] = None

class DiaryCreate(BaseModel):
    content: str
    mood: str

class DiaryUpdate(BaseModel):
    content: Optional[str] = None
    mood: Optional[str] = None

class DiaryOut(BaseModel):
    id: int
    user_id: int
    content: str
    mood: str
    planets_positions: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class AspectResponse(BaseModel):
    text: str
    planets: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None