#!/usr/bin/python
# -*-coding:utf-8-*-
import re, time
'''
读取login_config的配置，然后获取version，然后去修改version.txt里面的版本号
'''


def getVersion(filename, *args):
    verList = []
    f = ''
    index = 0
    try:
        f = open(filename, 'r')
        for line in f.readlines():
            print("%s line---%s len" %(line,len(args)))
            for arg in args:
                print(11111111)
                if line.startswith(arg):
                    print("ver===== ", line.split["="][1])
                    #versioncode = re.findall('\d+\.\d+\.\d+', line)
                    #verList.append(versioncode[0])
                    # 每一行都开头的字符串都只能是用户输入的某一种情况，所以最多只需要执行一次
                    index += 1
                    break
                # 如果所有的版本号都已经拿到，文件的后面部分就不需要再处理
                if index == len(args):
                    return verList
    except FileNotFoundError:
        print("文件不存在")
    finally:
        f.close()
        return verList


# def updateVersionCode(filename, newVersion):
#     f = ''
#     try:
#         f = open(filename, 'r+', encoding='utf8')
#         f.write(newVersion)
#     except FileNotFoundError:
#         print("文件不存在")
#     finally:
#         f.close()


login_config = r'/home/rungame/config.php'
version_config = r'D:\111\version.txt'
#获取版本号
versionList = getVersion(login_config, '$GameClientVer')

for version in versionList:
    print('version code is %s ' % version)

#修改版本号
#updateVersionCode(version_config, versionList[0])


