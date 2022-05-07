# 后端开发

## GetWeather.py

需要实现以下函数，已实现

```python
def get_Weather(situs):
    # situs:String类型，用户的最低级地址
    # return data=[[min,max,wet]*3,pm2.5]
```

myKey.py 里放置了和风天气 api 的密钥
## 中间键

proto文件编译指令：
`python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. data.proto`

# 后端接口

接口地址：```/api/v1/weather/getweather/<situs>```

# 前后端交互

如果网站访问的 api 的网站和自己不同源，浏览器一样会帮你发送request，但是会去检测response 的头部，如果api网站后端返回的respnse 的头部信息，没有允许跨域访问，那么你就不能够得到返回的信息。

不同源的标准：

- domain 域名不一样
- http还是https
- 端口号不一样

python-flask的解决办法：

使用flask_cors包

安装`pip install flask_cors`
初始化的时候加载配置，这样就可以支持跨域访问了

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run()
```
