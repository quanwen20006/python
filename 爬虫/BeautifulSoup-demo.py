# _*_ coding:utf-8 _*_
# @time  : 2020/8/18 09:33
# @Author: quanwen
# @File  : BeautifulSoup的使用学习
from bs4 import BeautifulSoup

html='''
<html>
    <head>
        <title>The document's story</title>
    </head>
    <body>
        <p class="title" name="dromouse"><b>The Dromouse's story</b>
            Once upon a time there were three little sister;and their name were
            <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
            <a href="http://example.com/lacle" class="sister" id="link2">Lacle</a>
            <a href="http://example.com/lily" class="sister" id="link3">Lily</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
    </body>
</html>
'''

soup = BeautifulSoup(html,'lxml')
# 格式化为html格式代码
print('prettify---', soup.prettify())
print('title---- ',soup.title.string)

# 标签选择器
print('head---- ',soup.head)
# 第一个p节点
print('p----', soup.p)

# 获取属性
print(soup.p.attrs['name'])
print(soup.p['name'])

# 获取内容
print('p.string ',soup.p.string)

# 嵌套选择
print('嵌套选择 ',soup.head.title.string)

# 子节点 子孙节点
print('子节点 ',soup.p.contents)
print('子节点 ',soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i,child)

print('子孙节点descendants ',soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)

# 父节点 祖先节点
print('父节点： ',soup.a)
print('父节点： ',soup.a.parent)
print('祖先节点： ',soup.a.parents)
for i,child in enumerate(soup.a.parents):
    print(i,child)


# 兄弟节点
print('后面的兄弟节点： ',soup.a.next_siblings)
for i,child in enumerate(soup.a.next_siblings):
    print('后面的兄弟节点： ',i,child)

print('前面的兄弟节点： ',soup.a.previous_siblings)
for i,child in enumerate(soup.a.previous_siblings):
    print('前面的兄弟节点： ',i,child)


# 标准选择器
html='''
<div class="panel">
    <div class="panel-head">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foos</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html,'lxml')
print(soup.find_all('ul'))
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
# attrs 根据属性来查找元素 --find_all 返回多个元素
print('attrs: ',soup.find_all(attrs={'id':'list-1'}))
print('attrs: ',soup.find_all(attrs={'name':'elements'}))

# 使用class来查找元素
print('根据class属性来查找元素（使用的时候clas需要加下划线）: ',soup.find_all(class_='element'))

# 根据 text来查找元素
print(soup.find_all(text='Foo'))

# 使用find来查找元素(如果查找不存在的元素就返回None)
print('使用find来查找元素: ',soup.find('ul'))

# css 选择器
# select传入css选择器即可以选择元素
print('css选择器： ',soup.select('.panel .panel-head'))
print('css选择器： ',soup.select('ul li'))
print('css选择器： ',soup.select('#list-2  .element'))

# 获取属性
for ul in soup.select('ul'):
    print('获取属性 ',ul['id'])
    print('获取属性 ',ul.attrs['class'])

# 获取内容
for item in soup.select('li'):
    print('获取内容 ',item.get_text())
