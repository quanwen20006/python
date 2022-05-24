# _*_ coding:utf-8 _*_

'''
属性装饰器
    1：把一个函数装饰成属性，可以对该方法进行getter和setter
    2：调用的时候当调用一个对象当属性
'''


class Person(object):
    def __init__(self, name, rmb):
        self.__name = name
        self.__rmb = rmb
        self.__password = "123456"

    # 下面的代码将rmb()方法转化成同名只读属性的getter方法。
    @property
    def rmb(self):
        # return self.__rmb
        inp = input("getter-请输入密码：")
        if inp == self.__password:
            return self.__rmb
        else:
            print("密码错误")


    @rmb.setter
    def rmb(self, rmb):
        inp = input("setter-请输入正确的密码才能设置RMB：")
        if inp == self.__password:
            self.__rmb = rmb
            print('已被修改为： ',self.__rmb)
        else:
            print("密码错误")


p = Person("jack", 10000)
# print("获得玩家的RMB是： ", p.getRmb())
# p.setRmb(12000)
# print("获得玩家的RMB是： ", p.getRmb())

print("getter: ", p.rmb)
p.rmb = 30000
print("getter: ", p.rmb)
