from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api.products import router as products_router
from app.api.farmers import router as farmers_router
from app.models.database import engine
from app.models import *
from app.schemas.farmers import Farmer

app = FastAPI()
# Add this code to initialize the database tables
Base.metadata.create_all(bind=engine)

# call the frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")


# call the api routes
app.include_router(products_router)
app.include_router(farmers_router)



@app.get("/")
def index():
    return FileResponse("index.html")


@app.get("/home")
def home():
    return FileResponse("home.html")


if __name__ == "__main__":
    app.run(app, host="127.0.0.1", port=8000)
