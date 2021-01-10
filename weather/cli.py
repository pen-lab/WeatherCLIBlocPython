import asyncio

from aiohttp import ClientSession
import typer

from weather.blocs.weather_event import WeatherRequested
from weather.blocs.weather_bloc import WeatherBloc
from weather.repositories.weather_api_client import WeatherApiClient
from weather.repositories.weather_repository import WeatherRepository


async def _main(city: str):
    async with ClientSession() as session:
        weather_api_client = WeatherApiClient(session)
        weather_repository: WeatherRepository = WeatherRepository(weather_api_client)
        bloc: WeatherBloc = WeatherBloc(weather_repository)
        await bloc._bind_state_subject()

        await bloc.dispatch(WeatherRequested(city))
        typer.echo(f'Weather for {bloc.state.weather.location}: {bloc.state.weather.temp}')


def weather(
        city: str = typer.Argument(...)
):
    asyncio.run(_main(city))


def main():
    typer.run(weather)

