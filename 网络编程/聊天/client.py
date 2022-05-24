# _*_ coding:utf-8 _*_
# @time  : 2020/7/17 22:30
# @Author: quanwen
# @File  :
import socket
'''
粘包解决，需要第一次传递文件大小等信息给接收端
'''

sk = socket.socket()
sk.connect(('127.0.0.1',8003))
while True:
    inp = input('>>> ')
    # 如果用户输入的是exit，就退出
    if inp.lower() == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    # 循环接收 --设置空btyes,累计读取，判断是否读取完
    result_len = int(str(sk.recv(1024),'utf8'))
    data = bytes()
    sk.send(bytes('ok','utf8'))
    while len(data) != result_len:
        temp = sk.recv(1024)
        data += temp
    print('接收消息: ',str(data,'utf8'))

sk.close()