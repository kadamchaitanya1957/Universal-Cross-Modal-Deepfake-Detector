UPLOAD_DIR = "uploads"

DEV_HOSTS = ("localhost", "127.0.0.1")
DEV_PORTS = (5173, 5174)

CORS_ALLOWED_ORIGINS = [
    f"http://{host}:{port}"
    for port in DEV_PORTS
    for host in DEV_HOSTS
]
