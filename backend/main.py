"""
Project Face — FastAPI Backend Main Entry Point
Audrey Evans Official / GlowStarLabs
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Import routes
from backend.api.routes.project_face import router as face_router
from backend.services.stripe_service import StripeService

app = FastAPI(
    title="Project Face",
    description="AI-powered facial recognition, emotion detection, age estimation, and skin analysis",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Stripe service
stripe_svc = StripeService()

# Mount API routes
app.include_router(face_router, prefix="/api/face", tags=["Face Analysis"])


@app.get("/api/health")
async def health():
    return {"status": "healthy", "service": "Project Face", "version": "1.0.0"}


@app.get("/api/stripe/config")
async def stripe_config():
    return {
        "publishable_key": stripe_svc.get_publishable_key(),
        "mode": os.getenv("STRIPE_MODE", "test"),
    }


# Serve frontend static files
static_dir = Path(__file__).parent.parent / "static"
if static_dir.exists():
    app.mount("/assets", StaticFiles(directory=str(static_dir / "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        file_path = static_dir / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(str(file_path))
        return FileResponse(str(static_dir / "index.html"))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8001, reload=True)
