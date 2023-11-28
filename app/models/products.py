#!/usr/bin/python3
"""This module defines a class product"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..models.database import Base


class Product(Base):
    """This is the class definition for a Product object"""

    __tablename__ = 'products'

    product_id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    image = Column(String(200), nullable=True)
    description = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    product_name = Column(String(60), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    category = Column(String, nullable=True)
    farmer_id = Column(String, ForeignKey('farmers.id'))

    def __init__(self, name="", price=0, quantity=0, description="", image="", category=""):
        """This is the initialization function for a Product object"""
        self.product_name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.image = image
        self.category = category
        
    def to_dict(self):
        """This method returns a dictionary representation of a Product instance"""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
