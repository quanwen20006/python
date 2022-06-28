#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: 上下文管理器.py
@time: 2019/10/24

with语句
try
except -- 如果except里面有return，先把return的结果放到堆栈，再执行finally的内容，
如果finally有return，就使用finally里面的return，如果没有就使用之前堆栈里面的return结果
finally
"""


def exe_try():
    try:
        print("code started")
        raise KeyError
    except KeyError as e:
        print("key error")
        return 2
    else:
        print("other error")
        return 3
    finally:
        print("finally")
        return 4


# 上下文管理协议-需要实现 __enter__ 和 __exit__ 两个魔法函数，实现后就可以使用with来调用
class Sample(object):
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print("do someing")


# 使用contentlib的版本（）
# 使用 contextlib.contextmanager 来创建上下文管理器
'''
1： 使用 @contextlib.contextmanager 装饰函数
2：函数体需要有迭代器
'''
import contextlib


@contextlib.contextmanager
def file_opens(file_name):
    print("file open")
    yield {}
    print("file end")


if __name__ == '__main__':
    # result = exe_try()
    # print(result)
    #
    # with Sample() as sample:
    #     sample.do_something()
    #
    # with open('../../chapter04/animal.py') as f:
    #     t = f.readlines()
    #     print("open --- file content: ", t)


    print("使用@contextlib.contextmanager实现上下文管理器")
    with file_opens("123.txt") as f:
        print("file open --- file process")