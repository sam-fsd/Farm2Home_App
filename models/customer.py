#!/usr/bin/python3
"""This module defines a class Customer"""

from models.user import User


class Customer(User):
    """Defines attributes of a customer"""

    def __init__(self, name="", location="", phone="", email="", password=""):
        """This is the initialization function for a Customer object"""
        super().__init__()
        self.name = name
        self.location = location
        self.email = email
        self.password = password
        self.phone = phone

    @property
    def email(self):
        """This is the getter function for the email attribute"""
        return self._email

    @email.setter
    def email(self, value):
        """This is the setter function for the email attribute"""
        self._email = value.lower()

    @property
    def password(self):
        """This is the getter function for the password attribute"""
        return self.__password

    @password.setter
    def password(self, value):
        """This is the setter function for the password attribute"""
        self.__password = value
