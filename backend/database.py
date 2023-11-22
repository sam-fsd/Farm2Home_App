#!/usr/bin/python3
"""This module connects to mysql database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/foodbank')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
