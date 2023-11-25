#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey
from  sqlalchemy.orm import relationship
from database import Base

class User():
    """This is the parent class for all users
    this is not a table in the database so does
    not inherit from Base"""

    # __tablename__ = 'users'
    
    id = Column(String(60), primary_key=True, default=uuid.uuid4) # generating id attr automatically
    created_at = Column(DateTime, default=datetime.utcnow())
    name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)
    location = Column(String(60), nullable=False)
    phone = Column(String(60), nullable=False)

    def __init__(self, name='', email='', password='', location='', phone=''):
        self.created_at = datetime.now()
        self.name = name
        self.email = email
        self.password = password
        self.location = location
        self.phone = phone

    def to_dict(self):
        """This method returns a dictionary representation of a User instance"""

        #MOD: used a dictionary comprehension to make this more dynamic incase you change the model
        user_dict = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return user_dict

    def __repr__(self): # allows more informative and readable
        return f"User(name='{self.name}', email='{self.email}', password='{self.password}', location='{self.location}')"
class Product(Base):
    """This is the class definition for a Product object"""

    __tablename__ = 'products'

    product_id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    product_name = Column(String(60), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, name="", price=0, quantity=0):
        """This is the initialization function for a Product object"""
        self.product_name = name
        self.price = price
        self.quantity = quantity
    
    def to_dict(self):
        """This method returns a dictionary representation of a Product instance"""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


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


class Customer(User, Base):
    """Defines attributes of a customer"""

    __tablename__ = 'customers'

    # id = Column(String(60), ForeignKey('users.id'), primary_key=True)

    def __init__(self, name="", location="", email="", password=""):
        """This is the initialization function for a Customer object"""
        super().__init__(name, email, password, location)
