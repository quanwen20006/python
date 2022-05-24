#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: 多继承_mro.py
@time: 2019/10/20

MRO 方法解析顺序
"""


class A:
    def __init__(self):
        print("class A")


class B:
    def __init__(self):
        print("class B")


class C(A):
    def __init__(self):
        print("class C")


class D(B):
    def __init__(self):
        print("class D")

# 宽度优先，执行顺序是Demo -> C -> A -> D -> B
class Demo(C, D):
    def __init__(self):
        print("聊天")


class E:
    def __init__(self):
        print("E")


class F(E):
    def __init__(self):
        print("E")


class H(E):
    def __init__(self):
        print("E")

# 广度优先，执行顺序是Demo1 -> H -> F-> E
class Demo1(H, F):
    def __init__(self):
        print("Demo1")


if __name__ == '__main__':
    print(Demo.__mro__)
    print(Demo1.__mro__)