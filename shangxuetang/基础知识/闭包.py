# _*_coding:utf-8 _*_
'''
学习闭包的使用
'''


def print_msg():
    msg = "i'm clouser"

    # printer是嵌套函数
    def printer():
        print(msg)

    return printer


# 获得一个闭包
closure = print_msg()
closure()


def counter(func):
    """统计函数的被调用次数"""
    count = 0
    def closure(*args, **kwargs):
        nonlocal count  # 内嵌作用域需要使用nonlocal关键字
        count += 1
        print("{}被调用了{}次了".format(func.__name__, count))
        return func(*args, **kwargs)
    return closure

def add(x,y):
    # print("sum:{}".format(x + y))
    return x+y

counter_add = counter(add)
counter_add(111, 222)
counter_add(11, 22)