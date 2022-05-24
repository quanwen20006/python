# _*_ coding:utf-8 _*_
# @time  : 2021/1/22 16:20
# @Author: quanwen
# @File  :
'''
组合替代多继承
'''
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
    mb = MobilePhone(CPU(),Screen())
    mb.cpu.calculate()
    mb.screen.show()