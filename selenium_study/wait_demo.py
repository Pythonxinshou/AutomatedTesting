# -*- coding:utf-8 -*-
# @Time : 2021/12/1 20:00
# @Author : 朱树剑
# @File : wait_demo.py
"""
        1. 强制等待
            sleep参数是以秒为单位的。
            优点:容易上手。在有需要的时候，直接调用即可。
            缺点:很蠢。造成大量的代码冗余，造成大量时间的浪费
            在日常测试中，一般情况下不会使用sleep，只有在特定场景下，或者临时性的调试下会使用sleep
            强制等待一定是time模块下的sleep，记住，是time模块
        2．隐式等待:
            本质意义上而言是driver对象的一个设置项。
            只需要设置一次即可生效，在整个driver生命周期中都有效
            implicitly_wait()参数是以秒为单位
            在页面加载完成之后，调用后续的代码，如果说没有找到对应的元素，进入隐式等待的时间周期。
            在时间周期内会一直等待该元素显示出来，如果获取成功，则继续后续的操作，
            如果超过最大时间周期仍未获取，则抛出异常。
            优点:在整个webdniver生命周期中，只需要设置一次，即可一直生效。
            缺点:如果在最大时间周期内无法找到元素，则不管了。
        3．显式等待:
            专门针对于元素来进行等待的操作行为
            和强制等待是相同的用法，需要等待的时候,就定义，不需要的时候就不定义。
            显示等待有两种不同的等待方法:until与until_not，两种方法的结果相反。
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 隐式等待：设置为具体的秒数即可
# driver.implicitly_wait(5)
driver.get('http://www.baidu.com')

driver.find_element('xpath', '//input[@id="kw"]').send_keys('虚竹')
driver.find_element('id', 'su').click()
# 显示等待，获取链接元素
link_el = WebDriverWait(driver, 10, 0.5).until(
    lambda el: driver.find_element('xpath', '//*[@id="1"]/h3/a'), message='显示等待查找失败'
)
print(link_el)
# driver.find_element('xpath', '//*[@id="1"]/h3/a').click()
# 强制等待
sleep(3)
driver.quit()