import configparser
import json
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

def weather_api_getter():
    # read api key
    config = configparser.ConfigParser()
    config.read('credentials.ini')
    key = config.get('credentials', 'weather_api_key')
    return key

api_key=weather_api_getter()
location = "Tokyo,JP"

#  PyOWMのコンフィグ設定
config_dict = get_default_config()
config_dict["language"] = "ja" # 取得データの言語設定

# PyOWMライブラリの初期化
owm = OWM(api_key, config_dict)
mgr = owm.weather_manager()

# 5日後までの天気データを取得
forecast = mgr.forecast_at_place(location, '3h', limit=40)
weather_data = []

# 各時間帯の天気データを辞書形式に変換してリストに追加
for weather in forecast.forecast:
    data = {
        'time': weather.reference_time('iso'),
        'status': weather.status,
        'temperature': weather.temperature('celsius')['temp'],
        'humidity': weather.humidity
    }
    weather_data.append(data)

# JSONファイルに保存
with open('weather.json', 'w') as file:
    json.dump(weather_data, file)

print("5日後までの天気データをweather.jsonに保存しました。")

