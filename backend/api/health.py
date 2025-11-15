from fastapi import APIRouter
from backend.db.session import engine  # async SQLAlchemy engine
from sqlalchemy import text
import logging

health_router = APIRouter()

@health_router.get("/health")
async def health():
    try:
        async with engine.connect() as conn:
            # use text() for raw SQL
            result = await conn.execute(text("SELECT 1"))
            # optional: fetch scalar to ensure query returned
            _ = result.scalar_one_or_none()
        db_status = "connected"
    except Exception as e:
        logging.exception("DB health check failed")
        db_status = "disconnected"
    return {
        "status": "healthy",
        "database": db_status
    }
