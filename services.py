import os
import uuid
from fastapi import HTTPException
from pdfminer.high_level import extract_text
from starlette.responses import JSONResponse
import requests
from dotenv import load_dotenv
from models import PDFResponse, ChatRequest, ChatResponse

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def generate_unique_pdf_id():
    return str(uuid.uuid4())


def save_pdf(file):
    pdf_id = generate_unique_pdf_id()
    file_location = f"./pdfs/{pdf_id}.pdf"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return pdf_id


def get_pdf_content(pdf_id):
    try:
        text = extract_text(f"./pdfs/{pdf_id}.pdf")
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail="The PDF content could not be extracted.")


async def generate_response(pdf_content, user_message):
    url = "https://api.yourgemini.com/generate"
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "content": pdf_content,
        "query": user_message,
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get("result")
    else:
        raise HTTPException(status_code=response.status_code, detail="The Gemini API call failed.")