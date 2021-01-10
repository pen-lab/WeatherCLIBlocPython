from typing import Final

from abc import ABC


class WeatherEvent(ABC):
    pass


class WeatherRequested(WeatherEvent):

    def __init__(self, city: str) -> None:
        self.city: Final[str] = city
