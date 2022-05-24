# _*_ coding:utf-8 _*_
# @time  : 2021/1/22 16:44
# @Author: quanwen
# @File  :

class CarFactory:
    def createCar(self,brand):
        if brand=='奔驰':
            return Benz()
        elif brand=='宝马':
            return BMW()
        elif brand=='奥迪':
            return Audi()
        else:
            return '未知品牌，无法创建'

class Benz:
    def __init__(self):
        print('奔驰创建成功')

class BMW:
    def __init__(self):
        print('宝马创建成功')

class Audi:
    def __init__(self):
        print('奥迪创建成功')

if __name__ == '__main__':
    car=CarFactory().createCar('奔驰')