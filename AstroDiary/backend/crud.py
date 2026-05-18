from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List, Optional
import models
import schemas
import auth

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        name=user.name,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate) -> Optional[models.User]:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None
    
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> bool:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return False
    
    db.delete(db_user)
    db.commit()
    return True

def authenticate_user(db: Session, email: str, password: str) -> Optional[models.User]:
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not auth.verify_password(password, user.hashed_password):
        return None
    return user

def create_diary_entry(db: Session, entry: schemas.DiaryCreate, user_id: int, planets_positions: str) -> models.DiaryEntry:
    db_entry = models.DiaryEntry(
        user_id=user_id,
        content=entry.content,
        mood=entry.mood,
        planets_positions=planets_positions
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_diary_entries_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[models.DiaryEntry]:
    return db.query(models.DiaryEntry).filter(
        models.DiaryEntry.user_id == user_id
    ).order_by(models.DiaryEntry.created_at.desc()).offset(skip).limit(limit).all()

def get_diary_entry_by_id(db: Session, entry_id: int, user_id: int) -> Optional[models.DiaryEntry]:
    return db.query(models.DiaryEntry).filter(
        and_(
            models.DiaryEntry.id == entry_id,
            models.DiaryEntry.user_id == user_id
        )
    ).first()

def update_diary_entry(db: Session, entry_id: int, user_id: int, entry_update: schemas.DiaryUpdate) -> Optional[models.DiaryEntry]:
    db_entry = get_diary_entry_by_id(db, entry_id, user_id)
    if not db_entry:
        return None
    
    update_data = entry_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_entry, field, value)
    
    db.commit()
    db.refresh(db_entry)
    return db_entry

def delete_diary_entry(db: Session, entry_id: int, user_id: int) -> bool:
    db_entry = get_diary_entry_by_id(db, entry_id, user_id)
    if not db_entry:
        return False
    
    db.delete(db_entry)
    db.commit()
    return True

def get_diary_entries_by_date_range(db: Session, user_id: int, start_date, end_date) -> List[models.DiaryEntry]:
    return db.query(models.DiaryEntry).filter(
        and_(
            models.DiaryEntry.user_id == user_id,
            models.DiaryEntry.created_at >= start_date,
            models.DiaryEntry.created_at <= end_date
        )
    ).order_by(models.DiaryEntry.created_at).all()

def get_recent_entries(db: Session, user_id: int, days: int = 7) -> List[models.DiaryEntry]:
    from datetime import datetime, timedelta
    start_date = datetime.now() - timedelta(days=days)
    return get_diary_entries_by_date_range(db, user_id, start_date, datetime.now())