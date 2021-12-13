# -*- coding:utf-8 -*-
# @Time : 2021/11/15 17:05 
# @Author : 朱树剑
# @File : demo_11.py
# @Software: PyCharm
while True:
    try:
        number = int(input('请输入一个整数：'))
        print(5/number)
        break
    except ValueError:
        print('输入无效，请输入整数')
    except ZeroDivisionError:
        print('0不能为除数')
