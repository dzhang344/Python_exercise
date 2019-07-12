import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(5)
browser.forward()
time.sleep(5)
browser.close()