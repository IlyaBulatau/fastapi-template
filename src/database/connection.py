from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from config import SETTINGS


async_engine = create_async_engine(SETTINGS.url, future=True, echo=True)
async_session = async_sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncSession: # type: ignore
    session = async_session()
    try:
        yield session
    except:
        await session.rollback()
    finally:
        await session.close()