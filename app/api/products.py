#!/usr/bin/python3
"""this module defines the routes for the products"""
from typing import List
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.products import Product as ProductModel
from app.schemas.products import ProductList, ProductCreate
from app.oauth2 import get_current_user
from sqlalchemy.exc import IntegrityError


router = APIRouter(
    prefix = '/api/v1/products',
    tags = ['Products']
)


@router.post("/", response_model=ProductList)
def create_product(
    product: ProductCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        farmer = current_user.get('user')
        if farmer is None:
            raise HTTPException(status_code=404, detail="Farmer not found")

        new_product = ProductModel(product_name=product.product_name, price=product.price, farmer_id=farmer.id)
        
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Please join as Farmer. YAY!!! {e}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[ProductList])
def get_products(db: Session = Depends(get_db),
                 current_user: dict = Depends(get_current_user)):
    products = db.query(ProductModel).all()
    return products
