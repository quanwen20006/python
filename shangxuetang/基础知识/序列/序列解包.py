# _*_ coding:utf-8 _*_
# @time  : 2021/1/10 11:58
# @Author: quanwen
# @File  :
x,y,z=(10,20,30)
(a,b,c) = (40,50,60)
print(x,y,x)
print(a,b,c)

my_dict = {'name': 'jack', 'age': 22, 'salary': 100000}

name,age,job = my_dict # 默认返回字典的所有键，再进行解包
print('name,age,job1： ',name,age,job)

name,age,job = my_dict.items() # 默认返回字典的所有键，再进行解包
print('name,age,job： ',name,age,job)