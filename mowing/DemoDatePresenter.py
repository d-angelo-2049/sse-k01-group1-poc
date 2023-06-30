import injector

from mowing.DatePresenter import DatePresenter
from mowing.EventsFetcher import EventsFetcher
from mowing.WeatherInfoFetcher import WeatherInforFetcher


class DemoDatePresenter(DatePresenter):

    @injector.inject
    def __init__(self, events: EventsFetcher, weather_info: WeatherInforFetcher):
        self.events = events
        self.weather_info = weather_info

    def present(self):
        print("this is demo date presenter")

        events = self.events.fetch()
        weather_info = self.weather_info.fetch()
