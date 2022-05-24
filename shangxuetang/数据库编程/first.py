# _*_ coding:utf-8 _*_
# @time  : 2021/8/23 上午1:36
# @Author: quanwen
# @File  :
import sqlite3
'''
操作sqlite3
1: 导入包
2：创建连接
3：创建游标对象
4：编写创建表的sql语句
5：执行sql -- excute()
6：执行多条sql语句 --excutemany()--（效果比excute高）
6：关闭游标
7：关闭数据库连接
'''

con = sqlite3.connect('./sqlite3-db/demo.db')
print(con)
cur = con.cursor()

sql_crt_tab = '''create table t_person(pno INTEGER primary key autoincrement,
        pname VARCHAR not null,
        age INTEGER)'''

sql = '''
        insert into t_person(pname,age) values (?,?)
    '''

try:
    cur.execute(sql,('张三',23))
    cur.executemany(sql,[("李四",24),("王五",30),("力巴",66)])
    con.commit() # 提交事务
    print('新增数据成功---')
except Exception as e:
    print('添加数据失败,需要回滚')
    con.rollback()
finally:
    cur.close() # 关闭游标
    con.close() # 关闭数据库连接