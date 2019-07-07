from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

soup = BeautifulSoup(html, 'lxml')
# prettify 进行缩进处理
print(soup.prettify())
print(soup.title.string)
print(soup.title)
print(type(soup.title))
print(soup.head)
# pick the first p tag
print(soup.p)
# get tag name
print(soup.title.name)
# get tag attributes
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
# class is a list
print(soup.p['class'])

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)


# get all child node
# 0 Once upon a time there were three little sisters; and their names were
#
# 1 <a class="sister" href="http://example.com/elsie" id="link1"><span>Elsie</span></a>
# 2 <span>Elsie</span>
# 3 Elsie
# 4
#
# 5 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# 6 Lacie
# 7  and
#
# 8 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# 9 Tillie
# 10 ;
# and they lived at the bottom of a well.
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# get direct parent node
print(soup.a.parent)
# get all parent nodes
print(soup.a.parents)
print(list(enumerate(soup.a.parents)))

print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))

print('Parent:')
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])


html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

# another way to pass attrs
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))

import re
print(soup.find_all(text=re.compile('Foo')))

# return first result
print(soup.find(name='ul'))
print(soup.find(class_='list'))


print(soup.select('.panel .panel-heading'))
# all li nodes under ul nodes
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))

for ul in soup.select('ul'):
    print(ul.select('li'))

for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)
