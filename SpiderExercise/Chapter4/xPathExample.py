from lxml import etree
# missing </li>, but etree will add it auto
text = '''
<div>
<ul>
<li class='item-0'><a href="link1.html">first item</a></li>
<li class='item-1'><a href="link2.html">second item</a></li>
<li class='item-inactive'><a href="link3.html">third item</a></li>
<li class='item-1'><a href="link4.html">fourth item</a></li>
<li class='item-0'><a href="link5.html">fifth item</a>
</ul>
</div>
'''


html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))


result = html.xpath('//*')
print(result)

result = html.xpath('//li')
print(result)

result = html.xpath('//li/a')
print(result)
# / get direct child node, // get all child node
result = html.xpath('//ul//a')
print(result)

# .. or parent:: to get parent node
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

result = html.xpath('//li[@class="item-0"]')
print(result)

result = html.xpath('//li[@class="item-0"]/text()')
print(result)

result = html.xpath('//li[@class="item-0"]//text()')
print('//li[@class="item-0"]//text() = ', result)

result = html.xpath('//li[@class="item-0"]/a/text()')
print('//li[@class="item-0"]/a/text() = ', result)

result = html.xpath('//li/a/@href')
print('//li/a/@href = ', result)

text = '''
<li class='li li-first' name='item'><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print("//li[contains(@class, 'li')]/a/text() = ", result)

result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print('//li[contains(@class, "li") and @name="item"]/a/text() = ', result)


text = '''
<div>
<ul>
<li class='item-0'><a href="link1.html">first item</a></li>
<li class='item-1'><a href="link2.html">second item</a></li>
<li class='item-inactive'><a href="link3.html">third item</a></li>
<li class='item-1'><a href="link4.html">fourth item</a></li>
<li class='item-0'><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print('//li[1]/a/text() = ', result)
result = html.xpath('//li[last()]/a/text()')
print('//li[list()]/a/text() = ', result)
# position less than 3 not include 3
result = html.xpath('//li[position()<3]/a/text()')
print('//li[position()<3]/a/text() = ', result)
# third from last
result = html.xpath('//li[last()-2]/a/text()')
print('//li[last()-2]/a/text() = ', result)

text = '''
<div>
<ul>
<li class='item-0'><a href="link1.html"><span>first item</span></a></li>
<li class='item-1'><a href="link2.html">second item</a></li>
<li class='item-inactive'><a href="link3.html">third item</a></li>
<li class='item-1'><a href="link4.html">fourth item</a></li>
<li class='item-0'><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print('//li[1]/ancestor::* = ', result)
result = html.xpath('//li[1]/ancestor::div')
print('//li[1]/ancestor::div = ', result)
result = html.xpath('//li[1]/attribute::*')
print('//li[1]/attribute::* = ', result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print('//li[1]/child::a[@href="link1.html"] = ', result)
result = html.xpath('//li[1]/descendant::span')
print('//li[1]/descendant::span = ', result)
# the second following node
result = html.xpath('//li[1]/following::*[2]')
print('//li[1]/following::*[2] = ', result)
result = html.xpath('//li[1]/following-sibling::*')
print('//li[1]/following-sibling::* = ', result)