from models import User, Farmer
import pytest

class TestUser:

    # User object can be created with valid name, email, password, and location
    def test_user_creation_with_valid_inputs(self):
        user = User(name="John Doe", email="johndoe@example.com", password="password", location="New York")
        assert user.name == "John Doe"
        assert user.email == "johndoe@example.com"
        assert user.password == "password"
        assert user.location == "New York"

    # User object can return a dictionary representation of itself using to_dict() method
    # def test_user_to_dict_method(self):
    #     user = User(name="John Doe", email="johndoe@example.com", password="password", location="New York")
    #     user_dict = user.to_dict()
    #     assert isinstance(user_dict, dict)
    #     assert user_dict["name"] == "John Doe"
    #     assert user_dict["email"] == "johndoe@example.com"
    #     assert user_dict["password"] == "password"
    #     assert user_dict["location"] == "New York"

    # Farmer object can be created with valid name, email, password, location, bio, and phone
    def test_farmer_creation_with_valid_inputs(self):
        farmer = Farmer(name="John Doe", email="johndoe@example.com", password="password", location="New York", bio="I am a farmer", phone="1234567890")
        assert farmer.name == "John Doe"
        assert farmer.email == "johndoe@example.com"
        assert farmer.password == "password"
        assert farmer.location == "New York"
        assert farmer.bio == "I am a farmer"
        assert farmer.phone == "1234567890"

    # User object cannot be created without a name
    def test_user_creation_without_name(self):
        with pytest.raises(TypeError):
            user = User(email="johndoe@example.com", password="password", location="New York")

    # User object cannot be created without an email
    def test_user_creation_without_email(self):
        with pytest.raises(TypeError):
            user = User(name="John Doe", password="password", location="New York")

    # User object cannot be created without a password
    def test_user_creation_without_password(self):
        with pytest.raises(TypeError):
            user = User(name="John Doe", email="johndoe@example.com", location="New York")