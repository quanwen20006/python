# _*_ coding:utf-8 _*_
# @time  : 2020/7/9 08:24
# @Author: quanwen
# @File  :
'''
Queue实现进程间通信
'''
from multiprocessing import Process,Queue,Pool
from time import sleep

#定义写入的方法
def write(q):
    a =['x','b','c','d']
    for i in a:
        print(('开始写入的值: %s') % i)
        q.put(i)
        sleep(1)

def reader(q):
    for i in range(q.qsize()):
        print('读取到的值: %s' % q.get())
        sleep(1)


if __name__ == '__main__':
    # 创建队列
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=reader, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()

    '''
    线程池创建的线程，使用Manager里面的Queue，而不是调用multiprocessing里面的Queue
    '''
    from multiprocessing import Manager
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply_async(write,(q,))
    pool.apply_async(reader, (q,))
    pool.close()
    pool.join()
