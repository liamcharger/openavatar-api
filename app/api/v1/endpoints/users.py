from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.db.models import User
from app.schemas.user import UserCreate, UserOut

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/create", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        uid=user.uid,
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
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

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    
    return db_user