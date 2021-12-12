# -*- coding:utf-8 -*-
# @Time : 2021/12/12 22:53
# @Author : 朱树剑
# @File : case_demo.py
"""
测试代码的内容编写与类的管理。
调用关键字驱动类实现自动化效果
"""

from Web_Keys.web_keys.keys import Keys

# 百度搜索业务流程
key = Keys('Chrome')
key.open('http://www.baidu.com')
key.input('id', 'kw', '虚竹')
key.click('id', 'su')
