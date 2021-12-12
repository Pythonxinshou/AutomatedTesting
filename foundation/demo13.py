# -*- coding:utf-8 -*-
# @Time : 2021/11/23 21:06
# @Author : 朱树剑
# @File : demo13.py

# 冒泡排序
def maopao(list1):
    for i in range(1, len(list1)):
        for j in range(len(list1)-i+1):
            if int(list1[j]) > int(list1[i]):
                print(list1[j], list1[i])
                list1[j], list1[i] = list1[i], list1[j]
                print(list1[j], list1[i])
    return list1


list1 = [8, 6, 5, 4, 2]
print(maopao(list1))


list1.sort()