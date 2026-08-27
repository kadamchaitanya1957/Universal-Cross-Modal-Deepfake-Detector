import os

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")

# Maximum accepted upload size in bytes (default 50 MB).
MAX_UPLOAD_SIZE = int(os.getenv("MAX_UPLOAD_SIZE", 50 * 1024 * 1024))

# Chunk size used when streaming uploads to disk.
UPLOAD_CHUNK_SIZE = 1024 * 1024

DEFAULT_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]


def get_allowed_origins() -> list[str]:
    """
    Allowed CORS origins, overridable with a comma separated ALLOWED_ORIGINS.
    """
    raw = os.getenv("ALLOWED_ORIGINS")

    if not raw:
        return DEFAULT_ALLOWED_ORIGINS

    return [origin.strip() for origin in raw.split(",") if origin.strip()]
