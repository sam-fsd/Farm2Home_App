#!/usr/bin/python3
"""This module defines a class Product"""

from datetime import datetime
import uuid


class Product():
    """This is the class definition for a Product object"""

    def __init__(self, name="", price=0, quantity=0):
        """This is the initialization function for a Product object"""
        self.product_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.product_name = name
        self.price = price
        self.quantity = quantity
