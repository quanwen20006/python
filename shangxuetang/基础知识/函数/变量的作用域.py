# _*_ coding:utf-8 _*_
# @time  : 2021/1/13 11:39
# @Author: quanwen
# @File  :

a = 100 # 全局变量
def f1():
    b = 4
    global a # 如果要改变全局变量的值，增加global关键字申明
    print('输出局部变量：',locals())
    print('a: ', a)
    print('输出全局变量：', globals())
    a = 300

f1()
print(a)

# 测试局部变量、全局变量执行效率
import math
import time
def test02():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print('耗时{0}'.format(end-start))

def test03():
    start = time.time()
    b = math.sqrt
    for i in range(10000000):
        b(30)
    end = time.time()
    print('耗时{0}'.format(end-start))

print(test02())
print(test03())


a = [10,20]
print(id(a))
# 把可变对象给到函数，会修改可变对象原本的内容---是深拷贝
def test03(m):
    print(id(m))
    m.append(30)
    print(id(m))

test03(a)
print('可变对象作为参数： ', a)

# 把不可变对象（int，float，字符串，元组，布尔值）给到函数，会创建新的对象
# 不可变对象---是浅拷贝
a = 100
print('a: {0}'.format(id(a)))
def test04(n):
    print('n: {0}'.format(id(n)))
    n += 200
    print('n: {0}'.format(id(n)))
    print(n)
test04(a)
print('变对象作为参数： ', 'a: {0}'.format(a))

