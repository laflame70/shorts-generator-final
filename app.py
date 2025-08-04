import os
import shutil
from fastapi import FastAPI, Request, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    gameplays = os.listdir("static/gameplays")
    return templates.TemplateResponse("index.html", {"request": request, "gameplays": gameplays})

@app.post("/upload/")
async def upload_video(file: UploadFile):
    # Assicurati che la directory esista
    upload_dir = "static/gameplays"
    os.makedirs(upload_dir, exist_ok=True)

    # Prendi solo il nome base del file (evita path rischiosi)
    filename = os.path.basename(file.filename)

    file_path = os.path.join(upload_dir, filename)

    # Salva il file ricevuto
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": filename}

@app.post("/export/")
async def export(destination: str = Form(...)):
    # Qui si collegherebbero le API di Instagram, TikTok o YouTube
    return {"message": f"Video esportato su {destination}"}
