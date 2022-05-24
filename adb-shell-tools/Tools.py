# -*-coding:utf-8 -*-
'''
    读取文件工具
'''


def readFile(filename):
    resultDict = []
    f = ''
    memLen = 0
    try:
        f = open(filename)
        for line in f.readlines():
            # 过滤采集中不完整的数据
            tempLine = (line.rstrip('\n').strip(' ').split(' '))
            lineList = []
            for i in tempLine:
                if len(i) > 2:
                    lineList.append(i)
            resultDict.append(lineList)
    except FileNotFoundError:
        print('文件不存在')
    finally:
        if f:
            f.close()
    return resultDict


a = readFile('log.txt')
print(a[1])
print(a[-1])


# a = "5366 u0_a188     10  10 1.9G 241M 199M S 33.0   8.9   0:35.66 com.dozengame.m+"
# tempList = a.split(' ')
#
# for i in tempList:
#     if len(i)>2:
#         print(i)
