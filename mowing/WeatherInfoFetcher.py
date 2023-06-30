import abc


# interface for fetching weather forecasts information
class WeatherInforFetcher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch(self):
        raise NotImplementedError()
