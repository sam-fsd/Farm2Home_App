#!/usr/bin/python3
"""this module defines the schemas for the products"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    name: str
    email: str
    location: str
    phone: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    created_at: str

    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    product_name: str
    price: float
    quantity: int
    description: str = ""
    image: str = ""
    category: str = ""

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: str
    created_at: str
    farmer_id: str

    class Config:
        from_attributes = True

class FarmerCreate(UserCreate):
    bio: str

class Farmer(User):
    bio: str
    products: List[Product] = []

    class Config:
        from_attributes = True

class Customer(User):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ProductBase(BaseModel):
    farmer_id: str
    product_name: str
    price: float
    quantity: int
    description: str = ""
    image: str = ""
    category: str = ""

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: str
    # created_at: str
    # farmer_id: str

    class Config:
        from_attributes = True



class Farmer(BaseModel):
    name: str
    email: str
    password: str
    location: str
    phone: str
    password: str

    

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class FarmerResponse(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    password: str
    location: str
    phone: str
    bio: str
    products: List[Product] = []

    class Config:
        from_attributes = True
