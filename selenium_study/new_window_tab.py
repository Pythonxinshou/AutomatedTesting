# -*- coding:utf-8 -*-
# @Time : 2021/11/30 22:24
# @Author : 朱树剑
# @File : new_window_tab.py
"""
    Selenium4.0新增的关于浏览器与标签页的管理
    new_window只支持4.0及以上版本
"""
from selenium import webdriver

driver = webdriver.Chrome()
handles = driver.window_handles
print(handles)
# 新增一个浏览器或句柄页  默认：tab，参数可选：window
driver.switch_to.new_window('window')
handles = driver.window_handles
print(handles)

driver.get('http://www.baidu.com')
