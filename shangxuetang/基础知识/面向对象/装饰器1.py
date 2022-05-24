# -*-coding:utf-8 -*-

'''
    装饰器的使用
    修改封闭、对扩展是开放
'''
import time
from functools import wraps


# 无返回值的装饰器
def decorator1(func):
    # 使用wraps修饰，再次使用的时候，被修饰的函数的时候，函数名不会被修改
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        re = func(*args, **kwargs)
        time.sleep(0.2)
        end = time.time()
        print(end - start)
        return re
    return wrapper

# 有返回值的装饰器


# f1函数加了注解、然后增加了新功能
@decorator1
def f1(t1):
    print('This is a function f1', t1, 'func f1\'s name is', f1.__name__)


@decorator1
def f2(t1, *args):
    # print("args", args)
    result = t1+args[0]
    print("f2的执行结果：", result)
    # print('This is a function f2', t1, ' *** ', args)
    return result


@decorator1
def f3(t1, *args, **kwargs):
    print('This is a function f3', kwargs)


f1('111')
result = f2(111, 222, 333, 444, 'ddd')
print("装饰器的返回值是：", result)
f3('111', 222, 333, a='123', b='xxx')


'''
类使用装饰器
'''


class remarkkable(object):
    def __init__(self, blanklines=0, ps="这是一个带参装饰器带demo"):
        self.blanklines = blanklines
        self.ps = ps

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            print("\n"*self.blanklines)
            print("-"*10, func.__name__, "-"*10)
            print("***", self.ps, "***" if self.ps else print(end=""))
            func(*args, **kwargs)
            print("-"*10, "END", "-"*10)
        return inner


@remarkkable(blanklines=1, ps="聊天")
def sayHello3(name, *args, boss=None, **kwargs):
    print("hello")
    print(name, args, boss, kwargs)


sayHello3("bill", "jobs", "jack马", boss="bill's wife", wife="梅琳达")
