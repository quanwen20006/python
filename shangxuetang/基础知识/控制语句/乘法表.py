# _*_ coding:utf-8_*__
'''
	打印99乘法表
'''
def print_chengfa():
    for i in range(1, 10):
        for x in range(1, i+1):
            print("% d*%d=%d" % (x, i, x*i), end="")
        print()

# 打印正方形
def print_zhengfang():
    for i in range(5):
        for y in range(5):
            print(i,end='\t')
        print()

# 用列表和字典存储表格的数据
def print_showtable():
    r1 = dict(name="高小一",age=18,salary=30000,city="北京")
    r2 = dict(name="高小二",age=19,salary=40000,city="上海")
    r3 = dict(name="高小三",age=20,salary=50000,city="深圳")
    r4 = dict(name="高小四",age=21,salary=100000,city="长沙")
    tb=[r1,r2,r3,r4]
    print('姓名\t', '年龄\t', '薪资\t', '城市')
    for i in tb:
        if i.get('salary')>20000:
            for k,v in i.items():
                print(v,end='\t')
        print()

if __name__ == '__main__':
    print_chengfa()
    print_zhengfang()
    print_showtable()

    # 使用zip循环多个集合
    names = ['test1','test2','test3','test4']
    ages =[11,12,114,18]
    jobs =['老师','程序员','律师']
    temp = zip(names,ages,jobs)
    print('zip多个集合： ',temp)
    for i in temp:
        print('i-----', i)
    for name,age,job in zip(names,ages,jobs):
        print('{0}--{1}---{2}'.format(name,age,job))