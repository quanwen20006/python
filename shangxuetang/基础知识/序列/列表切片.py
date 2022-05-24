# _*_ coding:utf-8 _*_
# @time  : 2021/1/10 09:43
# @Author: quanwen
# @File  :
# 列表切片
'''
排序 list.sort(reverse=True) --不生成新的序列
    sorted(list)--生成新的序列

max 返回列表里面最大的值
min 返回列表里面最小的值
sum 对列表的所有元素进行求和（非数字求和会报错）

浅拷贝：如果拷贝的值有对象（容器，对象），拷贝的是对象地址，即源对象修改，新的对象也修改
深拷贝：如果拷贝的值有对象（容器，对象），拷贝的进行更新，对源对象没影响，源对象修改对拷贝对对象也无影响
'''
import copy
import random
mlist = [91, 2, 33, 4, 5, 6,7]
mlist = reversed(mlist)
for i in mlist:
    print('使用reversed倒序排列表（生成的是迭代器）： ',i,end='#')
mlist = [91, 2, 33, 4, 5, 6,7]
print('列表切片-step为2：',mlist[1::2])
print('列表切片-倒序：',mlist[::-1])
mlist.sort()
print('列表排序(升序)： ',mlist)
mlist.sort(reverse=True)
print('sort(reverse=True)列表排序(降序)： ',mlist)
# 打乱列表的排序
random.shuffle(mlist)
print('random.shuffle列表排序(乱序)： ',mlist)

print(mlist[1:3])
mlist3 = [1, 2, 3, 4, 5, 1, ["test", "test2"]]
mlist2 = mlist3.copy()
mlist3[-1].append("test3")
mlist2[-1].append("test4")
print("mlist3: ", mlist3, " mlist2: ", mlist2)

mlist4 = copy.deepcopy(mlist3)  # 绝对拷贝
mlist3[-1].append("deepcopy")
mlist4[-1].append("deepcopy-1")
print("mlist3: ", mlist3, " mlist4: ", mlist4)
