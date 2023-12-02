#!/usr/bin/python3
"""this module defines the routes for the products"""
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..models.database import get_db
from ..models.farmer import Farmer as FarmerModel
from ..schemas.farmers import Farmer, FarmerCreate
# from .crud import create_product, get_products


router = APIRouter(
    prefix = '/api/v1/farmers',
    tags = ['Farmers']
)


@router.get("/", response_model=List[Farmer])
def get_farmers(db: Session = Depends(get_db)):
    try:
        farmers = db.query(FarmerModel).all()
        if farmers is None or len(farmers) == 0:
            raise HTTPException(status_code=404, detail="No farmers found. Please Join us!")
        return farmers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=Farmer)
def create_farmer(farmer: FarmerCreate, db: Session = Depends(get_db)):
    """
    Create a new farmer in the database.
    """
    try:
        # Validate the input data
        validated_farmer = FarmerCreate(**farmer.dict())

        # Check if the farmer already exists
        existing_farmer = db.query(FarmerModel).filter(FarmerModel.email == validated_farmer.email).first()
        if existing_farmer:
            raise HTTPException(status_code=400, detail="Farmer with the same email already exists")

        # Create a new FarmerModel instance and add it to the database
        try:
            db_farmer = FarmerModel(**validated_farmer.dict())
            db.add(db_farmer)
            db.commit()
            db.refresh(db_farmer)
        except Exception as e:
            db.rollback()
            print(str(e))
            raise HTTPException(status_code=500, detail=str(e))
        
        return db_farmer
    except Exception as e:
        # Handle the exception here, e.g. log the error or return an appropriate response
        db.rollback()
        raise e

    finally:
        db.close()

@router.get("/{farmer_id}", response_model=Farmer)
def get_one_farmer(farmer_id: str, db: Session = Depends(get_db)):
    one_farmer = db.query(FarmerModel).filter(FarmerModel.id == farmer_id).first()
    if not one_farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return one_farmer

