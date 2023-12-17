#!/usr/bin/python3
"""this module defines the schemas for the products"""
from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime
import uuid

class ProductCreate(BaseModel):
    """
    A Pydantic model that defines the schema for creating a product.
    """

    product_name: str
    price: float
    quantity: int
    description: str = ""
    image: str = ""
    category: str = ""
    farmer_id: Optional[str] = None


class ProductList(ProductCreate):
    """
    Represents a product with additional fields for the product ID,
    creation timestamp, and farmer ID.

    """

    product_id: uuid.UUID
    created_at: datetime
    farmer_id: uuid.UUID
