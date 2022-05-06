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
`python3.6 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. data.proto`
