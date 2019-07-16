from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pymongo
import time

# will not open browser, run in backend
# browser_options = webdriver.ChromeOptions()
# browser_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=browser_options)


# we also can use PhantomJS
# browser = webdriver.PhantomJS()
# we can set parameter too
# SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
url = 'https://www.amazon.com/s?k=ipad&ref=nb_sb_noss_2'
browser.get(url)

MONGO_URL = 'localhost'
MONGO_DB = 'amazon'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(host=MONGO_URL, port=27017)
db = client[MONGO_DB]


def index_page(page):
    print('spider ', page)
    try:
        get_products()
        page += 1
        xpath = '//li/a[contains(@href, "ipad&page=' + str(page) + '")]'
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        submit.click()
    except TimeoutException:
        index_page(page)


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('.s-include-content-margin.s-border-bottom ').items()
    for item in items:
        product = {
            'image': item.find('.s-image').attr('src'),
            'price': item.find('.a-price-whole').text() + item.find('.a-price-fraction').text(),
            'title': item.find('.a-size-medium.a-color-base.a-text-normal').text(),
            'review': item.find('.a-link-normal .a-size-base').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('saved to mongodb successfully')
    except Exception:
        print('failed to save result to mongodb ')


if __name__ == '__main__':
    for page in range(1,4):
        index_page(page)
        time.sleep(3)
    browser.close()