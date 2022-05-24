# _*_ coding:utf-8 _*_
# @time  : 2021/1/22 10:13
# @Author: quanwen
# @File  :

'''
__del__ 方法称为 "析构方法",用于实现对象被销毁时所需调操作。
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print('{0}的年龄是：{1}'.format(self.name,self.age))


    def __del__(self):
        print('销毁对象{0}'.format(self))


if __name__ == '__main__':
    p1 = Person('Jack',33)
    p1.info()
    del p1
    p2 = Person('Jones', 23)
    p2.info()
    print('程序结束')