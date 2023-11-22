#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *

SQLALCHEMY_DATABASE_URL = "mysql://root:root@localhost:3306/foodbank"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

try:
    with engine.connect() as connection:
        print("Connection successful")
except Exception as e:
    print("Failed to connect to database")
    print(e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
