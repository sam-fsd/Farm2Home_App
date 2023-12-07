#!/usr/bin/python3
"""This module defines a class product"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..models.database import Base
from sqlalchemy.dialects.postgresql import UUID


class Product(Base):
    """This is the class definition for a Product object"""

    __tablename__ = 'products'

    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    image = Column(String(200), nullable=True)
    description = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    product_name = Column(String(60), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    category = Column(String, nullable=True)
    farmer_id = Column(String, ForeignKey('farmers.id'), nullable=False)
    farmer = relationship("Farmer", back_populates="products", uselist=False)

    def __init__(self, product_name="", price=0, quantity=0, description="", image="", category="", farmer_id=""):
        """This is the initialization function for a Product object"""
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.image = image
        self.category = category
        self.farmer_id = farmer_id
        
    def to_dict(self):
        """This method returns a dictionary representation of a Product instance"""
        return {key: getattr(self, key) for key in self.__dict__.keys() if not key.startswith('_')}
