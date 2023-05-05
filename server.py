from flask import Flask,jsonify
from flask_cors import CORS
from matplotlib.font_manager import json_dump
import GetWeather
import json
import gzip
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_pyfile('config.ini')

@app.route('/api/v1/weather/getweather')
def getWeather():
    data=GetWeather.get_Weather()
    # data=jsonify(data)
    # print(data)
    return data

@app.route('/api/v1/weather/getweather/<situs>')
def getWeatherBySitus(situs):
    print(situs)
    data=GetWeather.get_Weather_situs(situs)
    # data=jsonify(data)
    # print(data)
    return data
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=8999)