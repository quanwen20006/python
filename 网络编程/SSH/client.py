# _*_ coding:utf-8 _*_
# @time  : 2020/7/17 22:30
# @Author: quanwen
# @File  :
import socket
'''
模拟ssh
'''
sk = socket.socket()
sk.connect(('127.0.0.1',8003))
while True:
    inp = input('请输入要执行的命令： ')
    # 如果用户输入的是exit，就退出
    if inp.lower() == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))

    data = sk.recv(1024)
    print('接收消息: ',str(data,'utf8'))

sk.close()