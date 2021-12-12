# -*- coding:utf-8 -*-
# @Time : 2021/11/9 21:21
# @Author : 朱树剑
# @File : demo01.py

# 第一个hello world
# print()是python中的一个函数  作用：是把括号中的内容显示在控制台
print('hello world')

# 是给代码起到备注的作用，不会运行  注释  单行注释    快捷键ctrl+/
# 注释： 单行注释，多行注释 '''注释内容'''
'''
三个单引号代表多行注释
可以换行，不会被执行
'''
"""
三个多引号同单引号
"""

# 一个print代表一行，end可以将换行改为对应内容，如','
print('hello world2', end=',')

print("""你好，
李焕英
""")

# 变量：   作用是用来存储数据
# 格式：   变量名=值   变量名可以随意命名，但不能是关键字
x = 3
print(x)

g = 'a'
print(g)

a = 6
b = 5
c = a+b
print(c)
print(a+b)