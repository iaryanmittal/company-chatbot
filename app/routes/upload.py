# app/routes/upload.py

from fastapi import APIRouter
from fastapi import UploadFile, File
import uuid
import shutil
from app.services.rag_service import ingest_chunks
import os

from app.services.pdf_service import (
    extract_text,
    create_chunks
)

router = APIRouter()


@router.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):

    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{uuid.uuid4()}.pdf"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    chunks = create_chunks(text)

    stored_chunks = ingest_chunks(
        chunks,
        file.filename
    )

    return {
        "characters": len(text),
        "chunks": len(chunks),
        "stored_chunks": stored_chunks
    }