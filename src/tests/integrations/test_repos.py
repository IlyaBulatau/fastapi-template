from sqlalchemy.ext.asyncio import AsyncSession

from domains.models import City
from repositories.cities import CityRepositiry


class TestCityRepository:
    new_city_name = "Minsk"

    async def test_city_add_in_database(self, db: AsyncSession):
        city_repo = CityRepositiry(session=db)
        city = await city_repo.add(self.new_city_name)

        assert type(city) == City
        assert city.name == self.new_city_name

    async def test_city_get_by_id_from_database(self, db: AsyncSession):
        city_repo = CityRepositiry(db)
        city = await city_repo.get(1)

        assert type(city) == City
        city.name == self.new_city_name

    async def test_get_all_cities_from_database(self, db: AsyncSession):
        city_repo = CityRepositiry(db)
        cities = await city_repo.list()

        assert type(cities) == list
        assert type(cities[0]) == City
        assert cities[0].id == 1


    