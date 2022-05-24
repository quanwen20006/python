# _*_ coding:utf-8 _*_
# @time  : 2021/1/13 12:13
# @Author: quanwen
# @File  :

'''
浅拷贝 不拷贝子对象的内容，只拷贝子对象的引用(子对象不拷贝)
深拷贝 拷贝连对象的内容也拷贝一份，对子对象对修改不会影响源对象
'''

import copy

a = [10,30,[4,5,6]]
b = copy.copy(a)
c = copy.deepcopy(a)
print('a: {0}'.format(a))
print('b: {0}'.format(b))
print('c: {0}'.format(c))

b.append(40)
c.append(100)
b[2].append(99)
c[2].append(999)
print('浅拷贝.....')
print('a: {0}'.format(a))
print('b: {0}'.format(b))

print('深拷贝.....')
print('a: {0}'.format(a))
print('c: {0}'.format(c))
