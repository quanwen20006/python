# _*_ coding:utf-8 _*_
'''
字符串操作
    正向搜索 最左第一个字符下标是0，直到len(str)-1
    反向搜索 最右第一个字符下标是-1，直到-len(str)
'''
mstr = "hello world"
print('mstr： ', mstr[-1], mstr[len(mstr)-1])

# 返回值是对应字符串的十进制整数
print('ord: ',ord('好'))

print(mstr[len(mstr)-1])
print(mstr[0:len(mstr):2])

# substring
print('he' in mstr)

# find 找到就返回，出现子字符串的下标，不存在子字符串就返回-1
print(mstr.find('rld'))

# index，找到子字符串的位置，未找到报错
print(mstr.index('ld'))

dollars = format(123000000.7889, ".2e")
print("我叫{}，今年{},我有{}元".format("bill", 20, dollars))

# count的使用
new_string = "hello world ,hello python,hello china"
print("count统计子字符串出现的次数： ", new_string.count("hello"))
print(new_string.replace("hello", "en"))

# 从控制台读取字符串
myname = input('请输入名字： ')
print('myname: ',myname)

#  字符串切片(包头不包尾)
# str[satrt:end:step]
demo = 'abcdefghaijklmanopq'
print(demo[1:5])
print('反向排： ',demo[::-1])
print('统计字符串出现a的次数 ', demo.count('a'))

demo ='a bc c d e'
print('字符串split', demo.split(' '))

# join的使用 字符串连接
# 字符串拼接最好使用join比+号拼接更高效
new_mster = "-".join("abcdddd")
print("new_mster: ", new_mster)

import time
time01 = time.time()
a=''
for i in range(1000000):
    a+=' demo '
time02 = time.time()
print('耗费时间： ',time02-time01)

time03 = time.time()
a=[]
for i in range(1000000):
    a.append(' demo ')
a = ''.join(a)
time04 = time.time()
print('耗费时间： ',time04-time03)

# 字符串潴留机制(只限于在控制台执行)
'''
 仅保存一份相同且不可变的字符串方法，不同的值会放在字符串驻留池
 驻留池只保留 由 下划线、数字、字母组成的字符串
'''
a = 'ab2_'
b = 'ab2_'
c = 'ab2#'
d = 'ab2#'
print('驻留池: ', a is b)
print('驻留池: ', c is d)

# 成员操作符
print('a' in 'dhjsdjks')

#字符串常用方法
demo='''在这种情1况下，美国国务卿2蓬佩奥坐不住了。在他于7日晚间发布推特称，这是“诽谤”，美国才不是“香蕉共和国”在'''
print('字符串长度： ',len(demo),' 开始字符串： ',demo.startswith('在这种'))
print('第一次出现字符串的位置： ', demo.find('在'),' 最后一次出现字符串的位置： ',demo.rfind('在'))
print('所有字符全是字母或数字： ',demo.isalnum())
print('所有字符全是字母（含汉字）： ',demo.isalpha())
print('所有字符全是数字： ',demo.isdigit())
print('所有字符全是大写： ',demo.isupper())
print('所有字符全是小写： ',demo.islower())
demo='\t\n'
print('所有字符全是空格： ',demo.isspace())
demo1 = ' abc AFd e '
print('去除字符串的首尾空格： ',demo1.strip())
print('大小写转换： ',demo1.upper())
demo2 = demo1.capitalize()
print('产生新的字符串首字符大写： ', demo2)
demo3 = demo1.title()
print('产生新的字符串,每个字符串的第一个字符大写： ',demo3 )
demo4 = demo1.swapcase()
print('产生新的字符串,大小写转换： ',demo4)

# 对字符串进行排版(按指定长度排版，不足用-替代)
print('左对齐：',demo1.ljust(20,'*'))
print('右对齐：',demo1.rjust(20,'*'))
print('居中对齐：',demo1.center(20,'*'))

# 字符串格式化
demo = '名字是: {0},年龄是{1}。{0}是个好小伙'
print('格式化后的字符串：',demo.format('Jack',22))
demo = '名字是: {name},年龄是{age}。{name}是个好小伙'
print('格式化后的字符串：',demo.format(name='Jack',age=22))

# 填充和对齐
# ^,<,> 分别是居中、左对齐、右对齐
# 语法说明 :&表示填充的字符(如果不写，表示默认填充空格) > 表示左对齐 8 表示字符的长度
demo = '名字是: {0},年龄是{1:&>8}。{0}是个好小伙'
print('填充+格式化后的字符是：',demo.format('jack',22))

# 数字格式化
demo = '名字是: {0},存款有{1:.2f}'
print('数字格式化：',demo.format('全文',10000000.1234))

# 意义如下，存款进行格式化，左对齐+2位长度
demo = '名字是: {0},存款有{1:#<2d}'
print('数字格式化：',demo.format('全文',1))
# 百分比显示
demo = '名字是: {0},存款有{1:.0%}'
print('数字格式化：',demo.format('全文',10000000))
# 科学计算法显示
demo = '名字是: {0},存款有{1:.2e}'
print('数字格式化：',demo.format('全文',10000000))

# 可变字符串
import io
demo ='Hello world'
demo_new = io.StringIO(demo)
print('可变字符串: ', demo_new.getvalue())
demo_new.seek(len(demo_new.getvalue()))
demo_new.write('quanwen')
print('可变字符串: ', demo_new.getvalue())


