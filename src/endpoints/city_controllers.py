from fastapi import Depends, APIRouter

from domains.models import City
from repositories.base import BaseRepositiry
from repositories.cities import CityRepositiry


router = APIRouter(prefix="/cities", tags=["City"])


@router.get(
    "/", response_model=City, status_code=200, summary="Получение города по ID"
)
async def get_city_by_id(
    city_id: int, city_repo: BaseRepositiry = Depends(CityRepositiry)
):
    city: City = await city_repo.get(city_id)

    return city


@router.post(
    "/", response_model=City, status_code=201, summary="Добавление города"
)
async def create_city(
    city_name: str, city_repo: BaseRepositiry = Depends(CityRepositiry)
):
    city: City = await city_repo.add(city_name)

    return city
