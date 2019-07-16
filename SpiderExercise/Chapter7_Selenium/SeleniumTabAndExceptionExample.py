import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.taobao.com/')
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://python.org')
except TimeoutException:
    print('Time Out')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
