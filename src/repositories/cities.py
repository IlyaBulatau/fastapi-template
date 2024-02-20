from sqlalchemy import Result, insert, select

from domains.models import City

from .base import BaseRepositiry


class CityRepositiry(BaseRepositiry):

    async def add(self, city_name: str) -> City:
        query = insert(City).values(name=city_name).returning(City)
        result: Result = await self.session.execute(query)
        await self.session.commit()

        city: City = result.scalar()
        return city

    async def get(self, id: int) -> City:
        query = select(City).filter(City.id == id)
        result: Result = await self.session.execute(query)

        city: City = result.scalar()
        return city
