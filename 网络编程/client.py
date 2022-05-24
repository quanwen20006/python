# _*_ coding:utf-8 _*_
# @time  : 2020/7/17 08:31
# @Author: quanwen
# @File  :

import socket
s_client = socket.socket()
s_client.connect(('127.0.0.1',8000))
print('s--- ')
# client 接收数据 recv() 会阻塞
data = s_client.recv(1024)
print('data: ',str(data,'utf-8'))