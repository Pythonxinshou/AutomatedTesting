# -*- coding:utf-8 -*-
# @Time : 2021/11/29 21:18
# @Author : 朱树剑
# @File : selenium_locate_with.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
# time.sleep(5)
# 定位输入框
el = driver.find_element('xpath','//input[@id="kw"]')
# el.send_keys('selenium')
# 定位右侧元素
search = driver.find_element(locate_with(By.TAG_NAME,'input').to_right_of(el))
# search.click()

# 定位左侧元素
search = driver.find_element(locate_with(By.TAG_NAME,'input').to_left_of(el))

# 定位上方元素
img = driver.find_element(locate_with(By.TAG_NAME,'img').above(el))
print(img)

# 定位下方元素
div = driver.find_element(locate_with(By.TAG_NAME,'div').below(el))
print(div.text)

# 临近元素
span = driver.find_element(locate_with(By.TAG_NAME,'span').near(el))
print(span)

to_left_of
to_right_of
above
below
near