#!/usr/bin/python3
"""this module defines the routes for the products"""
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..models.database import get_db
from ..models.farmer import Farmer as FarmerModel
from ..schemas.farmers import Farmer
# from .crud import create_product, get_products
from ..oauth2 import get_current_user


router = APIRouter(
    prefix = '/api/v1/farmers',
    tags = ['Farmers']
)


@router.get("/", response_model=List[Farmer])
def get_farmers(db: Session = Depends(get_db)):
    farmers = db.query(FarmerModel).all()
    return farmers


@router.get("/{farmer_id}", response_model=Farmer)
def get_one_farmer(farmer_id: str, db: Session = Depends(get_db)):
    one_farmer = db.query(FarmerModel).filter(FarmerModel.id == farmer_id).first()
    if not one_farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return one_farmer

#TODO: Add the following to app/api/farmers.py:
# fetch specific farmer details e.g phone
