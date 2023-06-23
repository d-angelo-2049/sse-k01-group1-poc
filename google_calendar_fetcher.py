import configparser
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build


# google calendar event fetcher for poc
def google_calendar_fetcher():
    # read api key
    config = configparser.ConfigParser()
    config.read('credentials.ini')
    calendar_id = config.get('credentials', 'calendar_id')
    api_key = config.get('credentials', 'google_api_key')

    # get events 2 weeks ahead in JST
    JST = timezone(timedelta(hours=+9))
    event_start = datetime.now(JST).isoformat()
    event_end = (datetime.now(JST) + timedelta(weeks=2)).isoformat()

    # event fetch
    api_version = 'v3'
    service = build('calendar', api_version, developerKey=api_key)
    events = service.events().list(
        calendarId=calendar_id,
        timeMin=event_start,
        timeMax=event_end,
        singleEvents=True,
        orderBy='startTime'
    ).execute().get('items', [])

    if not events:
        print('2週間以内のイベントは見つかりませんでした。')
    else:
        print('2週間以内のイベント:')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            summary = event['summary']
            print(f'{start} - {end}: {summary}')


if __name__ == '__main__':
    google_calendar_fetcher()
