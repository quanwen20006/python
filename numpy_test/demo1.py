# _*_ coding:utf-8 _*_
# @time  : 2020/7/5 17:26
# @Author: quanwen
# @File  :
import math

import numpy as np
# 使用arange创建数组
aArray = np.arange(10)
print('aArray: ',aArray,type(aArray))

# 创建array创建一维数组 dtyle指定数据对类型，ndmin代表是数据对维度（1维，2维，3维）
bArray = np.array([1,2,3,5,9,11],dtype=float)
print('bArray: ',bArray,type(bArray))

# 创建array创建二维数组
cArray = np.array([[1,2,4],[3,5,9],[11,33,22]],dtype=float)
print('cArray: ',cArray,type(cArray))

#对ndarray对象进行向量处理
print(np.sqrt(aArray))


# range 1-10（不包括10），步长是3
aRange = list(range(1,10,3))
print('aRange: ',aRange)

# arange创建数组 1-10 step为2 dtype=float
bRange = np.arange(1,11,2,dtype=float)
print('bRange: ',bRange)

# 随机数创建

import random
def randomTest():
    print(random.randint(1,10))
    aRandom = np.random.randint(1,11)
    #  随机创建一个数组，数组的元素数是4个，值为0-1之间
    bRandom = np.random.random(size=4)
    print('bRandom: ',bRandom)

    # 创建二维数组  表示创建一个 每一维都是4个元素的二维数组
    cRandom = np.random.random(size=(3,4))
    print('cRandom: ',cRandom)

    # 创建二维数组  表示创建一个 最后一维是5个元素的，第二维是4个元素，第三维是3个元素的3维数组
    dRandom = np.random.random(size=(3,4,5))
    print('dRandom: ',dRandom)

randomTest()

def randomIntTest():
    # 生成0-5之间的随机整数 一维(4个元素，每个元素的值从0-5随机)
    aInt = np.random.randint(6, size=4)
    print('aInt: ',aInt)

    # 生成5-10之间的随机二维整数 每一维(3个元素，每个元素的值从5-11随机)，共有4组
    bInt = np.random.randint(5,11, size=(4,3))
    print('bInt: ', bInt)

    # 生成5-10之间的随机二维整数 每一维(3个元素，每个元素的值从5-11随机)，共有4组
    cInt = np.random.randint(5,11, size=(4,3,5))
    print('cInt: ', cInt)

randomIntTest()

def randnTest():
    # 创建标准的正态分布，期望为0，方差为1
    a = np.random.randn(4)
    print('a: ',a)

randnTest()

# 创建指定期望和方差的正态分布
def randomNoamalTest():
    a = np.random.normal(size=5)#默认的期望值loc是0，方差scale=1.0
    print('a: ',a)

    b = np.random.normal(loc=2.0,scale=2.0,size=(3,4))  # 默认的期望值loc是0，方差scale=1.0
    print('b: ', b)

randomNoamalTest()
