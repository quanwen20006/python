#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: sequence_test.py
@time: 2019/10/24
"""
# 不可变对象
from _collections_abc import Sequence
# 可变对象
from _collections_abc import MutableSequence

my_list = []
my_list.append(1)
my_list.append('a')

c = my_list + [3, 4]
d = my_list + ('h3', 'h4')
print(c, d)

# 实际上调用的是 MutableSequence.__iadd__ ,然后本质上是调用 MutableSequence.extend 所以可以是列表，也可以是元祖
my_list += ['d', 'e', 'f']

my_list += ('h1', 'h2')
print(my_list)
