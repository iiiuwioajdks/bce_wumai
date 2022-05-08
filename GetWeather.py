import requests
import json
from myKey import KEY
mykey = '&key=' + KEY # EDIT HERE!

url_api_weather = 'https://query.asilu.com/weather/baidu/'
url_api_humidy = 'https://bird.ioliu.cn/weather'

def get(city_input):
    url = url_api_weather + '?city=' + city_input
    return requests.get(url).json()

def get_humidy(city_input):
    url = url_api_humidy + '?city=' +city_input
    return requests.get(url).json()

def get_Weather(situs):
    city_input = situs
    get_daily = get(city_input)
    get_hum = get_humidy(city_input)
    get_daily['hourly_hum']=[]
    for i in range(7):
        weather = get_hum['daily_forecast'][i]['cond']['txt_d']
        get_daily['weather'][i]['weather']=weather
    for i in range(8):
        hum = get_hum['hourly_forecast'][i]['hum']
        date = get_hum['hourly_forecast'][i]['date']
        get_daily['hourly_hum'].append({})
        get_daily['hourly_hum'][i]['hum']=hum
        get_daily['hourly_hum'][i]['date']=date
    return get_daily