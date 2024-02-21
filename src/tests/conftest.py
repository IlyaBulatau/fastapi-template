import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app import app
from database.orm import mapper_registry


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

        def overide_get_async_session():
            yield session

        app.dependency_overrides["get_async_session"] = (
            overide_get_async_session
        )
        yield session


@pytest.fixture(scope="session")
async def client(db):
    yield AsyncClient(app=app, base_url="http://test")
