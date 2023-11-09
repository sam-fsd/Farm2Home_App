#!/usr/bin/python3
"""This module defines a class Farmer"""

from models.user import User


class Farmer(User):
    """This is the class definition for a Farmer object"""

    def __init__(self, name="", bio="", location="", phone="", email="", password=""):
        """This is the initialization function for a Farmer object"""
        super().__init__()
        self.name = name
        self.bio = bio
        self.location = location
        self._email = email
        self.__password = password
        self.phone = phone
        self.products = []

    @property
    def email(self):
        """This is the getter function for the email attribute"""
        return self._email

    @property
    def password(self):
        """This is the getter function for the password attribute"""
        return self.__password

    @password.setter
    def password(self, value):
        """This is the setter function for the password attribute"""
        self.__password = value
