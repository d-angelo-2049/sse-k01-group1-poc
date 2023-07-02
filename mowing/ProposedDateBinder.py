from collections.abc import Callable

import injector

from mowing.DatePresenter import DatePresenter
from mowing.DemoDatePresenter import DemoDatePresenter
from mowing.EventsFetcher import EventsFetcher
from mowing.GoogleCalendarEventsFetcher import GoogleCalendarEventsFetcher
from mowing.OpenWeatherInforFetcher import OpenWeatherInforFetcher
from mowing.WeatherInfoFetcher import WeatherInforFetcher


class ProposedDateBinder:

    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)

    @classmethod
    def configure(cls, binder: injector.Binder):
        binder.bind(EventsFetcher, to=GoogleCalendarEventsFetcher)
        binder.bind(WeatherInforFetcher, to=OpenWeatherInforFetcher)
        binder.bind(DatePresenter, to=DemoDatePresenter)

    def resolve(self, cls):
        return self._injector.get(cls)
