from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *

Base = declarative_base()

# Change the database URL accordingly
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:root@localhost:3306/foodbank"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Create tables
Base.metadata.create_all(bind=engine, checkfirst=True)

# SessionLocal will be used to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.bind = engine

try:
    with engine.connect() as connection:
        print("Connection successful")
except Exception as e:
    print("Failed to connect to database")
    print(e)
