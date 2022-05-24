# _*_ coding:utf-8 _*_
# @time  : 2020/8/20 15:48
# @Author: quanwen
# @File  :

# demo =['banan','Apple','apple','Banan','word','hello']
# print(ord('A'))
# print(ord('B'))
sortList = ['A','B','C','a','b','c','d','h','w']
demo = input().split(',')
tempSort = []
# demo.sort()
for item in demo:
    temp = item[0]
    print('temp: ',temp)
    # print( )
    tempSort.append(sortList.index(temp))
    temp = 0
    print(tempSort)
for i in range(len(tempSort)):
    for j in range(len(tempSort)-1):
        if tempSort[j] < tempSort[j+1]:
            temp = tempSort[j]
            tempSort[j] = tempSort[j+1]
            tempSort[j+1] = temp

# t = [1,3,2,4,7]
# temp = 0
# for i in range(len(t)):
#     print('i: ',i)
#     for j in range(len(t)-1):
#         print('j: ', j)
#         # print('t[i]: ',t[i],'t[i+1] ',t[i+1])
#         if t[j] < t[j+1]:
#             temp = t[j]
#             t[j] = t[j+1]
#             t[j+1] = temp
#
# print(t)
