#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: instance-type.py
@time: 2019/08/17
"""


class A:
    pass


class B(A):
    pass


b = B()
print("b 是不是B:%s---b是不是A:%s" % (isinstance(b, B), isinstance(b, A)))
