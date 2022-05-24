#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: animal.py
@time: 2019/08/17

类实现同一个方法，即为多态---即多个类都会飞，即为鸟类
"""


class Animal(object):
    def say(self):
        print("i'm a Animal")


class Dog(object):
    t1 = [1, 2, 3]

    def say(self):
        print("i'm a Dog")

    def __getitem__(self, item):
        return self.t1[item]

    def __len__(self):
        return len(self.t1)


class Cat(object):
    def say(self):
        print("i'm a cat")


class Duck(object):
    def say(self):
        print("i'm a Duck")


animal_list = [Animal, Cat, Dog, Duck]

for animal in animal_list:
    animal().say()

a = ['test1', 'test2']
b = ['test2', 'test3']
c = Dog()
# 传递可迭代都对象，即可进行extend，--不需要是具体都类型，即符合迭代对象都规则即可，
a.extend(b)
print(a)

a.extend(c)
print(a)

print(len(c))

from collections.abc import Sized
print(isinstance(c, Sized))
