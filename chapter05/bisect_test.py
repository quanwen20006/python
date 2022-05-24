#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: bisect_test.py
@time: 2019/10/25
biaect 可以维护序列的升序降序
1：新建的时候即可进行排序
"""

import bisect
import array

list_test = []
bisect.insort(list_test, 'm')
bisect.insort(list_test, 'f')
bisect.insort(list_test, 'c')
bisect.insort(list_test, 'd')
print(list_test)


print(bisect.bisect_left(list_test, 'g'))
print(list_test)

# 定义array，存的类型需要提前确定，即只能存一类数据，也是和list的一个区别
my_array = array.array("i")
my_array.append(1)
print(my_array)
my_array.append('c')
print(my_array)

a = list
