# _*_ coding:utf-8 _*_
# @time  : 2021/1/11 11:29
# @Author: quanwen
# @File  :

'''
集合：无序，不重复
'''

mset = set()
mset = {1, 2, 3, "te"}
mset.add("myset")
mset.add(1)
print(mset)
mset1 = {i for i in "hello"}
print("mset1: ", mset1)
mset2 = {i for i in range(1, 10) if i % 2 == 0}
print("mset2: ", mset2)

# 集合的操作符
test_set1 = {2, 3, 6}
print('test_set1-----',type(test_set1))
test_set2 = {1, 2, 3, 5}
# 交集 intersection
print('交集： ',test_set1 & test_set2)
# 并集 union
print('并集： ',test_set1 | test_set2)
# 异或（求两个集合的差集）
print('异或： ',test_set1 ^ test_set2)
# 差集
print('差集： ',test_set2 - test_set1)

