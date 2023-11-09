#!/usr/bin/python3

from models.customer import Customer

customer = Customer("Sam", "Ruiru", "0712345678", "test@test.com")

print(customer.to_dict())
