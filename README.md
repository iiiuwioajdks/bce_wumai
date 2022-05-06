文件名GetWeather.py

get_Weather(situs)

IN:

`  situs:list类型，用户的地址`

Return：

`  data：list嵌套list类型，最里层list包含一天的天气情况`

  每一个list是一天的数据。

  {{min，max，wet}，{min，max，wet}，{min，max，wet},pm25}

proto文件编译指令：

`python3.6 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. data.proto`