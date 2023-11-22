#!/usr/bin/python3
"""This module defines a class Customer"""

from models.user import User
from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime

class Customer(User):
    """Defines attributes of a customer"""

    __tablename__ = 'customers'

    id = Column(String(60), ForeignKey('users.id'), primary_key=True)

    def __init__(self, name="", location="", email="", password=""):
        """This is the initialization function for a Customer object"""
        super().__init__(name, email, password, location)
