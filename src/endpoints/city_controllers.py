from typing import Annotated

from fastapi import Body, Depends, APIRouter

from domains.models import City
from repositories.base import BaseRepositiry
from repositories.cities import CityRepositiry


router = APIRouter(prefix="/cities", tags=["City"])


@router.get(
    "/",
    response_model=list[City],
    status_code=200,
    summary="Получение всех городов",
)
async def get_all_cities(city_repo: BaseRepositiry = Depends(CityRepositiry)):
    cities: list[City] = await city_repo.list()
    return cities


@router.get(
    "/{city_id}",
    response_model=City,
    status_code=200,
    summary="Получение города по ID",
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
    name: Annotated[str, Body(embed=True)],
    city_repo: BaseRepositiry = Depends(CityRepositiry),
):
    city: City = await city_repo.add(name)

    return city


@router.delete(
    "/{city_id}",
    response_model=None,
    status_code=204,
    summary="Удаление города по ID",
)
async def delete_city(
    city_id: int, city_repo: BaseRepositiry = Depends(CityRepositiry)
):
    await city_repo.remove(city_id)
    return None
