#!/usr/bin/python3
"""this module defines the routes for the products"""
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..models.database import get_db
from ..models.products import Product as FarmerModel
from ..schemas.farmers import FarmerCreate, FarmerResponse
# from .crud import create_product, get_products


router = APIRouter(
    prefix = '/api/v1/farmers',
    tags = ['Farmers']
)

@router.post("/", response_model=FarmerResponse)
def create_farmer(farmer: FarmerCreate, db: Session = Depends(get_db)):
    db_farmer = FarmerModel(**farmer.dict())
    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)
    return db_farmer.to_dict()

