# _*_ coding:utf-8 _*_
# @time  : 2020/7/6 08:25
# @Author: quanwen
# @File  :

from time import  sleep
'''
非并发，做多件事情的时候就是顺序的
'''
def sing():
    for i in range(3):
        print('正在唱歌...%d' %i)
        dance()
        sleep(1)

def dance():
    for i in range(3):
        print('正在跳舞...%d' %i)
        sleep(1)

if __name__ == '__main__':
    sing()
    # dance()