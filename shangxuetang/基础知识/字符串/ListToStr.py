# -*- coding:utf-8 -*-

'''
把列表的内容以字符串形式返回，且一个元素前面加And
'''

def ListSortStr(inList):
    ListLen = len(inList)
    s=''
    if ListLen == 0:
        return 'The List is Empty'
    elif ListLen == 1:
        return str(inList[0])
    else:
        for i in range(ListLen-1):
            s = s + str(inList[i])+','
        s = s + ' And ' + str(inList[-1])
        return s


if __name__ == '__main__':
    fruit = ['Apple', 'Banan', 'Orange']
    result = ListSortStr(fruit)
    print(result)
    temp = 'I am a Enginer'
    print(len(temp))
    a={False:'1'}
    print(a)