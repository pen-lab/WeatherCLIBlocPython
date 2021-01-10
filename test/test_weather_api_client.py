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


citys: list[CityData] = [
    CityData('London', 44418),
    CityData('Moscow', 2122265)
]


@pytest.mark.parametrize('city', citys)
async def test_get_location_id(weather_api_client: WeatherApiClient, city: CityData):
    city_id_london = await weather_api_client.get_location_id(city.name)

    assert city_id_london == city.id


async def test_fetch_weather(weather_api_client: WeatherApiClient):
    from weather.models.weather import Weather

    weather: Weather = await weather_api_client.fetch_weather(citys[0].id)

    assert weather.location == citys[0].name
