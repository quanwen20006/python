# _*_ coding:utf-8 _*_
# @time  : 2020/7/15 08:45
# @Author: quanwen
# @File  :

import threading
# 创建threadlocal对象
local = threading.local()
def process_student():
    student_name = local.name
    print('线程名: %s 学生名 %s' %( threading.current_thread().getName(),student_name))


def process_teacher(name):
    # 将传入的name值绑定到local到name上
    local.name = name
    process_student()

if __name__ == '__main__':
    t = threading.Thread(target=process_teacher,args=('jack',),name='thread1')
    t1 = threading.Thread(target=process_teacher,args=('jones',),name='thread2')
    t.start()
    t1.start()