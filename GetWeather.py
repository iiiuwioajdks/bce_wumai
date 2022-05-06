import requests
from myKey import KEY

''' official website  https://www.qweather.com '''
'''      dev website  https://dev.qweather.com'''
mykey = '&key=' + KEY # EDIT HERE!

url_api_weather = 'https://devapi.qweather.com/v7/weather/'
url_api_geo = 'https://geoapi.qweather.com/v2/city/'
url_api_air = 'https://devapi.qweather.com/v7/air/now'

def get(api_type,city_id):
    url = url_api_weather + api_type + '?location=' + city_id + mykey
    return requests.get(url).json()

def air(city_id):
    url = url_api_air + '?location=' + city_id + mykey
    return requests.get(url).json()

def get_city(city_kw):
    url_v2 = url_api_geo + 'lookup?location=' + city_kw + mykey
    city = requests.get(url_v2).json()['location'][0]

    city_id = city['id']
    district_name = city['name']
    city_name = city['adm2']
    province_name = city['adm1']
    country_name = city['country']
    lat = city['lat']
    lon = city['lon']

    return city_id, district_name, city_name, province_name, country_name, lat, lon


def get_Weather(situs):
    city_input = situs
    city_idname = get_city(city_input)
    city_id = city_idname[0]
    # get_now = get('now',city_id)
    get_daily = get('3d',city_id)
    air_now = air(city_id)['now']

    data=[]
    for i in range (3):
        temp=[]
        temp.append(get_daily['daily'][i]['tempMin'])
        temp.append(get_daily['daily'][i]['tempMax'])
        temp.append(get_daily['daily'][i]['humidity'])
        data.append(temp)
    situs=[]
    data.append(air_now['aqi'])

    return data
get_Weather("西安市")