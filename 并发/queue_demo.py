# _*_ coding:utf-8 _*_
# @time  : 2020/7/8 09:04
# @Author: quanwen
# @File  :

# queue 单向队列，先进先出
"""
1. 注意是包的导入,  import queue
2. q = queue.Queue(2), 初始化可以指定队列的大小
3. empty(), 判空
4. full(), 是否满了
5. put(), 添加一个元素
6. get(), 获取一个元素
7. qsize(),获取元素的个数
"""

from multiprocessing import Queue
# 创建队列
q = Queue(3) #指定队列的大小，默认队列是无限
# 向队列中插入元素
q.put('消息1')
q.put('消息2')
q.put('消息3')

# put添加可选参数,如果队列满，且等待时间超过1秒，就抛异常 raise Full
# 判断当前队列是否已满
print('判断当前队列是否已满: ',q.full())
if not q.full():
    q.put('消息4', block=True, timeout=1)
else:
    print('队列已满不添加元素')

# 读取并删除元素-get
# print(q.get())
# print(q.get())
# print(q.get())
# 判断队列是否为空
# if not q.empty():
#     print(q.get(block=True, timeout=1))

# 查看队列的大小--获取队列的大小在macos上无法运行
print('队列的大小： ', q.qsize())

