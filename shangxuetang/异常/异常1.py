# _*_ coding:utf-8 _*_
# @time  : 2021/1/25 11:13
# @Author: quanwen
# @File  :
'''
else excepct是选择逻辑，如果没有except就执行else
finally 是必须执行
'''

while True:
    try:
        inp = int(input('请输入数据：'))
        if inp < 88:
            print('数据小了')
        else:
            print('数据大了')
    except ValueError as e:
        print(e)
    else:
        if inp == 88:
            print('输入正确')
            break
    finally:
        print('执行完毕。。。')


