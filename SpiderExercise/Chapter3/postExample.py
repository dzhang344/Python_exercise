import urllib.parse
import urllib.request

# convert to bytes
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# timeout unit is second
# timeout = 1, if app does not get response in 1 second, return URLError exception
response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.001)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')