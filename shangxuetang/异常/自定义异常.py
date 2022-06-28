# _*_ coding:utf-8 _*_
# @time  : 2021/1/25 15:02
# @Author: quanwen
# @File  :

class AgeError(Exception):
    def __init__(self,errInfo):
        super().__init__(self)
        # Exception.__init__(self)
        self.errInfo = errInfo

    def __str__(self):
        return str(self.errInfo)+',年龄错误,年龄应该在1-120之间'


def throw_error():
    raise Exception("抛出一个异常")
    print("飞天猪")



# 测试代码
if __name__ == '__main__':
    age = int(input('请输入一个年龄：'))
    if age < 1 or age > 150:
        raise AgeError(age)
    else:
        print('正常的年龄：',age)

    # 抛出异常
    throw_error()