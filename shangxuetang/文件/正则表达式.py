# -*-coding:utf-8 -*-
'''
学习正则表达式
'''

import re
temp = '1here are moments in life when you miss someone so much 2that you just want to pick them from your dreams and hug them for real!3 '
# 概括字符串
# \d \D
# \w 单次字符 \W
# \s 空白字符 \S
result = re.findall('someone', temp)
resultNum = re.findall('\d', temp)

print(result, ' 数字共有%d个 内容为%s' % (len(resultNum), resultNum))

temp1 = 'abc, acd, acf, acc, adc, afc'
# 匹配中间是c或者f的，且a开头，c结尾的
temp1Result = re.findall('a[cf]c', temp1)
print(temp1Result)
# 匹配中间是c到f任意一个，且a开头，c结尾的
temp2Result = re.findall('a[c-f]c', temp1)
print(temp2Result)
# 排除中间是c到f任意一个，且a开头，c结尾的
temp3Result = re.findall('a[^c-f]c', temp1)
print(temp3Result)

# 匹配任何不可见字符
a = 'asdasdkajshkas\tdsa\ns'
temp4Result = re.findall('\s', a)
print('temp4Result', temp4Result)

b = 'python as123123php48java'
# 或者python java和php 即找字母，最少3位（php），最大6位（python）
temp5Result = re.findall('[a-z]{3,6}', b)
print('temp5Result ', temp5Result)

c = 'pytho0python1pythonn2'
# * 匹配0次或者无限多次
# + 匹配1次或者无限多次
temp6Result = re.findall('python*', c)
print('temp6Result: ', temp6Result)

# 在界限后面加问号会切换到非贪婪模式
# 贪婪模式--指找到后，会继续寻找
# 非贪婪模式--会去界限的最小值
b = 'python as123123php48java'
temp7Result = re.findall('[a-z]{3,6}?', b)
print('temp7Result ', temp7Result)

qq = '84381513'
# 边界匹配- ^匹配输入字行首 $匹配输入字行尾
# 规则为验证号码长度是否为4-8位,即数字开头，数字结尾，长度为4-8位
temp8Result = re.findall('^\d{4,8}$', qq)
print('temp8Result ', temp8Result)


# 组
# 查询py字符串里面Python2组且JS2组的字符串集合
py = 'pythonpythonJSJSpythonpythonJSythonpythonJSJSJS'
temp9Result = re.findall('(python){2}(JS){2}', py)
print('temp9Result: ', temp9Result)


# 匹配模式参数
# re.I(不区分大小写) re.S(可以匹配\n,改变点号的行为)
lanuage = 'pythonC#\nJavaC#|PhP'
temp10Result = re.findall('c#.{1}', lanuage, re.I | re.S)
print('temp10Result ', temp10Result)


# 正则表达式 sub方法的使用,默认第四个参数为0--即无限替换，如果为1就表示找到第一个且替换，后面的不替换
def convert(value):
    matched = value.group()
    # print('matched-------', matched)
    if int(matched) >= 6:
        return '9'
    else:
        return '0'


# lanuage = 'pythonC#\nJavaC#|PhP'
# temp11Result = re.sub('C#', convert, lanuage, 1)
# print('temp11Result ', temp11Result)


s = "3218C3721D86"
# 把数字替换，大于6的数字替换为9，小于6的替换为0
# 把函数名当做其他函数的参数
temp12Result = re.sub('\d', convert, s)
print('temp12Result', temp12Result)


# serach 搜索到符合规则的第一个值
# match 从被搜索的字符串开始位置进行检测
print('search ', re.search('\d', s).group())
print('match ', re.match('\d', s))
print('match-span ', re.match('\d', s).span())
print('match-group ', re.match('\d', s).group())

# group的使用-查找life 和 python中间的字符,
# group(0)反馈正则匹配的所有内容，group(1)返回匹配后的内容
s1 = 'life is short i use python'
temp13Result = re.search('life(.*)python', s1)
temp14Result = re.findall('life(.*)python', s1)#使用括号圈起来的不在包括范围内
# 以life开头，Python结尾的字符串
print('111111111', re.findall('^life(.*)python$', s1))
print('temp13Result ', temp13Result.group(1))
print('temp14Result ', temp14Result)

s2 = 'life8438151311python'
print('查找字符串中间的数字：', re.findall('^life(\d{0,})python$', s2))


# 多个group
s3 = 'life is short # i use python # i love python'
temp16Result = re.search('life(.*)python(.*)python', s3)
print('temp16Result ', temp16Result)
print('多个group：', temp16Result.group(0, 1, 2))
print('groups：', temp16Result.groups())


sIP = 'static serverAddress: string = "17w2.17.0.26"'
sDN = 'static serverAddress: string = "z.c1n"'

temp111Result = re.findall('((\d+\.)(\d+\.)(\d+\.)(\d+))|([a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]{3})', sIP)
temp222Result = re.findall('(([a-z]+)(\.[a-z]+)+)', sDN)

if temp111Result and temp222Result:
    print('IP %s------ 域名-%s-- ' % (temp111Result[0][0], temp222Result[0][0]))
else:
    print("匹配失败")

