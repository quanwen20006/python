# _*_ coding:utf-8 _*_
# @time  : 2021/1/23 21:45
# @Author: quanwen
# @File  :

'''
序列化--把对象转化成"串行化"数据形式，存到到硬盘或者通过网络传输到其他地方
pickle.dump(obj,file) 把obj内容序列化，存到文件中
pickle.load(file) 从file中读取数据，反序列化成对象
'''
import pickle

class Student:
    __num = 0

    def __init__(self,name,age,score):
        self.__name = name
        self.__age = age
        self.__score= score

    def getScore(self):
        return self.__score


if __name__ == '__main__':
    stu1 = Student('jack',17,99)
    with open('stu.dat','wb') as f:
        pickle.dump(stu1,f)

    with open('stu.dat','rb') as f:
        stu = pickle.load(f)
        # for line in f.readlines():
        #     print('line: ',pickle.lline)
        print('stu: ',stu)
