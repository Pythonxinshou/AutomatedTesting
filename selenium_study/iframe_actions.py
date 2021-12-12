# -*- coding:utf-8 -*-
# @Time : 2021/11/30 21:00
# @Author : 朱树剑
# @File : iframe_actions.py
'''
    页面元素操作时，可能会遇到有的内嵌窗体，工frame
    弹出新页面时，driver还是操作着原来的页面，是因为有句柄的存在
    一个页面==一个句柄
    操作新的页面，就需要切换到新的句柄，是一个固化的模式
        1．获取所有句柄
        2．切换到新的句柄
    PS:如果要关闭原有的标签页，操作新的页面:
        1．获取所有句柄
        2．关闭原有标签页3．切换到新句柄
    PPS:
'''
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
sleep(2)
driver.get('http://music.163.com')
driver.implicitly_wait(10)
driver.find_element('link text', '登录').click()
driver.find_element('link text', '选择其他登录模式').click()
driver.find_element('id', 'j-official-terms').click()
driver.find_element('link text', 'QQ登录').click()
sleep(2)
print(driver.title)
# 切换句柄
handles = driver.window_handles  # 获取当前所有句柄
print(handles)
# 关闭当前标签页
# driver.close()
driver.switch_to.window(handles[1])  # 切换到新的句柄页
print(driver.title)

# 切换到iframe：通过id，name直接切换iframe，也可以定位iframe元素，将元素作为参数传递
driver.switch_to.frame('ptlogin_iframe')
# driver.switch_to.frame(driver.find_element('id','ptlogin_iframe'))
driver.find_element('id','img_out_476241259').click()
# 从iframe切换到默认内容
driver.switch_to.default_content()
# 切换原句柄
sleep(1)
driver.switch_to.window(handles[0])
print(driver.title)