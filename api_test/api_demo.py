# -*- coding:utf-8 -*-
# @Time : 2021/12/7 20:14
# @Author : 朱树剑
# @File : api_demo.py
# 导包
import requests
import json

# requests常用方法
# requests.request()

# r = requests.get("http://www.baidu.com")
# 数据的生成
data = {
    'username': 'admin',
    'password': '123456'
}

# 接口地址
# 404 路径异常
url = 'http://39.98.138.157:5000/api/loqin'
# 将数据传递到对应的接口地址，来实现一次该接口的请求下发并返回响应结果:定义对应的请求方法
res = requests.post(url, data=data)
# 输出状态码，输出的是一个响应对象，默认显示状态码
print(res)

# 输出状态码，本身状态码的一个属性
print(res.status_code)

# 输出响应结果，返回原始内容，以字节的形式展示
print(res.content)
print('-' * 40)
# 输出响应结果：编译后的内容
print(res.text)

# 输出响应结果：最原生的桩体，对象在内存中的地址
print(res.raw)

# 请求头
url = 'http://39.98.138.157:5000/api/loqin'
res = requests.post(url, data=data)
print(res.request.headers)

# 请求头定义
hd = {
    'Content-Type': 'application/json'
}
res = requests.post(url, data=data, headers=hd)
print(res)
print(res.request.headers)

# 将data转化为json对象，通过使用json库来进行转换
# dumps是进行转型，将原有的字典数据转换为json格式
jsonData = json.dumps(data)
print(jsonData)
res = requests.post(url, data=data, headers=hd)
print(res)
print(res.text)
print(res.request.headers)
