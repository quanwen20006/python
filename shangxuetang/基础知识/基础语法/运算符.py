# _*_ coding:utf-8 _*_
# @time  : 2021/1/7 11:22
# @Author: quanwen
# @File  :

# 逻辑运算符
print('逻辑或： ', True or False)
print('逻辑与： ', True and False)
print('逻辑非： ', not True)

# 同一运算符（比较的是对象的地址）
class Dog:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

dog1 = Dog('小黑')
dog2 = Dog('小黑')
print('dog1: ',id(dog1), ' dog2: ', id(dog2))

a = '123'
b = '123'
c = a
print('同一运算符: ', a is c)
print('同一运算符: ', dog1 is dog2)
print('同一运算符: ', dog1 == dog2)

# 算数符的优先级
# 位运算符和算数运算符 > 比较运算符 > 赋值运算符 > 逻辑运算符
a = 0b11001
b = 0b10000

print("十进制-{}-{}".format(int(a),int(b)))

# bin(int)  二进制显示具体数字  注意：二进制显示如果可高位补零，如0b11和0b011是同一个数
c = a | b # 结果为：每个位进行或操作 （有一个为1时，都为1，否则为0）
print('按位或： ',bin(c))
d = a & b # # 结果为：每个位进行与操作（两个都个为1时，都为1，否则为0）
print('按位与： ',bin(d))
e = a ^ b # 异或 相同为0，不同为1（两个位相同为0，相异为1 (常用统计不相同数））
print('按位异或： ',bin(e))

# 左移（相当于成乘2） 右移（相当于成除2）--比乘法除法快
a = 3
print('左移: ', a<<2)
b = 24
print('右移: ', b>>3)


# 乘法
a = [1,2,3]
print('对列表进行乘法： ',a*2)

print(bin(16))


print(int(0b010000))
print(int(0b10000))

print(0b001)