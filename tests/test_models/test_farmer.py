import unittest


class TestFarmer(unittest.TestCase):

    # Creating a Farmer object with all required parameters should return a valid instance.
    def test_create_farmer_with_required_parameters(self):
        farmer = Farmer(name="John Doe", bio="I am a farmer", location="Farmville",
                        phone="1234567890", email="john@example.com", password="password")
        self.assertIsInstance(farmer, Farmer)

    # A Farmer object should have a bio, phone, and products list that can be accessed and modified.
    def test_farmer_attributes(self):
        farmer = Farmer(name="John Doe", bio="I am a farmer", location="Farmville",
                        phone="1234567890", email="john@example.com", password="password")
        self.assertEqual(farmer.bio, "I am a farmer")
        self.assertEqual(farmer.phone, "1234567890")
        farmer.bio = "I love farming"
        farmer.phone = "9876543210"
        self.assertEqual(farmer.bio, "I love farming")
        self.assertEqual(farmer.phone, "9876543210")

    # Calling the to_dict() method on a Farmer object should return a dictionary representation of the object with all attributes.
    def test_to_dict_method(self):
        farmer = Farmer(name="John Doe", bio="I am a farmer", location="Farmville",
                        phone="1234567890", email="john@example.com", password="password")
        farmer_dict = farmer.to_dict()
        self.assertIsInstance(farmer_dict, dict)
        self.assertEqual(farmer_dict['name'], "John Doe")
        self.assertEqual(farmer_dict['bio'], "I am a farmer")
        self.assertEqual(farmer_dict['location'], "Farmville")
        self.assertEqual(farmer_dict['phone'], "1234567890")

    # Creating a Farmer object with no parameters should still return a valid instance with default values.
    def test_create_farmer_with_no_parameters(self):
        farmer = Farmer()
        self.assertIsInstance(farmer, Farmer)
        self.assertEqual(farmer.bio, "")
        self.assertEqual(farmer.phone, "")

    # Adding a product to a Farmer's products list with an invalid name or price should raise an error.
    # def test_add_product_with_invalid_name_or_price(self):
    #     farmer = Farmer(name="John Doe", bio="I am a farmer", location="Farmville", phone="1234567890", email="john@example.com", password="password")
    #     with self.assertRaises(ValueError):
    #         farmer.add_product(name="", price=10)
    #     with self.assertRaises(ValueError):
    #         farmer.add_product(name="Apple", price=-5)
