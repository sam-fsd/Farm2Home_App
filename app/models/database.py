from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import settings
from app.models import *

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Creates a database session and provides it to the caller.

    Returns:
        generator: A generator that yields the session object.

    Example Usage:
        with get_db() as db:
            # Use the session 'db' to perform database operations
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
