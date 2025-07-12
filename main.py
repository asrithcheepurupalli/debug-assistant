from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def analyze_file(request: Request, file: UploadFile = File(...)):
    try:
        content = await file.read()
        decoded = content.decode("utf-8")

        prompt = (
            "You are a helpful AI assistant. A developer has pasted a log or Python error:\n\n"
            f"{decoded}\n\n"
            "Summarize the issue and suggest a possible fix in clear steps."
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert Python developer and debugger."},
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content.strip()

        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": result
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": f"Something went wrong: {e}"
        })