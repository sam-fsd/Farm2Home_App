#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
import re
import hashlib
from ..models.database import Base

class User():
    """This is the parent class for all users
    this is not a table in the database so does
    not inherit from Base"""

    id = Column(String(60), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow())
    name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(100), nullable=False)
    location = Column(String(60), nullable=False)
    phone = Column(String(60), nullable=False)

    def __init__(self, name='', email='', password='', location='', phone=''):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.name = name
        self.email = self.validate_and_set_email(email)
        self.password = self.hash_password(password)
        self.location = location
        self.phone = phone

    def validate_and_set_email(self, email):
        if not email:
            raise ValueError('Email is required')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError('Email is invalid')
        return email

    def hash_password(self, password):
        if not password:
            raise ValueError('Password is required')
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        """This method returns a dictionary representation of a User instance."""
        user_dict = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        return user_dict

    def __repr__(self):  # allows more informative and readable
        return f"User(name='{self.name}', email='{self.email}', password='{self.password}', location='{self.location}')"
