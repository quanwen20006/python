# _*_ coding:utf-8 _*_
# @time  : 2021/1/10 10:52
# @Author: quanwen
# @File  :
'''
元组定义
    不可变序列(如果有子序列，是指子序列的地址不能变)
    m_tuple = (para1,para2)
    m_tuple = (para1,)--只有一个元素需要加逗号
    m_tuple = para1,para2


'''
m_tuple = (1, 2, 3, True, "hello")
print(type(m_tuple), m_tuple)
# 另外一种方式定义
m_tuple1 = width, height = 300, 400
print(type(m_tuple1))

company = ("google", "apple", "huawei", "alibaba")
print(company[3])
for i in range(0, len(company)):
    print("company: ", company[i])

# 遍历集合
for i in company:
    print(i)

# 元祖操作
print((1, 2, 3)+(4, 5, 6))
print((1, 2, 3)*2)

# 元组的内容倒序显示
print(company[::-1])

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
# zip 将多个列表压缩并组合成元组，最终返回zip对象
# 压缩后的结果是：zip:  (1, 4, 7)	zip:  (2, 5, 8)	zip:  (3, 6, 9)
d = zip(a,b,c)
for i in d:
    print('zip: ',i,end='\t')

# 生成器
s = (x*2 for x in range(4))
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())

demo = (1,2,3,[11,22,33])
demo[3][1]=1111
print('demo: ',demo)
