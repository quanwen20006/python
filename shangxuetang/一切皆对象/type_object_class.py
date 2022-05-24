'''
python一切介对象

'''


class Animal(object):
    def __init__(self):
        print("Animal")


class Dog(Animal):
    def __init__(self):
        print("Dog")

# type是一个类，同时也是实例
# type类生成--->Dog类实例--->dog实例

# object类是最顶层基类
dog = Dog()
# 实例对象
print("dog的类型是%s dog的父类是%s 根类是%s type类的基类是%s" % (type(dog), Dog.__bases__, Animal.__bases__, type.__bases__))


print("object的父类是：", object.__bases__)

# 模版对象
print("dog的类型是%s Dog类型是%s object类型是%s type的类型是%s" % (type(dog), type(Dog), type(object), type(type)))

