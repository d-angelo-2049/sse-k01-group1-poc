import abc


class DatePresenter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def present(self):
        raise NotImplementedError()
