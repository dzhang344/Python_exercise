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


from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))

from urllib.parse import urlencode

params = {
    'name': 'germey',
    'age': 22
}

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))


from urllib.parse import parse_qsl

query = 'name=germey&age=22'
print(parse_qsl(query))


from urllib.parse import quote
# convert word to url code
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
