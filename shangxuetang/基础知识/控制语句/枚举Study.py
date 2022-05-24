from enum import Enum
from enum import IntEnum, unique

'''
    python枚举使用,枚举使用，或枚举遍历
    IntEnum 要求枚举类型的值，必须为整形
    unique 要求枚举类型的值必须唯一，用法如下
    @unique
    class A(Enum):
        YELLOW = 1
        GREEN = 1 # 会报错
'''


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print('类型:', VIP.GREEN.name, ' 值:', VIP.GREEN.value)
for v in VIP.__members__.items():
    print(v[0], v[1].value)
    #print('属性: ', v._name_, ' 值：', v._value_)


# 数据存了一个a 值为1，怎么查对应的是什么类型
a = 4
print('a的类型是：', VIP(a).name)

