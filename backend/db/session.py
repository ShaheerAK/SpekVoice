from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost/urdu_voice_ai"

# Create an async engine to connect to PostgreSQL asynchronously
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a sessionmaker factory for async DB sessions
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency to get DB session inside FastAPI
async def get_db():
    async with async_session() as session:
        yield session
