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
