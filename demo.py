# -*- coding:utf-8 -*-
# @Time : 2021/12/6 23:24
# @Author : 朱树剑
# @File : demo.py
from selenium.webdriver.common.by import By


def pp(method):
    if isinstance(method, str):
        method_dict = {
            'id': By.ID,
            'xpath': By.XPATH,
            'link text': By.LINK_TEXT,
            'partial link text': By.PARTIAL_LINK_TEXT,
            'name': By.NAME,
            'tag name': By.TAG_NAME,
            'class name': By.CLASS_NAME,
            'css selector': By.CSS_SELECTOR,
        }
        if method in method_dict:
            print(method)

pp('str')
pp('xpath')
pp('id')