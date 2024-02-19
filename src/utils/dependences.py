from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.connection import get_async_session


GET_ASYNC_SESSION = Depends(get_async_session)

