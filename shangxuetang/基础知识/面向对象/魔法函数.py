# _*_coding:utf-8 _*_

'''
魔法函数的使用
'''


class Person(object):
        # 构造方法
    def __init__(self, name, age,salary):
        print("我被创建了")
        self.__name = name
        self.__age = age
        self.__salary = salary

    # 析构方法
    def __del__(self):
        print("%s对象马上被干掉了..." % self.__name)
    # 自定义对象打印格式

    def __str__(self):
        return self.__name

    # 定义对象的长度
    def __len__(self):
        return 456

    #  对象的比较
    def __gt__(self, other):
        return self.__salary > other.__salary

    # 对象做加法
    def __add__(self, other):
        return self.__salary + other.__salary

    def __call__(self, *args, **kwargs):
        print('计算工资了')
        yearSalary = self.__salary*12
        daySalary = self.__salary//30
        print('月薪是：{0} 日薪是：{1}'.format(yearSalary,daySalary))
        return {'yearSalary':yearSalary,'daySalary':daySalary}

p = Person("jack", 34,10000)
p1 = Person("jones",33, 20000)
print('调用__call__方法',p())
print("len:", len(p))
print("对象的比较结果是：", p > p1)
print("对象的相加结果是：", p + p1)
