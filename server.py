from flask import Flask
import GetWeather
import json
app = Flask(__name__)
 
@app.route('/api/v1/weather/getweather/<situs>')
def getWeather(situs):

    data=GetWeather.get_Weather(situs)
    return json.dumps(data)
 
if __name__ == '__main__':
    app.debug = True
    app.run()