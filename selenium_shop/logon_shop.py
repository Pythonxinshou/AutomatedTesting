# -*- coding:utf-8 -*-
# @Time : 2021/11/29 22:09
# @Author : 朱树剑
# @File : logon_shop.py
from selenium import webdriver

# 创建webdriver对象
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(5)
# 访问地址
driver.get('http://39.98.138.157/shopxo/index.php')

# 点击登录按钮
logon = driver.find_element('xpath', '//a[text()="登录"]')
logon.click()
# 登录
driver.find_element('xpath', '//input[@name="accounts"]').send_keys('xiarenzhuxin')
driver.find_element('xpath', '//input[@name="pwd"]').send_keys('ZSJ1224')
driver.find_element('xpath', '//button[text()="登录"]').click()
# 搜索选择商品
driver.find_element('xpath', '//input[@name="wd"]').send_keys('iphone 6')
driver.find_element('xpath', '//input[@value="搜索"]').click()
driver.find_element('xpath', '//img[@class="goods-images"]').click()
# driver.find_element('xpath', '//li[@data-value="套餐二"]').click()
link_2 = WebDriverWait(driver, 10, 0.5).until(
    lambda el: driver.find_element('xpath', '//li[@data-value="套餐二"]'), message='套餐二查找失败'
)
link_2.click()
# driver.find_element('xpath', '//li[@data-value="银色"]').click()
link_silvery = WebDriverWait(driver, 10, 0.5).until(
    lambda el: driver.find_element('xpath', '//li[@data-value="银色"]'), message='银色查找失败'
)
link_silvery.click()
# driver.find_element('xpath', '//li[@data-value="64G"]').click()
link_64 = WebDriverWait(driver, 10, 0.5).until(
    lambda el: driver.find_element('xpath', '//li[@data-value="64G"]'), message='64G查找失败'
)
link_64.click()
driver.find_element('xpath', '//input[@type="number"]').send_keys('1')
driver.find_element('xpath', '//button[@title="加入购物车"]').click()
link_success = driver.find_element('xpath', '//p[text()="加入成功"]')
print(link_success)