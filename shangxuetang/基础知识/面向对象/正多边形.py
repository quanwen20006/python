# _*_ coding:utf-8 _*_

'''
正多边形
	私有属性：
		多边形的边数
		多边形的长度
		多边形的x，y轴坐标
	访问器+修改器
	公有方法：
		getPerimeter() 返回多边形的周长
		getArea() 返回多边形的面积
'''

import math


class RegularPolygon(object):
    PI = 3.14

    def __init__(self, side, length, x, y):
        self.__side = side
        self.__length = length
        self.__x = x
        self.__y = y
    # 计算多边形的周长

    def getPerimeter(self):
        return self.__side * self.__length
    # 计算多边形的面积

    def getArea(self):
        return (self.__side*(self.__length**2))/(4*math.tan(RegularPolygon.PI/self.__side))

    # 获取多边形的边数
    def getSide(self):
        return self.__side


r = RegularPolygon(6, 3, 10, 10)
print("正%d边形的周长是：%d" % (r.getSide(), r.getPerimeter()))
print("正%d边形的面积是：%.2f" % (r.getSide(), r.getArea()))
