#!/usr/bin/python3
"""this defines the authentication module"""
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.database import get_db
from models.user import User as UserModel
from schemas.user import Token, TokenData
from fastapi.security import OAuth2PasswordBearer
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY = {settings.secret_key}
ALGORITHM = {settings.algorithm}
ACCESS_TOKEN_EXPIRE_MINUTES = {settings.access_token_expire_minutes}


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(user_id=id)
    except JWTError as e:
        print(e)
        raise credentials_exception
    return token_data


def get_current_user(token_data: TokenData = Depends(verify_access_token), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token=token_data.access_token, credentials_exception=credentials_exception)
    user = db.query(UserModel).filter(UserModel.id == token.user_id).first()
    if user is None:
        raise credentials_exception
    return user
