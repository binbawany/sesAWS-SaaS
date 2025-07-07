from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import csv, io
from email_utils import send_email
from ai_utils import generate_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_contacts(file: UploadFile = File(...)):
    content = await file.read()
    reader = csv.DictReader(io.StringIO(content.decode()))
    contacts = [row for row in reader]
    return {"contacts": contacts}

@app.post("/send-email")
async def send_outreach(name: str = Form(...), email: str = Form(...)):
    subject, body = generate_email(name)
    send_email(to=email, subject=subject, body=body)
    return {"status": "Email sent"}