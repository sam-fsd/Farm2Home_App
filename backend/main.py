from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
