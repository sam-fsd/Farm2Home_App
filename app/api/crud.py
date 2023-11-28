#!/usr/bin/python3
"""this module defines the crud operations for the models"""
from sqlalchemy.orm import Session
from ..models.products import Product as DBProduct
from ..schemas.products import ProductCreate

