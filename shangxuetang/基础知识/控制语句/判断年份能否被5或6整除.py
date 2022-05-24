# _*_ coding:utf-8 _*_
'''
判断输入对年份能否被5或6整除
'''


import random


def answer():
    while(1):
        temp = int(input("请输入一个年份: "))
        if (temp % 5 == 0 or temp % 6 == 0):
            print("ok")
            break
        else:
            print("no")


answer()

'''
随机生成一个大写字符
'''


def randomCapital():
    start, end = ord('A'), ord('Z')

    temp = random.randint(start, end)
    return chr(temp)


test = randomCapital()
print("字符是： ", test)


'''
不断输入整数，直到输入0为止，最后统计正负数的个数，总数，平均值
'''


def sum_math():
    tempList = []
    x = 0
    y = 0
    while(1):
        temp = int(input("请输入整数"))
        if temp > 0:
            x = x + 1
        elif temp < 0:
            y = y + 1
        else:
            print("输入的是0")
            break
        tempList.append(temp)
    print("tempList: ", tempList, " x: ", x, " y:", y)


sum_math()


'''
判断一个输入三位数，确定是否为回文数，
回文数的规则，就是数的第一位和第三位是否相等
'''


def isHuiWen():
    while(1):
        temp = int(input("请输入一个三位整数："))
        if temp < 100:
            if (temp > -1000 and temp < -99):
                print("输入的数不符合要求：")
        elif temp > 999:
            print("输入的数不符合要求：")
        else:
            x = temp // 100
            y = temp % 10
            print("百位数是： %d，个位数是：%d " % (x, y))
            if x == y:
                print("%d is 回文数" % (temp))
                break


isHuiWen()


'''
求是否为闰年
'''


def leapYear():
    count = 0
    for year in range(2000, 2101):
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("%d 是闰年" % year)
            count += 1


leapYear()
