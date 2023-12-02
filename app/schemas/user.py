#!/usr/bin/python3
"""users schemas"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class User(BaseModel):
    """User schemas"""
    id: int
    email: str
    created_at: datetime
    name: str
    location: str
    phone: str


class UserCreate(BaseModel):
    """User create schemas"""
    email: str
    password: str
    name: Optional[str] = None
    location: Optional[str] = None
    phone: Optional[str] = None


class Token(BaseModel):
    """Token schemas"""
    access_token: str
    token_type: str = "bearer"

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    """Token data schemas"""
    email: Optional[str] = None
