# _*_ coding:utf-8 _*_
# @time  : 2020/7/9 08:47
# @Author: quanwen
# @File  :

import _thread
import time

def fun1(name,delay):
    print('开始运行 %s' % name)
    time.sleep(delay)
    print('运行fun1结束')

def fun2(name,delay):
    print('开始运行 %s' % name)
    time.sleep(delay)
    print('运行fun2结束')

if __name__ == '__main__':
    print('开始运行')
    # 创建线程,并传参
    _thread.start_new_thread(fun1,('thread1',3))
    _thread.start_new_thread(fun2,('thread2',1))
    time.sleep(6)