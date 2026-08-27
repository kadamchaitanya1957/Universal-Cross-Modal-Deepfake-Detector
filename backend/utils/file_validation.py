import os
import uuid

ALLOWED_MIME_TYPES = {
    # Images
    "image/jpeg": {".jpg", ".jpeg"},
    "image/png": {".png"},
    "image/webp": {".webp"},

    # Videos
    "video/mp4": {".mp4"},
    "video/quicktime": {".mov"},
    "video/x-msvideo": {".avi"},

    # Audio
    "audio/mpeg": {".mp3"},
    "audio/wav": {".wav"},
    "audio/x-wav": {".wav"},
    "audio/mp4": {".m4a", ".mp4"},

    # Documents
    "application/pdf": {".pdf"},
}


def is_allowed_file(content_type: str | None) -> bool:
    """
    Returns True if the uploaded file's MIME type is supported.
    Returns False otherwise.
    """

    if not content_type:
        return False

    return content_type in ALLOWED_MIME_TYPES


def is_extension_allowed(filename: str | None, content_type: str | None) -> bool:
    """
    Returns True if the filename extension matches the declared MIME type.
    """

    if not filename or not is_allowed_file(content_type):
        return False

    extension = os.path.splitext(filename)[1].lower()

    return extension in ALLOWED_MIME_TYPES[content_type]


def build_stored_filename(filename: str, content_type: str) -> str:
    """
    Returns a random, extension-only filename safe to join with a directory.

    The client supplied name is never used on disk, which prevents path
    traversal and overwriting of existing files.
    """

    extension = os.path.splitext(filename)[1].lower()

    if extension not in ALLOWED_MIME_TYPES[content_type]:
        raise ValueError("Extension does not match content type.")

    return f"{uuid.uuid4().hex}{extension}"
