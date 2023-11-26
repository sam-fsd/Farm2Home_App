#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime


class User():
    """This is the parent class for all users
    this is not a table in the database so does
    not inherit from Base"""

    # __tablename__ = 'users'

    id = Column(String(60), primary_key=True, default=uuid.uuid4)  # generating id attr automatically
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

        # MOD: used a dictionary comprehension to make this more dynamic incase you change the model
        user_dict = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return user_dict

    def __repr__(self):  # allows more informative and readable
        return f"User(name='{self.name}', email='{self.email}', password='{self.password}', location='{self.location}')"
