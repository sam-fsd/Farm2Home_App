#!/usr/bin/python3
"""users schemas"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    """
    Represents the base schema for a user.
    """
    name: str
    email: EmailStr
    password: str
    location: str
    phone: str


class UserCreate(UserBase):
    """
    Represents a schema for creating a user.
    """
    pass


class FarmerCreate(UserCreate):
    """
    Represents a schema for creating a farmer user.
    """
    bio: Optional[str] = None


class CustomerCreate(BaseModel):
    """
    Pydantic model for creating a customer.
    """
    name: str
    email: str
    password: str
    # location: Optional[str] = None  # Lets get customer location to allow matching with farmers
    # phone: Optional[str] = None


class UserLogin(BaseModel):
    """
    Pydantic model for user login.
    """
    email: str
    password: str
