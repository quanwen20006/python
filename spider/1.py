import re

a = '1.2万'
b = re.findall('\d*', a)
c = float(b[0])

print(a, c)
