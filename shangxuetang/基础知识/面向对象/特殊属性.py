# _*_ coding:utf-8 _*_
# @time  : 2021/1/22 15:52
# @Author: quanwen
# @File  :

class A:
    def aa(self):
        print('aa')

class B:
    def bb(self):
        print('bb')


class C(B,A):
    def __init__(self,n):
        self.n = n

    def cc(self):
        print('cc')

if __name__ == '__main__':
    c = C(3)
    print(c.__dir__())
    print(c.__dict__)