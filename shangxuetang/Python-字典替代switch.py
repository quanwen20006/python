'''
    字典隐射，替代switch
    分别说明几种情况
    1：字典无逻辑，使用字典.get方式去访问从而达到替代字典
        如：dict.get(day,default)
    2：字典有逻辑
        如下文
'''

day = 5


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'Unkown'


switcher = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}

day_name = switcher.get(day, get_default)()
print(day_name)
