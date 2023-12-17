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
    """
    Register a new user in the API.

    Args:
        user (Union[FarmerCreate, CustomerCreate]): A user object that can be either a FarmerCreate or CustomerCreate model.
            It contains the user's name, email, and password.
        user_type (str): A string indicating the type of user to be registered. It can be either "farmer" or "customer".
        db (Session, optional): A database session object obtained from the get_db function. Defaults to Depends(get_db).

    Raises:
        HTTPException: If the email provided by the user is already registered, it raises an HTTPException with a status code of 400 and a detail message of "Email already registered".
        HTTPException: If the user_type is not valid, it raises an HTTPException with a status code of 400 and a detail message of "Invalid user type".

    Returns:
        The newly created user object, which can be either a FarmerModel or CustomerModel depending on the user type.
    """
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
    return db_user


@router.post('/token')
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticates the user and generates an access token.

    Args:
        form_data (OAuth2PasswordRequestForm): An instance of `OAuth2PasswordRequestForm` containing the username and password entered by the user.
        db (Session): An instance of `Session` representing the database session.

    Returns:
        dict: A dictionary containing the access token and the token type.

    Raises:
        HTTPException: If the user is not found or the password is invalid.
        HTTPException: If there is an error creating the access token.
    """
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
