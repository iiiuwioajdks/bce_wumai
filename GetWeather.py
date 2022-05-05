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


def get_Weather(IP):
    city_input = "长安区"
    city_idname = get_city(city_input)
    city_id = city_idname[0]
    get_now = get('now',city_id)
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
    if city_idname[2] == city_idname[1]:
        print(city_idname[3], str(city_idname[2]) + '市')
        situs=city_idname[3]+str(city_idname[2]) + '市'
        data.append(situs)
    else:
        print(city_idname[3], str(city_idname[2]) + '市', str(city_idname[1]) + '区')
        situs=city_idname[3]+str(city_idname[2]) + '市'+str(city_idname[1]) + '区'
        data.append(situs)
    data.append(air_now['aqi'])
    # print(data)
    # print('当前天气：', get_now['now']['text'], get_now['now']['temp'], '°C', '体感温度', get_now['now']['feelsLike'], '°C')
    # print('空气质量指数：', air_now['aqi'])
    # print(get_daily['daily'][0]['fxDate'],get_daily['daily'][0]['textDay'],get_daily['daily'][0]['tempMin'], '-', get_daily['daily'][0]['tempMax'], '°C 湿度:',get_daily['daily'][0]['humidity'])
    # print(get_daily['daily'][1]['fxDate'],get_daily['daily'][1]['textDay'],get_daily['daily'][1]['tempMin'], '-', get_daily['daily'][1]['tempMax'], '°C 湿度:',get_daily['daily'][1]['humidity'])
    return data