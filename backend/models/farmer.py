#!/usr/bin/python3
"""This module defines a class Farmer"""

from models.user import User
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base

class Farmer(User, Base):
    """
    A class representing a farmer.
    """

    __tablename__ = 'farmers'

    farmer_id = Column(String(60), ForeignKey('users.id'), primary_key=True)
    bio = Column(String(60), nullable=False)
    phone = Column(String(60), nullable=False)
    products = relationship("Product", backref="farmer")

    def __init__(self, name="", bio="", location="", phone="", email="", password=""):

        super().__init__(name, email, password, location)
        self.bio = bio
        self.phone = phone
        # self.products = []

    def to_dict(self):

        #MOD: used a dictionary comprehension to make this more dynamic incase you change the model
        farmer_dict = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        farmer_dict['products'] = [product.to_dict() for product in self.products]
        return farmer_dict
