# _*_ coding:utf-8 _*_
# @time  : 2021/1/22 16:55
# @Author: quanwen
# @File  :

class MySingleton:
    _obj = None
    _initFlag = True

    def __new__(cls, *args, **kwargs):
        if cls._obj == None:
            cls._obj = object.__new__(cls)
        return cls._obj

    def __init__(self,name):
        if MySingleton._initFlag:
            print('init----')
            self.name = name
            MySingleton._initFlag = False

a = MySingleton('aa')
b = MySingleton('bb')

print(a)
print(b)