# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self, list):
        self.person = list

    def __str__(self):
        return '执行__str__函数'

    def __repr__(self):
        return "1"

    def __getitem__(self, item):
        return '执行该函数__getitem__'
        return self.person[item]

    def __len__(self):
        print('调用__len__方法')
        return len(self.person)+100


per = Person(['a', 'b', 'c', 'd', 'e', 'f'])
print(per)
print(len(per))
temp = per.person[:4]
for item1 in temp:
    print(item1)
