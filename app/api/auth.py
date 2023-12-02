#!/usr/bin/python3
"""authenticates users"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models import User
from app.schemas.user import Token
from app.oauth2 import create_access_token

router = APIRouter(
    prefix = '/api/v1/auth',
    tags = ['Authentication']
)

@router.post("/login", response_model=Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    if not user.verify_password(request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    access_token = create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type":"bearer"}
