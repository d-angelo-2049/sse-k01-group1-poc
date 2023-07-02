
from datetime import datetime, timedelta

import pytz

from mowing.OpenWeatherInforFetcher import OpenWeatherInforFetcher


fetcher = OpenWeatherInforFetcher()
weather_data = fetcher.fetch()

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

jst = pytz.timezone('Asia/Tokyo')
# Print the modified weather data
for data in modified_weather_data:
    utc_time = datetime.strptime(data['time'], '%Y-%m-%d %H:%M:%S%z')
    jst_time = utc_time.astimezone(jst)
    data['time'] = jst_time.strftime('%Y-%m-%d %H:%M:%S%z')
    # print(data)

print(modified_weather_data)