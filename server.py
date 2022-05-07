from flask import Flask
from flask_cors import CORS
import GetWeather
import json
app = Flask(__name__)
CORS(app, supports_credentials=True)
 
@app.route('/api/v1/weather/getweather/<situs>')
def getWeather(situs):

    data=GetWeather.get_Weather(situs)
    return json.dumps(data)
 
if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.1.105', port=8999)