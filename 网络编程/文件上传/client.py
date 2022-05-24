# _*_ coding:utf-8 _*_
# @time  : 2020/7/17 22:30
# @Author: quanwen
# @File  :
import socket
import os
'''
粘包解决，需要第一次传递文件大小等信息给接收端

使用方法：
post|1.png
'''

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print('BASE_DIR: ',BASE_DIR)
sk = socket.socket()
sk.connect(('127.0.0.1',8001))
while True:
    inp = input('>>> ')
    # 如果用户输入的是exit，就退出
    if inp.lower() == 'exit':
        break
    cmd, path = inp.split('|')
    path = os.path.join(BASE_DIR,path)
    filename = os.path.basename((path))
    size = os.stat(path).st_size
    file_info = 'post|%s|%s' % (filename,size)
    sk.send(bytes(file_info, 'utf8'))

    #打开文件并发送数据
    has_sent = 0
    with open(path,'rb') as f:
        while has_sent != size:
            data = f.read(1024)
            sk.sendall(data)
            has_sent += len(data)
sk.close()