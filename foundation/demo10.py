# -*- coding:utf-8 -*-
# @Time : 2021/11/16 20:56
# @Author : 朱树剑
# @File : demo10.py

# class Cat:
#     cat_color='白色'
#     cat_foot=4
#     cat_weight=20
#
#     def eat(self):
#         print(f'{self.name}小猫爱吃鱼')
#
#     def catch(self):
#         print(f'{self.name}小猫会抓老鼠')
#
# Tom = Cat()
# Tom.name='Tom'
# Tom.catch()
#
# Jack = Cat()
# Jack.name='Jack'
# Jack.eat()

# class Cat:
#     def __init__(self):
#         self.color = '白色'
#         self.foot=4
#
#     def eat(self):
#         print(f'{self.name},{self.color}小猫爱吃鱼')
#
#     def catch(self):
#         print('小猫会抓老鼠')
#
# Tom1 = Cat()
# Tom1.name='Tom'
# Tom1.eat()

class Cat:
    def __init__(self, color, foot, name):
        self.color = color
        self.foot = foot
        self.name = name

    def eat(self):
        print(f'{self.name}，{self.color}小猫爱吃鱼')

    def __str__(self):
        return f'这是一个对象的描述信息：{self.name}小猫爱吃鱼'


c = Cat('大红色', 4, '小翠花')
print(c)

# 怎么创建类  属性  方法  方法里面一定会加上self self代表创建的对象模板
# 具体的创建对象    实例化对象   对象名=类()
# 属性     方法      对象名.属性      对象名.方法()
# init函数    作用:创建对象的时候就执行init函数
# str函数    作用:返回对象的描述信息
# del函数    作用:销毁对象
