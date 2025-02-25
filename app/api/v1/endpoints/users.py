from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import shutil
import os
from app.db.session import get_db
from app.db.models import User
from app.schemas.user import UserCreate, UserOut
from app.core.security import hash_email
from uuid import uuid4

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/{hashed_email}", response_model=UserOut)
def get_user(hashed_email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email_hashed == hashed_email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/create", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    db_user = User(
        id=str(uuid4()),
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        email_hashed=hash_email(user.email),
        nickname=user.nickname,
        pronunciation=user.pronunciation,
        bio=user.bio,
        job=user.job,
        pronouns=user.pronouns,
        avatar_url=user.avatar_url,
        social_accounts=user.social_accounts,
        emails=user.emails,
        phone_numbers=user.phone_numbers,
        interests=user.interests
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/{user_id}/avatar", response_model=UserOut)
async def upload_profile_picture(user_id: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    upload_directory = "static/images"
    
    os.makedirs(upload_directory, exist_ok=True)

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if file.filename.split(".")[-1] not in ("jpg", "jpeg", "png"):
        raise HTTPException(status_code=400, detail="Invalid image format")

    file_path = f"{upload_directory}/{user_id}.{file.filename.split('.')[-1]}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    user.avatar_url = file_path
    db.commit()
    db.refresh(user)

    return user

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    
    return db_user
