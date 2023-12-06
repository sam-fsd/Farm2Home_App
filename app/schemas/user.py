#!/usr/bin/python3
"""users schemas"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    location: str
    phone: str


class UserCreate(UserBase):
    pass


class FarmerCreate(UserCreate):
    bio: str


class CustomerCreate(BaseModel):
    name: str
    email: str
    password: str
    location: str


class UserLogin(BaseModel):
    email: str
    password: str

