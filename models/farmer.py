#!/usr/bin/python3
"""This module defines a class Farmer"""

from models.user import User


class Farmer(User):
    """This is the class definition for a Farmer object"""

    def __init__(self, name="", bio="", location="", phone="", email="", password=""):
        """This is the initialization function for a Farmer object"""
        super().__init__(name, email, password, location)
        self.bio = bio
        self.phone = phone
        self.products = []

    def to_dict(self):
        farmer_dict = super().to_dict()
        farmer_dict['bio'] = self.bio
        farmer_dict['location'] = self.location
        farmer_dict['phone'] = self.phone
        farmer_dict['products'] = self.products
        return farmer_dict
