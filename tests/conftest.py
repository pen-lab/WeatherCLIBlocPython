from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest

import pytest
import dataclasses

from aiohttp import ClientSession

from weather.repositories.weather_api_client import WeatherApiClient


@pytest.fixture()
def path_test_data(request: FixtureRequest) -> Path:
    return Path(request.fspath).parent.joinpath('data')


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
