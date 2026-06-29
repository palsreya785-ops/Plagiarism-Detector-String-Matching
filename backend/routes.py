from fastapi import APIRouter, UploadFile, File
import shutil
import os

from utils.file_reader import read_document
from services.analyzer import analyze_documents

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/analyze")
async def analyze(
    original: UploadFile = File(...),
    submitted: UploadFile = File(...)
):

    original_path = os.path.join(
        UPLOAD_FOLDER,
        original.filename
    )

    submitted_path = os.path.join(
        UPLOAD_FOLDER,
        submitted.filename
    )

    with open(original_path, "wb") as buffer:
        shutil.copyfileobj(original.file, buffer)

    with open(submitted_path, "wb") as buffer:
        shutil.copyfileobj(submitted.file, buffer)

    original_text = read_document(original_path)

    submitted_text = read_document(submitted_path)

    result = analyze_documents(
        original_text,
        submitted_text
    )

    return result