#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.user import User


class Customer(User, Base):
    """Defines attributes of a customer"""

    __tablename__ = 'customers'

    def __init__(self, name="", location="", email="", password="", phone=""):
        """This is the initialization function for a Customer object"""
        super().__init__(name, email, password, location, phone)
