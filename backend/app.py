

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from config import get_allowed_origins

from routes.health import router as health_router


from routes.analyze import router as analyze_router


app = FastAPI(
    title="Universal Cross Modal Deepfake Detector",
    version="1.0.0",
    description="Backend API for AI authenticity detection."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(health_router)

app.include_router(analyze_router)



@app.get("/")
def root():
    return {"message": "Universal Cross Modal Deepfake Detector API"}
    