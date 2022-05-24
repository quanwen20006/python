# _*_ coding:utf-8 _*_
# @time  : 2020/7/9 08:56
# @Author: quanwen
# @File  :
import threading
import time

def fun1(name,delay):
    print('线程 {} 开始运行' .format(name) )
    time.sleep(delay)
    print('线程 {} 结束运行' .format(name))

def fun2(name,delay):
    print('线程 %s 开始运行' % name)
    time.sleep(delay)
    print('线程 %s 结束运行' % name)

if __name__ == '__main__':
    print('主线程开始')
    # 创建线程
    thread1 = threading.Thread(target=fun1,args=('fun1',3))
    thread2 = threading.Thread(target=fun1, args=('fun2', 9))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('主进程结束')
