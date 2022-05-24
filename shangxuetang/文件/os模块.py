# _*_ coding:utf-8 _*_
# @time  : 2021/1/23 22:21
# @Author: quanwen
# @File  :
'''
    os
        1：调用Windows操作系统文件和命令
        2：文件和目录操作
'''
import os
os.system('ping -c 6 www.baidu.com ')
# 调用可执行程序
# os.startfile('')
print('操作系统是：{0} 换行符是：{1}'.format(os.name,os.sep))
# repr函数的作用是返回一个对象的 string 格式
print('当前操作系统的换行符是： ',repr(os.linesep))
print('当前文件属性是：{0} '.format(os.stat('./stu.dat')))
print('当前目录是：{0}'.format(os.getcwd()))
# 改变工作目录  os.chdir('路径')
# os.mkdir('temp')
# 删除非空目录
# os.rmdir('./temp')

dirs = os.listdir('./temp') # 返回当前目的子目录和文件（但是不递归子目录）
print('dir: ',dirs)

