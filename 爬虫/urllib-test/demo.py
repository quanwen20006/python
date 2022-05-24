# _*_ coding:utf-8 _*_
# @time  : 2020/7/31 22:24
# @Author: quanwen
# @File  :

from urllib import request,parse

response = request.urlopen('http://www.baidu.com')
print('get: ',response.read().decode('utf8'))

data = bytes(parse.urlencode({'word':'hello'}),encoding='utf8')
response = request.urlopen('http://httpbin.org/post',data=data)
print('post: ',response.read())
