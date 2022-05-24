# -*-coding:utf-8 -*-
import socket


def getRemoteMachineInfo():
    remoteHost = 'www.sina.com.cn'
    try:
        print('IP Address: %s, HostName: %s' % (socket.gethostbyname(remoteHost), socket.gethostname()))
    except socket.error:
        print('%s: ' % remoteHost)


def findServerName():
    protocolName = 'tcp'
    for port in [80, 25, 53]:
        print('port: %s ==> service name: %s' % (port, socket.getservbyport(port, protocolName)))



if __name__ == '__main__':
    getRemoteMachineInfo()
    findServerName()
