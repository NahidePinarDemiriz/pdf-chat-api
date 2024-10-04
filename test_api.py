import requests

pdf_file_path = '/home/pinar/pdf-chat-api/pdfs/ai-tecuci-WIRE.pdf'

with open(pdf_file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post("http://127.0.0.1:8001/v1/pdf", files=files)

if response.status_code == 200:
    pdf_id = response.json()['pdf_id']
    print(f"PDF başarıyla yüklendi. pdf_id: {pdf_id}")
else:
    print(f"PDF yükleme hatası: {response.json()}")
