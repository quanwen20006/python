'''
列表推导式
语法：
      表达式  for item in 可迭代对象
      表达式  for item in 可迭代对象 if 条件判断
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [i**3 for i in a]
print(b)

# 如果i大于5，再进行列表推导式
c = [i**3 for i in a if i > 5]
print(c)


# 如果针对set集合进行列表推导式
d = {1, 2, 3, 4, 5, 6, 7, 8, 9}
e = {i**3 for i in a if i > 5}
print(e)

# 字典进行列表推导式
stu = {'a': 1,
      'b': 2,
      'c': 3
      }

f = (key for key, value in stu.items())
print('f: ',f)
for i in f:
      print('i: ',i)

# 字典推导式
my_text = 'Hello world'
char_count = {c:my_text.count(c) for c in my_text}
print('char_count: ',char_count)

# 生成元组--gnt是生成器对象，只能使用一次
gnt = (x for x in range(4))
print(tuple(gnt))
print(tuple(gnt))