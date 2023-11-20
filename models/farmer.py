#!/usr/bin/python3
"""This module defines a class Farmer"""

from models.user import User


class Farmer(User):
    """
    A class representing a farmer.

    Attributes:
        name (str): The name of the farmer.
        bio (str): The biography of the farmer.
        location (str): The location of the farmer.
        phone (str): The phone number of the farmer.
        email (str): The email address of the farmer.
        password (str): The password of the farmer.
        products (list): A list of products associated with the farmer.
    """

    def __init__(self, name="", bio="", location="", phone="", email="", password=""):
        """
        Initializes a Farmer object.

        Args:
            name (str, optional): The name of the farmer. Defaults to an empty string.
            bio (str, optional): The biography of the farmer. Defaults to an empty string.
            location (str, optional): The location of the farmer. Defaults to an empty string.
            phone (str, optional): The phone number of the farmer. Defaults to an empty string.
            email (str, optional): The email address of the farmer. Defaults to an empty string.
            password (str, optional): The password of the farmer. Defaults to an empty string.
        """
        super().__init__(name, email, password, location)
        self.bio = bio
        self.phone = phone
        self.products = []

    def to_dict(self):
        """
        Returns a dictionary representation of a Farmer instance.

        Returns:
            dict: A dictionary representation of a Farmer instance.
        """
        farmer_dict = super().to_dict()
        farmer_dict['bio'] = self.bio
        farmer_dict['location'] = self.location
        farmer_dict['phone'] = self.phone
        farmer_dict['products'] = self.products
        return farmer_dict
