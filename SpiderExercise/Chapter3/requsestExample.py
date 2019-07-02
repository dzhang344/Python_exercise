import urllib.request

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# data must be bytes
# headers usually used to simulate browser
# origin_req_host  request side hose name or IP address

# unverifiable default is False unverifiable should indicate whether the request is unverifiable
# An unverifiable request is one whose URL the user did not have the option to approve.
# For example, if the request is for an image in an HTML document,
# and the user had no option to approve the automatic fetching of the image, this should be true.

# method GET POST PUT

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
# another way to set header
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))