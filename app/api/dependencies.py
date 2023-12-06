#!/usr/bin/python3
"""this module defines the dependecies for the users"""
from fastapi import Depends, HTTPException, status
from app.models.user import User as UserModel
from app.models.farmer import Farmer as FarmerModel
from app.models.customer import Customer as CustomerModel
from app.oauth2 import get_current_user

def get_current_active_user(current_user: UserModel = Depends(get_current_user)):
    if current_user.is_active:
        return current_user
    raise HTTPException(status_code=400, detail="Inactive user")

def get_current_active_farmer(current_user: FarmerModel = Depends(get_current_user)):
    if current_user.is_farmer:
        return current_user
    raise HTTPException(status_code=400, detail="Only farmers can access this route")

def get_current_active_customer(current_user: CustomerModel = Depends(get_current_user)):
    if current_user.is_customer:
        return current_user
    raise HTTPException(status_code=400, detail="Only customers can access this route")