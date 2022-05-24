# _*_ coding:utf-8 _*_
# @time  : 2021/1/10 11:21
# @Author: quanwen
# @File  :

'''
字典：key-value对，无序
     字典的定义五种方式
        dict = {'key':value,'key':value}
        dict = dict(key=value,key=value)
        dict = dict([(key,value),(key,value)])
        k = [key1,key2,key3]
        v = [value1,value2,value3]
        dict = dict(zip(k,v))
        a = dict.fromkey([key1,key2,key3]) # 创建的字典值均为空

    # 删除元素
    del(dict[key])
    pop(dict[key])
    # 清除所有内容
    clear(dict)

    # 随机清除一项-因为本身无序，所以pop的时候就会随机删除一个
    dict.popitem()

'''
my_dict = {"name": "python", "age": 28, "fans": 1.23e9}
# print("keys: ", my_dict.keys)
my_dict['salary'] = 39000
# 循环字典
for key, value in my_dict.items():
    print("key: %s value %s" % (key, value))
my_dict.update({"key1": "value1", "key2": "value2"})


print("字典：", my_dict.pop('age'))
print("字典：", my_dict)