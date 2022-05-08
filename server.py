from flask import Flask,jsonify
from flask_cors import CORS
from matplotlib.font_manager import json_dump
import GetWeather
import json
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_pyfile('config.ini')

@app.route('/api/v1/weather/getweather/<situs>')
def getWeather(situs):

    data=GetWeather.get_Weather(situs)
    data=jsonify(data)
    return data
 
if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.1.105', port=8999)