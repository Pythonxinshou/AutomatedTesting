# # -*- coding:utf-8 -*-
# # @Time : 2021/11/23 14:34
# # @Author : 朱树剑
# # @File : demo_12.py
# # @Software: PyCharm
#
# # def check(fc):
# #     print('1')
# #     def inner():
# #         print('2')
# #         fc()
# #     return inner
# #
# # def comment():
# #     print('3')
# #
# # c = check(comment)
# # c()
#
# def check(fc):
#     print('1')
#
#     def inner():
#         print('2')
#         fc()
#
#     return inner
#
#
# @check
# def comment():
#     print('3')
#
#
# comment()

import time


# def decorate(fc):
#     def inner():
#         print(time.strftime('%Y-%m-%d %H:%M:%S'))
#         start_time = time.time()
#         a = fc()
#         print(a)
#         end_time = time.time()
#         print(time.strftime('%Y-%m-%d %H:%M:%S'))
#         print('总共花费%.2f秒' % (end_time - start_time))
#         return 2
#
#     return inner
#
#
# @decorate
# def un():
#     print('执行中')
#     time.sleep(1)
#     print('执行结束')
#     return 8
#
#
# print(un())

def decorate(fc):
    def inner(a, b, c):
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        start_time = time.time()
        a = fc(a, b, c)
        print(a)
        end_time = time.time()
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        print('总共花费%.2f秒' % (end_time - start_time))
        return 2

    return inner


@decorate
def un(a, b, c):
    print('执行中')
    time.sleep(1)
    print('执行结束')
    return a + b + c


print(un(1, 2, 3))
