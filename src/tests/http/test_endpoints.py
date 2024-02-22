from httpx import AsyncClient

from domains.models import City

# GET
async def test_healtcheck_endpoint(client: AsyncClient):
        response = await client.get("/ping")
        assert response.status_code == 200
        assert response.json() == "pong"


class TestCityEndpoint:

    # POST
    # @pytest.mark.skip(reason="session doesn't ovveride")
    async def test_create_city_endpoint(self, client: AsyncClient):
        data = {"name": "Moskow"}
        response = await client.post("cities/", json=data)
        
        assert response.status_code == 201
        result = response.json()

        assert result.get("name") == data.get("name")
        assert type(result.get("id")) == int
        assert type(result.get("created_at")) == str

    # GET
    # @pytest.mark.skip(reason="session doesn't ovveride")
    async def test_get_all_cities_endpoint(self, client: AsyncClient):
        response = await client.get("cities/")
        assert response.status_code == 200

        cities = response.json()
        assert type(cities) == list

        city_moskow: dict = cities[0]
        assert city_moskow.get("name") == "Moskow"
        assert type(city_moskow.get("id")) == int
        assert city_moskow.get("id") == 1

    # GET
    async def test_get_city_by_id_endpoint(self, client: AsyncClient):
        response = await client.get("cities/1")
        assert response.status_code == 200

        city = response.json()

        assert city.get("name") == "Moskow"
        assert city.get("id") == 1


    # DELETE
    async def test_delete_city_by_id_endpoint(self, client: AsyncClient):
        response = await client.get("cities/1")
        response.status_code == 204