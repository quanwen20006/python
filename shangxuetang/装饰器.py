# -*-coding:utf-8 -*-

'''
    装饰器的使用
    修改封闭、对扩展是开放
'''
import time
from functools import wraps


def decorator1(func):
    # 使用wraps修饰，再次使用的时候，被修饰的函数的时候，函数名不会被修改
    print("装饰器的使用---------")
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        time.sleep(0.2)
        end = time.time()
        print(end - start)
    return wrapper


# f1函数加了注解、然后增加了新功能
@decorator1
def f1(t1):
    print('This is a function f1', t1, 'func f1\'s name is',f1.__name__)

@decorator1
def f2(t1, *agrs):
    print('This is a function f2', t1, ' *** ', agrs)

@decorator1
def f3(t1, *agrs, **kwargs):
    print('This is a function f3', kwargs)

f1('111')
f2('111', 222, 333, 444 , 'ddd')
f3('111', 222, 333, a='123', b='xxx')
