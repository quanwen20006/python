# _*_ coding:utf-8 _*_
# @time  : 2020/7/17 08:31
# @Author: quanwen
# @File  :
'''
    socket服务端

    bind()
    listen()
    accept()

    recv()
    send()
    sendall()
'''

import socket
# 创建socket对象
s = socket.socket()
address = ('127.0.0.1', 8000)
# 绑定ip地址和端口
s.bind(address)
# 监听--可容纳排队3人，意思为第四个请求会直接被拒绝，前三个就依次等待
s.listen(3)
print('s listen: ')
# 等待客户端连接
coon,addr = s.accept()
print('coon: ',coon,' addr: ',addr)
# server发送消息
# inp = input('>>>')
# coon.send(bytes(inp,'utf-8'))