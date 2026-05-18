# ✨ AstroDiary — Дипломный проект

Веб-приложение для астрологического самоанализа и ведения дневника.

## 🚀 Быстрый старт

### 1. Бэкенд (FastAPI)
```bash
cd astrology-backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000


Фронтенд (React + Vite)

cd astrology-frontend
npm install
npm run dev


База данных (PostgreSQL)
Создайте БД astrology_db

Выполните скрипт init_db.sql



Структура проекта

.
├── astrology-backend/     # FastAPI (Python)
│   ├── main.py           # Точка входа, API роуты
│   ├── models.py         # SQLAlchemy модели
│   ├── auth.py           # JWT + хэширование
│   └── astro_logic.py    # Расчёт планет (симуляция)
├── astrology-frontend/    # React + TypeScript
│   ├── src/
│   │   ├── pages/        # Login, Dashboard, Horoscope, Diary
│   │   ├── api/          # Axios клиент
│   │   └── components/   # Header, PrivateRoute
└── docs/
    └── use-case-diagram.mmd


API Endpoints
Метод	Эндпоинт	Описание
POST	/api/auth/register	Регистрация
POST	/api/auth/login	JWT логин
GET	/api/users/me	Профиль
GET	/api/astro/current-aspect	Гороскоп дня
POST	/api/diary/entries	Запись в дневник
GET	/api/diary/entries	Все записи

Логин для теста
Email: test@mail.com

Пароль: (любой, т.к. хэш в БД заглушка, но в коде используется bcrypt — зарегистрируйтесь через /register)

📅 Задания из практики
Use-case диаграмма — docs/use-case-diagram.mmd

HTML + JS — все страницы реализованы на React

ER-диаграмма — описана через SQL CREATE TABLE (см. init_db.sql)


Технологии
React 18, TypeScript, Vite

FastAPI, SQLAlchemy

PostgreSQL, JWT

📝 Лицензия
Учебный проект.