# 1：函数赋值给变量
def ask(name="jones"):
    print(name)
    return 1


my_func = ask
my_func("函数赋值给变量： jack")


# 2：类赋值给变量
class Person(object):
    def __init__(self):
        print("Person jack jones")
    #
    def __str__(self):
        return "Person"


p = Person
p()
print("--------------")
# 3：可以添加到集合对象中
obj_list =[]
obj_list.append(Person)
obj_list.append(ask)
for i in obj_list:
    print("对象添加到集合： ",i())


# 4：函数可以当作返回值
def decorator_func():
    print("decorator_func start")
    return ask


my_func1 = decorator_func()
my_func1("Hello World!")


'''
    1：函数和类可以赋值给变量
    2：添加到集合中
    3：可以作为传递参数
    4：可以当做函数的返回值
'''
def ask(name='jack'):
    print('jack')


class Person(object):
    def __init__(self):
        print('person')

# 函数当返回值
def decoratror_func():
    print('dec start...')
    return ask

obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for item in obj_list:
    item()

my_func = ask
my_func('jones')
my_func1 = Person
my_func1()

my_func2 = decoratror_func()
my_func2('Tom')

a="123"
print('实例所属类：', type(a))
print('实例所属类由 %s ：创建 '% type(str))
print('实例所属类：',type(type))
print(my_func1.__bases__)
print(object.__bases__)
print('type由%s ：',type.__bases__)