# _*_ coding:utf-8 _*_
# @time  : 2020/7/17 22:30
# @Author: quanwen
# @File  :

import socket
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sk = socket.socket()
# 绑定ip和端口
sk.bind(('127.0.0.1',8001))

sk.listen(3)

# 等待客户端连接
coon,addr = sk.accept()
print('客户端连接成功: ',addr)
while True:
    try:
        # 如果客户端杀掉进程（不是exit），异常处理
        data = coon.recv(1024)
        print(str(data,'utf8'))

        cmd,filename,size = str(data,'utf8').split('|')
        path = os.path.join(BASE_DIR,'yuan',filename)
        size = int(size)

        has_revice = 0
        with open(path,'ab') as f:
            while has_revice != size:
                data = coon.recv(1024)
                f.write(data)
                has_revice += len(data)
    except Exception:
        break
    if not data:
        coon.close()
        coon, addr = sk.accept()
        continue
    # print('接收消息：',str(data,'utf8'))

    inp = input('>>>: ')
    coon.send((bytes(inp,'utf8')))

sk.close()
