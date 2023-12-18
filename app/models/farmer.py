#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..models.database import Base
from ..models.user import User


class Farmer(User, Base):
    """
    A class representing a farmer.
    """
    __tablename__ = 'farmers'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))  # Explicitly define the primary key
    bio = Column(String(60), nullable=True)
    email = Column(String(100), nullable=False, unique=True)

    products = relationship("Product", back_populates="farmer", foreign_keys="Product.farmer_id" , cascade="all, delete-orphan")

    def __init__(self, name="", bio="", location="", email="", password="", phone=""):
        """
        Initializes a Farmer object.

        """
        super().__init__(name, email, password, location, phone)
        self.bio = bio

    def to_dict(self):
        """
        Returns a dictionary representation of the Farmer object.

        Returns:
            dict: A dictionary containing the farmer's information and products.
        """
        farmer_dict = super().to_dict()
        farmer_dict['products'] = [product.to_dict() for product in self.products]
        return farmer_dict

    def get_products_by_category(self, category):
        """
        Returns a list of product dictionaries filtered by the specified category.

        Args:
            category (str): The category to filter the products by.

        Returns:
            list: A list of product dictionaries.
        """
        return [product.to_dict() for product in self.products if product.category == category]
    