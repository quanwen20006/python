# _*_ coding:utf-8 _*_
# @time  : 2020/7/15 08:10
# @Author: quanwen
# @File  :
'''
 生产者就是生产数据的线程，消费者就是消费数据的线程，在多线程开发中

 如果生产者处理速度很快，而消费者很慢，那么生产者就必须等待消费者处理完，才能继续生产数据

 同理，如果消费者的处理能力大于生产者，那么消费者必须等待生产者

 原理：生产者的数据放到队列，消费者从队列去取数据

'''

from threading import Thread
from queue import Queue
import time

class Prodcter(Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # 判断队列大小
            if queue.qsize()<1000:
                for i in range(100):
                    count += 1
                    msg = '生产第%d个产品'%count
                    queue.put(msg)
                    print(msg)
                time.sleep(0.5)

class Customer(Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # 判断队列大小
            if queue.qsize() > 100:
                for i in range(10):
                    count += 1
                    msg = self.name + ' 消费 ' + queue.get()
                    print(msg)
                time.sleep(1)


if __name__ == '__main__':
    queue = Queue()
    p = Prodcter()
    c = Customer()

    p.start()
    time.sleep(1)
    c.start()