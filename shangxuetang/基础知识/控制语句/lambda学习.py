'''
    主要是熟悉python的匿名函数，即高阶函数的使用，在Python中，lambda的语法是唯一的。其形式如下：
    lambda <argument_list>: <expression>

    其中，lambda是Python预留的关键字，argument_list和expression由用户自定义。具体介绍如下。

    1. 这里的argument_list是参数列表，它的结构与Python中函数(function)的参数列表是一样的。具体来说，argument_list可以有非常多的形式
    2. 这里的expression是一个关于参数的表达式。表达式中出现的参数需要在argument_list中有定义，并且表达式只能是单行的。以下都是合法的表达式
    3. 这里的lambda argument_list: expression表示的是一个函数。这个函数叫做lambda函数

'''
from functools import reduce

a = [1, 2, 3, 4, 5]


def tempxT(a): return a**2


print('tempxT: ', tempxT(11))

# 三元表达式
x = 1
y = 2
print("大于" if x > y else "小于")

# map,对sequence中的item依次执行function(item)，将执行结果function(item)组成一个List返回
tempX = [1, 2, 3, 4, 5]
print('map: ', list(map(lambda d: d**2, tempX)))

# reduce的使用.函数的参数必须多传一个
# 对sequence中的item顺序迭代调用function
tempY = reduce(lambda d, y: d*2, tempX, 10)
print('reduce: ', tempY)


# filter
tempA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tempZ = filter(lambda x: x % 2 == 1, tempA)
print("filter: ", list(tempZ))
