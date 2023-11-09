#!/usr/bin/python3
"""This module defines a class User"""
import uuid
from datetime import datetime


class User:
    """This is the parent class for all users"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def to_dict(self):
        """This method returns a dictionary representation of a User instance"""
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict
