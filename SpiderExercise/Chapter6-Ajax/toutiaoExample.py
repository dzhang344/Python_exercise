# https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json
# &keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20
# &en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1562728033134

from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
import pymongo
import time
import calendar

base_url = 'https://www.toutiao.com/api/search/content/?'

headers = {
    'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 ',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(offset):
    params = {
        'aid': '24',
        # 'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        # 'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        # 'timestamp': int(round(time.time() * 1000))
    }

    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('title'):
                title = item.get('title')
                images = item.get('image_list')
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


if __name__ == '__main__':
    for page in ['0', '20']:
        json = get_page(page)
        results = get_images(json)
        for result in results:
            print(result)
        time.sleep(2)