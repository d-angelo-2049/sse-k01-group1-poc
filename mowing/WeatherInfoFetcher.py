import abc


# interface for fetching weather forecasts information
class WeatherInforFetcher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_weather_info(self):
        raise NotImplementedError()
