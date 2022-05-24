#-*- coding:utf-8 -*-

'''
Collatz序列,根据用户输入的值，查找得到1

它有一个名为 number 的参数。如果参数是偶数，
那么 collatz()就打印出 number // 2，并返回该值。如果 number 是奇数，collatz()就打
印并返回 3 * number + 1
'''
def collatz(number):
    result = 0
    if number % 2 == 0:
        result = int(number/2)
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result


if __name__ == '__main__':
    while True:
        try:
            temp = int(input('请输入： '))
            if temp == 1:
                collatz(temp)
                break
            else:
                collatz(temp)
        except ValueError:
            print('请输入数字')
