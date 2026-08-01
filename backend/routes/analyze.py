
import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(
    tags=["Analyze"]
)

UPLOAD_DIR = "uploads"


@router.post("/analyze")
async def analyze(file: UploadFile = File(None)):
    if file is None:
        raise HTTPException(status_code=400, detail="No file provided")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "uploaded"
    }

