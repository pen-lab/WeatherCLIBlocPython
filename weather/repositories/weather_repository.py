from typing import Coroutine
from typing import Final

import asyncio

from weather.models.weather import Weather
from .weather_api_client import WeatherApiClient


class WeatherRepository:
    def __init__(self, weather_api_client: WeatherApiClient) -> None:
        self.weather_api_client: WeatherApiClient = weather_api_client

    async def get_weather(self, city: str) -> Coroutine:
        location_id: Final[int] = await self.weather_api_client.get_location_id(city)
        return await self.weather_api_client.fetch_weather(location_id)
