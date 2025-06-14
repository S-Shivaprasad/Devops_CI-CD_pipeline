from typing import Optional
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import json
import requests

from services.parser import parse_ci_file
from services.analyzer import analyze_pipeline
from models.llm_helper import ask_llm

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 🔍 Process pipeline from file path
def process_pipeline(file_path: str):
    try:
        print(f"📥 Processing file: {file_path}")
        pipeline_data = parse_ci_file(file_path)
        analysis = analyze_pipeline(pipeline_data)

        issue_summary = json.dumps({
            "pipeline": pipeline_data,
            "analysis": analysis
        }, indent=2)

        llm_response = ask_llm(issue_summary)

        return {
            "pipeline": pipeline_data,
            "analysis": analysis,
            "llm_response": llm_response
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "error": "Processing failed",
            "details": str(e)
        }

# 📦 Unified endpoint: supports file or URL
@app.post("/upload/")
async def upload_ci_file(
    file: Optional[UploadFile] = File(None),
    url: Optional[str] = Form(None)
):
    if file and url:
        return JSONResponse(
            {"error": "Please provide either a file or a URL, not both."},
            status_code=422
        )

    try:
        if file:
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            with open(file_path, "wb") as f:
                content = await file.read()
                f.write(content)

        elif url:
            response = requests.get(url)
            if response.status_code != 200:
                return JSONResponse({"error": "Failed to fetch file from URL"}, status_code=400)

            filename = os.path.basename(url.split("?")[0]) or "pipeline_from_url.yaml"
            if not filename.endswith((".yml", ".yaml")):
                filename += ".yaml"

            file_path = os.path.join(UPLOAD_DIR, filename)
            with open(file_path, "wb") as f:
                f.write(response.content)

        else:
            return JSONResponse({"error": "No file or URL provided."}, status_code=400)

        result = process_pipeline(file_path)
        return JSONResponse(result)

    except Exception as e:
        print(f"[❌ Backend Error] {e}")
        return JSONResponse({"error": f"Internal server error: {str(e)}"}, status_code=500)
