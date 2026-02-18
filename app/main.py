import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from jose import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

from app.database import engine, get_db
from app import models, schemas, crud

load_dotenv()

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


app = FastAPI(
    title="Ngrok Learnings API",
    description="A FastAPI application with User CRUD operations and Vercel Postgres",
    version="1.0.0"
)


# ─── Hello World ────────────────────────────────────────────────

@app.get("/")
def hello_world():
    return {"message": "Hello World"}


# ─── User Routes ────────────────────────────────────────────────

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users", response_model=List[schemas.UserResponse])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all users."""
    users = crud.get_all_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """Retrieve a user by their ID."""
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
