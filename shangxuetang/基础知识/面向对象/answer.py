# _*_coding:utf-8 _*_
class Fan(object):
    SLOW = 0
    MDEIUM = 1
    FAST = 2

    def __init__(self, speed=SLOW, on=False, radius=5.0, color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed
        return self.__speed


if __name__ == "__main__":
    fan = Fan(10, True, 6.0, 'red')
    s = fan.getSpeed()
    print("速度是：", s)
    s = fan.setSpeed(20)
    print("速度是：", s)
