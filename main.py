import os
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
import fitz  # PyMuPDF

UPLOAD_DIR = "/home/pinar/pdf-chat-api/pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

def extract_text_from_pdf(pdf_path: str) -> str:
    document = fitz.open(pdf_path)
    text = ""
    for page in document:
        text += page.get_text()
    return text

@app.post("/v1/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(pdf_path, "wb") as f:
        f.write(await file.read())
    return {"pdf_id": file.filename}

@app.post("/v1/chat/{pdf_id}")
async def chat_with_pdf(pdf_id: str, message: dict):
    pdf_path = os.path.join(UPLOAD_DIR, f"{pdf_id}")

    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=404, detail="PDF not found.")

    pdf_text = extract_text_from_pdf(pdf_path)

    user_message = message['message']
    response = f"Your question: {user_message}\nPDF Text: {pdf_text[:100]}..."
    return JSONResponse(content={"response": response})