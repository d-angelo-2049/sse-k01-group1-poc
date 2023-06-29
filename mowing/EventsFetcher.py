import abc


# interface for fetching events
class EventsFetcher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_events(self):
        raise NotImplementedError()
