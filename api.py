# api.py

from fastapi import APIRouter, UploadFile, File
from services import save_pdf, get_pdf_content, generate_response
from models import PDFResponse, ChatRequest, ChatResponse

router = APIRouter()

@router.post("/v1/pdf", response_model=PDFResponse)
async def upload_file(file: UploadFile = File(...)):
    pdf_id = save_pdf(file)
    return PDFResponse(pdf_id=pdf_id)

@router.post("/v1/chat/{pdf_id}", response_model=ChatResponse)
async def chat(pdf_id: str, message: ChatRequest):
    pdf_content = get_pdf_content(pdf_id)
    response = await generate_response(pdf_content, message.message)
    return ChatResponse(response=response)
