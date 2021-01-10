from typing import Final
from typing import Any

import asyncio
from typing import Coroutine

from aiohttp import ClientSession

from weather.models.weather import Weather

class WeatherApiClient:
    def __init__(self, http_client: ClientSession) -> None:
        self.base_url: Final[str] = 'https://www.metaweather.com'

        self.http_client: ClientSession = http_client

    async def get_location_id(self, city: str) -> Coroutine[Any, Any, Any]:
        location_url: Final[str] = f'{self.base_url}/api/location/search'
        params: dict[str, str] = {'query': city}
        async with self.http_client.get(location_url, params=params) as resp:
            location_response: Final[dict[str, Any]] = await resp.json()

        return location_response[0]['woeid']

    async def fetch_weather(self, location_id: int) -> Coroutine[Any, Any, Any]:
        weather_url: Final[str] = f'{self.base_url}/api/location/{location_id}'

        async with self.http_client.get(weather_url) as resp:
            if resp.status != 200:
                raise Exception('error getting weather for location')
            weather_data: dict[str, Any] = await resp.json()

        return Weather.from_json(weather_data)
         

