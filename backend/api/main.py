from fastapi import FastAPI
from backend.api import calls
from backend.api.health import health_router
from fastapi.middleware.cors import CORSMiddleware
import logging
import datetime

app = FastAPI()

# Include the calls router
app.include_router(calls.router)

# Include the health check router
app.include_router(health_router)

# Basic logging config
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO
)

# Allow all CORS (change later if a frontend is integrated)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "urdu-voice-ai",
        "version": "0.1.0",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

@app.post("/voice/webhook")
async def voice_webhook():
    logging.info("Received webhook call")
    return {"message": "Webhook endpoint placeholder"}
