from pydantic import BaseModel
from typing import Optional

class PDFResponse(BaseModel):
    pdf_id: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str