from typing import Any

from datetime import datetime
from pydantic import BaseModel, Field

from .weather_states import WeatherStates


class Weather(BaseModel):
    state: WeatherStates = Field(alias='weather_state_abbr')
    formatted_condition: str = Field(alias='weather_state_name')
    temp: float = Field(alias='the_temp')
    min_temp: float
    max_temp: float
    location_id: int = Field(alias='woeid')
    created: str
    last_updated: datetime
    location: str = Field(alias='title')

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> 'Weather':
        return cls(last_updated=datetime.now(), **data, **data['consolidated_weather'][0])



