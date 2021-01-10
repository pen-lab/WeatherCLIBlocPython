from typing import Any

from datetime import datetime
from pathlib import Path

import pytest

from weather.models.weather_states import WeatherStates
from weather.models.weather import Weather


@pytest.fixture()
def json_data(path_test_data: Path) -> dict[str, Any]:
    import json

    with open(path_test_data.joinpath('example_data.json'), 'r') as f:
        return json.load(f)


def test_load_from_json(json_data: dict[str, Any]):
    weather: Weather = Weather.from_json(json_data)
    assert weather.state.heavy_cloud == WeatherStates.heavy_cloud
    assert weather.location == 'London'
    assert weather.max_temp == 3.4899999999999998
