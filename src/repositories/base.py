from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from domains.models import BaseModel
from utils.dependences import GET_ASYNC_SESSION


class BaseRepositiry(ABC):

    def __init__(self, session: AsyncSession = GET_ASYNC_SESSION):
        self.session: AsyncSession = session
    
    @abstractmethod
    async def add(self, model: BaseModel) -> BaseModel:
        ...
    
    @abstractmethod
    async def get(self, id: int) -> BaseModel:
        ...