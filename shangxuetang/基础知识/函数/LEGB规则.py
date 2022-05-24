# _*_ coding:utf-8 _*_
# @time  : 2021/1/18 17:32
# @Author: quanwen
# @File  :
'''
LEGB是指python搜索变量的顺序

Local      局部变量
Enclosed   嵌套函数的变量
Global     全局变量
Built in   python内置变量

'''

# 测试LEGB
str = "global"

def outer():
    str = "outer"
    def inner():
        str = "inner"
        print(str)
    inner()


if __name__ == '__main__':
    outer()
