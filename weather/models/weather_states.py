from enum import Enum


class WeatherStates(str, Enum):
    show = 'sn'
    sleet = 'sl'
    hail = 'h'
    thunderstorm = 't'
    heavy_rain = 'hr'
    light_rain = 'lr'
    showers = 's'
    heavy_cloud = 'hc'
    light_cloud = 'lc'
    clear = 'c'
