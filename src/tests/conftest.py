import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app import app
from database.orm import mapper_registry
from database.connection import get_async_session



@pytest.fixture(scope="session")
async def db():
    url = "sqlite+aiosqlite:///database.db"
    engine = create_async_engine(url=url, echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.drop_all)
        await conn.run_sync(mapper_registry.metadata.create_all)

    sessionmaker = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with sessionmaker() as session:
        yield session


@pytest.fixture(scope="session")
async def client(db):

    def get_session_ovveride():
        return db
    
    app.dependency_overrides[get_async_session] = get_session_ovveride
    yield AsyncClient(app=app, base_url="http://test")
