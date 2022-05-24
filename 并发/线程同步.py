# _*_ coding:utf-8 _*_
# @time  : 2020/7/15 08:02
# @Author: quanwen
# @File  :
from threading import Thread,Lock
import time
'''
线程同步
'''

# 创建3把互斥锁
lock1 = Lock()
lock2 = Lock()
lock3 = Lock()

# 对lock2 lock3上锁
lock2.acquire()
lock3.acquire()

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('----task1---')
                time.sleep(1)
                # 释放lock2
                lock2.release()

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('----task2---')
                time.sleep(1)
                # 释放lock3
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('----task3---')
                time.sleep(1)
                # 释放lock1
                lock1.release()



if __name__ == '__main__':
    task1 = Task1()
    task2 = Task2()
    task3 = Task3()

    task2.start()
    task3.start()
    task1.start()