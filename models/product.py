#!/usr/bin/python3
"""This module defines a class Product"""

from models.user import User


class Product(User):
    """This is the class definition for a Product object"""

    def __init__(self, name="", price=0, quantity=0):
        """This is the initialization function for a Product object"""
        super().__init__()
        self.product_name = name
        self.price = price
        self.quantity = quantity
