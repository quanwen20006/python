# _*_ coding:utf-8 _*_
# @time  : 2021/1/25 14:55
# @Author: quanwen
# @File  :
'''
    通过traceback获取堆栈信息，并且写入文件
'''
import traceback

try:
    print('step1')
    num = 1/0
except:
    with open('./error.txt','a',encoding='utf-8') as f:
        traceback.print_exc(file=f)

a = [1,2,3,4]
print(a[6])