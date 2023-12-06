#!/usr/bin/python3
"""this module defines the routes for the products"""
from typing import Tuple
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.user import User as UserModel
from app.models.products import Product as ProductModel
from app.models.farmer import Farmer as FarmerModel
from app.schemas.products import ProductList, ProductCreate
from app.oauth2 import get_current_user, oauth2_scheme
from .dependencies import get_current_active_farmer
from app import oauth2


router = APIRouter(
    prefix = '/api/v1/products',
    tags = ['Products']
)
 

@router.post("/")
def create_product(
    product: ProductCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    sub = current_user.get("sub")
    user_type = current_user.get("user_type")

    if user_type != "Farmer":
        raise HTTPException(status_code=403, detail="Only farmers can create products")

    # Create the product instance
    db_product = ProductModel(**product.dict(), farmer_email=sub)

    # Add the product to the database
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
    

@router.get("/", response_model=ProductList)
def get_products(db: Session = Depends(get_db)):
    try:
        products = db.query(ProductModel).all()
        if products is None or len(products) == 0:
            raise HTTPException(status_code=404, detail="No products found. Please add some!")
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# #NOTE: This is not working

# @router.post("/", response_model=Product)
# def create_product(farmer_id: str, product: ProductCreate, db: Session = Depends(get_db),
#                    current_user: str = Depends(get_current_user)):
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
