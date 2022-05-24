# _*_ coding:utf-8 _*_
# @time  : 2020/7/8 08:54
# @Author: quanwen
# @File  :
'''
    多进程间的数据互相独立，不共享
'''
from multiprocessing import Process

num = 10
def work1():
    global num #修改全局变量需要在修改的地方前，添加global
    num += 5
    print('work1\'s num: ',num)

def work2():
    global num  # 修改全局变量需要在修改的地方前，添加global
    num += 15
    print('work2\'s num: ', num)

if __name__ == '__main__' :
    print('开始主进程')
    # 创建子进程
    p1 = Process(target=work1)
    p2 = Process(target=work2)
    # 启动子进程
    p1.start()
    p2.start()
    #主进程等待子进程结束
    p1.join()
    p2.join()

    print('主进程全局变量num %d' %num)