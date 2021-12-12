# -*- coding:utf-8 -*-
# @Time : 2021/11/30 20:19
# @Author : 朱树剑
# @File : normal_actions.py
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# # 窗口最大化
# driver.maximize_window()
# # 窗口最小化
# driver.minimize_window()
# # 设置浏览器窗口大小
# driver.set_window_size(1920, 1080)
#
# get可以获取url和文件
driver.get('http://www.baidu.com')
sleep(1)
#
# # 浏览器前进，后退，刷新
# driver.forward()
# driver.back()
# driver.refresh()
#
# # 输入和点击
# driver.find_element('xpath', '//*[@id="form"]/span[1]/span[1]').click()
# 文件上传：send_keys只限于input标签的文件上传和string的输入非input标签使用AutoIT
# driver.find_element('xpath', '//*[@id="fonm"]/div/div[2]/div[2]/input').send_keys('文件地址')
'''
    下拉列表框:现如今市场上基本都是基于input和div来实现的下拉列表框
        div，通过click来进行操作
        input下拉列表框:
            1．通过click来进行操作（是推荐行为)
            2．如果有readonly，就先remove掉，再通过send_keys输入（容易出现问题）
        select标签下拉列表框:是最为传统的形式，相对有年代感的系统才会存在。
'''
# div下拉列表与鼠标悬停
el = driver.find_element('xpath', '//span[text()="设置"]')
# 导入actionchains类进行悬停操作
ActionChains(driver).move_to_element(el).perform()
# 高级搜索
driver.find_element('link text', '高级搜索').click()
sleep(1)
driver.find_element('xpath','//*[@id="adv-setting-gpc"]/div/div[1]').click()
driver.find_element('xpath','//p[text()="最近一月"]').click()
# select标签下拉列表框
select = Select(driver.find_element('id','deviceType'))
'''
<select id="deviceType" name="deviceType" class="form-control m-b">
<option value selected="selected"></option>
<option value="0">自动驾驶</option>
<option value="1">定位铺助</option>
<option value="10">无人机</option>
<option value="11">液位传感器</option>
<option value="2">物联终端</option>
<option value="3">平地机</option>
<option value="4">基站</option>
<option value="5">气象站</option>
<option value="6">土壤传感器</option>
<option value="7">摄像头</option>
'''
# 获取指定的值，进行选择
select.select_by_index(1) # 从1开始
select.select_by_value('11') # 通过value值定位
select.select_by_visible_text('液位传感器') # 文本