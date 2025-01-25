from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    uid: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: str
    nickname: str
    pronunciation: Optional[str] = None
    bio: Optional[str] = None
    job: Optional[str] = None
    pronouns: Optional[str] = None
    avatar_url: Optional[str] = None
    social_accounts: Optional[List[str]] = None
    emails: Optional[List[str]] = None
    phone_numbers: Optional[List[str]] = None
    interests: Optional[List[str]] = None

class UserOut(BaseModel):
    id: str
    uid: str
    firstname: Optional[str]
    lastname: Optional[str]
    email: str
    nickname: str
    pronunciation: Optional[str]
    bio: Optional[str]
    job: Optional[str]
    pronouns: Optional[str]
    avatar_url: Optional[str]
    social_accounts: Optional[List[str]]
    emails: Optional[List[str]]
    phone_numbers: Optional[List[str]]
    interests: Optional[List[str]]

    class Config:
        from_attributes = True