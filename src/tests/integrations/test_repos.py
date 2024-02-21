from sqlalchemy.ext.asyncio import AsyncSession

from domains.models import City
from repositories.cities import CityRepositiry


async def test_city_add_in_database(db: AsyncSession):
    new_city_name = "Minsk"
    city_repo = CityRepositiry(session=db)
    city = await city_repo.add(new_city_name)

    assert type(city) == City
    assert city.name == new_city_name
