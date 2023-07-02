import abc


# interface for fetching events
class EventsFetcher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch(self):
        raise NotImplementedError()
