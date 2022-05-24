# _*_ coding:utf-8 _*_
# @time  : 2021/1/23 21:30
# @Author: quanwen
# @File  :
'''
文件的seek使用--操作的是字节,在utf8编码中一个汉字3个字节，中gbk编码中一个汉字2个字节

tell() 返回当前指针的位置
seek(offset [,whence])
    offset 偏移量
    whence不同的值代表不同含义
    0 从文件开头计算（默认值）
    1 从当前文件开始计算
    2 从文件末尾开始计算
'''

with open ('./Hotel California.txt',encoding='utf-8') as f:
    print('文件名是： ',f.name)
    print('当前指针是： ',f.tell())
    print('当前读取内容是：',f.readline())
    print('当前指针是： ', f.tell())
    f.seek(7,0) # 从头开始读取，从第三个字节开始
    print('当前读取内容是：', f.readline())

