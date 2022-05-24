# _*_ coding:utf-8 _*_
# @time  : 2021/1/22 16:08
# @Author: quanwen
# @File  :

import copy

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculate(self):
        print('计算----')


class Screen:
    def show(self):
        print('屏幕显示', self)


if __name__ == '__main__':
    c1 = CPU()
    s1 = Screen()
    c2 = c1
    print(c1)
    print(c2)

    # 浅拷贝--浅拷贝时，拷贝出来的新对象的地址和原对象是不一样的，但是新对象里面的可变元素（如列表）的地址和原对象里的可变元素的地址是相同的
    m1 = MobilePhone(c1,s1)
    m2 = copy.copy(m1)

    print(m1,m1.screen,m1.cpu)
    print(m2,m2.screen,m2.cpu)


    # 深拷贝---子孙也拷贝
    m3 = MobilePhone(c1, s1)
    m4 = copy.deepcopy(m3)

    print(m3, m3.screen, m3.cpu)
    print(m4, m4.screen, m4.cpu)
