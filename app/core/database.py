from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings


engine = create_async_engine(url=settings.db_url, echo=False)

async_session = async_sessionmaker(engine, expire_on_commit=False)

async def db_session():
    async with async_session() as session:
        yield session