# _*_coding:utf-8 _*_
'''
异常：使用练习
'''
import math

'''
接收3条边，计算三角形的面积
'''


class InvalidArgumentError(Exception):
    def __init__(self, msg):
        self.name = msg


def getTriangleArea(x, y, z):
    if not (x+y > z and x+z > y and y+z > x):
        raise InvalidArgumentError("边长不符合")
    p = (x+y+z)/2
    area = math.sqrt(p*(p-x)*(p-y)*(p-z))
    return area


while(1):
    try:
        a, b, c = eval(input("请输入三角形的三条边："))
        result = getTriangleArea(a, b, c)
        print("面积是： ", result)
        break
    except InvalidArgumentError as e:
        print(e)
