# _*_coding:utf-8 _*_
'''
元组： 有序，可重复，不可编辑
'''
import copy

'''
列表 有序，可重复，可编辑,任何数据
list：[1,2,3]
'''
mlist = [1, 2, 3, 4, 5, 1, "test"]
print(mlist,' 原始内存地址是：',id(mlist))

print("mlist: ", mlist)
# 列表推到式
mlist1 = [c for c in "hello world" if c != "o"]
print(mlist1)

'''
列表 增删改--append 增加在末尾一次增加一个  extend 扩战一个迭代（都是在原有列表）
pop 删除列表对最后一个元素，并且返回最后一个元素 list.pop()
del 删除指定列表指定元素 del list[0]
remove 删除列表首次出现对数据 list.remove('demo') 删除列表list里面对第一个demo字符串，不存在就抛异常
index 获得指定元素在列表中首次出现的索引  list.index('demo')
count 获得指定元素在列表中总次数  list.count('demo')


成员资格判断
in 'demo' in list  如果存在就返回True，不存在就返回False
'''

mlist.append("new")
mlist.extend([11,22])
mlist.insert(0,'insert')
print(mlist,' append后对内存地址是：',id(mlist))

mlist=mlist+[100]
print(mlist,' 加操作后对内存地址是：',id(mlist))

mlist[0] = "test"
mlist.remove(3)
print(mlist)
