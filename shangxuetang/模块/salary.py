# _*_ coding:utf-8 _*_
# @time  : 2021/1/25 17:16
# @Author: quanwen
# @File  :

'''
计算工资模块
'''
Company = '测试'
def YearSalary(salary):
    '''
    计算年工资 salary*12
    :param salary:
    :return:
    '''
    return salary*12

def DaySalary(salary):
    '''
    日薪是按一个月22.5天计算的 salary/22.5
    :param salary:
    :return:
    '''
    return salary/22.5