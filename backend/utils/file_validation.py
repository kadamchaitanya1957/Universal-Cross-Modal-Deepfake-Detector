ALLOWED_MIME_TYPES = {
    # Images
    "image/jpeg",
    "image/png",
    "image/webp",

    # Videos
    "video/mp4",
    "video/quicktime",
    "video/x-msvideo",

    # Audio
    "audio/mpeg",
    "audio/wav",
    "audio/x-wav",
    "audio/mp4",

    # Documents
    "application/pdf",
}


def is_allowed_file(content_type: str | None) -> bool:
    """
    Returns True if the uploaded file's MIME type is supported.
    Returns False otherwise.
    """

    if not content_type:
        return False

    return content_type in ALLOWED_MIME_TYPES