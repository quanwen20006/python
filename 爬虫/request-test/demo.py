# _*_ coding:utf-8 _*_
# @time  : 2020/7/31 22:54
# @Author: quanwen
# @File  :
import requests
from requests.exceptions import ConnectTimeout

# 直接get
response = requests.get('http://httpbin.org/get')

# 带参数带get
data = {
    'name':'jack jones',
    'age':22
}
response1 = requests.get('http://httpbin.org/get',params=data)


print(response.status_code)
print('response ',response.text)
print(response.cookies)

print('response1: ',response1.text)


# post 请求
response2 = requests.post('http://httpbin.org/post',params=data)
print('response2: ',response2.text)

# 会话维持 + 超时时间
s =requests.Session()
try:
    temp = s.get('http://httpbin.org/cookies/set/number/123456789',timeout=0.1)
    print('temp: ', temp.text)
except ConnectTimeout:
    print('连接超时')


response3 = s.get('http://httpbin.org/cookies')
print('response3: ',response3.text)


# 认证设置
from requests.auth import HTTPBasicAuth
r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user','123'))
print(r.status_code)