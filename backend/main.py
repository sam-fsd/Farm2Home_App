from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import *


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
