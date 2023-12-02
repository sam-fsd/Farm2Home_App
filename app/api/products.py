#!/usr/bin/python3
"""this module defines the routes for the products"""
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..models.database import get_db
from ..models.products import Product as ProductModel
from ..models.farmer import Farmer as FarmerModel
from ..schemas.products import Product, ProductCreate
# from .crud import create_product, get_products


router = APIRouter(
    prefix = '/api/v1/products',
    tags = ['Products']
)
 

@router.get("/", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    try:
        products = db.query(ProductModel).all()
        if products is None or len(products) == 0:
            raise HTTPException(status_code=404, detail="No products found. Please add some!")
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{farmer_id}/products", response_model=List[Product])
def get_farmer_products(farmer_id: str, db: Session = Depends(get_db)):
    farmer = db.query(FarmerModel).filter(FarmerModel.id == farmer_id).first()
    if not farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")

    products = db.query(ProductModel).filter(ProductModel.farmer_id == farmer_id).all()
    return products

#NOTE: This is not working

# @router.post("/", response_model=Product)
# def create_product(product: ProductCreate, db: Session = Depends(get_db)):
#     try:
#         farmer = db.query(FarmerModel).filter(FarmerModel.id == product.farmer_id).first()
#         if not farmer:
#             raise HTTPException(status_code=404, detail="Farmer not found")

#         new_product = ProductModel(name=product.name, price=product.price, farmer_id=product.farmer_id)
#         db.add(new_product)
#         db.commit()
#         db.refresh(new_product)
#         return new_product
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
