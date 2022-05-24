# _*_ coding:utf-8 _*_
# @time  : 2020/8/21 15:36
# @Author: quanwen
# @File  :
from pyquery import PyQuery as pq

html='''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">基础知识-item</li>
            <li class="item-1"><a href="link2.html">文件 item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">thrid item</span></a></li>
            <li class="item-0 actives abc"><a href="link3.html"><span class="bold">thrid item</span></a></li>
            <li class="item-1 active"><a href="link4.html">forth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</li>
        </ul>
    </div>
</div>
'''
# 初始化(有3种途径 字符串 url filename)
doc = pq(html)
# doc = pq(filename='demo.html')

print(doc('li'))
# url初始化
# doc = pq(url='http://www.baidu.com')
# print(doc('head'))
# print(doc('title'))

# css 选择器
print('css 选择器: ', doc('#container .list li'))

# 查找 子元素
items = doc('.list')
print('items: ',items)
its = items.find('li')
print('its: ',its)

lis = items.children('.active')
print('lis-children: ',lis)

# 父元素
items = doc('.list')
container = items.parent()
print('父元素: ',container)
# 多层级父元素查找
container = items.parents('.wrap')
print('父元素: ',container)

# 兄弟元素
li = doc(".list .item-0.active")
print('兄弟元素: ',li)
print('兄弟元素(所有的): ',li.siblings())
print('兄弟元素(class有active的): ',li.siblings('.active'))


# 遍历元素
lis = doc('li').items()
for item in lis:
    print('遍历元素item: ',item)

# 获取信息
a = doc('.item-0.active a')
print('获取信息 ',a.attr('href'))
print('获取信息 ',a.attr.href)
print('获取文本 ',a.text())
print('获取html ',a.html())

# dom操作
# addclass removeclass
li = doc('.item-0.active')
print('li: ',li)
li.removeClass('active')
print('li: ',li)
li.addClass('active')
print('li: ',li)

# attr css
li.attr('name','link')
print('li: ',li)
li.css('font-size','14px')
print('li: ',li)

# remove
html1='''
<div class="wrap">
    Hello,World
    <p>This is a paragraph.</p>
</div>
'''
doc = pq(html1)
wrap = doc('.wrap')
print('wrap: ',wrap)
print('text: ',wrap.text())
wrap.find('p').remove()
print('text: ',wrap.text())

# 伪类选择器
doc = pq(html)
li = doc('li:基础知识-child')
print('li-伪类选择器: ',li)
li = doc('li:nth-child(2)')
print('li-伪类选择器: ',li)
li = doc('li:last-child')
print('li-伪类选择器: ',li)
li = doc('li:gt(2)')
print('li-伪类选择器: ',li)


