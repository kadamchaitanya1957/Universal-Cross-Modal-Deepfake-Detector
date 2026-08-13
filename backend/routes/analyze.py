import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.file_validation import is_allowed_file
from services.analyzer import analyze_file

router = APIRouter(
    tags=["Analyze"]
)

UPLOAD_DIR = "uploads"


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not is_allowed_file(file.content_type):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_file(file_path)

    return {
    "filename": file.filename,
    "content_type": file.content_type,
    "status": "uploaded",
    **result
}