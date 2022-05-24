#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: 切片对象.py
@time: 2019/10/24

实现一个可切片的对象
"""

# 模式 [start:end:step]
# 切片操作
alist = [1, 2, 3, 4, 5, 6, 7, 8]
print(alist[::-1])

# 赋值操作
alist[3:3] = 'a'
print(alist)
alist[::2] = [0]*5
print(alist)


'''
需要看把Group作为可修改还是不可修改的切片对象，这样需要实现的魔法函数有差别

1：如把Group设置为不可变切片，就需要实现 Sequence里面的所有 abstractmethod 方法（包括Sequence继承的）
2：切片后的结果依然是切片

不可变对象
from _collections_abc import Sequence
可变对象
from _collections_abc import MutableSequence
'''

import numbers
class Group(object):
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reversed()

    def __getitem__(self, item):
        cls = type(self)
        print('cls: ', cls)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


if __name__ == '__main__':
    staffs = ['test1', 'test2', 'test3', 'test4']
    group = Group('测试', 'Dzg', staffs)
    sub_group = group[:2]

    sub_group1 = group[0]
    print(sub_group, sub_group1)


