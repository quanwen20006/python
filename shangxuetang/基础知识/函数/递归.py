# _*_ coding:utf-8 _*_
# @time  : 2021/1/15 20:49
# @Author: quanwen
# @File  :

def test01(n):
    print('test01: {0}'.format(n))
    if n == 0:
        print('called finished')
    else:
        test01(n-1)
    print('test01: {0}'.format(n))


# 使用递归计算阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)



if __name__ == '__main__':
    test01(4)
    result = factorial(5)
    print('result: {0}'.format(result))