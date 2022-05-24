# -*-coding:utf-8 -*-
'''
    类 = 特征 + 行为
    包含静态方法，类方法
    类方法、静态方法不需要创建实例就可以调用
    类方法，静态方法不能访问实例方法，实例方法可以访问静态方法+类方法
'''


class Student(object):
    #name = ''
    #age = 0
    __count = 0

    # 对象初始化函数
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        #Student.count += 1
        # 实例方法访问类变量
        #self.__class__.count += 1
        print('age: ', self.__age, ' name: ', self.__name)

    def print_profile(self):
        print('name: %s age: %s' % (self.__name, str(self.__age)))
        print("普通方法调用静态方法：", Student.add(11, 22))

    def info(self):
        if self.__name == "Jack":
            print("信息是：", self.__name, self.__age)
        else:
            print("no info")
    # 类方法-类方法访问类变量
    @classmethod
    def countSum(cls):
        cls.__count += 1
        # print(cls.count)

    @staticmethod
    def add(x, y):
        print("静态方法访问类的属性：", Student.__count)
        return x+y

    @classmethod
    def getCount(cls):
        # 只能访问类变量
        return cls.__count


stu = Student('Jack', 20)
print("查看类的所有属性：",dir(stu))
stu.countSum() # 等价于  Student.countSum(stu)
stu.info()

print("实例访问静态方法：", stu.add(99, 100))
stu.print_profile()
# print(stu.count)
stu1 = Student('JackJones', 22)
stu1.countSum()
stu1.info()
print('类的类方法：', Student.getCount())
print('类的类方法-实例调用：', stu1.getCount())

print(Student.add(1, 2))
print("类的静态方法：", Student.add(11, 22))
