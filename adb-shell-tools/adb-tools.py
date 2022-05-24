# -*- coding:utf-8 -*-

'''
    author:wen.quan@pheiot.com
'''
import subprocess
import time, os



class Device(object):
    SN = ''

    def __init__(self, packagename):
        self.SN = packagename

    @staticmethod
    def getDevice():
        flag = False
        order = 'adb devices'  # get connect devices
        pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
        #pi.wait()
        time.sleep(3)
        lines = pi.stdout.readlines()
        if len(lines) > 2:
            flag = True

        if os.name == 'nt':
            os.system('taskkill /F /IM grep.exe')
        else:
            os.kill(os.getpgid(pi.pid), 9)
        return flag

    def excuteCommond(self, num, filename='log1.txt'):
        try:
            commond = 'adb shell top -d 1 |grep ' + self.SN + ' >> ' + filename
            # print(commond)
            pi = subprocess.Popen(commond, shell=True, stdout=subprocess.PIPE)
            #pi.wait()
            time.sleep(num)
            if os.name == 'nt':
                os.system('taskkill /F /IM grep.exe')
            else:
                os.kill(os.getpgid(pi.pid), 9)
        except:
            print('执行异常')


packageName = 'com.dozengame.m+'
d = Device(packageName)
if Device.getDevice():
    print("devices connect")
    d.excuteCommond(15)
else:
    print("no devices connect")
