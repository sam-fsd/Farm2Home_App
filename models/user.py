#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime


class User:
    """This is the parent class for all users"""

    def __init__(self, name='', email='', password='', location='', phone=''):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.name = name
        self.email = email
        self.password = password
        self.location = location

    def to_dict(self):
        """This method returns a dictionary representation of a User instance"""
        user_dict = {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'name': self.name,
            'email': self.email,
            'location': self.location
        }
        return user_dict
