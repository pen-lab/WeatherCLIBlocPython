from typing import Final
from typing import Any

import asyncio
from typing import Coroutine

from aiohttp import ClientSession


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
         

