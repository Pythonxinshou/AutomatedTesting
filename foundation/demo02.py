# -*- coding:utf-8 -*-
# @Time : 2021/11/13 20:34
# @Author : 朱树剑
# @File : demo02.py

# def bigger(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# a = bigger(5, 8)
# print(a)
# a = bigger(9, 8)
# print(a)
# a = bigger(5, 5)
# print(a)

# def list_odd(list1):
#     list2=[]
#     for i in range(len(list1)):
#         if i%2!=0:
#             list2.append(list1[i])
#     return list2
#
# list1=[34,23,52,352,352,3523,5]
# print(list_odd(list1))

# def bigger(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# a = bigger(5, 8)
# print(a)
# a = bigger(9, 8)
# print(a)
# a = bigger(5, 5)
# print(a)

# def list_len(list2):
#     if len(list2)>5:
#         list2 = list2[:5]
#     return list2
#
# list2=[34,23,52,352,352,666,3523,5]
# print(list_len(list2))
#
# list2=[34,23,52]
# print(list_len(list2))

# def str_null(str1):
#     a = False
#     if str(str1).find(' '):
#         a = True
#     return a
#
# str1 = 'hello world'
# print(str_null(str1))

def bigger(x, y):
    if x > y:
        return x,y
    else:
        return y,x

# a=1 b=2 c=3
def bigest(a, b, c):
    a, b = bigger(a, b) #bigger(1,2)=2,1
    b, c = bigger(b, c)
    a, b = bigger(a, b)
    return a, b, c


print(bigest(1, 2, 3))
