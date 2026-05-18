from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
import models 
import  schemas
import auth
import crud
import astro_logic
from database import engine, get_db


# uvicorn main:app --reload --port 8000 запуск

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AstroDiary API", description="API для астрологического дневника", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
    email = auth.decode_access_token(token)
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный или просроченный токен",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = crud.get_user_by_email(db, email=email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не найден",
        )
    return user

@app.post("/api/auth/register", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже существует"
        )
    return crud.create_user(db=db, user=user)

@app.post("/api/auth/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль",
        )
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/users/me", response_model=schemas.UserOut)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

@app.put("/api/users/me", response_model=schemas.UserOut)
def update_user_me(
    user_update: schemas.UserUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    updated_user = crud.update_user(db, current_user.id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return updated_user

@app.delete("/api/users/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_me(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    crud.delete_user(db, current_user.id)

@app.get("/api/astro/current-aspect", response_model=schemas.AspectResponse)
def get_current_aspect(current_user: models.User = Depends(get_current_user)):
    if current_user.birth_date:
        aspect_text = astro_logic.calculate_aspect(current_user.birth_date)
    else:
        aspect_text = "Укажите дату рождения в профиле для точного персонального прогноза."
    
    planets = astro_logic.get_current_planet_positions()
    
    return schemas.AspectResponse(text=aspect_text, planets=planets)

@app.get("/api/astro/planet-positions")
def get_planet_positions():
    return {"planets": astro_logic.get_current_planet_positions()}

@app.post("/api/diary/entries", response_model=schemas.DiaryOut, status_code=status.HTTP_201_CREATED)
def create_diary_entry(
    entry: schemas.DiaryCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    planets_positions = astro_logic.get_current_planet_positions()
    db_entry = crud.create_diary_entry(db, entry, current_user.id, planets_positions)
    return db_entry

@app.get("/api/diary/entries", response_model=List[schemas.DiaryOut])
def get_diary_entries(
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    entries = crud.get_diary_entries_by_user(db, current_user.id, skip, limit)
    return entries

@app.get("/api/diary/entries/{entry_id}", response_model=schemas.DiaryOut)
def get_diary_entry(
    entry_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    entry = crud.get_diary_entry_by_id(db, entry_id, current_user.id)
    if not entry:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    return entry

@app.put("/api/diary/entries/{entry_id}", response_model=schemas.DiaryOut)
def update_diary_entry(
    entry_id: int,
    entry_update: schemas.DiaryUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    updated_entry = crud.update_diary_entry(db, entry_id, current_user.id, entry_update)
    if not updated_entry:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    return updated_entry

@app.delete("/api/diary/entries/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_diary_entry(
    entry_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    success = crud.delete_diary_entry(db, entry_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Запись не найдена")

@app.get("/api/diary/recent/{days}")
def get_recent_entries(
    days: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    entries = crud.get_recent_entries(db, current_user.id, days)
    return entries

@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "AstroDiary API работает!"}