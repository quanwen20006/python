#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         dict_abc
# Description:  
# Author:       quanwen
# Date:         2019/10/28
# -------------------------------------------------------------------------------
from collections.abc import Mapping

a = {"test1": {"company": "imooc"}, "test2": {"company": "imooc2"}}


# print(a.clear())

# 浅拷贝
new_dict = a.copy()
new_dict["test1"]["company"] ="imooc1"
print("a: %s new_dict: %s" % (a, new_dict))


# 深拷贝
import copy
new_dict = copy.deepcopy(a)
new_dict["test1"]["company"] ="imooc5"
print("a: %s new_dict: %s" % (a, new_dict))

# fromkeys
new_list = ["test3", "test4"]
new_dict = a.fromkeys(new_list, {"company": "imooc"})
print("new_dict fromkeys ", new_dict)

# setdefault
new_dict.setdefault("test5", "imooc")
print("new_dict setdefault ", new_dict)

# update
new_dict.update((("test6", "imooc"), ("test7", "imooc")))
new_dict.update([("test16", "imooc"), ("test17", "imooc")])
new_dict.update(c="x1", b="x2")
print("new_dict update ", new_dict)

