import pytest
from httpx import AsyncClient


async def test_healtcheck_endpoint(client: AsyncClient):
    response = await client.get("/ping")
    assert response.status_code == 200
    assert response.json() == "pong"


@pytest.mark.skip(reason="session doesn't ovveride")
async def test_create_city_endpoint(client: AsyncClient):
    data = {"name": "Minsk"}
    response = await client.post("cities/", json=data)
    assert response.status_code == 201


@pytest.mark.skip(reason="session doesn't ovveride")
async def test_get_all_cities_endpoint(client: AsyncClient):
    response = await client.get("cities/")
    assert response.status_code == 200
