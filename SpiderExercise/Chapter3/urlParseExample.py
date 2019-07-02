from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(type(result), result)

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(type(result), result)


result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')


from urllib.parse import urlunparse
# parameter must be 6
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

from urllib.parse import urlunsplit
# parameter must be 5
data = ['http', 'www.baidu.com', 'index.html;user', 'a=6', 'comment']
print(urlunsplit(data))