import configparser

from pyowm import OWM
from pyowm.utils.config import get_default_config

from mowing.WeatherInfoFetcher import WeatherInforFetcher


class OpenWeatherInforFetcher(WeatherInforFetcher):

    def __init__(self):
        # read api key
        config = configparser.ConfigParser()
        config.read('../credentials.ini')
        self.key = config.get('credentials', 'weather_api_key')
        self.location = "Tokyo,JP"
        self.config_dict = get_default_config()
        self.config_dict["language"] = "ja"

    def fetch(self):
        print("This is OpenWeatherInforFetcher")
        result = []
        owm = OWM(self.key, self.config_dict)
        mgr = owm.weather_manager()
        forecast = mgr.forecast_at_place(self.location, '3h', limit=40)

        for weather in forecast.forecast:
            data = {
                'time': weather.reference_time('iso'),
                'status': weather.status,
                'temperature': weather.temperature('celsius')['temp'],
                'humidity': weather.humidity
            }
            result.append(data)
        return result
