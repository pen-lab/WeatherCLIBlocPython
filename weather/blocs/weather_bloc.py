from typing import AsyncGenerator
from typing import Final

from bloc import Bloc
from bloc._bloc.bloc import S

from weather.models.weather import Weather
from weather.repositories.weather_repository import WeatherRepository

from .weather_event import WeatherEvent, WeatherRequested
from .weather_state import (
    WeatherState,
    WeatherInitial,
    WeatherLoadingInProgress,
    WeatherLoadSuccess,
    WeatherLoadFailure
)


class WeatherBloc(Bloc[WeatherEvent, WeatherState]):
    def __init__(self, weather_repository: WeatherRepository) -> None:
        super(WeatherBloc, self).__init__()
        self.weather_repository: WeatherRepository = weather_repository

    @property
    def initial_state(self) -> WeatherState:
        return WeatherInitial()

    async def map_event_to_state(self, event: WeatherEvent) -> AsyncGenerator[WeatherState, None]:
        if isinstance(event, WeatherRequested):
            yield WeatherLoadingInProgress

            try:
                weather: Final[Weather] = await self.weather_repository.get_weather(event.city)
                yield WeatherLoadSuccess(weather)
            except Exception:
                yield WeatherLoadFailure()

    @property
    def state(self) -> WeatherState:
        return super().state


