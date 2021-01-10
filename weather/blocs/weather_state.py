from abc import ABC

from weather.models.weather import Weather


class WeatherState(ABC):
    @property
    def weather(self) -> Weather:
        return self._weather


class WeatherInitial(WeatherState):
    pass


class WeatherLoadingInProgress(WeatherState):
    pass


class WeatherLoadSuccess(WeatherState):
    def __init__(self, weather: Weather) -> None:
        self._weather: Weather = weather


class WeatherLoadFailure(WeatherState):
    pass
