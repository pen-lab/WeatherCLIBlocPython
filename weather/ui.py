import asyncio

import typer

from bloc import BlocDelegate, Transition

from weather.blocs.weather_event import WeatherEvent
from weather.blocs.weather_state import (
    WeatherState,
    WeatherLoadFailure,
    WeatherLoadSuccess,
    WeatherLoadingInProgress
)


class WeatherUI(BlocDelegate):

    task = None
    is_loading = False

    async def on_transition(self, transition: Transition[WeatherEvent, WeatherState]) -> None:
        async def loading():
            iter_num: int = 0
            while self.is_loading:
                await asyncio.sleep(0.4)
                iter_num += 1
                print('Fetch weather' + ('.' * iter_num))

        if isinstance(transition.next_state, WeatherLoadFailure):
            self.is_loading = False
            print(f'Error: ')
        elif isinstance(transition.next_state, WeatherLoadSuccess):
            self.is_loading = False
            print(f'Weather for {transition.next_state.weather.location}: {transition.next_state.weather.temp}')
        else:
            self.is_loading = True
            print('Fetch weather')
            self.task = asyncio.create_task(loading())
