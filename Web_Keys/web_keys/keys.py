# -*- coding:utf-8 -*-
# @Time : 2021/12/12 21:29
# @Author : 朱树剑
# @File : keys.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from Web_Keys.options_web.chrome_options import options


def open_browser(text):
    if text == 'Chrome':
        # driver = webdriver.Chrome(options=options())
        driver = webdriver.Chrome()
        try:
            driver = getattr(webdriver, text)()
        except Exception as e:
            print(e)
            driver = webdriver.Chrome()
    return driver


class Keys:
    def __init__(self, text):
        self.driver = open_browser(text)
        # 隐式等待
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self, text):
        self.driver.get(text)

    # 查找元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 点击
    def click(self, name, value):
        self.locate(name, value).click()

    # 点击
    def input(self, name, value, text):
        self.locate(name, value).send_keys(text)

    # 退出
    def quit(self):
        self.driver.quit()

    # 显式等待
    def web_el_wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.locate(name, value), message='元素查找失败'
        )

    # 强制等待
    @staticmethod
    def wait(text):
        sleep(text)

    # 切换Iframe
    def switch_frame(self, value, name=None):
        if name is None:
            return self.driver.switch_to.frame(value)
        else:
            return self.driver.find_element(name, value)

    # 相对定位器
    def relative(self, method, value, el_ame, el_value, direction):
        el = self.locate(el_ame, el_value)
        relative_dict = {
            'left': 'to_left_of',  # 左侧
            'right': 'to_right_of',  # 右侧
            'above': 'above',  # 上方
            'below': 'below',  # 下方
            'near': 'near'  # 靠近
        }
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
                return self.driver.find_element(getattr(
                    locate_with(method_dict.get(method), value), relative_dict.get(direction))(el))
            else:
                print('method: ' + str(method) + ' 方法不存在')

    # 断言文本信息:可以捕获异常进行处理，也可以不捕获，因为报错就相当于断言失败。
    def assert_text(self, name, value, expect):
        try:
            reality = self.locate(name, value).text
            assert expect == reality, '断言失败，实际结果为:{}'.format(reality)
            return True
        except Exception as e:
            print('断言失败信息:' + str(e))
            return False
        # reality = self.locate(name, value).text
        # assert expect == reality, '断言失败，实际结果为:}'.format(reality)

    # 关闭当前句柄
    def close(self):
        self.driver.close()

    # 句柄切换
    def handles(self, value):
        self.driver.switch_to.window(self.driver.window_handles[value])

# # 切换句柄
# handles = driver.window_handles  # 获取当前所有句柄
# print(handles)
# # 关闭当前标签页
# # driver.close()
# driver.switch_to.window(handles[1])  # 切换到新的句柄页
# print(driver.title)
