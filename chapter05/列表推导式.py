#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:quanwen
@file: 列表推导式.py
@time: 2019/10/25

[表达式 for 变量 in 列表]    或者  [表达式 for 变量 in 列表 if 条件]

"""

'''
1：取出1-20之间的奇数
'''

odd_list = []

for i in range(21):
    if i % 2 == 1:
        odd_list.append(i)
print("odd_list: ", odd_list)


odd1_list = [i for i in range(21) if i%2 == 1]
print("odd1_list: ", odd1_list)
'''
2：逻辑复杂的情况
'''


def handle_item(item):
    return item * item


odd2_list = [handle_item(i) for i in range(21) if i % 2 == 1]
print("odd2_list: ", odd2_list)


# 生成器表达式
odd3_gen = (handle_item(i) for i in range(21) if i %2 == 1)
print("odd3_list: ", odd3_gen, type(odd3_gen))

odd3_list = list(odd3_gen)
print("odd3_list: ", odd3_list)

# 字典推导式
my_dict = {"a": 1, "b": 2, "c": 3}

reverse_my_dict = {value: key for key, value in my_dict.items()}
print("reverse_my_dict: ", reverse_my_dict)


vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for ele in vec for num in ele])


# 集合推导式
my_set = {key for key,value in my_dict.items()}
print(my_set)
