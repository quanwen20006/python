# _*_ coding:utf-8 _*_
# @time  : 2021/1/15 21:51
# @Author: quanwen
# @File  :

def outer():
    print('f1 running...')

    def inner():
        print('f2 running...')
    inner()


# 实际使用
def printChinesName(name,familyName):
    print("{0} {1}".format(familyName,name))

def printEnglishName(name,familyName):
    print("{0} {1}".format(name, familyName))

# 改造成嵌套函数
def printName(name,familyName,isChinese=False):
    flag = 10
    def inner_print(a,b):
        nonlocal flag # 申明为外部函数的局部变量，这样可以在内部函数使用外部函数的变量
        print("{0} {1} {2}".format(a, b, flag))
        flag = 20
        print("{0} {1} {2}".format(a, b, flag))

    if isChinese:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)


if __name__ == '__main__':
    outer()
    printName('jack','jones',isChinese=False)