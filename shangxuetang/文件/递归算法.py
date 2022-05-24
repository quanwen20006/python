# _*_ coding:utf-8 _*_
# @time  : 2021/1/23 23:57
# @Author: quanwen
# @File  :

'''
递归计算阶乘
阶乘：1*2*3*4*5*...*n
'''
import os
def jiechen(n):
    if n == 1:
        return 1
    else:
        return n*jiechen(n-1)
allFiles = []
def getAllFiles(path,level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filePath = os.path.join(path,file)
        if os.path.isdir(filePath):
            getAllFiles(filePath,level+1)
        allFiles.append('\t'*level+filePath)

if __name__ == '__main__':
    print(jiechen(3))
    getAllFiles('./temp',0)
    for f in allFiles:
        print(f)