# _*_ coding:utf-8 _*_
# @time  : 2020/7/6 09:00
# @Author: quanwen
# @File  :

from multiprocessing import Process
import time

'''
使用继承的方式创建进程，需要重写run方法
'''

class ClockProcess(Process):
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print('子进程开始执行的时间:{}'.format(time.ctime()))
        time.sleep(self.interval)
        print('子进程结束的时间:{}'.format(time.ctime()))

if __name__ == '__main__':
    print('主进程开始执行')
    cp = ClockProcess(1)
    cp.start()
    cp.join()
    print('主进程执行结束')
