import pytest
import dataclasses

from aiohttp import ClientSession

from weather.repositories.weather_api_client import WeatherApiClient


@dataclasses.dataclass
class CityData:
    name: str
    id: int


@pytest.fixture()
async def weather_api_client(aiohttp_client, loop) -> WeatherApiClient:
    async with ClientSession() as session:
        weather_api_client = WeatherApiClient(session)
        yield weather_api_client


@pytest.mark.parametrize('city', [CityData('London', 44418), CityData('Moscow', 2122265)])
async def test_hello(weather_api_client: WeatherApiClient, city: CityData):
    city_id_london = await weather_api_client.get_location_id(city.name)

    assert city_id_london == city.id
