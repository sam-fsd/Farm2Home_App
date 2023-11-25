#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey
from  sqlalchemy.orm import relationship
from models.database import Base
from user import User


class Customer(User, Base):
    """Defines attributes of a customer"""

    __tablename__ = 'customers'

    # id = Column(String(60), ForeignKey('users.id'), primary_key=True)

    def __init__(self, name="", location="", email="", password=""):
        """This is the initialization function for a Customer object"""
        super().__init__(name, email, password, location)