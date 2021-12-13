# -*- coding:utf-8 -*-
# 读取csv
# 1.创建一个csv
# 2.读取csv文件  csv的库

import csv

# 1.打开文件
# with open('./data/aa.csv','r',encoding='utf-8')as f:
#     csv.reader(f)
#     print(f)
#     for i in f:
#         print(i)

# 只想读取某一行
# with open('./data/aa.csv','r',encoding='utf-8')as f:
#     f1=csv.reader(f)
#     result=list(f1)
#     print(result,result[0])

# 只想读取某一列
# with open('./data/aa.csv','r',encoding='utf-8')as f:
#     f2=csv.reader(f)
#     print(f2)
#     for i in f2:
#         print(i[0])

# 往csv文件写数据
# stu1=[6,'虚竹',100]
# stu2=[7,'大猪蹄子',100]
# with open('./data/aa.csv','a',encoding='utf-8',newline='')as f:
#     # 把数据写到哪
#     writes1=csv.writer(f)
#     writes1.writerow(stu1)
#     writes1.writerow(stu2)

stus=[
    ('小明','aa'),
    ('小明2','bbb'),
    ('小明3','cccc'),
    ('小明4','ddd'),
]
with open('./data/aa.csv','a',encoding='utf-8',newline='')as f:
    writees=csv.writer(f)
    for i in stus:
        writees.writerow(i)


# read  readlines  readline
