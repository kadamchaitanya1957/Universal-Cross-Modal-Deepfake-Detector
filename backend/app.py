from fastapi import FastAPI

app = FastAPI(
    title="Universal Cross Modal Deepfake Detector",
    version="1.0.0",
    description="Backend API for AI authenticity detection."
)


@app.get("/")
def root():
    return {
        "message": "Universal Cross Modal Deepfake Detector API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }