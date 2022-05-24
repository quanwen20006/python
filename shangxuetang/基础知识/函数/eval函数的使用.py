# _*_ coding:utf-8 _*_
# @time  : 2021/1/13 18:14
# @Author: quanwen
# @File  :

s = 'print("abcde")'
eval(s)

a = 10
b = 20
print(eval('a+b'))

dict1 = dict(a=100,b=200)
d = eval('a+b',dict1)
print('d: ',d)