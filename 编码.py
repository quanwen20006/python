# _*_ coding:utf-8 _*_
# @time  : 2020/7/22 08:01
# @Author: quanwen
# @File  :
'''
    py3的数据类型

    str：unicode
    bytes：十六进制

    str   ---> bytes 编码,也可以使用encode进行编码
    bytes --->   str 解码,也可以使用decode进行解码
'''


s = 'Hello 你好'
print(type(s)) # <class 'str'>

b = bytes(s,'utf8')
print(b) # b'Hello \xe4\xbd\xa0\xe5\xa5\xbd'

t = b'Hello \xe4\xbd\xa0\xe5\xa5\xbd'
print(str(t,'utf8'))
