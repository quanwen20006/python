#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: 自省机制.py
@time: 2019/10/24

自省 是通过一定的机制查询到对象到内部结构-属性或方法
"""


class Person(object):
    name = "ren"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student("雅礼中学")
    print(user.__dict__)
    user.__dict__["school_addr"] = "长沙市"
    print(user.school_addr)
    print(Student.__dict__)
    print(user.name)
    print("通过dir打印对象的属性： ", dir(user))