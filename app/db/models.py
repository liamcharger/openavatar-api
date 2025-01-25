from sqlalchemy import Column, String, JSON
from .session import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    nickname = Column(String, nullable=False)
    pronunciation = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    job = Column(String, nullable=True)
    pronouns = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    social_accounts = Column(JSON, nullable=True) 
    emails = Column(JSON, nullable=True)
    phone_numbers = Column(JSON, nullable=True)
    interests = Column(JSON, nullable=True)