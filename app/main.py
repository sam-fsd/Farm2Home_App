#!/usr/bin/python3
"""Entry point of the application."""
from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api.products import router as products_router
from app.api.farmers import router as farmers_router
from app.api.auth import router as auth_router
from app.models.database import engine
from app.models import *
from app.schemas.farmers import Farmer

# initialize fastapi instance
app = FastAPI()

# initialize the database tables 
Base.metadata.create_all(bind=engine)

# call the frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/pages", StaticFiles(directory="pages"), name="pages")
app.mount("/images", StaticFiles(directory="images"), name="images")

# call the api routes
app.include_router(products_router)
app.include_router(farmers_router)
app.include_router(auth_router)


@app.get("/")
def index():
    return FileResponse("index.html")


@app.get("/home")
def home():
    """
    Returns the "home.html" file as a response.

    :return: FileResponse object serving the "home.html" file.
    """
    return FileResponse("home.html")

@app.get("/login")
def login():
    """
    Returns the "pages/login.html" file as a response.

    :return: FileResponse object serving the "pages/login.html" file.
    """
    return FileResponse("pages/login.html")

@app.get("/register")
def register():
    """
    Returns the "pages/signup.html" file as a response.

    :return: FileResponse object serving the "pages/signup.html" file.
    """
    return FileResponse("pages/signup.html")


if __name__ == "__main__":
    """
    Entry point of the application.
    
    Checks if the current module is being run as the main module and if so, starts the FastAPI application.
    
    Example Usage:
    if __name__ == "__main__":
        app.run(app, host="127.0.0.1", port=8000)
    """
    app.run(app, host="127.0.0.1", port=8000)
