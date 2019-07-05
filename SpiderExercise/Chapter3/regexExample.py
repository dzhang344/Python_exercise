import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())


# how to use .* greedy match
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())


# hot to use .*? lazy match
content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^He.*?(\d+).*?World', content)
print(result)
print(result.group(1))

# if use lazy match at the end, may not get anything
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)
print('result1', result1.group(1))
print('result2', result2.group(1))


content = '''Hello 1234567 World_This is
 a Regex Demo'''
print(len(content))
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))

content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)

content = 'Extra stings Hello 1234567 World_This is a Regex Demo'
result = re.search('He.*?(\d+).*?World', content)
print(result)


# re.findall()   find all results that matches the regex


content = 'fsd98f0s834i09d8f09sd0f98'
content = re.sub('\d+', '', content)
print(content)


# compile
# compile can pass re.S re.I
content1 = '2006-12-15 12:00'
content2 = '2016-12-17 12:55'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
print(result1, result2)