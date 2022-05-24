# _*_ coding:utf-8 _*_
import random


def tempxT(a):
    return a**2


# tempX = 11
def x(d): return d**2


def x1(x): return x+3


def sum(x):
    return x+2


print(x(3))


# print(lambda 112: x*2)


print(random.randint(1, 3))

tempX = [1, 2, 3, 4, 5]
a = map(sum, tempX)
print(a)


def temperature():
    temp = int(input("请输入待转换温度:"))
    # print(type(temp))

    result = (9/5)*temp + 32

    print("华氏温度: ", result)
    return result


temperature()

'''
输入一个0-999的数字，求输入数字的，每个位数相加，和为27的数字
'''


def sum():
    while(True):
        temp = int(input("请输入0-999的任意正整数: "))
        if temp < 10:
            print("不满足条件，请重新输入")
            # break
        elif (temp >= 10) and (temp <= 99):
            print("不满足条件，请重新输入", temp % 10)
            # break
        else:
            # //   两个数相除后取整
            x = temp // 100
            # %    两个数相除的余数
            y = temp % 100 // 10
            z = temp % 10
            result = x+y+z
            print('result: ', result, type(result))
            if result == 27:
                print("恭喜，输入的数据位数和符合要求")
                break


sum()

'''
猜数字游戏
又系统随机生成一个1000内的随机数
每次输入一个数来猜答案，输入反馈，是猜大来，还是猜小来
猜正确，游戏结束
-1为终止密码，输入的数据不在范围内给提示
'''
result = random.randint(1, 1000)
print("result: ", result)
while(True):
    guess = int(input("请输入1-1000的数字："))
    if guess == -1:
        break
    elif guess < 1 or guess > 1000:
        print("输出数据不在1-1000范围内请重新输入")
    else:
        if guess > result:
            print("猜大了，再来")
        elif guess < result:
            print("猜小了，再来")
        else:
            print("猜中了")
            break
