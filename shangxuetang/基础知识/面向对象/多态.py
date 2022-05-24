# _*_coding:utf-8 _*_
'''
多态的使用

为帝国创建一支军队，包含骑兵，弓箭手，法师
所有兵种都能够进行进攻和防守，但形态各异
通过输入将令，控制各个兵种但攻守细节
'''


class Soldier(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def attack(self):
        print("士兵攻击")

    def defend(self):
        print("士兵防守")


class Cavalry(Soldier):
    def __init__(self, name, age, hourse):
        super().__init__(name, age)
        self.hourse = hourse

    def attack(self):
        print("骑兵攻击")

    def defend(self):
        print("骑兵防守")


class Master(Soldier):
    def __init__(self, name, age, staff):
        super().__init__(name, age)
        self.staff = staff

    def attack(self):
        print("法师攻击")

    def defend(self):
        print("法师防守")


class Archer(Soldier):
    def __init__(self, name, age, arch):
        super().__init__(name, age)
        self.arch = arch

    def attack(self):
        print("弓箭手攻击")

    def defend(self):
        print("弓箭手防守")


soldier = Archer("solod1", 20, "ttt")
print("士兵的类型是：", type(soldier))
soldier.attack()
