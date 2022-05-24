# _*_ coding:utf-8 _*_
# @time  : 2020/7/9 13:03
# @Author: quanwen
# @File  :

from threading import *
num = 0

# 创建互斥锁
lock = Lock()
'''
    线程对全局变量进行操作，会造成数据紊乱
    
    解决办法：给线程加锁
    
    线程锁放置的地方需要使用正确
'''
def test1():
    global num
    lock.acquire()  # 上锁
    for i in range(1000000):
        num += 1
    lock.release() # 释放锁
    print('test1 num: ',num)

def test2():
    global num
    lock.acquire()  # 上锁
    for i in range(1000000):
        num += 1
    lock.release()  # 释放锁
    print('test2 num: ', num)


if __name__ == '__main__':
    print('main start...')
    thread1 = Thread(target=test1)
    thread2 = Thread(target=test2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print('main end...')