# _*_coding:utf-8 _*_
'''
银行卡类：
	私有属性：
		卡号、密码、余额，年化利率
	公开方法：
		设置密码：需要输入旧密码，才能设置新密码
		查看余额：需要输入密码
		提款：需要输入密码
		存钱：需要输入密码
		计算年利息

	用例：
		创建银行卡对象，设置卡号，密码，初始余额，年化利率
		存一笔钱
		取一笔钱
		打印余额
'''


class BankCard(object):
    def __init__(self, card, password, balance, rate):
        self.__card = card
        self.__password = password
        self.__balance = balance
        self.__rate = rate

    # 密码修改
    def changePassword(self, oldPassWord, newPassWord):
        if oldPassWord == self.__password:
            self.__password = newPassWord
            print("密码修改成功")
        else:
            print("请输入正确的密码，再进行密码修改，谢谢")

    # 存钱
    def depositMoney(self, card, password, money):
        if(card == self.__card and password == self.__password):
            self.__balance == money
        else:
            print("卡号信息不对，不能存钱")
        # 取钱

    def withdrawMoney(self, card, password, money):
        if(card == self.__card and password == self.__password):
            if(self.__balance >= money):
                self.__balance -= money
                return money
            else:
                print("余额不足")
        else:
            print("卡号信息不对")
    # 打印个人信息

    def getInfo(self):
        print("个人信息：卡号：%s 余额：%d 密码：%s" %
              (self.__card, self.__balance, self.__password))


bc = BankCard("123456", "123123", 10000, 0.8)
bc.getInfo()
bc.changePassword("123123", "123490")
bc.getInfo()
bc.withdrawMoney("123456", "123490", 4000)
bc.withdrawMoney("123456", "123490", 8000)
bc.getInfo()
