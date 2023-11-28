#!/usr/bin/python3
"""this module defines the routes for the products"""
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..models.database import get_db
from ..models.products import Product as ProductModel
from ..schemas.products import Product
# from .crud import create_product, get_products


router = APIRouter(
    prefix = '/api/v1/products',
    tags = ['Products']
)

@router.get("/", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products
