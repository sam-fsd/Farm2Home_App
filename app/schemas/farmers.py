#!/usr/bin/python3
"""farmers schemas"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from pydantic.fields import Field


class ProductBase(BaseModel):
    """
    Pydantic model for a basic product.
    """

    product_name: str
    price: float
    quantity: int
    description: str = ""
    image: str = ""
    category: str = ""


class ProductCreate(ProductBase):
    """
    Pydantic model for creating a new product.
    """
    pass


class Product(BaseModel):
    """
    Pydantic model for a product, including identification and creation details.
    """
    product_name: str
    price: float
    quantity: int
    description: str = ""
    created_at: datetime

    class Config:
        from_attributes = True


class Farmer(BaseModel):
    """
    Pydantic model for basic farmer information.
    """

    id: str
    name: str
    email: str
    location: str
    phone: str
    products: List[Product] = []


    class Config:
        from_attributes = True


class Token(BaseModel):
    """
    Pydantic model for an access token.
    """

    access_token: str
    token_type: str = "bearer"


class FarmerResponse(BaseModel):
    """
    Pydantic model for detailed farmer information, including a list of products.
    """

    id: str
    created_at: str
    name: str
    email: str
    location: str
    phone: str
    bio: str
    products: List[Product] = []

    class Config:
        from_attributes = True


class FarmerCreate(Farmer):
    """
    Pydantic model for creating a new farmer, including email and password.
    """

    email: str
    password: str