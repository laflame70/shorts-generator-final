
from fastapi import FastAPI, Request, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    gameplays = os.listdir("static/gameplays")
    return templates.TemplateResponse("index.html", {"request": request, "gameplays": gameplays})

@app.post("/upload/")
async def upload_video(file: UploadFile):
    with open(f"static/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

# Endpoint fittizi per simulare export
@app.post("/export/")
async def export(destination: str = Form(...)):
    # Qui si collegherebbero le API di Instagram, TikTok o YouTube
    return {"message": f"Video esportato su {destination}"}
