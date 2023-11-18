#!/usr/bin/python3
"""This module defines a class Customer"""

from models.user import User


class Customer(User):
    """Defines attributes of a customer"""

    def __init__(self, name="", location="", email="", password=""):
        """This is the initialization function for a Customer object"""
        super().__init__(name, email, password, location)
