from shangxuetang.基础知识.面向对象.People import People


class Student(People):

    def __init__(self, name, age, score):
        #People.__init__(self, name, age)
        #调用父类的构造方法
        super(Student, self).__init__(name, age)
        self.__score = score

    def do_homework(self):
        print('Student do homework')

    def learn(self):
        print('Student Learn....')

    def printStu(self):
        print('student name is %s score is %d' % (self.name, self._Student__score))


if __name__ == '__main__':
    stu = Student('Jack', 30, 90)
    stu.printStu()
    stu.do_homework()
