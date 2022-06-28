'''
    熟悉闭包
    定义：
    函数+环境变量，环境变量在函数的外部,且不能在内部在定义环境变量
'''

def cure_pre():
    a = 25
    print("函数开始执行----")
    def cure(x):
        print("函数执行时间----")
        a = 10
        print('cure...', a)
        return a*x*x
    print('cure_pre...', a)
    print("函数结束执行----")
    return cure


a = 10
f = cure_pre()
print(f(2))
