# _*_ coding:utf-8 _*_
# @time  : 2020/7/6 08:31
# @Author: quanwen
# @File  :
from multiprocessing import Process
from time import  sleep
'''
创建子进程----传递参数----运行
'''
def run_test(name,age,**kwargs):
    for i in range(2):
        print('子进程运行中，参数name: %s,age: %d' %(name,age))
        print('字典参数 kwargs: ',kwargs)
        sleep(0.5)

def worker(interval):
    print('work start')
    sleep(interval)
    print('work end')

if __name__ == '__main__':
    print('主进程正在执行')
    # 创建子进程--target接收执行的任务
    p=Process(target = run_test,args=('jones',18),kwargs={'m':33})
    # 调用子进程 p.start() 或者 p.run()
    p.start()

    p1 = Process(target=worker, args=(3,),name='worker')
    p1.start()
    p1.join() # 主进程等待调用join的子进程结束（可以传递参数，意义是等待子进程多久，时间为秒）
    print('主进程执行完毕',p1.name,p1.pid,' 进程是否运行： ',p1.is_alive())