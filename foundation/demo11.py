# -*- coding:utf-8 -*-
# @Time : 2021/11/17 20:04
# @Author : 朱树剑
# @File : demo11.py

# class Animal:
#     def eat(self):
#         print('动物有吃的功能')
#
#     def sleep(self):
#         print('动物有睡的功能')
#
#
# class Dog:
#     def eat(self):
#         print('狗有吃的功能')
#
#     def sleep(self):
#         print('狗有睡的功能')
#
#     def run(self):
#         print('狗有跑的功能')
#
#
# erha = Dog()
# erha.eat()
# erha.sleep()
# erha.run()

# class Animal:
#     def eat(self):
#         print('动物有吃的功能')
#
#     def sleep(self):
#         print('动物有睡的功能')
#
#
# class Dog(Animal):
#     def run(self):
#         print('狗有跑的功能')
#
#
# erha = Dog()
# erha.eat()
# erha.sleep()
# erha.run()


# 多重继承
# class Animal:
#     def eat(self):
#         print('吃')
#
#     def sleep(self):
#         print('睡')
#
#
# class Dog(Animal):
#     def run(self):
#         print('跑')
#
# class CommonDog(Dog):
#     def catch(self):
#         print('抓老鼠')
#
# class GodDog(Dog):
#     def fly(self):
#         print('飞')
#
#
# xtq = GodDog()
# xtq.eat()
# xtq.sleep()
# xtq.run()
# xtq.fly()


# 多继承
# class A:
#     def demoA(self):
#         print('A')
#
# class B:
#     def demoB(self):
#         print('B')
#
# class C(A,B):
#     pass
#
# c= C()
# c.demoA()
# c.demoB()


# class Master:
#     def __init__(self):
#         self.peifang = '师傅的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}制作蛋糕')
#
#
# class Schoole:
#     def __init__(self):
#         self.peifang = '学校的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}制作蛋糕')
#
#
# # 多继承，优先继承第一个类的属性和方法
# class Myself(Master, Schoole):
#     def __init__(self):
#         self.peifang = '自己的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}制作蛋糕')
# myself = Myself()
# myself.make_cake()

# 子类的重写，子类会覆盖父类同名的方法和属性


# super()   只能指向的一个父类
# class Master:
#     def __init__(self):
#         self.peifang = '师傅的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}制作蛋糕')
#
#
# class Schoole(Master):
#     def __init__(self):
#         self.peifang = '学校的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}制作蛋糕')
#         super().__init__()
#         super(Schoole, self).make_cake()
#
#
# # 多继承，优先继承第一个类的属性和方法
# class Myself(Schoole):
#     def __init__(self):
#         self.peifang = '自己的蛋糕配方'
#
#     def make_cake(self):
#         print(f'使用{self.peifang}制作蛋糕')
#         super().__init__()
#         super(Myself, self).make_cake()
#
#
# myself = Myself()
# myself.make_cake()


# 私有
# class Girl:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 18
#
#     def __desc(self):
#         print(f'大家好，我是{self.name}，年龄{self.__age}')
#
#
# class SmartGirl(Girl):
#     def sgirl(self):
#         print(f'大家好，我是:{self.name}，年龄{self.__age}')

#
# # 私有属性和方法不能在外部访问
# # qiuqiu = Girl('qq')
# # print(qiuqiu.__age)
# # qiuqiu.__desc()
#
# # jj = SmartGirl('啾啾')
# # jj.sgirl()
#
# 伪私有   并没有真正意义上的私有
# g = Girl('秀秀')
# print(g._Girl__age)
# g._Girl__desc()


# 多态:值的是同一类型的事物，有不同的形态
# 传入不同的对象，产生不同的结果动物类，动物创建猫，狗，猪会有不同形态

# 多态的定义:子类重写父类的方法，调用不同子类对象的相同父类方法，产生不同结果
# 子类重写父类的方法  两个类   最好是要去继承    不继承
# 调用不同的子类对象的相同父类的方法   父类  子类

# 多态的步骤：
# 定义父类
# 定义子类
# 子类对象给调用者，执行后可以看到不同子类执行的效果，也会不同

# class Dog:
#     def __init__(self,name):
#         self.name = name
#
#     def work(self):
#         print('看守家门')
#
# class BigDog(Dog):
#     def work(self):
#         print('抓小偷')
#
# class SmartDog(Dog):
#     def work(self):
#         print('缉毒')
#
# class Person:
#     def with_dog(sel, obj):
#         print(f'警员和{obj.name}一起去干什么')
#         obj.work()
#
# #要求狗和人一起    缉毒    抓小偷   传参    狗对象传人里面
# #调用不同的对象    会有不同的形态
#
# #创建一个狗对象
# xiaoqi=BigDog('神犬小七')
# erha=SmartDog('二哈')
#
# p=Person()
# p.with_dog(xiaoqi)
# p.with_dog(erha)

class Duck:
    def fly(self):
        print('鸭子会飞')

class Swan:
    def fly(self):
        print('天鹅会飞')

class Plan:
    def fly(self):
        print('飞机会飞')

def fly(obj):
    obj.fly()

d=Duck()
fly(d)