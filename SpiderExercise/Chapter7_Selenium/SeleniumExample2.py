from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('mq')
# input_second = browser.find_element_by_css_selector('#mq')
# input_third = browser.find_element_by_xpath('//*[@id="mq"]')
# print(input_first, input_second, input_third)
input_first.send_keys('iPhone')
time.sleep(1)
input_first.clear()
input_first.send_keys('iPad')
button = browser.find_element_by_xpath('//*[@title="提交"]')
button.click()


browser.close()