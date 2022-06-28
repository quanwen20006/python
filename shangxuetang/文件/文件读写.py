# _*_ coding:utf-8 _*_
# @time  : 2021/1/22 22:02
# @Author: quanwen
# @File  :
'''
with open(r'./Hotel California.txt',encoding='utf-8',mode='r') as  f:
    str = f.read()  #读取所有的内容
    str = f.read(3) #读取前三个字符（英文和中文都是一个字符）
    # 按行读取
    while True：
        flag = f.readline()
        if not flag:
            break
        else:
            print(flag,end='')

    # 使用迭代器读取(每次返回一行)
    for a in f:
        print(a,end='')

'''
result = []
with open(r'./Hotel California.txt', encoding='utf-8', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
    # print('lines: ',lines)
    # 把文件的内容末尾加上 #行号，然后写入新的文件
    result = [temp.strip('\n') + ' #' + str(index) + '\n' for index,temp in enumerate(lines)]


print('result: ', result)
with open(r'./Hotel California1.txt', encoding='utf-8', mode='w') as f:
    f.writelines(result)


print("------------")
for eachline in open("./Hotel California.txt"):
    print(eachline)