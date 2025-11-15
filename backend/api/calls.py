from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db.session import get_db
from backend.models.models import Call
from datetime import datetime

router = APIRouter()


# Create a test call entry in the database
@router.post("/calls/test")
async def create_test_call(db: AsyncSession = Depends(get_db)):
    try:
        new_call = Call(
            caller_number="1234567890",
            receiver_number="0987654321",
            call_start_time=datetime.utcnow(),
            call_end_time=datetime.utcnow(),
            status="completed"
        )
        db.add(new_call)
        await db.commit()
        await db.refresh(new_call)
        return {"message": "Test call created", "call_id": new_call.id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))



# Retrieve all call entries from the database
@router.get("/calls")
async def get_calls(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Call))
    calls = result.scalars().all()
    return calls
