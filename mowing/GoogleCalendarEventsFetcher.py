from mowing.EventsFetcher import EventsFetcher
import configparser
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build


class GoogleCalendarEventsFetcher(EventsFetcher):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../credentials.ini')
        self.calendar_id = config.get('credentials', 'calendar_id')
        self.api_key = config.get('credentials', 'google_api_key')
        self.JST = timezone(timedelta(hours=+9))

    def fetch(self):
        print("This is Google Calendar Events Fetcher")

        # get events 2 weeks ahead in JST
        event_start = datetime.now(self.JST).isoformat()
        event_end = (datetime.now(self.JST) + timedelta(days=5)).isoformat()

        # event fetch
        api_version = 'v3'
        service = build('calendar', api_version, developerKey=self.api_key)
        events = service.events().list(
            calendarId=self.calendar_id,
            timeMin=event_start,
            timeMax=event_end,
            singleEvents=True,
            orderBy='startTime'
        ).execute().get('items', [])

        result = []
        if not events:
            print('2週間以内のイベントは見つかりませんでした。')
            return result
        else:
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                end = event['end'].get('dateTime', event['end'].get('date'))
                summary = event['summary']
                result.append({'start': start, 'end': end, 'summary': summary})
            return result
