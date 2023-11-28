#!/usr/bin/python3
"""this module defines the schemas for the products"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    product_name: str
    price: float
    quantity: int
    description: Optional[str] = None
    image: Optional[str] = None



class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    created_at: datetime

    class Config:
        from_attributes = True