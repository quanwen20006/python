# _*_ coding:utf-8 _*_
# @time  : 2021/1/23 22:08
# @Author: quanwen
# @File  :
import csv
'''
读取csv文件的内容，然后写入
'''
result = []
with open('./购鞋清单.csv','r',encoding='utf-8') as f:
    a_csv = csv.reader(f)
    # print(a_csv)

    for row in a_csv:
        result.append(row)
        print(row)

with open('./购鞋清单1.csv','w',encoding='utf-8') as f:
    b_csv = csv.writer(f)
    for row in result:
        b_csv.writerow(row)