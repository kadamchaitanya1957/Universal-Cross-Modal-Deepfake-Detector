import os

from fastapi import APIRouter, UploadFile, File, HTTPException

from config import MAX_UPLOAD_SIZE, UPLOAD_CHUNK_SIZE, UPLOAD_DIR
from utils.file_validation import (
    build_stored_filename,
    is_allowed_file,
    is_extension_allowed,
)
from services.analyzer import analyze_file

router = APIRouter(
    tags=["Analyze"]
)


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not is_allowed_file(file.content_type):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    if not is_extension_allowed(file.filename, file.content_type):
        raise HTTPException(
            status_code=400,
            detail="File extension does not match its content type."
        )

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    stored_name = build_stored_filename(file.filename, file.content_type)
    file_path = os.path.join(UPLOAD_DIR, stored_name)

    written = 0

    try:
        with open(file_path, "wb") as buffer:
            while chunk := await file.read(UPLOAD_CHUNK_SIZE):
                written += len(chunk)

                if written > MAX_UPLOAD_SIZE:
                    raise HTTPException(
                        status_code=413,
                        detail="File is too large."
                    )

                buffer.write(chunk)

        result = analyze_file(file_path)
    except Exception:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise

    return {
        "filename": os.path.basename(file.filename),
        "content_type": file.content_type,
        "status": "uploaded",
        **result
    }
