import requests
import pygeoip
import gzip
import re
import socket
import json
from myKey import KEY
mykey = '&key=' + KEY # EDIT HERE!
ngzip = '&gzip=n'

url_api_weather = 'https://devapi.qweather.com/v7/weather/now'
url_api_lookup = 'https://geoapi.qweather.com/v2/city/lookup'
url_api_humidy = 'https://devapi.qweather.com/v7/air/5d'
url_api_humidy_now = 'https://devapi.qweather.com/v7/air/now'
url_all_in_one = 'https://devapi.qweather.com/v7/weather/7d'

def get_city_by_ip():
    # site = requests.get("http://checkip.dyndns.org/")
    # grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site.text)
    ip = "106.38.226.62"
    gi = pygeoip.GeoIP("ip_tools/GeoLiteCity.dat")
    rec = gi.record_by_addr(ip)
    long = round(rec['longitude'],2)
    lat = round(rec['latitude'],2)
    loc = str(long)+","+str(lat)
    url_lookup = url_api_lookup + '?location=' + loc + mykey
    response = requests.get(url_lookup).json()
    id = response['location'][0]['id']
    name = response['location'][0]['name']
    adm1 = response['location'][0]['adm1']
    return id, adm1+name

def get_weather(id):
    url = url_api_weather + '?location=' + id + mykey + ngzip
    return requests.get(url).json()

def get_humidy(id):
    url = url_api_humidy + '?location=' + id + mykey + ngzip
    return requests.get(url).json()

def get_air_now(id):
    url = url_api_humidy_now + '?location=' + id + mykey + ngzip
    return requests.get(url).json()

def get(id):
    url = url_all_in_one + '?location=' + id + mykey + ngzip
    return requests.get(url).json()

def get_Weather():
    id, name = get_city_by_ip()
    # city_input = situs
    # url_lookup = url_api_lookup + '?location=' + city_input + mykey
    # response = requests.get(url_lookup).json()
    # id = response['location'][0]['id']
    get_daily = get(id)
    get_hum = get_humidy(id)
    air_now = get_air_now(id)
    wea_now = get_weather(id)
    for i in range(5):
        try:
            get_daily["daily"][i]['air_quality'] = get_hum["daily"][i]
        except :
            break
    
    try:
        get_daily["city_name"] = name
        get_daily["air_quality_fxLink"] = get_hum["fxLink"]
        get_daily["daily"][0]["air_quality_now"] = air_now["now"]
        get_daily["daily"][0]["air_quality_now"]["fxLink"] = air_now["fxLink"]
        get_daily["daily"][0]["weather_now"] = wea_now["now"]
        get_daily["daily"][0]["wearher_now"]["fxLink"] = wea_now["fxLink"]
    except:
        get_daily["daily"][0]["air_quality_now"] = {}
    return get_daily

def get_Weather_situs(situs):
    city_input = situs
    url_lookup = url_api_lookup + '?location=' + city_input + mykey
    response = requests.get(url_lookup).json()
    id = response['location'][0]['id']
    get_daily = get(id)
    get_hum = get_humidy(id)
    air_now = get_air_now(id)
    wea_now = get_weather(id)
    for i in range(5):
        try:
            get_daily["daily"][i]['air_quality'] = get_hum["daily"][i]
        except :
            break
    
    try:
        get_daily["air_quality_fxLink"] = get_hum["fxLink"]
        get_daily["daily"][0]["air_quality_now"] = air_now["now"]
        get_daily["daily"][0]["air_quality_now"]["fxLink"] = air_now["fxLink"]
        get_daily["daily"][0]["weather_now"] = wea_now["now"]
        get_daily["daily"][0]["wearher_now"]["fxLink"] = wea_now["fxLink"]
    except:
        get_daily["daily"][0]["air_quality_now"] = {}
    return get_daily