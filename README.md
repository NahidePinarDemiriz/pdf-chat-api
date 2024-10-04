# PDF Chat API

PDF Chat API is a FastAPI application that allows users to upload and chat with PDF files. This project demonstrates the integration of external services (e.g., LLM API like Google Gemini) and efficient PDF content extraction for interactive conversations.  
### Project Overview

This project showcases a RESTful API where users can:

    Upload PDF documents.
    Query a chat interface to ask questions based on the content of the uploaded PDFs.

## Features

    Upload PDFs: Efficiently upload and store PDFs while extracting their text and metadata.
    LLM Integration: Use Google Gemini API (or other LLMs) to process natural language queries based on the PDF content.
    State Management: Store the extracted text, manage sessions, and maintain a robust error handling mechanism.
    Scalability: Optimized for large PDFs and concurrent requests.

## Requirements

Before running the project, make sure you have the following dependencies installed:

    Python 3.8+
    FastAPI
    Uvicorn
    PyPDF2
    python-dotenv
    requests (for API integration with Gemini or another LLM)

## Setup Instructions
### 1. Clone the Repository
`git clone https://github.com/your-username/pdf-chat-api.git
cd pdf-chat-api`
### 2. Create a Virtual Environment
`python3 -m venv venv`  
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`
### 3. Install Dependencies
`pip install -r requirements.txt`
### 4. Set Up Environment Variables
#### Create a .env file in the root directory and add your Google Gemini API key:
`touch .env`
#### In the .env file:
GEMINI_API_KEY=GEMINI_KEY
### 5. Running the Application
`uvicorn main:app --reload`
#### The application will now be running at http://127.0.0.1:8000.
### 6. Endpoints
#### Upload PDF

    Method: POST   
    Endpoint: /v1/pdf    
    Description: Upload a PDF file for processing.  
#### Example:
`curl -X POST "http://127.0.0.1:8000/v1/pdf" -F "file=@/home/pinar/pdf-chat-api/pdfs/ai-tecuci-WIRE.pdf"`
#### Response:
`{"pdf_id":"ai-tecuci-WIRE.pdf"}`
### Chat with PDF  
     Method: POST  
     Endpoint: /v1/chat/{pdf_id}  
     Description: Send a message to chat with the content of a specific PDF.  
`curl -X POST "http://127.0.0.1:8000/v1/chat/ai-tecuci-WIRE.pdf" -H "Content-Type: applicatiCan you show me the text content?."}'w me the text content?."}'`
#### Response:
`{
  "response": ".."
}`
