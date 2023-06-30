from datetime import datetime, timezone, timedelta, time

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
        self.calc_proposed_date()

    def calc_proposed_date(self):
        free_time_slots = []
        events = self.events.fetch()
        for weather_info in self.prepared_weather_info():

            # start time : 8:00 - 16:00
            weather_obj = datetime.strptime(weather_info['time'], "%Y-%m-%d %H:%M:%S%z")
            weather_time = datetime.strptime(weather_obj.strftime("%H:%M"), "%H:%M").time()
            eight_am = datetime.strptime("8:00", "%H:%M").time()
            four_pm = datetime.strptime("16:00", "%H:%M").time()

            if not (eight_am <= weather_time <= four_pm):
                # Early continue except 8:00-16:00
                # print(weather_time)
                continue
            if not weather_info['status'] in ['Clear', 'Clouds']:
                # print(weather_info['status'])
                continue

            # 天気情報の時刻
            weather_time = datetime.strptime(weather_info['time'], "%Y-%m-%d %H:%M:%S%z")
            # 3 hours later
            three_hours_later = weather_time + timedelta(hours=3)
            has_overlap = False
            for event in events:
                # google calendar event time
                event_start = datetime.fromisoformat(event['start'])
                event_end = datetime.fromisoformat(event['end'])
                if not (event_start > three_hours_later or event_end < weather_time):
                    has_overlap = True
                    break
            if not has_overlap:
                free_time_slots.append((weather_time, three_hours_later))

        # 結果の表示
        for slot in free_time_slots:
            print(f"Free time slot: {slot[0]} - {slot[1]}")

    def prepared_weather_info(self):

        weather_data = self.weather_info.fetch()

        # New list to store the modified weather data
        modified_weather_data = []

        # Iterate over each weather object in the original data
        for i in range(len(weather_data)):
            current_weather = weather_data[i]
            modified_weather_data.append(current_weather)  # Add the current weather object to the new list

            # Check if there is a next weather object
            if i < len(weather_data) - 1:
                next_weather = weather_data[i + 1]

                # Get the current and next timestamps
                current_timestamp = datetime.strptime(current_weather["time"], "%Y-%m-%d %H:%M:%S%z")
                next_timestamp = datetime.strptime(next_weather["time"], "%Y-%m-%d %H:%M:%S%z")

                # Calculate the time difference in hours
                time_difference_hours = (next_timestamp - current_timestamp).total_seconds() / 3600

                # If the time difference is greater than 1 hour, insert missing data
                if time_difference_hours > 1:
                    for j in range(1, int(time_difference_hours)):
                        new_timestamp = current_timestamp + timedelta(hours=j)
                        new_weather = {
                            "time": new_timestamp.strftime("%Y-%m-%d %H:%M:%S%z"),
                            "status": current_weather["status"],
                            "temperature": current_weather["temperature"],
                            "humidity": current_weather["humidity"]
                        }
                        modified_weather_data.append(new_weather)  # Add the new weather object to the new list

        # Print the modified weather data
        return modified_weather_data
