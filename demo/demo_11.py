from selenium import webdriver

driver = webdriver.Chrome()

alert = driver.switch_to.alert()
alert.text()  # 获取对话框文本值
alert.accept()  # 相当于点击“确认”
alert.dismiss()  # 相当于点击“取消”
alert.send_keys()  # 输入值（alert和confirm没有输入对话框，所以就不用能用了，只能使用在prompt里）
