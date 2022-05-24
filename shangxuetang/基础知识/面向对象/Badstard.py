# _*_coding:utf-8 _*_

'''
继续Person类实现一个坏蛋类，用来存储坏蛋信息
坏蛋拥有一切正常属性和功能
坏蛋有【恶习】属性和【作恶】方法
创建一个坏蛋，为其设置基本信息和恶习
'''
# from day3.People import People


class People(object):
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def learn(self):
        print('People learn...')


class Badstard(People):
    def __init__(self, name, age, nickname):
        super().__init__(name, age)
        self.nickname = nickname

    def info(self):
        print(self.name, self.age, self.nickname)

    def learn(self):
        print("Badstard learn")


p = Badstard("jack", 22, "jocky")
p.info()
p.learn()
