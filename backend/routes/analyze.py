import logging
import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.file_validation import is_allowed_file
from services.analyzer import AnalysisError, analyze_file

logger = logging.getLogger(__name__)

router = APIRouter(
    tags=["Analyze"]
)

UPLOAD_DIR = "uploads"


def _remove_partial_upload(file_path: str) -> None:
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass
    except OSError:
        logger.warning("Could not clean up partial upload %s", file_path, exc_info=True)


def _safe_filename(filename: str | None) -> str:
    name = os.path.basename(filename or "").strip()
    if not name or name in {".", ".."}:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file must have a valid filename."
        )
    return name


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not is_allowed_file(file.content_type):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    filename = _safe_filename(file.filename)

    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)
    except OSError:
        logger.exception("Could not create upload directory %s", UPLOAD_DIR)
        raise HTTPException(
            status_code=500,
            detail="Upload storage is unavailable."
        )

    file_path = os.path.join(UPLOAD_DIR, filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except OSError:
        logger.exception("Could not store uploaded file %s", filename)
        _remove_partial_upload(file_path)
        raise HTTPException(
            status_code=500,
            detail="Uploaded file could not be stored."
        )
    finally:
        await file.close()

    try:
        result = analyze_file(file_path)
    except AnalysisError as exc:
        logger.error("Analysis failed for %s: %s", filename, exc.message)
        raise HTTPException(status_code=exc.status_code, detail=exc.message)

    return {
        "filename": filename,
        "content_type": file.content_type,
        "status": "uploaded",
        **result
    }
