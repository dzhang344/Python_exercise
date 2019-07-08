text = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class='item-0'><a href="link1.html"><span>first item</span></a></li>
<li class='item-1'><a href="link2.html">second item</a></li>
<li class='item-inactive'><a href="link3.html">third item</a></li>
<li class='item-1 active'><a href="link4.html">fourth item</a></li>
<li class='item-0'><a href="link5.html">fifth item</a>
</ul>
</div>
</div>
'''

from pyquery import PyQuery as pq

doc = pq(text)
print(doc('li'))


# doc = pq(url="https://cuiqingcai.com")
# print(doc('title'))

# same as
# import requests
# doc = pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))

# doc = pq(filename='dome.html')
# print(doc('li'))

doc = pq(text)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

items = doc('.list')
print(items)
# all child node
lis = items.find('li')
print(lis)
# direct child node
lis = items.children()
print(lis)
lis = items.children('.item-inactive')
print(lis)

container = items.parent()
print(container)


parents = items.parents()
print(parents)

parent = items.parents('.wrap')
print(parent)

li = doc('.list .item-inactive')
print(li.siblings())

li = doc('.list .item-inactive')
print('------------------sibling item 0 --------------------------')
print(li.siblings('.item-1'))

li = doc('.item-1.active')
print(li)
print(str(li))

lis = doc('li').items()
for li in lis:
    print(li, type(li))


a = doc('.item-1.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)

a = doc('a')
for item in a.items():
    print(item.attr('href'))

a = doc('.item-1.active a')
print(a.text())

li = doc('.item-1.active')
print(li)
print(li.html())

li = doc('li')
# get several items, html just return first item
print(li.html())
#  text result all items text
print(li.text())


li = doc('.item-1.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

li.attr('name', 'link')
print(li)
li.removeAttr('name')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)


html = '''
<div class="wrap">
Hello World
<p>This is a paragraph.</p>
</div>
'''

doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())

wrap.find('p').remove()
print(wrap.text())

# other operations like append(), empty() and prepend()

print('------------------selections --------------------------')
doc = pq(text)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)
