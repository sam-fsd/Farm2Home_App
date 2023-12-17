#!/usr/bin/python3
"""this defines the authentication module"""
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from app.config import settings
from app.models.database import get_db
from sqlalchemy.orm import Session
from app.models.farmer import Farmer as FarmerModel
from app.models.customer import Customer as CustomerModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(*, data: dict):
    """
    Creates an access token by encoding the provided data dictionary.

    Args:
        data (dict): A dictionary containing the data to be encoded in the access token. It should have the keys "exp" (expiration time in minutes), "sub" (user identifier), and "user_type" (type of user).

    Returns:
        str: The encoded access token as a string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=to_encode.pop("exp"))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Retrieves the current user based on the provided access token.

    Args:
        token (str): The encoded access token.
        db (Session): The database session.

    Returns:
        dict: A dictionary containing the user object and the user type.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub: str = payload.get("sub")
        user_type: str = payload.get("user_type")

        print("payload: ", payload)
        print("user_type: ", user_type)

        if user_type == 'Farmer':
            user = db.query(FarmerModel).filter(FarmerModel.email == sub).first()
        elif user_type == 'Customer':
            user = db.query(CustomerModel).filter(CustomerModel.email == sub).first()
        else:
            raise credentials_exception

        if user is None:
            raise credentials_exception

        return {"user": user, "user_type": user_type}

    except JWTError:
        raise credentials_exception
