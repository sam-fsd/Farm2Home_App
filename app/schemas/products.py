#!/usr/bin/python3
"""this module defines the schemas for the products"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProductCreate(BaseModel):
    product_name: str
    price: float
    quantity: int
    description: str = ""
    image: str = ""
    category: str = ""
    farmer_id: Optional[str] = None


class ProductList(ProductCreate):
    # product_id: str
    created_at: datetime
    farmer_id: str
