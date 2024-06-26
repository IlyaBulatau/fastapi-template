from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import SETTINGS


async_engine = create_async_engine(SETTINGS.url, future=True, echo=True)
async_session = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncSession:  # type: ignore
    session = async_session()
    try:
        yield session
    finally:
        await session.rollback()
        await session.close()
