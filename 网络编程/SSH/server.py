# _*_ coding:utf-8 _*_
# @time  : 2020/7/17 22:30
# @Author: quanwen
# @File  :

import socket
import subprocess

sk = socket.socket()
# 绑定ip和端口
sk.bind(('127.0.0.1',8003))

sk.listen(3)

# 等待客户端连接
coon,addr = sk.accept()
print('客户端连接成功: ',addr)
while True:
    try:
        # 如果客户端杀掉进程（不是exit），异常处理
        data = coon.recv(1024)
    except Exception:
        break
    if not data:
        coon.close()
        coon, addr = sk.accept()
        continue
    print('接收到的命令是：',str(data,'utf8'))
    # 执行命令，且把执行结果输出到标准管道
    obj = subprocess.Popen(str(data,'utf8'),shell=True,stdout=subprocess.PIPE)
    shell_result = obj.stdout.read()
    # inp = input('>>>: ')
    result_len = len(shell_result)
    print('------',result_len)
    coon.send(bytes(str(result_len),'utf8'))
    coon.recv(1024)
    coon.send(shell_result)

sk.close()
