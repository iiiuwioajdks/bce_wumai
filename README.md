# 后端开发

## GetWeather.py

需要实现以下函数，已实现

```python
def get_Weather(situs):
    # situs:String类型，用户的最低级地址
    # return data=[[min,max,wet]*3,pm2.5]
```

myKey.py 里放置了和风天气 api 的密钥

# 后端接口

接口地址：```/api/v1/weather/getweather/<situs>```

# 前后端交互

后端 api 的网址和前端不同源，浏览器帮忙发送 request 时会去检测  response 的头部。如果后端返回的 response 的头部信息没有允许跨域访问，前端就不能够得到返回的信息。

**不同源的标准：**

- domain 域名不同
- http 与 https
- 端口号不同

**python-flask的解决办法：**

使用 flask_cors 包

安装 `pip install flask_cors`
初始化的时候加载配置，就可以支持跨域访问了。

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run()
```
