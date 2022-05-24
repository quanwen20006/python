# _*_coding:utf-8 _*_
'''
股票类：
	私有属性：
		代码，名称，昨日收盘价，当前价格
	提供私有属性获取方法getXXX()
	提供私有属性设置方法setXXX()
	公开方法：获取当前价格比昨日收盘价的涨跌幅
'''


class Stock(object):
    __code = None
    __name = None
    __close = None
    __price = None

    def __init__(self, code, name, close, price):
        self.__code = code
        self.__name = name
        self.__close = close
        self.__price = price

    def getPrice(self):
        print(self.__price)
        self.__price

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getClose(self):
        return self.__close

    # 获取涨跌幅
    def getRise(self):
        rise = (self.__price - self.__close)*100/self.__close
        return rise


s = Stock("002230", "科大讯飞", 57.18, 58)
print("%s的涨跌幅是：%.4f" % (s.getName(), s.getRise()))
s1 = Stock("002231", "阿里巴巴", 57.18, 59)
print("%s的涨跌幅是：%.4f" % (s1.getName(), s1.getRise()))
