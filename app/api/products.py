#!/usr/bin/python3
"""this module defines the routes for the products"""
from typing import List
from fastapi import HTTPException, Depends, APIRouter, File, UploadFile, Form
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.products import Product as ProductModel
from app.models.farmer import Farmer as FarmerModel
from app.schemas.products import ProductList, ProductCreate
from app.oauth2 import get_current_user
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix = '/api/v1/products',
    tags = ['Products']
)


@router.post("/", response_model=ProductList)
def create_product(
    # product: ProductCreate,
    product_name: str = Form(...),
    price: float = Form(...),
    description: str = Form(None),
    quantity: int = Form(...),
    category: str = Form(...),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
    image: UploadFile = File(...)
):
    try:
        farmer = current_user.get('user')
        if farmer is None:
            raise HTTPException(status_code=404, detail="Farmer not found")
        
        if not image.filename:
            raise HTTPException(status_code=400, detail="Image is required")
        
        image_path = f"images/{image.filename}"
        with open(image_path, "wb") as f:
            f.write(image.file.read())

        new_product = ProductModel(product_name=product_name,
                                   price=price,
                                   farmer_id=farmer.id,
                                    description=description,
                                    quantity=quantity,
                                    category=category,
                                   image=image_path)
        
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
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products

@router.get("/{product_id}", response_model=ProductList)
def get_one_product(product_id: str, db: Session = Depends(get_db)):
    one_product = db.query(ProductModel).filter(ProductModel.product_id==product_id).first()
    if not one_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return one_product

@router.get("/search/{product_name}", response_model=List[ProductList])
def search_product(product_name: str, db: Session = Depends(get_db)):
    products = db.query(ProductModel).filter(ProductModel.product_name.ilike(f'%{product_name}%')).all()
    if not products:
        raise HTTPException(status_code=404, detail="Product not found")
    return products

@router.get("/{product_id}/location", response_model=str)
def get_farmer_location(product_id: str, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.product_id==product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    farmer = db.query(FarmerModel).filter(FarmerModel.id == product.farmer_id).first()
    if not farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return farmer.location

@router.get("/{product_id}/phone", response_model=str)
def get_farmer_phone(product_id: str, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.product_id==product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    farmer = db.query(FarmerModel).filter(FarmerModel.id == product.farmer_id).first()
    if not farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return farmer.phone
