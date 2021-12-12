# -*- coding:utf-8 -*-
# @Time : 2021/11/14 21:03
# @Author : 朱树剑
# @File : demo03.py
# f = open('./test.txt', 'r+',encoding='utf-8')
# f.seek(7,0)
# f.write('tttt')
# # f.seek(0,1)
# # f.write('uuuu')
# f.close()

import os

# file1 = r'E:\PycharmProjects\AutomatedTesting\foundation\aa'
# os.mkdir(file1)

# 删除文件夹   目录不为空无法删除
# os.rmdir(file1)

# 删除非空目录    shutil
# import shutil

# shutil.rmtree(file1)

# 文件重命名     rename(原文件名， 新文件名)
# os.rename('aa', 'bb')
# os.rename('test.txt', 'test99.txt')

# 获取当前文件所属文件夹的绝对路径
print(os.getcwd())
# dirname获取父目录
print(os.path.dirname(os.path.abspath(__file__)))
# 获取当前文件的绝对路径
print(os.path.abspath(__file__))

# 判断是否为目录
f = r'E:\PycharmProjects\AutomatedTesting\foundation'
print(os.path.isdir(f))
# 判断是否为文件
print(os.path.isfile(f))
print(os.path.isfile(f+r'\demo03.py'))