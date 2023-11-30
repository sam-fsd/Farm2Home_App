#!/usr/bin/python3
"""this module defines the schemas for the products"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductCreate(BaseModel):
    product_name: str
    price: float
    quantity: int
    description: Optional[str] = ""
    image: Optional[str] = ""
    category: Optional[str] = ""


class Product(ProductCreate):
    product_id: str
    created_at: str
    farmer_id: str

    class Config:
        from_attributes = True

