#!/usr/bin/python3
"""farmers schemas"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


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



class Farmer(BaseModel):
    id: str
    name: str
    email: str
    # password: str
    location: str
    phone: str
    # Products: List[Product] = []
    # bio: str = ""


    class Config:
        from_attributes = True
    

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class FarmerResponse(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    # password: str
    location: str
    phone: str
    bio: str
    products: List[Product] = []

    class Config:
        from_attributes = True

class FarmerCreate(Farmer):
    email: str
    password: str