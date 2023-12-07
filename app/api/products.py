#!/usr/bin/python3
"""this module defines the routes for the products"""
from typing import List
from fastapi import HTTPException, Depends, APIRouter, UploadFile, File
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
        raise HTTPException(status_code=400, detail="Duplicate product or other integrity error")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[ProductList])
def get_products(db: Session = Depends(get_db),
                 current_user: dict = Depends(get_current_user)):
    products = db.query(ProductModel).all()
    return products


@router.post("/upload-image/{product_id}")
def upload_image(product_id: str, file: UploadFile = File(...),
                 current_user: dict = Depends(get_current_user),
                 db: Session = Depends(get_db)):
    try:
        # Check if the current user is a farmer
        if current_user['user_type'] != 'Farmer':
            raise HTTPException(status_code=403, detail="Only farmers can upload images")

        # Check if the product_id exists in the database
        product = db.query(ProductModel).filter(ProductModel.product_id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        # Save the image to a folder or cloud storage, and update the product model with the image URL
        # For simplicity, let's assume you have an 'images' folder in your project directory
        image_path = f"images/{product_id}_{file.filename}"
        with open(image_path, "wb") as image_file:
            image_file.write(file.file.read())

        # Update the product model with the image URL
        product.image = image_path
        db.commit()

        return {"message": "Image uploaded successfully", "image_url": image_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
