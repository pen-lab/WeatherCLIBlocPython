import pytest

from weather.blocs.weather_event import WeatherRequested
from weather.blocs.weather_bloc import WeatherBloc
from weather.repositories.weather_api_client import WeatherApiClient
from weather.repositories.weather_repository import WeatherRepository

from .conftest import citys, CityData


@pytest.fixture()
def moscow_data() -> CityData:
    return citys[1]


async def test_bloc(weather_api_client: WeatherApiClient, moscow_data: CityData):
    weather_repository: WeatherRepository = WeatherRepository(weather_api_client)
    bloc: WeatherBloc = WeatherBloc(weather_repository)
    await bloc._bind_state_subject()

    await bloc.dispatch(WeatherRequested(moscow_data.name))

    assert bloc.state.weather.location == moscow_data.name
