#!/usr/bin/python3
"""authenticates users"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.farmer import Farmer as FarmerModel
from app.models.customer import Customer as CustomerModel
from app.schemas.user import FarmerCreate, CustomerCreate
from typing import Union
from app.oauth2 import create_access_token
from app.config import settings
from jose import JWTError
from fastapi import HTTPException
from fastapi.responses import RedirectResponse


router = APIRouter(
    prefix = '/api/v1/auth',
    tags = ['Authentication']
)

@router.post('/register')
def register(user: Union[FarmerCreate, CustomerCreate],
             user_type: str, db: Session = Depends(get_db)):
    print(user_type)
    print(user)

    # Check if the email is unique in the specific table
    existing_farmer = db.query(FarmerModel).filter(FarmerModel.email == user.email).first()
    existing_customer = db.query(CustomerModel).filter(CustomerModel.email == user.email).first()

    if existing_farmer or existing_customer:
        raise HTTPException(status_code=400, detail="Email already registered")

    if user_type == "farmer":
        db_user = FarmerModel(**user.dict())
    elif user_type == "customer":
        db_user = CustomerModel(**user.dict())
    else:
        raise HTTPException(status_code=400, detail="Invalid user type")

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user)
    # Redirect to the login page
    return RedirectResponse(url="../../pages/login.html")


@router.post('/token')
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(FarmerModel).filter(FarmerModel.email == form_data.username).first()
    print("user:", user)

    if not user:
        user = db.query(CustomerModel).filter(CustomerModel.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")

    if not user.verify_password(form_data.password):
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    try:
        access_token = create_access_token(data={"sub": user.email,
                                                 "exp": settings.access_token_expire_minutes,
                                                 "user_type": user.__class__.__name__})
        return {"access_token": access_token, "token_type": "bearer"}    
    except JWTError as e:
        raise HTTPException(status_code=500, detail="Error creating access token") from e
