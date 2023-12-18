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
        """
        Initializes a User instance with the provided attributes.

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.name = name
        self.email = self.validate_and_set_email(email)
        self.password = self.hash_password(password)
        self.location = location
        self.phone = phone

    def validate_and_set_email(self, email):
        """
        Validates the provided email address and sets it as the value of the email attribute.

        Args:
            email (str): The email address to be validated and set.

        Returns:
            str: The validated email address.

        Raises:
            ValueError: If the email is empty or invalid.
        """
        if not email:
            raise ValueError('Email is required')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError('Email is invalid')
        return email

    def hash_password(self, password):
        """
        Hashes the provided password and sets it as the value of the password attribute.

        Args:
            password (str): The password to be hashed.

        Returns:
            str: The hashed password.

        Raises:
            ValueError: If the password is empty.
        """
        if not password:
            raise ValueError('Password is required')
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """
        Verifies if the provided password matches the hashed password stored in the password attribute.

        Args:
            password (str): The password to be verified.

        Returns:
            bool: True if the provided password matches the hashed password, False otherwise.
        """
        return self.password == hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        """
        Returns a dictionary representation of the User instance.

        Returns:
            dict: A dictionary representation of the User instance, excluding any attributes that start with an underscore.
        """
        user_dict = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        return user_dict

    def __repr__(self):
        """
        Returns a string representation of the User instance.

        Returns:
            str: A string representation of the User instance, including the values of name, email, password, and location.
        """
        return f"User(name='{self.name}', email='{self.email}', password='{self.password}', location='{self.location}')"
