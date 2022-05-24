#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: super关键字.py
@time: 2019/10/24

使用 super() 可以调用 __mro__的下一个的方法

super执行顺序是按__mro__来的

"""

class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


class Student(Person):
    def __init__(self, name, sex, age, grade):
        self.grade = grade
        super().__init__(name, sex, age)


if __name__ == '__main__':
    b = Student("Jack", "Male", 23, "三年级")
    print(b.grade, b.name)