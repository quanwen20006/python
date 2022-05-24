# 1：函数赋值给变量
def ask(name="jones"):
    print(name)
    return 1


my_func = ask
# my_func("jack")


# 2：类赋值给变量
class Person(object):
    def __init__(self):
        print("jack jones")
    #
    # def __str__(self):
    #     return "Person"


p = Person
# p()

# 3：可以添加到集合对象中
obj_list =[]
obj_list.append(Person)
obj_list.append(ask)
for i in obj_list:
    print(i())


# 4：函数可以当作返回值
def decorator_func():
    print("decorator_func start")
    return ask


my_func1 = decorator_func()
my_func1("Hello World!")