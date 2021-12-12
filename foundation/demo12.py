# -*- coding:utf-8 -*-
# @Time : 2021/11/20 18:44
# @Author : 朱树剑
# @File : demo12.py

# 装饰器: 字面意思  装饰  头上别朵花  手上首饰
# 编程里面的装饰。比如有个函数  登录的函数  增加其他的功能  装饰器
# 定义: 是给已有的函数增加额外的功能  本质是一个闭包函数

# 闭包函数:变量  函数销毁之后，有时候  有需要这个函数的变量  闭包解决这个问题
# 闭包的定义:在函数嵌套的前提下，内部函数使用外部函数的变量，并且外部函数返回内部函数
# 我们把这个使用外部函数恋量的内部函数称为闭包

# 形成条件:
# 1.实现函数嵌套
# 2.内部函数使用外部函数的变量#3.外部函数返回内部函数
# def atest1():
#     b=10
#     # 内部函数
#     def atest2():
#         print(b)
#     return atest2
#
# a = atest1()
# a()

# def test1(num1):
#     def test2(num2):
#         result = num1+num2
#         print(result)
#     return test2
#
# a = test1(2)
# a(3)

# 装饰器    @方法名
# 给已有的函数增加额外的功能
# def check(fc):
#     print('检查登录')
#     def inner():
#         print('登录')
#         fc()
#     return inner
#
# @check
# def comment():
#     print('发表评论')
#
# comment()


# 类去调用
# Foo.static_method()
# Foo.class_method()
# Foo.instance_method ( 'aa ')
# 静态方法和类方法都是可以通过类去调用

# 静态方法    静态方法中没有和类相关的东西    没有self   cls
# 独立的空间   公共的区域    都可以用
import time


# class TimeTest(object):
#     def __init__(self, hour, minture, second):
#         self.hour = hour
#         self.minture = minture
#         self.second = second
#
#     @staticmethod
#     def showTime():
#         return time.strftime('%H:%M:%S', time.localtime())
#
#
# print(TimeTest.showTime())

class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print('工具对象的总数%d' % cls.count)


tool1 = Tool('锄头')
tool2 = Tool('斧头')
tool3 = Tool('棒槌')
Tool.show_tool_count()
