# _*_ coding:utf-8 _*_

'''
定义规则
def demo1(a,b,*t,**kwargs):
    print('定义函数: ',a,b,t,kwargs)

demo1(11,22,123,222,111,x=11,y=22)

参数顺序
普通参数，可变参数，默认值参数，键值对参数

返回值
    return 语句结束函数执行，并返回值，如果不包括return则返回None值
'''


import random


def sayLove(arg1, *args, auther="qw", **kwargs):
    print(arg1, args, kwargs, auther)


sayLove(1, 2, 3, 4, 5, 5, 5, city="珠海", date="2月21")


def raiseSalary(salary):
    salary *= 2
    return salary


salary = 2000
result = raiseSalary(salary)
print("result: ", result, salary)

# 返回集合
def test03(x,y,z):
    return [x*10,y*20,z*30]

demo = test03(1,4,3)
print('demo的值是： ', demo)


def getRandomNumber(val):
    temp = random.randint(1, val)
    return temp


print("随机生成的数字n为：", getRandomNumber(10))


# 随机大写字母

def getRandomUpper(flag, start, end):
    '''生成随机数'''
    if flag:
        temp = random.randint(ord(start.upper()), ord(end.upper()))
    else:
        temp = random.randint(ord((start.lower())), ord(end.lower()))
    return chr(temp)


print("随机生成的字符为：", getRandomUpper(False, 'A', 'H'))
print(getRandomUpper.__doc__)

#定义函数
def demo1(a,b,c=99,*t,**kwargs):
    print('定义函数: ',a,b,c,t,kwargs)

demo1(11,22,123,222,111,x=11,y=22)
