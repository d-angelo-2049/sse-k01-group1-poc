from mowing.DatePresenter import DatePresenter
from mowing.ProposedDateBinder import ProposedDateBinder


def present_proposed_date():
    binder = ProposedDateBinder()
    date_presenter = binder.resolve(DatePresenter)
    date_presenter.present()


if __name__ == '__main__':
    present_proposed_date()
