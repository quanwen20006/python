'''
python 魔法函数--指的是双下划线开头、双下划线结尾的函数
'''


class Company(object):
    def __init__(self, employ_list):
        self.employee = employ_list

    def __getitem__(self, item):
        # 循环对象的时候会执行该方法，执行到抛异常截至
        # print("开始执行__getitem__")
        return self.employee[item]

    def __len__(self):
        # 执行类实例对象的len方法会执行该方法，如未定义即报错
        return len(self.employee)

    def __str__(self):
        return ".".join(self.employee)

    def __repr__(self):
        return "__repr__"


employee = Company(["Jack", "Jones", "Lily"])
# 下面这一行其实调用的就是__str__
print("employee---", employee)
# employee 和employee.__repr__() 意义是一样的
employee
employee.__repr__()


# 执行该方法需要company实现__len__方法
print( ("employee的类型是%s 长度是%d")  % (type(employee), len(employee)))

for em in employee:
    print(em)


#  __add__ 数学运算使用
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_instance):
        vec = Vector(self.x + other_instance.x, self.y + other_instance.y)
        return vec

    def __str__(self):
        return 'x is %s y is %s' % (self.x, self.y)


vector1 = Vector(1, 2)
vector2 = Vector(11, 12)
print(vector1+vector2)


class Num(object):

    def __init__(self, x):
        self.x = x

    def __abs__(self):
        return abs(self.x)


num1 = Num(-99)
print(abs(num1))
