# _*_ coding:utf-8 _*_
# @time  : 2020/7/8 08:34
# @Author: quanwen
# @File  :
import multiprocessing
import time

#进程执行的任务函数

'''
 申明线程池的大小，如果线程池还未满，就立即执行任务，
 如果线程池满了，就会等待线程池其中的一个任务完成后才能继续添加，以此类推
'''
def fun1(msg):
    print('start: ',msg)
    time.sleep(3)
    print('end: ',msg)

if __name__ == '__main__':
    # 创建容量为3的进程池
    pool = multiprocessing.Pool(3)

    # 添加任务
    for i in range(1,6):
        print('任务： ',i)
        msg = '任务%d'%i
        pool.apply_async(fun1,(msg,))
    # 如果进程池不再接收新的请求，调用close
    pool.close()
    # 等待子进程运行结束
    pool.join()