#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey
from  sqlalchemy.orm import relationship
from models.database import Base
from models.user import User


class Farmer(User, Base):
    """
    A class representing a farmer.
    """

    __tablename__ = 'farmers'

    bio = Column(String(60), nullable=True)
    products = relationship("Product", backref="farmer")

    def __init__(self, name="", bio="", location="", email="", password=""):

        super().__init__(name, email, password, location)
        self.bio = bio

    def to_dict(self):

        farmer_dict = super().to_dict()
        farmer_dict['products'] = [product.to_dict() for product in self.products]
        return farmer_dict
