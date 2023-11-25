from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# app.mount("/styles", StaticFiles(directory="../styles"), name="styles")
app.mount("/static", StaticFiles(directory="../static"), name="static")
# app.mount("/templates", StaticFiles(directory="../templates"), name="templates")
# app.mount("/images", StaticFiles(directory="../static/assets/images"), name="images")
# app.mount("/css", StaticFiles(directory="../css"), name="css")
# app.mount("/js", StaticFiles(directory="../js"), name="js")
# app.mount("/assets", StaticFiles(directory="../assets"), name="assets")
# app.mount("/scripts", StaticFiles(directory="../scripts"), name="scripts")
# app.mount("/icons", StaticFiles(directory="../assets/icons"), name="icons")


@app.get("/")
def index():
    return FileResponse("../index.html")

@app.get("/home")
def home():
    return FileResponse("../home.html")


if __name__ == "__main__":
    app.run(app, host="127.0.0.1", port=8000)
