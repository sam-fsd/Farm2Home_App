#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base


class User():
    """This is the parent class for all users"""

    # __tablename__ = 'users'
    
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)
    location = Column(String(60), nullable=False)

    def __init__(self, name='', email='', password='', location='', phone=''):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.name = name
        self.email = email
        self.password = password
        self.location = location

    def to_dict(self):
        """This method returns a dictionary representation of a User instance"""

        #MOD: used a dictionary comprehension to make this more dynamic incase you change the model
        user_dict = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return user_dict
