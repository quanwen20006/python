# _*_coding:utf-8 _*_

'''
回答是否有钱，是否帅炸
如果有钱且帅炸，凤姐就从了你
如果有钱或帅咋，我们还是做朋友好了
如果没钱还丑，有多远滚多远
'''


def check():
    money = input("请输入是否有钱：（Y/N）")
    handsome = input("请输入是否帅气：（Y/N）")
    hasmoney = True if(money == 'Y') else False
    hashandsome = True if(handsome == 'Y') else False

    if(hasmoney and hashandsome):
        print("从了你")
    elif (hasmoney or hashandsome):
        print("做朋友")
    else:
        print("bye")

if __name__ == '__main__':
    check()
