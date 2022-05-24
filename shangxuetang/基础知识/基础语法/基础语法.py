# _*_ coding:utf-8 _*_
'''
    主要是记录学习基础过程中的demo
    该文档记录的主要是基础知识
'''

# 逻辑运算符
print('逻辑运算符: ',True or 10)
print('逻辑运算符: ',False or 10)
print('逻辑运算符: ',False and 10)
print('逻辑运算符: ',True and 10)

# 链式赋值
a,b,c = 1,2,3

print(str(a) + ' '  + str(b) + ' ' +str(c))

# 变量互换
a,c = c,a
print(str(a) + ' '  + str(b) + ' ' +str(c))

print('浮点数除法/： ',8/2)
print('整数除法//： ',8//2)
print('模(取余)%： ',9%2)
print('同时取商和余数： ',divmod(10,2))

(x,y)= divmod(10,2)
print(x)
print(y)


# int类型转换
'''
浮点数去掉小数点后面的值
True为1 False为0
整数和浮点数进行计算，结果为浮点数
'''
print(int(False))
print(8*2.0)

# round 四舍五入,不改变源对象的值，产生新对象
print('四舍五入 ',round(3.84))


int = 1
# 查看数据的类型，使用type可查看到
print(type(int), int, '\n数据相加\t', type(1+1.1),
      '\n数据相乘\t', type(1*1.1), '\n数据相除\t', type(1/1))

# 整形数相除，但是想得到整形
print('整形相除、但是想得到整形：', type(1//1))


print('转换为16进制', hex(13))
print('转换为8进制', oct(13))
print('转换为2进制', bin(13))

print('let\'s go')

print('hello \\n world')

print('hello \\n world'[-3])


# 列表
tempList = ['ShangHai', 'BeiJing', 'TianJing', 'ShenZen']
print(tempList[2])
tempList.append('ChongQing')
print(tempList)

tempTuple = ('ShangHai', 'BeiJing', 'TianJing', 'ShenZen')
print(tempTuple[3])
print(tempTuple[1:3])

tempTuple1 = (1,)
print(type(tempTuple1))

# 获得字符串的十进制值
print(ord('a'))


# set集合
tempSet1 = set()
tempSet = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('空集合： ', type(tempSet1), '有内容集合： ', tempSet)
# print('获得set的值：',tempSet[1])

# 字典
tempDict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
tempDict1 = {}
print('有内容字典： ', tempDict, '空字典： ', type(tempDict1))
print('获取字典的值：', tempDict['Alice'])


print(35 <= 45 < 75)  # 等价于 45 》=35 and 45 《75
print(35 <= 25 < 75)


# 按位与-把值转换为2进制，然后每一位进行与值，如果都为1，就把结果设置为1，否则为0，
print(3 & 10)
print(3 | 10)

account = 'qiyue'
pwd = '123456'

user_account = input('please input account: ')
user_pwd = input('please input pwd: ')
# 流程控制
if user_account == account and user_pwd == pwd:
    print('succuess')
else:
    print('fail')

# for 循环--else 执行完列表后，再执行
fruitList = ['apple', 'pear', 'bananan']
for fruit in fruitList:
    print('fruit is :', fruit, end='\t')
else:
    print('打印完毕')

# while 循环--else 条件为False，再执行
count = 0
while count <= 10:
    count += 1
    print(count)
else:
    print('count is: ', count)

# for -- range -range不包含右边界
for i in range(1, 10):
    print('i is: ', i)
