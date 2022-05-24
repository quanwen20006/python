# _*_ coding:utf-8 _*_
# @time  : 2020/7/9 12:48
# @Author: quanwen
# @File  :
import threading
import time


def fun1(delay):
    print('线程 {} 开始运行' .format(threading.current_thread().getName()) )
    time.sleep(delay)
    print('线程 {} 结束运行' .format(threading.current_thread().getName()))

def fun2(delay):
    print('线程 %s 开始运行' % threading.current_thread().getName())
    time.sleep(delay)
    print('线程 %s 结束运行' % threading.current_thread().getName())

class Mythread(threading.Thread):
    # 重写构造方法
    def __init__(self,func,name,args):
        super().__init__(target=func,name=name,args=args)

    def run(self):
        self._target(*self._args)

if __name__ == '__main__':
    print('开始运行')
    t1 = Mythread(fun1,'thread1-1',(2,))
    t2 = Mythread(fun2, 'thread2-1', (4,))
    t1.start()

    t2.start()
    t1.join()
    t2.join()
    print('结束运行')
