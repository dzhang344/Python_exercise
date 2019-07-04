import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

r = requests.get('https://www.baidu.com')
print(r.cookies)

for key, value in r.cookies.items():
    print(key + '=' + value)


s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

response = requests.get('https://www.12306.cn')
print(response.status_code)


from requests.packages import urllib3

# disable warning
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# use local key and crt to pass SSL, key must be clear code明码
# response = requests.get('https://www.12306.cn', cert('/path/server.crt', '/path/key'))


# timeout
# connect and read, can set timeout time seperately
# r = requests.get('https://www', timeout=(5, 11, 30))

# authorization
# import requests
# from requests.auth import HTTPBasicAuth
#
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)

# another way to auth
# r = requests.get('http://localhost:5000', auth=('username', 'password'))

# OAuth auth
# from requests_oauthlib import OAuth1
# url = 'https://www.baidu.com'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)

from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 '
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)