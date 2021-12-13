# -*- coding:utf-8 -*-
# 文件处理  怎么读取文件  路径
# 具体应用 测试数据和测试代码分离开来  yaml文件 excel  txt  csv
# 拿到数据
# yaml文件
# excel文件读取
# txt
# csv
# 自动化测试中  测试数据yaml文件或者excel文件

# yaml文件读取
# 1.有个yaml文件 创建一个yaml文件 写yaml文件数据  读取yaml数据
# 2.第三库，安装  方式 pip install pyyaml  在setting中安装
# 3.引入
# 语法规则: 字典类型的数据  键: 值 :后要空格

import yaml

# 打开文件  设置可读  {}读的字典数据
# f=open('./data/test.yaml','r')
# # 读取yaml数据  txt文件  f.read
# data=yaml.load(f,yaml.FullLoader)
# print(data,type(data))
# 问题：读取yaml里面的秋水数据,通过键名拿到值
# print(data.get('name'))
# print(data['name'])
# f.close()

# 打开文件  读的是列表数据
# with open('./data/test1.yaml','r',encoding='utf-8') as f1:
#     # 拿到了测试数据
#     data=yaml.load(f1,yaml.FullLoader)
#     print(data,type(data))
#     # 列表怎么拿数据
#     print(data[1])

# 做项目的时候，交互[{}]
# with open('./data/test2.yaml','r',encoding='utf-8')as f:
#     data=yaml.load(f,yaml.FullLoader)
#     print(data)
# #    想拿到虚竹
#     print(data[1]['name'])
# [{id:1,name:'秋水',age:18,data:{adress:'长沙',stauts:'success'}}]

# with open('./data/test3.yaml','r',encoding='utf-8')as f:
#     data = yaml.load(f, yaml.FullLoader)
#     print(data)

