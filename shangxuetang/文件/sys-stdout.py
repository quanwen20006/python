# _*_ coding:utf-8 _*_
# @time  : 2022/6/28 18:14
# @Author: quanwen
# @File  :

import sys
# 保存原始sys.stdout进行备份
save_stdout = sys.stdout
# sys.stdout重定向，指向文件对象
sys.stdout = open("test1111.txt", "w")
# print调用sys.stdout的write方法（此时sys.stdout指向文件对象，实际上调用的就是文件对象的write方法），打印到test.txt文件
print("hello world")
# 恢复，标准输出流
sys.stdout = save_stdout
# print调用sys.stdout的write方法，标准输出流默认打印到控制台
print("hello world again")