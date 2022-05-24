#
'''
    迭代器是什么：python中的迭代器是访问可迭代对象的工具。迭代器可以看作是一个特殊的对象
               每次调用该对象时都会返回自身的下一个元素
    自定义迭代器，必须实现__iter__和__next__函数
    1: 迭代器，1次 使用完，如果需要多次使用，需要多次实例化
'''

class BookCollection(object):
    def __init__(self):
        self.cur = 0
        self.data = ['往事', '回味', '数学之美']

    def __iter__(self):
        return self

    def __next__(self):
        print("当前下标是：{}  数据的长度是：{}".format(self.cur,len(self.data)))
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r


bkc = BookCollection()
print("bks数据类型： ", type(bkc))
for book in bkc:
   print(book)

print(next(bkc))
print(next(bkc))
print(next(bkc))
