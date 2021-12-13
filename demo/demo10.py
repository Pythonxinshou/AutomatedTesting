# -*- coding:utf-8 -*-
# @Time : 2021/11/15 12:40 
# @Author : 朱树剑
# @File : demo_10.py
# @Software: PyCharm

# 读取csv
import csv

with open(r'aa.csv') as f:
    csv.reader(f)
    print(f)
    for i in f:
        print(i)

# 只读取一行，转换成list
with open(r'aa.csv') as f:
    f1 = list(csv.reader(f))
    print(f1, f1[0])

# 只读取一列
with open(r'aa.csv') as f:
    f1 = list(csv.reader(f))
    for i in f1:
        print(i[0])

# csv数据写入
list1 = ['11', '22', '33']
list2 = ['111', '222', '333']
with open(r'aa.csv', 'a', newline='') as f:
    write1 = csv.writer(f)
    write1.writerow(list1)
    write1.writerow(list2)
