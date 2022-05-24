import json

'''
json反序列化，序列化
'''
json_str = '{"name":"jack", "age":21}'
json_str1 = '[{"name":"jack", "age":21},{"name":"jones", "age":22}]'
per = json.loads(json_str)
per1 = json.loads(json_str1)

print('type: ', type(per), per)
print('type: ', type(per1), per1)
